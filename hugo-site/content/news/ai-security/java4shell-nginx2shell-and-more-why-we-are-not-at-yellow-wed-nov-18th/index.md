---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-21T00:31:30.757836+00:00'
exported_at: '2026-11-21T00:31:31.582068+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33532
structured_data:
  about: []
  author: ''
  description: 'Java4Shell, NGINX2Shell and more: Why we are not at "Yellow", Author:
    Johannes Ullrich'
  headline: 'Java4Shell, NGINX2Shell and more: Why we are not at "Yellow", (Wed, Nov
    18th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33532
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Java4Shell, NGINX2Shell and more: Why we are not at "Yellow", (Wed, Nov 18th)'
updated_at: '2026-11-21T00:31:30.757836+00:00'
url_hash: ea9ba29c00155fe87145b69e1ff5d0b8daf35c42
---

About a month ago, we went to Infocon Yellow for the first time in a few years. We decided to address the php2shell vulnerability and alert our readers to its significant impact. Following php2shell, we had a number of vulnerabilities and events that may also have scored high enough to trigger an Infocon "Yellow" [infocon]. In the last few days, we had a major Microsoft 365 outage, a critical vulnerability in Java, and a critical vulnerability in NGINX, which was disclosed today.

My plan today was to write a bit about attacks we are seeing against one of our Java-specific honeypots. But the results can be summarized in one sentence: We are seeing many attacks, but none that exploit Java4Shell (yet). Will it be an important issue? Probably. Should you patch? Sure. Will the world as we know it end? Maybe.

So why not go to "Yellow"? This is not a new question. Often people ask why we are on "Green" if they are seeing hundreds or thousands of attacks hitting their system each day. The Internet is a dangerous place. Shouldn't we be on "Yellow" (or "Orange") to reflect that danger? My answer has been: "Green" means the Internet is broken as usual. As long as the status is "Green", you should expect a normal "9-to-5" day. I have heard from organizations that have used our infocon to justify staffing and overtime, and I am well aware of the impact it may have.

The reason behind our conservative Infocon is that you can't be alert and "on guard" all the time. An alert status that is "high" all the time is meaningless and counterproductive. You must not treat these recent vulnerabilities as "emergencies". They are the "new normal". Treat them as such. You will not be able to patch nginx2shell across a large organization before the exploit is released. Instead of trying to do the impossible and fail, think beyond the vulnerability of the day. A new reality requires new procedures and techniques. Here are a few ideas:

* Automate patching as much as possible, in particular for less critical systems. Traditionally, automatic patching had two significant drawbacks. First, you may crash a system because of a failed patch. Secondly, the patch may not be applied correctly, and you treat a vulnerable system as "patched".

  Select less critical systems that would be at the end of your patch priority list. I'd rather take a system down myself than have ransomware do it for me. Having a system possibly patched is better than being sure the system isn't patched. And of course, there should be some testing, but that can wait a bit longer. This responds well to the faster development of exploits.
* Reduce your exposure. This should have been a priority years ago. But there are still too many systems connected to the internet that shouldn't be connected. Build a defensible architecture. The same is true for individual applications: reduce the "blast radius" by restricting which data and resources each application can access. And reduce your supply chain exposure. Do you get enough value from tools like Optimizely to justify the risk of them compromising your application?
* Avoid chasing squirrels. Do not change your plan and drop what you are doing just because the world is going to end. The world may end, in which case, patching one more system is probably not going to make a difference. Whether the world ends or not, at least you will be well-rested to deal with it.

During my classes, I am exposed to security professionals from a wide range of backgrounds, working in different industries and countries worldwide. The one thing they all have in common is that they do not have enough time, tools, and sometimes skills to do their job. Making the job you can't do right now any more urgent won't help. Work on tooling and resources, and develop a plan for applying best practices at a sustainable pace. Embrace AI tooling. It is immensely useful for automation. It is even more amazing at helping you get organized. Many partitioners are afraid that AI will do more harm than good, and they are not wrong. But use it where it helps you most. Are you great at writing little scripts but horrible at tracking and inventorying them? Give AI the job you suck at and develop a rapport with your tools. But embracing automation does include embracing AI tooling.

Finally, I got a lot of positive feedback on the final "conclusion" of yesterday's podcast, so I am going to link to it directly here:

[php2shell] https://isc.sans.edu/diary/33440

[infocon] https://isc.sans.edu/infocon.html

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|
![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-11-18%20at%202_47_04%E2%80%AFPM.png)