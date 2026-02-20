---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-20T10:15:30.397295+00:00'
exported_at: '2026-02-20T10:15:33.266941+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/customize-ai-agent-browsing-with-proxies-profiles-and-extensions-in-amazon-bedrock-agentcore-browser
structured_data:
  about: []
  author: ''
  description: 'Today, we are announcing three new capabilities that address these
    requirements: proxy configuration, browser profiles, and browser extensions. Together,
    these features give you fine-grained control over how your AI agents interact
    with the web. This post will walk through each capability with configuration examples
    and practical use cases to help you get started.'
  headline: Customize AI agent browsing with proxies, profiles, and extensions in
    Amazon Bedrock AgentCore Browser
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/customize-ai-agent-browsing-with-proxies-profiles-and-extensions-in-amazon-bedrock-agentcore-browser
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Customize AI agent browsing with proxies, profiles, and extensions in Amazon
  Bedrock AgentCore Browser
updated_at: '2026-02-20T10:15:30.397295+00:00'
url_hash: d56bec4bd3dcb32390d3324d7149acfc293c815c
---

AI agents that browse the web need more than basic page navigation. Our customers tell us they need agents that maintain session state across interactions, route traffic through corporate proxy infrastructure, and run with custom browser configurations.
[AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html)
provides a secure, isolated browser environment for your agents to interact with web applications. Until now, in Agent Core Browser, each browser session started from a blank slate with default settings and direct internet access, limiting what agents could accomplish in real-world enterprise environments.

Today, we are announcing three new capabilities that address these requirements:
[proxy configuration](https://aws.amazon.com/about-aws/whats-new/2026/02/bedrock-agentcore-browser-proxy/)
,
[browser profiles](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-agentcore-browser-profiles/)
, and
[browser extensions](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-agentcore-browser-custom-extensions/)
. Together, these features give you fine-grained control over how your AI agents interact with the web.

These three capabilities give you control over how AgentCore Browser sessions connect to the internet, what state they retain, and how they behave. Proxy configuration lets you route browser traffic through your own proxy servers, providing IP stability and integration with corporate network infrastructure. Browser profiles persist cookies and local storage across sessions, so agents can resume authenticated workflows without repeating login flows. Browser extensions load Chrome extensions into sessions to customize browser behavior for your use case. This post will walk through each capability with configuration examples and practical use cases to help you get started.

## How persistent browser profiles keep AI Agents running smoothly

Customers building agents for e-commerce testing, authenticated workflows, and multi-step user journeys need browser sessions that remember state. Without persistent profiles, agents are required to re-authenticate and rebuild context at the start of every session, adding latency and fragility to automated workflows. Browser profiles solve this by saving and restoring cookies and local storage between sessions, so an agent that logged into a portal yesterday can pick up where it left off today.

IP stability is another common requirement. Healthcare and financial portals validate sessions based on source IP address, and rotating AWS IP addresses cause frequent re-authentication cycles that break long-running workflows. Proxy support lets you route traffic through servers with stable egress IPs, maintaining session continuity and meeting IP allowlisting requirements. Organizations that route traffic through corporate proxies need to extend this practice to AI agents for browser sessions. Proxy configuration enables access to internal webpages and resources that require proxy-based connectivity.

Browser extensions allow custom configurations such as ad blocking, authentication helpers, or other browser-level customization. When combined with proxy logging, these capabilities helps provide access control and audit evidence that

may
[compliance programs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/compliance-validation.html)


such as FedRAMP, HITRUST, and PCI

.

## Feature 1: Proxy configuration

Browser
now supports routing browser traffic through your own external proxy servers. When you create a browser session with proxy configuration, AgentCore configures the browser to route HTTP and HTTPS traffic through your specified proxy servers.

### How it works

You call
`StartBrowserSession`
with a
`proxyConfiguration`
specifying your proxy server. If using authentication, AgentCore retrieves proxy credentials from AWS Secrets Manager. The browser session starts with your proxy configuration applied, and browser traffic routes through your proxy server based on your domain routing rules.

### Getting started with proxies

Complete these
[prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-proxies.html#browser-proxies-prerequisites)
before proceeding.

```
import boto3
import json
client = boto3.client('secretsmanager')
client.create_secret(
    Name='my-proxy-credentials',
    SecretString=json.dumps({
        'username': '<your-username>',
        'password': '<your-password>'
    })
)
```

**Step 2:**
Create a browser session with proxy configuration

```
session_client = boto3.client('bedrock-agentcore', region_name='<region>')

response = session_client.start_browser_session(
    browserIdentifier="aws.browser.v1",
    name="my-proxy-session",
    proxyConfiguration={
        "proxies": [{
            "externalProxy": {
                "server": "<your-proxy-hostname>",
                "port": 8080,
                "credentials": {
                    "basicAuth": {
                        "secretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>"
                    }
                }
            }
        }]
    }
)
print(f"Session ID: {response['sessionId']}")
```

The credentials field is optional for proxies without authentication.

### Domain-based routing

Use
`domainPatterns`
to route specific domains through designated proxies, and
`bypass.domainPatterns`
for domains that should connect directly:

```
proxyConfiguration={
    "proxies": [
        {
            "externalProxy": {
                "server": "corp-proxy.example.com",
                "port": 8080,
                "domainPatterns": [".company.com", ".internal.corp"]
            }
        },
        {
            "externalProxy": {
                "server": "general-proxy.example.com",
                "port": 8080
            }
        }
    ],
    "bypass": {
        "domainPatterns": [".amazonaws.com"]
    }
}
```

With this configuration, requests to



and
`internal.corp`




route through the corporate

proxy,

requests

to
`amazonaws.com`




bypass all proxies

, and everything else routes through the general proxy.

Th

e

s

e fields



are

just an example.


Bypass domains


can match
`bypass.domainPatterns`


to connect directly and


external

proxy



can be a

valid

proxy’s


`domainPatterns`



route through that proxy (first match wins based on array order).

### Routing precedence

When AgentCore Browser processes an outbound request, it walks through three tiers of routing rules to decide where to send the traffic. It first checks the bypass list. If the destination domain matches a
`bypass.domainPatterns`
entry, the request connects directly to the internet without using any proxy. If the domain does not match a bypass rule, AgentCore checks each proxy’s
`domainPatterns`
in order and routes the request through the first proxy whose pattern matches. If no proxy pattern matches either, the request falls through to the default proxy, which is the proxy entry that has no
`domainPatterns`
defined.

Test the new proxy feature with this
[code example](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/11-browser-with-proxy)
.

## Feature 2: Browser profiles

Browser profiles let you persist and reuse session data across multiple browser sessions, including cookies and local storage. An agent that authenticates with a web portal in one session can restore that state in a later session without logging in again. This is useful for authenticated workflows where re-login adds latency, e-commerce testing where shopping carts and form data need to survive between sessions, and multi-step user journeys that span multiple browser invocations.

The profile lifecycle has four stages. You start by calling
`create_browser_profile()`
to create a named profile. At the end of a session, you call
`save_browser_session_profile()`
to capture the current cookies and local storage into that profile. When you start a new session, you pass the profile identifier in the
`profileConfiguration`
parameter of
`start_browser_session()`
, which restores the saved state into the new browser. When you no longer need the profile, you call
`delete_browser_profile()`
to clean it up.

The following example shows an agent that adds items to a shopping cart in one session and verifies they persist in a subsequent session.

Complete these
[prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-profiles.html#browser-profiles-prerequisites)
before proceeding.

```
import boto3

control_client = boto3.client('bedrock-agentcore-control', region_name='<region>') # replace by your region

session_client = boto3.client('bedrock-agentcore', region_name='<region>') # replace by your region

# Create a browser profile
profile = control_client.create_browser_profile(name="ecommerce_profile")
profile_id = profile['profileId']

# Session 1: Add items to cart
session1 = session_client.start_browser_session(
    browserIdentifier=”aws.browser.v1”,
    name="shopping-session-1"
)
# ... agent navigates and adds items to cart ...

# Save session state to profile
session_client.save_browser_session_profile(
    sessionId=session1['sessionId'],
    browserIdentifier=”aws.browser.v1”,
    profileIdentifier=profile_id
)
session_client.stop_browser_session(sessionId=session1['sessionId'], browserIdentifier="aws.browser.v1")

# Session 2: Resume with saved profile
session2 = session_client.start_browser_session(
    browserIdentifier=”aws.browser.v1”,
    name="shopping-session-2",
    profileConfiguration={"profileIdentifier": profile_id}
)
# Cart items from Session 1 are now available
```

Test the new profile feature with this
[code example](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/10-browser-with-profile)
.

## Feature 3: Browser extensions

Browser extensions let you load Chrome extensions into AgentCore Browser sessions to customize how the browser behaves. You package extensions as ZIP files, upload them to
[Amazon Simple Storage Service](https://www.google.com/search?q=Amazon+Simple+Storage+Service&rlz=1C1GCEA_enUS1107US1107&oq=amazon+s3&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGDzSAQgyNTAyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&ved=2ahUKEwi4xuC6v9eSAxURm2oFHUlqEwMQgK4QegYIAQgAEAU)
(Amazon S3), and reference them when starting a browser session. This provides access to functionality available through the Chrome extension API, from proxy routing and ad blocking to authentication helpers and content modification. For example, you can inject authentication tokens for internal applications, remove ads, and track scripts that interfere with agent navigation, or modify page content to improve how agents interact with a site.

Your extension should follow the standard
[Chromium extension](https://www.chromium.org/developers/design-documents/extensions/)
format and adhere to Chromium extension guidelines.

Complete these
[prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-extensions.html#browser-extensions-prerequisites)
before proceeding.

1. Upload the extension to Amazon S3:

   ```
   # Upload extension to S3

   import boto3
   s3 = boto3.client('s3')
   s3.upload_file(
       'my-extension.zip',
       'amzn-s3-demo-bucket-extensions',
       'extensions/my-extension.zip'
   )
   ```
2. Then, start a session with the extension, pointing to the Amazon S3 bucket where you’ve uploaded the zip file:

   ```
   import boto3
   region = "<region>" # replace by your region
   client = boto3.client('bedrock-agentcore', region_name=region)

   response = client.start_browser_session(
       browserIdentifier="aws.browser.v1",
       name="my-session-with-extensions",
       sessionTimeoutSeconds=1800,
       viewPort={
           'height': 1080,
           'width': 1920
       },
       extensions=[
           {
               "location": {
                   "s3": {
                       "bucket": "amzn-s3-demo-bucket-extensions",
                       "prefix": "extensions/my-extension.zip"
                   }
               }
           },
           {
               "location": {
                   "s3": {
                       "bucket": "amzn-s3-demo-bucket-extensions",
                       "prefix": "extensions/another-extension.zip",
                       "versionId": "abc123"  # Optional - for versioned S3 buckets
                   }
               }
           }
       ]
   )

   print(f"Session ID: {response['sessionId']}")
   print(f"Status: {response['status']}")
   print(f"Automation Stream: {response['streams']['automationStream']['streamEndpoint']}")
   ```

Test the new extensions feature with this
[code example](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/05-AgentCore-tools/02-Agent-Core-browser-tool/12-browser-extensions)
.

## Conclusion

Proxy configuration, browser profiles, and browser extensions give AgentCore Browser the proxy routing, session persistence, and extensibility controls that customers need to deploy AI agents that browse the web in production. You can route traffic through your corporate proxy infrastructure, maintain session continuity across interactions, and customize browser behavior with extensions, all while keeping credentials secure in AWS Secrets Manager. Customers can carry e-commerce context and information among sessions, create your own extension and test it in a secure environment before release, and, also, have browser connecting into your network through proxies.

To get started, see the tutorials in the
[Amazon Bedrock AgentCore samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples)

repository and the Amazon Bedrock AgentCore Browser
[documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html)

.

For more information about pricing, visit
[Amazon Bedrock AgentCore Pricing](https://aws.amazon.com/bedrock/agentcore/pricing/)

.

---

## About the Authors

### Joshua Samuel

**Joshua Samuel**
is a Senior AI/ML Specialist Solutions Architect at AWS who accelerates enterprise transformation through AI/ML, and generative AI solutions, based in Melbourne, Australia. A passionate disrupter, he specializes in agentic AI and coding techniques – Anything that makes builders faster and happier. Outside work, he tinkers with home automation and AI coding projects, and enjoys life with his wife, kids and dog.

### Evandro Franco

**Evandro Franco**
is a Sr. Data Scientist working on Amazon Web Services. He is part of the Global GTM team that helps AWS customers overcome business challenges related to AI/ML on top of AWS, mainly on Amazon Bedrock AgentCore and Strands Agents. He has more than 18 years of experience working with technology, from software development, infrastructure, serverless, to machine learning. In his free time, Evandro enjoys playing with his son, mainly building some funny Lego bricks.

### Kosti Vasilakakis

**Kosti Vasilakakis**
is a Principal PM at AWS on the Agentic AI team, where he has led the design and development of several Bedrock AgentCore services from the ground up, including Runtime, Browser, Code Interpreter, and Identity. He previously worked on Amazon SageMaker since its early days, launching AI/ML capabilities now used by thousands of companies worldwide. Earlier in his career, Kosti was a data scientist. Outside of work, he builds personal productivity automations, plays tennis, and enjoys life with his wife and kids.

### Yan Marim

**Yan Marim**
is a Sr. GenAI Specialist Solutions Architect at Amazon Web Services, based in Brazil. As part of the LATAM Specialist team, he guides customers through their generative AI adoption journey, focusing on Amazon Bedrock and agentic AI solutions. In his free time, Yan enjoys spending quality time with his wife and dog, and watching soccer games.

### Kevin Orellana

**Kevin Orellana**
is a Software Development Engineer at Amazon Web Services on the Bedrock AgentCore team, based in Seattle. He builds and operates core infrastructure powering agentic AI capabilities, including Browser, Code Interpreter, and Runtime. Earlier in his career, Kevin worked on the Bedrock inference team hosting frontier models. In his free time, he enjoys hiking with his Goldendoodle, experimenting with multi-agent simulations, and working toward building a personal AI assistant that speaks English, Spanish, and Mandarin.