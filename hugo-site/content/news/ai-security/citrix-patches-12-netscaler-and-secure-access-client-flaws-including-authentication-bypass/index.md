---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T04:10:45.803507+00:00'
exported_at: '2026-11-15T04:10:46.951604+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html
structured_data:
  about: []
  author: ''
  description: Citrix patches 12 flaws in NetScaler and Secure Access Client that
    could enable denial-of-service, authentication bypass, or privilege escalation.
  headline: Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including
    Authentication Bypass
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication
  Bypass
updated_at: '2026-11-15T04:10:45.803507+00:00'
url_hash: c398aa3e92265ca6e4c3d73fa009aedda023fe8e
---

**

Ravie Lakshmanan
**

Nov 12, 2026

Vulnerability / Network Security

Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass.

The
[critical vulnerabilities](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697305)
that impact NetScaler ADC and NetScaler Gateway are listed below -

* **CVE-2026-120868**
  (CVSS score: 9.3) - A memory overflow vulnerability in Packet Processing can lead to unpredictable or erroneous behavior or DoS. (All NetScaler ADC and NetScaler Gateway deployments)
* **CVE-2026-107407**
  (CVSS score: 9.3) - A memory overflow vulnerability in SMPP traffic can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC configured with a Load Balancing or Content Switching virtual server of type SMPP)
* **CVE-2026-107408**
  (CVSS score: 9.3) - A memory corruption vulnerability in DNS / DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC configured for DNS load balancing and recursive DNS resolution)
* **CVE-2026-107409**
  (CVSS score: 9.3) - A memory corruption vulnerability in DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured with DNS Load Balancing over HTTPS)
* **CVE-2026-107410**
  (CVSS score: 9.3) - A memory overflow in NetScaler Push can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as Load Balancing virtual server  of type PUSH)
* **CVE-2026-107412**
  (CVSS score: 9.5) - Multiple memory overflow vulnerabilities can lead to unpredictable or erroneous behavior and DoS. (NetScaler configured as a Gateway or an AAA virtual server)
* **CVE-2026-107415**
  (CVSS score: 9.3) - A memory overflow vulnerability in Email OTP authentication can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC or NetScaler Gateway configured with an Email Action)
* **CVE-2026-111344**
  (CVSS score: 9.3) - A memory overflow vulnerability in Endpoint Analysis (EPA/EPAS) can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as a VPN virtual server or an authentication (AAA) virtual server with Endpoint Analysis)
* **CVE-2026-120864**
  (CVSS score: 9.3) - A memory overflow vulnerability in ICA proxy can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as a Gateway VPN virtual server, an AAA virtual server, or a CR virtual server of type HDX)

All the issues have been patched in the following versions -

* Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.57 and later releases
* Citrix NetScaler ADC and Citrix NetScaler Gateway 13.1-64.39 and later releases of 13.1
* Citrix NetScaler ADC 14.1-FIPS 14.1-73.58 FIPS and later releases of 14.1-FIPS
* Citrix NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1-37.293 and later releases of 13.1-FIPS and 13.1-NDcPP

Also addressed by Citrix are a number of flaws in NetScaler Console and Secure Access Client for Windows and Linux -

* **[CVE-2026-120869](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697320)**
  (CVSS score: 9.4) - An improper authentication vulnerability in NetScaler Console can allow an unauthenticated attacker to bypass authentication controls to access restricted resources on the appliance. (Fixed in NetScaler Console 14.1-74.34 and later)
* **[CVE-2026-118268](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697280)**
  (CVSS score: 8.5) - An improper privilege management vulnerability in Secure Access Client for Windows can allow a low-privileged user to escalate privileges to SYSTEM. (Fixed in Secure Access Client for Windows 26.11.1.6 and later)
* **[CVE-2026-118269](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697281)**
  (CVSS score: 8.5) - An improper privilege management vulnerability in Secure Access Client for Linux can allow a low-privileged user to gain root privileges. (Fixed in Secure Access Client for Linux 26.10.4 and later)

The security updates, Citrix said, follow a deeper review of its codebase by integrating artificial intelligence (AI)-assisted code analysis to detect and resolve vulnerabilities with an aim to harden the products before potential threats could materialize.

The company
[said](https://community.citrix.com/techzone-blogs/110_security-updates/security-updates-for-netscaler-adc-netscaler-gateway-and-netscaler-console/)
it's not aware of any exploits for any of the announced vulnerabilities, but urged customers to apply the updates as they are designed to "enhance the security posture of NetScaler."

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.