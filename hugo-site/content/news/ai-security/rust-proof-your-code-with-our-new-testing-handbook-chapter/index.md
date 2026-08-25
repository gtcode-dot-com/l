---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-25T18:45:01.109230+00:00'
exported_at: '2026-08-25T18:45:03.101681+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/07/13/rust-proof-your-code-with-our-new-testing-handbook-chapter
structured_data:
  about: []
  author: ''
  description: 'We’ve added a new chapter to our Testing Handbook: a comprehensive
    guide to security testing Rust programs.'
  headline: Rust-proof your code with our new Testing Handbook chapter
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/07/13/rust-proof-your-code-with-our-new-testing-handbook-chapter
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Rust-proof your code with our new Testing Handbook chapter
updated_at: '2026-08-25T18:45:01.109230+00:00'
url_hash: 7aa666921907d62ebf6486e123351a8b77e07508
---

We’ve added
[a new chapter to our Testing Handbook](https://appsec.guide/docs/languages/rust/)
: a comprehensive guide to security testing Rust programs. This chapter covers the tools and techniques we use at Trail of Bits to validate the security of Rust programs and systems.

```
fn
main()
{(|f:&amp;dyn
Fn(u128)-&gt;Box&lt;
dyn Iterator&lt;Item=
char&gt;+'static&gt;|f(*[&amp;(
0x7B736D70683F73u128&lt;&lt;64|
0x7A6A6D7C3F7A667D),&amp;(0x7B736Du128
&lt;&lt;64|0x70683F7073737A77)][((std::hint::
black_box(0.0f64)/0.0).to_bits()&gt;&gt;63)as usize])
.for_each(|c|print!("{c}")))(Box::leak(Box::new(|n:
u128|Box::new(std::iter::successors(Some(n),|&amp;n|Some(n&gt;&gt;8)
).take_while(|&amp;n|n&gt;0).map(|n|((n as u8)^0x1F)as char))as _)))}
```

## What’s in the chapter

The chapter starts with a security overview of what Rust’s guarantees do and don’t cover, including underappreciated issues like unwind safety, nondeterminism, and arithmetic errors. This leads into an overview of dynamic analysis, which covers a range of boosters for unit tests, how to use Miri to detect undefined behavior, property testing with
`proptest`
, coverage measurement, and mutation testing. The static analysis section then covers Clippy in depth, including a list of our favorite lints.

Beyond tooling, the chapter also covers what we’ve learned from auditing Rust codebases directly. Our gotchas and footguns checklist is a great reference for manual code reviews, and will help you find subtle issues like
`a &amp; b == c`
having different operator precedence than in C. The memory zeroization section offers three solutions to the tricky problem of guaranteeing that secrets are erased from memory.

Finally, the specialized testing sections cover tools like Kani (a model checker), and the supply chain section covers the full toolchain for vetting dependencies.

## Still oxidizing

We’ve also
[released rust-review](https://github.com/trailofbits/skills/tree/main/plugins/rust-review)
, a Claude Code plugin for automated Rust security reviews. Co-built with Aptos Labs, it targets over a dozen bug classes, from memory safety and concurrency hazards to FFI pitfalls and async cancellation issues. It’s a fast way to catch security issues in a Rust codebase before they make it to audit.

Our goal is to keep the handbook current as the Rust ecosystem evolves. If your favorite tool or gotcha isn’t covered,
[submit a PR](https://github.com/trailofbits/testing-handbook)
. And if you need help securing your Rust systems,
[contact us](https://www.trailofbits.com/contact/)
.