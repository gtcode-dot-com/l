---
ai_commentary:
- body: AI-driven forgeries raise the risk of fraudulent reimbursements, pushing providers
    and employers to strengthen verification beyond surface-level image checks.
  title: Security implications for expense systems
- body: Current detectors leverage image metadata and contextual data, but skilled
    forgers can undermine these signals, highlighting the ongoing arms race between
    forgery and detection.
  title: Detection strategies and their limits
- body: Implement multi-layer verification, cross-check travel and expense data, maintain
    robust server-side logs, and combine automated checks with human review to mitigate
    fake receipts.
  title: Practical steps for organizations
ai_commentary_meta:
  content_digest: 8371f8b518ad8ab2e803ee43ba9439aea032af6a
  generated_at: '2025-11-10T02:01:14.896686+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
category: ai-security
date: '2025-11-09T05:30:09.765094+00:00'
exported_at: '2025-11-09T05:31:58.079702+00:00'
feed: https://www.schneier.com/feed/atom/
source_url: https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html
structured_data:
  about: &id001
  - AI-generated receipts are increasingly realistic, including details like wrinkles,
    itemization, and signatures.
  - Historically, forgery relied on physical materials; AI now enables convincing
    digital forgeries with less effort.
  - Expense management platforms can be deceived by AI-created receipts, prompting
    reliance on image metadata and contextual cues for detection.
  - Metadata can be stripped or altered by users via photos or screenshots, complicating
    verification.
  - Organizations are using broader contextual signals (e.g., server names, timestamps,
    trip details) to assess authenticity, fueling an AI-forensics arms race.
  description: Overview of how AI-generated receipts have become increasingly realistic,
    the challenges they pose to expense verification, and the ongoing security arms
    race as organizations seek stronger detection and contextual analysis.
  headline: Faking Receipts with AI
  keywords: *id001
title: Faking Receipts with AI
updated_at: '2025-11-09T05:30:09.765094+00:00'
url_hash: 0d56074a0ecffd570ebd09c27ba45cfc2e125d2c
---

## Faking Receipts with AI

Over the past few decades, it’s become easier and easier to create fake receipts. Decades ago, it required special paper and printers—I remember a company in the UK advertising its services to people trying to cover up their affairs. Then, receipts became computerized, and faking them required some artistic skills to make the page look realistic.

Now, AI can
[do it all](https://arstechnica.com/ai/2025/10/ai-generated-receipts-make-submitting-fake-expenses-easier/)
:

> Several receipts shown to the FT by expense management platforms demonstrated the realistic nature of the images, which included wrinkles in paper, detailed itemization that matched real-life menus, and signatures.
>
> […]
>
> The rise in these more realistic copies has led companies to turn to AI to help detect fake receipts, as most are too convincing to be found by human reviewers.
>
> The software works by scanning receipts to check the metadata of the image to discover whether an AI platform created it. However, this can be easily removed by users taking a photo or a screenshot of the picture.
>
> To combat this, it also considers other contextual information by examining details such as repetition in server names and times and broader information about the employee’s trip.

Yet another AI-powered security arms race.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[forgery](https://www.schneier.com/tag/forgery/)
,
[fraud](https://www.schneier.com/tag/fraud/)

[Posted on November 7, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html)
•
[6 Comments](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.