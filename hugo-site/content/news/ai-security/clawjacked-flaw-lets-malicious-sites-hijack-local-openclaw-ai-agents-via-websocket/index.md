---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-01T02:28:55.926199+00:00'
exported_at: '2026-03-01T02:29:00.061769+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html
structured_data:
  about: []
  author: ''
  description: OpenClaw patches ClawJacked flaw, log poisoning bug, and multiple CVEs
    as 71 malicious ClawHub skills spread malware and crypto scams.
  headline: ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via
    WebSocket
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket
updated_at: '2026-03-01T02:28:55.926199+00:00'
url_hash: 79761b668f54bea7c19c7b91e8b2665053e03ddb
---

OpenClaw has fixed a high-severity security issue that, if successfully exploited, could have allowed a malicious website to connect to a locally running artificial intelligence (AI) agent and take over control.

"Our vulnerability lives in the core system itself – no plugins, no marketplace, no user-installed extensions – just the bare OpenClaw gateway, running exactly as documented," Oasis Security
[said](https://www.oasis.security/blog/openclaw-vulnerability)
in a report published this week.

The flaw has been codenamed
**ClawJacked**
by the cybersecurity company.

The attack assumes the following threat model: A developer has
[OpenClaw](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html)
set up and running on their laptop, with its
[gateway](https://docs.openclaw.ai/cli/gateway)
, a local WebSocket server, bound to localhost and protected by a password. The attack kicks in when the developer lands on an attacker-controlled website through social engineering or some other means.

The infection sequence then follows the steps below -

* Malicious JavaScript on the web page opens a WebSocket connection to localhost on the OpenClaw gateway port.
* The script brute-forces the gateway password by taking advantage of a missing rate-limiting mechanism.
* Post successful authentication with admin-level permissions, the script stealthily registers as a trusted device, which is auto-approved by the gateway without any user prompt.
* The attacker gains complete control over the AI agent, allowing them to interact with it, dump configuration data, enumerate connected nodes, and read application logs.

"Any website you visit can open one to your localhost. Unlike regular HTTP requests, the browser doesn't block these cross-origin connections," Oasis Security said. "So while you're browsing any website, JavaScript running on that page can silently open a connection to your local OpenClaw gateway. The user sees nothing."

"That misplaced trust has real consequences. The gateway relaxes several security mechanisms for local connections - including silently approving new device registrations without prompting the user. Normally, when a new device connects, the user must confirm the pairing. From localhost, it's automatic."

Following responsible disclosure, OpenClaw pushed a fix in less than 24 hours with
[version 2026.2.25](https://github.com/openclaw/openclaw/releases/tag/v2026.2.25)
released on February 26, 2026. Users are advised to apply the latest updates as soon as possible, periodically audit access granted to AI agents, and enforce appropriate governance controls for non-human (aka agentic) identities.

The development comes amid a broader security scrutiny of the OpenClaw ecosystem, primarily stemming from the fact that AI agents hold entrenched access to disparate systems and the authority to execute tasks across enterprise tools, leading to a significantly larger blast radius should they be compromised.

Reports from
[Bitsight](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances)
and
[NeuralTrust](https://neuraltrust.ai/blog/openclaw-moltbook)
have detailed how OpenClaw instances left connected to the internet pose an expanded attack surface, with each integrated service further broadening the blast radius and can be transformed into an attack weapon by embedding prompt injections in content (e.g., an email or a Slack message) processed by the agent to execute malicious actions.

The disclosure comes as OpenClaw also patched a log poisoning vulnerability that allowed attackers to write malicious content to log files via WebSocket requests to a publicly accessible instance on TCP port 18789.

Since the agent reads its own logs to troubleshoot certain tasks, the security loophole could be abused by a threat actor to embed indirect prompt injections, leading to unintended consequences. The
[issue](https://github.com/openclaw/openclaw/security/advisories/GHSA-g27f-9qjv-22pm)
was addressed in
[version 2026.2.13](https://github.com/openclaw/openclaw/releases/tag/v2026.2.13)
, which was shipped on February 14, 2026.

"If the injected text is interpreted as meaningful operational information rather than untrusted input, it could influence decisions, suggestions, or automated actions," Eye Security
[said](https://research.eye.security/log-poisoning-in-openclaw/)
. "The impact would therefore not be 'instant takeover,' but rather: manipulation of agent reasoning, influencing troubleshooting steps, potential data disclosure if the agent is guided to reveal context, and indirect misuse of connected integrations."

VIDEO

In recent weeks, OpenClaw has also been found susceptible to multiple vulnerabilities (
[CVE-2026-25593](https://github.com/openclaw/openclaw/security/advisories/GHSA-g55j-c2v4-pjcg)
,
[CVE-2026-24763](https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v)
,
[CVE-2026-25157](https://github.com/openclaw/openclaw/security/advisories/GHSA-q284-4pvr-m585)
,
[CVE-2026-25475](https://github.com/openclaw/openclaw/security/advisories/GHSA-r8g4-86fx-92mq)
,
[CVE-2026-26319, CVE-2026-26322, CVE-2026-26329](https://www.endorlabs.com/learn/how-ai-sast-traced-data-flows-to-uncover-six-openclaw-vulnerabilities)
), ranging from moderate to high severity, that could result in remote code execution, command injection, server-side request forgery (SSRF), authentication bypass, and path traversal. The vulnerabilities have been addressed in OpenClaw versions
[2026.1.20](https://github.com/openclaw/openclaw/releases/tag/v2026.1.20)
,
[2026.1.29](https://github.com/openclaw/openclaw/releases/tag/v2026.1.29)
,
[2026.2.1](https://github.com/openclaw/openclaw/releases/tag/v2026.2.1)
,
[2026.2.2](https://github.com/openclaw/openclaw/releases/tag/v2026.2.2)
, and
[2026.2.14](https://github.com/openclaw/openclaw/releases/tag/v2026.2.14)
.

"As AI agent frameworks become more prevalent in enterprise environments, security analysis must evolve to address both traditional vulnerabilities and AI-specific attack surfaces," Endor Labs said.

Elsewhere, new research has demonstrated that malicious skills uploaded to ClawHub, an open marketplace for downloading OpenClaw skills, are being used as conduits to deliver a new variant of
[Atomic Stealer](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)
, a macOS information stealer developed and rented by a cybercrime actor known as
[Cookie Spider](https://www.crowdstrike.com/en-us/adversaries/cookie-spider/)
.

"The infection chain begins with a normal SKILL.md that installs a prerequisite," Trend Micro
[said](https://www.trendmicro.com/en_us/research/26/b/openclaw-skills-used-to-distribute-atomic-macos-stealer.html)
. "The skill appears harmless on the surface and was even labeled as benign on VirusTotal. OpenClaw then goes to the website, fetches the installation instructions, and proceeds with the installation if the LLM decides to follow the instructions."

The instructions hosted on the website "openclawcli.vercel[.]app" include a malicious command to download a stealer payload from an external server ("91.92.242[.]30") and run it.

Threat hunters have also flagged a new
[malware delivery campaign](https://openguardrails.com/blog/clawhub-trojan-liucomment-malware-campaign)
in which a threat actor by the name @liuhui1010 has been identified, leaving comments on legitimate skill listing pages, urging users to explicitly run a command they provided on the Terminal app if the skill "doesn't work on macOS."

The command is designed to retrieve Atomic Stealer from "91.92.242[.]30," an IP address previously documented by
[Koi Security and OpenSourceMalware](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)
for distributing the same malware via malicious skills uploaded to ClawHub.

What's more, a recent analysis of 3,505 ClawHub skills by AI security company Straiker has
[uncovered](https://www.straiker.ai/blog/built-on-clawhub-spread-on-moltbook-the-new-agent-to-agent-attack-chain)
no less than 71 malicious ones, some of which posed as legitimate cryptocurrency tools but contained hidden functionality to redirect funds to threat actor-controlled wallets.

Two other skills, bob-p2p-beta and runware, have been attributed to a multi-layered cryptocurrency scam that employs an agent-to-agent attack chain targeting the AI agent ecosystem. The skills have been attributed to a threat actor who operates under the aliases "26medias" on ClawHub and "BobVonNeumann" on
[Moltbook](https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html)
and X.

"BobVonNeumann presents itself as an AI agent on Moltbook, a social network designed for agents to interact with each other," researchers Yash Somalkar and Dan Regalado said. "From that position, it promotes its own malicious skills directly to other agents, exploiting the trust that agents are designed to extend to each other by default. It's a supply chain attack with a social engineering layer built on top."

What bob-p2p-beta does, however, is instruct other AI agents to store Solana wallet private keys in plaintext, purchase worthless $BOB tokens on pump.fun, and route all payments through an attacker-controlled infrastructure. The second skill claims to offer a benign image generation tool to build the developer's credibility.

Given that ClawHub is becoming a new fertile ground for attackers, users are advised to audit skills before installing them, avoid providing credentials and keys unless it's essential, and monitor skill behavior.

The security risks associated with self-hosted agent runtimes like OpenClaw have also prompted Microsoft to issue an advisory, warning that unguarded deployment could pave the way for credential exposure/exfiltration, memory modification, and host compromise if the agent can be tricked into retrieving and running malicious code either through poisoned skills or prompt injections.

"Because of these characteristics, OpenClaw should be treated as untrusted code execution with persistent credentials," the Microsoft Defender Security Research Team
[said](https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/)
. "It is not appropriate to run on a standard personal or enterprise workstation."

"If an organization determines that OpenClaw must be evaluated, it should be deployed only in a fully isolated environment such as a dedicated virtual machine or separate physical system. The runtime should use dedicated, non-privileged credentials and access only non-sensitive data. Continuous monitoring and a rebuild plan should be part of the operating model."