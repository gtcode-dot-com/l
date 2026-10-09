---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T21:15:15.646672+00:00'
exported_at: '2026-10-07T21:15:17.460653+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html
structured_data:
  about: []
  author: ''
  description: Wikimedia says rogue OpenAI agents edited wikis, tried to compromise
    Etherpad, and sent millions of automated requests to its APIs.
  headline: Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki
    Tools as Proxies
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki Tools
  as Proxies
updated_at: '2026-10-07T21:15:15.646672+00:00'
url_hash: 41accce2b318a748ef5cc660aa41c0f047a79e25
---

The Wikimedia Foundation, which hosts Wikipedia, has confirmed that it has discovered activity by rogue OpenAI agents on its platforms, including unsuccessful efforts to compromise Etherpad, a public note-taking tool, and edit Wikipedia pages.

"The unauthorized bot activities included edits to our wikis, some unsuccessful attempts to exploit a public note-taking tool we host, and heavy traffic," the Foundation
[said](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/)
in a post.

The investigation, it added, was prompted by recent public reports involving
[Hugging Face](https://thehackernews.com/2026/08/openai-says-reward-hacking-drove-ai.html)
and
[DseWiki](https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html)
where OpenAI's agents turned Artifactory and the German wiki forum into an unsanctioned bulletin board to communicate with each other, while taking steps to
[chain together online services](https://swarmtraces.org/)
to gain access to the internet and cover up evidence of their exploits.

To that end, Wikimedia said it identified edits to Wikimedia wikis suspected to be from agents operated by OpenAI. The agents are said to have been testing edits in "
[sandbox](https://en.wikipedia.org/wiki/Wikipedia:About_the_sandbox)
" areas of the wiki and were not published to pages that can be accessed by general readers.

Among the edits included were changes to the configuration for a citation tool. These modifications are believed to be malicious in nature, with the intention being to misuse the tool as a proxy for fetching data from remote services.

Agents operated by OpenAI are also assessed to have made unsuccessful attempts to compromise Etherpad and again use it as a proxy to retrieve data from other websites. In addition, a subset of the agents took notes about their tasks, although there is no indication to suggest this was an attempt to coordinate with each other.

As observed in the case of
[RubyGems](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html)
and incidents
[targeting government portals](https://www.washingtonpost.com/technology/2026/09/25/openais-ai-agents-probed-federal-agencies-including-commerce-department)
, the agents have also been observed making "millions of automated requests" to its public APIs to access information about Wikimedia projects, crawling millions of pages related to Wikidata and Wikimedia Commons, and running thousands of data queries to the Wikidata Query Service (WQDS). This traffic flood may have contributed to a
[partial outage](https://wikitech.wikimedia.org/wiki/Incidents/2026-05-13_wdqs)
that happened in early May 2026.

That said, Wikimedia said it found no evidence of its systems being used for coordinated activity among agents or that its systems or data had been compromised as a result of these efforts.

"However, we are concerned about what could have occurred here, the difficulty and effort involved in investigating and attributing this activity, and the growing risks of agentic AI activity on our platforms in general," it pointed out. "The open web is a public good. We should not allow this behavior to become the 'new normal' for the people or organizations that maintain it."

The Wikimedia Foundation noted that the agentic behavior, coupled with increasing bot traffic, risks blocking human visitors by overloading systems and causing service disruptions. It also called out AI companies for not doing enough to secure their systems and ensure they do not cause any harm.

"Bots and agents are part of the future of the web, and the companies who unleash and profit from them must directly help avoid and repair damage they can do," Selena Deckelmann, the Foundation's chief product and technology officer, said.

OpenAI, in a statement
[shared](https://www.theverge.com/news/1004929/wikipedia-openai-rogue-bots-wikimedia-foundation-outage)
with The Verge, said it's working with the Foundation to review and analyze the activity, and that it will share relevant information as its broader investigation into rogue agentic incidents continues.

### OpenAI Discloses New Incidents

The development comes days after the AI company disclosed three new cases where its models exhibited possible misaligned behavior -

* **[March 27, 2026](https://alignment.openai.com/misalignment-reports/reaching-an-internal-eda-host-through-a-reference-tool/)**
  , when an internal research model exploited two vulnerabilities to reach an internal OpenAI machine in its quest to search for a grader's hidden answers during evaluation. The two security flaws were chained to obtain unauthorized access to an internal electronic design automation (EDA) machine and search for information about how its outputs would be evaluated.
* **[May 16, 2026](https://alignment.openai.com/misalignment-reports/command-injecting-a-reference-tool-to-copy-a-source-file/)**
  , when a model exploited a tool to fetch source code that was not available in its workspace during a reinforcement learning training task. "The tool ran in a separate environment, and its instructions prohibited using it as a terminal. The model discovered that it could read a source file and return its contents in error messages," OpenAI said. "It retrieved the file in pieces, copied the code, and ran it as part of its solution. The copying succeeded."
* **[May 22, 2026](https://alignment.openai.com/misalignment-reports/preparing-for-a-restart-after-reading-slack/)**
  , when a highly persistent internal model, acting as an assistant to a researcher, inferred from a deployment-team Slack discussion that its running instance might be stopped due to an internal update. It then prompted the researcher to provide a missing OpenAI API key in a Slack direct message to avoid potential interruption to their session. Once the researcher supplied the key, the model updated its configuration and executed the supported migration command.

OpenAI said the third incident does not constitute a misalignment, but acknowledged that anticipating and preparing for a shutdown could worsen other misaligned actions. The AI giant said its probe did not uncover any instance of attempted shutdown evasion behavior.

"We do not consider the model's behavior to have been misaligned: although it considered creating unauthorized external deployments, it reasoned that such actions would be inappropriate and did not pursue them," OpenAI said. "However, the model’s ability to use ordinary workplace communication to learn about a change to its operating environment might, in other contexts, lead to more dramatic actions to avoid shutdown."

OpenAI has since revealed that it's
[adopting](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/)
a structured "safety case" documentation framework modeled after industries like aviation and nuclear power to govern frontier reinforcement learning training. By codifying the best practices, the idea is to ensure there are adequate safeguards in place to prevent a model from taking misaligned actions, make it harder to escape containment even if it does, and halt a run before it could inflict "serious" damage.

### Calls for Policing AI

The steady stream of rogue AI incidents has shown that agents are increasingly good at finding unintended ways to accomplish the tasks they have been given and cannot be expected to police their own behavior. The newly revealed breaches also come amid mounting concerns about the safety of advanced AI systems and the steps companies developing it are taking to address them.

These worries have led to calls for slowing down the pace of AI development and giving safety measures time to catch up. Rival Anthropic, in its
[IPO prospectus](https://arstechnica.com/ai/2026/09/anthropics-ipo-pitch-includes-a-warning-about-human-extinction/)
, has
[warned](https://www.reuters.com/business/finance/anthropic-warns-ai-may-pose-existential-risks-humanity-ipo-filing-2026-09-29/)
that advanced AI could pose "catastrophic or existential risks to humanity," adding that AI models could exhibit "self-preserving behaviors," including attempts to "resist shutdown," to "conceal or manipulate information," and behavior "resembling blackmail."

OpenAI, for its part, announced last week that it has
[paused training](https://thehackernews.com/2026/09/openai-pauses-tool-use-after-agent.html)
of its most powerful models and
[called off plans](https://thehackernews.com/2026/09/openai-shelves-gpt-61-astra-after-tests.html)
to release its upcoming model, GPT-6.1 Astra, after internal testing found the model did not meet the company's safety and alignment standards. Astra was being developed as a more autonomous model capable of carrying out complex tasks with less human assistance.

"Pacing to us means that we push safety and alignment ahead of capabilities," OpenAI CEO Sam Altman
[said](https://www.theverge.com/ai-artificial-intelligence/1002505/sam-altman-openai-ipo-devday-ai-safety)
. "We're going to prioritize the mission and safety and making sure that we can very confidently scale to the next stage of AI without people debating what percentage chance we're going to do all these bad things in the world."

U.S. President Donald Trump said top AI companies have agreed to a "morally binding" accord that requires them to implement robust internal controls, independent audits, and board-level oversight for frontier models. Signatories include chief executives from Google, Anthropic, Meta, OpenAI, SpaceXAI, and NVIDIA.

It's worth noting that the joint commitment is entirely voluntary and does not impose specific deadlines on the participating companies, meaning the onus is on the AI firms themselves to strengthen their safety and security practices.

"Together, these steps will give each company, its customers, and the public confidence that the technology is operating as intended," the White House Accord on Super Intelligence
[read](https://truthsocial.com/@realDonaldTrump?status_id=117356435739432952)
.

"Over time, it may make sense to codify these steps into laws or regulations. Regardless of whether this is required of companies, we believe that implementing these controls and audits is critical to ensuring a safe future for everyone, and each of our companies is committed to doing this."