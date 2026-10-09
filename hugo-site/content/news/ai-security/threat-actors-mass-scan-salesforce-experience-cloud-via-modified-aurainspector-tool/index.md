---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T08:15:14.389195+00:00'
exported_at: '2026-03-10T08:15:16.894972+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/threat-actors-mass-scan-salesforce.html
structured_data:
  about: []
  author: ''
  description: Modified AuraInspector scans misconfigured Salesforce Experience Cloud
    sites, extracting CRM data and enabling targeted vishing campaigns.
  headline: Threat Actors Mass-Scan Salesforce Experience Cloud via Modified AuraInspector
    Tool
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/threat-actors-mass-scan-salesforce.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Threat Actors Mass-Scan Salesforce Experience Cloud via Modified AuraInspector
  Tool
updated_at: '2026-03-10T08:15:14.389195+00:00'
url_hash: cbbebe12213342a9309841dca4293e023cf723cb
---

**

Ravie Lakshmanan
**

Mar 10, 2026

Cloud Security / API Security

Salesforce has warned of an increase in threat actor activity that's aimed at exploiting misconfigurations in publicly accessible Experience Cloud sites by making use of a customized version of an open-source tool called AuraInspector.

The activity, per the company, involves the exploitation of customers'
[overly permissive Experience Cloud guest user configurations](https://www.salesforce.com/blog/misconfiguration-mistakes/)
to obtain access to sensitive data.

"Evidence indicates the threat actor is leveraging a modified version of the open-source tool AuraInspector [...] to perform mass scanning of public-facing Experience Cloud sites," Salesforce
[said](https://www.salesforce.com/blog/protecting-your-data-essential-actions-to-secure-experience-cloud-guest-user-access/)
.

"While the original AuraInspector is limited to identifying vulnerable objects by probing API endpoints that these sites expose (specifically the /s/sfsites/aura endpoint), the actor has developed a custom version of the tool capable of going beyond identification to actually extract data — exploiting overly permissive guest user settings."

[AuraInspector](https://thehackernews.com/2026/01/threatsday-bulletin-ai-voice-cloning.html#salesforce-audit-tool)
refers to an open-source tool designed to help security teams identify and audit access control misconfigurations within the Salesforce Aura framework. It was released by Google-owned Mandiant in January 2026.

Publicly accessible Salesforce sites use a dedicated guest user profile that enables an unauthenticated user to access landing pages, FAQs, and knowledge articles. However, if this profile is misconfigured with excessive permissions, it can potentially grant unauthenticated users access to more data than intended.

As a result, an attacker could exploit this security weakness to directly query Salesforce CRM objects without logging in. For this attack to work, two conditions have to be satisfied by Experience Cloud customers: they are using the guest user profile and have not adhered to Salesforce's recommended configuration guidance.

"At this time, we have not identified any vulnerability inherent to the Salesforce platform associated with this activity," Salesforce
[said](https://status.salesforce.com/generalmessages/20000244?locale=en-US)
. "These attempts are focused on customer configuration settings that, if not properly secured, may increase exposure."

The company attributed the campaign to a known threat actor group without taking its name, raising the possibility that it could be the work of ShinyHunters (aka UNC6240), which has a history of targeting Salesforce environments via third-party applications from
[Salesloft](https://thehackernews.com/2025/09/github-account-compromise-led-to.html)
and
[Gainsight](https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html)
.

Salesforce is recommending customers review their Experience Cloud guest user settings, ensure the Default External Access for all objects is set to Private, disable guest users' access to public APIs, restrict visibility settings to prevent guest users from enumerating internal organization members, disable self-registration if not required, and monitor logs for unusual queries.

"This threat actor activity reflects a broader trend of '
[identity-based](https://www.salesforce.com/blog/protecting-salesforce-data-after-an-identity-compromise/)
' targeting," it added. "Data harvested in these scans, such as names and phone numbers – is often used to build follow-on targeted social engineering and 'vishing' (voice phishing) campaigns."