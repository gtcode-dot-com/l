---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-17T22:16:29.791009+00:00'
exported_at: '2026-10-17T22:16:31.176037+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html
structured_data:
  about: []
  author: ''
  description: UAT-11985 targets Taiwan research affiliates with fake event invites
    that lead to AitM pages designed to capture Google passwords and MFA codes.
  headline: UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates
    With Google AitM Phishing
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates With
  Google AitM Phishing
updated_at: '2026-10-17T22:16:29.791009+00:00'
url_hash: 7ca539292393b0528fe92e12c57689d642323f55
---

Cybersecurity researchers have disclosed details of an advanced persistent threat (APT) spear-phishing campaign that has targeted individuals affiliated with Taiwan research organizations to direct victims to an adversary-in-the-middle (AitM) phishing framework designed to harvest their Google account credentials and multi-factor authentication (MFA) codes.

The activity is being tracked by Cisco Talos under the moniker
**UAT-11985**
, describing it as likely fueled by artificial intelligence (AI)-assisted content generation so as to quickly craft bespoke lures aimed at different targets within the confines of a common social engineering framework. The campaign was first observed in mid-2026.

"The operation leveraged legitimate public event themes and impersonated reputable academic and policy institutions to establish credibility," Talos researcher Joey Chen
[said](https://blog.talosintelligence.com/uat-11985/)
in an analysis.

"Beyond traditional email phishing, the actor incorporated QR code phishing (quishing) techniques by modifying legitimate event posters with malicious QR codes, expanding the attack surface beyond email recipients to secondary victims who may encounter printed materials."

Central to the operation is the use of legitimate or plausible public event information in spear-phishing emails and embedding within them a URL that points to attacker-controlled infrastructure, while hovering over the hyperlink displays a legitimate-looking Google Forms URL.

These invitation emails feature nearly identical syntactic structures despite the breadth of geopolitical topics being discussed, indicating the content was mass-produced from a reusable prompt template rather than painstakingly crafted for each target.

Specifically, the emails follow a three-part structure -

* The opening section offers a "polished (but overly elaborate) description" of the geopolitical or policy context.
* The second section is tailored to the recipient and paints them in a flattering light in an attempt to trigger engagement.
* The third and final section provides details of event logistics, including the topic, date, venue, and registration instructions.

The threat actor has been found to impersonate legitimate Taiwan-based institutions like the Taiwan European Union Centre, NCCU Institute of International Relations, and Taiwan Research Institute, fabricating the sender identities to make the messages appear more convincing.

"Taken together, the reuse of an almost-identical narrative structure, rhetorical style, personalized flattery, institutional impersonation, and deceptive registration mechanism strongly suggests a coordinated and carefully targeted spear-phishing campaign rather than three independent invitations," Talos said.

In a subset of cases, the phishing emails incorporate legitimate event posters scraped from legitimate websites, but with the QR codes modified to trick victims into scanning the malicious QR code to "register" for the event.

The phishing site imitates the look of a legitimate Google Form, but the primary goal of the site is to serve a pop-up that prompts the victim to sign-in with their Google account to complete the form. Doing so takes them to a bogus site featuring a spoofed Google login panel to capture their credentials and authentication challenges.

The pixel-perfect replica site is an adversary-in-the-middle (AitM) proxy that uses obfuscated JavaScript to gather and exfiltrate the entered information in real-time over a WebSocket connection, while simultaneously forwarding it to legitimate Google authentication servers.

Prior to establishing the WebSocket connection, the JavaScript payload collects device and browser information, including the locale, user agent, screen dimensions, and mobile-device status, which are then reported to the command-and-control (C2) server via a "google\_login\_start" request.

When the victim submits the password, the phishing page transmits the password, along with the account identifier and browser user-agent information, to the actor's HTTP C2 server through a "google\_login\_check" request. The threat actor's server, placed in an AitM position, then forwards the credentials to the actual Google authentication service.

"The spoofed Google login panels only support Simplified Chinese (zh-CN), Traditional Chinese (zh-TW), and English locales, with region detection based on the victim's browser 'navigator.languages,' strongly suggesting targeting of Chinese-speaking users," Chen explained.

"By deliberately splitting one-shot uploads with POST requests from low-latency state updates with WebSocket connection, the threat actor has engineered a seamless credential-harvesting relay. This allows the threat actor to mirror Google's dynamic authentication state in real time, ultimately achieving full account takeover without raising the victim's suspicion."

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.