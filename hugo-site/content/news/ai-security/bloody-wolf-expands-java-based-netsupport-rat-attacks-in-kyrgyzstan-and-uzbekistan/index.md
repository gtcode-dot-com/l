---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-28T00:00:07.463168+00:00'
exported_at: '2025-11-28T00:00:09.876564+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/bloody-wolf-expands-java-based.html
structured_data:
  about: []
  author: ''
  description: Bloody Wolf targets Kyrgyzstan and Uzbekistan with Java-based loaders
    delivering NetSupport RAT in sector-wide phishing attacks.
  headline: Bloody Wolf Expands Java-based NetSupport RAT Attacks in Kyrgyzstan and
    Uzbekistan
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/bloody-wolf-expands-java-based.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Bloody Wolf Expands Java-based NetSupport RAT Attacks in Kyrgyzstan and Uzbekistan
updated_at: '2025-11-28T00:00:07.463168+00:00'
url_hash: 16860247d8893f868f86c1ee2979ecd963795b1e
---

**

Nov 27, 2025
**

Ravie Lakshmanan

Malware / Social Engineering

The threat actor known as
**Bloody Wolf**
has been attributed to a cyber attack campaign that has targeted Kyrgyzstan since at least June 2025 with the goal of delivering NetSupport RAT.

As of October 2025, the activity has expanded to also single out Uzbekistan, Group-IB researchers Amirbek Kurbanov and Volen Kayo said in a report published in collaboration with Ukuk, a state enterprise under the Prosecutor General's office of the Kyrgyz Republic. The attacks have targeted finance, government, and information technology (IT) sectors.

"Those threat actors would impersonate the [Kyrgyzstan's] Ministry of Justice through official looking PDF documents and domain names, which in turn hosted malicious Java Archive (JAR) files designed to deploy the NetSupport RAT," the Singapore-headquartered company
[said](https://www.group-ib.com/blog/bloody-wolf/)
.

"This combination of social engineering and accessible tooling allows Bloody Wolf to remain effective while keeping a low operational profile."

[Bloody Wolf](https://thehackernews.com/2024/08/kazakh-organizations-targeted-by-bloody.html)
is the name assigned to a
[hacking group](https://thehackernews.com/2025/03/kaspersky-links-head-mare-to-twelve.html)
of unknown provenance that has used spear-phishing attacks to target entities in Kazakhstan and Russia using tools like STRRAT and NetSupport. The group is assessed to be active since at least late 2023.

The targeting of Kyrgyzstan and Uzbekistan using similar initial access techniques marks an expansion of the threat actor's operations in Central Asia, primarily impersonating trusted government ministries in phishing emails to distribute weaponized links or attachments.

The attack chains more or less follow the same approach in that the message recipients are tricked into clicking on links that download malicious Java archive (JAR) loader files along with instructions to install Java Runtime.

While the email claims the installation is necessary to view the documents, the reality is that it's used to execute the loader. Once launched, the loader then proceeds to fetch the next-stage payload (i.e., NetSupport RAT) from infrastructure that's under the attacker's control and set up persistence in three ways -

* Creating a scheduled task
* Adding a Windows Registry value
* Dropping a batch script to the folder "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

The Uzbekistan phase of the campaign is notable for incorporating geofencing restrictions, thereby causing requests originating outside of the country to be redirected to the legitimate data.egov[.]uz website. Requests from within Uzbekistan have been found to trigger the download of the JAR file from an embedded link within the PDF attachment.

Group-IB said the JAR loaders observed in the campaigns are built with Java 8, which was released in March 2014. It's believed that the attackers are using a bespoke JAR generator or template to spawn these artifacts. The NetSupport RAT payload is a old version of NetSupport Manager from October 2013.

"Bloody Wolf has demonstrated how low-cost, commercially available tools can be weaponized into sophisticated, regionally targeted cyber operations," it said. "By exploiting trust in government institutions and leveraging simple JAR-based loaders, the group continues to maintain a strong foothold across the Central Asian threat landscape."