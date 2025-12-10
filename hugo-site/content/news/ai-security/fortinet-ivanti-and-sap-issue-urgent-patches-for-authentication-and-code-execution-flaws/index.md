---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-10T12:03:08.054862+00:00'
exported_at: '2025-12-10T12:03:10.734604+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html
structured_data:
  about: []
  author: ''
  description: Vendors fix critical flaws across Fortinet, Ivanti, and SAP to prevent
    authentication bypass and remote code execution.
  headline: Fortinet, Ivanti, and SAP Issue Urgent Patches for Authentication and
    Code Execution Flaws
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fortinet, Ivanti, and SAP Issue Urgent Patches for Authentication and Code
  Execution Flaws
updated_at: '2025-12-10T12:03:08.054862+00:00'
url_hash: 930201868b7b12afe0871a204bac76d46a1c93ff
---

Fortinet, Ivanti, and SAP have moved to address critical security flaws in their products that, if successfully exploited, could result in an authentication bypass and code execution.

The Fortinet vulnerabilities affect FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager and relate to a case of improper verification of a cryptographic signature. They are tracked as
**CVE-2025-59718**
and
**CVE-2025-59719**
(CVSS scores: 9.8).

"An Improper Verification of Cryptographic Signature vulnerability [CWE-347] in FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication via a crafted SAML message, if that feature is enabled on the device," Fortinet
[said](https://fortiguard.fortinet.com/psirt/FG-IR-25-647)
in an advisory.

The company, however, noted that the FortiCloud SSO login feature is not enabled in the default factory settings. FortiCloud SSO login is enabled when an administrator registers the device to FortiCare and has not disabled the toggle "Allow administrative login using FortiCloud SSO" in the registration page.

To temporarily protect their systems against attacks exploiting these vulnerabilities, organizations are advised to disable the FortiCloud login feature (if enabled) until it can be updated. This can be done in two ways -

* Go to System -> Settings -> Switch "Allow administrative login using FortiCloud SSO" to Off
* Run the below command in the CLI -

```
config system global
set admin-forticloud-sso-login disable
end
```

### Ivanti Releases Fix for Critical EPM Flaw

Ivanti has also shipped updates to address four security flaws in Endpoint Manager (EPM), one of which is a critical severity bug in the EPM core and remote consoles. The vulnerability, assigned the CVE identifier
**CVE-2025-10573**
, carries a CVSS score of 9.6.

"Stored XSS in Ivanti Endpoint Manager prior to version 2024 SU4 SR1 allows a remote unauthenticated attacker to execute arbitrary JavaScript in the context of an administrator session," Ivanti
[said](https://forums.ivanti.com/s/article/Security-Advisory-EPM-December-2025-for-EPM-2024?language=en_US)
.

Rapid7 security researcher Ryan Emmons, who discovered and reported the shortcoming on August 15, 2025, said it allows an attacker with unauthenticated access to the primary EPM web service to join fake managed endpoints to the EPM server so as to poison the administrator web dashboard with malicious JavaScript.

"When an Ivanti EPM administrator views one of the poisoned dashboard interfaces during normal usage, that passive user interaction will trigger client-side JavaScript execution, resulting in the attacker gaining control of the administrator's session," Emmons
[said](https://www.rapid7.com/blog/post/cve-2025-10573-ivanti-epm-unauthenticated-stored-cross-site-scripting-fixed/)
.

Douglas McKee, director of vulnerability intelligence at Rapid7, said in a statement that CVE-2025-10573 represents a serious risk as it's trivial to exploit and can be done so by sending a fake device report to the server using a basic file format.

"While the attack only fully executes when an administrator views the dashboard, this is a routine and necessary task for IT staff; consequently, the likelihood of triggering the exploit during normal operations is high, ultimately allowing the attacker to take control of the administrator's session," McKee added.

Ensar Seker, CISO at threat intelligence company SOCRadar, also emphasized that the user interaction requirement doesn't reduce the vulnerability's threat level and that it has a "significant" exploitation potential when combined with social engineering.

"Remote code execution via JavaScript injection is no longer theoretical in supply chain attacks; it’s become operationally viable," Seker said. "Organizations must act swiftly to patch, and more importantly, implement rigorous user interface sanitization and privilege segmentation."

The company
[noted](https://www.ivanti.com/blog/december-2025-security-update)
that user interaction is required to exploit the flaw and that it's not aware of any attacks in the wild. It has been patched in EPM version 2024 SU4 SR1.

Also patched in the same version are three other high-severity vulnerabilities (CVE-2025-13659, CVE-2025-13661, and CVE-2025-13662) that could allow a remote, unauthenticated attacker to achieve arbitrary code execution. CVE-2025-13662, like in the case of CVE-2025-59718 and CVE-2025-59719, stems from improper verification of cryptographic signatures in the patch management component.

### SAP Fixes Three Critical Flaws

Lastly, SAP has
[pushed](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/december-2025.html)
December security updates to address 14 vulnerabilities across multiple products, including three critical-severity flaws. They are listed below -

* **CVE-2025-42880**
  (CVSS score: 9.9) - A code injection vulnerability in SAP Solution Manager
* **CVE-2025-55754**
  (CVSS score: 9.6) - Multiple vulnerabilities in Apache Tomcat within SAP Commerce Cloud
* **CVE-2025-42928**
  (CVSS score: 9.1) - A deserialization vulnerability in SAP jConnect SDK for Sybase Adaptive Server Enterprise (ASE)

Boston-based SAP security platform Onapsis has been credited with reporting CVE-2025-42880 and CVE-2025-42928. The company
[said](https://onapsis.com/blog/sap-security-patch-day-december-2025/)
it identified a remote-enabled function module in SAP Solution Manager that enables an authenticated attacker to inject arbitrary code.

"Given the central role of SAP Solution Manager in the SAP system landscape, we strongly recommend a timely patch," Onapsis security researcher Thomas Fritsch said.

CVE-2025-42928, on the other hand, allows for remote code execution by providing specially crafted input to the SAP jConnect SDK component. However, a successful exploitation requires elevated privileges.

With security vulnerabilities in Fortinet, Ivanti, and SAP's software frequently exploited by bad actors, it's essential that users move quickly to apply the fixes.