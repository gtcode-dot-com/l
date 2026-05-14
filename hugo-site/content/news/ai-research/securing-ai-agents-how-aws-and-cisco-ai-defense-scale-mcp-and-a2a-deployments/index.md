---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-14T21:15:03.677063+00:00'
exported_at: '2026-05-14T21:15:06.252256+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-how-aws-and-cisco-ai-defense-scale-mcp-and-a2a-deployments
structured_data:
  about: []
  author: ''
  description: 'The Cisco and AWS partnership addresses three challenges enterprises
    face when scaling AI agents: visibility gaps, security bottlenecks, and compliance
    risks. In this post, we explore how you can overcome AI security challenges through
    automated scanning and unified governance.'
  headline: 'Securing AI agents: How AWS and Cisco AI Defense scale MCP and A2A deployments'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-how-aws-and-cisco-ai-defense-scale-mcp-and-a2a-deployments
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Securing AI agents: How AWS and Cisco AI Defense scale MCP and A2A deployments'
updated_at: '2026-05-14T21:15:03.677063+00:00'
url_hash: ae37497e00efbf5bcf3756aa18525fe7cc2392a6
---

[Model Context Protocol](https://modelcontextprotocol.io/)
(MCP) adoption has accelerated rapidly since its introduction in November 2024. Enterprises now manage dozens to hundreds of MCP servers—tools that extend AI agent capabilities by connecting them to external data sources and APIs. The
[Agent-to-Agent (A2A) Protocol](https://a2a-protocol.org/latest/specification/)
followed in April 2025, enabling autonomous agents to communicate directly without human intervention. More recently,
[Agent Skills](https://agentskills.io/home)
emerged across enterprise infrastructure. This growth has created three security gaps: teams lack visibility into which tools and agents are deployed, manual security reviews can’t scale to match deployment velocity, and compliance frameworks require audit trails that don’t exist for autonomous AI agents.

Organizations face risks from unvetted MCP servers, A2A agents, and Skills: inadvertent access to sensitive data systems, compliance violations under SOX and GDPR frameworks that can result in regulatory penalties, and operational disruptions when vulnerable tools or malicious agents are discovered post-deployment. Security teams report that manual review processes can add several weeks to each AI application deployment, creating a backlog that grows as AI adoption accelerates. Audit failures from incomplete tool and agent tracking create regulatory exposure that compliance teams struggle to quantify.

The Cisco and AWS partnership addresses three challenges enterprises face when scaling AI agents: visibility gaps, security bottlenecks, and compliance risks. In this post, we explore how you can overcome AI security challenges through automated scanning and unified governance.

## Enterprise challenges and how Cisco and AWS address them

Through strategic collaboration, AWS and
[Cisco AI Defense](https://www.cisco.com/site/us/en/products/security/ai-defense/index.html)
provide comprehensive, automated security scanning for every MCP server, AI agent, and Agent Skill in the enterprise.
[AI Registry](https://github.com/agentic-community/mcp-gateway-registry)
, an AWS-backed open-source project, integrates with Cisco AI Defense to bring:

### Tool sprawl and visibility

Organizations deploying MCP servers and AI agents face a fundamental visibility challenge. Teams often add servers and agents ad-hoc across cloud and on-premises infrastructure, making it nearly impossible for security teams to maintain oversight. With dozens or even hundreds of tools and agents running without centralized governance, organizations lose visibility into what tools are available, which agents are communicating with each other, who’s using them, and whether they pose security risks.

The
[AI Registry](https://github.com/agentic-community/mcp-gateway-registry)
solves this through unified registration and discovery. Every MCP server, AI agent and Skill is registered in a single control plane, providing complete visibility. Beyond visibility, Cisco AI Defense integration provides added protection.

### Supply chain security at scale

Third-party MCP servers and A2A agents can contain vulnerabilities, malicious code, or insecure patterns that manual review can’t catch at scale. When a new server or agent is added to the registry, security scanning happens automatically before an AI component can access it. The scanner analyzes each MCP tool and A2A agent card and Agent Skill, generating detailed security reports. If issues are found, the component is automatically marked as disabled with a security-pending tag, requiring administrator review before granting access. This applies equally whether you’re registering an MCP server that provides database access, or an A2A agent that orchestrates multi-step workflows across your infrastructure.

> *“Security is a foundational requirement for enterprise AI adoption. By partnering with AWS on the AI Registry, Cisco AI Defense helps customers achieve comprehensive visibility and protection across their entire MCP server and agent ecosystems. The ability to scan open registries allows even small organizations to benefit from enterprise-grade security intelligence.”*
>
> *– Akshay Bhargava, VP of AI Product, AI Software and Platform at Cisco.*

### Compliance and security review bottlenecks

Security reviews traditionally create deployment bottlenecks, slowing agent rollout. Automated scanning with human review (in case of security vulnerabilities being found) enables self-service onboarding with built-in security guardrails. This transforms a manual, slow process into an automated one that helps with faster onboarding of new MCP servers, agents, and Skills.

> *“The partnership between AWS and Cisco AI Defense demonstrates how open collaboration accelerates enterprise innovation. The MCP Gateway Registry provides teams with a unified control plane for both agent and server governance, while Cisco’s scanning capabilities bring production-ready security to the MCP environment. This is exactly how we help customers build AI responsibly at scale.”*
>
> – Mahdi Sajjadpour, Director for Solution Architecture at Amazon Web Services.

With these enterprise challenges in mind, the following sections describe the technical implementation. Understanding how the scanning works will help you choose the right approach for your organization’s security posture.

## Unified security across MCP and A2A protocols

The AI Registry serves as a central control plane where MCP servers, AI agents and Skills are registered and discovered from, providing complete visibility across your AI infrastructure. These AI assets undergo security scanning workflows to maintain comprehensive protection across your entire agentic AI landscape.

When organizations register an MCP server with the Registry, the Cisco AI Defense MCP Scanner performs deep analysis of tool descriptions and schema. Similarly, when registering A2A agents, the Cisco AI Defense A2A Scanner analyzes agent capability declarations, agent skill definitions, and communication patterns. Similar scanning capabilities exist for AI Agent Skills through a Skills scanner that detects prompt injection, data exfiltration, and malicious code patterns. This approach makes sure that whether your AI infrastructure uses traditional tool access (MCP), autonomous agent collaboration (A2A), or Skills (via AI coding assistants for example), security scanning happens automatically before components become operational.

The following diagram shows a high-level overview of the security scanning and registration process. The scanning process can be initiated on demand to scan individual MCP servers and Agents or the entire Registry. Organizations typically configure a standalone Cron job that uses the Registry API to periodically scan the entire Registry and track vulnerabilities through their existing ticket management systems. The Registry also supports on-demand scanning of individual MCP servers, Agents and Skills. The results of the scans are stored inside the datastore in the Registry and are available for viewing on the Registry UI as well as retrievable via a Registry API.

![Architecture diagram showing the security scanning and registration process with AI Registry, Cisco AI Defense scanners, and vulnerability tracking](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/05/08/ML-20700-1.png)

Fig 1: Security scanning and registration process

An organization’s security posture is strengthened through multiple available scanning approaches that apply uniformly to both MCP, A2A agents and Skills:
[**YARA Analyzer**](https://virustotal.github.io/yara/)
for fast pattern-based detection of known threats like SQL injection, command injection, and hardcoded credentials;
**LLM Analyzer**
for AI-powered semantic analysis using frontier models available through
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
that examines tool logic, agent behavior, and capability declarations to identify sophisticated and novel threats; and
**Cisco AI Defense Proprietary Scanners**
—including the MCP Scanner, A2A Scanner and Skills Scanner—for advanced threat detection combining extensive threat intelligence with deep code analysis. The A2A Scanner specifically analyzes agent card metadata to detect supply-chain threats such as identity spoofing, prompt injection in metadata fields, hardcoded credentials, data exfiltration endpoints, and SSRF patterns. It also checks for A2A spec compliance violations and maps the findings to severity levels from LOW to CRITICAL.

When issues are detected, the system automatically disables vulnerable assets with detailed security reports, requiring administrator review before granting access. Security scanning integrates into your development workflows (CI/CD integration) as part of registering new servers and agents into the AI Registry, while maintaining complete security audit history for regulatory requirements like SOX and GDPR.

The following screenshot shows an MCP server for which security vulnerabilities were detected. Notice the red shield icon and disabled state of the server.

![Fig 2: MCP server with security vulnerabilities were detected](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/05/11/ml-20700-imagenew.png)

Fig 2: MCP server with security vulnerabilities were detected

These capabilities translate into concrete solutions for the specific challenges your teams face daily. The following sections examine how this partnership addresses scenarios you’re likely encountering right now.

## Open architecture and integration

The AI Registry is built on open standards and APIs, creating an environment where you and multiple parties benefit from unified security scanning: If you’re a
**Cisco AI Defense customer and AWS customer**
you can query the AI registry via its REST API to discover available MCP servers and agents, supporting programmatic threat detection at scale. This is a pattern that central IT teams in an organization can use to secure their AI assets hosted on AWS.

The registry uses the same REST API specification as Anthropic’s official MCP Registry, to support broad compatibility across the MCP environments and to support federation with other MCP deployments.

## Downstream workflow integration

Customers can integrate security scanning with existing enterprise workflows:

* Automatic ticket creation in ServiceNow for servers or agents with issues, triggering issue response processes
* Real-time Slack notifications alert teams immediately when high-severity findings are detected
* Issue data forwarded to Security Incident and Event Management (SIEM) systems like Splunk or Datadog for correlation with other security events
* Summary reports through compliance dashboards for audit readiness.

## Getting started

The following sections describe how to get started with the AI Registry and Cisco AI Defense integration depending on your current environment.

### For AWS customers

AWS customers can deploy the AI Registry and configure Cisco AI Defense MCP Scanner integration to add security scanning to their AI assets onboarding workflow. After configuration, you can monitor vulnerabilities on the Registry console as shown in the preceding screenshots.

The complete setup guide is available at:
[Security Scanner setup guide on GitHub](https://github.com/agentic-community/mcp-gateway-registry/blob/main/docs/security-scanner.md)

In addition to the integration with the open-source AI Registry, you can use Cisco AI Defense in CI/CD workflows to evaluate AI assets before registering them in the
[AWS Agent Registry](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
, a fully managed discovery service that provides a centralized catalog for organizing, curating, and discovering resources across an organization. This approach allows teams to assess MCP servers, tools, agents, agent skills, and custom resources prior to publication in the registry and before those assets are made available through approval workflows and semantic or keyword-based discovery. This
[code sample](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/10-Agent-Registry/01-advanced/admin-approval-workflow)
provides an example of the integration of Cisco AI Defense (OSS version) with AWS Agent Registry on the official AWS labs repo.

### For Cisco AI Defense customers

Cisco AI Defense customers can configure the MCP Scanner to target their organization’s registry, discover available MCP servers and agents through the registry API, generate comprehensive security reports, and integrate findings into existing security workflows.

For the full product capabilities, see the
[Cisco AI Defense documentation](https://securitydocs.cisco.com/docs/ai-def/user/168859.dita)
.

## Conclusion

In this post, we explored how the partnership between AWS and Cisco AI Defense provides automated security scanning for MCP servers, A2A agents, and Agent Skills across the enterprise. By combining the AI Registry’s centralized governance with Cisco AI Defense’s scanning capabilities, you can gain visibility into your AI infrastructure, enforce security policies at scale, and maintain compliance audit trails.

To get started, deploy the
[AI Registry](https://github.com/agentic-community/mcp-gateway-registry)
and configure the Cisco AI Defense scanner integration. For questions or feedback, leave a comment on this post.

---

## About the authors

### Amit Arora

Amit Arora is a Principal AI and ML Specialist Architect at Amazon Web Services, helping enterprise customers use cloud-based machine learning services to rapidly scale their innovations. He is also an adjunct lecturer in the MS data science and analytics program at Georgetown University in Washington, D.C.

### Arjun Sambamoorthy

Arjun Sambamoorthy is Senior Director of AI Engineering and Research in the AI Software and Platform group at Cisco, where he heads R&D for Cisco AI Defense. He co-founded Armorblox, an email security company acquired by Cisco in 2023. With 18+ years in cybersecurity spanning Netskope, Juniper Networks, and Sipera Systems, Arjun brings deep expertise in AI-driven security and platform engineering.

### Shweta Keshavanarayana

Shweta Keshavanarayana is a Senior Customer Solutions Manager at AWS. She works with AWS Strategic Customers and helps them in their cloud migration and modernization journey. Outside of work, she volunteers as a team manager for her sons’ U9 cricket team.