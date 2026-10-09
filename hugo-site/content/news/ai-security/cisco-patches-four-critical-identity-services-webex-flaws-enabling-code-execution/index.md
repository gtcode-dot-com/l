---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-16T12:15:14.087259+00:00'
exported_at: '2026-04-16T12:15:16.734231+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/cisco-patches-four-critical-identity.html
structured_data:
  about: []
  author: ''
  description: Cisco patches four CVEs up to CVSS 9.9 in ISE and Webex, preventing
    code execution and user impersonation risks.
  headline: Cisco Patches Four Critical Identity Services, Webex Flaws Enabling Code
    Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/cisco-patches-four-critical-identity.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cisco Patches Four Critical Identity Services, Webex Flaws Enabling Code Execution
updated_at: '2026-04-16T12:15:14.087259+00:00'
url_hash: 633f938264f316a77d209bb01d0f160a9b2b8c2c
---

**

Ravie Lakshmanan
**

Apr 16, 2026

Vulnerability / Network Security

Cisco has announced patches to address four critical security flaws impacting Identity Services and Webex Services that could result in arbitrary code execution and allow an attacker to impersonate any user within the service.

The details of the vulnerabilities are below -

* **[CVE-2026-20184](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-webex-cui-cert-8jSZYhWL)**
  (CVSS score: 9.8) - An improper certificate validation in the integration of single sign-on (SSO) with Control Hub in Webex Services that could allow an unauthenticated, remote attacker to impersonate any user within the service and gain unauthorized access to legitimate Cisco Webex services.
* **[CVE-2026-20147](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-traversal-8bYndVrZ)**
  (CVSS score: 9.9) - An insufficient validation of user-supplied input vulnerability in Identity Services Engine (ISE) and ISE Passive Identity Connector (ISE-PIC) that could allow an authenticated, remote attacker in possession of valid administrative credentials to achieve remote code execution by sending crafted HTTP requests.
* **[CVE-2026-20180 and CVE-2026-20186](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-4fverepv)**
  (CVSS scores: 9.9) - Multiple insufficient validation of user-supplied input vulnerabilities in ISE could allow an authenticated, remote attacker in possession of read only admin credentials to execute arbitrary commands on the underlying operating system of an affected device by sending crafted HTTP requests.

"A successful exploit could allow the attacker to obtain user-level access to the underlying operating system and then elevate privileges to root," Cisco said in an advisory for CVE-2026-20147, CVE-2026-20180, and CVE-2026-20186.

"In single-node ISE deployments, successful exploitation of this vulnerability could cause the affected ISE node to become unavailable, resulting in a denial of service (DoS) condition. In that condition, endpoints that have not already authenticated would be unable to access the network until the node is restored."

CVE-2026-20184 requires no customer action as it's cloud-based. However, customers who are using SSO are
[advised](https://help.webex.com/en-us/article/nstvmyo/Manage-single-sign-on-integration-in-Control-Hub#task_394598AFBCD3D73A488E6DBB99AD3214)
to upload a new identity provider (IdP) SAML certificate to Control Hub. The remaining vulnerabilities have been addressed in the following versions -

* **CVE-2026-20147**
  + Cisco ISE or ISE-PIC Release earlier than 3.1 (Migrate to a fixed release)
  + Cisco ISE Release 3.1 (3.1 Patch 11)
  + Cisco ISE Release 3.2 (3.2 Patch 10)
  + Cisco ISE Release 3.3 (3.3 Patch 11)
  + Cisco ISE Release 3.4 (3.4 Patch 6)
  + Cisco ISE Release 3.5 (3.5 Patch 3)
* **CVE-2026-20180 and CVE-2026-20186**
  + Cisco ISE Release earlier than 3.2 (Migrate to a fixed release)
  + Cisco ISE Release 3.2 (3.2 Patch 8)
  + Cisco ISE Release 3.3 (3.3 Patch 8)
  + Cisco ISE Release 3.4 (3.4 Patch 4)
  + Cisco ISE Release 3.5 (Not Vulnerable)

While Cisco noted that it is not aware of any of these shortcomings being exploited in the wild, it's essential that users update their instances to the latest version for optimal protection.