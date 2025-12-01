---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-01T21:28:22.888135+00:00'
exported_at: '2025-12-01T21:28:25.784113+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html
structured_data:
  about: []
  author: ''
  description: ShadyPanda abused browser extensions for seven years, turning 4.3M
    installs into a multi-phase surveillance and hijacking campaign.
  headline: ShadyPanda Turns Popular Browser Extensions with 4.3 Million Installs
    Into Spyware
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: ShadyPanda Turns Popular Browser Extensions with 4.3 Million Installs Into
  Spyware
updated_at: '2025-12-01T21:28:22.888135+00:00'
url_hash: 8758daf817899c6c8ea091cf0aac1540f27c9e34
---

A threat actor known as
**ShadyPanda**
has been linked to a seven-year-long browser extension campaign that has amassed over 4.3 million installations over time.

Five of these extensions started off as legitimate programs before malicious changes were introduced in mid-2024, according to a
[report](https://www.koi.ai/blog/4-million-browsers-infected-inside-shadypanda-7-year-malware-campaign)
from Koi Security, attracting 300,000 installs. These extensions have since been taken down.

"These extensions now run hourly remote code execution – downloading and executing arbitrary JavaScript with full browser access," security researcher Tuval Admoni said in a report shared with The Hacker News. "They monitor every website visit, exfiltrate encrypted browsing history, and collect complete browser fingerprints."

To make matters worse, one of the extensions, Clean Master, was featured and verified by Google at one point. This trust-building exercise allowed the attackers to expand their user base and silently issue malicious updates years later without attracting any suspicion.

Meanwhile, another set of five add-ons from the same publisher is designed to keep tabs on every URL visited by its users, as well as record search engine queries and mouse clicks, and transmit the information to servers located in China. These extensions have been installed about four million times, with
[WeTab](https://microsoftedge.microsoft.com/addons/detail/wetab-%E6%96%B0%E6%A0%87%E7%AD%BE%E9%A1%B5/bpelnogcookhocnaokfpoeinibimbeff)
alone accounting for three million installs.

Early signs of malicious activity were said to have been observed in 2023, when 20 extensions on the Chrome Web Store and 125 extensions on Microsoft Edge were published by developers named "nuggetsno15" and "rocket Zhang," respectively. All the identified extensions masqueraded as wallpaper or productivity apps.

These extensions were found to engage in affiliate fraud by stealthily injecting tracking codes when users visited eBay, Booking.com, or Amazon to generate illicit commissions from users' purchases. In early 2024, the attack shifted from seemingly harmless injections to active browser control through search query redirection, search query harvesting, and exfiltration of cookies from specific domains.

"Every web search was redirected through trovi.com – a known browser hijacker," Koi said. "Search queries logged, monetized, and sold. Search results manipulated for profit."

At some point in mid-2024, five extensions, three of which had been operating legitimately for years, were modified to distribute a malicious update that introduced backdoor-like functionality by checking the domain "api.extensionplay[.]com" once every hour to retrieve a JavaScript payload and execute it.

The payload, for its part, is designed to monitor every website visit and send the data in encrypted format to a ShadyPanda server ("api.cleanmasters[.]store"), along with a detailed browser fingerprint. Besides using extensive obfuscation to conceal the functionality, any attempt to access the browser's developer tools causes it to switch to benign behavior.

Furthermore, the extensions can stage adversary-in-the-middle (AitM) attacks to facilitate credential theft, session hijacking, and arbitrary code injection into any website.

The activity moved to the final stage when five other extensions published around 2023 to the Microsoft Edge Addons hub, including WeTab, leveraged its huge install base to enable comprehensive surveillance, including gathering every URL visited, search queries, mouse clicks, cookies, and browser fingerprints.

They also come fitted with capabilities to collect information about how a victim interacts with a web page, such as the time spent viewing it and scrolling behavior. The WeTab extension is still available for download as of writing.

The findings paint the picture of a sustained campaign that transpired over four distinct phases, progressively turning the browser extensions from a legitimate tool into data-gathering spyware. However, it bears noting that it's not clear if the attackers artificially inflated the downloads to lend them an illusion of legitimacy.

Users who installed the extensions are recommended to remove them immediately and rotate their credentials out of an abundance of caution.

"The auto-update mechanism – designed to keep users secure – became the attack vector," Koi said. "Chrome and Edge's trusted update pipeline silently delivered malware to users. No phishing. No social engineering. Just trusted extensions with quiet version bumps that turned productivity tools into surveillance platforms."

"ShadyPanda's success isn't just about technical sophistication. It's about systematically exploiting the same vulnerability for seven years: Marketplaces review extensions at submission. They don't watch what happens after approval."