---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-14T18:15:14.233852+00:00'
exported_at: '2026-03-14T18:15:16.454829+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html
structured_data:
  about: []
  author: ''
  description: CNCERT warns OpenClaw AI agent has weak defaults enabling prompt injection
    and data leaks, prompting China to restrict use on government systems.
  headline: OpenClaw AI Agent Flaws Could Enable Prompt Injection and Data Exfiltration
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenClaw AI Agent Flaws Could Enable Prompt Injection and Data Exfiltration
updated_at: '2026-03-14T18:15:14.233852+00:00'
url_hash: 63d09163b9de4f9c50ac9967ddb3f7d3fa2eca95
---

**

Ravie Lakshmanan
**

Mar 14, 2026

Artificial Intelligence / Endpoint Security

China's National Computer Network Emergency Response Technical Team (CNCERT) has
[issued](https://mp.weixin.qq.com/s/0M1sZq1HqwAAaMbRDBEZEw)
a warning about the security stemming from the use of
[OpenClaw](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)
(formerly Clawdbot and Moltbot), an open-source and self-hosted autonomous artificial intelligence (AI) agent.

In a post shared on WeChat, CNCERT noted that the platform's "inherently weak default security configurations," coupled with its privileged access to the system to facilitate autonomous task execution capabilities, could be explored by bad actors to seize control of the endpoint.

This includes risks arising from prompt injections, where malicious instructions embedded within a web page can cause the agent to leak sensitive information if it's tricked into accessing and consuming the content.

The attack is also
[referred](https://securelist.com/indirect-prompt-injection-in-the-wild/113295/)
to as indirect prompt injection (IDPI) or cross-domain prompt injection (XPIA), as adversaries, instead of interacting directly with a large language model (LLM), weaponize benign AI features like web page summarization or content analysis to
[run manipulated instructions](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)
. This can
[range from](https://www.pillar.security/blog/anatomy-of-an-indirect-prompt-injection)
evading AI-based ad review systems and influencing hiring decisions to search engine optimization (SEO) poisoning and generating biased responses by suppressing negative reviews.

OpenAI, in a blog post published earlier this week, said prompt injection-style attacks are evolving beyond simply placing instructions in external content to include elements of social engineering.

"AI agents are increasingly able to browse the web, retrieve information, and take actions on a user's behalf," it
[said](https://openai.com/index/designing-agents-to-resist-prompt-injection/)
. "Those capabilities are useful, but they also create new ways for attackers to try to manipulate the system."

The prompt injection risks in OpenClaw are not hypothetical. Last month, researchers at PromptArmor found that the
[link preview feature](https://www.aitextrisk.com/)
in messaging apps like Telegram or Discord can be turned into a data exfiltration pathway when communicating with OpenClaw by means of an indirect prompt injection.

The idea, at a high level, is to trick the AI agent into generating an attacker-controlled URL that, when rendered in the messaging app as a link preview, automatically causes it to transmit confidential data to that domain without having to click on the link.

"This means that in agentic systems with link previews, data exfiltration can occur immediately upon the AI agent responding to the user, without the user needing to click the malicious link," the AI security company
[said](https://www.promptarmor.com/resources/llm-data-exfiltration-via-url-previews-(with-openclaw-example-and-test))
. "In this attack, the agent is manipulated to construct a URL that uses an attacker's domain, with dynamically generated query parameters appended that contain sensitive data the model knows about the user."

Besides rogue prompts, CNCERT has also highlighted three other concerns -

* The possibility that OpenClaw may inadvertently and irrevocably delete critical information due to its misinterpretation of user instructions.
* Threat actors can
  [upload malicious skills](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)
  to repositories like ClawHub that, when installed, run arbitrary commands or deploy malware.
* Attackers can exploit
  [recently disclosed security vulnerabilities](https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html)
  in OpenClaw to compromise the system and leak sensitive data.

"For critical sectors – such as finance and energy – such breaches could lead to the leakage of core business data, trade secrets, and code repositories, or even result in the complete paralysis of entire business systems, causing incalculable losses," CNCERT added.

To counter these risks, users and organizations are advised to strengthen network controls, prevent exposure of OpenClaw's default management port to the internet, isolate the service in a container, avoid storing credentials in plaintext, download skills only from trusted channels, disable automatic updates for skills, and keep the agent up-to-date.

The development comes as Chinese authorities have moved to restrict state-run enterprises and government agencies from running OpenClaw AI apps on office computers in a bid to contain security risks, Bloomberg
[reported](https://www.bloomberg.com/news/articles/2026-03-11/china-moves-to-limit-use-of-openclaw-ai-at-banks-government-agencies)
. The ban is also said to extend to the families of military personnel.

The viral popularity of OpenClaw has also led threat actors to capitalize on the phenomenon to distribute malicious GitHub repositories posing as OpenClaw installers to deploy information stealers like Atomic and Vidar Stealer, and a Golang-based proxy malware known as
[GhostSocks](https://synthient.com/blog/ghostsocks-from-initial-access-to-residential-proxy)
using
[ClickFix-style instructions](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
.

"The campaign did not target a particular industry, but was broadly targeting users attempting to install OpenClaw with the malicious repositories containing download instructions for both Windows and macOS environments," Huntress
[said](https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer)
. "What made this successful was that the malware was hosted on GitHub, and the malicious repository became the top-rated suggestion in Bing’s AI search results for OpenClaw Windows."