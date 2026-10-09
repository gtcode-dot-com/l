---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T00:49:31.744024+00:00'
exported_at: '2026-10-06T00:49:33.950667+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation
structured_data:
  about: []
  author: ''
  description: Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation
  headline: Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation
updated_at: '2026-10-06T00:49:31.744024+00:00'
url_hash: 8ccdf0e9d14d0af57125811c7a69d6e0df340c84
---

Authorities in the Netherlands have arrested a 24-year-old convicted cybercriminal on suspicion of aiding in data thefts and extortions by the prolific hacker group
**ShinyHunters**
. In the days immediately following the suspect’s arrest, remaining ShinyHunters members dramatically escalated their attacks, stealing highly sensitive data from the
**FBI**
and extorting the Russian ransomware group
**Cl0p**
.

According to three sources familiar with the matter, the Dutch man arrested by authorities this month is
**Pepijn van der Stap**
, a convicted cybercriminal from Almere and Lelystad in the Netherlands. Van der Stap was previously convicted in 2023 in connection with a string of data thefts and extortions that prosecutors said earned between €1.5 million and €2.7 million.

At his trial in late 2023, van der Stap admitted that he lived a Dr. Jekyll and Mr. Hyde existence, secretly using the hacker handle “
**Umbreon**
” to extort victims and post their data on English language hacking communities like the now-defunct RaidForums and Breached. By day, however, van der Stap was working as a software engineer at the Amsterdam-based cybersecurity startup
**Hadrian**
, while volunteering at the
**Dutch Institute for Vulnerability Disclosure**
(DIVD), a nonprofit security research group.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/umbreon-nl-rf.png)

Pepijn van der Stap’s alter ego “Umbreon” selling a database on RaidForums, offering information on 2.3 million people from The Netherlands in September 2021. This user’s avatar is a depiction of the Pokemon character Umbreon. Image: KELA.

Van der Stap confessed to his data theft and extortion activity, and was sentenced to four years in prison (one of which was suspended). During his trial, van der Stap opted to remain in custody for a time rather than at home, saying he could not find better treatment on the outside for his ongoing psychological issues, which he claimed included PTSD related to childhood trauma. He was released from prison in December 2025.

In an interview with KrebsOnSecurity on September 9, 2026, Van der Stap cast himself as a reformed hacker who was trying to turn his life around and make a positive contribution to society. Van der Stap is currently employed as offensive security lead at the Dutch company
**Neo Security**
, which did not respond to requests for comment.

Van der Stap said he was still dealing with civil lawsuits and restitution related to his previous cybercrime victims, and that he was trying his best to make amends. But not long after that interview, the Dutch hacker abruptly stopped replying to messages. Efforts by others close to him also repeatedly failed to elicit a response for the past two weeks.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/pvds-li.png)

The LinkedIn profile for Pepijn van der Stap.

According to two sources with knowledge of the matter, Van der Stap was arrested by Dutch authorities on or around September 16, and has been held in custody for questioning since. One source said a colleague of theirs personally witnessed Dutch authorities carting items out of Van der Stap’s residence.

Authorities in the Netherlands have been
[asking the public for help](https://www.politie.nl/nieuws/2026/september/7/11-stem-van-verdachte-odido-hack-te-horen-in-opsporing-verzocht.html)
in identifying the voice in a recorded telephone call from February 2026 in which a native Dutch-speaking ShinyHunters member social engineered their way into
**Odido**
, the nation’s largest mobile telecommunications provider. In that intrusion, ShinyHunters tricked an Odido employee into logging in at a spoofed website, and then used that access to steal data on more than 6.2 million Dutch people.

Responding to Dutch news media, ShinyHunters confirmed that the suspect in the audio clip is indeed a member of the hacker collective.

“Our team member has our full support – emotionally, mentally, and financially,” the hackers said. “Everything has been arranged, including a criminal defense lawyer. We do not look down on our staff and members; we take excellent care of them,” reads a statement ShinyHunters shared with
[NL Times](https://nltimes.nl/2026/09/08/shinyhunters-lawyer-police-release-audio-clip-suspect-odido-hack)
. It remains unclear if the Dutch police have matched the Odido caller to a confirmed real-life identity. The Dutch police unit handling the Odido incident did not respond to requests for comment.

The group also lashed out at the authorities in the Netherlands. “The Dutch police will need all the luck in the world – and everyone’s prayers – if they want to catch him before we carry out another large-scale data theft in the Netherlands,” the ShinyHunters statement said. “Frankly, the Dutch police are a big joke; they are incapable of doing anything. Incompetent. Irrelevant. Unimportant. Useless.”

## FBI, CL0P HACKS

Just days after sources say Van der Stap was detained by Dutch authorities, ShinyHunters claimed credit for an unusually brazen breach at the FBI’s job application site apply.fbijobs.gov. According to
[reporting from 404 Media](https://archive.is/IQgWr)
, the data stolen from the FBI site includes Social Security numbers and
[personal information](https://www.bbc.com/news/articles/cw62me2vlj07o)
on more than 5,000 officials.

404 Media and
[Reuters reported](https://archive.is/IQgWr)
the FBI data included each person’s job title or team, such as special agent, threat intake examiner, major cybercrimes unit, and those investigating cyber threats from foreign state-backed actors. Reuters examined documents shared by ShinyHunters and found they included sensitive psychiatric and medical files of FBI staff. The FBI issued
[a brief statement](https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii?utm_campaign=email-Immediate&amp;utm_medium=email&amp;utm_source=national-press-releases&amp;utm_content=%5B2249041%5D-%2Fnews%2Fpress-releases%2Ffbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii)
confirming the hack.

ShinyHunters said it gained access to the FBI site and other victims by exploiting a recently patched vulnerability (CVE-2026-35273) in
**PeopleSoft**
, a software-as-a-service platform from the software giant
**Oracle**
that is broadly used by companies to manage hiring and human resources, benefits and payroll. Oracle quickly issued a fix for the Peoplesoft vulnerability that ShinyHunters reportedly began exploiting as a zero-day in June, and at the time Mandiant released web application firewall rules intended for organizations who couldn’t apply the security update quickly enough.

But on Friday, BleepingComputer reported that ShinyHunters
[used a URL-encoding trick](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)
to bypass Mandiant’s suggested web application firewall rules designed to mitigate the threat from the PeopleSoft flaw. In
[a report](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft)
released Sept. 25, security experts at
**Mandiant**
and the
**Google Threat Intelligence Group**
(GTIG) confirmed that ShinyHunters had mass-exploited the PeopleSoft vulnerability to steal data from dozens of systems across a range of industries, including higher education, technology, healthcare, agriculture, transportation and government.

Van der Stap’s former hacker alias Umbreon was hidden in plain sight throughout the imagery ShinyHunters used to spread news about the FBI hack: The defacement image that ShinyHunters left behind on the hacked FBI jobs site included an ASCII art design featuring the Pokemon character Umbreon. The message at the top read, “This site has been seized by ShinyHunters. rooting your systems since ’19 ;)” The image appears identical to a defacement message ShinyHunters used in their
[2020 hack](https://reliaquest.com/blog/the-eeveelution-of-shinyhunters-from-data-leaks-to-extortions/)
of the English-language cybercrime community Hackforums.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/fbi-umbreon-sh.png)

The defacement message left by ShinyHunters on the FBI jobs site included an ASCII art rendition of the Pokemon character Umbreon. Image: Bleeping Computer.

Multiple sources close to the ShinyHunters investigation said the group’s recent risky attacks against the FBI and one of Russia’s most venerated ransomware groups amounted to a major pivot away from the more measured tenor of the hacking gang’s operations. Those sources said the sudden shift came about after ShinyHunters was taken over by
[a teenage cybercriminal from Amman, Jordan](https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/)
who goes by the nickname
**Rey**
and operates as part of a cybercrime group called
**ScatteredLapsussHunters**
(SLSH), which experts say is an amalgamation of three hacking groups —
[**Scattered Spider**](https://krebsonsecurity.com/?s=scattered+spider)
,
[**LAPSUS$**](https://krebsonsecurity.com/?s=lapsus%24)
and
[**ShinyHunters**](https://krebsonsecurity.com/?s=shiny+hunters)
.

Those sources said Rey had an ongoing beef with the Dutch hacker over control of the ShinyHunters brand and data, and that the inclusion of the oversized Umbreon Pokemon image in the FBI jobs site defacement was likely an attempt by Rey to pin the hack on the Dutchman.

Rey was
[first publicly identified](https://www.kelacyber.com/blog/hellcat-hacking-group-unmasked-rey-and-pryx/)
by the cybersecurity firm
**KELA**
in March 2025. In advance of our
[November 2025 profile of Rey](https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/)
, KrebsOnSecurity messaged Rey’s father and asked for permission to interview his teenage son. Rey’s dad merely forwarded the message to his son, who admitted to participating in ransomware attacks and said he was trying to extricate himself from the SLSH hacker group.

## BLAMING UMBREON

Immediately after news of the FBI jobs site hack was picked up in the media, Rey’s main account on Twitter/X (Ryan Moran/@rmoskovy) was taunting the Cl0p ransomware group and the FBI, crudely depicting them as the twin towers in New York being struck by planes labeled “cl0p drama” and “fbi breach claim.” In the foreground of the city is the giant Pokemon figure of Umbreon.

![](https://krebsonsecurity.com/wp-content/uploads/2026/09/rey-cl0p-fbi.png)

A taunting meme uploaded to Twitter/X by Rey’s now-defunct account on Sept. 22. A giant float-sized version of the Pokemon character Umbreon can be seen in the bottom left.

On Sept. 24, KrebsOnSecurity again contacted Rey’s dad, asking to interview him and his son for a story on Rey’s apparent ascendency as the head of ShinyHunters. Just hours after that request, Rey deleted his longtime Twitter/X account. Meanwhile, Rey’s dad, who works for the Royal Jordanian Airlines, has failed to respond to a half-dozen emailed requests for comment about his son’s alleged activities.

Where does the bad blood between SLSH and ShinyHunters come from? According to
[a story in Wired](https://www.wired.com/story/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)
this month, ShinyHunters and SLSH members briefly partnered earlier this year to help better monetize important stolen credentials collected by
**TeamPCP**
, an upstart group that was having great success compromising global code supply chains with malicious software but hadn’t been able to profit much from their stolen data (two alleged leaders of TeamPCP
[were arrested last month in Australia](https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/)
, and in an interview the TeamPCP leader claimed they made just $20,000).

The Wired story noted how Mandiant had infiltrated TeamPCP and was secretly responsible for having the crime group’s stolen credentials burned so quickly: Mandiant was secretly feeding those credentials to the major cloud providers like Amazon and Microsoft, who quickly invalidated the stolen keys. Meanwhile, the formerly cooperating hacker groups began to blame one another for causing the credentials to become worthless.

Wired’s
**Andy Greenberg**
reported that a few weeks after partnering with TeamPCP, “ShinyHunters went rogue, carrying out its own extortions with TeamPCP’s credentials but without giving the supply-chain hackers their cut.”

Mandiant researcher
**Austin Larsen**
told KrebsOnSecurity earlier this month that ShinyHunters has been enjoying a successful extortion spree so far this year, and is on track to pull in nearly $100 million in extortion payments from cybercrime victims in 2026.

Van der Stap claims he was never motivated by money and that his earlier hacker activity was driven by a desire to have the world’s most complete collection of stolen databases. Speaking with reporters from Bloomberg in 2024, Van der Stap said that singular focus in turn fueled his desire to carry out cyberattacks.

“The hacking was very easy for me, and it wasn’t a compulsion,” he
[told Bloomberg](https://archive.ph/K47wB#selection-1447.0-1447.321)
. “My habit was collecting. Collecting data, organizing data, downloading data, creating folders.”

DIVD, the nonprofit security research group where Van der Stap previously served as a volunteer,
[disclosed on LinkedIn last week](https://www.linkedin.com/feed/update/urn:li:activity:7508986131779088384/)
that the organization was dealing with an internal cybersecurity incident that appears to have involved the malicious use of artificial intelligence. DIVD has released few details about that incident, but a spokesperson for the nonprofit told KrebsOnSecurity it does not appear related to ShinyHunters, nor are there any signs the matter involves the work of a previous volunteer.

**Update: 3:44 p.m. ET:**
Corrected Van der Stap’s age, which is 24 (not 23).

**Update, 4:54 p.m. ET:**
The Dutch police have confirmed the arrest of a 24-year-old in connection with the ShinyHunters investigation. In
[a statement on Twitter/X](https://x.com/Pol_Ops_Int/status/2104607979559342174)
, the Dutch police said the man will appear on Tuesday, September 29 before the chambers of the Rotterdam District Court, and that it will provide more information tomorrow.

**Sept. 29, 9:42 a.m. ET:**
The Dutch news outlet
**RTL**
[reports](https://www.rtl.nl/nieuws/binnenland/artikel/5656154/pepijn-van-der-s-verdacht-van-opdracht-geven-moorden)
that investigators suspect Van der Stap tried to orchestrate at least two murders. RTL reported the two murders were allegedly to be committed abroad, and that there are indications the suspect gave the order for this.

The FBI released
[a short video message](https://x.com/FBICyberDiv/status/2104923994801553646?s=46)
on the ShinyHunters investigation from Brett Leatherman, assistant director of the FBI’s cyber division, who thanked Dutch law enforcement partners for their assistance and urged remaining ShinyHunters members to turn themselves in.

“Arrests have a way of changing who is willing to talk, and seized infrastructure has a way of showing us who’s left,” Leatherman said. “The longer you stay in this, the more we learn about you. You know how to find us, and we know how to find you. I suggest you reach out to us while the choice is still yours.”