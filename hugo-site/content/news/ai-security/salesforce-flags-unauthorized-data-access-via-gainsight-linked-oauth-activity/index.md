---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-21T12:00:07.672568+00:00'
exported_at: '2025-11-21T12:00:09.952445+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html
structured_data:
  about: []
  author: ''
  description: Salesforce and Gainsight probe OAuth abuse tied to ShinyHunters as
    apps are pulled and customers alerted.
  headline: Salesforce Flags Unauthorized Data Access via Gainsight-Linked OAuth Activity
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Salesforce Flags Unauthorized Data Access via Gainsight-Linked OAuth Activity
updated_at: '2025-11-21T12:00:07.672568+00:00'
url_hash: 8cbc7863f903f2e1ccfb1b7992a94a03e13206cd
---

**

Nov 21, 2025
**

Ravie Lakshmanan

Data Breach / SaaS Security

Salesforce has warned of detected "unusual activity" related to Gainsight-published applications connected to the platform.

"Our investigation indicates this activity may have enabled unauthorized access to certain customers' Salesforce data through the app's connection," the company
[said](https://status.salesforce.com/generalmessages/20000233)
in an advisory.

The cloud services firm said it has taken the step of revoking all active access and refresh tokens associated with Gainsight-published applications connected to Salesforce. It has also temporarily removed those applications from the AppExchange as its investigation continues.

Salesforce did not disclose how many customers were impacted by the incident, but said it has notified them.

"There is no indication that this issue resulted from any vulnerability in the Salesforce platform," the company added. "The activity appears to be related to the app's external connection to Salesforce."

Out of an abundance of caution, the Gainsight app has been
[temporarily pulled](https://status.gainsight.com/incidents/gvng0kly8vwf)
from the HubSpot Marketplace and Zendesk connector access has been revoked. "This may also impact Oauth access for customer connections while the review is taking place," Gainsight said. "No suspicious activity related to Hubspot has been observed at this point."

In a post shared on LinkedIn, Austin Larsen, principal threat analyst at Google Threat Intelligence Group (GTIG), described it as an "emerging campaign" targeting Gainsight-published applications connected to Salesforce by compromising third-party OAuth tokens to potentially gain unauthorized access.

The activity is assessed to be tied to threat actors associated with the ShinyHunters (aka UNC6240) group, mirroring a similar set of attacks
[targeting Salesloft Drift instances](https://thehackernews.com/2025/09/github-account-compromise-led-to.html)
earlier this August.

According to DataBreaches.Net, ShinyHunters has
[confirmed](https://databreaches.net/2025/11/20/threat-actors-have-reportedly-launched-yet-another-campaign-involving-an-application-connected-to-salesforce/)
the campaign is their doing and stated that the Salesloft and Gainsight attack waves allowed them to steal data from nearly 1000 organizations.

Interestingly, Gainsight previously
[said](https://www.gainsight.com/security/)
it was also one of the Salesloft Drift customers impacted in the previous attack. But it's not clear at this stage if the earlier breach played a role in the current incident.

In that hack, the attackers accessed business contact details for Salesforce-related content, including names, business email addresses, phone numbers, regional/location details, product licensing information, and support case contents (without attachments).

"Adversaries are increasingly targeting the OAuth tokens of trusted third-party SaaS integrations," Larsen
[pointed out](https://www.linkedin.com/feed/update/urn:li:activity:7397331617578610690/)
.

In light of the malicious activity, organizations are advised to review all third-party applications connected to Salesforce, revoke tokens for unused or suspicious applications, and rotate credentials if anomalies are flagged from an integration.