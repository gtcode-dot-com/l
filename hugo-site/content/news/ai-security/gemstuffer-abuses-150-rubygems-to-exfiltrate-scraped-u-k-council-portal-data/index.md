---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:21:31.071508+00:00'
exported_at: '2026-05-14T21:21:32.349553+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html
structured_data:
  about: []
  author: ''
  description: GemStuffer used 150+ RubyGems to scrape U.K. council portals, turning
    the registry into a data exfiltration channel.
  headline: GemStuffer Abuses 150+ RubyGems to Exfiltrate Scraped U.K. Council Portal
    Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: GemStuffer Abuses 150+ RubyGems to Exfiltrate Scraped U.K. Council Portal Data
updated_at: '2026-05-14T21:21:31.071508+00:00'
url_hash: ff51c761ea4552ff965c4bc88a1110ef5264b38a
---

**

Ravie Lakshmanan
**

May 13, 2026

Software Supply Chain / Data Exfiltration

Cybersecurity researchers are calling attention to a new campaign dubbed
**GemStuffer**
that has targeted the RubyGems repository with more than 150 gems that use the registry as a data exfiltration channel rather than for malware distribution.

"The packages do not appear designed for mass developer compromise," Socket
[said](https://socket.dev/blog/gemstuffer)
. "Many have little or no download activity, and the payloads are repetitive, noisy, and unusually self-contained."

"Instead, the scripts fetch pages from U.K. local government democratic services portals, package the collected responses into valid .gem archives, and publish those gems back to RubyGems using hardcoded API keys."

The development comes as
[RubyGems temporarily disabled](https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html)
new account registration following what has been described as a major malicious attack. While it's not clear if the two sets of activities are related, the application security company said GemStuffer fits the "same abuse pattern," which involves using newly created packages with junk names to host the scraped data.

At a high level, the campaign abuses RubyGems as a place to stage the scraped council content. It does this by fetching hard-coded U.K. council portal URLs, packaging the HTTP responses into valid .gem archives, and publishing those archives to RubyGems using embedded registry credentials.

In some cases, the payload embedded within the gem creates a temporary RubyGems credential environment under "/tmp," overrides the HOME environment variant, builds a gem locally, and pushes it to RubyGems using the
[gem command-line interface](https://guides.rubygems.org/command-reference/)
(CLI), as opposed to depending on pre-existing RubyGems credentials on the target machine.

Other variants of the malicious gems have been found to eschew the CLI component in favor of uploading the archive directly to the RubyGems API via an HTTP POST request. Once the new gems have been published, all an attacker has to do is run a "gem fetch" command with the gem name and version to access the scraped data.

The novel scraping campaign has been found to target public-facing ModernGov portals used by Lambeth, Wandsworth, and Southwark, with an aim to collect committee meeting calendars, agenda item listings, linked PDF documents, officer contact information, and RSS feed content.It's not clear what exactly the end goals are, as the information appears to be publicly accessible anyway.

Socket has assessed that the systematic bulk collection and archival of this data raises the possibility that the attacker may be leveraging the "council portal access as a pivot to demonstrate capability against government infrastructure."

"It may be registry spam, a proof-of-concept worm, an automated scraper misusing RubyGems as a storage layer, or a deliberate test of package registry abuse," Socket said. "But the mechanics are intentional: repeated gem generation, version increments, hardcoded RubyGems credentials, direct registry pushes, and scraped data embedded inside package archives."