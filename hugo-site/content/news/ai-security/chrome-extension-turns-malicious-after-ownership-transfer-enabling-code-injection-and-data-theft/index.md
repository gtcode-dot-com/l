---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T00:15:15.621443+00:00'
exported_at: '2026-03-10T00:15:17.943099+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html
structured_data:
  about: []
  author: ''
  description: Malicious Chrome extensions tied to ownership transfers push malware
    and steal data, exposing thousands to credential theft and system compromise.
  headline: Chrome Extension Turns Malicious After Ownership Transfer, Enabling Code
    Injection and Data Theft
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Chrome Extension Turns Malicious After Ownership Transfer, Enabling Code Injection
  and Data Theft
updated_at: '2026-03-10T00:15:15.621443+00:00'
url_hash: afeb41f8683f02b6ca8877dc7ad364a5b9fd1695
---

Two Google Chrome extensions have turned malicious after what appears to be a case of
[ownership transfer](https://x.com/tuckner/status/2027416172442853830)
, offering attackers a way to push malware to downstream customers, inject arbitrary code, and harvest sensitive data.

The extensions in question, both originally associated with a developer named "akshayanuonline@gmail.com" (BuildMelon), are listed below -

* QuickLens - Search Screen with Google Lens (ID: kdenlnncndfnhkognokgfpabgkgehodd) - 7,000 users
* ShotBird - Scrolling Screenshots, Tweet Images & Editor (ID: gengfhhkjekmlejbhmmopegofnoifnjp) - 800 users

While QuickLens is no longer available for download from the Chrome Web Store, ShotBird remains accessible as of writing. ShotBird was
[originally launched](https://www.reddit.com/r/chrome_extensions/comments/1gkv28r/free_say_hello_to_shotbird_make_better/)
in November 2024, with its developer, Akshay Anu S (@AkshayAnuOnline),
[claiming](https://x.com/AkshayAnuOnline/status/1854777234541642035)
on X that the extension is suitable for "creating professional, studio-like visuals," and that all processing happens locally.

According to
[research](https://monxresearch-sec.github.io/shotbird-extension-malware-report/)
published by monxresearch-sec, the browser add-on received a "Featured" flag in January 2025, before it was passed on to a different developer ("loraprice198865@gmail.com") sometime last month.

In a similar vein, QuickLens was listed for sale on ExtensionHub on October 11, 2025, by "akshayanuonline@gmail.com" merely two days after it was published, Annex Security's John Tuckner
[said](https://annex.security/blog/pixel-perfect/)
. On February 1, 2026, the extension's owner changed to "support@doodlebuggle.top" on the Chrome Web Store listing page.

The malicious update introduced to QuickLens on February 17, 2026, kept the original functionality but introduced capacities to strip security headers (e.g., X-Frame-Options) from every HTTP response, allowing malicious scripts injected into a web page to make arbitrary requests to other domains, bypassing Content Security Policy (
[CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
) protections.

In addition, the extension contained code to fingerprint the user's country, detect the browser and operating system, and polls an external server every five minutes to receive JavaScript, which is stored in the browser's local storage and executed on every page load by adding a hidden 1×1 GIF <img> element and setting the JavaScript string as its "onload" attribute. This, in turn, causes the malicious code to be executed once the image is loaded.

"The actual malicious code never appears in the extension's source files," Tuckner explained. "Static analysis shows a function that creates image elements. That's it. The payloads are delivered from the C2 and stored in local storage -- they only exist at runtime."

A similar analysis of the ShotBird extension by monxresearch-sec has uncovered the use of direct callbacks to deliver JavaScript code instead of creating a 1x1 pixel image to trigger the execution. The JavaScript is engineered to display a bogus Google Chrome browser update prompt, clicking which users are served a ClickFix-style page to open the Windows Run dialog, launch "cmd.exe," and paste a PowerShell command, resulting in the download of an executable named "googleupdate.exe" on Windows hosts.

The malware then proceeds to hook input, textarea, select HTML elements, and capture any data entered by the victim. This could include credentials, PIN, card details, tokens, and government identifiers. It's also equipped to siphon data stored in the Chrome web browser, such as passwords, browsing history, and extension-related information.

"This is a two-stage abuse chain: extension-side remote browser control plus host-level execution pivot via fake updates," the researcher said. "The result is high-risk data exposure in-browser and confirmed host-side script execution on at least one affected system. In practical terms, this elevates the impact from browser-only abuse to likely credential theft and broader endpoint compromise."

It's assessed that the same threat actor is behind the compromise of the two extensions and is operating them in parallel, given the use of an identical command-and-control (C2) architecture pattern, ClickFix lures injected into the browsing context, and ownership transfer as an infection vector.

Interestingly, the original extension developer has
[published](https://chromewebstore.google.com/detail/radial-new-tab/fogdlfdfpjlpmpmnmeepffaikefkacnc)
[several](https://chromewebstore.google.com/detail/reditop-%E2%80%93-scroll-to-top-f/gddonialdhbldcdbnbloangmjnpcnhhd)
[other](https://chromewebstore.google.com/detail/audiomatch-youtube-audio/mejaghdgnidejbeofmfhnogbniipdjge)
[extensions](https://chromewebstore.google.com/detail/sidewiki-%E2%80%93-sidebar-for-wi/ofifhmaojnmphodmgkipjpjedgnhkbhl)
under their name on the Chrome Web Store, and all of them have received a Featured badge. The developer also has an
[account on ExtensionHub](https://www.extensionhub.io/akshayanu)
, although no extensions are currently listed for sale. What's more, the individual has
[attempted](https://www.reddit.com/r/DomainsForSale/comments/1r710f3/aiinfrastackcom_domain_for_sale_2500/)
to sell domains like "AIInfraStack[.]com" for $2,500, stating the "strong keyword domain" is "relevant for [sic] rapidly growing AI ecosystem."

"This is the extension supply chain problem in a nutshell," Annex Security said. "A 'Featured,' reviewed, functional extension changes hands, and the new owner pushes a weaponized update to every existing user."

The disclosure comes as Microsoft warned of the
[malicious Chromium‑based browser extensions](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html)
that masquerade as legitimate AI assistant tools to harvest LLM chat histories and browsing data.

"At scale, this activity turns a seemingly trusted productivity extension into a persistent data collection mechanism embedded in everyday enterprise browser usage, highlighting the growing risk browser extensions pose in corporate environments," the Microsoft Defender Security Research Team
[said](https://www.microsoft.com/en-us/security/blog/2026/03/05/malicious-ai-assistant-extensions-harvest-llm-chat-histories/)
.

In recent weeks, threat hunters have also flagged a malicious Chrome extension named lmΤoken Chromophore (ID: bbhaganppipihlhjgaaeeeefbaoihcgi) that impersonates imToken while advertising itself as a hex color visualizer in the Chrome Web Store to steal cryptocurrency seed phrases using phishing redirects.

"Instead of providing the harmless tool it promises, the extension automatically opens a threat actor-controlled phishing site as soon as it is installed, and again whenever the user clicks it," Socket researcher Kirill Boychenko
[said](https://socket.dev/blog/fake-imtoken-chrome-extension-steals-seed-phrases-via-phishing-redirects)
.

"On install, the extension fetches a destination URL from a hardcoded JSONKeeper endpoint (jsonkeeper[.]com/b/KUWNE) and opens a tab pointing to a lookalike Chrome Web Store-style domain, chroomewedbstorre-detail-extension[.]com. The landing page impersonates imToken using mixed-script homoglyphs and funnels victims into credential-capture flows that request either a 12 or 24-word seed phrase or a private key."

Other malicious extensions
[flagged](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-02-20-%20AI-Accelerated%20Malicious%20Chrome%20Extension%20Campaigns.txt)
by Palo Alto Networks Networks Unit 42 have been found to engage in affiliate hijacking and data exfiltration, with one of them – Chrome MCP Server - AI Browser Control (ID: fpeabamapgecnidibdmjoepaiehokgda) –
[serving](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-02-11-IOCs-for-RAT-disguinsed-as-AI-based-browser-extension.txt)
as a full-fledged remote access trojan while masquerading as an AI automation tool using the Model Context Protocol (MCP).

Unit 42 researchers have also revealed that
[three popular Chrome extensions](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)
– Urban VPN Proxy, Urban Browser Guard, and Urban Ad Blocker – are again available on the Chrome Web Store after previously being removed for scraping AI conversations from various chatbots, including OpenAI ChatGPT, Anthropic Claude, Microsoft Copilot, DeepSeek, Google Gemini, xAI Grok, Meta AI, and Perplexity.

"Following the public disclosure of the campaign on December 15, 2025, the developer updated benign versions in January 2026, likely in response to the report," researchers Qinge Xie, Nabeel Mohamed, Shresta Bellary Seetharam, Fang Liu, Billy Melicher, and Alex Starov
[said](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-02-13-IOCs-for-tactics-by-browser-extensions-to-avoid-bans.txt)
.

Furthermore, the cybersecurity company identified an extension called Palette Creator (ID: iofmialeiddolmdlkbheakaefefkjokp), which has over 100,000 users and whose previous version communicated with known network indicators associated with a campaign dubbed
[RedDirection](https://thehackernews.com/2025/07/weekly-recap-scattered-spider-arrests.html#:~:text=Malicious%20Browser%20Extensions%20Galore)
to carry out browser hijacking.

That's not all. A new campaign
[comprising](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-03-09-Threat-Alert-30K-domains-distributing-malicious-AI-related-browser-extension.txt)
over 30,000 domains has been found to initiate a redirect chain to route traffic to a landing page ("ansiblealgorithm[.]com") that's used for distributing a Chrome extension called OmniBar AI Chat and Search (ID: ajfanjhcdgaohcbphpaceglgpgaaohod).

The extension makes use of the chrome\_settings\_overrides API to alter Chrome settings and set the browser home page to omnibar[.]ai, as well as make the default search provider to a custom URL: "go.omnibar[.]ai/?api=omni&sub1=omnibar.ai&q={searchTerms}​" and track queries via an API parameter.

It's believed that the end goal is to perform browser-hijacking as part of what seems to be a large-scale affiliate marketing scheme, Unit 42 said, adding it identified two other extensions that exhibit the same browser-hijacking behavior consistent with OmniBar via home page override and search interception -

* AI Output Algo Tool (ID: eeoonfhmbjlmienmmbgapfloddpmoalh)
* Serpey.com official extension (ID: hokdpdlchkgcenfpiibjjfkfmleoknkp)

A deeper investigation of three more extensions published by the same developer ("jon@status77.com" aka Status 77) has uncovered that two of them track user browsing activity to inject affiliate markers, while a third one extracts and transmits user Reddit comment threads to a developer-controlled API endpoint -

* Care.Sale (ID: jaioobipjdejpeckgojiojjahmkiaihp)
* Giant Coupons Official Extension (ID: akdajpomgjgldidenledjjiemgkjcchc)
* Consensus - Reddit Comment Summarizer (ID: mkkfklcadlnkhgapjeejemflhamcdjld)

Users who have installed any of the aforementioned extensions are advised to remove them from their browsers with immediate effect, avoid side-loading or installing unverified productivity extensions, and audit browsers for any unknown extensions and uninstall them.