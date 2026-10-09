---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T02:58:23.638750+00:00'
exported_at: '2026-06-09T02:58:26.324471+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html
structured_data:
  about: []
  author: ''
  description: Debug flag disabled Microsoft 365 Android token checks, letting untrusted
    apps access accounts; patches issued May 12 to reduce risk
  headline: Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover
    Debug Flag
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug
  Flag
updated_at: '2026-06-09T02:58:23.638750+00:00'
url_hash: 37434cbdd7806e09c4593a48e7df8b69167d7586
---

**

Swati Khandelwal
**

Jun 03, 2026

Vulnerability / Mobile Security

A development flag left switched on in production builds of several Microsoft 365 Android apps disabled the check that limits account-token sharing to trusted Microsoft apps.

Any other app on the same phone could ask for the signed-in user's token and get it, then read email, open files, browse the calendar, and send messages as that user. No password, no login screen, no permission prompt.

Microsoft has patched it, and if you run Microsoft 365 apps on Android, update them.

The bug, which
[Enclave](https://enclave.ai/blog/flagleft-microsoft-365-android-forgotten-flag-account-takeover)
calls
**FlagLeft**
, hit Word, PowerPoint, Excel, Microsoft 365 Copilot, Microsoft Loop, and OneNote, six apps with billions of downloads between them. Teams shipped with the same flag set to false and were not affected, which Enclave reads as a slip rather than a design.

Microsoft 365 apps share account access on purpose, so signing into Word means you do not sign in again for PowerPoint. The handoff is supposed to verify who is asking and turn away anything that is not a trusted Microsoft app.

Enclave's Yanir Tsarimi and Ofek Levin found the check was being skipped because of a single line left in the shipping code:
**setIsDebugMode(true)**
. The flaw sat in a shared Microsoft SDK, so the same hole showed up in app after app.

The tokens handed over were FOCI tokens, the family refreshes tokens Microsoft uses for single sign-on across its apps. They can be refreshed and reused over long stretches, and the resulting traffic looks routine in logs. From the user's side, nothing visible happens.

VIDEO

Enclave built a working proof of concept that pulled tokens through an unverified third-party app and read email with them. Microsoft classifies these as local spoofing flaws; in plain terms, a malicious app already on the device is all it takes.

Microsoft issued four CVEs on May 12, all classed as spoofing under improper access control (CWE-284):
[CVE-2026-41100](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41100)
for Microsoft 365 Copilot (CVSS 4.4),
[CVE-2026-41101](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41101)
for Word (CVSS 7.1),
[CVE-2026-41102](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41102)
for PowerPoint (CVSS 7.1), and
[CVE-2026-42832](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42832)
for Excel (CVSS 7.7). The four CVEs cover Copilot, Word, PowerPoint, and Excel.

Enclave reported the same flaw in Loop and OneNote, but neither got a separate CVE in the May batch. NVD lists the patched Word build for Android as 16.0.19822.20190, with earlier versions affected. The other apps were fixed through the same Google Play updates.

Nothing in Microsoft's
[May Patch Tuesday release](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html)
was listed as publicly known or exploited, and there is no public evidence that the flaw was used before the fix.

What to do? Update Word, PowerPoint, Excel, Microsoft 365 Copilot, Loop, and OneNote from Google Play. Security teams managing Android fleets should push the updates through MDM and confirm devices are off builds earlier than 16.0.19822.20190.

The patch closes the hole, but it does not retroactively kill tokens that an attacker may already hold. FOCI refresh tokens outlive an app update, so for accounts on devices that ran an old build alongside untrusted apps, it is worth revoking refresh tokens and forcing a fresh sign-in.