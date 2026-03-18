---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-18T22:15:18.127225+00:00'
exported_at: '2026-03-18T22:15:20.311811+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/ofac-sanctions-dprk-it-worker-network.html
structured_data:
  about: []
  author: ''
  description: OFAC sanctions DPRK IT fraud network using fake jobs and AI tactics,
    exposing funding links to WMD programs and insider threats.
  headline: OFAC Sanctions DPRK IT Worker Network Funding WMD Programs Through Fake
    Remote Jobs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/ofac-sanctions-dprk-it-worker-network.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OFAC Sanctions DPRK IT Worker Network Funding WMD Programs Through Fake Remote
  Jobs
updated_at: '2026-03-18T22:15:18.127225+00:00'
url_hash: c76ac38a6eb1dd0a1224b2a3cb91249a0876585f
---

The U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) has sanctioned six individuals and two entities for their involvement in the Democratic People's Republic of Korea (DPRK)
[information technology (IT) worker scheme](https://thehackernews.com/2026/02/ukrainian-national-sentenced-to-5-years.html)
with an aim to defraud U.S. businesses and generate illicit revenue for the regime to fund its weapons of mass destruction (WMD) programs.

"The North Korean regime targets American companies through deceptive schemes carried out by its overseas IT operatives, who weaponize sensitive data and extort businesses for substantial payments,"
[said](https://home.treasury.gov/news/press-releases/sb0416)
Secretary of the Treasury Scott Bessent.

The
[fraudulent scheme](https://thehackernews.com/2026/01/north-korean-purplebravo-campaign.html)
, also called Coral Sleet/Jasper Sleet, PurpleDelta and Wagemole, relies on bogus documentation, stolen identities, and fabricated personas to help the IT workers obscure their true origins and land jobs at legitimate companies in the U.S. and elsewhere. A disproportionate portion of the salaries is then funneled back to North Korea to facilitate the nation's missile programs in violation of international sanctions.

In some cases, these efforts are
[complemented](https://thehackernews.com/2024/10/north-korean-it-workers-in-western.html)
by the deployment of malware to steal proprietary and sensitive information, as well as engaging in extortion efforts by demanding ransoms in return for not publicly leaking the stolen data.

The individuals and entities targeted by the latest round of OFAC sanctions are listed below -

* **Amnokgang Technology Development Company**
  , an IT company that manages delegations of overseas IT workers and conducts other illicit procurement activities to obtain and sell military and commercial technology through their overseas networks.
* **Nguyen Quang Viet**
  , the Chief Executive Officer of Vietnamese company
  **Quangvietdnbg International Services Company Limited**
  that facilitates currency conversion services for North Koreans. The company is estimated to have converted about $2.5 million into cryptocurrency between mid-2023 and mid-2025.
* **Do Phi Khanh**
  , an associate of Kim Se Un, who was
  [sanctioned](https://thehackernews.com/2025/07/us-sanctions-firm-behind-n-korean-it.html)
  by the U.S. in July 2025. Do is alleged to have acted as Kim's proxy and allowed Kim to use his identity to open bank accounts and launder proceeds from IT workers.
* **Hoang Van Nguyen**
  , who also assists Kim in opening bank accounts and enables cryptocurrency transactions for Kim.
* **Yun Song Guk**
  , a North Korean national who led a group of IT workers conducting freelance IT work from Boten, Laos, since at least 2023. Yun has coordinated several dozen financial transactions amounting to more than $70,000 with
  **Hoang Minh Quang**
  relating to IT services, and has worked with
  **York Louis Celestino Herrera**
  to develop freelance IT service contracts.

The development comes as LevelBlue highlighted the IT worker scheme's use of Astrill VPN to conduct their operations while located in countries like China, owing to the service's ability to bypass China's Great Firewall. The idea is to tunnel traffic through U.S. exit nodes, effectively allowing them to masquerade as legitimate domestic employees.

"These threat actors commonly operate from China rather than North Korea for two reasons: more reliable Internet infrastructure and the ability to leverage VPN services to conceal their true geographic origin," security researcher Tue Luu
[said](https://www.levelblue.com/blogs/spiderlabs-blog/how-levelblue-otx-and-cybereason-xdr-detected-a-north-korea-linked-remote-it-worker)
. "Lazarus Group's subgroups, including
[Contagious Interview](https://thehackernews.com/2026/03/north-korean-hackers-publish-26-npm.html)
, rely on this capability to access the global Internet unrestricted, manage command-and-control infrastructure, and mask their true location."

The cybersecurity company also said it detected an unsuccessful attempt made by North Korea to infiltrate an organization by replying to a help wanted ad. The IT worker, who was hired on August 15, 2025, as a remote employee to work on Salesforce data, was terminated 10 days later after exhibiting indicators showing consistent logins from China.

A notable aspect of Jasper Sleet's tradecraft is the use of artificial intelligence to enable identity fabrication, social engineering, and long‑term operational persistence at low cost, underscoring how AI‑powered services can lower technical barriers and augment threat actors' capabilities.

"Jasper Sleet leverages AI across the attack lifecycle to get hired, stay hired, and misuse access at scale," Microsoft
[said](https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/)
. "Threat actors are using AI to shortcut the reconnaissance process that informs the development of convincing digital personas tailored to specific job markets and roles."

Another crucial component involves using an AI application called Faceswap to insert the faces of North Korean IT workers into stolen identity documents and to generate polished headshots for resumes. In doing so, these efforts not only aim to improve the precision of their campaigns, but also increase the credibility by crafting convincing digital identities.

Furthermore, the remote IT worker threat is assessed to have leveraged agentic AI tools to create fake company websites, and to rapidly generate, refine, and reimplement malware components, in some cases by jailbreaking large language models (LLMs).

"Threat actors such as North Korean remote IT workers rely on long‑term, trusted access," Microsoft said. "Because of this fact, defenders should treat fraudulent employment and access misuse as an insider‑risk scenario, focusing on detecting misuse of legitimate credentials, abnormal access patterns, and sustained low‑and‑slow activity."

In a detailed report published by Flare and IBM X-Force examining the tactics and techniques employed by the IT worker operatives, it has come to light that the threat actors use timesheets for tracking job applications and work progress, IP Messenger (aka IPMsg) for decentralized internal communication, and Google Translate to translate job descriptions, craft applications, and even interpret responses from tools like ChatGPT.

The IT worker scheme is built atop a multi-tiered operational structure involving recruiters, facilitators, IT workers, and collaborators, each of whom play a distinct part -

* Recruiters, who are responsible for screening potential IT workers and recording initial interview sessions to send to facilitators.
* Facilitators and IT workers, who are tasked with persona creation, obtaining freelance or full-time employment, and onboarding new hires.
* Collaborators, who are recruited to donate their personal identity and/or information to help the IT workers complete the hiring process and receive company-issued laptops.

"With the help of recruited western collaborators, primarily from LinkedIn and GitHub, who, willingly or unwillingly, provide their identities for use in the IT worker fraud scheme, NKITW are able to penetrate more deeply and reliably into an organization, for a longer period of time," the companies
[said](https://flare.io/learn/resources/north-korean-infiltrator-threat)
in a report shared with The Hacker News.

"North Korea’s IT worker operations are widespread and deeply integrated within the DPRK party-state. It is an integral component in the DPRK's revenue-generation and sanctions-evasion machinery."