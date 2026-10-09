---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-10-09T00:56:21.341233+00:00'
exported_at: '2026-10-09T00:56:28.352303+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
language: en
source_url: https://www.niemanlab.org/2026/10/uber-agents-undercover-ai-personas-and-other-ways-newsrooms-are-using-ai-in-investigations
structured_data:
  about: []
  author: ''
  description: Hacks/Hackers and The New York Times hosted more than 100 journalists
    at the AI x Investigative Journalism Forum.
  headline: “Uber agents,” undercover AI personas, and other ways newsrooms are using
    AI in investigations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/10/uber-agents-undercover-ai-personas-and-other-ways-newsrooms-are-using-ai-in-investigations
  publisher:
    logo: /favicon.ico
    name: GTCode
title: “Uber agents,” undercover AI personas, and other ways newsrooms are using AI
  in investigations
updated_at: '2026-10-09T00:56:21.341233+00:00'
url_hash: 3f8fa372e5f28e3659de2b09868d4925972ffd86
---

Late last month, about 150 journalists, researchers, and technologists gathered on the 15th floor of The New York Times Building for a
[forum on how AI is changing investigative journalism](https://luma.com/ai-investigative-journalism-forum-2026)
.

Just outside the event space was a hallway commemorating the paper’s more than 140 Pulitzer Prize winners, dating back to 1918. One photograph had yet to be hung: a portrait of this year’s winners of the Pulitzer Prize for Investigative Reporting. For one of
[their winning stories](https://www.nytimes.com/2025/12/14/us/politics/sec-crypto-firms-trump-investigation.html)
, a team of Times reporters conducted an audit of the SEC’s crypto lawsuits to show weakening enforcement under the second Trump administration. The reporting
[was assisted](https://www.niemanlab.org/2026/08/a-record-breaking-eight-pulitzer-awardees-disclosed-ai-use-this-year/)
by large language models (LLMs).

The Times isn’t the only major newsroom using AI tools in major investigations. A
[record-breaking eight Pulitzer awardees](https://www.niemanlab.org/2026/08/a-record-breaking-eight-pulitzer-awardees-disclosed-ai-use-this-year/)
this year disclosed AI use to the judges. They used LLMs to organize, summarize, analyze, and translate large document dumps.

“At the Times we’re not doing ‘robots tell the news,’ but a number of different [kinds of AI adoption] that can make the work we do more efficient, more effective, and able to do things that otherwise would be very, very hard to do,” said
[Juliana Castro Varón](https://www.linkedin.com/in/julianacastro/)
, the Times’ senior design editor of AI initiatives, in a keynote. Often, “the most useful part [of AI] is the fact that it understands images and understands text, more than creating [them].”

The Times’ AI Initiatives team, a group of nine journalists and technologists leading AI strategy and deployment in the newsroom, co-hosted the event with

[Hacks/Hackers](https://www.hackshackers.com/)

, a nonprofit that brings journalists and technologists together to discuss media innovation. (Hacks/Hackers

[hosted a summit on AI and journalism](https://www.hackshackers.com/announcing-the-hacks-hackers-2026-ai-x-journalism-summit/)

in Baltimore for the past two years.)

The day was packed with workshops, panels, and presentations about the promise of AI for investigative journalism, led by the technology’s most vocal advocates in newsrooms. But the limitations of these tools — including persistent hallucination problems in LLMs, concerns about vibe-coding errors, and budget constraints as AI token costs pile up — were also a common theme.

“AI is very good at generating leads, but much less capable of establishing publishable evidence,” said
[Afrooz Mosallaei](http://linkedin.com/in/afrooz-mosallaei)
, a research associate at the Center for News, Technology &amp; Innovation, during a talk about the nonprofit’s
[recent report](https://cnti.org/briefing/ai-applications-in-investigative-journalism/)
on the topic. “A lot of tasks in an investigation — including verification, source development, textual understanding, and editorial judgment — remain fundamentally human responsibilities.”

### From search tool to “uber agent”

The release of the Epstein Files was a
[huge moment for AI in investigative journalism](https://www.niemanlab.org/2026/03/ai-powered-search-is-fueling-a-wave-of-epstein-files-transparency-projects/)
. Journalists across the U.S. woke up on January 30, 2026 to a Department of Justice drop of over 3.5 million pages of documents and tens of thousands of images and videos.

[Duy Nguyen](https://www.linkedin.com/in/duy-nguyen-a5bb12150)
, who leads AI science research at the Times, noted that the PDFs in the Epstein Files would stack as high as the Empire State Building if they were printed out, and would take 11 years for one reporter to read. (Epstein sent an average of 65 emails every day for a decade.) It would take a reporter a month to listen to and watch all the audio and video clips.

Many newsrooms decided that the early organization and research into these documents was a task primed for AI technologies. Engineers from the Associated Press, NPR, and the Times led a session on how they built tools to help reporters sift through the documents.

NPR built an internal search tool that let reporters across the newsroom find the documents relevant to their beats, said
[Kriti Singh](https://www.linkedin.com/in/kritisinghh/)
, a design technologist at NPR’s AI Labs. Her team classified documents by type (email, legal filing, flight log, witness list), grouped them by location (city, county, hotel, university), and extracted entities (making sure, for instance, that a search for “Prince Andrew” also surfaced files that mentioned “the Duke of York”).

The Times AI Initiatives team built the Epstein Files Engine, an internal chatbot to help reporters comb through the files. “There are so many sorts of threads that you can pull from such a big corpus, and the chat interface really allows [reporters] to dive deep,” said Nguyen. The engine’s interface was built with
[LibreChat](https://www.librechat.ai/)
, a free, open-source, self-hosted AI chat platform.

A few real prompts from reporters:

&gt; “Look at our Epstein coverage over the past three months and cross-reference with names of people most mentioned in the documents. Give me a subset of names we haven’t covered as often.”

&gt; “Find me Kathryn Ruemmler’s email where she said she is missing her ring in Epstein’s apartment.”

&gt; “Construct a timeline of Epstein’s death, give me a table that I can copy into a spreadsheet. Be very detailed. Surface witnesses, links and quotes where available.”

Ultimately, more than 100 Times journalists posed more than 5,000 questions to the engine, and it contributed to at least 20 published stories. “This was a signifier of just how powerful an agentic chat interface could be in a newsroom,” said Nguyen. (His team recently published an
[academic article](https://arxiv.org/abs/2609.30611)
detailing the tool’s development.)

Since then, the team has created other agentic search tools. Ahead of the Times’
[175th anniversary series](https://www.nytimes.com/interactive/2026/us/175-nyt-anniversary.html)
, they built “Morgue Bot,” which made it easier for reporters to dive into the Times’ archive.

Now, the team is taking chatbots to the newsroom at large. In July, they launched News Agent, which they’re calling the “front door to AI at The New York Times.” The general-purpose internal chatbot plugs into not just the Times’ archives and the Epstein Files, but other databases, internal documents like the Times’ style guide, and the web. News Agent also allows any Times reporter to build their own custom agentic search tool, tailored to a specific project.

“It’s an omnibus agent or an uber agent that basically acts as a drop-in replacement for chatbots like Gemini or ChatGPT,” said Nguyen, “but specifically geared to help reporters and editors within the Times newsroom.”

The team’s copy for the tool reads, “Ask anything.”

### Automating the source spreadsheet

Any beat reporter will tell you they have a love-hate relationship with their source spreadsheet — that Google Sheet or Excel file that lists the name, title, email address, and phone number of every source they’ve spoken to over the years. Such documents are perfect for remembering the name of a researcher you spoke to five years ago without having to dig through your inbox. But they’re tedious to update.

“It can become a dead document that never gets checked,” said
[J.D. Capelouto](http://linkedin.com/in/j-d-capelouto-49b752ab)
, a technology reporter and the newly named AI lead at Semafor.

To try to keep his own source spreadsheet alive and up-to-date, Capelouto made a tool in

[Google Apps Script](https://developers.google.com/apps-script)

, a platform that lets users build small “assistants” within Google Workspace. When he emails someone for the first time, he adds an inbox tag called “New Source.” At the end of each day, the script scans his inbox for any tagged emails, then populates a Google Sheet with all the relevant information about them, including adding a category tag and generating a logline summarizing what they discussed. (There are obvious risks in handling anonymous or sensitive sourcing, but Capelouto said the tool creates minimal new security vulnerabilities since it stays within Google’s ecosystem.)

From there, Capelouto started building on top of the spreadsheet. A pop-up sidebar lets him ask who might be a good person to speak with for a story; the tool combs through the spreadsheet and suggests names.

Every morning, a script also scans the web for the news of the day on Capelouto’s beat, cross-references those headlines with the source spreadsheet, and sends him an email suggesting a topic to cover and a source to contact. Some of the suggestions aren’t useful, Capelouto admitted, but others have actually prompted him to reach out to someone he’d forgotten about.

“A lot of times in journalism, some of the source management work is just saying, ‘Hey, how’s it going?” he said. “This can begin a conversation, then you get a scoop from that.”

![](https://www.niemanlab.org/images/NYT-AI-x-Journalism-3.jpg)

Philip Bump of Hearst Connecticut Media Group presents at the AI x Investigative Journalism Forum in The New York Times Building on September 25, 2026. (Photo courtesy of Hacks/Hackers)

### Undercover AI personas

Most conversations about AI-generated imagery in investigative journalism
[revolve around verification](https://www.cjr.org/feature/the-future-of-visual-investigations-if-we-cant-trust-our-eyes.php)
. As AI-altered images and deepfakes flood the internet, how do reporters verify the images they come across online, or those sent to them by whistleblowers?

The forum didn’t tackle these questions head on, but one presentation highlighted the ways that AI image generators can be harnessed to protect the identity of journalists.

Last year, The Markup co-published
[an investigation into Match Group](https://themarkup.org/investigations/2025/02/13/dating-app-tinder-hinge-cover-up)
, the dating app giant that owns Tinder, Hinge, and OkCupid. The
[nonprofit tech publication owned by CalMatters](https://www.niemanlab.org/2024/04/seeking-innovative-stable-and-interested-how-the-markup-and-calmatters-matched-up/)
found that despite an official policy of banning users who are reported for assault, the company failed to keep them off their platforms and hid the scale of the problem from the public.

In one case, a Denver cardiologist who was repeatedly accused of drugging and sexually assaulting women he met on Hinge remained active on the platform for three years, even after two different women reported his abuse. (In 2024, he was
[convicted](https://www.cbsnews.com/colorado/news/stephen-matthews-sentenced-158-years-drugging-sexually-assaulting-women-met-dating-apps-cardiologist/)
of crimes against 11 women and sentenced to 158 years to life in prison.)

The Markup’s reporters decided to go undercover. They posed as users on Match-owned apps, then reported themselves from other accounts to see how easy it was to stay on the platform.

There was only one problem. “We came across this ethical dilemma: Am I gonna ask my staff or myself to take a photo and put it on the Tinder account?” recalled
[Sisi Wei](https://www.linkedin.com/in/sisiwei)
, the chief impact officer at The Markup and CalMatters.

Even stock photos would subject real people, who had not consented to their likeness being used in the investigation, to reputational harm. Instead, The Markup turned to AI image generators. They found a company that generates visual test imagery and had developed a way to train models without relying too heavily on images of real people.

“They look like real human beings, but if you turn on a light switch, you can tell that AI is here,” said Wei. But they were still “real” enough to bypass the dating apps’ content moderation filters. With these new AI headshots and personas in hand, the reporters went back on the apps and created 50 different accounts.

Ultimately, their investigation found that even after one of these personas was reported and kicked off a Match-owned dating app, they could get back onto the platforms without changing identifying information. Earlier this year, the 18-month long investigation won a
[SABEW Award for best technology business reporting](https://sabew.org/2026/03/2025-best-in-business-honorees-judging-comments/)
.

“AI became a way for us to protect our own staff from needing to be a part of the experiment,” said Wei.