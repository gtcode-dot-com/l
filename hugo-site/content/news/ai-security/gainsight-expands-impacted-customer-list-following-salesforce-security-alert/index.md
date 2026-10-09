---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-27T12:00:07.538526+00:00'
exported_at: '2025-11-27T12:00:09.806938+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html
structured_data:
  about: []
  author: ''
  description: Gainsight widens its breach fallout as ShinyHunters push an AI-tuned
    ShinySp1d3r ransomware alliance.
  headline: Gainsight Expands Impacted Customer List Following Salesforce Security
    Alert
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Gainsight Expands Impacted Customer List Following Salesforce Security Alert
updated_at: '2025-11-27T12:00:07.538526+00:00'
url_hash: e9514246ad42f6c224d8f4c5368254851e099690
---

**

Nov 27, 2025
**

Ravie Lakshmanan

Ransomware / Cloud Security

Gainsight has disclosed that the recent suspicious activity targeting its applications has affected more customers than previously thought.

The company
[said](https://communities.gainsight.com/community-news-2/salesforce-security-advisory-relating-to-gainsight-faqs-29809)
Salesforce initially provided a list of 3 impacted customers and that it has "expanded to a larger list" as of November 21, 2025. It did not reveal the exact number of customers who were impacted, but its CEO, Chuck Ganapathi,
[said](https://www.gainsight.com/blog/supporting-our-customers-and-community-an-update-on-the-recent-security-advisory-related-to-gainsight/)
"we presently know of only a handful of customers who had their data affected."

The development comes as Salesforce warned of detected "unusual activity" related to Gainsight-published applications connected to the platform, prompting the company to revoke all access and refresh tokens associated with them. The breach has been claimed by a notorious cybercrime group known as ShinyHunters (aka Bling Libra).

A number of other precautionary steps have been enacted to contain the incident. This includes Zendesk, Gong.io, and HubSpot temporarily suspending their Gainsight integrations, and Google disabling OAuth clients with callback URIs like gainsightcloud[.]com. HubSpot, in its own advisory,
[said](https://trust.hubspot.com/?tcuUid=8558d1b8-1314-4a67-a90c-063d8f995ff9)
it found no evidence to suggest any compromise of its own infrastructure or customers.

In an FAQ, Gainsight has also listed the products for which the ability to read and write from Salesforce has been temporarily unavailable -

* Customer Success (CS)
* Community (CC)
* Northpass - Customer Education (CE)
* Skilljar (SJ)
* Staircase (ST)

The company, however, emphasized that Staircase is not affected by the incident and that Salesforce removed the Staircase connection out of caution in response to an ongoing investigation.

Both Salesforce and Gainsight have published indicators of compromise (IoCs) associated with the breach, with one user agent string, "Salesforce-Multi-Org-Fetcher/1.0", used for unauthorized access, also flagged as previously employed in the Salesloft Drift activity.

According to
[information](https://help.salesforce.com/s/articleView?id=005229029&type=1)
from Salesforce, reconnaissance efforts against customers with compromised Gainsight access tokens were first recorded from the IP address "3.239.45[.]43" on October 23, 2025, followed by subsequent waves of reconnaissance and unauthorized access starting November 8.

To further secure their environments, customers are asked to follow the steps below -

* Rotate the S3 bucket access keys and other connectors like BigQuery, Zuora, Snowflake etc., used for connections with Gainsight
* Log in to Gainsight NXT directly, rather than through Salesforce, until the integration is fully restored
* Reset NXT user passwords for any users who do not authenticate via SSO.
* Re-authorize any connected applications or integrations that rely on user credentials or tokens

"These steps are preventative in nature and are designed to ensure your environment remains secure while the investigation continues," Gainsight said.

The development comes against the backdrop of a new ransomware-as-a-service (RaaS) platform called
[ShinySp1d3r](https://thehackernews.com/2025/08/cybercrime-groups-shinyhunters.html)
(also spelled Sh1nySp1d3r) that's being developed by Scattered Spider, LAPSUS$, and ShinyHunters (SLSH). Data from ZeroFox has revealed that the cybercriminal alliance has been responsible for at least 51 cyberattacks over the past year.

"While the ShinySp1d3r encryptor has some features common to other encryptors, it also boasts features that have never been seen before in the RaaS space," the company said.

"These include: Hooking the EtwEventWrite function to prevent Windows Event Viewer logging, terminating processes that keep files open – which would normally prevent encryption – by iterating over processes before killing them, [and] filling free space in a drive by writing random data contained in a .tmp file, likely to overwrite any deleted files."

ShinySp1d3r also comes with the ability to
[search](https://hackyourmom.com/en/novyny/shinyhunters-stvoryly-novyj-potuzhnyj-raas-detali-majbutnih-atak-uzhe-vidomi/)
for open network shares and encrypt them, as well as propagate to other devices on the local network through deployViaSCM, deployViaWMI, and attemptGPODeployment.

In a report published Wednesday, independent cybersecurity journalist Brian Krebs
[said](https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/)
the individual responsible for releasing the ransomware is a core SLSH member named "Rey" (aka
[@ReyXBF](https://web.archive.org/web/20250418062459/https://twitter.com/ReyXBF/status/1913116530658705661)
), who is also one of the three administrators of the group's Telegram channel. Rey was previously an administrator of
[BreachForums](https://thehackernews.com/2025/09/doj-resentences-breachforums-founder-to.html)
and the data leak website for
[HellCat ransomware](https://thehackernews.com/2025/01/experts-find-shared-codebase-linking.html)
.

Rey, whose identity has been unmasked as Saif Al-Din Khader, told Krebs that ShinySp1d3r is a rehash of HellCat that has been modified with artificial intelligence (AI) tools and that he has been cooperating with law enforcement since at least June 2025.

"The emergence of a RaaS program, in conjunction with an EaaS [extortion-as-a-service] offering, makes SLSH a formidable adversary in terms of the wide net they can cast against organizations using multiple methods to monetize their intrusion operations," Palo Alto Networks Unit 42 researcher Matt Brady
[said](https://unit42.paloaltonetworks.com/new-shinysp1d3r-ransomware/)
. "Additionally, the
[insider recruitment](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploit-chrome-0.html#:~:text=Salesforce%20Warns%20of%20Unauthorized%20Data%20Access%20via%20Gainsight%2DLinked%20Apps)
element adds yet another layer for organizations to defend against."