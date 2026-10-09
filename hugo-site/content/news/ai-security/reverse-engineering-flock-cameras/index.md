---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T00:14:30.808661+00:00'
exported_at: '2026-10-04T00:14:39.242635+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html
structured_data:
  about: []
  author: ''
  description: 'Hackers captured a Flock camera and got a look (alternate link) at
    the software: While much of the automatic license plate reader’s (ALPR) most sensitive
    storage remained encrypted and inaccessible, the joint analysis of the recovered
    data shows that software running on the device explicitly detects people as well
    a...'
  headline: Reverse-Engineering Flock Cameras
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Reverse-Engineering Flock Cameras
updated_at: '2026-10-04T00:14:30.808661+00:00'
url_hash: 0cc433038125f05d296e58ad52546f3bb15ecfee
---

## Reverse-Engineering Flock Cameras

Hackers captured a Flock camera and got a
[look](https://www.404media.co/hackers-stole-flocks-camera-software-revealing-how-the-company-tracks-cars-and-people-2/)
(alternate
[link](https://archive.ph/gQoMs)
) at the software:

&gt; While much of the automatic license plate reader’s (ALPR) most sensitive storage remained encrypted and inaccessible, the joint analysis of the recovered data shows that software running on the device explicitly detects people as well as vehicles, license plates, and bicycles. The camera can produce dozens of images of a single passing vehicle and, according to several weeks of recovered logs, generated more than a million images. Its computer-vision software also sometimes isolated bumper stickers and other graphics, including, in one case, an American flag patch on a motorcyclist’s saddlebag.

If you’re wondering how the hackers got by disk encryption, one of the unencrypted partitions contained the key for an encrypted partition. That’s pretty bad security engineering.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[cameras](https://www.schneier.com/tag/cameras/)
,
[cars](https://www.schneier.com/tag/cars/)
,
[reverse engineering](https://www.schneier.com/tag/reverse-engineering/)

[Posted on September 21, 2026 at 10:37 AM](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html)
•
[10 Comments](https://www.schneier.com/blog/archives/2026/09/reverse-engineering-flock-cameras.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.