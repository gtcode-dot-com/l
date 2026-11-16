---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-16T18:21:51.742765+00:00'
exported_at: '2026-11-16T18:21:53.789153+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html
structured_data:
  about: []
  author: ''
  description: Amazon's decoy records show suspected ARTEX agents hunting AI provider
    keys across exposed apps, but reported theft remains unverified.
  headline: Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps
    for API Keys
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps for
  API Keys
updated_at: '2026-11-16T18:21:51.742765+00:00'
url_hash: f159cf23a7b20d4c61ef2119409a560217d5e068
---

Attackers' AI agents have been hunting for weak spots in internet-exposed AI apps such as
**LiteLLM**
,
**One API**
, and
**Dify**
to steal the AI provider keys stored inside, according to the agents' own records.

The records, which Amazon's threat intelligence team captured with decoy servers, describe stolen keys being used to run the AI models that powered the search for more keys.

The team said this week that it cannot verify the outcomes reported by the agents. It has moderate confidence that the agents ran on
**ARTEX**
, an open-source AI tool for penetration testing.

The records include a playbook of known entry points for each targeted product. It lists default administrator credentials such as LiteLLM's default master key, unfinished installs that an outsider could take over, and known flaws in
**Langflow**
and
**RAGFlow**
.

In a separate case reported this week, Cloudflare's incident responders saw ARTEX gain access to a compromised API token that had been used for CI/CD. The token had no IP restrictions or rate limiting, and the activity that followed included 400 database dump requests in an hour. The company has not said whether those requests returned any data.

An operator gives ARTEX a target and a goal, and a planner agent splits the goal into tasks for worker agents that run security tools. To decide each next step, the agents send their work to a large language model (LLM).

The decoy servers, part of a network called
**MadPot**
, posed as popular LLM services. From October 3 to late last week, the agents sent it requests that often carried a campaign's full history, including the operators' instructions and the agents' reported findings.

Those
[captured agent records](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/)
describe work done on systems MadPot does not watch. "Amazon Threat Intelligence did not observe that activity as it happened and cannot verify the outcomes the agents reported, but the records show what the actors were pursuing," the team said.

The team assessed, with moderate confidence, that the operators were separate China-linked groups, citing Simplified Chinese prompts and China time zone settings, among other evidence.

In the main campaign, the agents looked for internet-exposed AI apps, extracted the provider keys stored inside, verified that the keys worked, and added them to a shared pool. They focused on apps that hold keys for many providers, because one weak admin page there can expose many accounts.

Targets named in the records include LLM gateways and proxies such as One API, New API, Veloera, Sub2API and LiteLLM, and AI app builders such as Dify, FastGPT, Langflow, RAGFlow, Open WebUI, LobeChat and Ollama.

The playbook also covers management and provider settings endpoints that need no login, an authentication bypass through the isCliRequest header in One API family systems, and server-side request forgery (SSRF) through URL-fetch features to reach cloud metadata services. Other entries cover secrets left in client-side JavaScript, source maps, debug routes and environment files.

When the agents found cloud credentials, they targeted managed services that host AI models, secret stores, and application identities, prioritizing premium AI models over general cloud access.

To find leaked keys, the agents used internet scanning services and certificate transparency logs, and searched GitHub repositories and event archives, npm and PyPI packages, container image layers, notebooks, model-hosting spaces, paste sites, and Telegram channels.

The records cover hundreds of targets across AI app platforms and other systems. The team notified AWS customers who may have been affected.

Microsoft reported last week that attackers were using agentic AI tools such as ARTEX for
[GitHub secret hunting](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)
, looking for exposed credentials that included API keys for AI inference.

On August 26, the company described an
[earlier RAGFlow attack](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html)
, in which a hidden hook captured AI provider keys as users entered them, and a compromise of a LiteLLM gateway that exposed provider keys.

In its
[RAGFlow case study](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)
, the company had only low confidence about which flaw, if any, let the attackers run code. It did not link those attacks to ARTEX.

The decoy records also describe a second campaign in which agents attempted to bypass identity checks at two cryptocurrency exchanges using deepfakes.

One verification vendor's server rejected the live deepfake video on every attempt the agents made to record it. The team did not say whether the forged photos of ID documents that the agents also fabricated passed document checks.

Over the past eight weeks, Cloudflare's incident responders were called into multiple investigations involving ARTEX and tools built from it.

In more than one incident, an attacker gained access to a customer's environment with a major cloud provider and moved directly into the customer's Cloudflare account. The common root cause was static CI/CD tokens that never expired, granting broad access across the customer's cloud setup, according to the company.

In the ARTEX case, the compromised token was an account-level API token. The compromise most likely came through a third-party cloud provider, according to the company's
[incident findings](https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/)
. How the token was first stolen has not been disclosed.

New Worker scripts with names such as artex-\*, artex-pgrecon-\*, artex-pgw-\* and artex-do-\* appeared in the account, each name matching a different task. The activity ran at more than 69 requests per minute across several parts of the account. It included attempts to establish persistence and validate session tokens for other third-party apps.

Much of this activity was lightly guided by a human operator, the company believes. Whether any attempt at persistence worked has not been disclosed.

Over three days this week, more than 50 families of AI penetration testing frameworks tried to scan the company's customers, and the IP addresses seen running such frameworks now number in the thousands.

The FBI said in a
[FLASH alert](https://www.ic3.gov/CSA/2026/261113.pdf)
this week that a range of attackers have used ARTEX since at least August against organizations in many sectors around the world. The alert summarizes 11 earlier reports and describes no new incident.

ARTEX's developer made its GitHub repository unavailable on October 8 after reports of abuse, but community forks, archived copies, and a commercial version called ARTEX PRO keep it available.

The alert's examples include an
[earlier campaign](https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html)
against South Korean financial institutions that stole personal information on about 67,000 people, and the
[ConnectWise compromise](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)
.

### What Defenders Can Check

"None of the techniques in these campaigns were new. What AI agents change is the speed and persistence of the attacker," Amazon's threat intelligence team said. The agents succeeded where basic security was missing, including default or hard-coded credentials, keys left in code and public files, interfaces and inference endpoints without authentication, and unpatched software.

The team recommends treating AI apps, model gateways, and inference endpoints like other production systems, assuming that exposed secrets will be found quickly, and watching for misuse through unexpected spending or unusual usage.

Here is the status of the flaws named in the playbook:

| Product | Flaw | Status |
| --- | --- | --- |
| Langflow | CVE-2025-3248, missing authentication that lets a remote attacker run code | Versions before 1.3.0 are affected, and 1.3.0 is the fixed version ( [release notes](https://github.com/langflow-ai/langflow/releases/tag/1.3.0) ). CISA added the flaw to its Known Exploited Vulnerabilities (KEV) catalog on May 5, 2025, after [earlier Langflow exploitation](https://thehackernews.com/2025/05/critical-langflow-flaw-added-to-cisa.html) , and the [KEV entry](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-3248) marks it as known to be used in ransomware campaigns. |
| RAGFlow | CVE-2026-28797, server-side template injection (SSTI) that lets any logged-in user run operating system commands on the server. The attack needs a registered account, and self-registration is on by default, the [security advisory](https://github.com/infiniflow/ragflow/security/advisories/GHSA-vvwj-fvwh-4whx) says. | NVD lists 0.24.0 and earlier as affected. The advisory lists no patched version. Version 0.25.0, released on April 21, renders templates in the sandbox the advisory recommends, according to its [SSTI fix notes](https://github.com/infiniflow/ragflow/releases/tag/v0.25.0) . |
| One API family | Authentication bypass through the `isCliRequest` header | The team's report names no affected versions or fix. |

Other checks that apply to these attacks:

* Change default administrator credentials, such as LiteLLM's default master key, and do not leave a new install unfinished where an outsider could take it over.
* Search configuration files, environment variables, deployment scripts, CI/CD pipelines and databases for embedded secrets, keep scanning repositories and container images for exposed ones, and rotate exposed credentials quickly, as the FBI advises.
* Give Cloudflare API tokens an expiry date and limit the client IP addresses that can use them. Both are optional
  [token restriction settings](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)
  , and new tokens carry a
  `cfut_`
  prefix that secret scanners can detect.
* Look for Cloudflare Worker scripts named
  `artex-*`
  ,
  `artex-pgrecon-*`
  ,
  `artex-pgw-*`
  or
  `artex-do-*`
  .
* Check logs for the 11 IP addresses published with the decoy findings, and for the more than 2,500 addresses that researchers at Cisco Talos link to ARTEX in their
  [indicator files](https://github.com/Cisco-Talos/IOCs/tree/main/2026/11)
  .
* The researchers'
  [detection rules](https://blog.talosintelligence.com/artex-and-beyond/)
  for ARTEX are Snort 3 rules 7:76, 7:77 and 7:78, and Snort 2 rules 1:67494, 1:67495 and 1:67496. Rules 7:78 and 1:67496 are off by default and detect traces of norma, the agent harness ARTEX uses.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.