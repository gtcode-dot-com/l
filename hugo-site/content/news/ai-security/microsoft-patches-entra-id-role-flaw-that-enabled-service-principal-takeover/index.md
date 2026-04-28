---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-28T08:15:14.066892+00:00'
exported_at: '2026-04-28T08:15:16.484402+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/microsoft-patches-entra-id-role-flaw.html
structured_data:
  about: []
  author: ''
  description: Agent ID Administrator enabled service principal takeover before April
    9, 2026 patch, exposing privilege escalation risk in Entra ID tenants.
  headline: Microsoft Patches Entra ID Role Flaw That Enabled Service Principal Takeover
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/microsoft-patches-entra-id-role-flaw.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patches Entra ID Role Flaw That Enabled Service Principal Takeover
updated_at: '2026-04-28T08:15:14.066892+00:00'
url_hash: 7d44ce82c7b22166f27b91c51fe615f4b855798b
---

**

Ravie Lakshmanan
**

Apr 28, 2026

Vulnerability / Identity Management

An administrative role meant for artificial intelligence (AI) agents within Microsoft Entra ID could enable privilege escalation and identity takeover attacks, according to new findings from
**Silverfort**
.

[Agent ID Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
is a privileged built-in role introduced by Microsoft as part of its
[agent identity platform](https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform)
to handle all aspects of an AI agent's identity lifecycle operations in a tenant. The platform enables AI agents to authenticate securely and access necessary resources, as well as discover other agents.

However, the shortcoming discovered by the identity security platform meant that users assigned the Agent ID Administrator role could take over arbitrary
[service principals](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals)
, including those beyond agent-related identities, by becoming an owner and then add their own credentials to authenticate as that principal.

"That's full service principal takeover," security researcher Noa Ariel
[said](https://www.silverfort.com/blog/agent-id-administrator-scope-overreach-service-principal-takeover-in-entra-id/)
. "In tenants where high-privileged service principals exist, it becomes a privilege escalation path."

This ownership of a service principal effectively opens the door to an attacker to operate within the scope of its existing permissions. If the targeted service principal holds elevated permissions – particularly privileged directory roles and high-impact Graph app permissions – it can give an attacker broader control over the tenant.

VIDEO

Following responsible disclosure on March 1, 2026, Microsoft rolled out a patch across all cloud environments to remediate the scope overreach on April 9. Following the fix, any attempt to assign ownership over non-agent service principals using the Agent ID Administrator role is now blocked, and leads to a "Forbidden" error message being displayed.

Silverfort noted that the architectural issue highlights the need for validating how roles are scoped and permissions are applied, especially when it comes to shared identity components and new identity types are built on top of the foundations of existing primitives.

To mitigate the threat posed by this risk, organizations are advised to monitor sensitive role usage, particularly those related to service principal ownership or credential changes, track service principal ownership changes, secure privileged service principals, and audit credential creation on service principals.

"Agent identities are part of the broader shift toward non-human identities, built for the age of AI agents," Ariel noted. "When role permissions are applied on top of shared foundations without strict scoping, access can extend beyond what was originally intended. In this case, that gap led to broader access, especially when privileged service principals were involved."

"Additionally, the overall risk is influenced by tenant posture, particularly around privileged service principals, where ownership abuse remains a well-known and impactful attack path."