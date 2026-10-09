---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T02:33:27.044891+00:00'
exported_at: '2026-10-07T02:33:32.169644+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
structured_data:
  about: []
  author: ''
  description: Public PoC for CVE-2026-86950 triggers a controlled out-of-bounds write
    in CoreGraphics; code execution is not demonstrated.
  headline: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible
    Delivery Path
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery
  Path
updated_at: '2026-10-07T02:33:27.044891+00:00'
url_hash: a4068745cb2ed655f5a4b759be93834a1251d6f0
---

Security researchers have published the first public proof-of-concept for
**CVE-2026-86950**
, an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals.

The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working exploit is separate work the analysis does not demonstrate.

Apple patched the flaw on
[September 28](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html)
, crediting Meta Product Security with the discovery and noting it may have been used in an "extremely sophisticated attack against specific targeted individuals on versions of iOS before iOS 27."

The U.S. Cybersecurity and Infrastructure Security Agency
[added the flaw](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950)
to its Known Exploited Vulnerabilities catalog the following day, requiring federal agencies to apply the fix by October 2.

Apple has not listed iOS 27 or macOS Golden Gate 27 as affected in the September 28 advisories. No workaround has been described for systems that cannot update immediately.

### What the Researchers Found

The analysis was published September 30 by Dion Blazakis, Josh Maine, and Anna Groza of
[Calif](https://calif.io/research/the-great-glyph-grift)
, a firm known for research into
[zero-click attack surfaces](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)
in messaging apps. They started from a publicly available binary comparison of iOS 26.7 and 26.7.1.

CoreGraphics is the Apple framework for 2D drawing, image rendering, and PDF processing. It was the only library changed in 26.7.1, with the same fix applied more than 20 times across eight rasterizer functions.

The patched code converts a glyph coordinate from floating-point to a 32-bit fixed-point value. Before the patch, two of the eight functions handled out-of-range values differently: one saturated the result, the other truncated it.

That difference caused the calculated bounding box for a glyph to be too narrow. CoreGraphics then allocated a working buffer smaller than the edges it needed to draw, and wrote outside it.

To trigger the bug, the researchers built a TrueType font with coordinates large enough to force the overflow. Embedding it in a PDF with a text matrix and nested composite-glyph scaling pushes those coordinates past the limit. They published the generation scripts and a sample PDF in a
[public GitHub repository](https://github.com/califio/publications/tree/main/MADBugs/CVE-2026-86950)
.

The harness calls the same ImageIO thumbnail path an app uses when previewing a received attachment. The researchers say the crash occurs on both macOS and iOS.

The macOS result includes a full debugger call stack. The iOS claim is Calif's, with no separate trace published.

The crash exposes a controlled out-of-bounds write that affects two adjacent 16-bit values in a buffer that the attacker can control, allowing writes to the stack or heap. Calif says converting that primitive into working code execution is separate work. Calif did not obtain the in-the-wild sample and cannot say how the attacker completed the chain.

### The WhatsApp Question

Calif examined WhatsApp because Meta Product Security was credited with finding the flaw. The firm compared two recent WhatsApp versions, 26.37.73 and 26.38.74, and found new code in WhatsApp's
[Kaleidoscope](https://engineering.fb.com/2026/01/27/security/rust-at-scale-security-whatsapp/)
attachment scanner.

The newer version reads PDF files for embedded font streams and flags suspicious ones with three defect tags: MalformedFontProgram, UndecodableFontProgram, and UnverifiedFontProgram. Any such tag returns a high-risk score to WhatsApp's attachment checker, which then stops automatic parsing of the flagged file.

Calif described those changes as circumstantial evidence pointing toward WhatsApp as a possible delivery vector. The firm's post describes its research as covering a possible WhatsApp zero-click path.

The published analysis does not describe or test a WhatsApp delivery path. The initial version did: it said the researchers' analysis suggested WhatsApp could deliver a PDF that triggers the flaw when a victim opens a chat from a trusted contact with automatic media downloads on.

That sentence was removed 85 minutes after publication in a commit by Calif CEO Thai Duong, who described the change as removing the WhatsApp speculation.

The analysis closes with a question: whether the flaw "was combined with additional vulnerabilities in WhatsApp to reach parsing with less user interaction." That phrasing suggests the path Calif studied would require user action or further WhatsApp vulnerabilities in the chain.

WhatsApp has published no advisory linking this flaw to its products. Its 2026 advisory page lists two unrelated vulnerabilities.

The Hacker News asked Meta whether WhatsApp was involved in the reported attacks. Meta did not respond before publication.

An earlier case makes the hypothesis plausible. In August 2025, WhatsApp assessed that a flaw in its linked-device synchronization messages may have been combined with a separate Apple out-of-bounds write and used against fewer than 200 targeted users, a pair of vulnerabilities
[THN covered at the time](https://thehackernews.com/2025/08/whatsapp-issues-emergency-update-for.html)
.

The Hacker News asked Calif about the removed delivery claim and whether the researchers had obtained the in-the-wild sample since publication. Calif did not respond before publication.

No network indicators, attacker identifiers, or exploit payload names have been made public. Apple has not said whether Lockdown Mode would have blocked the delivery path used in the reported attacks.