---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-09T09:44:51.276020+00:00'
exported_at: '2026-08-09T09:44:52.918621+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
structured_data:
  about: []
  author: ''
  description: Outlook CSS techniques can spoof Microsoft sign-in and capture passwords,
    while Gmail image-set() can trigger external requests from malicious email c
  headline: New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New CSS Attacks Can Break Webmail Defenses to Steal Passwords and Tokens
updated_at: '2026-08-09T09:44:51.276020+00:00'
url_hash: f57597fba6eebeb6416fb6f5494be8907c27c6f3
---

**

Swati Khandelwal
**

Aug 08, 2026

Email Security / Vulnerability

New research shows content inside an email can escape its message boundary and interfere with the webmail interface.

Across attack chains spanning Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and AOL Mail, the techniques can capture passwords, take over third-party accounts, leak tokens, hijack trusted UI actions, and manipulate AI tools that read email.

PortSwigger researcher
**Gareth Heyes**
presented the work at Black Hat USA 2026. One Outlook/Firefox chain spoofs a Microsoft sign-in screen and captures the password a recipient types. A Yahoo/AOL paste race can expose a Medium email-login token and let an attacker sign in as the victim. A Gmail/Cowork chain can exfiltrate a Slack token after prompt injection and user interaction.

The paper presents proof-of-concept research and does not report malicious exploitation. Public PoCs remain available as of August 8. The researcher said Fastmail fixed two CSS mutation bugs and a Proton Mail proxy bypass stopped working when he retested it, while Outlook label-jacking and Gmail's image-set() bypass still worked when the research was published on August 6.

The paper does not state whether the full Outlook password-capture chain was fixed. For webmail providers, the paper recommends isolating HTML email in sandboxed iframes and tightly restricting CSS, custom attributes, select menus, and image requests.

The
[research](https://portswigger.net/research/css-the-bomb-inside-your-inbox)
follows two paths: abuse HTML and CSS that webmail already allows, or create a discrepancy between what a sanitizer approves and what the browser or application ultimately creates. Both can cross the boundary between an untrusted message and its trusted interface.

Outlook shows how the pieces can combine. Allowed label elements can trigger controls outside the message, while application JavaScript can turn sanitized custom attributes into new DOM nodes carrying CSS outside the sanitizer's allow list. A media-query parsing trick then gave the attacker arbitrary CSS.

The chain disguises a select element as a password field, and Firefox resets its roughly one-second option-selection timer when the select moves offscreen, making capture real-time.

VIDEO

Yahoo Mail and AOL Mail exposed a different route. In Firefox, pasted HTML could briefly retain active CSS before sanitization. In the Medium demonstration, the attacker initiates an email-login flow, the victim copies attacker-supplied CSS to the clipboard, and then pastes it into a Yahoo or AOL draft. The resulting requests reveal enough of the 12-character login token for the attacker's server to reconstruct it, which can then be used to sign in as the victim.

The paper also introduces a click-based exfiltration technique for cases where Content Security Policy (CSP) blocks external resources. Given style injection and a numeric token rendered as text in the email, CSS can determine which digits occur and how often, hide non-matching links, and leave the matching link across the page. A victim click sends the digits and their frequency to the attacker's server.

VIDEO

AI-connected email creates another route. Gmail's image-set() fallback could make an external request despite sanitization. Heyes and PortSwigger colleague Pete Hendy chained it to an indirect prompt-injection email processed by Anthropic's Claude Cowork through a connected
[Gmail connector](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
.

In the demonstrated setup, after the attacker triggered a Slack token confirmation email and the victim asked Cowork to process the emails, the injected instructions caused it to retrieve the token and place it in an HTML draft; viewing the draft leaked it.

A Fastmail demonstration targeted OpenAI's Atlas AI browser. CSS pseudo-elements and opacity made the human see harmless text while the model read hidden instructions. When the user asked Atlas to translate the visible text, the hidden prompt caused it to open tabs and encode the victim's name in URL fragments. OpenAI is
[deprecating Atlas](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)
and says it is scheduled to stop working on August 9, 2026.

Other findings include Fastmail "CSS hotwiring," which can redirect clicks into unintended and multi-step UI actions. An escaped-backslash Fastmail image-proxy bypass relies on an allow-listed user.fm domain to
[reveal when an email is viewed](https://thehackernews.com/2025/03/cybercriminals-exploit-css-to-evade.html)
.

Heyes separately demonstrated a Proton Mail vector that exposed the recipient's IP address. Proton's
[current tracker-protection documentation](https://proton.me/support/email-tracker-protection)
says the service is designed to hide a user's personal IP address and exact email-open time.

The accompanying
[public repository](https://github.com/portswigger/css-the-bomb-inside-your-inbox)
contains PoCs for the disclosed techniques. The defensive guidance starts with strict isolation, then character allow lists for CSS validation, checks for CSS gadgets before allowing custom attributes, blocking select menus and dangerous selectors, and preventing attacker-controlled image requests and allow-listed domains.