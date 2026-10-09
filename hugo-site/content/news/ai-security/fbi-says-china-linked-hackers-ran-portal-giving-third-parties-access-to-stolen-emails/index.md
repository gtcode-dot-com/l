---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T19:08:03.829812+00:00'
exported_at: '2026-10-08T19:08:05.846057+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/fbi-says-china-linked-hackers-ran.html
structured_data:
  about: []
  author: ''
  description: FBI says Integrity Technology Group-linked hackers stole email in Southeast
    Asia using custom tools and a scanner with over 1,300 scripts.
  headline: FBI Says China-Linked Hackers Ran Portal Giving Third Parties Access to
    Stolen Emails
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/fbi-says-china-linked-hackers-ran.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: FBI Says China-Linked Hackers Ran Portal Giving Third Parties Access to Stolen
  Emails
updated_at: '2026-10-08T19:08:03.829812+00:00'
url_hash: ffc305faa6eeb9788c962d09fd67636b4a8f845f
---

Hackers tied to a Chinese cybersecurity company stole email from government organizations, law enforcement agencies, healthcare systems, and religious institutions in Southeast Asia, the FBI and agencies in 6 other countries said on October 8.

The company,
**Integrity Technology Group**
, has been sanctioned by the U.S. and the UK. The hackers scanned websites for flaws using a tool containing more than 1,300 scripts, guessed passwords for Microsoft 365 and Exchange accounts, and copied mailboxes using tools designed to collect mail.

The hackers have been breaking into networks since at least mid-January 2021, according to the agencies'
[joint advisory](https://www.ic3.gov/CSA/2026/261008.pdf)
. It describes the hacking in the present tense but provides no date for any theft and does not specify how many organizations were breached.

The same hackers targeted U.S. government services, critical manufacturing, healthcare, and IT organizations, along with U.S. law enforcement, education, and religious groups. Organizations in Southeast Asia, Africa, and North America were also targeted.

The hackers also run a web application that "provides third-party access to stolen email content," the advisory said. It does not identify those third parties.

In September 2024, the FBI
[disrupted a botnet](https://thehackernews.com/2024/09/new-raptor-train-iot-botnet-compromises.html)
, a network of hijacked devices, that the U.S. Justice Department said Integrity Technology Group controlled. It held more than 200,000 routers, cameras, and other consumer devices, and Lumen researchers had named it Raptor Train.

The 2024 action dealt with the botnet. The new advisory covers how the hackers get into networks and what they take. It is based on evidence the FBI recovered and observed during several investigations related to the company.

### Who Is Behind It

The agencies describe Integrity Technology Group as "a China-based for-profit company with links to the Chinese government" whose employees build or get cyber tools "for use and sale," host infrastructure, and break into networks.

The advisory uses a single label, "the threat actors," for the company and the hackers it enables. It does not say which of them carried out each break-in.

The U.S. Treasury
[sanctioned the company](https://thehackernews.com/2025/01/us-treasury-sanctions-beijing.html)
in January 2025 for its role in several computer break-ins against U.S. victims. The UK
[sanctioned it](https://www.gov.uk/government/news/uk-clamps-down-on-china-based-companies-for-reckless-and-irresponsible-activity-in-cyberspace)
in December 2025.

Christopher Wray, then the FBI director,
[said in 2024](https://www.fbi.gov/news/speeches-and-testimony/director-wray-s-remarks-at-the-2024-aspen-cyber-summit)
that the company's "chairman has publicly admitted that for years his company has collected intelligence and performed reconnaissance for Chinese government security agencies."

The hackers' methods are "consistent with" activity that security companies track as Flax Typhoon, Ethereal Panda, and RedJuliett, among others, the advisory said. Those names may not match the U.S. government's own tracking one-to-one, and the same hackers may also carry out work unrelated to Integrity Technology Group.

Flax Typhoon is Microsoft's name for a China-based group that it
[described in 2023](https://thehackernews.com/2023/08/china-linked-flax-typhoon-cyber.html)
as targeting organizations in Taiwan.

Integrity Technology Group rejected the U.S. accusations in January 2025. It told the Shanghai Stock Exchange that the U.S. move had no factual basis,
[the Associated Press reported](https://www.clickondetroit.com/business/2025/01/06/china-protests-us-sanctions-for-its-alleged-role-in-hacking-complains-of-foreign-hacker-attacks/)
. A Chinese Foreign Ministry spokesperson, asked about the sanctions, said China firmly opposed the U.S. action, according to the same report.

### How the Hackers Get In

The hackers look for flaws in networks and web applications with open-source scanners such as Nmap, masscan, and WPScan, the advisory said. Their scans focus on ports 21, 22, 53, 80, 443, and 1080.

"The use of open source tools typically found on GitHub suggests the threat actors tend to look for more vulnerable targets," the agencies said.

The hackers have also used a scanner called MicroScan since as early as 2017. It is a Python web application containing more than 1,300 penetration testing scripts designed to scan websites for specific flaws. The hackers have used the scripts against services including OpenSSL, Oracle WebLogic Server, Rejetto HFS, WordPress, Juniper ScreenOS, Jenkins, and Apache Struts.

The UK's National Cyber Security Centre, one of the agencies behind the advisory, said in
[its news release](https://www.ncsc.gov.uk/news/china-linked-actors-called-out-by-uk-and-international-partners-for-targeting-sensitive-data)
that the hackers are "uniquely using AI tools, such as automated scanning." The advisory itself does not mention AI.

The hackers mostly get in with command-line tools built on exploit code written in languages such as Python and Go. The advisory lists 8 known flaws that it says were successfully exploited. The flaws were found in the hackers' penetration testing scripts.

The table shows the affected versions as the advisory gives them and, where one could be confirmed, the release that fixes the flaw.

| Flaw | Product | Affected Versions in the Advisory | Fixed In |
| --- | --- | --- | --- |
| CVE-2014-6278 | GNU Bash | Through 4.3 bash43-026 | Not confirmed |
| CVE-2015-3306\* | ProFTPD | 1.3.5 | [1.3.5a](https://github.com/proftpd/proftpd/blob/1.3.5/NEWS) |
| CVE-2015-5477\* | ISC BIND | 9.x before 9.9.7-P2 and 9.10.x before 9.10.2-P3 | [9.9.7-P2 or 9.10.2-P3](https://kb.isc.org/docs/aa-01272) |
| CVE-2016-3081\* | Apache Struts | 2.3.19 to 2.3.20.2, 2.3.21 to 2.3.24.1, and 2.3.25 to 2.3.28 | [2.3.20.3, 2.3.24.3, or 2.3.28.1](https://cwiki.apache.org/confluence/spaces/WW/pages/62693266/S2-032) |
| CVE-2019-11510 | Pulse Connect Secure | 8.2 before 8.2R12.1, 8.3 before 8.3R7.1, and 9.0 before 9.0R3.4 | 8.2R12.1, 8.3R7.1, or 9.0R3.4, from the advisory's ranges |
| CVE-2021-22205 | GitLab | All versions starting from 11.9 | [13.8.8, 13.9.6, or 13.10.3](https://nvd.nist.gov/vuln/detail/CVE-2021-22205) , per its NVD record |
| CVE-2021-3199\* | ONLYOFFICE Document Server | 5.1.5 through 5.6.2 | [5.6.3](https://github.com/ONLYOFFICE/DocumentServer/blob/903fe5ab7a275bd69c3c3346af2d21cf87ebeabf/CHANGELOG.md#563) |
| CVE-2023-22894\* | Strapi | Up to 4.5.5 | [4.8.0](https://strapi.io/blog/security-disclosure-of-vulnerabilities-cve) |

The advisory marks 5 of the 8 with an asterisk and describes them as newly added to the Known Exploited Vulnerabilities (KEV) catalog, the list of flaws that the U.S. Cybersecurity and Infrastructure Security Agency (CISA) says have been used in attacks. They were not in the
[catalog data that CISA publishes on GitHub](https://github.com/cisagov/kev-data)
(version 2026.10.04) when The Hacker News checked at 18:05 UTC on October 8.

Strapi's own advisory gives a wider range than the joint advisory. It says versions from 3.2.1 through 4.7.9, but not including 4.8.0, are affected.

Two flaws depend on a setting. The Struts flaw works only when Dynamic Method Invocation is turned on, and Apache says turning it off is an alternative to upgrading. The ONLYOFFICE flaw applies when JWT is used, according to its NVD record.

The BIND flaw is a denial-of-service bug that makes the DNS server exit.

Another way in is a fake login. The FBI recovered a cross-site scripting (XSS) payload that changes a vulnerable web page to show username and password fields.

After a visitor enters any username and password, the page offers a password-protected ZIP file that holds a program named live700\_v1.exe. That program starts a process named DiagTrack.exe, the same name as a legitimate Windows program, which sends encrypted traffic to dns.studiocloud[.]xyz.

The FBI attributes that domain to Integrity Technology Group and assesses that the malware likely targets email.

The hackers also use password spraying, which means trying a few common passwords against many accounts. For this, they use EBurst, an open-source Python tool that targets Microsoft 365 and Exchange accounts.

EBurst tries logins through Exchange interfaces that include ECP, EWS, OAB, OWA, RPC, API, MAPI, PowerShell, Autodiscover, and Microsoft-Server-ActiveSync, according to its README file. Defenders should cover these interfaces, the agencies said.

### How They Stay and What They Take

To keep access, the hackers install SoftEther, a legitimate VPN program that security software is less likely to flag, the advisory said. They often rename the installer conhost.exe or dllhost.exe so it looks like a Windows file, and they set the client to reconnect each time the machine starts.

To take credentials, they ran a tool named DC.exe that uses DCSync, a technique that copies data from a domain controller through Active Directory's replication service. It copied account credentials, group membership details, and trust relationships.

For email, the hackers built a bot from a PHP script named Curlc4.txt. It collects mail through Exchange Web Services (EWS), an interface that also gives access to calendars and contacts.

The bot compresses the mail, sometimes encrypts it, and uploads it to a remote server. The script appears to be stand-alone rather than installed on a hacked device, and its main command-and-control domain was natcloudservice[.]com.

A second tool, office-cli, keeps going back to Microsoft 365 accounts to take mail from different time periods. It works from configuration files that hold a client ID, tenant ID, and secret, and it avoids detection by using legitimate access methods, the agencies said.

The FBI also saw the hackers download databases or pull data from victims' email by hand.

In some cases, the hackers limited access to the stolen data to IP addresses in Xiamen, China.

Users of the web application for third parties can view the mail of a specific account by adding arguments to a URL.

### What Defenders Should Do

The agencies urge defenders to hunt for signs of this activity in their own networks. The steps they recommend include:

* Turn off unused services and ports, such as remote access and file sharing.
* Sanitize user input in web applications to block XSS.
* Require multifactor authentication (MFA), especially for webmail, VPNs, and accounts that reach critical systems.
* Watch for unexpected Active Directory replication, a sign of DCSync.
* Check cloud accounts for connected applications that can read files and email.
* Review web application logs for attack attempts.
* Apply patches, including for the 8 flaws listed above.
* Replace products that no longer get updates.

For a suspected compromise, the advisory's steps are to isolate the affected hosts, hunt to learn how far the break-in went, and report it under national rules. The hackers should be removed after enough hunting data has been collected, and the network then hardened.

The advisory has 39 pages of indicators of compromise (IOCs), the domains, IP addresses, and file hashes linked to the hackers. The agencies say several date back to as early as 2016 and recommend checking them before blocking.

Some are not new. The Hacker News found that 10 IP addresses in the list also appeared in the
[September 2024 advisory](https://www.ic3.gov/CSA/2024/240918.pdf)
on the botnet, where they were tied to its command-and-control servers.

The dates do not match. The new list shows those 10 addresses as last seen on June 5, 2024. The 2024 advisory showed them as last seen between August 28 and September 4, 2024.

So a "last seen" date in the new list is not always the latest one on record. Apart from dates that show when a domain's registration expires, the most recent "last seen" dates in the tables are from 2025.