---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-21T00:03:11.544053+00:00'
exported_at: '2025-12-21T00:03:15.596031+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html
structured_data:
  about: []
  author: ''
  description: A Russia-aligned threat group uses Microsoft 365 device code phishing
    to steal credentials and take over accounts, tracked since September 2025.
  headline: Russia-Linked Hackers Use Microsoft 365 Device Code Phishing for Account
    Takeovers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Russia-Linked Hackers Use Microsoft 365 Device Code Phishing for Account Takeovers
updated_at: '2025-12-21T00:03:11.544053+00:00'
url_hash: 5bfa18fab150c1ea3910f9ed10af986150dca1c4
---

**

Dec 19, 2025
**

Ravie Lakshmanan

Cybersecurity / Cloud Security

A suspected Russia-aligned group has been attributed to a phishing campaign that employs device code authentication workflows to steal victims' Microsoft 365 credentials and conduct account takeover attacks.

The activity, ongoing since September 2025, is being tracked by Proofpoint under the moniker
**UNK\_AcademicFlare**
.

The attacks involve using compromised email addresses belonging to government and military organizations to strike entities within government, think tanks, higher education, and transportation sectors in the U.S. and Europe.

"Typically, these compromised email addresses are used to conduct benign outreach and rapport building related to the targets' area of expertise to ultimately arrange a fictitious meeting or interview," the enterprise security company
[said](https://www.proofpoint.com/us/blog/threat-insight/access-granted-phishing-device-code-authorization-account-takeover)
.

As part of these efforts, the adversary claims to share a link to a document that includes questions or topics for the email recipient to review before the meeting. The URL points to a Cloudflare Worker URL that mimics the compromised sender's Microsoft OneDrive account and instructs the victim to copy the provided code and click "Next" to access the supposed document.

However, doing so redirects the user to the legitimate Microsoft device code login URL, where, once the previously provided code is entered, it causes the service to generate an access token that can then be recovered by the three actors to take control of the victim account.

Device code phishing was
[documented](https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html)
in detail by both Microsoft and Volexity in February 2025, attributing the use of the attack method to Russia-aligned clusters such as Storm-2372, APT29, UTA0304, and UTA0307. Over the past couple of months,
[Amazon Threat Intelligence](https://thehackernews.com/2025/08/amazon-disrupts-apt29-watering-hole.html)
and
[Volexity](https://thehackernews.com/2025/12/weekly-recap-usb-malware-react2shell.html#:~:text=Russian%20Hackers%20Spoof%20European%20Security%20Events%20in%20Phishing%20Wave)
have warned of continued attacks mounted by Russian threat actors that abuse the device code authentication flow.

Proofpoint said UNK\_AcademicFlare is likely a Russia-aligned threat actor given its targeting of Russia-focused specialists at multiple think tanks and Ukrainian government and energy sector organizations.

Data from the company shows that multiple threat actors, both state-aligned and financially-motivated, have latched onto the phishing tactic to deceive users into giving them access to Microsoft 365 accounts. This includes an e-crime group named TA2723 that has used salary-related lures in phishing emails to direct users to fake landing pages and trigger device code authorization.

The October 2025 campaign is assessed to have been fueled by the ready availability of crimeware offerings like the Graphish phishing kit and red-team tools such as
[SquarePhish](https://github.com/secureworks/SquarePhish)
.

"Similar to SquarePhish, the tool is designed to be user-friendly and does not require advanced technical expertise, lowering the barrier for entry and enabling even low-skilled threat actors to conduct sophisticated phishing campaigns," Proofpoint said. "The ultimate objective is unauthorized access to sensitive personal or organizational data, which can be exploited for credential theft, account takeover, and further compromise."

To counter the risk posed by device code phishing, the best option is to create a Conditional Access policy using the Authentication Flows condition to block device code flow for all users. If that's not feasible, it's advised to use a policy that uses an allow-list approach to allow device code authentication for approved users, operating systems, or IP ranges.