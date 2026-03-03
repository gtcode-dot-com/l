---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T20:07:52.591293+00:00'
exported_at: '2026-03-03T20:07:56.038182+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-tines-enhances-security-analysis-with-amazon-quick-suite
structured_data:
  about: []
  author: ''
  description: In this post, we show you how to connect Quick Suite with Tines to
    securely retrieve, analyze, and visualize enterprise data from any security or
    IT system. We walk through an example that uses a MCP server in Tines to retrieve
    data from various tools, such as AWS CloudTrail, Okta, and VirusTotal, to remediate
    secur...
  headline: How Tines enhances security analysis with Amazon Quick Suite
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-tines-enhances-security-analysis-with-amazon-quick-suite
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How Tines enhances security analysis with Amazon Quick Suite
updated_at: '2026-03-03T20:07:52.591293+00:00'
url_hash: 21972139aca16f99d8cd1cbe41263b68ca603dad
---

Organizations face challenges in quickly detecting and responding to user account security events, such as repeated login attempts from unusual locations. Although security data exists across multiple applications, manually correlating information and making corrective actions often delays effective response. With
[Amazon Quick Suite](https://aws.amazon.com/quicksuite/)
and
[Tines](https://www.tines.com/)
, you can automate the investigation and remediation process by integrating data from multiple security tools, and providing visual insights for faster decision-making.

Quick Suite is a digital workspace that provides business users agentic AI capabilities to quickly answer questions and turn insights into actions. Quick Suite brings AI-powered research, business intelligence (BI), and automation into a single application. You can build automated workflows where multiple AI assistants work together, using your company data and the internet to answer business questions faster and more accurately. Users connect additional applications to Quick Suite using built-in integrations and the Model Context Protocol (MCP), a protocol that standardizes how AI assistants communicate with external tools. Tines is an intelligent workflow platform with a built-in MCP Server Builder. An MCP server is a program that exposes an application’s capabilities through a standard protocol so AI assistants can call them as tools. In Tines, you define MCP tools that read from or write to your internal or third-party applications, and Quick Suite can query those tools directly. With full audit trails in Tines, customers maintain visibility and governance across every workflow. This pattern enables Quick Suite users to bring proprietary or siloed data into their AI-driven analysis workflows without deploying new infrastructure or writing custom integration code.

In this post, we show you how to connect Quick Suite with Tines to securely retrieve, analyze, and visualize enterprise data from any security or IT system. We walk through an example that uses a MCP server in Tines to retrieve data from various tools, such as
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
,
[Okta](https://www.okta.com/)
, and
[VirusTotal](https://www.virustotal.com/)
, to remediate security events using Quick Suite.

## Use case: Orchestrated security investigation and remediation

As a member of a security team, you stay ahead of security events with regular account security data review. This involves triaging information from multiple sources to determine if there are indicators that signal the need to dive more deeply into the data. With Quick Suite and Tines, you can investigate and remediate security events using natural language. This integrated approach leads to faster decision-making, without requiring custom scripts or manual correlation across multiple security applications.

Once connected to Quick Suite as well as your security and IT tools, Tines can:

* Analyze internet protocol (IP) addresses in VirusTotal to assess event risk
* Retrieve account details from Okta and BambooHR
* Review authentication logs and user activity in CloudTrail
* Flag suspicious IP addresses and, after analyst approval, block them in CrowdStrike

In Quick Suite, you can then visualize this data to gain immediate insights such as:

* Geographic mapping of login attempts with risk scoring
* Timeline of user activity before and after suspicious logins
* Correlation between accounts and affected systems
* Remediation status tracking for security events

This enables you to ask natural language questions, for example:

* Show all login attempts from high-risk countries in the last 24 hours
* Display user activity timeline
* List all systems the user accessed
* Generate a report of remediation actions taken for the security event

Explore additional use cases in the
[Tines story library](https://www.tines.com/library/)
.

## Solution overview

Tines can help you integrate with services that expose an API, automate retrieval or transformation of that data, and provide the resulting workflow as an MCP server. The MCP client in Quick Suite can connect directly to the Tines MCP server and access the tools defined within the server.

This pattern provides the following benefits:

* A simple, governed integration layer between Quick Suite and internal or external tools
* The ability to connect systems that don’t currently have an MCP server
* A straightforward and powerful way to create new MCP tools for custom data sources without custom engineering or development work
* Consistent, secure connectivity without maintaining custom scripts or servers

For Quick Suite customers, the result is faster insight and less manual effort, with built-in control over how Quick Suite connects to enterprise data sources.

The workflow consists of four components:

* **Quick Suite**
  – Connects to the Tines MCP server using the Quick Suite MCP client, retrieves the data, and enables analysis through chat and dashboards
* **Tines MCP Server**
  – A published endpoint that exposes the workflow as an MCP tool
* **Security or IT API**
  – Any REST API that returns network, endpoint, asset, or configuration data
* **Tines workflow**
  – A sequence of actions that retrieves, normalizes, or enriches this data

The following diagram illustrates this architecture.

![Data flow diagram showing AWS Security Intelligence Platform architecture with Security Analyst using Amazon QuickSuite and Tines to query and analyze security threats across multiple integrated security tools including AWS CloudTrail, Security Hub, CrowdStrike, VirusTotal, Okta, and BambooHR.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-1.png)

## Prerequisites

To deploy this solution, you must have the following:

* A Quick Suite account within your AWS account with a Professional subscription and an Author, or higher, user role. Refer to
  [Model Context Protocol (MCP) integration](https://docs.aws.amazon.com/quicksuite/latest/userguide/mcp-integration.html)
  for more information.
* A Tines tenant. All plans, including the free Community Edition, support creating MCP servers
* API credentials for the chosen security or IT system.

## Create MCP server in Tines

You can import an MCP server from the
[Tines story library](https://www.tines.com/library/stories/1324549)
into your Tines tenant. Alternatively, complete the following steps to create a custom MCP server in Tines:

1. Create a new Story.

![Demo application Stories section empty state interface with navigation menu and create new story button](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-2.png)

2. Open the Templates browser and search for MCP.

![This screenshot displays the AWS Quick Suite workflow automation configuration interface within a demo environment. The interface features a three-panel layout designed for building, searching, and configuring automated workflows with various integration tools.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-3.png)

3. Drag the MCP action to the storyboard.

![AWS Quick Suite workflow builder interface showing integration modules including Webhook, HTTP Request, Email, AI Agent, and other automation tools with a central template selection area](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-4.png)

4. Choose
   **MCP Server**
   in the right pane and note the MCP server URL to connect Quick Suite.

![This screenshot displays the AWS Quick Suite workflow builder interface, showing the configuration panel for integrating an MCP (Model Context Protocol) Server into an automated workflow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-5.png)

5. Add as many tools as required for your workflow from the list of templates, or configure your own custom tools.

![AWS Quick Suite interface showing MCP Server configuration with workflow tools, access control settings, and AWS CLI integration.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-6.png)

6. Connect the tools with your account in the associated applications using standard authentication methods (such as API key or OAuth).

![AWS Quick Suite workflow builder interface showing integration tools grid on left (Webhook, HTTP Request, Email tools, AI Agent, Event Transform, Trigger, Send to Story), MCP Server component in center connected to "Run AWS CLI command" action, and configuration panel on right displaying AWS CLI setup with "Not connected" status and "Connect to AWS CLI" button.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-7.png)

The following screenshot shows a custom MCP server example for user account security analysis and remediation.

![Tines MCP Server integration card for QuickSuite showing available security automation actions including case management, threat intelligence reports, email reputation checks, Okta log searches, and user lookup across multiple platforms](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-8.png)

## Connect Quick Suite to Tines MCP server

Complete the following steps to connect Quick Suite to the Tines MCP server:

1. On the Quick Suite console, choose
   **Integrations**
   under
   **Connections**
   in the navigation pane.
2. Choose the
   **Actions**
   tab under
   **Existing integrations**
   .
3. Choose the plus sign next to
   **Model Context Protocol.**

![Amazon QuickSuite integrations dashboard displaying the Actions tab with a list of available MCP integrations, their status, visibility settings, owners, and last modification dates for security workflow automation](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-9.png)

4. On the
   **Create integration**
   page, enter a name and description for your Tines integration.
5. For
   **MCP server endpoint**
   , enter the MCP server URL from your MCP server in your Tines story, then choose
   **Next**
   .

![Create integration dialog for Tines Triage MCP in QuickSuite, showing configuration fields for integration name, description, MCP server endpoint URL, and auto-publishing settings to enable security case automation](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-10.png)

6. On the next page, configure the authentication settings and choose
   **Create and continue**
   to see the tools from your Tines MCP server.
7. Choose
   **Next**
   to complete the connection.

![Tines Triage MCP integration summary page displaying connection details, enabled actions for security case analysis and remediation, including threat intelligence lookups, AWS CloudTrail log searches, and multi-platform user investigations](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-20134-image-11.png)

## Query and visualize data in Quick Suite

After you’re connected, you can use the Quick Suite chat assistant to retrieve and explore data in real time, generate visual dashboards and charts from the returned results, and combine this data with existing AWS datasets for broader analysis. Quick Suite automatically selects and retrieves data from your Tines integration based on the content of the chat messages. This gives you a simple and scalable way to operationalize security and IT data using the BI and AI capabilities in Quick Suite. The following screenshot shows a sample security query.

![Security incident investigation showing a comprehensive timeline analysis of a sophisticated multi-phase cyberattack, detailing reconnaissance, credential compromise, data exfiltration, and persistence tactics with critical security findings](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/Screenshot-2026-02-17-at-9.54.25%E2%80%AFp.m..png)

The following screenshot shows the query result, including a security event timeline graph.

![Interactive security incident timeline visualization displaying attack progression from IP [IP_ADDRESS], showing data breach activities including S3 bucket enumeration, sensitive file downloads, and ACL modifications with detailed activity timestamps and impact assessment](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/Screenshot-2026-02-17-at-9.55.59%E2%80%AFp.m..png)

## Clean up

To avoid incurring ongoing charges, clean up the resources you created as part of this solution.

## Conclusion

Connecting Quick Suite and Tines using MCP transforms how organizations analyze their security and IT data. This solution reduces the need for custom integration code and provides centralized governance of integrations, standardized data retrieval, and improved operational visibility. Security and IT teams can extend their analytics capabilities to any API-enabled system through a single, auditable layer that scales across their tooling landscape.

[Get Started with Quick Suite](https://aws.amazon.com/quicksuite/getting-started/)
to create a Quick Suite instance in your AWS account and visit the
[Tines home page](https://www.tines.com/)
to sign up for a Tines Community Edition account. Once you have access, you can create your first MCP server and connect your existing security and IT tools using the Tines prebuilt templates. Finally, configure Quick Suite to access your new data sources and start analyzing data through natural language queries.

For more details, refer to the
[Amazon Quick Suite User Guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/what-is.html)
and
[Tines MCP server documentation](https://www.tines.com/docs/actions/templates/mcp-server/)
.

---

### About the Authors

### Yannick Gloster

**Yannick Gloster**
is a Software Engineer based in Dublin, Ireland, originally from Santa Barbara, California. He works on AI features and infrastructure at Tines, building Workbench, AI agents, and scalable AI infrastructure for the platform powering the world’s most important workflows. Yannick has a master’s degree in computer science from Trinity College Dublin, Ireland. In his spare time, he enjoys sailing, playing Counter-Strike and Deadlock, and watching Formula 1.

### Jonah Craig

**Jonah Craig**
is a Startup Solutions Architect based in Dublin, Ireland. He works with startup customers across the UK and Ireland and focuses on developing AI/ML and generative AI solutions. Jonah has a master’s degree in computer science and regularly speaks on stage at AWS conferences, such as the annual AWS London Summit and the AWS Dublin Cloud Day. In his spare time, he enjoys creating music and releasing it on Spotify.

### Ashok Mahajan

**Ashok Mahajan**
is a Senior Solutions Architect at Amazon Web Services. Based in the NYC Metropolitan area, Ashok is a part of Global Startup team focusing on Security Startups and helps them design and develop secure, scalable, and innovative solutions and architecture using the breadth and depth of AWS services and their features to deliver measurable business outcomes.

### Bobby Williams

**Bobby Williams**
is a Senior Solutions Architect at AWS. He has decades of experience designing, building, and supporting enterprise software solutions that scale globally. He works on solutions across industry verticals and horizontals and is driven to create a delightful experience for every customer.