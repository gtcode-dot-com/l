---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:29:52.087644+00:00'
exported_at: '2026-10-07T04:29:54.561469+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/china-aligned-ta419-targets-us-ai.html
structured_data:
  about: []
  author: ''
  description: TA419 targets U.S. AI policy experts with reply-triggered AitM phishing
    that captures Microsoft credentials and session cookies.
  headline: China-Aligned TA419 Targets U.S. AI Policy Experts With Microsoft AitM
    Phishing
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/china-aligned-ta419-targets-us-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Aligned TA419 Targets U.S. AI Policy Experts With Microsoft AitM Phishing
updated_at: '2026-10-07T04:29:52.087644+00:00'
url_hash: 453d2c5398a1fe249f3b30bfc35a52de4769dd60
---

**

Ravie Lakshmanan
**

Oct 04, 2026

Cyber Espionage / Phishing

A new China-nexus cyber espionage group known as
**TA419**
has been attributed to multiple credential phishing campaigns targeting artificial intelligence (AI) experts working for U.S. think tanks, universities, and legal sector organizations.

The campaigns have impersonated prominent economists and AI policymakers, as well as a prominent Anthropic employee, to single out an AI policy expert at a U.S. think tank in February 2026. The phishing email carried the subject line "Request for Feedback on Military Integration of Claude."

"This activity likely supports wider Chinese intelligence objectives to better understand ongoing developments within the U.S. AI policy and regulatory landscape and occurs amid intense strategic competition, accusations of model distillation, and export controls involving the U.S. and China," Proofpoint
[said](https://www.proofpoint.com/us/blog/threat-insight/hallucinating-credibility-china-aligned-ta419-impersonates-its-way-us-ai-policy)
in an analysis published this week.

The enterprise security company has described TA419 as a China-aligned and espionage-motivated threat actor that has a track record of orchestrating credential phishing campaigns against individuals working for U.S.- and Japan-based think tanks, defense contractors, universities, and law firms since at least April 2025.

Around July 2026, the threat actor is said to have impersonated several individuals, including a former member of the White House Office of Science and Technology Policy leadership team, as part of credential phishing campaigns targeting AI policy experts in the U.S.

The attack begins with harmless invitations that aim to establish trust with the target. It's only when the recipient responds to the outreach that the next stage kicks in, with the adversary following it up with a shortened URL that triggers a multi-stage redirection chain, which leads to an OneDrive adversary-in-the-middle (AitM) credential phishing page after completing a Cloudflare Turnstile check.

The page employs a technique called
[Frameless BitB](https://github.com/waelmas/frameless-bitb)
, a version of the browser-in-the-browser (
[BitB](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html)
) attack that
[spoofs](https://www.kaspersky.com/blog/browser-in-the-browser-phishing-facebook/55374/)
a trusted website or login page by crafting a fake browser window within a legitimate browser session using HTML, CSS, and JavaScript.

While BitB works by serving the sign-in page inside an
[iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
,
[Frameless BitB](https://www.youtube.com/watch?v=luJjxpEwVHI)
, as the name implies, achieves the same goal without using the HTML element. "This can be achieved by injecting scripts and HTML besides the original content using search and replace (aka substitutions), then relying completely on HTML/CSS/JS tricks to make the visual effect," security researcher Wael Masri noted back in January 2024.

According to Proofpoint, TA419 has extended the open-source tool with a bespoke telemetry and automation module that tracks the target's Microsoft sign-in flow and captures the credential information using the AitM proxy, while relaying the details to the real Microsoft infrastructure in the background.

The main advantage this method offers is that the victim doesn't notice anything is amiss, as the sign-in event is successful and there are no indications that the resulting session cookies have been stealthily captured by the attacker.

To safeguard against this threat, organizations are recommended to enable phishing-resistant authentication methods like passkeys, and individual targets who are the focus of TA419 activity should treat unsolicited subject-matter outreach with caution, and verify their authenticity before proceeding further.

"TA419 has consistently shown an interest in defense, national security, energy, international relations, and foreign policy targets, predominantly with a nexus to the U.S. and Japan," Proofpoint said. "The targeting of AI policy experts represents an extension of that remit rather than a departure from it."