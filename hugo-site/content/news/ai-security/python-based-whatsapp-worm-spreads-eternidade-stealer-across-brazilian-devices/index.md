---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-20T00:00:06.705930+00:00'
exported_at: '2025-11-20T00:00:09.511196+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html
structured_data:
  about: []
  author: ''
  description: Eternidade Stealer spreads via WhatsApp hijacking, using Python scripts
    and IMAP-driven C2 updates to target Brazilian users.
  headline: Python-Based WhatsApp Worm Spreads Eternidade Stealer Across Brazilian
    Devices
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Python-Based WhatsApp Worm Spreads Eternidade Stealer Across Brazilian Devices
updated_at: '2025-11-20T00:00:06.705930+00:00'
url_hash: 643e7abaecbfcd61058b4db9bff0bb325e19ee9c
---

Cybersecurity researchers have disclosed details of a new campaign that leverages a combination of social engineering and WhatsApp hijacking to distribute a Delphi-based banking trojan named
**Eternidade Stealer**
as part of attacks targeting users in Brazil.

"It uses Internet Message Access Protocol (IMAP) to dynamically retrieve command-and-control (C2) addresses, allowing the threat actor to update its C2 server," Trustwave SpiderLabs researchers Nathaniel Morales, John Basmayor, and Nikita Kazymirskyi
[said](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/spiderlabs-ids-new-banking-trojan-distributed-through-whatsapp/)
in a technical breakdown of the campaign shared with The Hacker News.

"It is distributed through a WhatsApp worm campaign, with the actor now deploying a Python script, a shift from previous PowerShell-based scripts to hijack WhatsApp and spread malicious attachments.

The findings come close on the heels of another campaign dubbed
[Water Saci](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html)
that has targeted Brazilian users with a worm that propagates via WhatsApp Web known as SORVEPOTEL, which then acts as a conduit for
[Maverick](https://www.bluevoyant.com/blog/advanced-banking-trojan-maverick-uses-whatsapp-to-prey-on-brazilian-users)
, a .NET banking trojan that's assessed to be an evolution of a .NET banking malware dubbed
[Coyote](https://thehackernews.com/2025/07/new-coyote-malware-variant-exploits.html)
.

The Eternidade Stealer cluster is part of a broader activity that has abused the ubiquity of WhatsApp in the South American country to compromise target victim systems and use the messaging app as a propagation vector to launch large-scale attacks against Brazilian institutions.

Another notable trend is the
[continued](https://thehackernews.com/2023/05/alert-brazilian-hackers-targeting-users.html)
[preference](https://thehackernews.com/2024/03/new-banking-trojan-chavecloak-targets.html)
for
[Delphi-based malware](https://thehackernews.com/2024/07/experts-warn-of-mekotio-banking-trojan.html)
for threat actors targeting Latin America, largely driven not only because of its technical efficiency but also by the fact that the programming language was taught and used in software development in the region.

The starting point of the attack is an obfuscated Visual Basic Script, which features comments written mainly in Portuguese. The script, once executed, drops a batch script that's responsible for delivering two payloads, effectively forking the infection chain into two -

* A Python script that triggers WhatsApp Web-based dissemination of the malware in a worm-like fashion
* An MSI installer that makes use of an AutoIt script to launch Eternidade Stealer

The Python script, similar to SORVEPOTEL, establishes communication with a remote server and leverages the open-source project
[WPPConnect](https://github.com/wppconnect-team/wppconnect)
to automate the sending of messages in hijacked accounts via WhatsApp. To do this, it harvests a victim's entire contact list, while filtering out groups, business contacts, and broadcast lists.

The malware then proceeds to capture, for each contact, their WhatsApp phone number, name, and information signaling whether they are a saved contact. This information is sent to the attacker-controlled server over an HTTP POST request. In the final stage, a malicious attachment is sent to all the contacts in the form of a malicious attachment by making use of a messaging template and populating certain fields with time-based greetings and contact names.

The second leg of the attack commences with the MSI installer dropping several payloads, including an AutoIt script that checks to see if the compromised system is based in Brazil by inspecting whether the operating system language is Brazilian Portuguese. If not, the malware self-terminates. This indicates a hyper-localized targeting effort on the part of the threat actors.

The script subsequently scans running processes and registry keys to ascertain the presence of installed security products. It also profiles the machine and sends the details to a command-and-control (C2) server. The attack culminates with the malware injecting the Eternidade Stealer payload into "svchost.exe" using process hollowing.

A Delphi-based credential stealer, Eternidade continuously scans active windows and running processes for strings related to banking portals, payment services, and cryptocurrency exchanges and wallets, such as Bradesco, BTG Pactual, MercadoPago, Stripe, Binance, Coinbase, MetaMask, and Trust Wallet, among others.

"Such a behavior reflects a classic banker or overlay-stealer tactic, where malicious components lie dormant until the victim opens a targeted banking or wallet application, ensuring the attack triggers only in relevant contexts and remains invisible to casual users or sandbox environments," the researchers said.

Once a match is found, it contacts a C2 server, details for which are fetched from an inbox linked to a terra.com[.]br email address, mirroring a tactic recently adopted by Water Saci. This allows the threat actors to update their C2, maintain persistence, and evade detections or takedowns. In the event that the malware is unable to connect to the email account using hard-coded credentials, it uses a fallback C2 address embedded in the source code.

As soon as a successful connection with the server is established, the malware awaits incoming messages that are then processed and executed on the infected hosts, enabling the attackers to record keystrokes, capture screenshots, and steal files. Some of the notable commands are listed below -

* <|OK|>, to collect system information
* <|PING|>, to monitor user activity and report the currently active window
* <|PedidoSenhas|>, to send a custom overlay for credential theft based on the active window

Trustwave said an analysis of threat actor infrastructure led to the discovery of two panels, one for managing the Redirector System and another login panel, likely used to monitor infected hosts. The Redirector System contains logs showing the total number of visits and blocks for connections attempting to reach the C2 address.

While the system only permits access to machines located in Brazil and Argentina, blocked connections are redirected to "google[.]com/error." Statistics recorded on the panel show that 452 out of 454 visits were blocked due to the geofencing restrictions. Only the remaining two visits are said to have been redirected to the campaign's targeted domain.

Of the 454 communication records, 196 connections originated from the U.S., followed by the Netherlands (37), Germany (32), the U.K. (23), France (19), and Brazil (3). The Windows operating system accounted for 115 connections, although panel data indicates that connections also came from macOS (94), Linux (45), and Android (18).

"Although the malware family and delivery vectors are primarily Brazilian, the possible operational footprint and victim exposure are far more global," Trustwave said. "Cybersecurity defenders should remain vigilant for suspicious WhatsApp activity, unexpected MSI or script executions, and indicators linked to this ongoing campaign."