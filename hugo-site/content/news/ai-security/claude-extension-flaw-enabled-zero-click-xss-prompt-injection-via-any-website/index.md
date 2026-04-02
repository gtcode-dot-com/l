---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T03:49:15.332106+00:00'
exported_at: '2026-04-02T03:49:17.712510+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/claude-extension-flaw-enabled-zero.html
structured_data:
  about: []
  author: ''
  description: Claude extension flaw enabled silent prompt injection via XSS and weak
    allowlist, risking data theft and impersonation until Feb 19, 2026 fix.
  headline: Claude Extension Flaw Enabled Zero-Click XSS Prompt Injection via Any
    Website
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/claude-extension-flaw-enabled-zero.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Claude Extension Flaw Enabled Zero-Click XSS Prompt Injection via Any Website
updated_at: '2026-04-02T03:49:15.332106+00:00'
url_hash: 3ed9939d98eb515cdeb808bc06d9f9cc7f3f0efc
---

**

Ravie Lakshmanan
**

Mar 26, 2026

Browser Security / Vulnerability

Cybersecurity researchers have disclosed a vulnerability in Anthropic's Claude Google Chrome Extension that could have been exploited to trigger malicious prompts simply by visiting a web page.

The flaw "allowed any website to silently inject prompts into that assistant as if the user wrote them," Koi Security researcher Oren Yomtov
[said](https://www.koi.ai/blog/shadowprompt-how-any-website-could-have-hijacked-anthropic-claude-chrome-extension)
in a report shared with The Hacker News. "No clicks, no permission prompts. Just visit a page, and an attacker completely controls your browser."

The issue, codenamed
**ShadowPrompt**
, chains two underlying flaws:

* An overly permissive origin allowlist in the extension that allowed any subdomain matching the pattern (\*.claude.ai) to send a prompt to Claude for execution.
* A document object model (
  [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
  )-based cross-site scripting (
  [XSS](https://owasp.org/www-community/attacks/xss/)
  ) vulnerability in an Arkose Labs CAPTCHA component hosted on "a-cdn.claude[.]ai."

Specifically, the XSS vulnerability enables the execution of arbitrary JavaScript code in the context of "a-cdn.claude[.]ai." A threat actor could leverage this behavior to inject JavaScript that issues a prompt to the Claude extension.

The extension, for its part, allows the prompt to land in Claude's sidebar as if it's a legitimate user request simply because it comes from an allow-listed domain.

"The attacker's page embeds the vulnerable Arkose component in a hidden <iframe>, sends the XSS payload via postMessage, and the injected script fires the prompt to the extension," Yomtov explained. "The victim sees nothing."

VIDEO

Successful exploitation of this vulnerability could allow the adversary to steal sensitive data (e.g., access tokens), access conversation history with the AI agent, and even perform actions on behalf of the victim (e.g., sending emails impersonating them, asking for confidential data).

Following responsible disclosure on December 27, 2025, Anthropic deployed a patch to the Chrome extension (version 1.0.41) that enforces a strict origin check requiring an exact match to the domain "claude[.]ai." Arkose Labs has since fixed the XSS flaw at its end as of February 19, 2026.

"The more capable AI browser assistants become, the more valuable they are as attack targets," Koi said. "An extension that can navigate your browser, read your credentials, and send emails on your behalf is an autonomous agent. And the security of that agent is only as strong as the weakest origin in its trust boundary."