---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-17T16:57:42.232594+00:00'
exported_at: '2025-11-17T16:57:44.845803+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html
structured_data:
  about: []
  author: ''
  description: Google reports Rust cut Android memory bugs below 20% while improving
    speed, safety, and development reliability.
  headline: Rust Adoption Drives Android Memory Safety Bugs Below 20% for First Time
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Rust Adoption Drives Android Memory Safety Bugs Below 20% for First Time
updated_at: '2025-11-17T16:57:42.232594+00:00'
url_hash: c8af924c17ec7c5208ae15b8d2121e9d46b6e49b
---

**

Nov 17, 2025
**

Ravie Lakshmanan

Vulnerability / Mobile Security

Google has disclosed that the company's continued adoption of the Rust programming language in Android has resulted in the number of memory safety vulnerabilities falling below 20% of total vulnerabilities for the first time.

"We adopted Rust for its security and are seeing a 1000x reduction in memory safety vulnerability density compared to Android's C and C++ code. But the biggest surprise was Rust's impact on software delivery," Google's Jeff Vander Stoep
[said](https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html)
. "With Rust changes having a 4x lower rollback rate and spending 25% less time in code review, the safer path is now also the faster one."

The development comes a little over a year after the tech giant
[disclosed](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html)
that its transition to Rust led to a decline in memory safety vulnerabilities from 223 in 2019 to less than 50 in 2024.

The company pointed out that Rust code requires fewer revisions, necessitating about 20% fewer revisions than their C++ counterparts, and has contributed to a decreased rollback rate, thereby improving overall development throughput.

Google also said it's planning to expand Rust's "security and productivity advantages" to other parts of the Android ecosystem, including
[kernel](https://source.android.com/docs/core/architecture/kernel/release-notes)
, firmware, and critical first-party apps like
[Nearby Presence](https://developers.google.com/nearby)
, Message Layer Security (
[MLS](https://thehackernews.com/2023/07/google-messages-getting-cross-platform.html)
), and Chromium, which has had its parsers for PNG, JSON, and web fonts replaced with memory-safe implementations in Rust.

Furthermore, it has emphasized the need for a defense-in-depth approach, stating that the programming language's built-in memory safety features are just one part of a comprehensive memory safety strategy.

As an example, Google highlighted its discovery of a memory safety vulnerability (
[CVE-2025-48530](https://www.cve.org/CVERecord?id=CVE-2025-48530)
, CVSS score: 8.1) in CrabbyAVIF, an AVIF (AV1 Image File) parser/decoder implementation in
[unsafe Rust](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html)
, that could have resulted in remote code execution. While the linear buffer overflow flaw never made it into a public release, it was
[patched](https://thehackernews.com/2025/08/google-fixes-3-android-vulnerabilities.html)
by Google as part of its Android security update for August 2025.

Further analysis of the "near-miss" vulnerability found that it was rendered non-exploitable by
[Scudo](https://source.android.com/docs/security/test/scudo)
, a dynamic user-mode memory allocator in Android that's designed to combat heap-related vulnerabilities, such as buffer overflow, use after free, and double free, without sacrificing performance.

Emphasizing that unsafe Rust is "already really quite safe," Google said the vulnerability density is significantly lower as opposed to C and C++, adding that the incorporation of an
["unsafe" code block in Rust](https://rustfoundation.org/media/unsafe-rust-in-the-wild-notes-on-the-current-state-of-unsafe-rust/)
doesn't automatically disable the programming language's safety checks.

"While C and C++ will persist, and both software and hardware safety mechanisms remain critical for layered defense, the transition to Rust is a different approach where the more secure path is also demonstrably more efficient," it said.