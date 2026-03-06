---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-06T00:15:31.052375+00:00'
exported_at: '2026-03-06T00:15:34.740614+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/embed-amazon-quick-suite-chat-agents-in-enterprise-applications
structured_data:
  about: []
  author: ''
  description: Organizations find it challenging to implement a secure embedded chat
    in their applications and can require weeks of development to build authentication,
    token validation, domain security, and global distribution infrastructure. In
    this post, we show you how to solve this with a one-click deployment solution
    to embe...
  headline: Embed Amazon Quick Suite chat agents in enterprise applications
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/embed-amazon-quick-suite-chat-agents-in-enterprise-applications
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Embed Amazon Quick Suite chat agents in enterprise applications
updated_at: '2026-03-06T00:15:31.052375+00:00'
url_hash: ce33277cafd41212ec6414ddcf24f9ad5546eb41
---

Organizations can face two critical challenges with conversational AI. First, users need answers where they work—in their CRM, support console, or analytics portal—not in separate tools. Second, implementing a secure embedded chat in their applications can require weeks of development to build authentication, token validation, domain security, and global distribution infrastructure.

[Amazon Quick Suite](https://aws.amazon.com/quicksuite/)
[embedded chat](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-quick-suite-embedded-chat/)
helps solve the first challenge by bringing conversational AI directly into your applications, so users can query structured data, search documents, and trigger actions without switching tools.

In this post, we show you how to solve the second challenge with a one-click deployment solution to embed the chat agents using the Quick Suite
[Embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk)
in enterprise portals.

## Solution overview

The solution deploys a secure web portal for the embedded chat using
[Amazon CloudFront](https://aws.amazon.com/cloudfront/)
for global content delivery,
[Amazon Cognito](https://aws.amazon.com/cognito/)
for
[OAuth 2.0](https://auth0.com/intro-to-iam/what-is-oauth-2)
authentication,
[Amazon API Gateway](https://aws.amazon.com/api-gateway/)
for REST API endpoints,
[AWS Lambda](https://aws.amazon.com/lambda/)
for serverless API processing, and
[OpenID Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)
(OIDC) federation for identity integration with the Quick Suite.

The solution implements defense-in-depth security with multiple layers of protection:
[DDoS](https://aws.amazon.com/shield/ddos-attack-protection/)
protection on CloudFront, a private
[Amazon Simple Storage Service](https://aws.amazon.com/s3/)
(Amazon S3) bucket with
[origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html)
helping prevent direct access to frontend assets,
[AWS WAF](https://aws.amazon.com/waf/)
rate limiting protection on API Gateway, and
[JSON Web Token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html)
(JWT) signature validation using Amazon Cognito public keys before generating time-limited user-specific embed URLs with least-privilege
[AWS Identity and Access Management](https://aws.amazon.com/iam/)
(IAM) permissions.

The following diagram illustrates the solution architecture.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-1.png)

The workflow consists of the following steps:

1. Users access the web portal URL, which routes to CloudFront.
2. CloudFront uses origin access control to fetch HTML, CSS, and JavaScript files from a private S3 bucket.
3. The web application checks for a valid authentication token and redirects unauthenticated users to the Amazon Cognito hosted UI for OAuth 2.0 login.
4. Users enter credentials on the Amazon Cognito login page, which validates them and redirects back to the CloudFront URL with a single-use authorization code.
5. The application extracts the authorization code and makes an HTTPS API call to API Gateway, which passes through AWS WAF rate limiting.
6. API Gateway invokes a Lambda function with the authorization code.
7. The Lambda function makes a server-to-server HTTPS call to the Amazon Cognito OAuth token endpoint, exchanging the authorization code for JWT tokens (ID token, access token, refresh token).
8. The function validates the ID token’s cryptographic signature using Amazon Cognito public keys
   [JSON Web Key Set](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html)
   (JWKS) with thread-safe caching.

The following is a decoded JWT example:

```
{"at_hash": "abcdefifB5vH2D0HEvLghi", "sub": "12345678-abcd-1234-efgh-123456789012", "email_verified": true, "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_EXAMPLE123", "cognito:username": "12345678-abcd-1234-efgh-123456789012", "origin_jti": "abcd1234-5678-90ef-ghij-klmnopqrstuv", "aud": "1a2b3c4d5e6f7g8h9i0j1k2l3m", "event_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "token_use": "id", "auth_time": 1704063600, "exp": 1704067200, "iat": 1704063600, "jti": "abcdef12-3456-7890-abcd-ef1234567890", "email": "user123@example.com"}
```

9. The Lambda function calls the
   [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
   (AWS STS)
   [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)
   API with the verified ID token to assume the IAM web identity role and receive temporary AWS credentials.
10. The function uses the temporary credentials to call the Quick Suite
    [ListUsers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUsers.html)
    API to verify the user exists, then calls the
    [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html)
    API to help generate a secure embedded URL with domain restrictions.
11. The function returns the embed URL in a JSON response with
    [cross-origin resource sharing](https://aws.amazon.com/blogs/networking-and-content-delivery/cors-configuration-through-amazon-cloudfront/)
    (CORS) headers through API Gateway to CloudFront. The following is an embed URL example:

    ```
    {"ChatEmbedUrl": "https://us-east-1.quicksight.aws.amazon.com/embedding/abcdefe827dd4ef8b4e1fb921db046c4/quick/chat?code=Abcdef....&amp;amp;identityprovider=quicksight&amp;amp;isauthcode=true", "user": "user123@example.com"}
    ```
12. The CloudFront application uses the Quick Suite Embedding SDK to create an embedding context and render the chat interface in an HTML iframe with secure cross-origin communication.

You can deploy the solution with the following high-level steps:

1. Deploy the serverless infrastructure using the
   [AWS Cloud Development Kit](https://aws.amazon.com/cdk/)
   (AWS CDK).
2. Provision users in Amazon Cognito and Quick Suite.
3. Share the Quick Suite assets (chat agent and associated connections, knowledge base).
4. Access the web portal to use Quick Suite chat agents.

## Prerequisites

The following prerequisites are required to deploy the solution demonstrated in this post:

## Deploy serverless infrastructure using AWS CDK

Complete the following steps to deploy the serverless infrastructure using the AWS CDK:

1. Clone the
   [GitHub repository](https://github.com/aws-samples/sample-quicksuite-chat-embedding)
   :

```
git clone git@github.com:aws-samples/sample-quicksuite-chat-embedding.git
cd sample-quicksuite-chat-embedding
```

2. Deploy the infrastructure:

You will be prompted to enter your AWS Region code, AWS CloudFormation stack ID and portal title, and your AWS CLI profile.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-2.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-3.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-4.png)

## Provision users in Amazon Cognito and Quick Suite

Complete the following steps to provision users in Amazon Cognito and Quick Suite:

1. Create an Amazon Cognito user in an Amazon Cognito user pool:

```
python scripts/create_cognito_user.py --profile <aws-profile> <cognito-user-email>
```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-5.png)

2. Create a federated user in Quick Suite:

```
python scripts/create_quicksuite_user.py --profile <aws-profile> <cognito-user-email>
```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-6.png)

## Share Quick Suite chat agent

Complete the following steps to share your Quick Suite chat agent:

1. Sign in to the Quick Suite console using credentials with the Quick Suite Author Pro role.
2. Choose
   **Chat agents**
   in the navigation pane.
3. Select the agents you want to share (for example, AnyCompany Ecom order assistant) and choose
   **Share**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-7.png)

4. Search for the user name (for example, user123@example.com) you created earlier.
5. Choose
   **Share**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-8.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-9.png)

After sharing this agent, you also need to share each linked resource of the agent separately to confirm full functionality.

## Access web portal to use the Quick Suite chat agents

Complete the following steps to access the web portal and start using the chat agents:

1. Look for the temporary password in the Amazon Cognito verification email.
2. Access the CloudFront URL from your web browser with the user ID and temporary password.
3. You will be prompted to change your password at your first login.

After the successful login, you can see
**My Assistant**
in the chat interface.

4. Choose the Region to connect to the custom Quick Suite chat agents.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-10.png)

5. To see the chat agents shared with you, choose
   **Shared with me**
   under
   **Filter**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-11.png)

6. Choose the agent you want and start chatting.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-12.png)

The following screenshots show chat interactions of a customer service representative tracking an example online order and processing its return as requested by a verified customer over the phone.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-13.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-14.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-15.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-16.png)

## Clean up

To clean up your resources, delete the AWS resources deployed:

## Conclusion

This solution addresses core challenges for embedding conversational AI at scale: securing authentication for thousands of concurrent users across global locations, maintaining enterprise-grade security with comprehensive audit trails, and simplifying deployment with automated infrastructure provisioning. You can customize the portal branding, adjust security policies, and integrate with existing identity providers. You can scale to thousands of concurrent users automatically while maintaining pay-as-you-go pricing.

To try this solution, clone the
[GitHub repository](https://github.com/aws-samples/sample-quicksuite-chat-embedding)
and deploy the complete infrastructure with one click to embed Quick Suite chat agents.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/24/ML-20358-17-photo-100x100.jpg)
**Satyanarayana Adimula**
is a Senior Builder in AWS Generative AI Innovation & Delivery. Leveraging over 20 years of data and analytics expertise, he specializes in building agentic AI systems that enable large enterprises to automate complex workflows, accelerate decision-making, and achieve measurable business outcomes.