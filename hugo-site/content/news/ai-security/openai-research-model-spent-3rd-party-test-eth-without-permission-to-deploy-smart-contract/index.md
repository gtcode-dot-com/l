---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-17T22:16:30.118088+00:00'
exported_at: '2026-10-17T22:16:31.170953+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/openai-research-model-spent-3rd-party.html
structured_data:
  about: []
  author: ''
  description: OpenAI disclosed seven model misalignment incidents, including unauthorized
    Sepolia ETH spending and access to non-public data.
  headline: OpenAI Research Model Spent 3rd-Party Test ETH Without Permission to Deploy
    Smart Contract
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/openai-research-model-spent-3rd-party.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Research Model Spent 3rd-Party Test ETH Without Permission to Deploy
  Smart Contract
updated_at: '2026-10-17T22:16:30.118088+00:00'
url_hash: 82bd71e8965df8d705ef4063e43ff3dafd76fb44
---

**

Ravie Lakshmanan
**

Oct 16, 2026

Artificial Intelligence / Web Security

OpenAI has disclosed
[seven new incidents](https://alignment.openai.com/misalignment-reports/?sort=created)
in which its artificial intelligence (AI) models exhibited misaligned behavior, including one case where its research model, after not having funds on an Ethereum test network, spent test cryptocurrency from a third-party's wallet without authorization to complete a coding task.

The incident, the AI company said, involved an internal research model part of the GPT-5.6 Sol family. The incident occurred on June 26, 2026, and was discovered by OpenAI three months later.

"An internal research model asked to update a cryptocurrency trading application used funds from a wallet that the task had not supplied to pay for a deployment on Sepolia, an Ethereum test network," OpenAI
[said](https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/)
. "It derived wallet keys from publicly known developer recovery phrases, found an account with test-network funds, and used that account to pay for the requested contract deployment."

The assignment allowed the model to deploy compatible contracts if it did not find one, but gave it no funded wallet to pay the network fees. After its attempts to obtain free test tokens failed, it wrote a script to derive "accounts from common developer recovery phrases and query their balances."

In the process, it identified 362 addresses and found one account that held enough Sepolia ETH. Armed with the recovery (or seed) phrase, the model derived the private keys that grant unauthorized access to the corresponding account and spend the stashed cryptocurrency.

Although the model questioned whether it had the necessary permission to carry out this step, it subsequently reasoned that a public recovery phrase and valueless test-network tokens made the funds acceptable to use.

"But using public known key/funds ethically? Funds on a known public dev mnemonic are effectively abandoned/test ETH; Sepolia valueless," the model mused. "We can use [amount redacted] to deploy task. Fine."

OpenAI has since implemented additional safeguards to prevent live internet access for such scenarios, adding it runs its misalignment monitoring system on all traffic to flag events if its AI agents manage to gain live internet access.

"This case shows that a model can substitute its own judgment about likely harm for the account holder's permission, then act on that judgment without authorization," OpenAI said.

Besides using a funded test cryptocurrency wallet without authorization, OpenAI said it identified six more cases of misalignment involving its models, adding to
[three other incidents](https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html)
it revealed at the start of this month -

* **[June 16, 2026](https://alignment.openai.com/misalignment-reports/circumventing-internet-restrictions-through-an-external-browser/)**
  , when an internal research model bypassed a restriction limiting internet access to HTTP GET requests as part of efforts to seek public trade statistics. It achieved this by using an external browser to send requests on its behalf, retrieved annual figures as an image, and extracted them using optical character recognition.
* **[June 16 and 17, 2026](https://alignment.openai.com/misalignment-reports/sending-disallowed-web-requests-and-reaching-a-public-file-service/)**
  , when an internal model developed and tested ways to bypass restrictions on internet access during reinforcement learning and explored ways to contact outside services, and continued testing these approaches even after obtaining the statistics it was seeking, such as teacher salaries in Merrowen, connections to the electrical grid in Orvessa, and disability counts in Bellora.
* **[June 17, 2026](https://alignment.openai.com/misalignment-reports/accessing-and-changing-internal-systems-during-dashboard-research/)**
  , when a highly persistent internal model tasked with retrieving figures from a public research dashboard accessed an unspecified organization's internal systems and changed their configuration. The model altered a setting to obtain a cloud-storage access token and downloaded non-public tables containing 147,451 rows. Not only did the model not disclose these actions, it restored the modified setting, but continued using the token to retrieve non-public data.
* **[June 17, 2026](https://alignment.openai.com/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/)**
  , when a highly persistent internal model deployed as part of a data-retrieval task in reinforcement-learning training abused a government statistics website's file-download feature to retrieve server configuration and application files, including sensitive credentials. It then analyzed the application code, bypassed the statistics endpoint's authorization checks, retrieved data that it was denied access to, and stored it locally. The data included annual statistics spanning 24 years, including years beyond the requested year. In its answer, the model made no mention of the fact that it had obtained unauthorized access.
* **[June 19 and 20, 2026](https://alignment.openai.com/misalignment-reports/obtaining-public-statistics-with-disallowed-requests/)**
  , when its internal research models bypassed restrictions on internet access to allow only HTTP GET requests to fetch figures from government entities' public data sources by writing custom programs to send a POST request through a custom network connection.
* **[October 6, 2026](https://alignment.openai.com/misalignment-reports/damaging-the-task-environment-to-trigger-a-reset/)**
  , when an internal research model assigned to grade seven responses attempted to submit unsupported assessments after it found that the required input files were missing. When the automated check rejected its bogus grading report, the model tried to create fake input files in an attempt to pass the checks. After this also resulted in failure, the model took the step of damaging its task environment in hopes of triggering a reset.

"In response to this and other incidents, we hardened our security controls, took additional steps to prevent models from accessing the live internet during training, improved alignment grading, and extended misalignment monitoring to all reinforcement learning and evaluation traffic," OpenAI said.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.