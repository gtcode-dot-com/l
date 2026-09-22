---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-22T04:27:07.108647+00:00'
exported_at: '2026-09-22T04:27:21.257960+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
source_url: https://www.niemanlab.org/2026/08/googles-new-ai-tool-helps-fact-checkers-investigate-ai-fakes
structured_data:
  about: []
  author: ''
  description: Backstory automates provenance checks, reverse image searches, and
    context tracing to speed up verification work.
  headline: Google’s new AI tool helps fact-checkers investigate AI fakes
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/08/googles-new-ai-tool-helps-fact-checkers-investigate-ai-fakes
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google’s new AI tool helps fact-checkers investigate AI fakes
updated_at: '2026-09-22T04:27:07.108647+00:00'
url_hash: 696429e017c89bb72c518280b18478629980dcec
---

Every day the
[fact-checking team](https://www.indiatoday.in/fact-check)
for one of India’s largest news organizations works to debunk a slew of false and misleading images circulating across social media. For the six-person team at India Today, that might include addressing an
[AI-generated archival photograph](https://www.indiatoday.in/fact-check/story/fact-check-viral-indira-gandhi-dhirendra-brahmachari-photo-is-ai-generated-2973268-2026-08-17)
of a politician, a
[clip of deadly flooding](https://www.indiatoday.in/fact-check/story/kerala-floods-video-fact-check-karachi-pakistan-not-kerala-2963109-2026-08-04)
ripped from its original context, or a
[full-on deepfake](https://www.indiatoday.in/fact-check/story/this-mukesh-ambani-video-is-a-deepfake-it-sells-a-scam-2433006-2023-09-08)
of India’s richest man.

[Backstory](https://deepmind.google/blog/exploring-the-context-of-online-images-with-backstory/)
, an experimental tool from Google’s AI research lab, Google DeepMind, is helping India Today sort through this stream of slop, scams, and disinformation.

After uploading an image and entering a basic question, Backstory can automatically run checks to determine whether the image is AI-generated, whether it shows signs of manipulation, and where else the image has appeared throughout its lifetime on the internet. Built on top of
[Google’s Gemini](https://deepmind.google/models/gemini/?_gl=1*v8kbv3*_up*MQ..*_ga*Njc2NDM5MzkxLjE3NTE4ODYzMTk.*_ga_LS8HVHCNQ0*czE3NTE4ODYzMTgkbzEkZzAkdDE3NTE4ODYzMTgkajYwJGwwJGgw)
family of large language models (LLMs), Backstory also leans on AI agents to decide which authentication tools it will use and in what order it will use them. The final output is an AI-generated report summarizing what Backstory found out about the image, with citations, as well as a log of the steps it took along the way.

![Backstory gif](https://www.niemanlab.org/images/Backstory.gif)

At India Today, Backstory is primarily used to take the first pass on fact-checking a piece of content, speeding up the beginning of the verification workflow.

“On our team, almost everybody uses Backstory in combination with other things. We use it as a quick reference — it gives you some context, it gives you some direction,” said
[Bal Krishna](https://x.com/bala3047)
, who leads the fact-checking team. “It is doing all the work you might have done with five different tools, five different logins, in the same place. That’s the beauty of it.”

In the past, reporters at India Today might have needed to separately run an image through an AI image detector, conduct a reverse image search, and then stitch together a timeline of its historical appearances. Backstory will do all those things at once and, for now, it is entirely free to use.

“The unique value add for Backstory is that there are a number of bites at the apple,” said
[Zoe Darmé](https://www.linkedin.com/in/zoe-darm%C3%A9-a8661a4/)
, a product manager for Frontier AI Research, the team at DeepMind building the tool. “A lot of times when we’re talking about looking at an image, trying to understand it in context, people are focusing on one part of the chain. Backstory is really trying to pull it all together into a single user experience.”

Backstory is still only available through Google’s Trusted Testers Program, but India Today’s fact-checkers are among the thousands of journalists, OSINT experts, librarians, and information literacy researchers Google has brought on to trial the tool. The team is currently collecting feedback from this group to make improvements.

That’s already a departure from the many AI authentication tools built without adequate input from journalists, according to a
[report published in July by Princeton’s Center for Information Technology Policy](https://www.niemanlab.org/2026/07/ai-authentication-tools-are-built-without-proper-journalist-input-new-report-finds/)
.

Many other commercial AI detections tools don’t take into account more nuanced forms of manipulation — like divorcing a photograph from its original context — that journalists encounter all the time. A lot of these tools also output percent confidence ratings. For example, they might spit out an 80% likelihood that an image is AI-generated. These ratings are a “black box” with little clarity provided on how ratings are decided or ways to communicate those numbers to readers, according to the report.

Darmé told me she thinks of journalists as Backstory’s core users, but does hope to make the tool more widely available in the future. Even if Backstory launched publicly, she says it will most likely appeal to a niche audience invested in the nuances of image verification, and looking to answer more than the binary question of whether an image is “real” or “fake.”

According to
[Mike Caulfield](https://hapgood.us/about/)
, a digital literacy expert and creator of the
[SIFT method](https://guides.lib.uchicago.edu/c.php?g=1241077&amp;p=9082322)
, building for this niche might be even more impactful than building a universal tool for anyone on the internet.

“Information environments work in this very intermediated way, where what actually has the most impact on an information environment is to help the helpers,” Caulfield told me, explaining that vetted information flows out from trusted sources, including journalists and fact-checkers, but also more casual hobbyists he calls the “
[family fact-checker](https://www.poynter.org/fact-checking/2020/have-you-become-a-personal-fact-checker-to-your-family-and-friends/)
.”

Caulfield describes Backstory as filling a hole in the market by building for these helpers. He notes that not every beat reporter who needs to verify an image is going to have subscriptions to high-quality AI detection tools, or the expertise to use the dozen of tools in an OSINT specialist’s toolbox.

“There hasn’t really been a tool for something in between the general user and that highly specialized user; between Bob from Peoria [Illinois] — not to pick on Peoria — and

[Craig Silverman](https://www.craigsilverman.ca/)

,” said Caulfield, name-checking the disinformation expert and investigative journalist. “This is a tool that really hits that underserved middle.”

As part of its AI detection features, Backstory can run a tool call for
[SynthID](https://deepmind.google/models/synthid/)
— a way to check for watermarks embedded in images created with
[Nano Banana](https://gemini.google/overview/image-generation/)
, Google’s AI image generation model. Backstory also checks an image’s content credentials, looking for encrypted metadata added by companies who have signed onto the
[Coalition for Content Provenance and Authenticity (C2PA) standard](https://c2pa.org/)
, including Google, Adobe, and the BBC.

Caulfield, however, says the tool’s ability to trace the history of an image online is often its most useful feature. That feature allows journalists to see an image in its original context, and chart how that context may have changed over time.

“The integration aspect — telling the full story of the image — turns out to be the really time-consuming part,” said Caulfield. “Backstory takes an initial process that would take you 50 minutes, and it can shrink it down to three.”

This feature takes on a challenge that long predates the rise of AI-generated imagery. “If you talk to any fact-checker, I don’t think anybody is going to tell you that they wouldn’t have loved to have this tool in 2016,” he said.

Google DeepMind, like many of the largest AI model makers, has contributed to the more recent explosion of AI-generated imagery on the internet.
[Nano Banana](https://gemini.google/overview/image-generation/)
has been routinely criticized for contributing to
[disinformation about politicians and public health](https://www.newsguardtech.com/special-reports/google-new-ai-image-generator-misinformation-superspreader/)
, and
[even for its use by online scammers](https://www.youtube.com/watch?v=U9h0-6NnmAQ)
.

Most recently, Google Earth came under fire in late July for
[integrating Nano Banana](https://blog.google/products-and-platforms/products/earth/nano-banana-google-earth-image-generation/)
into its platform, allowing users to easily manipulate and alter 3D satellite images. Just a day later, Google announced it would
[roll back the feature](https://www.bbc.com/news/articles/c9349yx2ydvo)
and build “stronger guardrails” after examples of false and misleading imagery spread widely online.

Darmé says the decision to build Backstory wasn’t a direct response to these types of criticisms, but it was an attempt to address

[deteriorating trust in media content](https://www.gstatic.com/marketing-cms/9a/ba/d9442b4b4082855ba7f0c78f79c5/determining-trustworthiness-en.pdf)

on the internet at large.

“Having worked on tools that brought image generation to a large population of users, having listened really closely to feedback from users in terms of what they wanted, there’s a clear user need,” she said, explaining DeepMind’s investment in building an easy-to-use provenance tool. “That might be something slightly different than [feeling] this team has one-to-one personal responsibility to release a tool because we also are in a company that releases Nano Banana.”

Like most tools powered by LLMs, Backstory can’t guarantee accuracy. A disclaimer appears at the bottom of the tool, similar to the one that appears on Google’s general AI assistants: “Backstory can make mistakes, so double-check it.”

A common problem with using LLMs to authenticate images is conflation, when the models mistake one image with another that is visually similar, according to Caulfield. “If you put in an image that can be described in the same way as another image that’s very popular online, it’s not uncommon for the LLM to confuse the two images,” he told me.

This problem surfaced in my own testing. After prompting Backstory to generate a report on the history of my own headshot, it ended up mistaking my image with the headshot of another journalist, Carlos Maza. His headshot came up with the same text search terms, including “man with curly hair,” “black cap,” “smiling.” Backstory output a full report on the history of Maza’s headshot on the Internet, before I fed my name into the tool and it eventually corrected itself.

![](https://www.niemanlab.org/images/Screenshot-2026-08-17-at-5.06.58-PM.png)

There are other limitations with the tool. Right now, Backstory can only process images, though the team is exploring video and other modalities, according to Darmé. In its context tracing reports, Backstory can also only reference images that have been indexed on search engines. Even when Backstory claims to have found the origin of an image, it could have had a life beyond the tool’s view.

“It’s possible that something might have originated on TikTok, which is not indexed. It might have originated on WhatsApp or Signal or any other closed group,” said

[Bal Krishna](https://x.com/bala3047)

. “Using Backstory you should keep these limitations in mind. We always do.”

Due to these current shortcomings, Bal Krishna says India Today does not cite Backstory’s AI-generated reports directly in its published fact-checks, and reporters are expected to manually confirm any information they pull from the tool.

Still, he considers Backstory the “first robust tool made by a big tech company that was offered to fact-checkers” for image verification, and is hopeful it will only improve as feedback from testers is folded into the product.

When I asked if Backstory had sped up the daily work of his fact-checkers, he responded, “There is no doubt about it.”