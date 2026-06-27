---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-27T04:22:54.794901+00:00'
exported_at: '2026-06-27T04:22:57.216466+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/allenai/hybrid-token-prediction
structured_data:
  about: []
  author: ''
  description: A Blog post by Ai2 on Hugging Face
  headline: Which tokens does a hybrid model predict better?
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/allenai/hybrid-token-prediction
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Which tokens does a hybrid model predict better?
updated_at: '2026-06-27T04:22:54.794901+00:00'
url_hash: 04bd48744b58f91b4b4c38e365eef5ffe03e9092
---

# Which tokens does a hybrid model predict better?

📄

**Tech report:**
&lt;https://arxiv.org/abs/2606.20936&gt;

[![Hybrid token prediction blog draft will also be published to Hugging Face - Goog-image-1](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/5-hA9oXDAmu9e__tV-FYM.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/5-hA9oXDAmu9e__tV-FYM.png)

Which kinds of tokens does a model predict well, and which does it not? That question is especially intriguing in the case of hybrids, a language model architecture that’s begun to challenge the standard transformer and that we’ve been investigating with
[Olmo Hybrid](https://allenai.org/blog/olmohybrid)
.

Hybrids can match or beat transformers on standard benchmarks, but the headline numbers don’t reveal much about what specific advantages hybrid models have over transformers.

In an attempt to shed light on these token-level behaviors, we recently conducted experiments comparing our own strongest 7B transformer,
[Olmo 3](https://allenai.org/blog/olmo3)
, and hybrid model, Olmo Hybrid, head-to-head. Specifically, we compare the differences in model predictions in a fine-grained way across different types of tokens, or units of information that appear as input to an LLM.

Because Olmo 3 and Olmo Hybrid were built to be as alike as possible outside their architectures — closely matched in data, tokenizer, and training recipe — any difference in their predictions mostly reflects the architecture itself. Viewing these differences at the token level allows us to glean insights about the specific strengths of hybrid models over transformers.

[Our results](https://arxiv.org/abs/2606.20936)
show that the hybrid’s advantage is real across many tokens, but not all. Olmo Hybrid is strongest on tokens that carry meaning, such as nouns, verbs, and adjectives, and on tokens that can only be predicted by following what’s going on, like which person a pronoun refers to. But the hybrid’s advantage almost disappears on tokens that simply repeat something already in the input — a word or phrase reproduced verbatim from earlier — where the answer is sitting right there to be looked up. That’s where the transformer’s strength lies.

## Attention versus recurrence, and measuring the difference

A language model is built from a stack of repeated layers, each one refining its representation of every token using the tokens around it.

A transformer uses attention in every layer. The model can draw directly on every earlier token at once, weighing how relevant each is to the current prediction. That makes attention good at recalling a specific earlier token exactly, even when that token appeared far back in the input. The catch is that every token is compared against all the earlier ones, so attention’s cost climbs steeply as the input grows. Additionally, while attention is strong at recalling and aggregating information, it also struggles to represent information that evolves sequentially over time.

A hybrid model keeps a few attention layers but swaps the rest for recurrent layers. Unlike an attention layer, a recurrent layer reads tokens left to right and carries a fixed-size memory, folding each new token into memory as it goes so the cost of processing each token stays flat however long the input gets. That memory is compressed and lossy, so a recurrent layer can’t reach back for an exact earlier token the way attention can. But it is well suited to keeping a running account of anything that changes as the model reads tokens, providing a complementary strength to attention.

To isolate the areas of strength and weakness for attention and recurrent layers, we fed Olmo 3 and Olmo Hybrid passages of text: articles, Wikipedia entries, books, and scientific papers, as well as structured text like Python, HTML, and LaTeX. We scored each model on how well it predicted each token from the tokens before it in a given sample.

Both models saw the same earlier tokens and assigned a probability to every possible next token. We recorded the probability each gave to the token that actually followed. We then summarize the difference between the two models token by token by computing the loss gap, or the difference in loss between the two models. A positive gap means the hybrid predicted the real next token better. A negative gap means the transformer did.

To find where the loss gaps might concentrate, we ran several analyses. First, we sorted each token into a category and averaged the loss gap within these categories. Because a raw average can be skewed by other factors, such as a category’s rarity or how often tokens repeat in a sample of text, we re-checked each pattern with a regression that estimates the category’s own effect while holding other factors constant.

## What real text shows

[![Hybrid token prediction social copy - Google Docs-image-2](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/jhU9qFfYhuKlt4BqOGyIh.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/jhU9qFfYhuKlt4BqOGyIh.png)

We find that Olmo Hybrid has lower loss than Olmo 3 on most kinds of tokens, though not by the same amount on each.

In prose, the clearest divide is between content words — meaning-bearing nouns, verbs, and adjectives — and function words like “the,” “of,” and “is.” The hybrid predicts content words better than the transformer, with a loss gap around

0.04
0.04





0.04
, whereas the gap is closer to

0.02
0.02





0.02
on function words.

In particular, on content-word categories like adverbs and adjectives, the advantage of hybrid models is especially pronounced, though some function-word categories like existentials, such as “there,” also show a large advantage for hybrid models. In short, the hybrid’s edge is biggest on the words that say what a sentence is about and smallest on the grammatical words any model can nearly guess from syntax.

In contrast, we find some specific contexts where the advantage of hybrid models over transformers disappears. The first is closing, but not opening, braces, a pattern that is robust across brackets in language, code, and markup. Why? It’s known that attention suffices for representing bracket matching, which suggests attention alone suffices for closing brace prediction.

[![Hybrid token prediction social copy - Google Docs-image-3](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/O_9IONHpoc8kd31TP1MnR.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/O_9IONHpoc8kd31TP1MnR.png)

The second place where the hybrid’s advantage all but disappears is when the next token simply repeats something already in the passage. We spot these cases by looking for repeated n-grams: runs of text where the token that completes a sequence has appeared, verbatim, earlier in the same passage. The longer the repeated run, the smaller the hybrid’s lead, until it approaches zero.

Finally, inspired by these findings, we explore using filtered losses on specific types of tokens as an evaluation to better compare different architectures in pretraining experiments. We use three 1B-parameter models from our earlier
[Olmo Hybrid work](https://example.com)
: a transformer, a hybrid, and a pure recurrent model with no attention at all.

On meaning-bearing tokens that aren’t repeats, the hybrid and pure recurrent model overtake the transformer, with the hybrid performing the best. On repeated tokens, the pure recurrent model — with no attention to reach back for the copy — falls behind both the hybrid and the transformer.

Thus, these filtered token losses reveal different fine-grained differences between architectures, including copying abilities and differences on content words, early in training in a way that would not otherwise be visible.

## Where this leaves us

[![Hybrid token prediction social copy - Google Docs-image-4](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/6i5GcnfYp7U6KfYpsN3e2.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/6i5GcnfYp7U6KfYpsN3e2.png)

*Filtered token losses surface architecture differences during 1B pretraining. Token-loss curves at WSD-annealed checkpoints for a transformer, a hybrid, and a pure recurrent neural network, or RNN.*

Two lessons follow from this work.

First, a single overall loss — the model’s average error across all tokens — is too blunt to compare transformer and hybrid architectures. Scoring the loss on just the tokens that test a specific model ability surfaces key differences.

Second, specifically for hybrid models, we found evidence of particular advantages on open-class tokens, which perhaps is related to the state-tracking capabilities of RNN layers.

As a next step, we’re taking these findings into our ongoing hybrid modeling work. We believe the best hybrid architectures will come from understanding, token by token, what each component of a model does well. We hope studies like this help that understanding grow across the whole AI community.

We encourage you to read our
[full report](https://arxiv.org/abs/2606.20936)
, explore
[Olmo 3](https://allenai.org/blog/olmo3)
, try
[Olmo Hybrid](https://allenai.org/blog/olmohybrid)
, and dig into their associated open artifacts.