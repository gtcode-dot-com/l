---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-27T03:43:12.422182+00:00'
exported_at: '2026-06-27T03:43:14.424498+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html
structured_data:
  about: []
  author: ''
  description: 'This is a fascinating explotation of how LLMs fall for prompt injection
    attacks. It turns out that they learn to recognize the style of text in different
    role/instruction blocks, and not just the tags. Their conclusion: Role tags were
    a formatting trick that became the security architecture and the cognitive scaffol...'
  headline: Interesting Paper Exploring Prompt Injection
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Interesting Paper Exploring Prompt Injection
updated_at: '2026-06-27T03:43:12.422182+00:00'
url_hash: 9a25c67747344fc8ea9c924bd694682201716bfa
---

## Interesting Paper Exploring Prompt Injection

[This](https://role-confusion.github.io/)
is a fascinating explotation of how LLMs fall for prompt injection attacks. It turns out that they learn to recognize the style of text in different role/instruction blocks, and not just the tags.

Their conclusion:

&gt; Role tags were a formatting trick that became the security architecture and the cognitive scaffolding of modern LLMs. We’ve shown that this architecture doesn’t survive into the model’s actual representations, and that such role confusion is linked to prompt injection.
&gt;
&gt; Unless LLMs achieve genuine role perception, we think injection defense will remain a perpetual whack-a-mole game. And the continuous nature of role boundaries opens the threat of injections designed to subtly shift LLM states through seemingly innocuous text, legally and at scale.
&gt;
&gt; More generally, roles are quietly one of the most important abstractions in the LLM stack, providing the boundaries meant to separate self from other, thought from communication, instruction from data. They’re human-controlled switches in an otherwise continuous system. We think they deserve a lot more study than they’ve gotten.

Full paper: “
[Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277)
.” Simon Willison
[comments](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/)
.

[Posted on June 25, 2026 at 7:23 AM](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html)
•
[8 Comments](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.