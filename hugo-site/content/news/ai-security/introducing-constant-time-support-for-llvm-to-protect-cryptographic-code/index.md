---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-13T12:03:14.951521+00:00'
exported_at: '2025-12-13T12:03:17.612835+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2025/12/02/introducing-constant-time-support-for-llvm-to-protect-cryptographic-code
structured_data:
  about: []
  author: ''
  description: "\n                Trail of Bits developed constant-time coding support
    for LLVM that prevents compilers from breaking cryptographic implementations vulnerable
    to timing attacks, introducing the __builtin_ct_select family of intrinsics that
    preserve constant-time properties throughout compilation.\n            "
  headline: Introducing constant-time support for LLVM to protect cryptographic code
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2025/12/02/introducing-constant-time-support-for-llvm-to-protect-cryptographic-code
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Introducing constant-time support for LLVM to protect cryptographic code
updated_at: '2025-12-13T12:03:14.951521+00:00'
url_hash: 596ef669dea18078380dd1b06d19a5d3fb378356
---

Trail of Bits has developed
[constant-time coding support for LLVM](https://github.com/llvm/llvm-project/pull/166702)
, providing developers with compiler-level guarantees that their cryptographic implementations remain secure against branching-related timing attacks. These changes are being reviewed and will be added in an upcoming release, LLVM 22. This work introduces the
`__builtin_ct_select`
family of intrinsics and supporting infrastructure that prevents the Clang compiler, and potentially other compilers built with LLVM, from inadvertently breaking carefully crafted constant-time code. This post will walk you through what we built, how it works, and what it supports. We’ll also discuss some of our future plans for extending this work.

## The compiler optimization problem

Modern compilers excel at making code run faster. They eliminate redundant operations, vectorize loops, and cleverly restructure algorithms to squeeze out every bit of performance. But this optimization zeal becomes a liability when dealing with cryptographic code.

Consider this seemingly innocent constant-time lookup from
[Sprenkels (2019)](https://electricdusk.com/cmov-conversion.html)
:

```
uint64_t constant_time_lookup(const size_t secret_idx,
  const uint64_t table[16]) {
    uint64_t result = 0;
    for (size_t i = 0; i < 8; i++) {
        const bool cond = i == secret_idx;
        const uint64_t mask = (-(int64_t)cond);
        result |= table[i] & mask;
    }

    return result;}
```

This code carefully avoids branching on the secret index. Every iteration executes the same operations regardless of the secret value. However, as compilers are built to make your code go faster, they would see an opportunity to improve this carefully crafted code by optimizing it into a version that includes branching.

The problem is that any data-dependent behavior in the compiled code would create a timing side channel. If the compiler introduces a branch like
`if (i == secret_idx)`
, the CPU will take different amounts of time depending on whether the branch is taken. Modern CPUs have branch predictors that learn patterns, making correctly predicted branches faster than mispredicted ones. An attacker who can measure these timing differences across many executions can statistically determine which index is being accessed, effectively recovering the secret. Even small timing variations of a few CPU cycles can be exploited with sufficient measurements.

## What we built

Our solution provides cryptographic developers with explicit compiler intrinsics that preserve constant-time properties through the entire compilation pipeline. The core addition is the
`__builtin_ct_select`
family of intrinsics:

```
// Constant-time conditional selection
result = __builtin_ct_select(condition, value_if_true, value_if_false);
```

This intrinsic guarantees that the selection operation above will compile to constant-time machine code, regardless of optimization level. When you write this in your C/C++ code, the compiler translates it into a special LLVM intermediate representation intrinsic (llvm.ct.select.\*) that carries semantic meaning: “this operation must remain constant-time.”

Unlike regular code that the optimizer freely rearranges and transforms, this intrinsic acts as a barrier. The optimizer recognizes it as a security-critical operation and preserves its constant-time properties through every compilation stage, from source code to assembly.

## Real-world impact

In their recent study “
[Breaking Bad: How Compilers Break Constant-Time Implementations](https://arxiv.org/pdf/2410.13489.pdf)
,” Srdjan Čapkun and his graduate students Moritz Schneider and Nicolas Dutly found that compilers break constant-time guarantees in numerous production cryptographic libraries. Their analysis of 19 libraries across five compilers revealed systematic vulnerabilities introduced during compilation.

With our intrinsics, the problematic lookup function becomes this constant-time version:

```
uint64_t
constant_time_lookup(const size_t secret_idx,
                     const uint64_t table[16]) {
  uint64_t result = 0;

  for (size_t i = 0; i < 8; i++) {
    const bool cond = i == secret_idx;
    result |= __builtin_ct_select(cond, table[i], 0u);
  }
  return result;
}
```

The use of an intrinsic function prevents the compiler from making any modifications to it, which ensures the selection remains constant time. No optimization pass will transform it into a vulnerable memory access pattern.

## Community engagement and adoption

Getting these changes upstream required extensive community engagement. We published our
[RFC on the LLVM Discourse](https://discourse.llvm.org/t/rfc-constant-time-coding-support/87781)
forum in August 2025.

The RFC received significant feedback from both the compiler and cryptography communities. Open-source maintainers from Rust Crypto, BearSSL, and PuTTY expressed strong interest in adopting these intrinsics to replace their current inline assembly workarounds, while providing valuable feedback on implementation approaches and future primitives. LLVM developers helped ensure the intrinsics work correctly with auto-vectorization and other optimization passes, along with architecture-specific implementation guidance.

### Building on existing work

Our approach synthesizes lessons from multiple previous efforts:

* [**Simon and Chisnall
  `__builtin_ct_choose`**
  (2018)](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8406587)
  : This work provided the conceptual foundation for compiler intrinsics that preserve constant-time properties, but was never upstreamed.
* [**Jasmin**
  (2017)](https://acmccs.github.io/papers/p1807-almeidaA.pdf)
  : This work showed the value of compiler-aware constant-time primitives but would have required a new language.
* **Rust’s
  `#[optimize(never)]`**
  experiments: These experiments highlighted the need for fine-grained optimization control.

## How it works across architectures

Our implementation ensures
`__builtin_ct_select`
compiles to constant-time code on every platform:

**x86-64:**
The intrinsic compiles directly to the
**`cmov`**
(conditional move) instruction, which always executes in constant time regardless of the condition value.

**i386:**
Since i386 lacks
`cmov`
, we use a masked arithmetic pattern with bitwise operations to achieve constant-time selection.

**ARM and AArch64:**
For AArch64, the intrinsic is lowered to the CSEL instruction, which provides constant-time execution. For ARM, since ARMv7 doesn’t have a constant-time instruction like AAarch64, the implementation generates a masked arithmetic pattern using bitwise operations instead.

**Other architectures:**
A generic fallback implementation uses bitwise arithmetic to ensure constant-time execution, even on platforms we haven’t natively added support for.

Each architecture needs different instructions to achieve constant-time behavior. Our implementation handles these differences transparently, so developers can write portable constant-time code without worrying about platform-specific details.

## Benchmarking results

Our partners at ETH Zürich are conducting comprehensive benchmarking using their test suite from the “Breaking Bad” study. Initial results show the following:

* **Minimal performance overhead**
  for most cryptographic operations
* **100% preservation**
  of constant-time properties across all tested optimization levels
* **Successful integration**
  with major cryptographic libraries including HACL\*, Fiat-Crypto, and BoringSSL

## What’s next

While
`__builtin_ct_select`
addresses the most critical need, our RFC outlines a roadmap for additional intrinsics:

### Constant-time operations

We have future plans for extending the constant-time implementation, specifically for targeting arithmetic or string operations and evaluating expressions to be constant time.

```
_builtin_ct<op> // for constant-time arithmetic or string operation
__builtin_ct_expr(expression)  // Force entire expression to evaluate without branches
```

### Adoption path for other languages

The modular nature of our LLVM implementation means any language targeting LLVM can leverage this work:

**Rust:**
The Rust compiler team is exploring how to expose these intrinsics through its
`core::intrinsics`
module, potentially providing safe wrappers in the standard library.

**Swift:**
Apple’s security team has expressed interest in adopting these primitives for its cryptographic frameworks.

**WebAssembly:**
These intrinsics would be particularly useful for browser-based cryptography, where timing attacks remain a concern despite sandboxing.

## Acknowledgments

This work was done in collaboration with the
[System Security Group](https://syssec.ethz.ch/)
at ETH Zürich. Special thanks to Laurent Simon and David Chisnall for their pioneering work on constant-time compiler support, and to the LLVM community for their constructive feedback during the RFC process.

We’re particularly grateful to our Trail of Bits cryptography team for its technical review.

## Resources

---

The work to which this blog post refers was conducted by Trail of Bits based upon work supported by DARPA under Contract No. N66001-21-C-4027 (Distribution Statement A, Approved for Public Release: Distribution Unlimited). Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the United States Government or DARPA.