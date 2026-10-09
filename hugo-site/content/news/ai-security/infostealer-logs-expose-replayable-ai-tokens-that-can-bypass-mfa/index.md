---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-27T18:29:51.551375+00:00'
exported_at: '2026-09-27T18:29:53.299993+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html
structured_data:
  about: []
  author: ''
  description: Infostealer logs expose replayable AI session tokens and API keys that
    can bypass login controls and enable unauthorized account access.
  headline: Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Infostealer Logs Expose Replayable AI Tokens That Can Bypass MFA
updated_at: '2026-09-27T18:29:51.551375+00:00'
url_hash: 2c0350c3fa60e4a4500c2719978587bca3913c0c
---

Cybercriminals are hijacking artificial intelligence (AI) user accounts via information stealer logs to create "stolen keys" that grant illicit access to tools from model providers like Google, Anthropic, and others.

Information stealers like Lumma Stealer or Vidar are equipped to harvest a wide range of data from compromised systems. This can include credential, session tokens, and API keys.

Once the data is stolen, threat actors who have purchased access to these off-the-shelf offerings put them up for sale on underground forums in the form of stealer logs to enable follow-on attacks.

"Session tokens and API keys are sought specifically by threat actors because it is often possible to replay those secrets and bypass credential-based authentication," Jeremy Kirk, director of threat intelligence at Okta,
[said](https://www.okta.com/blog/threat-intelligence/signing_in_without_actually_signing_in)
in a report shared with The Hacker News.

"Once successfully replayed, a threat actor is effectively logged in to an LLM service without actually logging in. Use of these skeleton keys makes abuse more challenging but not impossible to detect."

The identity services provider said it analyzed a 7 GB infostealer dump released on a Telegram channel on August 2, 2026, and found that the stealer log contained data belonging to 5,871 infected machines across 162 countries.

Among those were thousands of unexpired authentication tokens corresponding to services like Google, Microsoft, Anthropic, Amazon, Gamma, Notion, Character.ai, Cursor, Poe.com, and Pika AI. Of the 44,791 unique JSON web tokens (JWTs) from the dataset, 555 JWTs were likely related to authentication for AI services.

Similar to a session token, a valid JWT can be
[abused to obtain direct account access](https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen)
, while bypassing regular authentication using a username and password, as well as multi-factor authentication (MFA).

Okta said it also identified 2,937 authentication-related JSON Web Encryption (
[JWE](https://auth0.com/docs/secure/tokens/access-tokens/json-web-encryption)
) data structures representing encrypted JWTs. Most of these tokens are said to have been set by OpenAI, which uses NextAuth.js. Although these keys can only be decrypted and parsed by the party holding the key, it's still possible for an attacker to replay these tokens and gain access to an account as long as they are not expired.

In all, the stolen data is said to have contained 1,843 unexpired JWTs and JWEs on the day it was released. Worryingly, 17.7% of the 44,791 JWTs have been found to include plaintext personally identifiable information (PII), such as name, phone number, or email address.

"This is another problematic aspect since that information does not expire or disappear, and it directly links a user with a specific service, which could be useful for social engineering attempts or phishing," Kirk said.

One key aspect worth mentioning here is that session replay attacks may not work in scenarios where an organization uses IP allowlisting, a security feature that blocks all network traffic except for specific, approved IP addresses or ranges. In addition, Google has added support for Device Bound Session Credentials (
[DBSC](https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html)
) to Chrome to cryptographically link a session token to a device so that a stolen token cannot be used on another system.

Besides credentials and tokens, an analysis of the stealer dump using
[TruffleHog](https://github.com/trufflesecurity/trufflehog)
has unearthed 24 still-valid API keys for four AI-related services, such as Google Gemini, OpenAI, Groq, and OpenRouter. An attacker who is in possession of such a key can weaponize it for espionage, extortion, or resource theft, and rack up AI token bills.

The abuse of API keys by bad actors to gain unauthorized access to a victim's large language model (LLM) and use the services to accomplish their goals, or sell the access to other cybercriminals, is referred to as
[LLMjacking](https://thehackernews.com/2025/02/microsoft-exposes-llmjacking.html)
. The
[technique](https://www.fortinet.com/blog/threat-research/someone-else-is-using-your-ai)
is similar to campaigns that secretly use a system's resources to mine cryptocurrency, while passing the
[heavy compute bills onto the victim](https://auth0.com/blog/llmjacking-stolen-api-key-hidden-cost/)
.

As adoption of AI surges within enterprise environments, data siphoned from infostealers has diversified the portfolio for cybercriminals to monetize, with
[new black market sites](https://thehackernews.com/2026/08/poison-claude-sells-discounted-claude.html)
emerging in the threat landscape for purchasing stolen token bundles and anti-detect browsers.

In one Telegram post flagged by Okta, an unspecified vendor has been spotted selling access to Claude, Cursor, ChatGPT, and Gemini at a discounted price, in addition to offering 24x7 support and money-back guarantees. Another service called Poison Claude claims to provide access to Anthropic's Opus 4.8, Opus 4.7, Opus 4.6, and Sonnet 4.6 models.

"Accessing accounts using stolen session data requires specific tooling," Okta said. "So-called 'anti-detect' browsers have features designed to use stolen authentication data and avoid security controls."

"Other tools, such as the open-source anti-detect browser Camoufox or the automation tool SeleniumBase, can load data stolen from a browser's sessionStorage and localStorage easily from a file. Many of these tools allow users to configure proxies, enabling them to bypass 'impossible travel' detections or behavioral triggers that would otherwise flag unauthorized access."

The development comes as Google
[disclosed](https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html)
that it has observed "more personas seeking to purchase AI-related accounts and more sellers advertising these accounts" across the cybercrime underground amid growing threat actor use of AI. Posts on these forums have indicated buyer demand for Claude and Gemini credentials, in conjunction with autonomous coding IDEs like Cursor Pro and Devin.

In at least one incident response engagement handled by Google's Mandiant team, a threat actor was found to have gained initial access to a victim's cloud environment through an exposed GitHub Personal Access Token (PAT) and leveraged it to deploy unauthorized AI infrastructure and scale high-performance compute resources.

"The cost of premium model access and high-performance compute is one of the primary barriers for threat actors seeking to operationalize AI," Google Threat Intelligence Group (GTIG) said. "This has resulted in increased targeting, exfiltration, and sale of AI accounts across cybercrime communities coupled with a growing number of intrusions involving the compromise of enterprise cloud environments to hijack compute resources."

The findings highlight a pressing need to secure access to AI systems, monitor for session token reuse, scope API keys, and use OAuth 2.0 flows with short-lived tokens that expire quickly in the event they get stolen.

"As frontier model access grows more expensive, the incentive to steal rather than pay for it grows too," Kirk said. "Stronger authentication and the use of phishing-resistant technologies such as passkeys has made username-and-password takeovers harder, but it does not stop a stolen session token or API key."