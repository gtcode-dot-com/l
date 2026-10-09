---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-17T00:39:32.632666+00:00'
exported_at: '2026-02-17T00:39:39.074528+00:00'
feed: http://bair.berkeley.edu/blog/feed.xml
language: en
source_url: http://bair.berkeley.edu/blog/2024/09/20/linguistic-bias
structured_data:
  about: []
  author: ''
  description: The BAIR Blog
  headline: 'Linguistic Bias in ChatGPT: Language Models Reinforce Dialect Discrimination'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://bair.berkeley.edu/blog/2024/09/20/linguistic-bias
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Linguistic Bias in ChatGPT: Language Models Reinforce Dialect Discrimination'
updated_at: '2026-02-17T00:39:32.632666+00:00'
url_hash: 3570f8eadb18c3dd6c1233a60792d051681cd2e5
---

![](https://bair.berkeley.edu/static/blog/linguistic-bias/image1.png)

*Sample language model responses to different varieties of English and native speaker reactions.*

ChatGPT does amazingly well at communicating with people in English. But whose English?

[Only 15%](https://www.similarweb.com/website/chat.openai.com/#geography)
of ChatGPT users are from the US, where Standard American English is the default. But the model is also commonly used in countries and communities where people speak other varieties of English. Over 1 billion people around the world speak varieties such as Indian English, Nigerian English, Irish English, and African-American English.

Speakers of these non-âstandardâ varieties often face discrimination in the real world. Theyâve been told that the way they speak is
[unprofessional](https://doi.org/10.2307/3587696)
or
[incorrect](https://doi.org/10.4324/9781410616180)
,
[discredited as witnesses](https://muse.jhu.edu/article/641206/summary)
, and
[denied housing](https://www.taylorfrancis.com/chapters/edit/10.4324/9780203986615-17/linguistic-profiling-john-baugh)
âdespite
[extensive](https://www.routledge.com/Language-Society-and-Power-An-Introduction/Mooney-Evans/p/book/9780367638443)
[research](https://books.google.com/books?id=QRFIsGWZ5O4C)
indicating that all language varieties are equally complex and legitimate. Discriminating against the way someone speaks is often a proxy for discriminating against their race, ethnicity, or nationality. What if ChatGPT exacerbates this discrimination?

To answer this question,
[our recent paper](https://arxiv.org/pdf/2406.08818)
examines how ChatGPTâs behavior changes in response to text in different varieties of English. We found that ChatGPT responses exhibit consistent and pervasive biases against non-âstandardâ varieties, including increased stereotyping and demeaning content, poorer comprehension, and condescending responses.

## Our Study

We prompted both GPT-3.5 Turbo and GPT-4 with text in ten varieties of English: two âstandardâ varieties, Standard American English (SAE) and Standard British English (SBE); and eight non-âstandardâ varieties, African-American, Indian, Irish, Jamaican, Kenyan, Nigerian, Scottish, and Singaporean English. Then, we compared the language model responses to the âstandardâ varieties and the non-âstandardâ varieties.

First, we wanted to know whether linguistic features of a variety that are present in the prompt would be retained in GPT-3.5 Turbo responses to that prompt. We annotated the prompts and model responses for linguistic features of each variety and whether they used American or British spelling (e.g., âcolourâ or âpractiseâ). This helps us understand when ChatGPT imitates or doesnât imitate a variety, and what factors might influence the degree of imitation.

Then, we had native speakers of each of the varieties rate model responses for different qualities, both positive (like warmth, comprehension, and naturalness) and negative (like stereotyping, demeaning content, or condescension). Here, we included the original GPT-3.5 responses, plus responses from GPT-3.5 and GPT-4 where the models were told to imitate the style of the input.

## Results

We expected ChatGPT to produce Standard American English by default: the model was developed in the US, and Standard American English is likely the best-represented variety in its training data. We indeed found that model responses retain features of SAE far more than any non-âstandardâ dialect (by a margin of over 60%). But surprisingly, the model
*does*
imitate other varieties of English, though not consistently. In fact, it imitates varieties with more speakers (such as Nigerian and Indian English) more often than varieties with fewer speakers (such as Jamaican English). That suggests that the training data composition influences responses to non-âstandardâ dialects.

ChatGPT also defaults to American conventions in ways that could frustrate non-American users. For example, model responses to inputs with British spelling (the default in most non-US countries) almost universally revert to American spelling. Thatâs a substantial fraction of ChatGPTâs userbase likely hindered by ChatGPTâs refusal to accommodate local writing conventions.

**Model responses are consistently biased against non-âstandardâ varieties.**
Default GPT-3.5 responses to non-âstandardâ varieties consistently exhibit a range of issues: stereotyping (19% worse than for âstandardâ varieties), demeaning content (25% worse), lack of comprehension (9% worse), and condescending responses (15% worse).

![](https://bair.berkeley.edu/static/blog/linguistic-bias/image2.png)

*Native speaker ratings of model responses. Responses to non-âstandardâ varieties (blue) were rated as worse than responses to âstandardâ varieties (orange) in terms of stereotyping (19% worse), demeaning content (25% worse), comprehension (9% worse), naturalness (8% worse), and condescension (15% worse).*

When GPT-3.5 is prompted to imitate the input dialect, the responses exacerbate stereotyping content (9% worse) and lack of comprehension (6% worse). GPT-4 is a newer, more powerful model than GPT-3.5, so weâd hope that it would improve over GPT-3.5. But although GPT-4 responses imitating the input improve on GPT-3.5 in terms of warmth, comprehension, and friendliness, they exacerbate stereotyping (14% worse than GPT-3.5 for minoritized varieties). That suggests that larger, newer models donât automatically solve dialect discrimination: in fact, they might make it worse.

## Implications

ChatGPT can perpetuate linguistic discrimination toward speakers of non-âstandardâ varieties. If these users have trouble getting ChatGPT to understand them, itâs harder for them to use these tools. That can reinforce barriers against speakers of non-âstandardâ varieties as AI models become increasingly used in daily life.

Moreover, stereotyping and demeaning responses perpetuate ideas that speakers of non-âstandardâ varieties speak less correctly and are less deserving of respect. As language model usage increases globally, these tools risk reinforcing power dynamics and amplifying inequalities that harm minoritized language communities.

**Learn more here:
[[ paper ]](https://arxiv.org/pdf/2406.08818)**

---