---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-22T04:27:20.020543+00:00'
exported_at: '2026-09-22T04:27:21.245363+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
source_url: https://www.niemanlab.org/2026/08/claude-is-changing-how-it-generates-prose-to-be-more-detectable-and-maybe-worse
structured_data:
  about: []
  author: ''
  description: 'It was in 1964 that Supreme Court Justice Potter Stewart, asked to
    define obscenity for the purposes of law, wrote his famous heuristic: "I know
    it when I see it." But when it comes to AI-generated content, we may think we
    know it when we see it — but our methods are far from perfect. W…'
  headline: Claude is changing how it generates prose to be more detectable (and maybe
    worse?)
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/08/claude-is-changing-how-it-generates-prose-to-be-more-detectable-and-maybe-worse
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Claude is changing how it generates prose to be more detectable (and maybe
  worse?)
updated_at: '2026-09-22T04:27:20.020543+00:00'
url_hash: 2f1ce66c7a61a194405a182c26d23ebabca46bef
---

It was in 1964 that Supreme Court Justice Potter Stewart, asked to define obscenity for the purposes of law, wrote his famous heuristic:
[“I know it when I see it.”](https://en.wikipedia.org/wiki/I_know_it_when_I_see_it)
But when it comes to AI-generated content, we may
*think*
we know it when we see it — but our methods are far from perfect. We’ve each assembled our own set of tells to look out for:
[too much “delving” and “fostering,”](https://meresophistry.substack.com/p/id-like-to-delve-into-how-ai-is-fostering)
[absolute phrases](https://youtu.be/0DDuG6b7aw8?si=AIKZ_i9GrVLvmAHy&amp;t=1029)
,
[negative parallelism](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/)
, or just
[too many em-dashes](https://medium.com/@brentcsutoras/the-em-dash-dilemma-how-a-punctuation-mark-became-ais-stubborn-signature-684fbcc9f559)
. But nothing is foolproof.

AI providers have leaned into the idea of adding watermarks to the content they generate —
[sometimes visible](https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/)
to humans,
[sometimes visible](https://deepmind.google/models/synthid/)
only to a dedicated tool. But adding a watermark to visual media is a much less sticky problem than adding it to text — text that might be edited or removed from its original context. Other than looking for “It’s not X. It’s Y,” how can we know if a set of words we read came from a human or a chatbot?
[European regulators](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)
are forcing Big AI to come up with answers.

Last week,
[Anthropic announced](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)
that it would begin
[adding invisible watermarks](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/)
to the text it generates, and on Friday, it
[explained how it’s going to work](https://www.anthropic.com/news/claude-text-watermark)
. Daring Fireball’s John Gruber
[has a good, clear piece](https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing)
that explains both the methodology and how it, in his mind, perverts the act of writing. In essence, it involves Claude intentionally changing some of the words it’s generating to less-likely options — picking “guava” instead of “mango,” say, or “auto” instead of “car” — in patterns that Anthropic can then detect.
[Some people](https://www.businessinsider.com/claude-users-cancel-subscriptions-citing-anthropic-new-ai-watermark-2026-8)
don’t like it; Gruber hates it:

&gt; One of my fundamental problems with this is that no two synonyms carry the exact same meaning. “
&gt;
&gt; *He leaped at the chance*
&gt;
&gt; ” and “
&gt;
&gt; *He jumped at the opportunity*
&gt;
&gt; ” are very similar sentences expressing the same general sentiment, but they are
&gt;
&gt; *not*
&gt;
&gt; the same. The exact words we choose when writing matter. I want any LLM I use to choose the very best, most precise words at every single decision point. An obvious constraint that I accept is time and computation. Within the constraint of executing inference quickly, and at a certain cost per token, I want the best words. This constraint matches human writing. I could surely write a better column by taking longer to write it. I write with a sense of how much care I should put into every word and punctuation choice I make. I take more time with certain paragraphs, sentences, or even individual word choices when my gut feeling says I should.
&gt;
&gt; In other words, these are
&gt; *necessary*
&gt; trade-offs. These factors are all in
&gt; *my*
&gt; interest: speed, cost, quality. Ideally I would like perfect writing, at instantaneous generation speed, at zero cost. None of those things are possible. Computation is not free of charge (and cloud-based LLM inference with leading models is actually expensive). Inference is not instantaneous. And great writing, whether natural or artificial, can only
&gt; *approach*
&gt; perfection.
&gt;
&gt; The idea that anything other than
&gt; *my*
&gt; needs should factor into the generation of text for
&gt; *me*
&gt; is patently offensive.

Whether it’s more or less offensive than any other AI-generated text is an exercise left to the reader.

Show tags

Hide tags