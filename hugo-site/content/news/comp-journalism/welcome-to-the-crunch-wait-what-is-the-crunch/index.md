---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2025-11-11T15:20:00.732876+00:00'
exported_at: '2025-11-11T15:20:02.501045+00:00'
feed: https://www.theguardian.com/media/data-journalism/rss
source_url: https://www.theguardian.com/news/2023/nov/30/the-crunch-noisychart-audio-video-series
structured_data:
  about: []
  author: ''
  description: Why we’re making charts with audio, and how that relates to our new
    video series and newsletter
  headline: Welcome to The Crunch. Wait, what is The Crunch?
  keywords: []
  main_image: ''
  original_source: https://www.theguardian.com/news/2023/nov/30/the-crunch-noisychart-audio-video-series
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Welcome to The Crunch. Wait, what is The Crunch?
updated_at: '2025-11-11T15:20:00.732876+00:00'
url_hash: 8f88044cda0dd101b51d33f497be7fefd2a5212d
---

Welcome to The Crunch! I’m Nick Evershed, Guardian Australia’s data editor, and today we are launching a
[new video series](https://www.theguardian.com/australia-news/video/2023/nov/30/the-crunch-what-australias-love-for-suvs-means-for-emissions-and-safety-video)
and
[newsletter](https://www.theguardian.com/news/2023/nov/08/sign-up-for-the-crunch-newsletter-our-free-email-with-the-best-charts-graphs-and-dataviz)
, and bringing together our data, interactive and visual journalism under a
[single banner](https://www.theguardian.com/news/series/the-crunch)
.

Today also represents a significant milestone in Guardian Australia’s goal to make our data journalism more accessible – bringing it to audio and video as well as giving vision-impaired people an alternative to “alt text” when accessing our charts.

## What is a noisychart?

The Crunch will take one key chart on an important topic, such as the housing crisis or climate change, turn it into audio and video, and discuss what it means for the world with an expert or a journalist who has been working in the area. We may also throw in a few extra charts for good measure. We like charts.

You can watch or listen to the pilot episode here, which charts the rise of SUVs and asks: why does it feel like every car is an SUV now?

The Crunch: what Australia's love for SUVs means for emissions and safety – video

To do this, we’re
[using the noisycharts app](https://www.theguardian.com/news/datablog/2022/nov/16/noisycharts-sound-graphs-data-sonification-introducing-guardian-australia-software-tool-app-examples)
I have been working on (in between doing my usual job!) over the past year.

The app maps data against an audio parameter, usually frequency or pitch (I have also tested other parameters such as volume, tempo and panning). The audio is then output with an animated chart, which we use for our video or podcast reporting.

Sydney's record-breaking rainfall

You can read more about the history of the project
[here](https://www.theguardian.com/news/datablog/2022/nov/16/noisycharts-sound-graphs-data-sonification-introducing-guardian-australia-software-tool-app-examples)
but we hope it will help bring our work to a wider audience – allowing people who use screen readers to hear the trends instead of relying on alt text, which unfortunately is poorly implemented in many places.

The noisycharts tool is not yet ready for a public release as it relies on a Guardian tool to turn spreadsheets into charts. I’m hoping to have a public version available early next year which lets anyone create a chart by copy-pasting data or uploading a spreadsheet.

## How will this make graphs more accessible?

The other news is that by building an app that lets me test different approaches to sonification of data, as well as spending some time reading the existing academic literature on the topic, I think I am close to my goal of building a default audio mode into our in-house chart tool. That is, making the majority of charts we publish in an article available as audio versions.

[Here’s a work-in-progress demo of the accessibility mode I’ve been working on](https://interactive.guim.co.uk/embed/superyacht-testing/index.html?key=1hxk6BFGjfsbTV8uRqlJWCvuiqZXUyqAgPrQXU08bVuk&location=docsdata)
(it works best in Chrome, may have bugs and may not work at all in the Guardian app, so click to load it in a mobile browser).

[And here’s another one](https://interactive.guim.co.uk/embed/superyacht-testing/index.html?key=oz-datablogs-2023-union-membership-decline-over-time&location=yacht-charter-data)
which shows how it handles missing data.

[skip past newsletter promotion](#EmailSignup-skip-link-15)


Sign up to
The Crunch

Free fortnightly newsletter

Our data journalists showcase the most important charts and dataviz from the Guardian and around the web, free every fortnight



**Privacy Notice:**
Newsletters may contain information about charities, online ads, and content funded by outside parties. If you do not have an account, we will create a guest account for you on
[theguardian.com](https://www.theguardian.com)
to send you this newsletter. You can complete full registration at any time. For more information about how we use your data see our
[Privacy Policy](https://www.theguardian.com/help/privacy-policy)
. We use Google reCaptcha to protect our website and the Google
[Privacy Policy](https://policies.google.com/privacy)
and
[Terms of Service](https://policies.google.com/terms)
apply.

after newsletter promotion

The tricky part is designing an app that works systemically to produce the best results based on a minimum of user input. For example, figuring out what date intervals the chart is using so it can be read out properly.

I’ve also added a function to enable people to pause and resume the chart playback, and use shortcut keys to move through the data point-by-point like a cursor, as well as switch between data series. Research suggests that while sonification of data can be effective in communicating trends, it can be difficult to identify the actual values being played at any given moment. It’s in an early stage, but this “cursor” function aims to help people find specific values if they need to.

I’ve got a few more features to add and bugs to fix and then I hope to be able to send this to people and organisations for testing and feedback – so please get in touch if you’d like to help:
[nick.evershed@theguardian.com](mailto:nick.evershed@theguardian.com)
.

## Send us cool charts

If you’re an academic, researcher, analyst, data journalist or just a general dataviz-enthusiast and you’ve made a cool, important or interesting chart, or you’ve seen one and would like to share it, then please email us at
[thecrunch@theguardian.com](mailto:thecrunch@theguardian.com)
and we might feature it in our fortnightly newsletter.

## Like and subscribe

Otherwise, if you want to get a round-up of the best charts from the Guardian and elsewhere, as well as get notified when there’s a new episode of our video series, then you can
[sign up for the fortnightly newsletter here](https://www.theguardian.com/news/2023/nov/08/sign-up-for-the-crunch-newsletter-our-free-email-with-the-best-charts-graphs-and-dataviz)
.

You can also follow us on
[X (formerly Twitter)](https://twitter.com/NickEvershed)
,
[Bluesky](https://bsky.app/profile/nickevershed.bsky.social)
or
[Threads](https://www.threads.net/)
and subscribe to the
[Guardian Australia YouTube channel](https://www.youtube.com/channel/UCoWKwd06OC0Y0XpvAa8jfdw?sub_confirmation=1)
.