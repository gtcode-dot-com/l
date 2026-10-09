---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T15:28:41.450981+00:00'
exported_at: '2025-11-13T15:28:43.243061+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html
structured_data:
  about: []
  author: ''
  description: Microsoft fixes 63 flaws, including an exploited Windows Kernel zero-day
    and a critical RCE bug.
  headline: Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day
    Under Active Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under
  Active Attack
updated_at: '2025-11-13T15:28:41.450981+00:00'
url_hash: b7f4fd2b5bbca90ab4b928c091a67d2d84efb02e
---

**

Nov 12, 2025
**

Ravie Lakshmanan

Vulnerability / Patch Tuesday

Microsoft on Tuesday released patches for
[63 new security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2025-Nov)
identified in its software, including one that has come under active exploitation in the wild.

Of the 63 flaws, four are rated Critical and 59 are rated Important in severity. Twenty-nine of these vulnerabilities are related to privilege escalation, followed by 16 remote code execution, 11 information disclosure, three denial-of-service (DoS), two security feature bypass, and two spoofing bugs.

The patches are in addition to the
[27 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
the Windows maker addressed in its Chromium-based Edge browser since the release of
[October 2025's Patch Tuesday](https://thehackernews.com/2025/10/two-new-windows-zero-days-exploited-in.html)
update.

The zero-day vulnerability that has been listed as exploited in Tuesday's update is
[CVE-2025-62215](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62215)
(CVSS score: 7.0), a privilege escalation flaw in Windows Kernel. The Microsoft Threat Intelligence Center (MSTIC) and Microsoft Security Response Center (MSRC) have been credited with discovering and reporting the issue.

"Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Kernel allows an authorized attacker to elevate privileges locally," the company said in an advisory.

That said, successful exploitation hinges on an attacker who has already gained a foothold on a system to
[win a race condition](https://www.action1.com/patch-tuesday/patch-tuesday-november-2025/)
. Once this criterion is satisfied, it could permit the attacker to obtain SYSTEM privileges.

"An attacker with low-privilege local access can run a specially crafted application that repeatedly attempts to trigger this race condition," Ben McCarthy, lead cybersecurity engineer at Immersive, said.

"The goal is to get multiple threads to interact with a shared kernel resource in an unsynchronized way, confusing the kernel's memory management and causing it to free the same memory block twice. This successful 'double free' corrupts the kernel heap, allowing the attacker to overwrite memory and hijack the system's execution flow."

It's currently not known how this vulnerability is being exploited and by whom, but it's assessed to be used as part of a post-exploitation activity to escalate their privileges after obtaining initial access through some other means, such as social engineering, phishing, or exploitation of another vulnerability, Satnam Narang, senior staff research engineer at Tenable, said.

"When chained with other bugs this kernel race is critical: an RCE or sandbox escape can supply the local code execution needed to turn a remote attack into a SYSTEM takeover, and an initial low‑privilege foothold can be escalated to dump credentials and move laterally," Mike Walters, president and co-founder of Action1, said in a statement.

Also patched as part of the updates are two heap-based buffer overflow flaws in Microsoft's Graphics Component (
[CVE-2025-60724](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-60724)
, CVSS score: 9.8) and Windows Subsystem for Linux GUI (
[CVE-2025-62220](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62220)
, CVSS score: 8.8) that could result in remote code execution.

Another vulnerability of note is a high-severity privilege escalation flaw in Windows Kerberos (CVE-2025-60704, CVSS score: 7.5) that takes advantage of a missing cryptographic step to gain administrator privileges. The vulnerability has been codenamed CheckSum by Silverfort.

"The attacker must inject themselves into the logical network path between the target and the resource requested by the victim to read or modify network communications," Microsoft
[said](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-60704)
. "An unauthorized attacker must wait for a user to initiate a connection."

Silverfort researchers Eliran Partush and Dor Segal, who discovered the shortcoming, described it as a
[Kerberos constrained delegation](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-constrained-delegation-overview)
vulnerability that allows an attacker to impersonate arbitrary users and gain control over an entire domain by means of an adversary-in-the-middle (AitM) attack.

An attacker who is able to successfully exploit the flaw could escalate privileges and move laterally to other machines in an organization. More concerning, threat actors could also gain the ability to impersonate any user in the company, allowing them to gain unfettered access or become a domain administrator.

"Any organization using Active Directory, with the Kerberos delegation capability turned on, is impacted," Silverfort
[said](https://www.silverfort.com/blog/you-win-some-you-checksum-kerberos-delegation-vulnerability-cve-2025-60704/)
. "Because Kerberos delegation is a feature within Active Directory, an attacker requires initial access to an environment with compromised credentials."

### Software Patches from Other Vendors

In addition to Microsoft, security updates have also been released by other vendors over the past several weeks to rectify several vulnerabilities, including —

* [Adobe](https://helpx.adobe.com/security/security-bulletin.html)
* [Amazon Web Services](https://aws.amazon.com/security/security-bulletins/)
* [AMD](https://www.amd.com/en/resources/product-security.html#security)
* [Apple](https://support.apple.com/en-us/HT201222)
* [ASUS](https://www.asus.com/security-advisory/)
* [Atlassian](https://confluence.atlassian.com/security/security-bulletin-october-21-2025-1652920034.html)
* [AutomationDirect](https://community.automationdirect.com/s/internal-database-security-advisory/Internal_Database_Security_Advisory__c/Default)
* [Bitdefender](https://www.bitdefender.com/consumer/support/?post_type=security_advisories)
* [Broadcom](https://support.broadcom.com/web/ecx/search?searchString=cve&activeType=all&from=0&sortby=post_time&orderBy=desc&pageNo=1&aggregations=%5B%7B%22type%22%3A%22_type%22%2C%22filter%22%3A%5B%22notification_docs%22%5D%7D%5D&uid=d042dbba-f8c4-11ea-beba-0242ac12000b&resultsPerPage=50&exactPhrase=&withOneOrMore=&withoutTheWords=&pageSize=50&language=en&state=34&suCaseCreate=false)
  (including VMware)
* [Cisco](https://tools.cisco.com/security/center/publicationListing.x)
* [Citrix](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695486&articleURL=NetScaler_ADC_and_NetScaler_Gateway_Security_Bulletin_for_CVE_2025_12101)
* [ConnectWise](https://www.connectwise.com/company/trust/security-bulletins)
* [D-Link](https://supportannouncement.us.dlink.com/)
* [Dell](https://www.dell.com/support/security/)
* [Devolutions](https://devolutions.net/security/advisories/)
* [Drupal](https://www.drupal.org/security)
* [Elastic](https://discuss.elastic.co/c/announcements/security-announcements/31)
* [F5](https://my.f5.com/manage/s/new-updated-articles#sort=%40f5_updated_published_date%20descending&f:@f5_document_type=[Security%20Advisory]&periodFilter=0&dateField=1)
* [Fortinet](https://www.fortiguard.com/psirt)
* [GitLab](https://about.gitlab.com/releases/2025/10/22/patch-release-gitlab-18-5-1-released/)
* [Google Android](https://source.android.com/docs/security/bulletin/2025-11-01)
* [Google Chrome](https://chromereleases.googleblog.com/)
* [Google Cloud](https://cloud.google.com/support/bulletins)
* [Grafana](https://grafana.com/security/security-advisories/)
* [Hitachi Energy](https://www.hitachienergy.com/in/en/products-and-solutions/cybersecurity/alerts-and-notifications)
* [HP](https://support.hp.com/us-en/security-bulletins)
* [HP Enterprise](https://support.hpe.com/connect/s/securitybulletinlibrary?language=en_US#sort=%40hpescuniversaldate%20descending&layout=table&numberOfResults=25&f:@kmdoclanguagecode=[cv1871440]&hpe=1)
  (including Aruba Networking and
  [Juniper Networks](https://supportportal.juniper.net/s/global-search/%40uri?language=en_US#sort=date%20descending&f:ctype=[Security%20Advisories])
  )
* [IBM](https://www.ibm.com/support/pages/bulletin/)
* [Intel](https://www.intel.com/content/www/us/en/security-center/default.html)
* [Ivanti](https://forums.ivanti.com/s/searchallcontent?language=en_US#q=CVE&t=All&sort=date%20descending&f:@sfkbknowledgearticletypec=[Security%20Advisory])
* [Jenkins](https://www.jenkins.io/security/advisories/)
* [Lenovo](https://support.lenovo.com/us/en/product_security/ps500001-lenovo-product-security-advisories)
* Linux distributions
  [AlmaLinux](https://errata.almalinux.org/)
  ,
  [Alpine Linux](https://security.alpinelinux.org)
  ,
  [Amazon Linux](https://alas.aws.amazon.com/)
  ,
  [Arch Linux](https://security.archlinux.org/advisory)
  ,
  [Debian](https://www.debian.org/security/#DSAS)
  ,
  [Gentoo](https://security.gentoo.org/glsa)
  ,
  [Oracle Linux](https://linux.oracle.com/ords/f?p=105:21::::RP::)
  ,
  [Mageia](https://advisories.mageia.org/)
  ,
  [Red Hat](https://access.redhat.com/security/security-updates/security-advisories)
  ,
  [Rocky Linux](https://errata.rockylinux.org/)
  ,
  [SUSE](https://www.suse.com/support/update/)
  , and
  [Ubuntu](https://ubuntu.com/security/notices)
* [MediaTek](https://corp.mediatek.com/product-security-bulletin/November-2025)
* [Mitsubishi Electric](https://www.mitsubishielectric.com/en/psirt/vulnerability/index.html)
* [MongoDB](https://www.mongodb.com/resources/products/mongodb-security-bulletins)
* [Moxa](https://www.moxa.com/en/support/product-support/security-advisory)
* Mozilla
  [Firefox and Firefox ESR](https://www.mozilla.org/en-US/security/advisories/)
* [NVIDIA](https://www.nvidia.com/en-us/security/)
* [Oracle](https://www.oracle.com/security-alerts/)
* [Palo Alto Networks](https://security.paloaltonetworks.com/)
* [QNAP](https://www.qnap.com/en/security-advisories)
* [Qualcomm](https://docs.qualcomm.com/product/publicresources/securitybulletin/)
* [Rockwell Automation](https://www.rockwellautomation.com/en-us/company/about-us/sustainability/trust-security/security-advisories.html?sort=pubAsc)
* [Ruckus Wireless](https://support.ruckuswireless.com/security)
* [Samba](https://www.samba.org/samba/history/security.html)
* [Samsung](https://security.samsungmobile.com/securityUpdate.smsb)
* [SAP](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/november-2025.html)
* [Schneider Electric](https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp)
* [Siemens](https://new.siemens.com/global/en/products/services/cert.html#SecurityPublications)
* [SolarWinds](https://www.solarwinds.com/trust-center/security-advisories)
* [SonicWall](https://www.sonicwall.com/search/#t=Support&sort=date%20descending&f:sourceTypeFacetId=[Notices]&f:@language=[English])
* [Splunk](https://advisory.splunk.com/)
* [Spring Framework](https://spring.io/security)
* [Supermicro](https://www.supermicro.com/en/support/security_center#!advisories)
* [Synology](https://www.synology.com/en-in/security/advisory)
* [TP-Link](https://support.omadanetworks.com/us/document/108456/)
* [WatchGuard](https://www.watchguard.com/wgrd-psirt/advisories)
  , and
* [Zoom](https://explore.zoom.us/en/trust/security/security-bulletin/)