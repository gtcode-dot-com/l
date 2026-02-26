---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T12:15:14.384936+00:00'
exported_at: '2026-02-26T12:15:16.644446+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html
structured_data:
  about: []
  author: ''
  description: 'LLMs are bad at generating passwords: There are strong noticeable
    patterns among these 50 passwords that can be seen easily: All of the passwords
    start with a letter, usually uppercase G, almost always followed by the digit
    7. Character choices are highly uneven ­ for example, L , 9, m, 2, $ and # appeared
    in all 50 passwords, but 5 and @ only appeared in one password each, and most
    of the letters in the alphabet never appeared at all. There are no repeating characters
    within any password. Probabilistically, this would be very unlikely if the passwords
    were truly random ­ but Claude preferred to avoid repeating characters, possibly
    because it “looks like it’s less random”. ...'
  headline: LLMs Generate Predictable Passwords
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: LLMs Generate Predictable Passwords
updated_at: '2026-02-26T12:15:14.384936+00:00'
url_hash: 682aa6d546e455c916ee0a5738c055f83df49294
---

## LLMs Generate Predictable Passwords

LLMs are
[bad](https://www.irregular.com/publications/vibe-password-generation)
at generating passwords:

> There are strong noticeable patterns among these 50 passwords that can be seen easily:
>
> * All of the passwords start with a letter, usually uppercase G, almost always followed by the digit 7.
> * Character choices are highly uneven ­ for example, L , 9, m, 2, $ and # appeared in all 50 passwords, but 5 and @ only appeared in one password each, and most of the letters in the alphabet never appeared at all.
> * There are no repeating characters within any password. Probabilistically, this would be very unlikely if the passwords were truly random ­ but Claude preferred to avoid repeating characters, possibly because it “looks like it’s less random”.
> * Claude avoided the symbol \*. This could be because Claude’s output format is Markdown, where \* has a special meaning.
> * Even entire passwords repeat: In the above 50 attempts, there are actually only 30 unique passwords. The most common password was G7$kL9#mQ2&xP4!w, which repeated 18 times, giving this specific password a 36% probability in our test set; far higher than the expected probability 2-100 if this were truly a 100-bit password.

This result is not surprising. Password generation seems precisely the thing that LLMs shouldn’t be good at. But if AI agents are doing things autonomously, they will be creating accounts. So this is a problem.

Actually, the whole process of authenticating an autonomous agent has all sorts of deep problems.

News
[article](https://gizmodo.com/ai-generated-passwords-are-apparently-quite-easy-to-crack-2000723660)
.

Slashdot
[story](https://it.slashdot.org/story/26/02/19/1842201/llm-generated-passwords-look-strong-but-crack-in-hours-researchers-find)

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[LLM](https://www.schneier.com/tag/llm/)
,
[passwords](https://www.schneier.com/tag/passwords/)
,
[random numbers](https://www.schneier.com/tag/random-numbers/)
,
[reports](https://www.schneier.com/tag/reports/)

[Posted on February 26, 2026 at 7:07 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html)
•
[0 Comments](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html#respond)

Sidebar photo of Bruce Schneier by Joe MacInnis.