---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-15T14:15:14.315995+00:00'
exported_at: '2026-04-15T14:15:16.722164+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/april-patch-tuesday-fixes-critical.html
structured_data:
  about: []
  author: ''
  description: Critical SAP, Adobe, Fortinet, and Microsoft flaws disclosed in April
    Patch Tuesday, enabling RCE and data theft risks.
  headline: April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft,
    Fortinet, and More
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/april-patch-tuesday-fixes-critical.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft, Fortinet,
  and More
updated_at: '2026-04-15T14:15:14.315995+00:00'
url_hash: e24df1d700dcbb916dc6676c0d3d351c288e3789
---

**

Ravie Lakshmanan
**

Apr 15, 2026

Vulnerability / Data Breach

A number of critical vulnerabilities impacting products from Adobe, Fortinet, Microsoft, and SAP have taken center stage in April's Patch Tuesday releases.

Topping the list is an SQL injection vulnerability impacting SAP Business Planning and Consolidation and SAP Business Warehouse (
[CVE-2026-27681](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/april-2026.html)
, CVSS score: 9.9) that could result in the execution of arbitrary database commands.

"The vulnerable ABAP program allows a low-privileged user to upload a file with arbitrary SQL statements that will then be executed," Onapsis
[said](https://onapsis.com/blog/sap-security-notes-april-2026-patch-day/)
in an advisory.

In a potential attack scenario, a bad actor could abuse the affected upload-related functionality to run malicious SQL against BW/BPC data stores, extract sensitive data, and delete or corrupt database content.

"Manipulated planning figures, broken reports, or deleted consolidation data can undermine close processes, executive reporting, and operational planning," Pathlock
[said](https://pathlock.com/blog/security-alerts/sap-patch-day-april-2026-critical-sql-injection-authorization-flaws/)
. "In the wrong hands, this issue also creates a credible path to both stealthy data theft and overt business disruption."

Another security vulnerability that deserves a mention is a critical-severity remote code execution in Adobe Acrobat Reader (
[CVE-2026-34621](https://thehackernews.com/2026/04/adobe-patches-actively-exploited.html)
, CVSS score: 8.6) that has come under active exploitation in the wild.

That said, there are many unknowns at this stage. It is not clear how many people have been affected by the hacking campaign. Nor is there any information about who is behind the activity, who is being targeted, and what their motives could be.

Also
[patched](https://helpx.adobe.com/security/security-bulletin.html)
by Adobe are
[five critical flaws in ColdFusion versions 2025 and 2023](https://helpx.adobe.com/security/products/coldfusion/apsb26-38.html)
that, if successfully exploited, could lead to arbitrary code execution, application denial-of-service, arbitrary file system read, and security feature bypass.

The vulnerabilities are listed below -

* **CVE-2026-34619**
  (CVSS score: 7.7) - A path traversal vulnerability leading to security feature bypass
* **CVE-2026-27304**
  (CVSS score: 9.3) - An improper input validation vulnerability leading to arbitrary code execution
* **CVE-2026-27305**
  (CVSS score: 8.6) - A path traversal vulnerability leading to arbitrary file system read
* **CVE-2026-27282**
  (CVSS score: 7.5) - An improper input validation vulnerability leading to security feature bypass
* **CVE-2026-27306**
  (CVSS score: 8.4) - An improper input validation vulnerability leading to arbitrary code execution

Fixes have also been released for two critical FortiSandbox vulnerabilities that could result in authentication bypass and code execution -

* **[CVE-2026-39813](https://fortiguard.fortinet.com/psirt/FG-IR-26-112)**
  (CVSS score: 9.1) - A path traversal vulnerability in FortiSandbox JRPC API that could allow an unauthenticated attacker to bypass authentication via specially crafted HTTP requests. (Fixed in versions 4.4.9 and 5.0.6)
* **[CVE-2026-39808](https://fortiguard.fortinet.com/psirt/FG-IR-26-100)**
  (CVSS score: 9.1) - An operating system command injection vulnerability in FortiSandbox that could allow an unauthenticated attacker to execute unauthorized code or commands via crafted HTTP requests. (Fixed in version 4.4.9)

The development comes as Microsoft
[addressed](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html)
a staggering 169 security defects, including a spoofing vulnerability impacting Microsoft SharePoint Server (CVE-2026-32201, CVSS score: 6.5) that could allow an attacker to view sensitive information. The company said it's being actively exploited, although there are no insights into the in-the-wild exploitation associated with the bug.

"SharePoint services, especially those used as internal document stores, can be a treasure trove for threat actors looking to steal data, especially data that may be leveraged to force ransom payments using double extortion techniques by threatening to release the stolen data if payment is not made," Kev Breen, senior director of threat research at Immersive, said.

"A secondary concern is that threat actors with access to SharePoint services could deploy weaponised documents or replace legitimate documents with infected versions that would allow them to spread to other hosts or victims moving laterally across the organization."

## Software Patches from Other Vendors

In addition to Microsoft, security updates have also been released by other vendors over the past several weeks to rectify several vulnerabilities, including —

* [ABB](https://www.abb.com/global/en/company/about/cybersecurity/alerts-and-notifications)
* [Amazon Web Services](https://aws.amazon.com/security/security-bulletins/)
* [AMD](https://www.amd.com/en/resources/product-security.html#security)
* [Apple](https://support.apple.com/en-us/HT201222)
* [ASUS](https://www.asus.com/security-advisory/)
* [AVEVA](https://www.aveva.com/en/support-and-success/cyber-security-updates/)
* [Broadcom](https://support.broadcom.com/web/ecx/security-advisory)
  (including VMware)
* [Canon](https://psirt.canon/advisory-information/#id_2229656)
* [Cisco](https://tools.cisco.com/security/center/publicationListing.x)
* [Citrix](https://support.citrix.com/support-home/topic-article-list?trendingCategory=20&trendingTopicName=Latest%20Security%20Bulletin)
* [CODESYS](https://www.codesys.com/ecosystem/security/latest-codesys-security-advisories/)
* [D-Link](https://supportannouncement.us.dlink.com/)
* [Dassault Systèmes](https://www.3ds.com/trust-center/security/security-advisories)
* [Dell](https://www.dell.com/support/security/)
* [Devolutions](https://devolutions.net/security/advisories/)
* [dormakaba](https://www.dormakabagroup.com/en/security-advisories)
* [Drupal](https://www.drupal.org/security)
* [Elastic](https://discuss.elastic.co/c/announcements/security-announcements/31)
* [F5](https://my.f5.com/manage/s/new-updated-articles#f-f5_document_type=Security%20Advisory&aq=%40f5_original_published_date%20%3E%3D%20now-7d)
* [Fortinet](https://www.fortiguard.com/psirt)
* [Foxit Software](https://www.foxit.com/support/security-bulletins.html)
* [FUJIFILM](https://www.fujifilm.com/fbglobal/eng/company/news/notice)
* [Gigabyte](https://www.gigabyte.com/us/Support/Security)
* [GitLab](https://docs.gitlab.com/releases/18/patch-release-gitlab-18-10-3-released/)
* Google
  [Android](https://source.android.com/docs/security/bulletin/2026/2026-04-01)
  and
  [Pixel](https://source.android.com/docs/security/bulletin/pixel/2026/2026-04-01)
* [Google Chrome](https://chromereleases.googleblog.com/)
* [Google Cloud](https://cloud.google.com/support/bulletins)
* [Grafana](https://grafana.com/security/security-advisories/)
* [Hitachi Energy](https://www.hitachienergy.com/in/en/products-and-solutions/cybersecurity/alerts-and-notifications)
* [HP](https://support.hp.com/us-en/security-bulletins)
* [HP Enterprise](https://support.hpe.com/connect/s/securitybulletinlibrary?language=en_US#sort=%40hpescuniversaldate%20descending&layout=table&numberOfResults=25&f:@kmdoclanguagecode=[cv1871440]&hpe=1)
  (including Aruba Networking and
  [Juniper Networks](https://supportportal.juniper.net/s/global-search/%40uri?language=en_US#sort=date%20descending&f:ctype=[Security%20Advisories])
  )
* [Huawei](https://www.huawei.com/en/psirt/all-bulletins)
* [IBM](https://www.ibm.com/support/pages/bulletin/)
* [Ivanti](https://hub.ivanti.com/s/searchallcontent?language=en_US#q=CVE&sortCriteria=date%20descending&f-sfkbknowledgearticletypec=Security%20Advisory&f-commonlanguage=English)
* [Jenkins](https://www.jenkins.io/security/advisories/)
* [Lenovo](https://support.lenovo.com/us/en/product_security/ps500001-lenovo-product-security-advisories)
* Linux distributions
  [AlmaLinux](https://errata.almalinux.org)
  ,
  [Alpine Linux](https://security.alpinelinux.org)
  ,
  [Amazon Linux](https://alas.aws.amazon.com)
  ,
  [Arch Linux](https://security.archlinux.org/advisory)
  ,
  [Debian](https://www.debian.org/security/#DSAS)
  ,
  [Gentoo](https://security.gentoo.org/glsa)
  ,
  [Oracle Linux](https://linux.oracle.com/ords/f?p=105:21::::RP::)
  ,
  [Mageia](https://advisories.mageia.org)
  ,
  [Red Hat](https://access.redhat.com/security/security-updates/security-advisories)
  ,
  [Rocky Linux](https://errata.rockylinux.org/)
  ,
  [SUSE](https://www.suse.com/support/update/)
  , and
  [Ubuntu](https://ubuntu.com/security/notices)
* [MediaTek](https://corp.mediatek.com/product-security-bulletin/April-2026)
* [Mitel](https://www.mitel.com/support/security-advisories)
* [Mitsubishi Electric](https://www.mitsubishielectric.com/en/psirt/vulnerability/index.html)
* [MongoDB](https://www.mongodb.com/resources/products/mongodb-security-bulletins)
* [Moxa](https://www.moxa.com/en/support/product-support/security-advisory)
* Mozilla
  [Firefox, Firefox ESR, and Thunderbird](https://www.mozilla.org/en-US/security/advisories/)
* [NETGEAR](https://www.netgear.com/about/security/)
* [Node.js](https://nodejs.org/en/blog/vulnerability/march-2026-security-releases)
* [NVIDIA](https://www.nvidia.com/en-us/security/)
* [ownCloud](https://owncloud.com/security/)
* [Palo Alto Networks](https://security.paloaltonetworks.com/)
* [Phoenix Contact](https://www.phoenixcontact.com/en-pc/service-and-support/psirt)
* [Progress Software](https://community.progress.com/s/global-search/%40uri#t=KnowledgeBase&sort=date%20descending&numberOfResults=100&f:@sfdcareaofinterest=[Defects]&f:@sfarticletypec=[Product_Alert,Critical_Alert])
* [QNAP](https://www.qnap.com/en/security-advisories)
* [Qualcomm](https://docs.qualcomm.com/product/publicresources/securitybulletin/)
* [Rockwell Automation](https://www.rockwellautomation.com/en-us/company/about-us/sustainability/trust-security/security-advisories.html?sort=pubAsc)
* [Ruckus Wireless](https://support.ruckuswireless.com/security)
* [Samsung](https://security.samsungmobile.com/securityUpdate.smsb)
* [Schneider Electric](https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp)
* [Siemens](https://new.siemens.com/global/en/products/services/cert.html#SecurityPublications)
* [SonicWall](https://www.sonicwall.com/search/#t=Support&sort=date%20descending&f:sourceTypeFacetId=[Notices]&f:@language=[English])
* [Splunk](https://advisory.splunk.com/)
* [Spring Framework](https://spring.io/security)
* [Supermicro](https://www.supermicro.com/en/support/security_center#!advisories)
* [Synology](https://www.synology.com/en-in/security/advisory)
* [TP-Link](https://www.tp-link.com/us/press/security-advisory/)
* [WatchGuard](https://www.watchguard.com/wgrd-psirt/advisories)
  , and
* [Xiaomi](https://trust.mi.com/zh-CN/misrc/bulletins?tab=advisory)