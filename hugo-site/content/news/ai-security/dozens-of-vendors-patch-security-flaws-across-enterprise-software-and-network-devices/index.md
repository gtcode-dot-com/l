---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-11T14:15:13.739418+00:00'
exported_at: '2026-03-11T14:15:16.176808+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/dozens-of-vendors-patch-security-flaws.html
structured_data:
  about: []
  author: ''
  description: SAP patches two critical flaws (CVSS 9.8, 9.1) affecting FS-QUO and
    NetWeaver, preventing remote code execution risks in enterprise systems.
  headline: Dozens of Vendors Patch Security Flaws Across Enterprise Software and
    Network Devices
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/dozens-of-vendors-patch-security-flaws.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Dozens of Vendors Patch Security Flaws Across Enterprise Software and Network
  Devices
updated_at: '2026-03-11T14:15:13.739418+00:00'
url_hash: 8c33a5a84869646fe49336672ceb66499f860be2
---

**

Ravie Lakshmanan
**

Mar 11, 2026

Vulnerability / Enterprise Security

SAP has
[released](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/march-2026.html)
security updates to address two critical security flaws that could be exploited to achieve arbitrary code execution on affected systems.

The vulnerabilities in question listed below -

* **CVE-2019-17571**
  (CVSS score: 9.8) - A code injection vulnerability in SAP Quotation Management Insurance application (FS-QUO)
* **CVE-2026-27685**
  (CVSS score: 9.1) - An insecure deserialization vulnerability in SAP NetWeaver Enterprise Portal Administration

"The application uses an outdated artifact of Apache Log4j 1.2.17 that is vulnerable to CVE-2019-17571," SAP security company Onapsis
[said](https://onapsis.com/blog/sap-security-patch-day-march-2026/)
. "It allows an unprivileged attacker to execute arbitrary code remotely on the server, causing high impact on confidentiality, integrity, and availability of the application."

CVE-2026-27685, on the other hand, stems from missing or insufficient validation during the deserialization of uploaded content, which could allow an attacker to upload untrusted or malicious content.

"Only the fact that an attacker requires high privileges for a successful exploit prevents the vulnerability from being tagged with a CVSS score of 10," Onapsis added.

The disclosure comes as Microsoft shipped patches for
[84 vulnerabilities](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html)
across products, including dozens of privilege escalation and remote code execution flaws.

On Tuesday, Adobe also announced patches for
[80 vulnerabilities](https://helpx.adobe.com/security.html)
, four of which are critical flaws impacting Adobe Commerce and Magento Open Source that could result in privilege escalation and security feature bypass. Separately, it fixed five critical vulnerabilities in Adobe Illustrator that could pave the way for arbitrary code execution.

Elsewhere, Hewlett Packard Enterprise put out fixes for five shortcomings in Aruba Networking AOS-CX. The most severe of the flaws is CVE-2026-23813 (CVSS score: 9.8), an authentication bypass affecting the management interface.

"A vulnerability has been identified in the web-based management interface of AOS-CX switches that could potentially allow an unauthenticated remote actor to circumvent existing authentication controls," HPE
[said](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05027en_us&docLocale=en_US)
. "In some cases, this could enable resetting the admin password."

"Exploitation of this Aruba vulnerability potentially gives attackers full control of AOS-CX network devices and the ability to compromise an entire system undetected," Ross Filipek, CISO at Corsica Technologies, said in a statement.

"A successful compromise could lead to the disruption of network communications or the erosion of the integrity of key business services. This flaw is a reminder that vulnerabilities in network devices are becoming more common in today's hyper-connected world. When attackers gain privileged access to these devices, it puts organizations at significant risk."

### Software Patches from Other Vendors

Security updates have also been released by other vendors over the past few weeks to rectify several vulnerabilities, including —

* [ABB](https://www.abb.com/global/en/company/about/cybersecurity/alerts-and-notifications)
* [Amazon Web Services](https://aws.amazon.com/security/security-bulletins/)
* [AMD](https://www.amd.com/en/resources/product-security.html#security)
* [Arm](https://developer.arm.com/Arm%20Security%20Center#sortCriteria=%40published%20descending&numberOfResults=48)
* [Atlassian](https://www.atlassian.com/trust/security/advisories)
* [Bosch](https://psirt.bosch.com/security-advisories/)
* [Broadcom](https://support.broadcom.com/web/ecx/search?searchString=cve&activeType=all&from=0&sortby=post_time&orderBy=desc&pageNo=1&aggregations=%5B%7B%22type%22%3A%22_type%22%2C%22filter%22%3A%5B%22notification_docs%22%5D%7D%5D&uid=d042dbba-f8c4-11ea-beba-0242ac12000b&resultsPerPage=50&exactPhrase=&withOneOrMore=&withoutTheWords=&pageSize=50&language=en&state=34&suCaseCreate=false)
  (including VMware)
* [Canon](https://psirt.canon/advisory-information/#id_2229656)
* [Cisco](https://tools.cisco.com/security/center/publicationListing.x)
* [Commvault](https://documentation.commvault.com/securityadvisories/)
* [Dassault Systèmes](https://www.3ds.com/trust-center/security/security-advisories)
* [Dell](https://www.dell.com/support/security/)
* [Devolutions](https://devolutions.net/security/advisories/)
* [Drupal](https://www.drupal.org/security)
* [Elastic](https://discuss.elastic.co/c/announcements/security-announcements/31)
* [F5](https://my.f5.com/manage/s/new-updated-articles#f-f5_document_type=Security%20Advisory&aq=%40f5_original_published_date%20%3E%3D%20now-7d)
* [Fortinet](https://www.fortiguard.com/psirt)
* [Fortra](https://www.fortra.com/security/advisories/product-security)
* [Foxit Software](https://www.foxit.com/support/security-bulletins.html)
* [GitLab](https://about.gitlab.com/releases/2026/02/25/patch-release-gitlab-18-9-1-released/)
* Google
  [Android](https://source.android.com/docs/security/bulletin/2026/2026-03-01)
  and
  [Pixel](https://source.android.com/docs/security/bulletin/pixel/2026/2026-03-01)
* [Google Chrome](https://chromereleases.googleblog.com/)
* [Google Cloud](https://cloud.google.com/support/bulletins)
* [Google Pixel Watch](https://source.android.com/docs/security/bulletin/pixel-watch/2026/2026-03-01)
* [Google Wear OS](https://source.android.com/docs/security/bulletin/wear/2026/2026-03-01)
* [Grafana](https://grafana.com/security/security-advisories/)
* [Hitachi Energy](https://www.hitachienergy.com/in/en/products-and-solutions/cybersecurity/alerts-and-notifications)
* [Honeywell](https://www.honeywell.com/us/en/product-security#security-notices)
* [HP](https://support.hp.com/us-en/security-bulletins)
* [HP Enterprise](https://support.hpe.com/connect/s/securitybulletinlibrary?language=en_US#sort=%40hpescuniversaldate%20descending&layout=table&numberOfResults=25&f:@kmdoclanguagecode=[cv1871440]&hpe=1)
  (including Aruba Networking and
  [Juniper Networks](https://supportportal.juniper.net/s/global-search/%40uri?language=en_US#sort=date%20descending&f:ctype=[Security%20Advisories])
  )
* [IBM](https://www.ibm.com/support/pages/bulletin/)
* [Intel](https://www.intel.com/content/www/us/en/security-center/default.html)
* [Ivanti](https://hub.ivanti.com/s/searchallcontent?language=en_US#q=CVE&sortCriteria=date%20descending&f-sfkbknowledgearticletypec=Security%20Advisory)
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
* [MediaTek](https://corp.mediatek.com/product-security-bulletin/March-2026)
* [Mitsubishi Electric](https://www.mitsubishielectric.com/en/psirt/vulnerability/index.html)
* [Moxa](https://www.moxa.com/en/support/product-support/security-advisory)
* Mozilla
  [Firefox, Firefox ESR, and Thunderbird](https://www.mozilla.org/en-US/security/advisories/)
* [n8n](https://github.com/n8n-io/n8n/security)
* [NVIDIA](https://www.nvidia.com/en-us/security/)
* [Palo Alto Networks](https://security.paloaltonetworks.com/)
* [QNAP](https://www.qnap.com/en/security-advisories)
* [Qualcomm](https://docs.qualcomm.com/product/publicresources/securitybulletin/)
* [Ricoh](https://www.ricoh.com/products/security/vulnerabilities)
* [Samsung](https://security.samsungmobile.com/securityUpdate.smsb)
* [Schneider Electric](https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp)
* [ServiceNow](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1226057)
* [Siemens](https://new.siemens.com/global/en/products/services/cert.html#SecurityPublications)
* [SolarWinds](https://www.solarwinds.com/trust-center/security-advisories)
* [Splunk](https://advisory.splunk.com/)
* [Synology](https://www.synology.com/en-in/security/advisory)
* [TP-Link](https://www.tp-link.com/us/press/security-advisory/)
* [Trend Micro](https://success.trendmicro.com/en-US/solution/KA-0022458)
* [WatchGuard](https://www.watchguard.com/wgrd-psirt/advisories)
* [Western Digital](https://www.westerndigital.com/support/product-security)
* [Zoom](https://explore.zoom.us/en/trust/security/security-bulletin/)
  , and
* [Zyxel](https://www.zyxel.com/global/en/support/security-advisories)