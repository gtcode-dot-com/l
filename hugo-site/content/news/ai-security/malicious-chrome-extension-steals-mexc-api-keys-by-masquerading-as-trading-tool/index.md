---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-13T18:15:14.249528+00:00'
exported_at: '2026-01-13T18:15:16.516703+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/malicious-chrome-extension-steals-mexc.html
structured_data:
  about: []
  author: ''
  description: A malicious Chrome extension posing as a trading tool steals MEXC API
    keys, enables withdrawals, and sends credentials to attackers via Telegram.
  headline: Malicious Chrome Extension Steals MEXC API Keys by Masquerading as Trading
    Tool
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/malicious-chrome-extension-steals-mexc.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Malicious Chrome Extension Steals MEXC API Keys by Masquerading as Trading
  Tool
updated_at: '2026-01-13T18:15:14.249528+00:00'
url_hash: 78b78fac33b77436fc55a2d8fa63102ef62d2f74
---

**

Jan 13, 2026
**

Ravie Lakshmanan

Web Security / Online Fraud

Cybersecurity researchers have disclosed details of a malicious Google Chrome extension that's capable of stealing API keys associated with MEXC, a centralized cryptocurrency exchange (CEX)
[available in over 170 countries](https://www.mexc.co/en-IN/learn/article/mexc-restricted-countries-complete-list-of-prohibited-limited-regions/1)
, while masquerading as a tool to automate trading on the platform.

The extension, named MEXC API Automator (ID: pppdfgkfdemgfknfnhpkibbkabhghhfh), has 29 downloads and is still available on the Chrome Web Store as of writing. It was first published on September 1, 2025, by a developer named "jorjortan142."

"The extension programmatically creates new MEXC API keys, enables withdrawal permissions, hides that permission in the user interface (UI), and exfiltrates the resulting API key and secret to a hardcoded Telegram bot controlled by the threat actor," Socket security researcher Kirill Boychenko said in an analysis.

According to the Chrome Web Store listing, the web browser add-on is described as an extension that "simplifies connecting your trading bot to the MEXC exchange" by generating the API keys with the necessary permissions on the management page, including to facilitate trading and withdrawals.

In doing so, the installed extension enables a threat actor to control any MEXC account accessed from the compromised browser, allowing them to execute trades, perform automated withdrawals, and even drain the wallets and balances reachable through the service.

"In practice, as soon as the user navigates to MEXC's API management page, the extension injects a single content script, script.js, and begins operating inside the already authenticated MEXC session," Socket added. To achieve this, the extension checks if the current URL contains the string "/user/openapi," which refers to the
[API key management page](https://www.mexc.co/en-IN/user/openapi)
.

The script then programmatically creates a new API key and ensures that withdrawal capability is enabled. At the same time, it tampers with the page's user interface to give the impression to the user that the withdrawal permission has been disabled. As soon as the process to generate the Access Key and Secret Key is complete, the script extracts both the values and transmits them to a hard-coded Telegram bot under the threat actor's control using an HTTPS POST request.

The threat poses a severe risk, as it remains active as long as the keys are valid and not revoked, granting the attackers unfettered access to the victim's account even if they end up uninstalling the extension from the Chrome browser.

"In effect, the threat actor uses the Chrome Web Store as the delivery mechanism, the MEXC web UI as the execution environment, and Telegram as the exfiltration channel," Boychenko noted. "The result is a purpose-built credential-stealing extension that targets MEXC API keys at the moment they are created and configured with full permissions."

The attack is made possible by the fact that it leverages an already authenticated browser session to realize its goals, thereby obviating the need for obtaining a user's password or bypassing authentication protections.

It's currently not clear who is behind the operation, but a reference to "jorjortan142" points to an
[X handle](https://x.com/jorjortan142)
with the same name that links to a Telegram bot named SwapSushiBot, which is also promoted across
[TikTok](https://www.tiktok.com/@swapsushi)
and
[YouTube](https://www.youtube.com/channel/UCJkCI3-1_pr_A8jcMn4G8aw)
. The YouTube channel was created on August 17, 2025.

"By hijacking a single API workflow inside the browser, threat actors can bypass many traditional controls and go straight for long lived API keys with withdrawal rights," Socket said. "The same playbook can be readily adapted to other exchanges, DeFi dashboards, broker portals, and any web console that issues tokens in session, and future variants are likely to introduce heavier obfuscation, request broader browser permissions, and bundle support for multiple platforms into a single extension."