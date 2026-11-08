---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-08T05:29:55.405839+00:00'
exported_at: '2026-11-08T05:29:56.383781+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/qa-hey-ai-who-should-i-vote-for-this-year-1030
structured_data:
  about: []
  author: ''
  description: The LLM Election Observatory is a dashboard built by MIT researchers
    that examines, in real-time, how popular AI chatbots are responding to questions
    about the 2026 midterm elections.
  headline: 'Q&A: Hey AI, who should I vote for this year?'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/qa-hey-ai-who-should-i-vote-for-this-year-1030
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Q&A: Hey AI, who should I vote for this year?'
updated_at: '2026-11-08T05:29:55.405839+00:00'
url_hash: 226d6d5c25cb9ac1ca62efc394810317f24f426c
---

MIT professors Adam Berinsky and Chara Podimata discuss a new project to track how AI chatbots are responding to questions about the 2026 U.S. midterm elections.

*People are peppering artificial intelligence chatbots everyday with questions, but when it comes to politics and the looming 2026 U.S. midterm elections, what role are AI platforms playing? Could an AI chatbot sway a voter to switch parties or re-examine their political beliefs?*

*MIT researchers have built a new dashboard, called the*
[*LLM Election Observatory*](https://www.llmelectionobservatory.org/)
*, to examine, in real-time, how popular AI chatbots are responding to questions about the 2026 midterm elections. The team behind the dashboard — led by*
[*Professor Adam Berinsky*](https://polisci.mit.edu/people/adam-berinsky)
*,*
[*Assistant Professor Chara Podimata*](https://mitsloan.mit.edu/faculty/directory/chara-podimata)
,
*and*
[*Professor Charles Stewart III*](https://polisci.mit.edu/people/charles-stewart-iii)
*— has extensive experience studying voting and election administration, AI and misinformation, and how AI systems are impacting human decision making. In an effort to better understand how AI is shaping the election, they designed the dashboard to simulate how individuals across the country communicate with chatbots.*

*The team tracks how different AI systems respond to the same fixed set of questions on a range of topics, including election certification, hot-button issues, result predictions, news coverage, and more. Every few days, the LLM Election Observatory team runs the questions through the chatbots again, monitoring how their responses vary as the election gets closer depending on user location, political party affiliation, identity and other factors. The goal of this work is not to merely understand how AI systems spread information, but also better comprehend how they are shaping political discourse and voter understanding of political issues across the country.*

MIT News
*chatted with Podimata, the Class of 1942 Career Development Professor, an assistant professor of operations research and statistics in the MIT Sloan School of Management, and a member of the Laboratory for Information and Decision Systems; and Berinsky, the Mitsui Professor and a professor in the Department of Political Science, about their work with the LLM Election Observatory, how AI could impact the midterms, and what voters should keep in mind when they interact with chatbots.*

**Q**
: What was the inspiration for this project and what are you hoping to learn through the LLM Election Observatory?

**Podimata**
: People are increasingly using AI chatbots to find and make sense of political and election-related information. That makes it important to understand what information these systems actually provide, not just at one moment in time but throughout an election cycle. This is particularly challenging because the models themselves are continually getting updates, the political information inputs available to them are themselves changing, and their answers can depend on how a user asks a question or what information the user provides about themselves.

One basic problem is that we currently do not have a good historical record of this information environment. If an AI system gives a particular answer about an election today and gives a different answer several weeks later, it can be very difficult to reconstruct after the fact what voters would have seen at each point in time. One important goal of our project is simply to systematically document that environment as it develops and make the resulting data available to other researchers and to the public.

Ultimately, factual accuracy is only the first frontier. We absolutely need to understand whether chatbots provide accurate political information, but we also need to pay just as much attention to the subtler ways in which they may shape people’s understanding of political issues. Differences in framing, emphasis, uncertainty, and cited sources can matter enormously, even in the absence of outright misinformation.

**Q**
: Professor Podimata, you studied how LLMs shaped political discourse and information during the 2024 election. What were the main takeaways of that research and how did those findings inform this new project?

**Podimata**
: The LLM Election Observatory builds on my previous
[work](https://arxiv.org/abs/2509.18446)
during the 2024 presidential election, which found evidence of meaningful variation in AI models’ responses over time and across prompt framings, as well as differences in how models characterized candidates and implicitly anticipated the election outcome.

The 2026 midterms give us an opportunity to expand that work substantially. Midterm elections are particularly interesting because there are many state and local contests unfolding simultaneously, alongside broader national political narratives. Our new audit survey therefore asks both contest-specific questions about the U.S. House and Senate candidates, but also broader questions about voting information and other aspects of the election information environment.

**Q**
: Why do you think it’s so important to be studying how chatbots are responding to political queries across different groups of users?

**Podimata**
: We all build our own “microcosms” through our interactions with chatbots. And yet, we lack systematic ways of understanding how these individualized information environments are shaped by who we are or how they evolve over time as we and the information environment changes.

For example, people may not realize that what their favorite chatbot tells them about a political issue may be quite different from what their friend’s favorite chatbot tells them about the exact same issue. And importantly, these differences matter even when the information being provided is factually correct. Chatbots may frame the same facts differently, emphasize different aspects of an issue, express different levels of uncertainty, or draw on entirely different sources, even when responding to identical queries between different users. As a result, two users may walk away with very different perceptions of the same underlying facts, without ever realizing that their experiences differed.

In some ways, this brings back many of the concerns we (as researchers and society) have grappled with in the context of social media. On social media, users and researchers could, at least to some extent, observe the information circulating across different Facebook groups, Instagram accounts, or TikTok communities. With chatbots, these information environments are largely invisible to anyone outside the individual conversation. We cannot easily observe what different users are being told, let alone systematically compare those responses or track how they change over time. This is precisely why projects like the LLM Election Observatory are so important: By systematically collecting and publicly sharing chatbot responses, we can begin to make these otherwise invisible differences observable and open to scrutiny.

**Q**
: What sorts of questions and AI responses are you tracking through the dashboard?

**Podimata**
: There are several questions we ultimately want this dataset to help us study. For example: Do different models provide systematically different information for the same questions? Do their responses change over the course of the campaign? Does the answer a particular model gives change depending on how a user frames the question or describes themselves (e.g., does it change if the model gets informed that the user is a Democrat or a Republican)? And, finally, what are the sources that the models pull information from when answering election-related questions?

Our
[public dashboard](http://llmelectionobservatory.org/)
is an important part of the project. We want people both from and outside of academia to be able to see the data we are collecting as the election unfolds rather than only seeing the results months later in an academic paper. The dashboard therefore presents the underlying data and some preliminary descriptive analyses, and we plan to make the dataset available for other researchers to study as well. We expect the dashboard to evolve as the data and our methods evolve.

Through this dashboard, we wanted to build on the scientific methodology we developed in 2024 but also to make the research much more accessible and useful to the public while the election is actually unfolding. Not only that, but the addition of MIT political science experts in the team cannot be overstated; Adam and Charles have really helped expand the questions that we are asking in our audit.

**Q**
: What do you wish voters across the country knew about AI chatbots when it comes to searching for election information?

**Berinsky**
: People should be sure to remember that just because a chatbot sounds confident doesn’t mean it is accurate. AI systems are designed to answer the questions that people ask them in an authoritative voice even when they are wrong, incomplete, or leaning on a weak source. These answers are a reasonable place to start, but voters shouldn’t stop there.

**Q**
: What are your findings thus far?

**Podimata**
: We have not yet done the full, longitudinal analysis, so we are only going to talk about broad strokes here, but a few broad patterns seem to be visible in the 2026 data. Across the different user identities we present, we see differences in how the answers are presented, in which sources a model cites, and in tone — sometimes even when the underlying facts are the same. What we cannot yet say is how stable those differences are, how they move over the course of the election, or how a real person would read and react to them. Our future analyses will take this up. It also underscores why the continuous record of responses we are collecting matters more than any single snapshot that you might see in the days around the election.

**Q**
: Professor Berinsky, your research has also shown that in some cases AI chatbots can be harnessed to help refute misinformation. Can you talk a bit about this?

**Berinsky**
: In my undergraduate course on information and social media I have been talking for a while about how AI can cut both ways. On one hand, these tools can generate misleading claims in text, pictures, and video at a scale we have never seen. Basically, AI can help bad actors “flood the zone” with misinformation. On the other hand, some of the most promising recent work demonstrates that evidence-based dialogues with a chatbot can durably reduce belief in conspiracy theories and other beliefs that are not supported by the balance of publicly available evidence.

AI has the potential to do such debunking at scale — something we have long struggled to do. The lesson from decades of misinformation research is that any technology (be it print, radio, or television in earlier eras) is not inherently good or bad for promoting truth. The devil is in the details in how it is built and deployed. Independent auditing like this project can help us assess the ultimate impact of such technologies.

**Q:**
Can you talk a bit about your overall goal with this research?

**Podimata**
: AI is a transformative technology, and people understandably have very different expectations (and feelings) about what it will mean for society at large. All of us have people in our lives that are overly enthusiastic about AI, others that are deeply concerned, and many more that are somewhere in between trying to understand what this technology can and cannot do. Our goal here is not to begin from the assumption that AI is either good or bad for elections. Instead, we hope to shed some light onto one part of this transformation: what information major AI systems are actually giving people about an election as it unfolds.