---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-30T02:37:52.341599+00:00'
exported_at: '2026-09-30T02:37:55.477390+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin
structured_data:
  about: []
  author: ''
  description: Fermat's margin was too narrow for his proof. Ours would have fit just
    fine, thanks to a wonderfully cursed Lean bug.
  headline: A “proof” of Fermat’s Last Theorem that fits the margin
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A “proof” of Fermat’s Last Theorem that fits the margin
updated_at: '2026-09-30T02:37:52.341599+00:00'
url_hash: b98b8f24a190351786c9d475526545de25044341
---

Fermat famously claimed to have a “truly marvelous proof” of his
[Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem)
, but he never wrote it down, insisting the margin of his page was too narrow to contain it. A few centuries later, Anthropic announced a complete
[formalization of Fermat’s Last Theorem using 13 million lines](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
of Lean code (clearly not what Fermat intended). Luckily, we found a wonderfully cursed
[Lean bug](https://github.com/leanprover/lean4/issues/14684)
, shown below, that suggests the proof may have fit the margin after all. The issue affects all stable versions of Lean up to 4.33.1, and the patch is incorporated in v4.34.0-rc1.

![“Figure showing a “checked” proof of Fermat’s Last Theorem using Lean 4.33.1”](/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/proof-fermat-image_hu_f4c2a5f3789324fb.webp)


A “checked” proof of Fermat’s Last Theorem using Lean 4.33.1

The blue checkmarks in the screenshot above would suggest that Lean considers this proof correct. This seems odd given the amount of work Sir Andrew Wiles put into this problem and the vast size of Claude’s proof. So what is going on?

The “proof” clearly doesn’t make any sense and exploits an issue in Lean. We found the issue while using GPT-5.6 to experiment with a new skill for code review. We want to clarify up front that the issue is not a kernel
[soundness issue](https://github.com/leanprover/lean4/pull/14806)
, but it happens to nicely fit any discussion of strings, lengths, and substrings.

The issue affects
`String.Pos.Raw.extract`
, Lean’s low-level string-slicing function. When asked to extract a one-byte slice at an
[astronomically large position](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/runtime/object.cpp#L2221-L2232)
, Lean’s
[logical definition](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/Init/Data/String/Basic.lean#L3012-L3014)
returns
[the empty string](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/Init/Data/String/Basic.lean#L3017)
. But the
[compiled native code](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/runtime/object.cpp#L2374)
returns
[the entire original string](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/runtime/object.cpp#L2376)
. That disagreement is enough to manufacture a contradiction. Lean’s ordinary evaluator “proves” that the tiny slice was empty, while native evaluation “proves” that the very same slice contained “a truly marvelous proof.” Put those together, and Lean concludes that the empty string equals a non-empty string. And once you have a contradiction, you can prove anything, including Fermat’s Last Theorem.

On the bright side, the Lean team was considerably faster than mathematical history. About 90 minutes after we reported the issue, hargoniX opened a fix for the
[memory-safety problem](https://github.com/leanprover/lean4/pull/14687)
, and it was merged roughly three hours after filing. The
[remaining semantic mismatch](https://github.com/leanprover/lean4/pull/14717)
was fixed by Rob23oba five days after the report, closing the issue. We’d like to give a huge shoutout to hargoniX, Rob23oba, and the Lean team for the fast turnaround.

As a reminder, when dealing with external proofs, follow Lean’s guidance for
[validating a Lean proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
. In our proof-of-concept code above,
`#print axioms flt`
shows
`'flt' depends on axioms: [propext, Classical.choice, Quot.sound, flt._native.native_decide.ax_1_1]`
. The extra axiom
`native_decide`
adds the compiler to the trusted boundary, and therefore needs to be used with care. Machine-checked proofs will increasingly enable an unprecedented level of trust in mathematical results and critical software. However, more work is needed (e.g.,
[lean4lean](https://github.com/digama0/lean4lean)
and
[alternative kernel implementations](https://arena.lean-lang.org/)
) to ensure that proofs aren’t deemed correct through exploitation of issues in theorem provers.

Fermat’s theorem took 350+ years to prove. If you don’t want to wait that long for your code to be audited,
[contact us](https://trailofbits.com/contact/)
.