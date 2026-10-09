---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-27T00:00:08.357768+00:00'
exported_at: '2025-11-27T00:00:10.653218+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/qilin-ransomware-turns-south-korean-msp.html
structured_data:
  about: []
  author: ''
  description: Bitdefender links Qilin ransomware to a South Korean MSP hack that
    stole 1M files and 2 TB from 28 victims.
  headline: Qilin Ransomware Turns South Korean MSP Breach Into 28-Victim 'Korean
    Leaks' Data Heist
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/qilin-ransomware-turns-south-korean-msp.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Qilin Ransomware Turns South Korean MSP Breach Into 28-Victim 'Korean Leaks'
  Data Heist
updated_at: '2025-11-27T00:00:08.357768+00:00'
url_hash: b2be8e96759e2c38965749f68f641414cf4152c5
---

South Korea's financial sector has been targeted by what has been described as a sophisticated supply chain attack that led to the deployment of Qilin ransomware.

"This operation combined the capabilities of a major Ransomware-as-a-Service (RaaS) group, Qilin, with potential involvement from North Korean state-affiliated actors (Moonstone Sleet), leveraging Managed Service Provider (MSP) compromise as the initial access vector," Bitdefender
[said](https://www.bitdefender.com/en-us/blog/businessinsights/korean-leaks-campaign-targets-south-korean-financial-services-qilin-ransomware)
in a report shared with The Hacker News.

Qilin has emerged as one of the most active ransomware operations this year, with the RaaS crew exhibiting "explosive growth" in the month of October 2025 by
[claiming](https://www.cyfirma.com/research/tracking-ransomware-october-2025/)
over
[180 victims](https://cyble.com/blog/ransomware-attacks-surge-october-2025/)
. The group is responsible for 29% of all ransomware attacks, per data from
[NCC Group](https://www.nccgroup.com/newsroom/ncc-group-monthly-threat-pulse-review-of-october-2025/)
.

The Romanian cybersecurity company said it decided to dig deeper after uncovering an
[unusual spike](https://www.bitdefender.com/en-us/blog/businessinsights/bitdefender-threat-debrief-october-2025)
in ransomware victims from South Korea in September 2025, when it became the second-most affected country by ransomware after the U.S., with 25 cases, a significant jump from an average of about 2 victims per month between September 2024 and August 2025.

Further analysis found that all 25 cases were attributed exclusively to the Qilin ransomware group, with 24 of the victims in the financial sector. The campaign was given the moniker
**Korean Leaks**
by the attackers themselves.

While Qilin's origins are likely Russian, the group describes itself as "political activists" and "patriots of the country." It follows a traditional affiliate model, which involves recruiting a diverse group of hackers to carry out the attacks in return for taking a small share of up to 20% of the illicit payments.

One particular affiliate of note is a North Korean threat actor tracked as
[Moonstone Sleet](https://thehackernews.com/2024/05/microsoft-uncovers-moonstone-sleet-new.html)
, which, according to Microsoft, has deployed a custom ransomware variant called FakePenny in an attack targeting an unnamed defense technology company in April 2024.

Then, earlier this February, a significant pivot occurred when the adversary was
[observed](https://thehackernews.com/2025/03/thn-weekly-recap-new-attacks-old-tricks.html#:~:text=Moonstone%20Sleet%20Deploys%20Qilin%20Ransomware)
delivering Qilin ransomware at a limited number of organizations. While it's not exactly clear if the latest set of attacks was indeed carried out by the hacking group, the targeting of South Korean businesses aligns with its strategic objectives.

Korean Leaks took place over three publication waves, resulting in the theft of over 1 million files and 2 TB of data from 28 victims. Victim posts associated with four other entities were removed from the data leak site (DLS), suggesting that they may have been taken down either following ransom negotiations or a unique internal policy, Bitdefender said.

The three waves are as follows -

* **Wave 1**
  , comprising 10 victims from the financial management sector that was published on September 14, 2025
* **Wave 2**
  , comprising nine victims that were published between September 17 and 19, 2025
* **Wave 3**
  , comprising nine victims that were published between September 28 and October 4, 2025

An unusual aspect about these leaks is the departure from established tactics of exerting pressure on compromised organizations, instead leaning heavily on propaganda and political language.

"The entire campaign was framed as a public-service effort to expose systemic corruption, exemplified by the threats to release files that could be 'evidence of stock market manipulation' and names of 'well-known politicians and businessmen in Korea,'" Bitdefender said of the first wave of the campaign.

Subsequent waves went on to escalate the threat a notch higher, claiming that the leak of the data could pose a severe risk to the Korean financial market. The actors also called on South Korean authorities to investigate the case, citing stringent data protection laws.

A further shift in messaging was observed in the third wave, where the group initially continued the same theme of a national financial crisis resulting from the release of stolen information, but then switched to a language that "more closely resembled Qilin's typical, financially motivated extortion messages."

Given that Qilin
[boasts](https://thehackernews.com/2025/06/qilin-ransomware-adds-call-lawyer.html)
of an "in-house team of journalists" to help affiliates with writing texts for blog posts and help apply pressure during negotiations, it's assessed that the group's core members were behind the publication of the DLS text.

"The posts contain several of the core operator's signature grammatical inconsistencies," Bitdefender said. "However, this control over the final draft does not mean the affiliate was excluded from having a critical say in the key messaging or overall direction of the content."

To pull off these attacks, the Qilin affiliate is said to have breached a single upstream managed service provider (MSP), leveraging the access to compromise several victims at once. On September 23, 2025, the Korea JoongAng Daily
[reported](https://koreajoongangdaily.joins.com/news/2025-09-23/business/finance/More-than-20-management-companies-may-have-suffered-data-breaches-after-a-ransomware-attack/2406352)
that more than 20 asset management companies in the country were infected with ransomware following the compromise of GJTec.

To mitigate these risks, it's essential that organizations enforce Multi-Factor Authentication (MFA), apply the Principle of Least Privilege (PoLP) to restrict access, segment critical systems and sensitive data, and take proactive steps to reduce attack surfaces.

"The MSP compromise that triggered the 'Korean Leaks' operation highlights a critical blind spot in cybersecurity discussions," Bitdefender said. "Exploiting a vendor, contractor, or MSP that has access to other businesses is a more prevalent and practical route that RaaS groups seeking clustered victims can take."