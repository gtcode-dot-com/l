---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-05T04:38:19.623524+00:00'
exported_at: '2026-10-05T04:38:20.841176+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html
structured_data:
  about: []
  author: ''
  description: Carbonato targets unauthenticated Docker daemons, installs Hermes Agent,
    and uses Telegram to run operator-directed AI-generated commands.
  headline: Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled
    Hermes AI Agent
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes
  AI Agent
updated_at: '2026-10-05T04:38:19.623524+00:00'
url_hash: 0254725a880e170880999ae65b859035ae26e557
---

Cybersecurity researchers have disclosed details of a new botnet malware called
**Carbonato**
that's targeting exposed Docker daemons to deploy an open-source artificial intelligence (AI) agent framework called
[Hermes Agent](https://hermes-agent.nousresearch.com/)
.

"The implant installs the framework unchanged, then overwrites its SOUL.md persona file," ThreatDown
[said](https://www.threatdown.com/blog/carbonato/)
. "The 39-line prompt directs it to execute tasks received through Telegram, maintain persistence, and collect credentials."

At a high level, the botnet breaks into Docker daemons exposed without authentication on port 2375 and scans neighboring networks every five minutes to propagate further. On each host, it installs Hermes Agent with instructions to follow operators' Telegram commands.

The cybersecurity company said it found the operation through an unauthenticated Docker registry that's been publicly accessible since May 2026. The staged data has been found to include details of the botnet and a separate campaign that distributed trojanized cryptocurrency wallet apps.

CARBONATO possesses worm-like capabilities in that it can spread to other hosts with unauthenticated Docker daemons. Once a host is discovered, it launches a privileged container and run commands on the underlying system.

"It uses a privileged​ ​container​ ​to​ ​run​ ​commands​ ​on​ ​each​ ​host,​ ​establishes​ ​persistence and remote access, then scans nearby networks for further Docker daemons," ThreatDown said. "Hermes​​ Agent​​ gives ​​the​ ​operators​​ a​​ Telegram​​ interface ​​to ​​send ​​tasks ​​to ​​compromised​​ hosts,​​ and​​ its persona names AI API keys and other credentials as the priority."

All of this is achieved by means of a shell script that launches a reverse SSH tunnel​​ from the victim to a relay located in Costa Rica, after which it installs an SSH server with the operators' key and reports the new deployment through Telegram with the container details.

The malware also takes steps to evade detection by masquerading as a system component and establishes persistence using cron jobs and watchdog scripts that ensure the implant is re-launched if the malicious artifacts are removed.

With the persistence set up, the next step involves deploying the Hermes Agent and overwriting its SOUL.md persona file with a custom prompt that asks the AI tool to assume the role of a "senior hacker, pentester, and exploit developer" named GH0ST and instructs it to "maintain persistence, respond over Telegram, and execute any operation the operator asks" without "moral or ethical restrictions."

The agent then enters into an interactive command loop that interprets incoming tasks through Telegram and forwards them to the appropriate large language model (LLM) gateway. The model then writes the terminal commands that are executed by the agent and returns the results back to the threat actor over the messaging platform.

The activity has not been attributed to any known threat actor or group. Language, timezone, and infrastructure clues indicate that the operators are based in Costa Rica.

### Rising Attack-Chain Automation

The disclosure comes amid growing threat actor use of AI tools and models to automate various aspects of the cyber attack lifecycle and offload offensive work.

In July 2026, Palo Alto Networks
[linked](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)
a China-based threat actor dubbed "knaithe" and "KnYuan" to an AI-enabled hacking campaign that leveraged DeepSeek, via the Hermes Agent framework configured to accept instructions over Telegram, to enumerate targets, source exploit tools, and launch attacks without human intervention.

That same month, Hunt.io also
[highlighted](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent)
another operation in which attackers used Hermes Agent in unattended "YOLO" mode to target Thailand's Ministry of Finance (MOF), ultimately breaching multiple systems within the network.

"The combination is what stands apart: an AI agent coordinating the work, a cross-platform implant holding access, and scripts written for this specific target," Hunt.io said. "Together they describe an operator who invested significant preparation into penetrating a single government target."

As recently as last week, Gambit Security said it identified a Chinese-speaking financially motivated operator running three open-source AI harnesses against hundreds of online retailers, compromising at least 27 companies, stealing over 600,000 credit card details from two entities, and injecting skimmer scripts into five online stores.

The activity, which has been ongoing since July 2026, uses AI at all stages of the attack, with results of one informing the next -

* Strix, an AI penetration testing tool for vulnerability hunting
* Cairn, an autonomous penetration testing engine for autonomous end-to-end exploitation by launching 105 attack projects between September 10 and 15, 2026, using DeepSeek v4.1 Flash
* Hermes, for orchestration, post-exploitation, tactical guidance, and directing the malicious activity using Anthropic Claude Opus 4.6

The threat actor is said to have loaded the Chinese system persona titled "SOUL - Red Team Operator" onto Hermes Agent and carried out the attack largely without any human involvement, and erased the card data from the victims' Magento database once the data had been exfiltrated.

The stolen card details correspond to victims from the U.S., the U.A.E., Saudi Arabia, the U.K., New Zealand, Ireland, Singapore, Kuwait, Australia, and Hong Kong.

"At very low cost, the AI tools demonstrated a level of patience, persistence, and creativity that most human attackers would be unlikely to sustain in this kind of attack, and achieved far greater results, far faster," security researcher Eyal Sela
[said](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)
. "Organizations must adapt to a reality where attacks are significantly faster and more comprehensive by shifting to a resilience-first mentality and a security stack that matches the AI speed."

The findings also coincide with the discovery of a new Go-based Windows implant called
[CLOSEDQUORUM](https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html)
that can query up to four LLM providers, namely DeepSeek, Alibaba Qwen, Mistral, and Google Gemini (and in this order), to autonomously determine the next course of action during the post-compromise stage of an attack.

The voting system allows the malware to take a predefined set of actions based on the winning decision, thereby automating the command-and-control (C2) chain and eliminating the need for continuous attacker commands. These actions include credential theft, shellcode injection using process hollowing or Early Bird APC injection, persistence, and likely lateral movement.

"CLOSEDQUORUM appears to operate as an operator-configured service rather than malware deployed directly by its developer," Cisco Talos said. "DeepSeek holds the deciding vote in any tie. If DeepSeek failed and isn't in the quorum, Qwen's vote is the deciding vote, and so on down the priority order. The tie behavior is fully deterministic and biased toward DeepSeek."