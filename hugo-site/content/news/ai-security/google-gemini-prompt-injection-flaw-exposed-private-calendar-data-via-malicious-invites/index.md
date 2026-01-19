---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-19T18:15:13.062639+00:00'
exported_at: '2026-01-19T18:15:15.331284+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html
structured_data:
  about: []
  author: ''
  description: Researchers found an indirect prompt injection flaw in Google Gemini
    that bypassed Calendar privacy controls and exposed private meeting data.
  headline: Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via
    Malicious Invites
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious
  Invites
updated_at: '2026-01-19T18:15:13.062639+00:00'
url_hash: 2485b428446a6a68fef4fef9054a82d819823cd5
---

Cybersecurity researchers have disclosed details of a security flaw that leverages indirect prompt injection targeting Google Gemini as a way to bypass authorization guardrails and use Google Calendar as a data extraction mechanism.

The vulnerability, Miggo Security's Head of Research, Liad Eliyahu, said, made it possible to circumvent Google Calendar's privacy controls by hiding a dormant malicious payload within a standard calendar invite.

"This bypass enabled unauthorized access to private meeting data and the creation of deceptive calendar events without any direct user interaction," Eliyahu
[said](https://www.miggo.io/post/weaponizing-calendar-invites-a-semantic-attack-on-google-gemini)
in a report shared with The Hacker News.

The starting point of the attack chain is a new calendar event that's crafted by the threat actor and sent to a target. The invite's description embeds a natural language prompt that's designed to do their bidding, resulting in a prompt injection.

The attack gets activated when a user asks Gemini a completely innocuous question about their schedule (e.g., Do I have any meetings for Tuesday?), prompting the artificial intelligence (AI) chatbot to parse the specially crafted prompt in the aforementioned event's description to summarize all of users' meetings for a specific day, add this data to a newly created Google Calendar event, and then return a harmless response to the user.

"Behind the scenes, however, Gemini created a new calendar event and wrote a full summary of our target user's private meetings in the event's description," Miggo said. "In many enterprise calendar configurations, the new event was visible to the attacker, allowing them to read the exfiltrated private data without the target user ever taking any action."

Although the issue has since been addressed following responsible disclosure, the findings once again illustrate that AI-native features can broaden the attack surface and inadvertently introduce new security risks as more organizations use AI tools or build their own agents internally to automate workflows.

"AI applications can be manipulated through the very language they're designed to understand," Eliyahu noted. "Vulnerabilities are no longer confined to code. They now live in language, context, and AI behavior at runtime."

The disclosure comes days after Varonis detailed an attack named
[Reprompt](https://thehackernews.com/2026/01/researchers-reveal-reprompt-attack.html)
that could have made it possible for adversaries to exfiltrate sensitive data from artificial intelligence (AI) chatbots like Microsoft Copilot in a single click, while bypassing enterprise security controls.

The findings illustrate the need for
[constantly evaluating](https://phare.giskard.ai/)
large language models (LLMs) across key safety and security dimensions, testing their penchant for hallucination, factual accuracy, bias, harm, and jailbreak resistance, while simultaneously securing AI systems from traditional issues.

Just last week, Schwarz Group's XM Cyber revealed new ways to escalate privileges inside Google Cloud Vertex AI's Agent Engine and Ray, underscoring the need for enterprises to audit every service account or identity attached to their AI workloads.

"These vulnerabilities allow an attacker with minimal permissions to hijack high-privileged Service Agents, effectively turning these 'invisible' managed identities into 'double agents' that facilitate privilege escalation," researchers Eli Shparaga and Erez Hasson
[said](https://xmcyber.com/blog/double-agent-service-agent-privilege-escalation-in-google-vertex-ai/)
.

Successful exploitation of the double agent flaws could permit an attacker to read all chat sessions, read LLM memories, and read potentially sensitive information stored in storage buckets, or obtain root access to the Ray cluster. With Google stating that the services are currently "working as intended," it's essential that organizations review identities with the Viewer role and ensure adequate controls are in place to prevent unauthorized code injection.

The development coincides with the discovery of multiple vulnerabilities and weaknesses in different AI systems -

* [Security flaws](https://kb.cert.org/vuls/id/383552)
  (CVE-2026-0612, CVE-2026-0613, CVE-2026-0615, and CVE-2026-0616) in The Librarian, an AI-powered personal assistant tool provided by TheLibrarian.io, that
  [enable an attacker](https://mindgard.ai/blog/thelibrarian-ios-ai-security-disclosure)
  to access its internal infrastructure, including the administrator console and cloud environment, and ultimately leak sensitive information, such as cloud metadata, running processes within the backend, and system prompt, or log in to its internal backend system.
* A vulnerability that
  [demonstrates](https://www.praetorian.com/blog/exploiting-llm-write-primitives-system-prompt-extraction-when-chat-output-is-locked-down/)
  how system prompts can be extracted from intent-based LLM assistants by prompting them to display the information in Base64-encoded format in form fields. "If an LLM can execute actions that write to any field, log, database entry, or file, each becomes a potential exfiltration channel, regardless of how locked down the chat interface is," Praetorian said.
* An attack that
  [demonstrates](https://www.promptarmor.com/resources/hijacking-claude-code-via-injected-marketplace-plugins)
  how a
  [malicious plugin](https://code.claude.com/docs/en/discover-plugins)
  uploaded to a marketplace for Anthropic Claude Code can be used to bypass human-in-the-loop protections via
  [hooks](https://docs.claude.com/en/docs/claude-code/hooks#json-output-example%3A-pretooluse-with-approval)
  and exfiltrate a user's files via indirect prompt injection.
* A critical vulnerability in Cursor (
  [CVE-2026-22708](https://github.com/cursor/cursor/security/advisories/GHSA-82wg-qcm4-fp2w)
  ) that enables remote code execution via indirect prompt injection by exploiting a fundamental oversight in how agentic IDEs handle shell built-in commands. "By abusing implicitly trusted shell built-ins like export, typeset, and declare, threat actors can silently manipulate environment variables that subsequently poison the behavior of legitimate developer tools," Pillar Security
  [said](https://www.pillar.security/blog/the-agent-security-paradox-when-trusted-commands-in-cursor-become-attack-vectors)
  . "This attack chain converts benign, user-approved commands -- such as git branch or python3 script.py -- into arbitrary code execution vectors."

A security analysis of five Vibe coding IDEs, viz. Cursor, Claude Code, OpenAI Codex, Replit, and Devin, who found coding agents, are good at avoiding SQL injections or XSS flaws, but struggle when it comes to handling SSRF issues, business logic, and enforcing appropriate authorization when accessing APIs. To make matters worse, none of the tools included CSRF protection, security headers, or login rate limiting.

The test highlights the current limits of vibe coding, showing that human oversight is still key to addressing these gaps.

"Coding agents cannot be trusted to design secure applications," Tenzai's Ori David
[said](https://blog.tenzai.com/bad-vibes-comparing-the-secure-coding-capabilities-of-popular-coding-agents/)
. While they may produce secure code (some of the time), agents consistently fail to implement critical security controls without explicit guidance. Where boundaries aren't clear-cut – business logic workflows, authorization rules, and other nuanced security decisions – agents will make mistakes."