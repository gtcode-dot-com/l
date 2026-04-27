---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-27T16:15:16.968477+00:00'
exported_at: '2026-04-27T16:15:19.716917+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html
structured_data:
  about: []
  author: ''
  description: Checkmarx data surfaced after March 23, 2026 supply chain attack, prompting
    repository lockdown and investigation, raising exposure concerns.
  headline: Checkmarx Confirms GitHub Repository Data Posted on Dark Web After March
    23 Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Checkmarx Confirms GitHub Repository Data Posted on Dark Web After March 23
  Attack
updated_at: '2026-04-27T16:15:16.968477+00:00'
url_hash: c823a7e1605b8c312bfe26f3b9eee7d7689b39f3
---

**

Ravie Lakshmanan
**

Apr 27, 2026

Checkmarx has disclosed that its ongoing investigation tied to the supply chain security incident has revealed that a cybercriminal group published data related to the company on the dark web.

"Based on current evidence, we believe this data originated from Checkmarx's GitHub repository, and that access to that repository was facilitated through the initial supply chain attack of March 23, 2026," the Israeli security company
[said](https://checkmarx.com/blog/checkmarx-security-update-april-26/)
.

It also emphasized that the GitHub repository is maintained separately from its customer production environment, adding that no customer data is stored in the repository. Checkmarx said its forensic probe into the incident is ongoing and that it's actively working to verify the nature and scope of the posted data.

Furthermore, the company said it has locked down access to the affected GitHub repository as part of its incident response efforts.

"If we determine that customer information was involved in this incident, we will notify customers and all relevant parties immediately," it said.

The development comes after the Dark Web Informer
[shared](https://x.com/DarkWebInformer/status/2048185612209881515)
in an X post that the LAPSUS$ cybercrime group claimed three victims on its data leak site, one of which includes Checkmarx. The data, per the listing, contains source code, employee database, API keys, and MongoDB/MySQL credentials.

Checkmarx
[suffered a breach](https://thehackernews.com/2026/03/teampcp-hacks-checkmarx-github-actions.html)
late last month following the Trivy supply chain attack, as a result of which two of its GitHub Actions workflows and two plugins distributed via the Open VSX marketplace were tampered with to push a credential stealer capable of harvesting a wide range of developer secrets. The threat actor known as TeamPCP claimed responsibility for the attack.

Last week, the financially motivated group is
[suspected](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html)
to have compromised Checkmarx's KICS Docker image, along with the two VS Code extensions and a GitHub Actions workflow with a similar credential-stealing malware. This, in turn, had a cascading impact, leading to a brief compromise of the
[Bitwarden CLI npm package](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html)
.