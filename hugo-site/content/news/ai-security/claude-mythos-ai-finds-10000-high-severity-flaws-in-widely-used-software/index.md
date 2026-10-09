---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-24T00:20:02.605809+00:00'
exported_at: '2026-05-24T00:20:05.134335+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html
structured_data:
  about: []
  author: ''
  description: Anthropic uncovered 10,000 vulnerabilities through Project Glasswing,
    driving urgent patching efforts and stronger cyber defenses.
  headline: Claude Mythos AI Finds 10,000 High-Severity Flaws in Widely Used Software
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Claude Mythos AI Finds 10,000 High-Severity Flaws in Widely Used Software
updated_at: '2026-05-24T00:20:02.605809+00:00'
url_hash: 72d496497a9b3978d510a42859bf49d2ddf85da4
---

**

Ravie Lakshmanan
**

May 23, 2026

Artificial Intelligence / Vulnerability

Anthropic on Friday
[disclosed](https://www.anthropic.com/research/glasswing-initial-update)
that Project Glasswing has helped uncover more than 10,000 high- or critical-severity vulnerabilities across some of the most "systemically" important software across the world since the cybersecurity initiative went live last month.

[Project Glasswing](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
is a defensive effort launched by the artificial intelligence (AI) company to secure critical global software infrastructure. It grants a small set of about 50 partners exclusive, early access to Claude Mythos Preview, a frontier model with capabilities to autonomously identify vulnerabilities in widely-used software before bad actors can exploit them.

Of these vulnerabilities, 6,202 have been classified as high- or critical-severity flaws impacting more than 1,000 open-source projects. Subsequent analysis of these vulnerability candidates has identified that 1,726 are valid true positives. As many as 1,094 flaws are assessed to be either high- or critical-severity.

One of the identified weaknesses is a critical flaw in WolfSSL (
[CVE-2026-5194](https://nvd.nist.gov/vuln/detail/CVE-2026-5194)
, CVSS score: 9.1) that could allow an attacker to forge certificates and masquerade as a legitimate service. In all, these efforts have led to 97 findings being patched upstream and 88 advisories being issued.

"The relative ease of finding vulnerabilities compared with the difficulty of fixing them amounts to a major challenge for cybersecurity," Anthropic acknowledged. "Confronting this challenge successfully will make our software far safer than before."

The development comes as software vendors are
[shipping more fixes](https://www.paloaltonetworks.com/blog/2026/05/defenders-guide-frontier-ai-impact-cybersecurity-may-2026-update/)
than
[ever before](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)
, driven by a surge in AI-assisted vulnerability discovery, with Microsoft
[noting](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html)
that the number of new patches it expects to release on a monthly basis to "continue trending larger for some time."

Autonomous offensive security platform XBOW has
[described](https://xbow.com/blog/mythos-offensive-security-xbow-evaluation)
Mythos Preview as "a major advance" that's "substantially better than prior models at finding vulnerability candidates" and "adept at analyzing source code with a security mindset." Recent analyses have also found the model to excel at
[turning vulnerabilities](https://blog.cloudflare.com/cyber-frontier-models/)
into
[end-to-end attack chains](https://red.anthropic.com/2026/exploit-evals/)
.

Mythos Preview's utility, Anthropic added, goes beyond finding security flaws. In one case, a Glasswing partner bank is said to have leveraged the AI model to detect and prevent a fraudulent $1.5 million wire transfer after an unknown threat actor breached a customer's email account and made spoof phone calls.

Given that models with similar capabilities to Mythos could become broadly available in the near future, Anthropic is urging software developers to shorten their patch cycles and make security fixes available as quickly as possible. It's worth mentioning here that Oracle has recently shifted to a
[monthly patch cycle](https://blogs.oracle.com/security/accelerating-vulnerability-detection-and-response-at-oracle)
to address critical security issues.

"Network defenders should shorten their patch testing and deployment timelines," Anthropic said. "These include steps like hardening networks' default configurations, enforcing multi-factor authentication, and keeping comprehensive logs for detection and response."

The AI company also said it has launched a
[Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)
that allows security professionals to use its models without guardrails for legitimate purposes such as vulnerability research, penetration testing, and red teaming. This is similar to
[OpenAI's Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html)
, which also allows defenders to leverage
[GPT-5.5-Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)
for specialized workflows.

Models like Mythos Preview and GPT-5.5-Cyber have yet to be released to the public owing to concerns that there currently exist no adequate safeguards to
[prevent their misuse](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)
at a large scale.

"Glasswing helps the most systemically important cyber defenders gain an asymmetric advantage," it pointed out. "However, there is an urgent need for as many organizations as possible to shore up their cyber defenses. We hope that our generally available models, and the new tools, resources, and research we're providing to accompany them, will support those organizations to improve their cybersecurity posture."