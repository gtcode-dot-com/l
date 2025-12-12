---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-12T08:03:57.803088+00:00'
exported_at: '2025-12-12T08:04:00.313517+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters
structured_data:
  about: []
  author: ''
  description: Meet Rey, the Admin of ‘Scattered Lapsus$ Hunters’
  headline: Meet Rey, the Admin of ‘Scattered Lapsus$ Hunters’
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Meet Rey, the Admin of ‘Scattered Lapsus$ Hunters’
updated_at: '2025-12-12T08:03:57.803088+00:00'
url_hash: ac6d73c3fda8e0919c90b0f5cfe2cf2fe28f0d07
---

A prolific cybercriminal group that calls itself “
**Scattered LAPSUS$ Hunters**
” has dominated headlines this year by regularly stealing data from and publicly mass extorting dozens of major corporations. But the tables seem to have turned somewhat for “Rey,” the moniker chosen by the technical operator and public face of the hacker group: Earlier this week, Rey confirmed his real life identity and agreed to an interview after KrebsOnSecurity tracked him down and contacted his father.

Scattered LAPSUS$ Hunters (SLSH) is thought to be an amalgamation of three hacking groups —
[**Scattered Spider**](https://krebsonsecurity.com/?s=scattered+spider)
,
[**LAPSUS$**](https://krebsonsecurity.com/?s=lapsus%24)
and
[**ShinyHunters**](https://krebsonsecurity.com/?s=shiny+hunters)
. Members of these gangs hail from many of the same chat channels on the
**Com**
, a mostly English-language cybercriminal community that operates across an ocean of Telegram and Discord servers.

In May 2025, SLSH members launched
[a social engineering campaign](https://krebsonsecurity.com/2025/10/shinyhunters-wage-broad-corporate-extortion-spree/)
that used voice phishing to trick targets into connecting a malicious app to their organization’s Salesforce portal. The group later launched a data leak portal that threatened to publish the internal data of three dozen companies that allegedly had Salesforce data stolen, including
**Toyota**
,
**FedEx**
,
**Disney/Hulu**
, and
**UPS**
.

![](https://krebsonsecurity.com/wp-content/uploads/2025/10/sf-extortionsite.png)

The new extortion website tied to ShinyHunters, which threatens to publish stolen data unless Salesforce or individual victim companies agree to pay a ransom.

Last week, the SLSH Telegram channel featured an offer to recruit and reward “insiders,” employees at large companies who agree to share internal access to their employer’s network for a share of whatever ransom payment is ultimately paid by the victim company.

SLSH has solicited insider access previously, but their latest call for disgruntled employees started making the rounds on social media at the same time news broke that the cybersecurity firm
**Crowdstrike**
had fired an employee for
[allegedly sharing screenshots of internal systems](https://techcrunch.com/2025/11/21/crowdstrike-fires-suspicious-insider-who-passed-information-to-hackers/)
with the hacker group (Crowdstrike said their systems were never compromised and that it has turned the matter over to law enforcement agencies).

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/slsh-insider.png)

The Telegram server for the Scattered LAPSUS$ Hunters has been attempting to recruit insiders at large companies.

Members of SLSH have traditionally used other ransomware gangs’ encryptors in attacks, including malware from ransomware affiliate programs like ALPHV/BlackCat, Qilin, RansomHub, and DragonForce. But last week, SLSH announced on its Telegram channel
[the release of their own ransomware-as-a-service operation](https://www.bleepingcomputer.com/news/security/meet-shinysp1d3r-new-ransomware-as-a-service-created-by-shinyhunters/)
called
**ShinySp1d3r**
.

The individual responsible for releasing the ShinySp1d3r ransomware offering is a core SLSH member who goes by the handle “Rey” and who is currently one of just three administrators of the SLSH Telegram channel. Previously, Rey was an
[administrator](https://web.archive.org/web/20241201110456/https://twitter.com/ReyXBF/status/1863177457450573835)
of the data leak website for
**Hellcat**
, a ransomware group that surfaced in late 2024 and was involved in attacks on companies including
**Schneider Electric**
,
**Telefonica**
, and
**Orange Romania**
.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/slsh-tg.png)

A recent, slightly redacted screenshot of the Scattered LAPSUS$ Hunters Telegram channel description, showing Rey as one of three administrators.

Also in 2024, Rey would take over as administrator of the
[most recent incarnation of BreachForums](https://web.archive.org/web/20241129001040/https://twitter.com/ReyXBF/status/1862288027579801821)
, an English-language cybercrime forum whose domain names have been seized on multiple occasions by the FBI and/or by international authorities. In April 2025, Rey
[posted on Twitter/X](https://web.archive.org/web/20250418062459/https://twitter.com/ReyXBF/status/1913116530658705661)
about another FBI seizure of BreachForums.

On October 5, 2025, the FBI
[announced](https://x.com/FBI/status/1977464345651982491)
it had once again seized the domains associated with BreachForums, which it described as a major criminal marketplace used by ShinyHunters and others to traffic in stolen data and facilitate extortion.

“This takedown removes access to a key hub used by these actors to monetize intrusions, recruit collaborators, and target victims across multiple sectors,” the FBI said.

Incredibly, Rey would make a series of critical operational security mistakes last year that provided multiple avenues to ascertain and confirm his real-life identity and location. Read on to learn how it all unraveled for Rey.

## WHO IS REY?

According to the cyber intelligence firm
**Intel 471**
, Rey was an active user on various
**BreachForums**
reincarnations over the past two years, authoring more than 200 posts between February 2024 and July 2025. Intel 471 says Rey previously used the handle “
**Hikki-Chan**
” on BreachForums, where their first post shared data allegedly stolen from the
**U.S. Centers for Disease Control and Prevention**
(CDC).

In that February 2024 post about the CDC, Hikki-Chan says they could be reached at the Telegram username
**@wristmug**
. In May 2024, @wristmug posted in a Telegram group chat called “Pantifan” a copy of an extortion email they said they received that included their email address and password.

The message that @wristmug cut and pasted appears to have been part of an
[automated email scam](https://krebsonsecurity.com/2018/07/sextortion-scam-uses-recipients-hacked-passwords/)
that claims it was sent by a hacker who has compromised your computer and used your webcam to record a video of you while you were watching porn. These missives threaten to release the video to all your contacts unless you pay a Bitcoin ransom, and they typically reference a real password the recipient has used previously.

“Noooooo,” the @wristmug account wrote in mock horror after posting a screenshot of the scam message. “I must be done guys.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/mustbedone.png)

A message posted to Telegram by Rey/@wristmug.

In posting their screenshot, @wristmug redacted the username portion of the email address referenced in the body of the scam message. However, they did not redact their previously-used password, and they left the domain portion of their email address (@proton.me) visible in the screenshot.

## O5TDEV

Searching on @wristmug’s rather unique 15-character password in the breach tracking service
**Spycloud**
finds it is known to have been used by just one email address:
**cybero5tdev@proton.me**
. According to Spycloud, those credentials were exposed at least twice in early 2024 when this user’s device was infected with an infostealer trojan that siphoned all of its stored usernames, passwords and authentication cookies (a finding that was
[initially revealed](https://www.kelacyber.com/blog/hellcat-hacking-group-unmasked-rey-and-pryx/)
in March 2025 by the cyber intelligence firm
**KELA**
).

Intel 471 shows the email address cybero5tdev@proton.me belonged to a BreachForums member who went by the username
**o5tdev**
. Searching on this nickname in Google brings up at least two website defacement archives showing that a user named o5tdev was previously involved in
[defacing sites with pro-Palestinian messages](https://web.archive.org/web/20251124165751/https://haxor.id/archive/mirror/179443)
. The screenshot below, for example, shows that 05tdev was part of a group called
**Cyb3r Drag0nz Team**
.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/hackedbyo5tdev.png)

Rey/o5tdev’s defacement pages. Image: archive.org.

A 2023 report from
**SentinelOne**
described Cyb3r Drag0nz Team as a hacktivist group with a history of launching DDoS attacks and cyber defacements as well as engaging in data leak activity.

“Cyb3r Drag0nz Team claims to have leaked data on over a million of Israeli citizens spread across multiple leaks,” SentinelOne
[reported](https://www.sentinelone.com/blog/hacktivism-in-the-israel-hamas-conflict-citizen-data-leaked-using-old-malware/)
. “To date, the group has released multiple .RAR archives of purported personal information on citizens across Israel.”

The cyber intelligence firm
**Flashpoint**
finds the Telegram user @05tdev was active in 2023 and early 2024, posting in Arabic on anti-Israel channels like “Ghost of Palestine” [full disclosure: Flashpoint is currently an advertiser on this blog].

## ‘I’M A GINTY’

Flashpoint shows that Rey’s Telegram account (ID7047194296) was particularly active in a cybercrime-focused channel called
**Jacuzzi**
, where this user shared several personal details, including that their father was an airline pilot. Rey claimed in 2024 to be 15 years old, and to have family connections to Ireland.

Specifically, Rey mentioned in several Telegram chats that he had Irish heritage, even posting a graphic that shows the prevalence of the surname “
**Ginty**
.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/imaginty.png)

Rey, on Telegram claiming to have association to the surname “Ginty.” Image: Flashpoint.

Spycloud indexed hundreds of credentials stolen from cybero5dev@proton.me, and those details indicate that Rey’s computer is a shared Microsoft Windows device located in Amman, Jordan. The credential data stolen from Rey in early 2024 show there are multiple users of the infected PC, but that all shared the same last name of Khader and an address in Amman, Jordan.

The “autofill” data lifted from Rey’s family PC contains an entry for a 46-year-old
**Zaid Khader**
that says his mother’s maiden name was Ginty. The infostealer data also shows Zaid Khader frequently accessed internal websites for employees of
**Royal Jordanian Airlines**
.

## MEET SAIF

The infostealer data makes clear that Rey’s full name is
**Saif Al-Din Khader**
. Having no luck contacting Saif directly, KrebsOnSecurity sent an email to his father Zaid. The message invited the father to respond via email, phone or Signal, explaining that his son appeared to be deeply enmeshed in a serious cybercrime conspiracy.

Less than two hours later, I received a Signal message from Saif, who said his dad suspected the email was a scam and had forwarded it to him.

“I saw your email, unfortunately I don’t think my dad would respond to this because they think its some ‘scam email,'” said Saif, who told me he turns 16 years old next month. “So I decided to talk to you directly.”

Saif explained that he’d already heard from European law enforcement officials, and had been trying to extricate himself from SLSH. When asked why then he was involved in releasing SLSH’s new ShinySp1d3r ransomware-as-a-service offering, Saif said he couldn’t just suddenly quit the group.

“Well I cant just dip like that, I’m trying to clean up everything I’m associated with and move on,” he said.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/hellcat.png)

The former Hellcat ransomware site. Image: Kelacyber.com

He also shared that ShinySp1d3r is just a rehash of Hellcat ransomware, except modified with AI tools. “I gave the source code of Hellcat ransomware out basically.”

Saif claims he reached out on his own recently to the Telegram account for
**Operation Endgame,**
the codename for an ongoing law enforcement operation
[targeting cybercrime services, vendors and their customers](https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/)
.

“I’m already cooperating with law enforcement,” Saif said. “In fact, I have been talking to them since at least June. I have told them nearly everything. I haven’t really done anything like breaching into a corp or extortion related since September.”

Saif suggested that a story about him right now could endanger any further cooperation he may be able to provide. He also said he wasn’t sure if the U.S. or European authorities had been in contact with the Jordanian government about his involvement with the hacking group.

“A story would bring so much unwanted heat and would make things very difficult if I’m going to cooperate,” Saif said. “I’m unsure whats going to happen they said they’re in contact with multiple countries regarding my request but its been like an entire week and I got no updates from them.”

Saif shared a screenshot that indicated he’d contacted Europol authorities late last month. But he couldn’t name any law enforcement officials he said were responding to his inquiries, and KrebsOnSecurity was unable to verify his claims.

“I don’t really care I just want to move on from all this stuff even if its going to be prison time or whatever they gonna say,” Saif said.