---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-10-02T01:12:40.822880+00:00'
exported_at: '2026-10-02T01:12:43.807359+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
source_url: https://www.niemanlab.org/2026/09/two-years-ago-meta-killed-crowdtangle-can-a-new-ai-tool-fill-the-void
structured_data:
  about: []
  author: ''
  description: Arbiter uses large language models and AI agents to help journalists
    see the next harmful narrative on social media before it peaks.
  headline: Two years ago, Meta killed CrowdTangle. Can a new AI tool fill the void?
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/09/two-years-ago-meta-killed-crowdtangle-can-a-new-ai-tool-fill-the-void
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Two years ago, Meta killed CrowdTangle. Can a new AI tool fill the void?
updated_at: '2026-10-02T01:12:40.822880+00:00'
url_hash: fe03de616495e8ffcf80387340a8ffde84485925
---

In 2024, Meta
[shuttered CrowdTangle](https://www.niemanlab.org/2024/03/a-window-into-facebook-closes-as-meta-sets-a-date-to-shut-down-crowdtangle/)
, a tool used to track how content spread across Facebook and Instagram. The portal was an essential tool for journalists, fact-checkers, and researchers, who used it for more than a decade to monitor viral content — and the spread of misinformation.

CrowdTangle’s end came
[slowly](https://www.bloomberg.com/news/articles/2022-06-23/meta-pulls-support-for-tool-used-to-keep-misinformation-in-check)
. Meta disinvested in the tool over years by
[cutting funding](https://www.bloomberg.com/news/articles/2022-06-23/meta-pulls-support-for-tool-used-to-keep-misinformation-in-check)
,
[disbanding teams](https://www.wsj.com/tech/meta-to-replace-widely-used-data-tooland-largely-cut-off-reporter-access-43fc3f9d)
, and
[restricting users](https://knightcolumbia.org/content/researchers-nyu-knight-institute-condemn-facebooks-effort-to-squelch-independent-research-about-misinformation)
. When the company finally announced in March 2024 that CrowdTangle would cease operations in August, a petition signed by
[more than 100 social media watchdog groups and others](https://www.mozillafoundation.org/en/campaigns/open-letter-to-meta-support-crowdtangle-through-2024-and-maintain-crowdtangle-approach/)
warned that, as a result, “almost all outside efforts to identify and prevent political disinformation, incitements to violence, and online harassment of women and minorities will be silenced.”

Now, a new crop of AI-powered tools is trying to fill the void.

[Arbiter](https://arbiter.simppl.org/)

is one of the projects leading the way. The platform uses large language models (LLMs) and AI agents to pull posts from social media platforms and analyze them at scale. It collects data from social media APIs, academic data dumps, and third-party data scraping companies. The platform currently works across several social media platforms, including Facebook, Instagram, Twitter (X), YouTube, TikTok, Reddit, Bluesky, and 4chan.

At the beginning of this year, Arbiter began onboarding its first news organizations, which now include the German public broadcaster
[Deutsche Welle](https://www.dw.com/en/top-stories/s-9097)
(DW), the Argentine fact-checking organization
[Chequeado](https://chequeado.com/)
, and the Filipino news site
[Rappler](https://www.rappler.com/)
. Users from more than 100 organizations have registered. For journalists trying to report on the harmful content distributed by social media platforms, access to a robust tool built independently from those companies is essential.

“We need independent mechanisms because it’s often been the case that incentive structures have clashed, and then good work that was done got washed away,” said
[Swapneel Mehta](http://linkedin.com/in/swapneelm)
, the co-founder and president of SimPPL, the nonprofit behind the tool. “I want to build resilient mechanisms because the fact-checkers and journalists that we support can’t deal with their work being threatened…They have enough external challenges to their work.”

Prompt Arbiter with a question in plain language about a topic on social media and it will automatically identify keywords, label and cluster posts pushing specific narratives, extract claims, identify accounts pushing the same message across platforms, and output an AI-generated summary report. It can also produce reports on multiple platforms at once, tracking how narratives move across the internet.

One of Arbiter’s most novel features is its ability to map out trend lines for specific narratives, including when they first emerge and when they peak on specific platforms. The feature aims to help journalists see what false or misleading narrative might be on the horizon. It is one that Mehta says sets it apart from other “
[social listening](https://muckrack.com/blog/why-social-listening-matters-for-pr)
” tools on the market, many of which are built for the PR and marketing industries.

“Social listening systems tell you where conversations are happening as they blow up. [They] send you alerts,” explained Mehta. “The problem is, as journalists, you want to be ahead of the alert. You want to be the one providing the alert, not receiving the alert.” As he puts it, by that time “the harms are done.”

### How Arbiter sees what’s next

Arbiter is the flagship product from
[SimPPL](https://www.simppl.org/)
, a nonprofit that has spent years exploring how to bring AI into the work of reporters and researchers working on information integrity. Mehta co-founded the AI research lab in 2021 with
[Dhara Mungra](https://dharamungra.github.io/)
, another data scientist who now leads SimPPL’s product team.

Mehta’s past work includes developing a civic and health misinformation classifier system at Twitter, conducting research at Adobe and the University of Oxford, and coaching grantees of
[JournalismAI](https://www.journalismai.info/)
, a program out of the London School of Economics that supports AI projects in newsrooms around the world.

Arbiter is trying to solve a few problems that journalists and fact-checkers frequently face on social media. One is the poor quality of search results on platforms. “You really want a contextual layer on top. [For instance,] if I’m searching for climate skepticism, it’s not going to literally search for the word skeptic in all the posts,” Mehta told me.

Another challenge is making sense of the social media data that journalists can get their hands on. Simply plugging these data sets into commercial LLMs often returns few actionable insights. “Anyone who’s dealt with more than 100,000 pieces of data knows that throwing them at an LLM first blows up your credit card bill and then gives you garbage outputs that you can’t control,” he said.

To make sense of its data, Arbiter isn’t building on top of a single foundation model, but instead leaning on eight to ten different AI models within its stack. “From encoding your queries, to figuring out the right posts to retrieve, identifying coordinated networks within these posts, semantic similarity, network mapping, all use different [models],” said Mehta. Some of these layers are model-agnostic, and Arbiter allows newsrooms to select their preferred LLM provider.

![](https://www.niemanlab.org/images/Arbiter-Screenshot-Nepa.jpg)

One of the first newsrooms to test Arbiter was
[Nest Center](https://www.nestmongolia.org/)
, a media NGO based in Ulaanbaatar, Mongolia. Among its initiatives is the fact-checking site and Facebook page, the
[Mongolian Fact-Checking Center (MFCC)](https://mfcc.mn/)
. In recent years, Nest’s fact-checkers have reported on coordinated disinformation campaigns from Russia and China, Mongolia’s neighbors to the north and south.

“We were dependent on CrowdTangle, and then Meta gave us the Meta Content Library,” said
[Duuya Baatar](https://www.linkedin.com/in/duuyabaatar/)
, the cofounder and chairperson of Nest Center, referencing Meta’s own replacement tool for CrowdTangle. Released in November 2023, the Meta Content Library (MCL) has been
[criticized](https://www.niemanlab.org/2024/03/over-100-watchdog-groups-sign-letter-demanding-meta-keep-crowdtangle-running/)
for restricting journalists’ access and removing the automated insights and sophisticated search features found in CrowdTangle. (Nest has MCL access as a member of Meta’s third-party fact-checking program, the U.S. version of which was
[shuttered in early 2025](https://www.niemanlab.org/2025/01/a-hard-hit-for-the-fact-checking-community-and-journalism-meta-eliminates-fact-checking-in-the-u-s/)
.)

“If you’re looking at a specific post, and if you want to look at a specific narrative, then MCL is okay. If you want to analyze how the information ecosystem is changing, then MCL is nowhere near CrowdTangle,” she said.

That’s the need that Arbiter has been meeting in Nest’s early testing. Soon after the newsroom received access, Baatar entered a prompt about a
[recent Mongolian Supreme Court ruling](https://www.ifj.org/es/sala-de-prensa/blog/detalle/category/press-freedom/article/ifjblog-the-case-that-reached-the-courts-and-won)
. The court had found that a criminal code outlawing the dissemination of “false information,” which had long been used to harass and intimidate journalists, was unconstitutional. The parliament was then tasked with drafting a replacement to the code.

Arbiter’s review of Facebook flagged some surprising commentary posted by several smaller accounts. Instead of focusing on “false information,” these accounts said Parliament’s replacement code would focus on “libel” and “defamation.” That, Baatar knew, would bolster the government’s ability to
[suppress press freedom](https://www.article19.org/resources/mongolia-criminalization-of-defamation-is-another-disturbing-attack-on-media-freedom-threatening-anti-corruption-efforts/)
in Mongolia.

“It was only my first use of Arbiter, and I was thinking that’s strange. I mean, as if that’s gonna happen,” Baatar told me. But weeks later, the
[Mongolian parliament announced a working group](https://arbiter.simppl.org/reports/nest-mongolia-article-13-14)
focused on folding libel and defamation into the criminal code.

Though Baatar had dismissed the early warning signs from Arbiter at the time, she said it bolstered her trust in the product. Now, three Nest Center staffers have full access to Arbiter and use it to monitor content in Mongolian on Facebook. (One of Baatar’s first notes to the Arbiter team was to improve its Mongolian capabilities, and they’ve gotten much better since January, she told me.)

“It helps us see certain narratives that are not popular now, but may become popular later,” she said.

![](https://www.niemanlab.org/images/Arbiter-Network-Mapping-Nepal.jpg)

Currently, all the newsrooms trialing Arbiter are using it for free. That accessibility has been key for the Nest Center, which can’t afford alternatives like
[Meltwater](https://www.meltwater.com/en)
and other
[AI-powered social listening tools](https://www.cision.com/)
that weren’t built primarily for journalists. Arbiter is still exploring revenue streams beyond newsroom subscriptions, since Mehta says he’s conscious that many of the news organizations that could use the tool are cash-strapped.

Despite these advantages, though, Baatar doesn’t consider Arbiter a full replacement for CrowdTangle. “The only concern that I hear from my team is the volume of what it can actually get from sources,” said Baatar. While MCL is better for monitoring specific posters and specific posts because of the volume of content you can access through Meta directly, Arbiter is stronger at trend lines and emerging narratives. “MCL plus Arbiter is coming close to Crowdtangle.”

### Finding the data workarounds

Arbiter went through months-long review processes to gain access to the APIs of major platforms, including Facebook and Instagram. Still, the tool is subject to Meta’s strict limitations on its API usage, most importantly rate-limiting: Using the API alone, Arbiter can only access so many posts at a time.

To build out its access, Mehta said he’s been working with third-party data providers that have vendor agreements with platforms, identifying carve-outs to collect public data without violating terms of service, and leaning on data donations from academics and civil society organizations. That last approach, he says, is inspired by the work many disinformation researchers have done
[on WhatsApp](https://journals.sagepub.com/doi/10.1177/20501579251326809)
, using data donations to access posts on the otherwise encrypted messaging app.

In the long term, Mehta says he doesn’t see Arbiter as adversarial to social media giants and wants to continue working with Meta and other platforms through their APIs as long as they are willing. But he knows he can’t count on that access.

“Often these processes start off when you’re a small organization and they approve you because you don’t pose any kind of concern for management,” he said. “But as you grow, the kind of work you do changes.”

Disinformation researchers have been the target of major lawsuits in recent years for terms of service violations. In 2023,
[Elon Musk’s X sued the Center for Countering Digital Hate (CCDH)](https://www.wired.com/story/twitter-x-ccdh-lawsuit-data-crackdown/)
for allegedly “scraping” the platform and improperly using a third-party social listening tool called
[Brandwatch](https://www.brandwatch.com/)
. The case was
[later dismissed](https://knightcolumbia.org/content/federal-judge-dismisses-elon-musks-x-corps-lawsuit-against-nonprofit-researchers)
. But Arbiter has still been working with a team of lawyers to review its processes and find any legal vulnerabilities in its current API workarounds.

“The last two or three years have been focused on figuring out the legal ways to activate the work that we’re doing,” Mehta said.

When it comes to CrowdTangle itself, Mehta says his goals for Arbiter go beyond simply servicing the newsrooms that used to rely on it. The tool’s ability to conduct analysis across platforms, not just Meta-owned ones, is one of its strongest features. Identifying a claim emerging across YouTube and X and Facebook, all at once, was something CrowdTangle could never do.

Still, the service’s shuttering loomed large in our conversations. “CrowdTangle is not a service that was mandated or regulated to continue being offered at any point. Platforms could decide that this was not a net positive and stop offering it,” said Mehta. If platforms will not take on this responsibility, he says someone else should be able to. “These are public conversations, and collecting public conversations in the public interest should not be illegal.”

Illustration of door opening by

[Yalcinsonat](https://stock.adobe.com/images/half-open-secret-door-new-opportunities-concept-vector-fear-of-the-unknown-step-inside-the-future/462387220)

from Adobe Stock. Screenshots of Arbiter’s narrative monitoring and network mapping claims about the 2026 Nepal floods courtesy of SimPPL.