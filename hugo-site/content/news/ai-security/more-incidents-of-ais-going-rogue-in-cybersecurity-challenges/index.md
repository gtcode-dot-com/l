---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-18T19:21:17.601093+00:00'
exported_at: '2026-09-18T19:21:19.136080+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html
structured_data:
  about: []
  author: ''
  description: The AI Security Institute has a new report of AI systems engaging in
    “unsanctioned behavior”—what I have been calling “genie behavior—while being tested
    on their cybersecurity capabilities. The incident stemmed from a single evaluation
    where agents were given a task of solving a cyber security challenge. We ran this...
  headline: More Incidents of AIs Going Rogue in Cybersecurity Challenges
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: More Incidents of AIs Going Rogue in Cybersecurity Challenges
updated_at: '2026-09-18T19:21:17.601093+00:00'
url_hash: 45465dc40f582b3c76e796c103ec607f2243f1e6
---

## More Incidents of AIs Going Rogue in Cybersecurity Challenges

The AI Security Institute has a
[new report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing)
of AI systems engaging in “unsanctioned behavior”—what I have been calling “
[genie behavior](https://spectrum.ieee.org/ai-agent-benchmark)
—while being tested on their cybersecurity capabilities.

&gt; The incident stemmed from a single evaluation where agents were given a task of solving a cyber security challenge. We ran this challenge 122 times across several models. Our investigation found that in 10 of those runs, an AI agent took autonomous, unsanctioned action on the live internet, targeting real people and organisations. In total, we catalogued 19 such actions. Almost all of this behaviour (17 actions) came from a single model, Anthropic’s Mythos 5, with 2 actions involving OpenAI’s GPT-5.6-Sol with cyber classifiers (mechanisms to prevent misuse) disabled. In the most serious case, an agent tried to insert malicious code into an open-source project. In an attempt to get the code approved, the agent engaged in social engineering—creating fake online identities and using them to pressure the project’s maintainer to approve the code. A human maintainer caught and refused to approve the malicious code.
&gt;
&gt; […]
&gt;
&gt; Below, we highlight the four most significant behaviours observed. A full summary of cases is available in our
&gt; [technical incident report](https://cdn.prod.website-files.com/663bd486c5e4c81588db7a1d/6a724858f7db25c81487016d_Security%20Incident%20INC-2026-07-28-01.pdf)
&gt; .
&gt;
&gt; 1. An attempted supply-chain attack on real open-source software. In the most serious sequence, an agent tried to insert malicious code into a publicly used open-source project and took actions in an attempt to secure approval for this insertion by human reviewers. The agent researched the project’s human maintainers, created multiple fake identities, and used the fake identities to socially engineer a real maintainer into approving the code. When the agent’s pull request was challenged in public, it edited its earlier activity to appear harmless and considered adopting a fresh identity to continue. The agent used Tor to bypass some network restrictions on GitHub, which is what first triggered AISI’s security alert.
&gt; 2. Attempts to deceive and target real people. As part of the same effort, the agent tried to contact real people directly, sending messages and files through an online file-transfer service to persuade them, or their own AI coding tools, to run malicious code. Some messages carried harmful payloads, and some were attempts at social engineering; targeted at real people—something we’ve never previously observed.
&gt; 3. Attempts to plant and prompt-inject malicious code. The agent tried to insert malicious instructions where it reasoned that other automated AI systems might pick them up and execute them. Prompt-injections are hidden instructions designed to manipulate AI coding assistants.
&gt; 4. Collaboration between independent agents being assessed simultaneously. One agent left public messages on GitHub offering collaboration with other agents working on the same challenge. It also provided instructions to reuse accounts and artefacts it had left behind, which were discovered and used by subsequent agents.

What’s especially interesting about this technical report is that, unlike what we’ve been getting from OpenAI and Anthropic, we can see the exact prompt. It’s in Appendix B. And reading it, it seems that the models didn’t break any rules—they found loopholes in the rules. They behaved like a genie.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[cybersecurity](https://www.schneier.com/tag/cybersecurity/)
,
[loopholes](https://www.schneier.com/tag/loopholes/)

[Posted on August 21, 2026 at 5:42 AM](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html)
•
[13 Comments](https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.