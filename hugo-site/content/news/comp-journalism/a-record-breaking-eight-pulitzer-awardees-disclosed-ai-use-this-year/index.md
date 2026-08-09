---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-08-09T09:51:03.058972+00:00'
exported_at: '2026-08-09T09:51:08.135572+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
source_url: https://www.niemanlab.org/2026/08/a-record-breaking-eight-pulitzer-awardees-disclosed-ai-use-this-year
structured_data:
  about: []
  author: ''
  description: Five winners and three finalists detailed their AI adoption to the
    judging committee.
  headline: A record-breaking eight Pulitzer awardees disclosed AI use this year
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/08/a-record-breaking-eight-pulitzer-awardees-disclosed-ai-use-this-year
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A record-breaking eight Pulitzer awardees disclosed AI use this year
updated_at: '2026-08-09T09:51:03.058972+00:00'
url_hash: 50a9fb60c0589582781ddc4a29d7dadbf620b555
---

A translation of a
[mass shooter’s cryptic journal](https://www.startribune.com/no-going-back-minneapolis-church-shooter-turned-violent-after-religious-but-sometimes-turbulent-upbringing/601464119)
in the days after an attack. A
[public records review](https://www.wsj.com/us-news/officials-pushed-for-better-warning-system-years-before-devastating-texas-floods-0143b5f1)
that revealed failures to install flood warning systems in Central Texas. An
[exposé](https://apnews.com/article/chinese-surveillance-silicon-valley-uyghurs-tech-xinjiang-8e000601dadb6aea230f18170ed54e88)
of American technology companies’ complicity in building the Chinese surveillance state. An
[audit of the SEC’s crypto lawsuits](https://www.nytimes.com/2025/12/14/us/politics/sec-crypto-firms-trump-investigation.html)
that showed weakening enforcement under the second Trump administration.

On May 4, the Pulitzer Prizes recognized these stories among
[the winners and finalists](https://www.pulitzer.org/prize-winners-by-year/2025)
across 15 journalism categories. The reporters behind each of these stories also disclosed using AI to the judging committee. Ultimately, five award winners and three finalists this year disclosed AI adoption in their submissions — the most since the disclosure requirement was added in 2024.

For

[the past](https://www.niemanlab.org/2025/05/how-this-years-pulitzer-awardees-used-ai-in-their-reporting/)
[two years](https://www.niemanlab.org/2024/05/for-the-first-time-two-pulitzer-winners-disclosed-using-ai-in-their-reporting/)

, I’ve spoken to Pulitzer-recognized reporters about how they used AI in their reporting. Both years, generative AI took a back seat to more conventional machine learning technologies, like using embedding models to produce complex data visualizations and pattern recognition models to analyze satellite imagery in conflict zones. This year, though, generative AI tools and commercial large language models (LLMs) were more commonly used, largely to speed up the process of combing through document dumps.

“To state the obvious, perhaps, AI is here to stay,”
[Marjorie Miller](https://www.pulitzer.org/news/journalist-marjorie-miller-elected-administrator-pulitzer-prizes)
, the administrator of the Pulitzer Prizes, told me. “The industry [used to be] far more apprehensive about AI tools than it is today, with a clearer understanding now of what uses might be appropriate — data collection and analysis, for example — and when it might not, such as in writing and editing stories in any format that might be considered for a Pulitzer Prize.”

Miller cautioned that as AI evolves, reporters will need to “ensure and reassure” the Pulitzers that submissions are ultimately produced by human beings, even when AI is used as an assistive tool. Given recent
[controversies](https://www.theatlantic.com/technology/2026/07/commonwealth-prize-ai-writing-jamir-nazir/687806/)
over AI-generated text allegedly appearing in prize-winning literary works, Miller also said next year the Pulitzers will include an AI disclosure question in their book entry forms.

### Finding the needle in a stack of public records

In the days after deadly floods hit Kerr County, Texas in the summer of 2025, reporters at The Wall Street Journal had a clear reporting question: Had this area ever dealt with dangerous flooding before?

To find an answer, the reporters turned to public records. The team built a custom scraper that pulled every public meeting minute, agenda, and transcript from the Kerr County website.

Journalists are trained to find the needle in a haystack, but doing so on a breaking news timeline can be challenging. To speed up the document review, the reporters leaned on a pre-built internal tool called WSJPT (a play on ChatGPT). The tool standardizes basic LLM requests across reporting projects, including prompts for summarization, classification, and image description. In this case, the reporters used the tool to summarize every page of every document scraped from the county portal.

The team combed through these summaries using a combination of LLMs and more old-school natural language processing (NLP) techniques (e.g.
[stemming, lemmatization](https://www.ibm.com/think/topics/stemming-lemmatization)
) to find sections that referenced past flooding events.

“We aren’t obviating the need for human investigation of a pile of documents — and I don’t think we would if we could,” said
[John West](https://www.linkedin.com/in/john-west-b3483466)
, a computational journalist at the Journal. “Instead, we’re trying to sort the pile so the most relevant stuff is right at the top.” West clarified that every section flagged as possibly relevant by these tools was read by a reporter, and then every document deemed relevant was read in full.

![](https://www.niemanlab.org/images/The-Wall-Street-Journal-Flood-Investigation-scaled.jpg)

Based on this analysis, the Journal identified former Sheriff Rusty Hierholzer, who had pushed county commissioners to install a stronger flood-warning system a decade ago. In 2016, Hierholzer called for the installation of outdoor sirens, recounting an experience flying in helicopters and “pulling kids out of trees here (in) our summer camps” when floods hit nearby Kendall County in 1987, killing 10 campers. Hierholzer’s recommendations were not implemented at the time, the Journal found.

The findings were foundational to

[one news story](https://www.wsj.com/us-news/officials-pushed-for-better-warning-system-years-before-devastating-texas-floods-0143b5f1)

and several follow-ups on the floods. The Pulitzers named the Journal’s overall coverage a

[finalist in the Breaking News category](https://www.pulitzer.org/finalists/staff-wall-street-journal-4)

. West says this playbook — using a “mix of off-the-shelf and custom software” to summarize and parse documents — was also central to the Journal’s reporting on the Epstein Files this year. That coverage was a

[finalist in the Public Service category](https://www.pulitzer.org/finalists/wall-street-journal-work-led-khadeeja-safdar-and-joe-palazzolo)

.

Like many of the investigations this year that disclosed AI adoption to the Pulitzer judges, no AI disclosure (such as a label, footnote, or accompanying methodology) appeared in the Journal’s own stories on the Central Texas floods.

“We did not disclose the use of AI. It functioned as a sophisticated way of searching through the documents, but we read the docs, and ran the findings down,” said West.

He contrasted that choice with a recent Journal investigation about toxic fume incidents on U.S. commercial aircraft. That story used LLMs to read more than one million FAA documents and to generate incident rates per airline and aircraft. For that story, which did disclose AI usage, West said he “got to write
[the longest methodology statement](https://www.wsj.com/business/airlines/how-the-journal-analyzed-more-than-one-million-faa-reports-7e7e043a)
I’ve ever written.”

### Translating on a breaking news deadline

On August 27, 2025, a 23-year-old woman killed two children and wounded 27 others during a mass shooting at the Annunciation Catholic Church in Minneapolis, Minnesota. The shooting rocked the local community, but in the hours that followed, there were few answers about the shooter’s motivations.

When news of the shooting first broke, reporters at The Minnesota Star Tribune gathered in a Slack channel to

[coordinate their coverage](https://www.poynter.org/reporting-editing/2025/minnesota-star-tribune-artificial-intelligence/)

. They identified the shooter’s YouTube account and videos showing her turning the pages of a journal written in a language the team didn’t recognize.

[Dana Chiueh](https://www.linkedin.com/in/danachiueh)
, an engineer in the Star Tribune’s AI Lab (now a fellow at ProPublica), took screenshots of the videos and entered them into an enterprise ChatGPT account. The chatbot recognized the text as
[Faux Cyrillic](https://en.wikipedia.org/wiki/Faux_Cyrillic)
, a variant of Russian typography that can be used to spell out English words.

“[Faux Cyrillic] is not a real language. It can be thought of more as a type of code that one might use if they were trying to conceal what they were writing,” said Chiueh, explaining that ChatGPT allowed them to quickly see if there was relevant background information buried in the code.

After hours of tedious manual screenshotting, Chiueh wrote a custom script to pull the screenshots from the YouTube videos automatically. Ultimately, ChatGPT was able to produce an initial translation pass on hundreds of journal pages, over 600,000 words.

“At first we were doing something really scrappy. That spirit of being able to quickly prototype and iterate is something that is really useful for a breaking news situation,” she said.

![](https://www.niemanlab.org/images/The-Minnesota-Star-Tribune-mass-shooting-journal-translation.jpg)

A team of journalists then put the translations into Google’s NotebookLM, a Gemini-powered notetaking tool they used to search for keywords and pull out themes. They found mentions of past jobs, relationships, and locations the shooter had visited, like pawn shops and shooting ranges — all information that informed the outlet’s shoe-leather reporting.

“We were very conscious that AI hallucinates, so we made sure that any quotes, context, and anecdotes were reviewed by a human translator,” said
[Tom Scheck](https://www.startribune.com/author/tom-scheck/601438086)
, investigations editor at the Star Tribune.

Rather than sending the entire AI-generated translation to a professional, reporters flagged important passages for review by two Russian language academics at the nearby St. Olaf College. For the most part, the AI-generated translations were correct, but the academics found a few errors, including a passage that misrepresented the shooter’s potential motivation.

If it weren’t for the help of AI translation, Scheck says the Tribune would probably have hired a translator to go through the documents from the beginning, slowing down their turnaround time. Instead, the triaged translations informed
[an initial story on the manifesto](https://www.startribune.com/manifesto-videos-from-minneapolis-suspect-praised-mass-killers-fixated-on-school-shootings/601462521)
the night of the attack and contributed significantly to a
[profile of the shooter](https://www.startribune.com/no-going-back-minneapolis-church-shooter-turned-violent-after-religious-but-sometimes-turbulent-upbringing/601464119)
published four days later. Both stories were a part of the coverage that won the Star Tribune a Pulitzer in the
[Breaking News category](https://www.pulitzer.org/winners/staff-minnesota-star-tribune)
.

“AI allowed us to take a first pass on the content and then prioritize what we [might] use,” he said. “We know we have to run the marathon, but AI helped us start at mile marker five instead of at the traditional starting line.”

### Making a trove of documents searchable

Over the past 25 years, the Chinese government has built up a sophisticated mass surveillance program. A series of investigations published by the Associated Press last year exposed just how many of the technologies fueling this surveillance apparatus were sold to China by American companies.

Reporters mapped the supply chains for state-of-the-art surveillance tools, tracking their development in Silicon Valley and deployment in China, implicating companies like Nvidia, Intel, IBM, Dell, HP, Cisco, Oracle and Microsoft. The reporting earned the AP a Pulitzer win in the
[International Reporting category](https://www.pulitzer.org/winners/dake-kang-garance-burke-byron-tau-aniruddha-ghosal-and-yael-grauer-contributor-associated)
.

![Associated Press Investigation into Chinese surveillance state header image.](https://www.niemanlab.org/images/Associated-Press-Investigation.jpg)

Key to these stories were tens of thousands of leaked emails and databases from a Chinese surveillance company, as well as thousands of government records and procurement documents (like vendor bids, signed contracts, and invoices). AI was essential to sifting through these documents and making them searchable, according to
[Garance Burke](https://www.linkedin.com/in/garanceburke/)
, a global investigative journalist at the AP who worked on the project. The AP used LLMs to identify specific company contracts, summarize government records, flag specific people or technologies for further investigation, and organize all the information collected into more easily managed databases.

[![](https://www.niemanlab.org/images/tansa-credit-1-315x177.jpg)](https://www.niemanlab.org/2026/06/tansa-is-pioneering-a-new-model-for-investigative-journalism-in-japan/?relatedstory)

In other words, AI was an assistant in the early reporting and research stages of the investigation, helping to make sense of a massive pile of documents. The team unearthed evidence that IBM had worked with the Chinese defense contractor Huadi to design a national fingerprint database, and evidence that Intel and Nvidia helped enable AI capabilities on surveillance cameras used in Xinjiang and Tibet. The documents also showed that HP sold the Chinese police “digital fencing” products, which have been used to track when Uyghurs and other surveilled populations try to travel outside their home towns and provinces,

[among many other findings](https://apnews.com/article/chinese-surveillance-silicon-valley-uyghurs-tech-xinjiang-a80904158b771a14d5a734947f28d71b)

.

“The AI tools helped reporters search and review large volumes of public records more efficiently, but they did not replace the reporting or verification process,” said Burke. “Reporters manually reviewed documents surfaced through AI, independently assessed the accuracy of AI-generated summaries, and did not quote from those summaries.”

### Using LLMs to double-check human work

Donald Trump is the self-declared “
[crypto president](https://www.reuters.com/world/us/trump-pitches-himself-crypto-president-san-francisco-tech-fundraiser-2024-06-07/)
” — an industry booster who
[earned over $1.4 billion](https://www.bbc.com/news/articles/cvgmv98ez3zo)
in personal crypto business dealings during his first year back in office. A team of reporters at The New York Times wondered if the administration’s pro-crypto stance had influenced the work of agencies that regulate the industry, namely the SEC.

To try to answer that question, the Times reviewed all of the SEC’s crypto-related enforcement actions dating back to 2017. The analysis surfaced a troubling trend. Since Trump took office again in 2025, the SEC had pulled back on more than 60% of its ongoing crypto cases, lessening penalties, freezing suits, and even dismissing cases entirely.

![The New York Times SEC Investigation header image.](https://www.niemanlab.org/images/The-New-York-Times-SEC-Investigation.jpg)

“It is unheard of for the agency to retreat from a swath of lawsuits against a single industry,” wrote the reporters in
[their investigation published last December](https://www.nytimes.com/2025/12/14/us/politics/sec-crypto-firms-trump-investigation.html)
. “Although the particulars of the crypto lawsuits differed, many of these firms had something in common: financial ties to Mr. Trump.”

The investigation is one of several stories that exposed Trump’s ongoing conflicts of interest with the crypto industry and earned the Times a
[Pulitzer win in the Investigative Reporting category](https://www.pulitzer.org/winners/staff-new-york-times-3)
.

Many of the Pulitzer awardees that used AI this year disclosed using LLMs to speed up and prioritize document review. The Times investigation stands apart. For their investigation, reporters downloaded more than 10,000 documents, including thousands of SEC news releases and over 700 federal court cases, according to Miller, the Pulitzers administrator. Reporters read and classified each of these documents manually over the course of several months. LLMs were only brought into the reporting process after this full human review was completed.

Reporters used OpenAI’s GPT-5 model to conduct a secondary review of the documents and check their work. They fed the model the documents from each of the lawsuits, as well as a detailed set of instructions on how to classify them. These classifications labeled “whether a case was crypto-related, whether it was inherited by the next administration and how liability was decided,” according to a

[methodology published by the reporting team](https://www.nytimes.com/2025/12/14/us/politics/times-sec-cryptocurrency-analysis.html)

.

The team compared the GPT-5 classifications with the ones assigned manually. When there were discrepancies, reporters went back and read the documents again to double-check their work. The Times declined to provide further details on this review process.

Hallucinations and other errors produced by LLMs are often cited as reasons not to use generative AI in investigative reporting. In this case, Times reporters turned the tables. They used LLMs as a tool to help keep human error in check.