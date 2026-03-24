---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-24T04:49:10.507921+00:00'
exported_at: '2026-03-24T04:49:13.787262+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/enforce-data-residency-with-amazon-quick-extensions-for-microsoft-teams
structured_data:
  about: []
  author: ''
  description: In this post, we will show you how to enforce data residency when deploying
    Amazon Quick Microsoft Teams extensions across multiple AWS Regions. You will
    learn how to configure multi-Region Amazon Quick extensions that automatically
    route users to AWS Region-appropriate resources, helping keep compliance with
    GDPR a...
  headline: Enforce data residency with Amazon Quick extensions for Microsoft Teams
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/enforce-data-residency-with-amazon-quick-extensions-for-microsoft-teams
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Enforce data residency with Amazon Quick extensions for Microsoft Teams
updated_at: '2026-03-24T04:49:10.507921+00:00'
url_hash: a409313e20121cc873b8d1f63f2dbc16429459b3
---

Organizations with users in multiple geographies face data residency requirements such as General Data Protection Regulation (GDPR) in Europe, country-specific data sovereignty laws, and internal compliance policies.
[Amazon Quick](https://aws.amazon.com/quick/)
with Microsoft 365 extensions supports Regional routing to meet these requirements.

Amazon Quick supports multi-Region deployments so you can route users to AWS Region-specific Amazon Quick resources (
[Quick chat agents](https://aws.amazon.com/quick/chat-agents/)
,
[Quick Flows](https://aws.amazon.com/quick/flows/)
,
[knowledge bases](https://docs.aws.amazon.com/quick/latest/userguide/knowledge-base-integrations.html)
, and more). Regulated industries such as financial services, healthcare, energy, and telecommunications commonly use this pattern to keep data within specific geographical boundaries.

If you integrate Amazon Quick with Microsoft 365 applications, in this instance Microsoft Teams, users must authenticate and connect to their appropriate Regional Amazon Quick resources. Regional routing makes sure users access the chat agents and resources they build in their Amazon Quick Region. In this post, we will show you how to enforce data residency when deploying Amazon Quick Microsoft Teams extensions across multiple AWS Regions. You will learn how to configure multi-Region Amazon Quick extensions that automatically route users to AWS Region-appropriate resources, helping keep compliance with GDPR and other data sovereignty requirements.

## Solution overview

In this post, we present a real-world example with MyCompany, a fictional global organization with European headquarters accessing Amazon Quick in the Europe (Ireland) Region (
`eu-west-1`
) and a US branch in the US East (N. Virginia) Region (
`us-east-1`
). A single Amazon Quick account has AWS Region-specific chat agents (
`MyCompany-Knowledge-Agent-eu-west-1 and MyCompany-Knowledge-Agent-us-east-1`
) containing localized corporate information.

Regional routing requires
[AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
with a trusted token issuer (TTI) for cross-system authentication. This post uses Microsoft Entra ID for group-based access control to demonstrate how organizations can automatically route users to their appropriate AWS Regions, though other identity management approaches are possible. This post focuses on the
[Amazon Quick extension for Microsoft Teams](https://docs.aws.amazon.com/quicksuite/latest/userguide/teams-extension.html)
as the primary example.

The following architecture diagram demonstrates how to automate user routing across multiple AWS Regions by integrating Microsoft Entra ID with IAM Identity Center. By using Microsoft Entra ID group membership to direct users to their designated Regional Amazon Quick deployments, you can maintain data residency within specific geographic boundaries while providing a consistent experience for your global workforce.

![Architecture diagram showing a 6-step integration workflow between Amazon Quick and Microsoft Teams across two AWS regions (eu-west-1 and us-east-1), including IAM Identity Center, AWS Secrets Manager, and MS Entra ID components](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image1.png)

To implement this design, you will follow a multi-phase process that begins with
[AWS Management Console](http://aws.amazon.com/console)
configuration and concludes with the deployment of Regional add-ons to your users. At a high level, this post shows you how to configure identity and trust one time, then repeat a small set of Regional steps per AWS Region. The following steps summarize the high-level workflow:

1. Initiate setup on the Amazon Quick console and choose the AWS Region to configure.
2. Configure the Regional Microsoft Teams extension integration, including an
   [AWS Identity and Access Management](https://aws.amazon.com/iam/)
   (IAM) role and
   [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
   secret for that AWS Region, and trust IAM Identity Center as a token issuer.
3. Activate the extension in Amazon Quick to generate the Regional manifest file.
4. Register the extension callbacks in your Microsoft Entra ID application and complete the activation callback for the application across all AWS Regions.
5. Deploy the Microsoft Teams add-on (
   `[YOUR_COMPANY_NAME]-Teams-[AWS_REGION]`
   ) to your Regional user groups through Microsoft Entra ID.
6. Map the Regional add-on to its designated knowledge agent (
   `[YOUR_COMPANY_NAME]-Teams-[AWS_REGION] Agent`
   ) to grant users access to localized data.

## Prerequisites

Your AWS environment must have Amazon Quick active in your target AWS Regions, along with the identity and secret management services used to handle Regional authentication. For AWS services, you must have the following in place:

* An active Amazon Quick account
* IAM Identity Center configured and managing user identities for your organization with
  [SAML integration with Microsoft Entra ID](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html)
* Secrets Manager available in both target AWS Regions for storing authentication credentials
* IAM access to create roles and policies

For Microsoft 365, you must have the following for admin access:

* A Global Administrator or Application Administrator role in Microsoft Entra ID
* Access to Microsoft 365 Admin Center for application deployment
* Permissions to create and configure Enterprise applications in Microsoft Entra ID

## Create Microsoft Entra ID application

We start by establishing the shared identity foundation used by every AWS Region. In this first step, you create a Microsoft Entra ID application. The Microsoft 365 extensions use the Microsoft Entra ID application to authenticate users against Amazon Quick through IAM Identity Center. Complete the following steps to create your application:

1. In your Azure account, choose
   **App registrations**
   , then choose
   **New registration**
   .
2. For
   **Supported account types**
   , choose
   **Accounts in this organizational directory only (Personal use only – Single tenant)**
   .
3. Choose
   **Register**
   .
4. Navigate to the application registration’s
   **Manage – Authentication**
   tab.
5. Choose
   **Add Redirect URL**
   .
6. Choose
   **Web**
   .
7. For this post, we use two redirect URLs, using the pattern
   `https://qbs-cell001.dp.appintegrations.[AWS_REGION].prod.plato.ai.aws.dev/auth/idc-tti/callback`
   :
   1. `https://qbs-cell001.dp.appintegrations.eu-west-1.prod.plato.ai.aws.dev/auth/idc-tti/callback`
   2. `https://qbs-cell001.dp.appintegrations.us-east-1.prod.plato.ai.aws.dev/auth/idc-tti/callback`

Microsoft Entra ID uses the callback URLs to return the user’s sign-in response to IAM Identity Center for the correct AWS Region (
`eu-west-1`
or
`us-east-1`
). Use these exact URLs—they are the actual values required for Amazon Quick deployments.

![Amazon Quick IDC Extension Authentication configuration panel showing the Redirect URI configuration tab with two Web-type callback URLs for AWS regions us-east-1 and eu-west-1.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image2.png)

8. Grant the Microsoft Graph
   **User.Read**
   permission to allow the application to sign in users and read their basic profile information. This delegated permission does not require admin consent.

![Amazon Quick IDC Extension API permissions panel showing Microsoft Graph delegated permission User.Read configured with "No" admin consent requirement.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image3.png)

In subsequent steps, you will need your Microsoft tenant ID, application client ID, and client secret value.

## Create trusted token issuer in IAM Identity Center

In this step, you create trusted token issuers in IAM Identity Center. A trusted token issuer is a configuration in IAM Identity Center that validates tokens issued by Microsoft Entra ID. You can use it for cross-system authentication, so users can move between Microsoft 365 and AWS without repeated sign-ins. Complete the following steps to configure the trusted token issuer with your Microsoft tenant’s issuer URL and map the email attribute:

1. On the IAM Identity Center console, choose
   **Settings**
   in the navigation pane.
2. Choose
   **Create trusted token issuer**
   .
3. For
   **Issuer URL**
   , enter the URL for your trusted token issuer in the format
   `https://login.microsoftonline.com/[YOUR_TENANT_ID]/v2.0`
   , using the tenant ID you retrieved from the previous step.
4. For
   **Trusted token issuer name**
   , enter a name for your trusted token issuer in the format
   `[YOUR_COMPANY_NAME]-MS365Extensions-Trust-Token-Issuer`
   , using your company name.
5. Choose
   **Create trusted token issuer**
   .

This configuration applies to each AWS Region where you will be deploying the extensions.

![AWS IAM Identity Center form for creating a trusted token issuer with Microsoft Entra ID login URL, issuer name "MyCompany-MS365Extensions-Trust-Token-Issuer", and email-to-email attribute mapping for JWT identity propagation.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image4.png)

With the global identity components in place, you can now configure each AWS Region with its own secrets, roles, and extension settings that enforce data residency for each geographic AWS Region.

## Set up IAM permissions and Secrets Manager entries

In this step, you create the necessary secrets to store Microsoft 365 extension credentials and IAM permissions that grant read access to secrets.

Create one secret per AWS Region (
`eu-west-1`
and
`us-east-1`
) in Secrets Manager following the name convention
`[YOUR_COMPANY_NAME]/MS365/Extensions/[AWS_REGION]`
:

```
{
    "client_id":"[YOUR_CLIENT_ID]",
    "client_secret":"[YOUR_CLIENT_SECRET]"}
```

Create an IAM policy called
`[YOUR_COMPANY_NAME]-MS365-Extensions-Policy`
:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SecretManagerPermissions",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "[SECRET_EU_WEST_1_ARN]",
                "[SECRET_US_EAST_1_ARN]"
            ]
        },
        {
            "Sid": "TokenIssuerPermissions",
            "Effect": "Allow",
            "Action": [
                "sso:DescribeTrustedTokenIssuer"
            ],
            "Resource": "[YOUR_TTI_ARN]"
        }
    ]
}
```

Use the following trust relationship:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "eu-west-1.prod.appintegrations.plato.aws.internal",
                    "us-east-1.prod.appintegrations.plato.aws.internal",
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}
```

Each time you activate a new AWS Region, you must create a new secret in Secrets Manager and add the new secret Amazon Resource Name (ARN) to the Resource list in the IAM policy. You must also add the new AWS Region you want to activate to the Service field in the IAM role trust relationship. This field identifies the Regional Service Principal, which is the specific AWS service identity (for example,
`eu-west-1.prod.appintegrations.plato.aws.internal`
) that requires permission to assume your IAM roles in that specific AWS Region.

Take note of the created IAM role ARN. You will need it in the next step.

## Configure extensions in Amazon Quick

Complete the following steps to create Amazon Quick managed extensions for Microsoft Teams:

1. Sign in to the Amazon Quick console.
2. In the top right, choose the profile icon.
3. Choose the
   **EU (Ireland)**
   Region.
4. On the drop-down menu, choose
   **Manage Quick.**
5. Under
   **Permissions**
   in the navigation pane, choose
   **Extension access**
   .
6. Choose
   **Add extension access**
   .
7. Set up your trusted token issuer:
   1. For
      **Trusted Token Issuer Arn**
      , enter the ARN for the trusted token issuer you created.
   2. For
      **Aud claim**
      , enter your client ID.

The Audience (Aud) claim is a security identifier that validates the authentication token is only used by the specific application it was intended for, preventing unauthorized access from other entities. These settings are shared across extension accesses in this AWS Region.

![Add extension access wizard Step 1 showing Trusted Token Issuer Setup with red-highlighted required input fields for Trusted Token Issuer ARN and Aud claim, and a blue warning banner about global settings impact.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image5.png)

8. Select
   **Microsoft Teams**
   from the available extension types.

![Add extension access wizard Step 2 showing four Microsoft 365 service options — Word Add-in, Outlook Add-in, Teams bot (selected), and Slack bot — for creating extension access.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image6.png)

9. Configure the extension with your Microsoft 365 tenant ID, security attributes, and authentication settings:
   1. Enter a name and optional description.
   2. For
      **Microsoft tenant ID**
      , enter your tenant ID.
   3. For
      **Secrets Role ARN**
      , enter the ARN for your Secrets Manager role.
   4. For
      **Secrets ARN**
      , enter the ARN for your secret. The ARN is Region-specific and must point to your Regional AWS resources.

![Add extension access Details step showing Microsoft Teams extension configuration form with Name "Teams-access", M365 Tenant ID, Email-to-User Principal Name attribute mapping, and Authentication settings fields for Secrets Role ARN and Secrets ARN.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image7.png)

10. Return to the Amazon Quick console.
11. Choose
    **Extensions**
    in the navigation pane, then choose
    **Create extension**
    .
12. Create a Microsoft Teams extension.
13. Choose the options menu (three dots) next to your extension and choose
    **Install**
    .

This process creates an Enterprise application in Microsoft Entra ID with the unique URLs and instructions Microsoft 365 Teams needs to communicate with the specific Regional AWS assets. Application installation requires permissions to install an Enterprise application in Microsoft Entra ID.

![Amazon Quick Extensions page showing Browser-extension marked "Available" and MyCompany-extension-teams-eu-west-1 for Microsoft Teams, with context menu displaying Install option highlighted in green.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image8.png)

When the installation is complete, the following entry will be displayed in the Microsoft Entra ID Enterprise application.

![Microsoft Entra Enterprise applications admin portal showing search results for "qbs-cell001-prod-dub-teams" with one matching application found and its Object ID displayed.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image9.png)

14. Repeat these steps to create an extension and install the application in the
    `us-east-1`
    Region. Follow the same naming convention with the AWS Region suffix, and use the secret ARN for the
    `us-east-1`
    Region.

![Amazon Quick Extensions page showing Browser-extension marked "Available" for Chrome, Firefox, and Edge, and MyCompany-extension-teams-us-east-1 for Microsoft Teams marked "Available", with context menu showing Install option highlighted in green.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image10.png)

## Create chat agents

After the Regional applications are deployed, you create the AWS Region-specific chat agents that each add-on will access. Each AWS Region maintains its own agent with localized knowledge bases. Complete the following steps:

1. Open the Amazon Quick console in
   `eu-west-1`
   .
2. In the navigation pane, choose
   **Chat agents**
   , then choose
   **Create chat agent**
   .
3. Create a Regional chat agent in
   `eu-west-1`
   with European corporate knowledge. The naming convention includes the AWS Region identifier for easy management across multiple Regions:
   `[YOUR_COMPANY_NAME]-Knowledge-Agent-eu-west-1`
   .

![Amazon Quick chat agents list filtered by "Recently used" showing MyCompany-Knowledge-Agent-eu-west-1 modified 3 minutes ago, a redacted agent entry modified 11 days ago, and My Assistant default system agent modified 3 months ago, all with Chat action buttons.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image11.png)

4. Repeat these steps to create a chat agent in
   `us-east-1`
   with US-specific corporate information, called
   `[YOUR_COMPANY_NAME]-Knowledge-Agent-us-east-1`
   .

![Amazon Quick chat agents management list showing MyCompany-Knowledge-Agent-us-east-1 created by Me with owner permission modified 2 minutes ago, and My Assistant default system agent created by System without owner permission modified 2 months ago.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image12.png)

The final step is deploying the correct Regional add-on to the correct user group in Microsoft 365.

## Deploy Microsoft Teams applications

In the last step, you assign each Microsoft Teams application to their respective Regional groups. Complete the following steps:

1. In
   [Microsoft Teams Admin Center](https://admin.teams.microsoft.com/policies/manage-apps)
   , choose
   **Team apps**
   .
2. Choose
   **Manage apps**
   and filter the applications by “Amazon Quick.”

![Microsoft Teams admin center app management table showing two Amazon Quick entries available to "Everyone" with "Unblocked" status, filtered by search query "amazon quick".](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image13.png)

3. Choose on the first application (in the
   `eu-west-1`
   Region) and choose
   **Edit Availability**
   .
4. Assign the extension to specific Regional user groups rather than the entire organization. This group-based deployment automatically routes your users to their correct Regional Amazon Quick account resources.

![Microsoft Teams admin center Manage Apps page showing two Amazon Quick app entries with "Unblocked" status, and Edit availability side panel open with "Specific users or groups" selected and MyCompany-group-eu-west-1 (1 member) configured.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image14.png)

5. Repeat the same process with the Microsoft Teams application in
   `us-east-1`
   Region.

The following screenshot shows what the configuration will look like in Microsoft Teams Admin Center.

![Microsoft Teams admin center Manage Apps search results showing two Amazon Quick app entries, both unblocked and available to 1 group, supported on multiple Microsoft platforms, published by Amazon.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image15.png)

After deployment propagates, you can validate that users are automatically routed to the correct Regional agent.

## Verify the implementation

EU users can use MyCompany-Teams-eu-west-1 agent when they are interacting with the Microsoft Teams extension. The plugin will select the
**My Assistant**
chat agent as default, so you must choose the settings (gear) icon and choose the
`MyCompany-Knowledge-Agent-eu-west-1 chat`
agent.

![Microsoft Teams admin center Manage Apps search results showing two Amazon Quick app entries, both unblocked and available to 1 group, supported on multiple Microsoft platforms, published by Amazon.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image15.png)

![Amazon Quick Settings dialog showing selected agent "MyCompany-Knowledge-Agent-eu-west-1", conversation scope set to "Agent's Associations", Web Search enabled, with Back, Save Default, and Save Current action buttons.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image18.png)

The following screenshot shows an example of interacting with the chat agent.

![Amazon Quick chat interface showing MyCompany-Knowledge-Agent-eu-west-1 active with Agent's Associations scope and Web Search enabled, displaying welcome message "Hello again! Welcome back" with thumbs up/down feedback buttons and New Chat option.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/06/ml-20253-image19.png)

US users can use the
`MyCompany-Knowledge-Agent-us-east-1`
chat agent, demonstrating successful Regional routing without manual configuration.

## Troubleshooting

The following tips can help you troubleshoot some common issues you might encounter while setting up Amazon Quick extensions:

* Quick extension does not show in Microsoft Teams:
  + Wait 24–48 hours for Microsoft 365 deployment propagation
  + Verify the user is in the correct Microsoft Entra ID group
  + Clear the Microsoft Office add-on cache and restart Teams
* Issues with authentication in Amazon Quick extension:
  + Verify the redirect URLs match exactly in Microsoft Entra ID
  + Check the trusted token issuer configuration
  + Confirm the IAM role trust relationship includes the correct service principal
* Wrong agent listed in the Amazon Quick extension:
  + Verify user group membership (should only be in one Regional group)
  + Check the manifest-to-group assignment in Microsoft 365 Admin Center
  + Have the user sign out and sign in again
* The agents drop-down list in the Amazon Quick extension is empty:
  + Validate the agent is shared with users on the Amazon Quick console
  + Verify the agent exists in the same AWS Region as the extension
  + Check agent permissions are set to at least User level

## Clean up

To avoid ongoing charges, clean up the resources you created as part of this post if you no longer need them.

## Conclusion

This multi-Region Amazon Quick extension solution for Microsoft 365 provides compliant, AWS Region-aware AI capabilities to your global workforce. The architecture and implementation steps in this post show how to integrate enterprise AI with productivity tools while maintaining data residency and compliance boundaries.

For more details on AI-powered assistants that enhance productivity without switching applications, refer to
[Extension access](https://docs.aws.amazon.com/quicksuite/latest/userguide/extension-access.html)
. Refer to
[Getting started with Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/getting-started.html)
to start using Amazon Quick today.

---

## About the authors

[“Ramón Díez Lejarazu”](https://www.linkedin.com/in/ramondiez/)
is an AI Strategist and Builder at Amazon Web Services who builds AI-powered solutions grounded in real business needs. He leads projects with the firm conviction that technology must solve actual problems for people and organizations.

[“Anneline Sibanda”](https://www.linkedin.com/in/anneline-s/)
is an AI Builder at Amazon Web Services, specializing in the architecture and delivery of agentic and generative AI solutions. She is a key technical partner for enterprises bridging the gap between innovative concepts and production-ready applications.

[“David Perez Caparrós”](https://www.linkedin.com/in/davidperezcaparros/)
is a Principal AI Strategist at Amazon Web Services, where he helps customers and industry partners design, deploy, and operate generative AI solutions on AWS. With over 15 years of experience, David has become a trusted advisor to organizations navigating their AI transformation journeys.