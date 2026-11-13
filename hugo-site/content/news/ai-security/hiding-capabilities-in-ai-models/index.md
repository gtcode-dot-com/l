---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-13T19:23:34.640391+00:00'
exported_at: '2026-11-13T19:23:35.789032+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html
structured_data:
  about: []
  author: ''
  description: 'Interesting research: “AI Models Can Provably Hide Arbitrary Capabilities”
    Abstract: Capability evaluations aim to surface dangerous model behaviors before
    deployment, but their reliability depends on the assumption that hidden capabilities
    can be elicited. We show this assumption does not hold under adversarial con...'
  headline: Hiding Capabilities in AI Models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hiding Capabilities in AI Models
updated_at: '2026-11-13T19:23:34.640391+00:00'
url_hash: 6c05e107bb76f251f525616cba1b6c327f800cce
---

## Hiding Capabilities in AI Models

Interesting research: “
[AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928)
”

&gt; **Abstract:**
&gt; Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training, using a small chemical reaction prediction task as a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[AI](https://www.schneier.com/tag/ai/)
,
[encryption](https://www.schneier.com/tag/encryption/)

[Posted on October 27, 2026 at 7:01 AM](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html)
•
[11 Comments](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.