---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-04T00:03:08.427333+00:00'
exported_at: '2025-12-04T00:03:10.707859+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html
structured_data:
  about: []
  author: ''
  description: Water Saci and RelayNFC drive advanced Brazil-targeted attacks using
    WhatsApp worm tactics and real-time NFC payment theft.
  headline: Brazil Hit by Banking Trojan Spread via WhatsApp Worm and RelayNFC NFC
    Relay Fraud
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Brazil Hit by Banking Trojan Spread via WhatsApp Worm and RelayNFC NFC Relay
  Fraud
updated_at: '2025-12-04T00:03:08.427333+00:00'
url_hash: ce46c515511b477f5614057711782c27faecf586
---

The threat actor known as
**[Water Saci](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html)**
is actively evolving its tactics, switching to a sophisticated, highly layered infection chain that uses HTML Application (HTA) files and PDFs to propagate via WhatsApp a worm that deploys a banking trojan in attacks targeting users in Brazil.

The latest wave is characterized by the attackers shifting from PowerShell to a Python-based variant that spreads the malware in a worm-like manner over WhatsApp Web.

"Their new multi-format attack chain and possible use of artificial intelligence (AI) to convert propagation scripts from PowerShell to Python exemplifies a layered approach that has enabled Water Saci to bypass conventional security controls, exploit user trust across multiple channels, and ramp up their infection rates," Trend Micro researchers Jeffrey Francis Bonaobra, Sarah Pearl Camiling, Joe Soares, Byron Gelera, Ian Kenefick, and Emmanuel Panopio
[said](https://www.trendmicro.com/en_us/research/25/l/water-saci.html)
.

In these attacks, users receive messages from trusted contacts on WhatsApp, urging them to interact with malicious PDF or HTA attachments and activate the infection chain and ultimately drop a banking trojan that can harvest sensitive data. The PDF lure instructs victims to update Adobe Reader by clicking on an embedded link.

Users who receive HTA files are deceived into executing a Visual Basic Script immediately upon opening, which then runs PowerShell commands to fetch next-stage payloads from a remote server, an MSI installer for the trojan and a Python script that's responsible for spreading the malware via WhatsApp Web.

"This newly observed variant allows for broader browser compatibility, object-oriented code structure, enhanced error handling, and faster automation of malware delivery through WhatsApp Web," Trend Micro said. "Together, these changes make propagation faster, more resilient to failure, and easier to maintain or extend."

The MSI installer, for its part, serves as a conduit for delivering the banking trojan using an AutoIt script. The script also runs checks to ensure that only one instance of the trojan is running at any given point of time. It accomplishes this by verifying the presence of a marker file named "executed.dat." If it does not exist, the script creates the file and notifies an attacker-controlled server ("manoelimoveiscaioba[.]com").

Other AutoIt artifacts uncovered by Trend Micro have also been found to verify whether the Windows system language is set to Portuguese (Brazil), proceeding further to scan the infected system for banking-related activity only if this criteria is met. This includes checking for folders related to major Brazilian banking applications, security, and anti-fraud modules, such as Bradesco, Warsaw, Topaz OFD, Sicoob, and Itaú.

It's worth noting Latin America (LATAM)-focused banking trojans like
[Casbaneiro](https://thehackernews.com/2023/07/casbaneiro-banking-malware-goes-under.html)
(aka Metamorfo and Ponteiro) have
[incorporated similar features](https://thehackernews.com/2025/06/malicious-browser-extensions-infect-722.html)
as far back as 2019. Furthermore, the script analyzes the user's Google Chrome browsing history to search visits to banking websites, specifically a hard-coded list comprising Santander, Banco do Brasil, Caixa Econômica Federal, Sicredi, and Bradesco.

The script then proceeds to another critical reconnaissance step that involves checking for installed antivirus and security software, as well as harvesting detailed system metadata. The main functionality of the malware is to monitor open windows and extract their window titles to compare them against a list of banks, payment platforms, exchanges, and cryptocurrency wallets.

If any of these windows contain keywords related to targeted entities, the script looks for a TDA file dropped by the installer and decrypts and injects it into a hollowed "svchost.exe" process, following which the loader searches for an additional DMP file containing the banking trojan.

"If a TDA file is present, the AutoIt script decrypts and loads it as an intermediate PE loader (Stage 2) into memory," Trend Micro explained. "However, if only a DMP file is found (no TDA present), the AutoIt script bypasses the intermediate loader entirely and loads the banking trojan directly into the AutoIt process memory, skipping the process hollowing step and running as a simpler two-stage infection."

Persistence is achieved by constantly keeping tabs on the newly spawned "svchost.exe" process. Should the process be terminated, the malware starts afresh and waits to re-inject the payload the next time the victim opens a browser window for a financial service that's targeted by Water Saci.

The attacks stand out for a major tactical shift. The banking trojan deployed is not Maverick, but rather a malware that exhibits structural and behavioral continuity with Casbaneiro. This assessment is based on the AutoIt-based delivery and loader mechanism employed, as well as the window title monitoring, Registry-based persistence, and IMAP-based fallback command-and-control (C2) mechanism.

Once launched, the trojan carries out "aggressive" anti-virtualization checks to sidestep analysis and detection, and gathers host information through Windows Management Instrumentation (
[WMI](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
) queries. It makes Registry modifications to set up persistence and establishes contact with a C2 server ("serverseistemasatu[.]com") to send the collected details and receive backdoor commands that grant remote control over the infected system.

Besides scanning the titles of active windows to identify whether the user is interacting with banking or cryptocurrency platforms, the trojan forcibly terminates several browsers to force victims to reopen banking sites under "attacker-controlled conditions." Some of the supported features of the trojan are listed below -

* Send system information
* Enable keyboard capture
* Start/stop screen capture
* Modify screen resolution
* Simulate mouse movements and clicks
* Perform file operations
* Upload/download files
* Enumerate windows, and
* Create fake banking overlays to capture credentials and transaction data

The second aspect of the campaign is the use of a Python script, an enhanced version of its PowerShell predecessor, to enable malware delivery to every contact via WhatsApp Web sessions using the Selenium browser automation tool.

There is "compelling" evidence to suggest that Water Saci may have used a large language model (LLMs) or code-translation tool to port their propagation script from PowerShell to Python, given the functional similarities between the two versions and the inclusion of emojis in console outputs.

"The Water Saci campaign exemplifies a new era of cyber threats in Brazil, where attackers exploit the trust and reach of popular messaging platforms like WhatsApp to orchestrate large-scale, self-propagating malware campaigns," Trend Micro said.

"By weaponizing familiar communication channels and employing advanced social engineering, threat actors are able to swiftly compromise victims, bypass traditional defenses, and sustain persistent banking trojan infections. This campaign demonstrates how legitimate platforms can be transformed into powerful vectors for malware delivery and underscores the growing sophistication of cybercriminal operations in the region."

### Brazil Targeted by New RelayNFC Android Malware

The development comes as Brazilian banking users are also being targeted by a previously undocumented Android malware dubbed RelayNFC that's designed to carry out Near-Field Communication (
[NFC](https://thehackernews.com/2025/09/raton-android-malware-detected-with-nfc.html)
) relay attacks and siphon contactless payment data. The campaign has been running since early November 2025.

"RelayNFC implements a full real-time APDU relay channel, allowing attackers to complete transactions as though the victim's card were physically present," Cyble
[said](https://cyble.com/blog/relaynfc-nfc-relay-malware-targeting-brazil/)
in an analysis. "The malware is built using React Native and Hermes bytecode, which complicates static analysis and helps evade detection."

Primarily spread via phishing, the attack makes use of decoy Portuguese-language sites (e.g., "maisseguraca[.]site") to trick users into installing the malware under the pretext of securing their payment cards. The end goal of the campaign is to capture the victim's card details and relay them to attackers, who can then perform fraudulent transactions using the stolen data.

Like other NFC relay malware families such as
[SuperCard X](https://thehackernews.com/2025/04/supercard-x-android-malware-enables.html)
and
[PhantomCard](https://thehackernews.com/2025/08/new-android-malware-wave-hits-banking.html)
, RelayNFC operates as a reader that's designed to gather the card data by instructing the victim to tap their payment card on the device. Once the card data is read, the malware displays a message that prompts them to enter their 4- or 6-digit PIN. The captured information is then sent to the attacker's server through a WebSocket connection.

"When the attacker initiates a transaction from their POS-emulator device, the C&C server sends a specially crafted message of type 'apdu' to the infected phone," Cyble said. "This message contains a unique request ID, a session identifier, and the APDU command encoded as a hexadecimal string."

"Upon receiving this instruction, RelayNFC parses the packet, extracts the APDU data, and forwards it directly to the victim device's NFC subsystem, effectively acting as a remote interface to the physical payment card."

The cybersecurity company said its investigation also uncovered a separate phishing site ("test.ikotech[.]online") that distributes an APK file with a partial implementation of Host Card Emulation (HCE), indicating that the threat actors are experimenting with different NFC relay techniques.

Because HCE allows an Android device to emulate a payment card, the mechanism allows a victim's card interactions to be transmitted between a legitimate payment-of-sale (PoS) terminal and an attacker-controlled device, thereby facilitating a real-time NFC relay attack. The feature is assessed to be under development, as the APK file does not register the HCE service in the package manifest file.

"The RelayNFC campaign highlights the rapid evolution of NFC relay malware targeting payment systems, particularly in Brazil," the company said. "By combining phishing-driven distribution, React Native-based obfuscation, and real-time APDU relaying over WebSockets, the threat actors have created a highly effective mechanism for remote EMV transaction fraud."