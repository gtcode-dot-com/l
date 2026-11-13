---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-13T03:10:49.159149+00:00'
exported_at: '2026-11-13T03:10:51.265098+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/chainalysis-breach-exposes-all-users.html
structured_data:
  about: []
  author: ''
  description: Chainalysis says an agentic cyberattack exposed all users' names, usernames,
    password hashes and live tokens, prompting service shutdowns.
  headline: Chainalysis Breach Exposes All Users' Credentials, Forces Shutdown of
    Key Services
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/chainalysis-breach-exposes-all-users.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Chainalysis Breach Exposes All Users' Credentials, Forces Shutdown of Key Services
updated_at: '2026-11-13T03:10:49.159149+00:00'
url_hash: 6facdf5f94dfdf61881da285416d99f838837e37
---

Blockchain analysis firm Chainalysis has
[revealed](https://www.chainalysis.com/blog/security-incident-october-30/)
that its ongoing investigation into the agentic cyber attack targeting its systems also exposed names, usernames, password hashes and live tokens for all users.

"While we investigated, we removed access to Reactor and Data Solutions," the company said. "At this time we continue to have no evidence that any investigations data has been accessed or Chainalysis attribution data has been manipulated."

Chainalysis said it has implemented additional proactive monitoring systems to detect unusual activity, adding it took the Know Your Transaction (KYT) user interface and API offline, alongside other address screening products and the login page.

Previously, Chainalysis said it was probing what it described as an "ongoing multi-front cyber attack," leading to the discovery of an "on-path attack" that exposed a subset of customer passwords. The company said the attack vector has since been addressed.

Out of an abundance of caution, Chainalysis has also taken the step of locking the impacted accounts.

"For customers who just received an email from us instructing you to reset your Chainalysis password, resetting this password won't be possible right now," it noted. "We still encourage you, where necessary, to reset your password on other systems where you may be reusing credentials."

The development comes less than a week after Chainalysis
[said](https://thehackernews.com/2026/10/chainalysis-confirms-intrusion-into.html)
it was the target of a cybersecurity incident in which an external actor leveraged offensive agentic techniques to obtain unauthorized access to its systems and internal tools.

The company said it intends to begin restoring access to KYT and Address Screening, urging customers to contact its support email (support@chainalysis.com) or their Chainalysis account team with trusted IP addresses, which will be added to an allowlist. From there, users can reset their passwords and rotate API keys to register transactions.

"We are working around the clock to harden our systems and bring Reactor and Data Solutions back online," Chainalysis said. "We will require additional protections to access accounts, including that every user will have to reset passwords and rotate API keys as appropriate. We will communicate these changes as necessary."

It's unclear who is behind the attack, but Chainalysis notes it was similar to "many other tech platforms in recent weeks."

### Rise in AI-Linked Attacks

Indeed, a
[number of companies](https://thehackernews.com/2026/11/chainstack-reports-production-systems.html)
, including Chainstack, OpenCode, Warp, and WorkOS, have disclosed that they have been targeted by artificial intelligence (AI)-driven attacks, some of which involve an autonomous penetration testing tool called ARTEX.

According to Microsoft, threat actors are using an agentic AI offensive framework to search public GitHub repositories for exposed secrets, such as credentials, application credentials, and AI inference-related API keys across multiple applications and cloud services, to conduct follow-on attacks.

"Agentic tooling like
[ARTEX](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)
allows threat actors to not only scan for secrets across multiple repositories at a quicker pace but also use the agents to analyze the output and conduct follow-on attacks, cutting down on the need for the threat actor to have hands-on-keyboard interactions throughout the attack chain," the tech giant said.

In at least one case, an AI agent is said to have progressed from scanning GitHub for secrets to exfiltrating data from Azure Key Vault in just five minutes. The activity is assessed to be ongoing from August 2026.

Some aspects of the campaign
[correspond](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)
to post-exploitation activity involving the misuse of valid application credentials to access Microsoft Entra ID tenants of certain organizations and connected Azure and Microsoft 365 resources. The sign-in events originated from two IP addresses, 199.19.77[.]84 and 199.19.77[.]18.

"The agent successfully conducted service principal sign-ins on dozens of associated applications across multiple tenants," Microsoft said.

"The threat actor targeted operations that return credentials, including storage account keys, App Service settings, connection strings and publishing credentials, AI and machine learning (ML) connections and datastores, and Azure Kubernetes Service (AKS) user credentials. The compromised applications subsequently accessed SharePoint and OneDrive in the targeted organization tenants, including file downloads and mailbox-item access."

In addition, the threat actor has been observed attempting to steal Azure resources, including compromised Azure AI services, likely as part of efforts to facilitate broader attack activity.

Another notable aspect of the campaign is that the agentic AI tools have been found obtaining a token for a single-tenant OAuth application in the same target organization, then use the compromised OAuth application to enumerate other cloud resources within the organization. In a handful of cases, Microsoft said it observed the agents exfiltrating secrets from the organization's Azure Key Vault.

"During this activity, the AI agents repeatedly demonstrated a focus on credentials that provide access to AI services, such as API keys for major AI service providers and OAuth applications with access to Foundry Tools (previously known as Azure Cognitive Services)," Microsoft said.

The development also coincides with a
[surge in attacks](https://www.wiz.io/blog/the-rise-of-agentic-attacks)
targeting AI developer platforms over the past month,
[allowing threat actors](https://labs.cloudsecurityalliance.org/research/csa-research-note-inference-provider-platform-chain-campaign/)
to resell access, abuse them as free compute (i.e., LLMjacking), and use them as attribution cover for further attacks.

In a report published this week, Google
[disclosed](https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html)
that cybercriminals have established a business model out of stealing cloud access to commercial large language models (LLMs) and reselling it to paying customers.

The monetization infrastructure centers on LLM Mixers, who act as an illicit intermediary to advertise access to compromised enterprise LLM accounts on underground markets without their customers needing to set up their own legitimate API credentials or cloud infrastructure.

In other words, LLM mixers turn stolen enterprise model access into a criminal routing gateway for paying subscribers, while the legitimate owner's systems continue to accept requests. These services help proxy requests across stolen accounts, distribute consumption, and obscure the original source of access.

The emerging LLMjacking ecosystem "create[s] a market that makes the theft easily monetizable, likely driving more actors to undertake operations to steal credentials," Wiz
[said](https://www.wiz.io/blog/black-october-for-ai-developer-platforms)
.

The Google-owned subsidiary also said it identified at least two resale operations leveraging stolen AWS Bedrock keys obtained from two different organizations – llm-routing[.]com (momo) and xingjiabiapi[.]org – both of which offer a wide selection of frontier models for discount prices. That said, there is no evidence that the operators of these websites were responsible for the initial platform compromises.

Interestingly, the IP address linked to llm-routing[.]com, 23.106.46[.]239, hosted an Artex landing page in mid-October 2026 and has been flagged by Zeabur as an indicator of compromise. Last month, Zeabur
[disclosed](https://thehackernews.com/2026/10/threatsday-ai-secrets-leak-pingcap.html#3-2-million-secrets-exposed)
a security breach in which an unknown threat actor exploited credentials stored in plaintext to compromise its infrastructure, exfiltrating over 3.2 million environment variable records and data associated with 321,810 accounts.

The following IP addresses have been used to test stolen keys and are suspected to be linked to LLM token abuse and resale -

* 23.106.46.239
* 38.246.114.118
* 104.243.32.50
* 31.57.201.201

"Threat actors are not only using AI as a tool to conduct attacks, they are also compromising victim environments solely to abuse their finances for mass Large Language Model (LLM) execution, incurring hundreds of thousands of dollars in AI API charges," Wiz
[said](https://www.wiz.io/blog/from-phishing-to-llmjacking)
.

### Reactor, KYT, and Address Screening Back Online

In an update shared on November 7, 2026, Chainalysis said Reactor, KYT, and Address Screening products have been restored and are back online. The move comes after the company urged customers to submit their trusted IP addresses to be added to an allowlist for access restoration.

"We've restored these products with enhanced security measures, and we're asking customers to reconnect in a specific way to keep accounts and data protected," it said.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.