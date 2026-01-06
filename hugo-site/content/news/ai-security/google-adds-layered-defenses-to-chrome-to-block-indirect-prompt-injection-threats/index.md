---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-10T00:03:08.352774+00:00'
exported_at: '2025-12-10T00:03:10.583976+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/google-adds-layered-defenses-to-chrome.html
structured_data:
  about: []
  author: ''
  description: Chrome adds new layered defenses to block prompt injections, restrict
    origin access, and prevent unsafe AI actions.
  headline: Google Adds Layered Defenses to Chrome to Block Indirect Prompt Injection
    Threats
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/google-adds-layered-defenses-to-chrome.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Adds Layered Defenses to Chrome to Block Indirect Prompt Injection Threats
updated_at: '2025-12-10T00:03:08.352774+00:00'
url_hash: cb0c3e3062f17e4da0fedd4e83d245b4f506b7a6
---

Google on Monday announced a set of new security features in Chrome, following the company's addition of agentic artificial intelligence (AI) capabilities to the web browser.

To that end, the tech giant said it has implemented layered defenses to make it harder for bad actors to exploit indirect prompt injections that arise as a result of exposure to untrusted web content and inflict harm.

Chief among the features is a User Alignment Critic, which uses a second model to independently evaluate the agent's actions in a manner that's isolated from malicious prompts. This approach complements Google's existing techniques, like
[spotlighting](https://arxiv.org/abs/2403.14720)
, which instruct the model to stick to user and system instructions rather than abiding by what's embedded in a web page.

"The User Alignment Critic runs after the planning is complete to double-check each proposed action," Google
[said](https://security.googleblog.com/2025/12/architecting-security-for-agentic.html)
. "Its primary focus is task alignment: determining whether the proposed action serves the user's stated goal. If the action is misaligned, the Alignment Critic will veto it."

The component is designed to view only metadata about the proposed action and is prevented from accessing any untrustworthy web content, thereby ensuring that it is not poisoned through malicious prompts that may be included in a website. With the User Alignment Critic, the idea is to provide safeguards against any malicious attempts to exfiltrate data or hijack the intended goals to carry out the attacker's bidding.

"When an action is rejected, the Critic provides feedback to the planning model to re-formulate its plan, and the planner can return control to the user if there are repeated failures," Nathan Parker from the Chrome security team said.

Google is also enforcing what's called Agent Origin Sets to ensure that the agent only has access to data from origins that are relevant to the task at hand or data sources the user has opted to share with the agent. This aims to address site isolation bypasses where a compromised agent can interact with arbitrary sites and enable it to exfiltrate data from logged-in sites.

This is implemented by means of a gating function that determines which origins are related to the task and categorizes them into two sets -

* Read-only origins, from which Google's Gemini AI model is permitted to consume content
* Read-writable origins, to which the agent can type or click on in addition to reading from

"This delineation enforces that only data from a limited set of origins is available to the agent, and this data can only be passed on to the writable origins," Google explained. "This bounds the threat vector of cross-origin data leaks."

Similar to the User Alignment Critic, the gating function is not exposed to untrusted web content. The planner is also required to obtain the gating function's approval before adding new origins, although it can use context from the web pages a user has explicitly shared in a session.

Another key pillar underpinning the new security architecture relates to transparency and user control, allowing the agent to create a work log for user observability and request their explicit approval before navigating to sensitive sites, such as banking and healthcare portals, permitting sign-ins via Google Password Manager, or completing web actions like purchases, payments, or sending messages.

Lastly, the agent also checks each page for indirect prompt injections and operates alongside Safe Browsing and on-device scam detection to block potentially suspicious content.

"This prompt-injection classifier runs in parallel to the planning model's inference, and will prevent actions from being taken based on content that the classifier determined has intentionally targeted the model to do something unaligned with the user's goal," Google said.

To further incentivize research and poke holes in the system, the company said it will pay up to $20,000 for demonstrations that result in a breach of the security boundaries. These
[include](https://bughunters.google.com/about/rules/chrome-friends/5745167867576320/chrome-vulnerability-reward-program-rules#qualifying-ai-report-categories)
indirect prompt injections that allow an attacker to -

* Carry out rogue actions without confirmation
* Exfiltrate sensitive data without an effective opportunity for user approval
* Bypass a mitigation that should have ideally prevented the attack from succeeding in the first place

"By extending some core principles like origin-isolation and layered defenses, and introducing a trusted-model architecture, we're building a secure foundation for Gemini's agentic experiences in Chrome," Google said. "We remain committed to continuous innovation and collaboration with the security community to ensure Chrome users can explore this new era of the web safely."

The announcement
[follows research](https://www.gartner.com/en/documents/7211030)
from Gartner that called on enterprises to block the use of agentic AI browsers until the associated risks, such as indirect prompt injections, erroneous agent actions, and data loss, can be appropriately managed.

The research also warns of a possible scenario where employees "might be tempted to use AI browsers and automate certain tasks that are mandatory, repetitive, and less interesting." This could cover cases where an individual dodges mandatory cybersecurity training by instructing the AI browser to complete it on their behalf.

"Agentic browsers, or what many call AI browsers, have the potential to transform how users interact with websites and automate transactions while introducing critical cybersecurity risks," the advisory firm said. "CISOs must block all AI browsers in the foreseeable future to minimize risk exposure."

The development comes as the U.S. National Cyber Security Centre (NCSC) said that large language models (LLMs) may suffer from a persistent class of vulnerability known as prompt injection and that the problem can never be resolved in its entirety.

"Current large language models (LLMs) simply do not enforce a security boundary between instructions and data inside a prompt,"
[said](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)
David C, NCSC technical director for Platforms Research. "Design protections need to therefore focus more on deterministic (non-LLM) safeguards that constrain the actions of the system, rather than just attempting to prevent malicious content reaching the LLM."