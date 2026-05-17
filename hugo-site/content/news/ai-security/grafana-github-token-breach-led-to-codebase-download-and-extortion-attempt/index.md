---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-17T16:12:22.285731+00:00'
exported_at: '2026-05-17T16:12:24.592973+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html
structured_data:
  about: []
  author: ''
  description: Grafana disclosed an unauthorized party accessed its GitHub environment
    and downloaded its codebase via a token.
  headline: Grafana GitHub Token Breach Led to Codebase Download and Extortion Attempt
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Grafana GitHub Token Breach Led to Codebase Download and Extortion Attempt
updated_at: '2026-05-17T16:12:22.285731+00:00'
url_hash: 570d34eb2ef025873ee9a848a0d0aabde37231b1
---

**

Ravie Lakshmanan
**

May 17, 2026

Data Breach / Cybercrime

Grafana has disclosed that an "unauthorized party" obtained a token that granted them the ability to access the company's GitHub environment and download its codebase.

"Our investigation has determined that no customer data or personal information was accessed during this incident, and we have found no evidence of impact to customer systems or operations," Grafana
[said](https://x.com/grafana/status/2055827123236171827)
in a series of posts on X.

The company also said it immediately launched a forensic analysis upon discovering the activity and that it identified the source of the leak, adding the compromised credentials have since been invalidated, and extra security measures have been implemented to secure against unauthorized access.

Furthermore, Grafana revealed the attacker tried to blackmail and extort the company, demanding they make a payment to prevent the stolen database from being published.

Grafana said it has opted not to pay the ransom, citing the U.S. Federal Bureau of Investigation (FBI). The agency has previously warned against negotiating ransoms with perpetrators, as there is no guarantee that doing so will help affected companies get their data back.

"It also encourages perpetrators to target more victims and offers an incentive for others to get involved in this type of illegal activity," the FBI
[states](https://www.fbi.gov/how-we-can-help-you/scams-and-safety/common-frauds-and-scams/ransomware)
on its website.

Grafana did not reveal when the incident took place or since when the threat actor had access to its environment, only revealing that it learned of the attack "recently." The breach has not been attributed to any known threat actor or group.

However, reports from
[Hackmanac](https://x.com/H4ckmanac/status/2055380899840078266)
and
[Ransomware.live](https://ransomware.live/group/coinbasecartel)
indicate that a cybercrime group named CoinbaseCartel has claimed responsibility for the incident.

Per details shared by
[Halcyon](https://www.halcyon.ai/jp/threat-group/coinbasecartel)
and
[Fortinet FortiGuard Labs](https://www.fortiguard.com/threat-actor/6386/coinbase-cartel-ransomware)
, CoinbaseCartel is a data extortion crew that emerged in September 2025. It's assessed to be an offshoot of the ShinyHunters, Scattered Spider, and LAPSUS$ ecosystems.

The group, which only focuses on data theft and extortion, unlike traditional ransomware groups, has amassed 170 victims across healthcare, technology, transportation, manufacturing, and business services.

The company also did not reveal what codebase the attacker downloaded, but Grafana offers various solutions like
[Grafana Cloud](https://grafana.com/docs/grafana-cloud/introduction/)
, a fully-managed, cloud-hosted observability platform for applications and infrastructure. The Hacker News has reached out to Grafana for comment, and we will update the story if we hear back.

The development comes days after American educational technology company Instructure
[made the controversial decision](https://thehackernews.com/2026/05/instructure-reaches-ransom-agreement.html)
to settle with the ShinyHunters extortion group after the latter threatened to leak terabytes of data belonging to thousands of schools and universities across the U.S.