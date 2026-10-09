---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T22:54:58.372825+00:00'
exported_at: '2026-10-06T22:55:00.028959+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html
structured_data:
  about: []
  author: ''
  description: Star Blizzard uses fake event invites and RedFlick scheduled tasks
    to install CosmicPulse on Windows systems tied to Ukraine.
  headline: Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites
    to Deliver Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites to
  Deliver Backdoor
updated_at: '2026-10-06T22:54:58.372825+00:00'
url_hash: 643a969864727d3f41c3e627575a5d53812b180d
---

Russian state hackers known as
**Star Blizzard**
have been using fake event invitations to trick people into installing a backdoor on their Windows computers, according to Microsoft.

The campaigns, aimed at people and organizations tied to Ukraine, have affected more than 100 organizations since January, mostly in the U.S. and U.K. At least one computer was infected, but the number of breached organizations has not been disclosed.

Security agencies in the U.S., U.K., Australia, Canada and New Zealand
[said in December 2023](https://thehackernews.com/2023/12/microsoft-warns-of-coldrivers-evolving.html)
that Star Blizzard almost certainly works under Center 18 of Russia's Federal Security Service (FSB). The group has long stolen email passwords by posing as people its targets know.

By 2023, it had already used
[fake conference and event invitations](https://www.ncsc.gov.uk/news/star-blizzard-continues-spear-phishing-campaigns)
as bait, often exchanging messages with a target before sending a malicious link.

Microsoft counted at least
[13 larger campaigns](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)
this year, each with tens to hundreds of emails, on top of the group's usual targeted phishing.

Since March, those campaigns have used email accounts on WordPress and cPanel websites, which Microsoft is highly confident the group hacked for that purpose. Before, the group mostly used free email services such as Proton and Microsoft consumer accounts.

In 2025, the group delivered its malware through fake CAPTCHA pages that tricked targets into running commands themselves, a method known as
[ClickFix](https://thehackernews.com/2025/10/google-identifies-three-new-russian.html)
. This year it switched to a method Microsoft calls RedFlick. RedFlick uses scheduled tasks, jobs that Windows runs automatically, to install a backdoor named CosmicPulse.

The invitations name well-known think tanks or NGOs as hosts, such as Chatham House and the Atlantic Council. Many emails are written to appear to come from within the target's organization.

The first email usually carries no attachment. If the target replies, the group sends a password-protected RAR or ZIP archive, with the password shown in an image.

The first campaigns, in January and February, posed as Ukrainian authorities and sent fake tax audit and fine notices to users of the Ukrainian email service Ukr.net. Later lures included a water shutdown notice for hotels in Kyiv and a payment notice for staff at an international financial organization.

One March campaign worked differently. People who replied to an Atlantic Council-themed invitation got a link to DarkSword, an iPhone exploit kit, instead of the Windows backdoor, according to Microsoft.

Proofpoint reported Atlantic Council-themed emails from the group
[in March](https://thehackernews.com/2026/03/ta446-deploys-leaked-darksword-ios.html)
, along with a sharp rise in its email volume.

[Trellix](https://www.trellix.com/advanced-research-center/threat-reports/secondsight-threat-hunting-report-september-2026/)
found 4 such emails sent on March 26. Its confidence that the emails led to DarkSword is medium, because the exploit pages were offline and no exploit code was recovered.

### How the Backdoor Gets In

Microsoft traced several versions of the infection chain. In all of them, a shortcut (LNK) file disguised as a PDF initiates the attack, and a Windows Installer (MSI) package sets up scheduled tasks.

Opening the shortcut quietly runs commands that fetch the installer from a remote server. In January, a hidden script used the SSH program to download it. In July, the shortcut downloaded a PDF with a hidden command that tries to fetch the installer.

In the version seen in April, the installer created 3 scheduled tasks named to look like normal network components:

* Internet Quality Test Connection
* Network Configuration Manager
* System Health Monitor

The first task sends the computer name and user name to the group's command-and-control (C2) server and can run more code from a remote location. The second sets up WebDAV, a Windows feature that opens a web address as if it were a folder. The third uses control.exe, the Windows Control Panel program, to run the next stage from the C2 server.

The next stage is a downloader disguised as a Control Panel item. It installs CosmicPulse, a Python-based backdoor. The downloader is the one earlier reports called NOROBOT or
[BAITSWITCH](https://thehackernews.com/2025/09/new-coldriver-malware-campaign-joins-bo.html)
.

Microsoft says these techniques overlap with a June campaign,
[reported by Digital Security Lab Ukraine](https://dslua.org/publications/spearphishing-via-fake-urc-2026-invitations-targets-ukrainian-csos/)
, that targeted Ukrainian civil society organizations. That campaign used fake invitations to the Ukraine Recovery Conference. The lab did not name the attackers and could not recover the final payload.

Two indicators appear in both Microsoft's list and the June report, a comparison by The Hacker News found: the IP address 103.160.59[.]97 and the domain secure-dns-hub[.]com. Sharing them does not by itself show that the same group ran both campaigns.

### What Defenders Can Check

Microsoft published hunting queries and indicators for the campaigns, with advice for government bodies, NGOs, and think tanks that work on or support Ukraine policy. It also notifies customers it sees as targeted or compromised.

One domain, secure-dns-hub[.]com, was still in use when Microsoft published the report on September 29, according to the company.

Organizations likely to be targeted can take these steps:

* Check sender addresses. In these campaigns, the real organization's name appears before the @ sign rather than in the domain. When in doubt, contact the sender through a phone number or email address you already know.
* Search for the 3 scheduled task names above and for the Microsoft Defender detections Trojan:Script/RedFlick and Backdoor:Python/CosmicPulse.
* Widen the time range of Microsoft's 3 Defender XDR hunting queries, which look back only 7 days as published. Defender's advanced hunting keeps up to
  [30 days of raw data](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview)
  , so checking back to January needs logs kept longer, for example in Microsoft Sentinel.
* Block or limit outbound SSH connections the business does not need. The January version used SSH to fetch its installer.
* If you use Microsoft Defender, turn on the attack surface reduction rules that block rare, new, or untrusted executable files and obfuscated scripts.
* Use phishing-resistant sign-in methods. The group still runs password phishing with Evilginx, a tool that can also steal session cookies to get around two-factor authentication.
* Update iPhones to iOS 26.3 or later, which fixes all 6 flaws DarkSword uses, and turn on Lockdown Mode where that is not yet possible, Trellix advises.

Microsoft's public report does not list specific cleanup steps for a computer where the tasks are found. Defender XDR customers can check the company's threat analytics reports, which include recommended response actions.