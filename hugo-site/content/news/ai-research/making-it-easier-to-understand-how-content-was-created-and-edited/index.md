---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-24T00:02:32.866845+00:00'
exported_at: '2026-05-24T00:02:34.347109+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/making-it-easier-to-understand-how-content-was-created-and-edited
structured_data:
  about: []
  author: ''
  description: We're expanding our tools to help you understand how content was created
    and edited across the web.
  headline: Making it easier to understand how content was created and edited
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/making-it-easier-to-understand-how-content-was-created-and-edited
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Making it easier to understand how content was created and edited
updated_at: '2026-05-24T00:02:32.866845+00:00'
url_hash: 68616f3660cd09d0a207fd5735f9645d9143c289
---

As generative media becomes more advanced and accessible, it’s helpful to know where content comes from, and whether it’s been altered. Today, we’re expanding our content transparency and verification tools in Search, Gemini, Chrome, Pixel and Cloud, and deepening our partnership with the broader industry.

## Scaling our technology

Three years ago, we introduced
[SynthID](https://deepmind.google/blog/identifying-ai-generated-images-with-synthid/)
, our industry-leading digital watermarking technology that embeds imperceptible signals into AI-generated content. Since then, we've integrated SynthID into our generative media models and products, watermarking over 100 billion images and videos and 60,000 years of audio.

Across a growing number of our generative media tools, we use
[C2PA Content Credentials](https://contentcredentials.org/)
, the industry standard that shows how media was created and modified, with or without AI.
[Pixel 10](https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html)
was the first smartphone to provide Content Credentials for images in its native camera app, and we are expanding this technology to include video on Pixel 8, 9 and 10 phones in the coming weeks.

By using this technology at the point of capture, Pixel documents when content has been captured by a camera. In an era of generative media, we believe that identifying authentic, unedited content can be just as important as knowing when a file was made or edited using AI.

## Providing more ways to verify content

Our goal is to make it easier to learn more about the content you encounter online. That’s why we recently added SynthID verification for image, video and audio to the
[Gemini app](https://blog.google/innovation-and-ai/products/ai-image-verification-gemini-app/)
. Already, it’s been used 50 million times globally, and we’re expanding this verification capability to Search today and Chrome over the coming weeks.

You can learn about an image's origin by using Search features like Lens, AI Mode and Circle to Search, as well as Gemini in Chrome. Just ask, "Is this made with AI?” or “Is this AI generated?”

We’re also adding verification for C2PA Content Credentials, to easily check if content is an unaltered original from a camera or if it has been modified, and by what tools. This feature is rolling out in the Gemini app starting today, and it will come to Search and Chrome in the coming months. This builds on features like the
[labels on YouTube](https://blog.youtube/news-and-events/disclosing-ai-generated-content/)
that identify AI-generated content and our work with trusted testers on
[Backstory](https://deepmind.google/blog/exploring-the-context-of-online-images-with-backstory/)
to make detection tools faster and more reliable.