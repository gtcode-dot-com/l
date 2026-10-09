---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-17T12:03:16.163034+00:00'
exported_at: '2025-12-17T12:03:18.777015+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/compromised-iam-credentials-power-large.html
structured_data:
  about: []
  author: ''
  description: Amazon reports a new AWS crypto mining campaign abusing IAM credentials,
    ECS, EC2, and termination protection for persistence.
  headline: Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/compromised-iam-credentials-power-large.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign
updated_at: '2025-12-17T12:03:16.163034+00:00'
url_hash: 8be549b12a521ef026809e1182dd59b8b4c09dd2
---

**

Dec 16, 2025
**

Ravie Lakshmanan

Malware / Threat Detection

An ongoing campaign has been observed targeting Amazon Web Services (AWS) customers using compromised Identity and Access Management (
[IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
) credentials to enable cryptocurrency mining.

The activity, first detected by Amazon's GuardDuty managed threat detection service and its automated security monitoring systems on November 2, 2025, employs never-before-seen persistence techniques to hamper incident response and continue unimpeded, according to a new report shared by the tech giant ahead of publication.

"Operating from an external hosting provider, the threat actor quickly enumerated resources and permissions before deploying crypto mining resources across ECS and EC2," Amazon
[said](https://aws.amazon.com/blogs/security/cryptomining-campaign-targeting-amazon-ec2-and-amazon-ecs/)
. "Within 10 minutes of the threat actor gaining initial access, crypto miners were operational."

The multi-stage attack chain essentially begins with the unknown adversary leveraging compromised IAM user credentials with admin-like privileges to initiate a discovery phase designed to probe the environment for EC2 service quotas and test their permissions by invoking the
[RunInstances API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html)
with the "DryRun" flag set.

This enabling of the "DryRun" flag is crucial and intentional as it enables the attackers to validate their IAM permissions without actually launching instances, thereby avoiding racking up costs and minimizing their forensic trail. The end goal of the step is to determine if the target infrastructure is suitable for deploying the miner program.

The infection proceeds to the next stage when the threat actor calls
[CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html)
and
[CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)
to create IAM roles for autoscaling groups and AWS Lambda, respectively. Once the roles are created, the "
[AWSLambdaBasicExecutionRole](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
" policy is attached to the Lambda role.

In the activity observed to date, the threat actor is said to have created dozens of ECS clusters across the environment, in some cases exceeding 50 ECS clusters in a single attack.

"They then called RegisterTaskDefinition with a malicious DockerHub image yenik65958/secret:user," Amazon said. "With the same string used for the cluster creation, the actor then created a service, using the task definition to initiate crypto mining on ECS Fargate nodes."

The DockerHub image, which has since been taken down, is configured to run a shell script as soon as it's deployed to launch cryptocurrency mining using the
[RandomVIREL](https://github.com/virel-project/randomvirel)
mining algorithm. Additionally, the threat actor has been observed creating autoscaling groups that are set to scale from 20 to 999 instances in an effort to exploit EC2 service quotas and maximize resource consumption.

The EC2 activity has targeted both high-performance GPU and machine learning instances and compute, memory, and general-purpose instances.

What makes this campaign stand apart is its use of the
[ModifyInstanceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.html)
action with the "disableApiTermination" parameter set to "True," which prevents an instance from being terminated using the Amazon EC2 console, command line interface, or API. This, in turn, has the effect of requiring victims to re-enable API termination before deleting the impacted resources.

"Instance termination protection can impair incident response capabilities and disrupt automated remediation controls," Amazon said. "This technique demonstrates an understanding of common security response procedures and intent to maximize the duration of mining operations."

This is not the first time the security risk associated with ModifyInstanceAttribute has come to light. In April 2024, security researcher Harsha Koushik
[demonstrated](https://medium.com/kernel-space/the-dangers-of-modifyinstanceattribute-d4290ca7a457)
a proof-of-concept (PoC) that detailed how the action can be abused to take over instances, exfiltrate instance role credentials, and even seize control of the entire AWS account.

Furthermore, the attacks entail the creation of a
[Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
that can be invoked by any principal and an IAM user "user-x1x2x3x4" to which the AWS managed policy "
[AmazonSESFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSESFullAccess.html)
" is attached, granting the adversary complete access over the Amazon Simple Email Service (SES) to likely carry out phishing attacks.

To secure against the threat, Amazon is urging AWS customers to follow the steps below -

* Enforce strong identity and access management controls
* Implement temporary credentials instead of long-term access keys
* Use multi-factor authentication (MFA) for all users
* Apply the principle of least privilege (PoLP) to IAM principals to restrict access
* Add container security controls to scan for suspicious images
* Monitor unusual CPU allocation requests in ECS task definitions
* Use AWS CloudTrail to log events across AWS services
* Ensure AWS GuardDuty is enabled to facilitate automated response workflows

"The threat actor's scripted use of multiple compute services, in combination with emerging persistence techniques, represents a significant advancement in crypto mining attack methodologies," Amazon concluded.