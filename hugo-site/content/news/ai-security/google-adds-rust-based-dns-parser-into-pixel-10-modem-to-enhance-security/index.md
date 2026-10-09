---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-14T14:15:19.315391+00:00'
exported_at: '2026-04-14T14:15:21.592863+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/google-adds-rust-based-dns-parser-into.html
structured_data:
  about: []
  author: ''
  description: Google adds a Rust-based DNS parser to Pixel 10 modem firmware, reducing
    memory vulnerabilities and strengthening defenses against baseband exploits.
  headline: Google Adds Rust-Based DNS Parser into Pixel 10 Modem to Enhance Security
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/google-adds-rust-based-dns-parser-into.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Adds Rust-Based DNS Parser into Pixel 10 Modem to Enhance Security
updated_at: '2026-04-14T14:15:19.315391+00:00'
url_hash: c28421179d0bafcc7290b22143fdde42635534a6
---

**

Ravie Lakshmanan
**

Apr 14, 2026

Mobile Security / Network Security

Google has announced the integration of a Rust-based Domain Name System (DNS) parser into the modem firmware as part of its ongoing efforts to beef up the security of Pixel devices and push memory-safe code at a more foundational level.

"The new Rust-based DNS parser significantly reduces our security risk by mitigating an entire class of vulnerabilities in a risky area, while also laying the foundation for broader adoption of memory-safe code in other areas," Jiacheng Lu, a software engineer part of the Google Pixel Team,
[said](https://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html)
.

The security boost via Rust integration is available for Pixel 10 devices, making it the first Pixel device to integrate a memory-safe language into its modem.

The move builds upon a series of initiatives the tech giant has taken to harden the cellular baseband modem against exploitation. In late 2023, it
[highlighted](https://thehackernews.com/2023/12/google-using-clang-sanitizers-to.html)
the role played by Clang sanitizers like Overflow Sanitizer (IntSan) and BoundsSanitizer (BoundSan) to catch undefined behavior during program execution.

A year later, it also
[detailed](https://thehackernews.com/2024/10/android-14-adds-new-security-features.html)
the various security measures built into the modem firmware to combat 2G exploits and baseband attacks that exploit memory-safety vulnerabilities like buffer overflows to achieve remote code execution.

These security advances have been complemented by Google's steady adoption of Rust into
[Android](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html)
and
[low-level firmware](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html)
. In November 2025, the company
[revealed](https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html)
that the number of memory safety vulnerabilities fell below 20% of total vulnerabilities discovered in the mobile operating system last year.

Google said it opted for the DNS protocol for its Rust implementation owing to the fact that it underpins modern cellular communications and that vulnerabilities in the system can expose users to malicious attacks when designed in a memory-unsafe language, resulting in out-of-bound memory accesses, as in the case of
[CVE-2024-27227](https://nvd.nist.gov/vuln/detail/cve-2024-27227)
.

"With the evolution of cellular technology, modern cellular communications have migrated to digital data networks; consequently, even basic operations such as call forwarding rely on DNS services," it added. "Implementing the DNS parser in Rust offers value by decreasing the attack surfaces associated with memory unsafety."

To that end, Google has chosen the "
[hickory-proto](https://crates.io/crates/hickory-proto)
" crate, a
[Rust-based DNS client, server, and resolver](https://github.com/hickory-dns/hickory-dns)
, to implement the protocol, while modifying it to support bare metal and embedded environments. Another important component of this change is the use of a custom tool called "
[cargo-gnaw](https://fuchsia.googlesource.com/fuchsia/+/master/tools/cargo-gnaw/)
" to easily resolve and maintain more than 30 dependencies introduced by the crate.

The internet company also noted that the DNS Rust crate is not optimized for use in memory-constrained systems, and that one possible code size optimization could be achieved by adding extra feature flags to ensure modularity and selectively compile only required functionality.

"For the DNS parser, we declared the DNS response parsing API in C and then implemented the same API in Rust," Google said. "The Rust function returns an integer standing for the error code. The received DNS answers in the DNS response are required tobe updated to in-memory data structures that are coupled with the original C implementation;therefore, we use existing C functions to do it. The existing C functions are dispatched from the Rust implementation."