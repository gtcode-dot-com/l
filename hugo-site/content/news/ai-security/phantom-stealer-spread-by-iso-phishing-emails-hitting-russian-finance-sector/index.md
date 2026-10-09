---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-16T00:03:27.991414+00:00'
exported_at: '2025-12-16T00:03:30.895789+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/phantom-stealer-spread-by-iso-phishing.html
structured_data:
  about: []
  author: ''
  description: Researchers report phishing emails in Russia using ISO attachments
    to deploy Phantom Stealer against finance and related sectors.
  headline: Phantom Stealer Spread by ISO Phishing Emails Hitting Russian Finance
    Sector
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/phantom-stealer-spread-by-iso-phishing.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Phantom Stealer Spread by ISO Phishing Emails Hitting Russian Finance Sector
updated_at: '2025-12-16T00:03:27.991414+00:00'
url_hash: eb26fdc40f9cfb22ec03cfdfc1a57bd727769d37
---

Cybersecurity researchers have disclosed details of an active phishing campaign that's targeting a wide range of sectors in Russia with phishing emails that deliver
[Phantom Stealer](https://thehackernews.com/2025/09/noisy-bear-targets-kazakhstan-energy.html#cyber-attacks-reported-against-russia)
via malicious ISO optical disc images.

The activity, codenamed Operation MoneyMount-ISO by Seqrite Labs, has primarily singled out finance and accounting entities, with those in the procurement, legal, payroll verticals emerging as secondary targets.

"This campaign employs a fake payment confirmation lure to deliver the Phantom information-stealing malware through a multi-stage attachment chain," the cybersecurity company
[said](https://www.seqrite.com/blog/operation-moneymount-iso-deploying-phantom-stealer-via-iso-mounted-executables/)
.

The infection chain begins with a phishing email that masquerades as legitimate financial communications, urging recipients to confirm a recent bank transfer. Attached to the email is a ZIP archive that claims to contain additional details, but, instead, contains an ISO file that, when launched, mounts on the system as a virtual CD drive.

The ISO image ("Подтверждение банковского перевода.iso" or "Bank transfer confirmation.iso") serves as an executable that's designed to launch Phantom Stealer by means of an embedded DLL ("CreativeAI.dll").

Phantom Stealer is capable of extracting data from cryptocurrency wallet browser extensions installed in Chromium-based browsers and desktop wallet apps, as well as grab files, Discord authentication tokens, and browser-related passwords, cookies, and credit card details.

It also monitors clipboard content, logs keystrokes, and runs a series of checks to detect virtualized, sandboxed, or analysis environments, and if so, aborts its execution. Data exfiltration is achieved via a Telegram bot or to an attacker-controlled Discord webhook. On top of that, the stealer enables file transfer to an FTP server.

In recent months, Russian organizations, mainly human resources and payroll departments, have also been targeted by phishing emails that employ lures related to bonuses or internal financial policies to deploy a previously undocumented implant named DUPERUNNER that loads
[AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
, an open-source command-and-control (C2) framework.

Dubbed
[DupeHike](https://www.seqrite.com/blog/operation-dupehike-ung0902-targets-russian-employees-with-duperunner-and-adaptixc2/)
, the campaign has been attributed to a threat cluster named UNG0902.

"The ZIP has been used as a preliminary source of spear-phishing-based infection containing decoys with PDF and LNK extension, which downloads the implant DUPERUNNER, which finally executes the Adaptix C2 Beacon," Seqrite said.

The LNK file ("Документ\_1\_О\_размере\_годовой\_премии.pdf.lnk" or "Document\_1\_On\_the\_amount\_of\_the\_annual\_bonus.pdf.lnk"), in turn, proceeds to download DUPERUNNER from an external server using "powershell.exe." The primary responsibility of the implant is to retrieve and display a decoy PDF and launch AdaptixC2 by injecting it into a legitimate Windows process like "explorer.exe," "notepad.exe," and "msedge.exe."

Other phishing campaigns have taken aim at finance, legal, and aerospace sectors in Russia to distribute
[Cobalt Strike](https://www.seqrite.com/blog/operation-frostbeacon-multi-cluster-cobalt-strike-campaign-targets-russia/)
and malicious tools like Formbook, DarkWatchman, and PhantomRemote that are capable of data theft and hands-on keyboard control. The email servers of compromised Russian companies are used to send the spear-phishing messages.

French cybersecurity company Intrinsec has attributed the intrusion set targeting the Russian aerospace industry to hacktivists aligned with Ukrainian interests. The activity, detected between June and September 2025, shares overlaps with
[Hive0117](https://thehackernews.com/2025/05/darkwatchman-sheriff-malware-hit-russia.html)
,
[Operation CargoTalon](https://thehackernews.com/2025/07/cyber-espionage-campaign-hits-russian.html)
, and
[Rainbow Hyena](https://thehackernews.com/2025/07/weekly-recap-sharepoint-0-day-chrome.html#:~:text=Rainbow%20Hyena%20Goes%20After%20Russian%20Firms)
(aka Fairy Trickster, Head Mare, and PhantomCore).

Some of these efforts have also been found to redirect users to phishing login pages hosted on the InterPlanetary File System (
[IPFS](https://thehackernews.com/2022/11/several-cyber-attacks-observed.html)
) and Vercel, designed to steal credentials associated with Microsoft Outlook and Bureau 1440, a Russian aerospace company.

"The campaigns observed between June and September 2025 [...] aimed at compromising entities actively cooperating with Russia's army amidst the current conflict with Ukraine, largely assessed by the Western sanctions imposed on them," Intrinsec
[said](https://www.intrinsec.com/campaigns-targeting-the-aerospace-industry-in-russia/)
.