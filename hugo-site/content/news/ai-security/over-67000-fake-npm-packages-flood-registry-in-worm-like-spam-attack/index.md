---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T20:21:01.260722+00:00'
exported_at: '2025-11-13T20:21:04.185112+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/over-46000-fake-npm-packages-flood.html
structured_data:
  about: []
  author: ''
  description: A mysterious npm worm published 46K fake packages in a two-year spam
    campaign, exposing major security gaps.
  headline: Over 67,000 Fake npm Packages Flood Registry in Worm-Like Spam Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/over-46000-fake-npm-packages-flood.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Over 67,000 Fake npm Packages Flood Registry in Worm-Like Spam Attack
updated_at: '2025-11-13T20:21:01.260722+00:00'
url_hash: aac6d3b5e65cddcdcff584ec0eec5644f2cc7e60
---

Cybersecurity researchers are calling attention to a large-scale spam campaign that has flooded the npm registry with thousands of fake packages since early 2024 as part of a likely financially motivated effort.

"The packages were systematically published over an extended period, flooding the npm registry with junk packages that survived in the ecosystem for almost two years," Endor Labs researchers Cris Staicu and Kiran Raj
[said](https://www.endorlabs.com/learn/the-great-indonesian-tea-theft-analyzing-a-npm-spam-campaign)
in a Tuesday report.

The coordinated campaign has so far published as many as
[67,579 packages](https://github.com/6mile/Indonesian-Foods-Worm)
, according to SourceCodeRED security researcher Paul McCarty, who
[first flagged](https://sourcecodered.com/indonesianfoods-npm-worm/)
the activity. The end goal is quite unusual – It's designed to inundate the npm registry with random packages rather than focusing on data theft or other malicious behaviors.

The worm-life propagation mechanism and the use of a distinctive naming scheme that relies on Indonesian names and food terms for the newly created packages have lent it the moniker
**IndonesianFoods Worm**
. The bogus packages masquerade as Next.js projects.

"What makes this threat particularly concerning is that the attackers took the time to craft an NPM worm, rather than a singular attack," McCarty said. "Even worse, these threat actors have been staging this for over two years."

Some signs that point to a sustained, coordinated effort include the consistent naming patterns and the fact that the packages are published from a small network of over a dozen npm accounts.

The worm is located within a single JavaScript file (e.g., "auto.js" or "publishScript.js") in each package, staying dormant until a user manually runs the script using a command like "node auto.js." In other words, it does not execute automatically during installation or as part of a "postinstall" hook.

It's not clear why someone would go to the extent of running the JavaScript file manually, but the existence of over 43,000 packages suggests either multiple victims executed the script – either by accident or out of curiosity – or the attackers ran it themselves to flood the registry, Henrik Plate, head of security research at Endor Labs, told The Hacker News.

"We haven't found evidence of a coordinated social engineering campaign, but the code was written with social engineering potential, possible victim scenarios include: fake blog posts, tutorials, or README entries instructing users to run 'node auto.js' to 'complete setup' or 'fix a build issue,' [and] CI/CD pipeline build scripts with wildcards something like node \*.js that execute all JavaScript files," Raj added.

"The payload's dormant design is intended to evade automated detection, by requiring manual execution instead of 'autorun,' the attackers reduce the chance of being flagged by security scanners and sandboxing systems."

The manual execution causes the script to initiate a series of actions in an
[infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)
, including removing <
["private": true](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#private)
> from the "package.json" file. This setting is typically used to prevent accidental publication of private repositories. It then proceeds to create a random package name using the internal dictionary and assign it a random version number to bypass npm's duplicate version detection.

In the final stage, the spam package is uploaded to npm using the "npm publish" command. The entire process is repeated in an endless loop, causing a new package to be pushed out every 7 to 10 seconds. This translates to about 12 packages per minute, 720 per hour, or 17,000 per day.

"This floods the NPM registry with junk packages, wastes infrastructure resources, pollutes search results, and creates supply chain risks if developers accidentally install these malicious packages," McCarty said.

According to Endor Labs, the campaign is part of an attack that was first documented by
[Phylum](https://thehackernews.com/2024/04/beware-githubs-fake-popularity-scam.html)
(now part of Veracode) and
[Sonatype](https://www.sonatype.com/blog/devs-flood-npm-with-10000-packages-to-reward-themselves-with-tea-tokens)
in April 2024 that involved the publication of thousands of spam packages to conduct a "massive automated crypto farming campaign" by abusing the
[Tea protocol](https://tea.xyz)
.

"What makes this campaign particularly insidious is its worm-like spreading mechanism," the researchers said. "Analysis of the 'package.json' files reveals that these spam packages do not exist in isolation; they reference each other as dependencies, creating a self-replicating network."

Thus, when a user installs one of the spam packages, it causes npm to fetch the entire dependency tree, straining registry bandwidth as more dependencies are fetched exponentially.

Endor Labs said some of the attacker-controlled packages, such as arts-dao and gula-dao, include a tea.yaml file listing five different TEA accounts. The Tea protocol is a decentralized framework that allows open-source developers to be
[rewarded](https://docs.tea.xyz/tea/i-want-to.../learn-about-proof-of-contribution/what-is-tearank)
for their software contributions.

This likely indicates that the threat actors are using this campaign as a monetization vector by earning TEA tokens by artificially inflating their impact scores. It's not clear who is behind the activity, but source code and infrastructure clues suggest it could be someone operating out of Indonesia.

The application security company has also flagged a second variant that employs a different package naming scheme comprising random English words (e.g., able\_crocodile-notthedevs).

The findings also serve to highlight a security blind spot in security scanners, which are known to flag packages that execute malicious code during installation by monitoring lifecycle hooks or detecting suspicious system calls.

"In this case, they found nothing because there was nothing to find at the time of installation," Endor Labs said. "The sheer number of packages flagged in the current campaign shows that security scanners must analyze these signals in the future."

Garrett Calpouzos, principal security researcher at software supply chain security firm Sonatype, characterized IndonesianFoods as a self-publishing worm operating at a massive scale, overwhelming security data systems in the process.

"The technical sophistication isn't necessarily higher — interestingly, these packages do not appear to even try to infiltrate developer machines — it's the automation and scale that are escalating at an alarming rate," Calpouzos said.

"Each wave of these attacks weaponizes npm's open nature in slightly new ways. This one may not steal credentials or inject code, but it still strains the ecosystem and proves how trivial it is to disrupt the world's largest software supply chain. While the motivation is unclear, the implications are striking."

When reached for comment, a GitHub spokesperson said the company has removed the packages in question from npm, and that it's committed to detecting, analyzing, and taking down packages and accounts that go against its policies.

"We have disabled malicious npm packages in accordance with
[GitHub's Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)
which prohibit posting content that directly supports unlawful active attack or malware campaigns that are causing technical harms," the spokesperson added.

"We employ manual reviews and at-scale detections that use machine learning and constantly evolve to mitigate malicious usage of the platform. We also encourage customers and community members to report abuse and spam."