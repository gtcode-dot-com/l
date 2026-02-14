---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-14T20:06:52.421759+00:00'
exported_at: '2026-02-14T20:06:55.068826+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/mastering-amazon-bedrock-throttling-and-service-availability-a-comprehensive-guide
structured_data:
  about: []
  author: ''
  description: This post shows you how to implement robust error handling strategies
    that can help improve application reliability and user experience when using Amazon
    Bedrock. We'll dive deep into strategies for optimizing performances for the application
    with these errors. Whether this is for a fairly new application or matured AI
    application, in this post you will be able to find the practical guidelines to
    operate with on these errors.
  headline: 'Mastering Amazon Bedrock throttling and service availability: A comprehensive
    guide'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/mastering-amazon-bedrock-throttling-and-service-availability-a-comprehensive-guide
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Mastering Amazon Bedrock throttling and service availability: A comprehensive
  guide'
updated_at: '2026-02-14T20:06:52.421759+00:00'
url_hash: b2f3921c3f85ddc56e310028b0790d46f6f8266f
---

In production generative AI applications, we encounter a series of errors from time to time, and the most common ones are requests failing with
**429 ThrottlingException**
and
**503 ServiceUnavailableException**
errors. As a business application, these errors can happen due to multiple layers in the application architecture.

Most of the cases in these errors are retriable but this impacts user experience as the calls to the application get delayed. Delays in responding can disrupt a conversation’s natural flow, reduce user interest, and ultimately hinder the widespread adoption of AI-powered solutions in interactive AI applications.

One of the most common challenges is multiple users flowing on a single model for widespread applications at the same time. Mastering these errors means the difference between a resilient application and frustrated users.

This post shows you how to implement robust error handling strategies that can help improve application reliability and user experience when using
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
. We’ll dive deep into strategies for optimizing performances for the application with these errors. Whether this is for a fairly new application or matured AI application, in this post you will be able to find the practical guidelines to operate with on these errors.

## Prerequisites

* AWS account with Amazon Bedrock access
* Python 3.x and boto3 installed
* Basic understanding of AWS services
* **IAM Permissions**
  : Ensure you have the following minimum permissions:
  + `bedrock:InvokeModel`
    or
    `bedrock:InvokeModelWithResponseStream`
    for your specific models
  + `cloudwatch:PutMetricData`
    ,
    `cloudwatch:PutMetricAlarm`
    for monitoring
  + `sns:Publish`
    if using SNS notifications
  + Follow the principle of least privilege – grant only the permissions needed for your use case

Example IAM policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel"
      ],
      "Resource": "arn:aws:bedrock:us-east-1:123456789012:model/anthropic.claude-*"
    }
  ]
}
```

**Note:**
This walkthrough uses AWS services that may incur charges, including Amazon CloudWatch for monitoring and Amazon SNS for notifications. See AWS pricing pages for details.

## Quick Reference: 503 vs 429 Errors

The following table compares these two error types:

| Aspect | 503 ServiceUnavailable | 429 ThrottlingException |
| --- | --- | --- |
| Primary Cause | Temporary service capacity issues, server failures | Exceeded account quotas (RPM/TPM) |
| Quota Related | Not Quota Related | Directly quota-related |
| Resolution Time | Transient, refreshes faster | Requires waiting for quota refresh |
| Retry Strategy | Immediate retry with exponential backoff | Must sync with 60-second quota cycle |
| User Action | Wait and retry, consider alternatives | Optimize request patterns, increase quotas |

## Deep dive into 429 ThrottlingException

A 429 ThrottlingException means Amazon Bedrock is deliberately rejecting some of your requests to keep overall usage within the quotas you have configured or that are assigned by default. In practice, you will most often see three flavors of throttling: rate-based, token-based, and model-specific.

### 1. Rate-Based Throttling (RPM – Requests Per Minute)

**Error Message:**

```
ThrottlingException: Too many requests, please wait before trying again.
```

Or:

```
botocore.errorfactory.ThrottlingException: An error occurred (ThrottlingException) when calling the InvokeModel operation: Too many requests, please wait before trying again
```

**What this actually indicates**

Rate-based throttling is triggered when the total number of Bedrock requests per minute to a given model and Region crosses the RPM quota for your account. The key detail is that this limit is enforced across the callers, not just per individual application or microservice.

Imagine a shared queue at a coffee shop: it does not matter which team is standing in line; the barista can only serve a fixed number of drinks per minute. As soon as more people join the queue than the barista can handle, some customers are told to wait or come back later. That “come back later” message is your 429.

**Multi-application spike scenario**

Suppose you have three production applications, all calling the same Bedrock model in the same Region:

* App A normally peaks around 50 requests per minute.
* App B also peaks around 50 rpm.
* App C usually runs at about 50 rpm during its own peak.

Ops has requested a quota of 150 RPM for this model, which seems reasonable since 50 + 50 + 50 = 150 and historical dashboards show that each app stays around its expected peak.

However, in reality your traffic is not perfectly flat. Maybe during a flash sale or a marketing campaign, App A briefly spikes to 60 rpm while B and C stay at 50. The combined total for that minute becomes 160 rpm, which is above your 150 rpm quota, and some requests start failing with ThrottlingException.

You can also get into trouble when the three apps shift upward at the same time over longer periods. Imagine a new pattern where peak traffic looks like this:

* App A: 75 rpm
* App B: 50 rpm
* App C: 50 rpm

Your new true peak is 175 rpm even though the original quota was sized for 150. In this situation, you will see 429 errors regularly during those peak windows, even if average daily traffic still looks “fine.”

**Mitigation strategies**

For rate-based throttling, the mitigation has two sides: client behavior and quota management.

**On the client side:**

* Implement request rate limiting to cap how many calls per second or per minute each application can send. APIs, SDK wrappers, or sidecars like API gateways can enforce per-app budgets so one noisy client does not starve others.
* Use exponential backoff with jitter on 429 errors so that retries can become gradually less frequent and are de-synchronized across instances.
* Align retry windows with the quota refresh period: because RPM is enforced per 60-second window, retries that happen several seconds into the next minute are more likely to succeed.

**On the quota side:**

* Analyze CloudWatch metrics for each application to determine true peak RPM rather than relying on averages.
* Sum those peaks across the apps for the same model/Region, add a safety margin, and request an RPM increase through AWS Service Quotas if needed.

In the previous example, if App A peaks at 75 rpm and B and C peak at 50 rpm, you should plan for at least 175 rpm and realistically target something like 200 rpm to provide room for growth and unexpected bursts.

### 2. Token-Based Throttling (TPM – Tokens Per Minute)

**Error message:**

```
botocore.errorfactory.ThrottlingException: An error occurred (ThrottlingException) when calling the InvokeModel operation: Too many tokens, please wait before trying again.
```

#### Why token limits matter

Even if your request count is modest, a single large prompt or a model that produces long outputs can consume thousands of tokens at once. Token-based throttling occurs when the sum of input and output tokens processed per minute exceeds your account’s TPM quota for that model.

For example, an application that sends 10 requests per minute with 15,000 input tokens and 5,000 output tokens each is consuming roughly 200,000 tokens per minute, which may cross TPM thresholds far sooner than an application that sends 200 tiny prompts per minute.

#### What this looks like in practice

You may notice that your application runs smoothly under normal workloads, but suddenly starts failing when users paste large documents, upload long transcripts, or run bulk summarization jobs. These are symptoms that token throughput, not request frequency, is the bottleneck.

#### How to respond

To mitigate token-based throttling:

* Monitor token usage by tracking InputTokenCount and OutputTokenCount metrics and logs for your Bedrock invocations.
* Implement a token-aware rate limiter that maintains a sliding 60-second window of tokens consumed and only issues a new request if there is enough budget left.
* Break large tasks into smaller, sequential chunks so you spread token consumption over multiple minutes instead of exhausting the entire budget in one spike.
* Use streaming responses when appropriate; streaming often gives you more control over when to stop generation so you do not produce unnecessarily long outputs.

For consistently high-volume, token-intensive workloads, you should also evaluate requesting higher TPM quotas or using models with larger context windows and better throughput characteristics.

### 3. Model-Specific Throttling

**Error message:**

```
botocore.errorfactory.ThrottlingException: An error occurred (ThrottlingException) when calling the InvokeModel operation: Model anthropic.claude-haiku-4-5-20251001-v1:0 is currently overloaded. Please try again later.
```

#### What is happening behind the scenes

Model-specific throttling indicates that a particular model endpoint is experiencing heavy demand and is temporarily limiting additional traffic to keep latency and stability under control. In this case, your own quotas might not be the limiting factor; instead, the shared infrastructure for that model is temporarily saturated.

#### How to respond

One of the most effective approaches here is to design for graceful degradation rather than treating this as a hard failure.

* Implement model fallback: define a priority list of compatible models (for example, Sonnet → Haiku) and automatically route traffic to a secondary model if the primary is overloaded.
* Combine fallback with cross-Region inference so you can use the same model family in a nearby Region if one Region is temporarily constrained.
* Expose fallback behavior in your observability stack so you can know when your system is running in “degraded but functional” mode instead of silently masking problems.

## Implementing robust retry and rate limiting

Once you understand the types of throttling, the next step is to encode that knowledge into reusable client-side components.

### Exponential backoff with jitter

Here’s a robust retry implementation that uses exponential backoff with jitter. This pattern is essential for handling throttling gracefully:

```
import time
import random
from botocore.exceptions import ClientError

def bedrock_request_with_retry(bedrock_client, operation, **kwargs):
    """Secure retry implementation with sanitized logging."""
    max_retries = 5
    base_delay = 1
    max_delay = 60

    for attempt in range(max_retries):
        try:
            if operation == 'invoke_model':
                return bedrock_client.invoke_model(**kwargs)
            elif operation == 'converse':
                return bedrock_client.converse(**kwargs)
        except ClientError as e:
            # Security: Log error codes but not request/response bodies
            # which may contain sensitive customer data
            if e.response['Error']['Code'] == 'ThrottlingException':
                if attempt == max_retries - 1:
                    raise

                # Exponential backoff with jitter
                delay = min(base_delay * (2 ** attempt), max_delay)
                jitter = random.uniform(0, delay * 0.1)
                time.sleep(delay + jitter)
                continue
            else:
                raise
```

This pattern avoids hammering the service immediately after a throttling event and helps prevent many instances from retrying at the same exact moment.

### Token-Aware Rate Limiting

For token-based throttling, the following class maintains a sliding window of token usage and gives your caller a simple yes/no answer on whether it is safe to issue another request:

```
import time
from collections import deque

class TokenAwareRateLimiter:
    def __init__(self, tpm_limit):
        self.tpm_limit = tpm_limit
        self.token_usage = deque()

    def can_make_request(self, estimated_tokens):
        now = time.time()
        # Remove tokens older than 1 minute
        while self.token_usage and self.token_usage[0][0] < now - 60:
            self.token_usage.popleft()

        current_usage = sum(tokens for _, tokens in self.token_usage)
        return current_usage + estimated_tokens <= self.tpm_limit

    def record_usage(self, tokens_used):
        self.token_usage.append((time.time(), tokens_used))
```

In practice, you would estimate tokens before sending the request, call
`can_make_request`
, and only proceed when it returns True, then call
`record_usage`
after receiving the response.

## Understanding 503 ServiceUnavailableException

A 503 ServiceUnavailableException tells you that Amazon Bedrock is temporarily unable to process your request, often due to capacity pressure, networking issues, or exhausted connection pools. Unlike 429, this is not about your quota; it is about the health or availability of the underlying service at that moment.

### Connection Pool Exhaustion

**What it looks like:**

```
botocore.errorfactory.ServiceUnavailableException: An error occurred (ServiceUnavailableException) when calling the ConverseStream operation (reached max retries: 4): Too many connections, please wait before trying again.
```

In many real-world scenarios this error is caused not by Bedrock itself, but by how your client is configured:

* By default, the
  `boto3`
  HTTP connection pool size is relatively small (for example, 10 connections), which can be quickly exhausted by highly concurrent workloads.
* Creating a new client for every request instead of reusing a single client per process or container can multiply the number of open connections unnecessarily.

To help fix this, share a single Bedrock client instance and increase the connection pool size:

```
import boto3
from botocore.config import Config

# Security Best Practice: Never hardcode credentials
# boto3 automatically uses credentials from:
# 1. Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
# 2. IAM role (recommended for EC2, Lambda, ECS)
# 3. AWS credentials file (~/.aws/credentials)
# 4. IAM roles for service accounts (recommended for EKS)

# Configure larger connection pool for parallel execution
config = Config(
    max_pool_connections=50,  # Increase from default 10
    retries={'max_attempts': 3}
)
bedrock_client = boto3.client('bedrock-runtime', config=config)
```

This configuration allows more parallel requests through a single, well-tuned client instead of hitting client-side limits.

### Temporary Service Resource Issues

**What it looks like:**

```
botocore.errorfactory.ServiceUnavailableException: An error occurred (ServiceUnavailableException) when calling the InvokeModel operation: Service temporarily unavailable, please try again.
```

In this case, the Bedrock service is signaling a transient capacity or infrastructure issue, often affecting on-demand models during demand spikes. Here you should treat the error as a temporary outage and focus on retrying smartly and failing over gracefully:

* Use exponential backoff retries, similar to your 429 handling, but with parameters tuned for slower recovery.
* Consider using cross-Region inference or different service tiers to help get more predictable capacity envelopes for your most critical workloads.

## Advanced resilience strategies

When you operate mission-critical systems, simple retries are not enough; you also want to avoid making a bad situation worse.

### Circuit Breaker Pattern

The circuit breaker pattern helps prevent your application from continuously calling a service that is already failing. Instead, it quickly flips into an “open” state after repeated failures, blocking new requests for a cooling-off period.

* **CLOSED**
  (Normal): Requests flow normally.
* **OPEN**
  (Failing): After repeated failures, new requests are rejected immediately, helping reduce pressure on the service and conserve client resources.
* **HALF\_OPEN**
  (Testing): After a timeout, a small number of trial requests are allowed; if they succeed, the circuit closes again.

#### Why This Matters for Bedrock

When Bedrock returns 503 errors due to capacity issues, continuing to hammer the service with requests only makes things worse. The circuit breaker pattern helps:

* Reduce load on the struggling service, helping it recover faster
* Fail fast instead of wasting time on requests that will likely fail
* Provide automatic recovery by periodically testing if the service is healthy again
* Improve user experience by returning errors quickly rather than timing out

The following code implements this:

```
import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open" # Testing if service recovered

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")

        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except Exception as e:
            self.on_failure()
            raise

    def on_success(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED

    def on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()

        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

# Usage
circuit_breaker = CircuitBreaker()

def make_bedrock_request():
    return circuit_breaker.call(bedrock_client.invoke_model, **request_params)
```

### Cross-Region Failover Strategy with CRIS

Amazon Bedrock cross-Region inference (CRIS) helps add another layer of resilience by giving you a managed way to route traffic across Regions.

* **Global CRIS Profiles**
  : can send traffic to AWS commercial Regions, typically offering the best combination of throughput and cost (often around 10% savings).
* **Geographic CRIS Profiles**
  : CRIS profiles confine traffic to specific geographies (for example, US-only, EU-only, APAC-only) to help satisfy strict data residency or regulatory requirements.

For applications without data residency requirements, global CRIS offers enhanced performance, reliability, and cost efficiency.

From an architecture standpoint:

* For non-regulated workloads, using a global profile can significantly improve availability and absorb regional spikes.
* For regulated workloads, configure geographic profiles that align with your compliance boundaries, and document those decisions in your governance artifacts.

Bedrock automatically encrypts data in transit using TLS and does not store customer prompts or outputs by default; combine this with CloudTrail logging for compliance posture.

## Monitoring and Observability for 429 and 503 Errors

You cannot manage what you cannot see, so robust monitoring is essential when working with quota-driven errors and service availability. Setting up comprehensive
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
monitoring is essential for proactive error management and maintaining application reliability.

**Note:**
CloudWatch custom metrics, alarms, and dashboards incur charges based on usage. Review
[CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/)
for details.

### Essential CloudWatch Metrics

Monitor these CloudWatch metrics:

* **Invocations**
  : Successful model invocations
* **InvocationClientErrors**
  : 4xx errors including throttling
* **InvocationServerErrors**
  : 5xx errors including service unavailability
* **InvocationThrottles**
  : 429 throttling errors
* **InvocationLatency**
  : Response times
* **InputTokenCount/OutputTokenCount**
  : Token usage for TPM monitoring

For better insight, create dashboards that:

* Separate 429 and 503 into different widgets so you can see whether a spike is quota-related or service-side.
* Break down metrics by ModelId and Region to find the specific models or Regions that are problematic.
* Show side-by-side comparisons of current traffic vs previous weeks to spot emerging trends before they become incidents.

### Critical Alarms

Do not wait until users notice failures before you act. Configure CloudWatch alarms with Amazon SNS notifications based on thresholds such as:

**For 429 Errors:**

* A high number of throttling events in a 5-minute window.
* Consecutive periods with non-zero throttle counts, indicating sustained pressure.
* Quota utilization above a chosen threshold (for example, 80% of RPM/TPM).

**For 503 Errors:**

* Service success rate falling below your SLO (for example, 95% over 10 minutes).
* Sudden spikes in 503 counts correlated with specific Regions or models.
* Service availability (for example, <95% success rate)
* Signs of connection pool saturation on client metrics.

#### Alarm Configuration Best Practices

* Use
  [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/)
  topics to route alerts to your team’s communication channels (Slack, PagerDuty, email)
* Set up different severity levels: Critical (immediate action), Warning (investigate soon), Info (trending issues)
* Configure alarm actions to trigger automated responses where appropriate
* Include detailed alarm descriptions with troubleshooting steps and runbook links
* Test your alarms regularly to make sure notifications are working correctly
* Do not include sensitive customer data in alarm messages

### Log Analysis Queries

CloudWatch Logs Insights queries help you move from “we see errors” to “we understand patterns.” Examples include:

**Find 429 error patterns:**

```
fields @timestamp, @message
| filter @message like /ThrottlingException/
| stats count() by bin(5m)
| sort @timestamp desc
```

**Analyze 503 error correlation with request volume:**

```
fields @timestamp, @message
| filter @message like /ServiceUnavailableException/
| stats count() as error_count by bin(1m)
| sort @timestamp desc
```

## Wrapping Up: Building Resilient Applications

We’ve covered a lot of ground in this post, so let’s bring it all together. Successfully handling Bedrock errors requires:

1. **Understand root causes**
   : Distinguish quota limits (429) from capacity issues (503)
2. **Implement appropriate retries**
   : Use exponential backoff with different parameters for each error type
3. **Design for scale**
   : Use connection pooling, circuit breakers, and Cross-Region failover
4. **Monitor proactively**
   : Set up comprehensive CloudWatch monitoring and alerting
5. **Plan for growth**
   : Request quota increases and implement fallback strategies

## Conclusion

Handling 429 ThrottlingException and 503 ServiceUnavailableException errors effectively is a crucial part of running production-grade generative AI workloads on Amazon Bedrock. By combining quota-aware design, intelligent retries, client-side resilience patterns, cross-Region strategies, and strong observability, you can keep your applications responsive even under unpredictable load.

As a next step, identify your most critical Bedrock workloads, enable the retry and rate-limiting patterns described here, and build dashboards and alarms that expose your real peaks rather than just averages. Over time, use real traffic data to refine quotas, fallback models, and regional deployments so your AI systems can remain both powerful and dependable as they scale.

For teams looking to accelerate incident resolution, consider enabling
[AWS DevOps Agent](https://aws.amazon.com/devops-agent/)
—an AI-powered agent that investigates Bedrock errors by correlating CloudWatch metrics, logs, and alarms just like an experienced DevOps engineer would. It learns your resource relationships, works with your observability tools and runbooks, and can significantly reduce mean time to resolution (MTTR) for 429 and 503 errors by automatically identifying root causes and suggesting remediation steps.

**Learn More**

---

**About the Authors**

### Farzin Bagheri

Farzin Bagheri is a Principal Technical Account Manager at AWS, where he supports strategic customers in achieving the highest levels of cloud operational maturity. Farzin joined AWS in 2013, and his focus in the recent years has been on identifying common patterns in cloud operation challenges and developing innovative solutions and strategies that help both AWS and its customers navigate complex technical landscapes.

### Abel Laura

Abel Laura is a Technical Operations Manager with AWS Support, where he leads customer-centric teams focused on emerging generative AI products. With over a decade of leadership experience, he partners with technical support specialists to transform complex challenges into innovative, technology-driven solutions for customers. His passion lies in helping organizations harness the power of emerging AI technologies to drive meaningful business outcomes. In his free time, Abel enjoys spending time with his family and mentoring aspiring tech leaders.

### Arun KM

Arun is a Principal Technical Account Manager at AWS, where he supports strategic customers in building production-ready generative AI applications with operational excellence. His focus in recent years has been on Amazon Bedrock, helping customers troubleshoot complex error patterns, customize open-source models, optimize model performance, and develop resilient AI architectures that can maximize return on investment and scale reliably in production environments.

### Aswath Ram A Srinivasan

**Aswath Ram A Srinivasan**
is a Sr. Cloud Support Engineer at AWS. With a strong background in ML, he has three years of experience building AI applications and specializes in hardware inference optimizations for LLM models. As a Subject MatterExpert, he tackles complex scenarios and use cases, helping customers unblock challenges and accelerate their path to production-ready solutions using Amazon Bedrock, Amazon SageMaker, and other AWS services. In his free time, Aswath enjoys photography and researching Machine Learning and Generative AI.