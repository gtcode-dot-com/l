---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-04T16:15:17.482045+00:00'
exported_at: '2026-05-04T16:15:19.798481+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32948
structured_data:
  about: []
  author: ''
  description: 'DShield Honeypot Update, Author: Johannes Ullrich'
  headline: DShield Honeypot Update, (Mon, May 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32948
  publisher:
    logo: /favicon.ico
    name: GTCode
title: DShield Honeypot Update, (Mon, May 4th)
updated_at: '2026-05-04T16:15:17.482045+00:00'
url_hash: 3f68827aaeacb46dbb6caf1fb149b7c343992d93
---

This week, I will release a few updates to our DShield honeypot. The update should happen automatically if you have "automatic updates" enabled on your system. There will be two major changes:

### Compatibility with Ubuntu 26.04 / new versions of Raspberry Pi OS

Ubuntu released version 26.04 LTS about a week ago. It will pretty much work already, but I made some adjustments if you are using the "minimum server install". 24.04 will continue to be supported. There have been some issues with 26.04, particularly with some tools that were converted to Rust. You will be ok staying with 24.04 LTS for now. Earlier versions of Ubuntu (22.04, 20.04) will no longer be supported.

Whenever you upgrade your operating system to a new major version, I recommend you reinstall the honeypot from scratch. You may want to retain the "dshield.ini" file to simplify the reinstall. Reinstalling from scratch ensures that all required dependencies are installed.

For older Ubuntu versions, Python dependencies make support rather difficult. For in-place upgrades, I will try to maintain compatibility as much as possible, but new installs should use either 24.04 or 26.04.

The next update will also fix any issues with new versions of Raspberry Pi OS. The goal is to maintain compatibility with the 32- and 64-bit versions of "trixie" and "bookworm".  Testing for Raspberry Pi OS is a bit more complex because it requires physical devices. If anybody has a good way to virtualize Raspberry Pi OS: Please let me know :)

### Updating Cowrie

The next update will also include an updated version of Cowrie. We have fallen quite a bit behind, and I hope to add some new features. If you currently do not see any Cowrie (ssh/telnet) logs in your account, please update your API key ("Auth Key"). Some older API keys are not compatible with the current version of Cowrie. Newer keys are random hexadecimal strings, while older keys are base64 encoded random strings.

As always, please use our
[contact form](https://isc.sans.edu/contact.html)
if you are running into any problems.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|