---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-26T03:03:04.954128+00:00'
exported_at: '2026-09-26T03:03:06.290337+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
source_url: https://www.niemanlab.org/2026/08/japanese-publishers-are-fighting-imposter-news-sites-with-a-cryptographic-signature
structured_data:
  about: []
  author: ''
  description: The Yomiuri Shimbun, The Asahi Shimbun, and NHK have all signed onto
    the Originator Profile standard.
  headline: Japanese publishers are fighting imposter news sites with a cryptographic
    signature
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/08/japanese-publishers-are-fighting-imposter-news-sites-with-a-cryptographic-signature
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Japanese publishers are fighting imposter news sites with a cryptographic signature
updated_at: '2026-09-26T03:03:04.954128+00:00'
url_hash: 24876af6f014105e29a24d170593d2616c473e39
---

On January 1, 2024, a 7.5 magnitude earthquake struck Japan’s Noto Peninsula, killing more than 700 people. In the days that followed,
[AI-generated images](https://www.nippon.com/en/in-depth/d00987/)
of the wreckage circulated widely and
[fake philanthropic websites](https://www.scmp.com/news/hong-kong/health-environment/article/3363405/typhoon-dolphin-grounds-hong-kong-flights-disrupts-trips-and-business-japan)
scammed people out of donations.
[False claims](https://web.archive.org/web/20240203134123/https://www3.nhk.or.jp/nhkworld/en/news/20240202_19/)
that people were trapped under rubble
[diverted rescue efforts](https://www.nippon.com/en/japan-data/h02108/)
away from the places that needed them most. An unproven
[conspiracy theory](https://www.asahi.com/ajw/articles/15102962)
that the quake was “artificial” — including posts saying it was a man-made attack by North Korea — started trending on social media.

Natural disasters have long been flashpoints for disinformation in Japan. Similar

[falsehoods surfaced](https://www.japantimes.co.jp/news/2026/08/04/japan/society/kumamoto-earthquake-misinformation/)

online after a major earthquake hit Kumamoto Prefecture last month. But the 2024 Noto earthquake was a call to action for a coalition of Japanese news publishers, advertisers, and technology companies that was already pushing for better tools to fight misinformation.

Their solution: a new web standard called
[Originator Profile](https://originator-profile.org/en-US/)
(OP), which helps ordinary users verify who published or created a website.

OP uses cryptographic digital signature technology to create tamper-proof credentials for websites. Each ID card confirms who published the content, whether professional organizations vouch for that publisher, and information about the publisher’s editorial and ethical standards. The exact user interface is not finalized, but a
[new browser extension](https://originator-profile.org/en-US/news/aeqeioa7p8zl/)
released last month displays the information in a pop-up sidebar.

OP isn’t meant to judge whether all of the content on a website is
*true*
. It doesn’t authenticate specific photographs or video clips. Instead, it authenticates the site itself — for example, confirming that a news article is genuinely coming from the news organization it claims to be.

“We aren’t trying to dictate whether the information is accurate or not. It’s all about provenance: Where did this information originate?” said
[Makoto Yoshiike](http://linkedin.com/in/makoto-yoshiike-ba771240?originalSubdomain=jp)
, deputy secretary general of the Originator Profile Collaborative Innovation Partnership (OP-CIP), the group advocating for the standard’s adoption.

OP is far from the first attempt at building new provenance tools in an information ecosystem flooded with
[AI slop](https://www.niemanlab.org/2025/10/ai-generated-news-sites-spout-viral-slop-from-forgotten-urls/)
,
[deepfake scammers](https://www.niemanlab.org/2025/10/scammers-are-using-video-deepfakes-of-journalists-to-peddle-products-online/)
, and
[“LLM poisoning” campaigns](https://www.niemanlab.org/2026/06/at-globalfact-fact-checkers-reckon-with-declining-grant-funding-and-ai-generated-disinfo-on-the-rise/)
. Watermarking tools like
[Google’s](https://www.washingtonpost.com/technology/2023/08/29/google-wants-watermark-ai-generated-images-stop-deepfakes/)
SynthID and cryptographically signed metadata like the
[C2PA standard](https://www.niemanlab.org/2021/11/adobe-and-news-orgs-are-working-on-a-new-tool-that-could-identify-a-photos-origin-and-combat-misinformation/)
aim to
[tackle similar problems](https://www.niemanlab.org/2026/07/ai-authentication-tools-are-built-without-proper-journalist-input-new-report-finds/)
, but so far have mostly focused on addressing the rise of AI-generated imagery and audio.

“OP works within the HTML — it’s focused on the web page itself,” said Yoshiike. “We don’t want a whitelist for good media, separated from bad media. We just want to say it actually came from the authenticated sender of information.”

The idea for OP dates back to 2021, when it grew out of a project at Dentsu, the largest advertising and public relations firm in Japan. Even before the release of commercial AI image generators, the advertising giant struggled with malicious digital ads and scammers profiting from them. The company set out to find a way to authenticate an advertiser’s information as an ad passes through the programmatic ecosystem.

To develop the technical specs for OP, Dentsu partnered with

[Jun Murai](https://www.internethalloffame.org/inductee/jun-murai/)

, a professor at Keio University who is often credited as a founding father of the Japanese internet. He developed the web standards that allow Japanese language characters to travel through email and internet messages, among other innovations.

Next, Dentsu got news publishers on board. The largest daily newspaper in Japan, The Yomiuri Shimbun, was a founding member of OP-CIP. From the news industry’s perspective, there was a clear need to authenticate webpages that might be used as sources, but also a need to protect their brands, at a time when generative AI tools have made it easier than ever to spoof legitimate news publications.

Yomiuri itself has faced this challenge. “I actually caught one red-handed on Facebook,” said Yoshiike, noting that he’s been served fake versions of The Yomiuri Shimbun on his feed. “It’s still happening, individuals mimicking our article pages and luring users to fraudulent websites. Most of it is junk, but it happens every day.”

![Yomiuri Shimbun building](https://www.niemanlab.org/images/AdobeStock_400300688_Editorial_Use_Only-1.jpg)

In December 2022,
[OP-CIP was officially established](https://originator-profile.org/en-US/news/press-release_20230117/)
with nearly a dozen news publishers on board. The Noto earthquake in 2024, however, expanded the project’s scope. The Japanese national government, realizing the value of the authentication tool for government websites that deliver messages in crisis situations, began
[funding OP-CIP](https://japannews.yomiuri.co.jp/society/general-news/20240829-207832/)
, and the organization started welcoming local governments into its ranks.

“When disasters strike, there is no end to fraudulent information being disseminated, individuals impersonating local governments or public utilities,” said
[Tatsuya Kurosaka](http://linkedin.com/in/tekusuke?originalSubdomain=jp)
, a project associate professor at Keio University and secretary general of OP-CIP. “That’s why we are thinking not only about the media context, but also public information more generally as well.”

Today, OP-CIP has built an impressive coalition of supporters. Among them are dozens of members of the Japanese Newspaper Publishers and Editors Association (

*Nihon Shinbun Kyokai*

). Major television networks, including NHK, the national public broadcaster, have also signed on. Members of the group from the tech sector include LINE-Yahoo (LY), which operates the most popular news aggregator in Japan and the messaging app LINE, which is used by

[more than 80% of the country](https://www.businessofapps.com/data/line-statistics/)

.

While those members publicly signed on to support OP, so far only a handful have fully integrated the technology into their own operations. The Yomiuri Shimbun and The Asahi Shimbun, the two largest newspapers in Japan by circulation, have integrated OP into their content management systems, according to Yoshiike, who also works at The Yomiuri Shimbun as the senior deputy chief officer for the president’s office. Tottori Prefecture in Western Japan has also launched OP on its prefectural government websites. Dentsu is currently rolling out the technology for its ad buys, with hopes that it can help counter the recent sharp
[rise in ad fraud and AI scam ads across the country](https://www.techtimes.com/articles/323490/20260807/meta-had-six-weeks-stop-japans-804m-scam-crisis-it-chose-revenue.htm)
.

Yoshiike says that by early 2027 OP-CIP plans to have 50 major organizations operating with the OP standard in place.

Ultimately, though, the group sees Japan as its testing ground. In the years to come, they hope to export the technology and make it an international web standard, with the participation of international news publishers and global technology companies. The
[World Wide Web Consortium](https://www.w3.org/)
(W3C), which is responsible for existing global internet standards like HTML and CSS, has already created its own OP working group to explore this possibility.

“We’re pushing full speed with implementation in Japanese society to show the W3C community how it works,” Yoshiike said.

Last month, OP-CIP released its first public tool to retrieve and visualize the cryptographically signed profiles on websites. The browser extension, called OP Inspector, is available on
[Chrome](https://chromewebstore.google.com/detail/op-inspector/namnjenlimojacngjhddjdjpakfaepeb)
and
[Firefox](https://addons.mozilla.org/en-US/firefox/addon/op-inspector/)
. When a user lands on a Yomiuri Shimbun article, for example, the extension activates a pop-up sidebar that shows a badge verifying that Yomiuri Shimbun is the organization operating the webpage and links to the publication’s
[editorial standards policy](https://info.yomiuri.co.jp/rinen/)
and
[privacy policies](https://info.yomiuri.co.jp/privacypolicy/about.html)
.

![](https://www.niemanlab.org/images/Screenshot-2026-08-12-at-2.21.32-PM.png)

Right now, the extension is only meant for developers working with the OP standard, though there are plans to fine-tune and release an extension for general internet users down the line. Eventually, OP-CIP hopes it can abandon the need for extensions and apps altogether. One current idea, if the standard is taken up by W3C, is for a badge to appear within a browser URL bar so that users can click it and access the OP without ever downloading an extension.

“My mother is 88 years old. I’m designing OP technology to be simple enough for even my mom to use,” said Kurosaka. “No specific skills are required.”

The project faces clear hurdles as it moves into the next stages of development. One will be adoption by social media platforms that are major vectors for disinformation on the internet. Currently, OP can’t appear on individual social media posts like article links shared on Facebook. It’s only accessible when a user navigates to that article’s webpage, limiting its impact on social media-fueled disinformation.

“I think it is a huge open question,” said Yoshiike. “Our technology side hasn’t caught up with the current social media standards. OP works within the HTML, so it’s not used in the application itself.”

Fully realizing OP’s potential will also require earning the support of tech giants like Google and Apple that hold tremendous influence within W3C. As search increasingly becomes a direct source of news for users through products like AI Overviews and AI Mode, their participation becomes even more essential.

“The last thing standing between us and the users is big tech companies,” said Yoshiike. “We know that it’s not going to come easy.”

Screenshot of a site impersonating The Yomiuri Shimbun and a screenshot of the real Yomiuri Shimbun website courtesy of OP-CIP. Photo of The Yomiuri Shimbun building by JHVEPhoto licensed via Adobe Stock. Screenshot of an article on The Yomiuri Shimbun site with the OP Inspector browser extension activated.