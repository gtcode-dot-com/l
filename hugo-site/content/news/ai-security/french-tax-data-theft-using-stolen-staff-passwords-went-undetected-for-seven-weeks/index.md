---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T22:54:57.803010+00:00'
exported_at: '2026-10-06T22:55:00.034835+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/french-tax-data-theft-using-stolen.html
structured_data:
  about: []
  author: ''
  description: French tax data theft used stolen staff passwords and evaded DGFIP
    and ANSSI monitoring.
  headline: French Tax Data Theft Using Stolen Staff Passwords Went Undetected for
    Seven Weeks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/french-tax-data-theft-using-stolen.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: French Tax Data Theft Using Stolen Staff Passwords Went Undetected for Seven
  Weeks
updated_at: '2026-10-06T22:54:57.803010+00:00'
url_hash: d6d690a45d2cd808509e80e8c77574340f0e9181
---

An attacker used stolen passwords of staff at France's tax administration to take tax data on hundreds of thousands of taxpayers and businesses in June and July.

Neither the tax administration nor France's national cybersecurity agency saw the data leave. The attack was not sophisticated, the agency, ANSSI, says in a
[report](https://cyber.gouv.fr/documents/821/20260923_NP_TLPCLEAR_ANSSI_Rapport_incident_DGFIP.pdf)
(in French) published on Tuesday: it worked because of weak login protection, poorly separated networks and gaps in monitoring.

The tax administration, known as the DGFIP, runs France's tax website, impots.gouv.fr. The data came from E-Contact, the tool taxpayers use to message the tax administration.

The stolen data covers
[a little over 350,000 individuals](https://www.impots.gouv.fr/sites/default/files/media/2_actu/2026-08_acces_illegitime_donnees/faq_acces_illegitime_donnes_fiscales_particuliers.pdf)
and
[a little over 250,000 businesses](https://www.impots.gouv.fr/sites/default/files/media/2_actu/2026-08_acces_illegitime_donnees/faq_acces_illegitime_donnes_fiscales_professionnels.pdf)
, the DGFIP says. Taxpayers' own online accounts and passwords were not compromised.

For individuals, the data that may have been viewed or copied includes their tax ID, contact details, family situation, reference taxable income and tax withholding rate, plus a list of the messages they exchanged with the DGFIP. For fewer than 250 people, the messages themselves may also have been taken.

For businesses, it covers the company name, SIREN registration number, address and basic details of their messages. For fewer than 2,076 businesses, the content of those messages may have been seen.

The theft became known on August 12, when the attacker claimed it on an online forum, seven weeks after the first batch of data was taken. Prime Minister Sébastien Lecornu then
[asked ANSSI for an in-depth audit](https://cyber.gouv.fr/actualites/lanssi-publie-le-rapport-dincident-sur-les-cyberattaques-ayant-touche-la-dgfip/)
. In August, the ministry overseeing the DGFIP offered a different explanation.

It
[said at the time](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)
that the DGFIP's access checks had not revealed the theft "because of the sophistication of the attack" (translated from French).

### How the Attacker Got In

The attacker used two separate routes, according to the report. The first began with suspicious logins in early May and led to E-Contact.

The first route relied on several dozen passwords belonging to DGFIP staff, stolen over three months. They were probably taken by infostealers, malware that quietly copies saved logins, from computers the DGFIP did not manage, most likely staff's own devices.

Two portals the attacker used, PIGP and ADER, asked only for a password, so a stolen one worked at once. PIGP is a web portal that DGFIP staff used for email and HR services. ADER provides access to certain DGFIP applications via the RIE, the network that connects French government ministries.

The attacker reached the RIE through compromised Education ministry systems connected to it. Sensitive DGFIP applications were not separated from the rest of the RIE, allowing them to be accessed from parts of the network with no apparent need. Investigators also found traces of many attempts to move into other government bodies on the network.

The accounts the attacker used had no special privileges, yet they could reach a large amount of data. ANSSI did not look at how user rights were managed for this report.

The second route led to land-registry data. It went through APEX, a portal for partners such as notaries and land surveyors, which asked for a password and a one-time code sent by email.

The DGFIP's investigation found that a land surveyor's computer at a private firm had possibly been compromised, allowing the attacker to bypass that code. The data was taken between July 27 and August 8. It concerns nearly 435,000 households, according to a note from the Senate finance committee, dated September 4 and
[reported by Public Sénat](https://www.publicsenat.fr/actualites/economie/piratage-du-portail-des-impots-un-controle-du-senat-releve-des-fragilites-structurelles-dans-le-systeme)
.

### Why No One Saw the Theft

The DGFIP already had a routine for stolen staff logins, ANSSI says. Its security operations center (SOC) is the team that watches for attacks. When the SOC detected a compromised account or a threat intelligence provider flagged one, it reset the password.

That routine caught some of the attacker's activity but not the theft. On June 7, searches using a stolen account set off an alert and a same-day password reset, but the SOC missed that the attacker had moved from PIGP to ADER.

On June 23, the provider flagged another account the attacker was using, and searches made with it opened a SOC ticket at 8:50 p.m. Paris time. At 4:26 a.m. the next day, the attacker began pulling data from E-Contact via ADER using automated scraping tools that copy data page by page.

The SOC handled the ticket at 10:40 a.m. by resetting the account's password. The reset addressed the alert on PIGP but did not terminate the attacker's open session on ADER. Data kept flowing for almost 16 more hours, until 2:31 a.m. on June 25.

In July, the SOC again caught the attacker's searches but not the theft. The attacker restarted the automated extraction on July 22 with another stolen account. The SOC spotted suspicious searches with that account the next day and reset it on July 24.

The DGFIP's SOC was not monitoring ADER at all. No system linked the warning signs, such as logins at night and connections from VPNs, from addresses in India or from addresses known to be malicious. Data volumes raised no alert either, including the 11 GB exchanged between June 22 and 25.

The number of requests each user made was not checked either, although scraping needs one request per page. On their own, such signals usually cause many false alarms, but together they could have raised an alert, ANSSI says.

ANSSI's own monitoring missed the theft too. Its detection sensors sit only at the entry and exit points of the RIE and the internet, and the agency has no access to application logs.

Because the attacker used real staff accounts, ANSSI's network monitoring did not see the activity. Even so, the total number of requests should have raised alerts, the agency says.

On June 9, the Education ministry's security team told the security teams of all ministries about an incident on its network, shared 17 indicators of compromise and asked them to watch connections from the ministry's addresses. The attacker had already used one of those addresses and did so again in late June. ANSSI says the time taken to analyze and share such indicators should have been kept to a minimum.

On August 6, ANSSI passed the DGFIP two suspicious addresses it had found by searching its past sensor data. The DGFIP blocked them and reset five accounts, but neither agency identified the theft until the attacker claimed it on August 12.

### What Has Changed and What ANSSI Recommends

When the report was written, DGFIP staff accounts had been shut out of ADER since August 13 and out of PIGP since August 18. The DGFIP does not expect to reopen either portal to them.

APEX was locked and the surveyor's account disabled on August 14, and the firm's other accounts were disabled four days later. These cuts significantly disrupted some DGFIP services and partner organizations.

An action plan has been drawn up to extend monitoring to all DGFIP business applications, implement strong authentication, and set limits on the amount of data that can be accessed. ANSSI says only a fuller audit, already planned, will identify all the weaknesses that could be exploited.

E-Contact, which had no second login step, will have one, and tools to detect unusual volumes of data viewed or copied will be deployed, according to the Senate note. By the time of the note, staff could no longer reach DGFIP tools from their personal devices.

ANSSI's recommendations for the DGFIP include:

* Revoke every active session, on all applications and portals, whenever a password is reset.
* When an account is reported as compromised, check what it did from the likely date of compromise.
* Use multi-factor authentication (MFA) on every application, with a second factor that still protects the account if the password is stolen. A one-time code sent by email is not enough if the same password opens the mailbox. Hardware tokens or authenticator apps, ideally on a separate device, are preferred.
* Monitor every business application in a SIEM, a system that collects security logs. Set quotas on the records accessed, requests made and data exchanged over a given period.
* Do not allow personal devices to access work resources.