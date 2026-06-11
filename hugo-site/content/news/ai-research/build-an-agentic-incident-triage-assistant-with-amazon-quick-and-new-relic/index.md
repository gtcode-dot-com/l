---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-11T02:00:41.592183+00:00'
exported_at: '2026-06-11T02:00:42.982025+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/build-an-agentic-incident-triage-assistant-with-amazon-quick-and-new-relic
structured_data:
  about: []
  author: ''
  description: 'This post shows engineering teams how to apply that principle to one
    of the most time-sensitive workflows in engineering: incident triage. You will
    build a custom incident triage assistant agent using Amazon Quick that orchestrates
    a response with the New Relic Model Context Protocol (MCP) Server and Asana through
    n...'
  headline: Build an agentic incident triage assistant with Amazon Quick and New Relic
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/build-an-agentic-incident-triage-assistant-with-amazon-quick-and-new-relic
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Build an agentic incident triage assistant with Amazon Quick and New Relic
updated_at: '2026-06-11T02:00:41.592183+00:00'
url_hash: 1b8a1a3937467420f3242ff4170cb32080fd4760
---

Incident triage is time-sensitive because site reliability engineers (SREs) and support engineers often need to collect evidence, assess user impact, and create follow-up work across separate tools. With
[Amazon Quick](https://aws.amazon.com/quick/?trk=0ea79374-057c-4897-84f0-5fe792905a8f&amp;sc_channel=ps&amp;trk=10b9c297-8863-409e-9f2e-174496633033&amp;sc_channel=ps&amp;ef_id=CjwKCAjw2rrQBhBuEiwAarLWHW6nUthPqp8HtP8G-s1F4l5Tv34wvulNXQqzG7SIkkBo0hz7GjUzaxoCgfwQAvD_BwE:G:s&amp;s_kwcid=AL!4422!3!806967542617!e!!g!!amazon%20quick!23532473728!195603221991&amp;gad_campaignid=23532473728&amp;gbraid=0AAAAADjHtp9JUcIrM3z181nwI5FS4bw4Z&amp;gclid=CjwKCAjw2rrQBhBuEiwAarLWHW6nUthPqp8HtP8G-s1F4l5Tv34wvulNXQqzG7SIkkBo0hz7GjUzaxoCgfwQAvD_BwE)
and New Relic, you can coordinate those investigation and handoff steps in a single conversational workflow.

This post shows engineering teams how to apply that principle to one of the most time-sensitive workflows in engineering: incident triage. You will build a custom incident triage assistant agent using Amazon Quick that orchestrates a response with the
[New Relic Model Context Protocol (MCP) Server](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/)
and Asana through native integrations. From a single prompt, the Amazon Quick agent investigates the incident, assembles a root cause analysis (RCA) brief with evidence links, and creates a tracked Asana task ready for handoff.

For engineering leaders, reducing mean time to resolution (MTTR) is one way to drive better business impact. In internal testing using New Relic’s own applications, the agent reduced the evidence-gathering phase of incident triage. This led to faster resolution, lower risk of knowledge loss between engineering shifts, and a consistent investigation standard across the entire on-call rotation.

The incident triage assistant pattern in this post is one application of a broader capability in Amazon Quick: connecting enterprise tools to AI agents through native integrations.

## New Relic MCP Server integration for Amazon Quick overview

With Amazon Quick chat agents, you can explore data and take actions through open-ended conversations backed by connected
**action connectors**
, pre-built integrations that link Amazon Quick to external services.
[New Relic is a built-in connector in Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/newrelic-integration.html)
, providing access to its AI reasoning tools for incident response and performance analysis. Asana is another Amazon Quick built-in connector that supports task creation. The agent orchestrates both, producing an RCA brief and an Asana task from a single prompt. There are five New Relic reasoning tools the agent uses.

![Diagram of five New Relic reasoning tools available to the Amazon Quick chat agent](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-1.png)

These tools do the investigative work, and the agent decides which ones to call based on your prompt:

* **generate\_alert\_insights\_report**
  identifies key alert drivers.
* **generate\_user\_impact\_report**
  quantifies blast radius, including the number of users and services affected.
* **analyze\_entity\_logs**
  surfaces error signatures and exceptions.
* **analyze\_transactions**
  identifies slow or failing requests.
* **natural\_language\_to\_nrql\_query**
  converts plain-English questions into New Relic Query Language (NRQL) and runs them against your observability data.

The following image shows the end-to-end workflow from prompt to Asana task.

![End-to-end incident triage workflow diagram showing Amazon Quick orchestrating New Relic reasoning tools and creating an Asana task](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-2.png)

*Figure 1: Incident triage workflow using Amazon Quick, New Relic MCP Server, and Asana.*

The following implementation section walks through the full setup with screenshots. The following prompt is what an on-call engineer sends to start the investigation. Amazon Quick calls all five New Relic tools in one response, assembles the RCA brief, and then creates the Asana task:

*“Checkout is slow and we are seeing server errors on checkout-service in production. Check the last 24 hours. Generate RCA brief.”*

## Prerequisites

Before building the incident triage assistant, make sure that you have the required Amazon Quick, New Relic, and Asana access in place, including the permissions needed to create integrations, authenticate connectors, and configure task handoff.

* **Amazon Quick account.**
  A Professional subscription is required. You need Author permissions or higher to create integrations and chat agents. See
  [Amazon Quick pricing](https://aws.amazon.com/quick/pricing/)
  for current tier details.
* **New Relic account.**
  [The New Relic connector is built into Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/newrelic-integration.html)
  . You authenticate using your existing New Relic account credentials during connector setup.
* **Asana account.**
  A workspace containing a project named
  **SRE Incident Triage**
  . You need administrative access to create an OAuth application in the
  [Asana developer console](https://app.asana.com/0/my-apps)
  to obtain OAuth credentials.

## Implementation

In this section, you will set up the New Relic and Asana integrations, create the incident triage assistant in Amazon Quick, and test the end-to-end workflow from investigation to RCA brief to Asana task creation.

### Step 1: Set up the New Relic integration

[New Relic is available as a built-in connector](https://docs.aws.amazon.com/quick/latest/userguide/newrelic-integration.html)
in the Amazon Quick Integrations console. Navigate to
**Integrations**
and choose the
**Actions**
tab. Locate the New Relic tile (Figure 2) and choose the plus (+) icon to begin setup.

![New Relic tile in the Amazon Quick Integrations console with the plus icon to add the connector](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-3.png)

*Figure 2: New Relic tile in the Amazon Quick Integrations console.*

In the
**Create integration**
dialog (Figure 3), enter a name for the
**New Relic Integration**
and an optional description. Keep the connection type as
**Public network**
. The authentication method shows
**No additional credentials are needed**
at this stage. You authenticate with your New Relic account in a later step. Choose
**Create and continue**
, then choose
**Done**
.

![Create integration dialog in Amazon Quick configuring a New Relic MCP Server integration with public network connection](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-4.png)

*Figure 3: Creating the New Relic MCP Server integration in Amazon Quick.*

The integration now appears in the Existing actions panel with a status of Available (Figure 4). Choose the integration name to open its detail page.

![New Relic and Asana integrations listed as Available in the Existing actions panel of the Amazon Quick Integrations console](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-5.png)

*Figure 4: New Relic and Asana integrations listed as Available in the Amazon Quick Integrations console.*

The detail page shows the available New Relic actions and the connection details including the Base URL, Authorization URL, and Token URL (Figure 5). Choose
**Sign in**
and authenticate with your New Relic account credentials to activate the connection.

![New Relic MCP Server integration detail page in Amazon Quick listing available actions and the Sign in button to authenticate](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-6.png)

*Figure 5: New Relic MCP Server integration detail page showing available actions. Choose Sign in to authenticate with your New Relic account.*

### Step 2: Set up the Asana integration

The Asana connector uses OAuth 2.0. Before configuring it in Amazon Quick, create an OAuth application in the
[Asana developer console](https://app.asana.com/0/my-apps)
to obtain your Client ID and Client Secret. Then navigate to
**Integrations**
→
**Actions**
in Amazon Quick and select Asana. Enter the following values:

* **Base URL:**
  https://app.asana.com/api/1.0.
* **Authorization URL:**
  https://app.asana.com/-/oauth\_authorize.
* **Redirect URL:**
  Copy this value from the Amazon Quick configuration screen and paste it into your Asana OAuth app’s allowed redirect URLs before saving.
* **Client ID and Client Secret:**
  From your Asana OAuth application.

For full setup instructions, see
[Asana integration](https://docs.aws.amazon.com/quicksuite/latest/userguide/asana-integration.html)
in the Amazon Quick User Guide.

The integration now appears in the Existing actions panel with a status of
**Available**
.

![New Relic and Asana integrations listed as Available in the Existing actions panel after both connectors have been configured](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-5.png)

*Figure 6: New Relic and Asana integrations listed as Available in the Amazon Quick Integrations console.*

### Step 3: Create the Incident triage assistant chat agent

Navigate to
**Chat agents**
and choose
**Create chat agent**
. Give the agent a name and purpose, then replace the generated instructions with the following. For full setup steps, see
[Custom chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/custom-agents.html)
in the Amazon Quick User Guide.

In the
**Actions**
section of the agent builder, choose
**Link existing integration**
and add both the New Relic integration and the Asana integration you created in Steps 1 and 2. After linking, the available actions from each integration are accessible to the agent.

Replace the generated agent instructions with the following:

```
You are the Incident triage assistant.

Primary job
Help on-call engineers triage incidents using New Relic reasoning
tools. When the investigation is complete, create an Asana task
with the RCA brief.

How to respond
Keep responses concise and operational.
Do not guess. Use tool outputs as evidence.
If inputs are missing, ask for: service or entity name,
environment, and time window.

Default RCA brief format:
Summary (1-2 lines)
Blast radius
Likely trigger
Key evidence (bullets with links)
Recommended next actions (3 bullets)

Tool routing: New Relic investigation
alert fired, key drivers, signals changed -&gt; generate_alert_insights_report
blast radius, customer impact, users affected -&gt; generate_user_impact_report
logs, error signature, exceptions, anomalies -&gt; analyze_entity_logs
slow requests, latency, transactions -&gt; analyze_transactions
segmentation by region, version, endpoint -&gt; natural_language_to_nrql_query

Tool routing: output
After generating the RCA brief -&gt; create an Asana task.
Task fields: Name = incident title, Notes = full RCA brief with
evidence links, Due date = today, Tags = [sre-triage, incident].
Confirm the Asana project name with the user if not already known.

Output rules
If a tool call fails (permissions, timeout, missing entity),
state what failed and what input you need next.
Do not include PII, customer identifiers, user IDs, email addresses, IP addresses, session tokens, raw credentials, internal hostnames, infrastructure topology details, database connection strings, or environment variables in the RCA brief or Asana task notes.
```

### Step 4: Test the workflow

Open the Incident triage assistant from Amazon Quick and send the following prompt. The agent calls New Relic reasoning tools, assembles the RCA brief, and asks you to confirm before creating the Asana task.

“Checkout is slow and we are seeing server errors on checkout-service in production. Check the last 24 hours. Generate RCA brief.”

The following image shows the agent calling New Relic reasoning tools in sequence before assembling the RCA brief.

![Incident triage agent in Amazon Quick calling New Relic reasoning tools in sequence from a single user prompt](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-8.png)

*Figure 7: The Incident triage agent calling New Relic reasoning tools from a single prompt.*

The following image shows the full RCA brief, including summary, blast radius, likely trigger, key evidence with links back to New Relic, and three recommended next actions.

![Generated RCA brief in the Amazon Quick chat showing summary, blast radius, likely trigger, evidence links, and recommended next actions for the checkout-service incident](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-9.png)

*Figure 8: RCA brief generated by the Incident triage agent for the checkout-service incident.*

When the agent asks to confirm the Asana project, reply: “Yes, create an Asana task in project SRE Incident Triage with this RCA brief.”

![Asana task created by the incident triage agent in the SRE Incident Triage project containing the RCA brief and evidence links](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/04/ML-20579-10.png)

*Figure 9: Asana task created by the Incident triage agent in the SRE Incident Triage project.*

## Security and governance considerations

Before sharing the agent with your on-call rotation, address the following:

* **Least privilege for New Relic.**
  The New Relic connector runs with the permissions of your authenticated account. Use a dedicated service account with the New Relic standard Read only role, or a custom role limited to the application performance monitoring (APM), logs, alerts, entities, and NRQL read or query access required for the triage actions. Do not use full admin credentials.
* **Asana permission scoping.**
  Use a dedicated Asana service account with create-task access limited to the SRE Incident Triage project. Verify your OAuth app scopes include only what the agent requires: tasks:write, tasks:read, projects:read, and workspaces:read.
* Treat Asana task notes as a handoff summary, not a raw incident data export. Don’t include personally identifiable information (PII), customer identifiers, user IDs, email addresses, IP addresses, session tokens, internal hostnames, infrastructure topology details, database connection strings, environment variables, or raw credentials in Asana tasks.
* **Credential storage.**
  Rotate New Relic and Asana OAuth credentials according to your organization’s key rotation policy.
* **Audit logging.**
  Amazon Quick logs the action connector invocations.

## Clean up resources

If you built this solution as a prototype, remove the following resources to avoid ongoing charges:

1. In Amazon Quick, delete the
   **custom**
   chat agent.
2. In Amazon Quick, delete the
   **New Relic Integration**
   and
   **Asana Integration**
   connectors.
3. In the Asana developer console, revoke the OAuth application credentials created for this integration.
4. Rotate or delete any test credentials used during setup, following your organization’s security policy.

## Conclusion

In this post, we showed you how to build an agentic incident triage agent using Amazon Quick that connects to the New Relic MCP Server and Asana through native integrations. From a single prompt, the agent calls five New Relic reasoning tools, assembles a root cause analysis brief with evidence links, and creates a tracked Asana task ready for handoff.

The agent removes the manual coordination between your observability system and your tracking system. Every investigation produces a consistent RCA format, regardless of who is on call, making shift handoffs faster and post-mortems more straightforward to run.

To get started, follow the
[New Relic integration for Amazon Quick article](https://docs.aws.amazon.com/quick/latest/userguide/newrelic-integration.html)
, and the
[Amazon Quick User Guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/)
. We encourage you to explore the solution and adapt it for your environment.

---

## About the authors

### Ebbey Thomas

[Ebbey](https://www.linkedin.com/in/ebbeythomas/)
is a Senior Generative AI Specialist Solutions Architect at AWS. He works with customers to identify practical use cases for AI agents and turn them into production-grade generative AI solutions. Ebbey holds a BS in Computer Engineering and an MS in Information Management from Syracuse University. Outside of work, he enjoys coffee, the outdoors, workouts, road trips, and spending time with his family.

### Muthuvelan Swaminathan

[Muthuvelan](https://www.linkedin.com/in/muthuvelan-swaminathan-0863834/)
is a Principal Partner Architect at New Relic partnership organization building technical integrations with leading cloud providers and strategic partners. Through partner enablement, solution engineering and ecosystem alignment Muthuvelan helps drive product innovation at New Relic to ensure enterprises eliminate disruptions in their digital experiences for their customers.