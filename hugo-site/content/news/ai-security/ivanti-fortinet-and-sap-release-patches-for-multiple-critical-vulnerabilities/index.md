---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T02:00:13.999063+00:00'
exported_at: '2026-06-11T02:00:17.093795+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
structured_data:
  about: []
  author: ''
  description: Fortinet, Ivanti, and SAP patched critical flaws up to CVSS 10.0, reducing
    RCE, admin takeover, and data exposure risks.
  headline: Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities
updated_at: '2026-06-11T02:00:13.999063+00:00'
url_hash: 2d6261af0b08e26794c5e89017fc66847fb8cd04
---

**

Ravie Lakshmanan
**

Jun 10, 2026

Vulnerability / Patch Management

Fortinet, Ivanti, and SAP have released security updates to address multiple critical security vulnerabilities that could result in arbitrary code execution and information disclosure.

The security flaw patched by Fortinet relates to a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI. It's tracked as
**CVE-2026-25089**
(CVSS score: 9.1).

"An improper neutralization of special elements used in an OS command vulnerability [CWE-78] in FortiSandbox, FortiSandbox Cloud and FortiSandbox PaaS WEB UI may allow an unauthenticated attacker to execute unauthorized commands via specifically crafted HTTP requests," Fortinet
[said](https://fortiguard.fortinet.com/psirt/FG-IR-26-141)
.

The issue impacts the following products and versions -

* FortiSandbox 5.0.0 through 5.0.5 (Upgrade to 5.0.6 or above)
* FortiSandbox 4.4.0 through 4.4.8 (Upgrade to 4.4.9 or above)
* FortiSandbox Cloud 5.0.4 through 5.0.5 (Upgrade to 5.0.6 or above)
* FortiSandbox PaaS 5.0.4 through 5.0.5 (Upgrade to 5.0.6 or above)

On Tuesday, Ivanti also
[published](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Sentry-CVE-2026-10520-CVE-2026-10523?language=en_US)
fixes for two critical security flaws impacting Ivanti Sentry (formerly MobileIron Sentry) -

* **CVE-2026-10520**
  (CVSS score: 10.0) - An operating system command injection vulnerability before versions R10.5.2, R10.6.2, and R10.7.1 that allows a remote unauthenticated user to achieve root-level remote code execution.
* **CVE-2026-10523**
  (CVSS score: 9.9) - An authentication bypass vulnerability before versions R10.5.2, R10.6.2, and R10.7.1 that allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access.

watchTowr Labs, which published additional details of CVE-2026-10520, said an attacker could exploit the vulnerability by issuing a specially crafted HTTP request to the "/mics/api/v2/sentry/mics-config/handleMessage" endpoint, which is then interpreted as a MICS configuration command and executed by a backend component named "handleExecute()."

The patch shipped by Ivanti incorporates additional controls that block access to the vulnerable endpoint, causing unauthenticated requests to be redirected to the login page.

"Ivanti did not just remove attacker control over the vulnerable execution path," security researcher Sonny Macdonald
[said](https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/)
. "They also added a layer of protection in front of it to make reaching the endpoint significantly more difficult. In other words: they added authentication."

Rounding off the list of updates is SAP, which
[pushed out fixes](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/june-2026.html)
for four critical vulnerabilities in NetWeaver AS ABAP and ABAP Platform, as well as SAP Commerce Cloud and SAP Data Hub -

* **CVE-2026-44748**
  (CVSS score: 9.9) - XML signature wrapping vulnerability in SAML authentication in SAP NetWeaver AS ABAP and ABAP Platform
* **CVE-2026-27671**
  (CVSS score: 9.8) - Memory corruption vulnerability in Application Server ABAP of SAP NetWeaver and ABAP Platform
* **CVE-2026-22732**
  (CVSS score: 9.1) - Potential Spring security vulnerability within SAP Commerce Cloud and SAP Data Hub
* **CVE-2026-40128**
  (CVSS score: 9.0) - Directory traversal vulnerability in SAP NetWeaver Application Server Java (Web Container)

"The application allows an authenticated attacker with normal privileges to obtain a valid signed message and send modified signed XML documents with tampered identity information to the verifier," SAP security company Onapsis
[said](https://onapsis.com/blog/sap-security-patch-day-june-2026/)
.

"Due to an improper XML signature verification, the manipulated identity information is accepted, leading to unauthorized access to sensitive user data and potential disruption of normal system usage."

As for CVE-2026-27671, the defect allows an unauthenticated attacker to send a crafted RFC request that exploits how the SAP kernel validates the RFC protocol to achieve memory corruption.

There is no evidence that any of the aforementioned flaws have been exploited in the wild. However, it's always a safe practice to update to the latest version for optimal protection.