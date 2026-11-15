---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:32:28.294396+00:00'
exported_at: '2026-11-15T07:32:29.214654+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/citrix-patches-10-critical-netscaler-vulnerabilities
structured_data:
  about: []
  author: ''
  description: Citrix has patched critical-severity NetScaler vulnerabilities that
    could lead to unexpected behavior or denial-of-service (DoS).
  headline: Citrix Patches 10 Critical NetScaler Vulnerabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/citrix-patches-10-critical-netscaler-vulnerabilities
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Citrix Patches 10 Critical NetScaler Vulnerabilities
updated_at: '2026-11-15T07:32:28.294396+00:00'
url_hash: 884f319d841d0d291ca54d465c746d4be9a72bc6
---

**Citrix on Thursday announced patches for 28 vulnerabilities in NetScaler ADC and NetScaler Gateway, including nine critical-severity bugs.**

The critical flaws stem from memory overflow issues in Packet Processing, SMPP traffic, DNS / DNS-over-HTTPS (DoH), NetScaler Push, Email OTP authentication, Endpoint Analysis (EPA/EPAS), and ICA proxy, and could lead to unpredictable/erroneous behavior or denial-of-service (DoS) conditions.

They are tracked as CVE-2026-120868, CVE-2026-107407 to CVE-2026-107410, CVE-2026-107412, CVE-2026-107415, CVE-2026-111334, and CVE-2026-120864.

Most of the remaining 19 security defects are high-severity weaknesses leading to similar outcomes. Citrix also patched several medium-severity bugs, including CVE-2026-111338, which exposes sensitive authentication material in a log file.

NetScaler ADC and Gateway versions 14.1-73.57 and later, 13.1-64.39 and later, 14.1-73.58 FIPS and later, and 13.1-FIPS and 13.1-NDcPP 13.1-37.293 and later contain the relevant patches.

[Citrix urges](https://community.citrix.com/techzone-blogs/110_security-updates/security-updates-for-netscaler-adc-netscaler-gateway-and-netscaler-console/)
customers to update their instances as soon as possible, and details CVE preconditions associated with some of the vulnerabilities.

Advertisement. Scroll to continue reading.

On Thursday, the company also announced patches for a critical-severity flaw in NetScaler Console. Tracked as CVE-2026-120869 (CVSS score of 9.4), it could allow unauthenticated attackers to bypass controls and access restricted resources.

The security defect impacts all NetScaler Console 14.1 releases before 14.1-74.34.

Citrix makes no mention of any of these vulnerabilities being exploited in the wild, but vulnerabilities in NetScaler are a frequent target for threat actors.

**Related:**
[Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’](https://www.securityweek.com/nightmare-eclipse-drops-windows-zero-day-exploit-signdrop/)

**Related:**
[PHP2Shell Exploited in Destructive Check Point Gateway Attacks](https://www.securityweek.com/php2shell-exploited-in-destructive-check-point-gateway-attacks/)

**Related:**
[Chrome, Firefox Updates Patch Over 180 Vulnerabilities](https://www.securityweek.com/chrome-firefox-updates-patch-180-vulnerabilities/)

**Related:**
[Hackers Deploy Malware in Fresh ScreenConnect Campaign](https://www.securityweek.com/hackers-deploy-malware-in-fresh-screenconnect-campaign/)