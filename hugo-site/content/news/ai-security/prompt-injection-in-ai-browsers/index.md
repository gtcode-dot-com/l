---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T00:57:27.462308+00:00'
exported_at: '2025-11-13T00:57:34.963509+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html
structured_data:
  about: []
  author: ''
  description: 'This is why AIs are not ready to be personal assistants: A new attack
    called ‘CometJacking’ exploits URL parameters to pass to Perplexity’s Comet AI
    browser hidden instructions that allow access to sensitive data from connected
    services, like email and calendar. In a realistic scenario, no credentials or
    user interaction are required and a threat actor can leverage the attack by simply
    exposing a maliciously crafted URL to targeted users. […] CometJacking is a prompt-injection
    attack where the query string processed by the Comet AI browser contains malicious
    instructions added using the ‘collection’ parameter of the URL...'
  headline: Prompt Injection in AI Browsers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Prompt Injection in AI Browsers
updated_at: '2025-11-13T00:57:27.462308+00:00'
url_hash: 114a6b78671056d80ffb8244334044967d1998dd
---

## Prompt Injection in AI Browsers

[This](https://www.bleepingcomputer.com/news/security/commetjacking-attack-tricks-comet-browser-into-stealing-emails/)
is why AIs are not ready to be personal assistants:

> A new attack called ‘CometJacking’ exploits URL parameters to pass to Perplexity’s Comet AI browser hidden instructions that allow access to sensitive data from connected services, like email and calendar.
>
> In a realistic scenario, no credentials or user interaction are required and a threat actor can leverage the attack by simply exposing a maliciously crafted URL to targeted users.
>
> […]
>
> CometJacking is a prompt-injection attack where the query string processed by the Comet AI browser contains malicious instructions added using the ‘collection’ parameter of the URL.
>
> LayerX researchers say that the prompt tells the agent to consult its memory and connected services instead of searching the web. As the AI tool is connected to various services, an attacker leveraging the CometJacking method could exfiltrate available data.
>
> In their tests, the connected services and accessible data include Google Calendar invites and Gmail messages and the malicious prompt included instructions to encode the sensitive data in base64 and then exfiltrate them to an external endpoint.
>
> According to the researchers, Comet followed the instructions and delivered the information to an external system controlled by the attacker, evading Perplexity’s checks.

I wrote
[previously](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html)
:

> Prompt injection isn’t just a minor security problem we need to deal with. It’s a fundamental property of current LLM technology. The systems have
> [no ability to separate trusted commands from untrusted data](https://www.schneier.com/blog/archives/2024/05/llms-data-control-path-insecurity.html)
> , and there are an infinite number of prompt injection attacks with
> [no way to block them](https://llm-attacks.org/)
> as a class. We need some new fundamental science of LLMs before we can solve this.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[browsers](https://www.schneier.com/tag/browsers/)
,
[cyberattack](https://www.schneier.com/tag/cyberattack/)
,
[LLM](https://www.schneier.com/tag/llm/)

[Posted on November 11, 2025 at 7:08 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html)
•
[11 Comments](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.