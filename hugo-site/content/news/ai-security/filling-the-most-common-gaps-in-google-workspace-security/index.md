---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-22T12:15:12.969612+00:00'
exported_at: '2026-01-22T12:15:15.553562+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/filling-most-common-gaps-in-google.html
structured_data:
  about: []
  author: ''
  description: Google Workspace provides a strong baseline, yet default settings expose
    gaps in email security, access control, and data visibility.
  headline: Filling the Most Common Gaps in Google Workspace Security
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/filling-most-common-gaps-in-google.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Filling the Most Common Gaps in Google Workspace Security
updated_at: '2026-01-22T12:15:12.969612+00:00'
url_hash: abf84fdc6b34349dbfb71b1fe0d8b683383471c8
---

**

The Hacker News
**

Jan 22, 2026

Email Security / SaaS Security

Security teams at agile, fast-growing companies often have the same mandate: secure the business without slowing it down. Most teams inherit a tech stack optimized for breakneck growth, not resilience. In these environments, the security team is the helpdesk, the compliance expert, and the incident response team all rolled into one.

Securing the cloud office in this scenario is all about finding leverage: identifying the strategic control points that drive the most resilience without adding operational overhead.

Google Workspace provides an excellent security foundation, but its native tooling has inherent limitations, and relying on the default configurations can cause headaches. To build a truly resilient program, there are some common-sense first steps teams can take to secure Workspace natively, before intelligently augmenting the platform where its capabilities fall short.

## Secure email, the primary attack vector and largest archive

Email remains the most reliable target for attackers, as an initial attack method, as a vector to other connected apps and systems, and as a target for sensitive data. While Gmail's default security is solid at catching some threats, it often struggles with targeted threats and sophisticated social engineering and payload-less attacks.

### The gaps in native protection

* **BEC and Targeted spear phishing:**
  business email compromise (BEC) attacks often contain no malicious links or attachments, instead relying on social engineering that bypasses traditional defenses.
* **Environmental context**
  : Google doesn't know who your VIPs are, which partners you work with, or how frequently you receive invoices from vendors, making it difficult to flag subtle anomalies worth scrutinizing.
* **Data archive at rest:**
  for most companies, email is the largest repository of sensitive data. If an account is compromised, the attacker has access to years of confidential conversations, attachments, contracts, and more.

### How to improve Gmail's security today

While Google can't provide all the capabilities of a modern email security platform, there are steps you can take to ensure your core Gmail configurations are as secure as possible.

* **Turn on advanced scanning:**
  enable Google's enhanced pre-delivery message scanning and malware protection to ensure you're making the most of Google's capabilities.
* **Implement basic email hygiene:**
  configure SPF, DKIM, and DMARC. These protocols prove your emails are actually from you, and are critical for preventing domain spoofing.
* **Automate future settings:**
  ensure the "Apply future recommended settings automatically" option is checked to stay current as Google rolls out more security updates.

## Move beyond authentication to manage access

Multi-factor authentication (MFA) is the single most important control you can implement today, but it's not a magic bullet. Your access control can't stop at the login page.

### Too many windows and side doors

* **Malicious OAuth access:**
  compromised tokens, illicit consent grants, man-in-the-middle attacks, or simple misconfigurations can allow attackers access that appears perfectly legitimate to security tooling.
* **Legacy access:**
  protocols like IMAP and POP don't natively support MFA, and App Passwords can be circumvented.
* **Detection gaps:**
  Google can alert on suspicious sign-ins, but connecting that signal to other suspicious activity across the environment is a manual, time-consuming process.

### Harden your access control immediately

* **Enforce strong MFA:**
  not all MFA is created equal. At the very least, disable SMS or phone calls as MFA authentication methods. Ideally, adopt phishing-resistant methods like physical security keys or Yubikeys.
* **Disable legacy protocols:**
  turn off POP and IMAP access for all users within the Gmail settings.
* **Deny by default for OAuth:**
  require users to request access to unconfigured third-party apps rather than granting access by default.

## The next steps to proactive, modern security

A properly-configured Google Workspace offers a solid foundation for securing a fast-growing company. But as your company grows, your attack surface grows with it. For lean security teams who need to maximize their efficiency and their effectiveness, the end goal isn't just to have the right settings; it's to have visibility across all of Google Workspace, with detection and response capabilities to detect subtle signs of compromise if an account is breached.

Material Security builds on Google's foundation, providing visibility and context that Workspace lacks natively across the emails, files, and accounts within your environment.

### Advanced email protection

[Material's inbound protection](https://material.security/product/email?utm_source=third-party&utm_medium=blog&utm_campaign=20260122-the-hacker-news)
combines threat research with AI, user report automation, and custom detection rules to provide multi-layered coverage to catch and remediate sophisticated threats. Granular automated remediations protect the entire organization from the first detection or user report, and automatically triage and respond to user-reported phishing.

Material is also the only platform on the market that protects sensitive email content, automatically detecting, classifying, and securing sensitive emails and attachments behind an MFA prompt, protecting critical information even in a breach.

### Context-aware account security

A richer set of signals across the entire cloud office enables Material to detect and
[stop account takeovers](https://material.security/product/accounts?utm_source=third-party&utm_medium=blog&utm_campaign=20260122-the-hacker-news)
early. Material monitors all activity across the cloud office, including suspicious logins, unusual data retrieval patterns and file-sharing behavior, password resets, out-of-policy forwarding rules, and much more. This enables organizations to understand their risks and threats holistically and take action faster than with native tools alone.

### Data discovery and protection

Material fills in the gaps in Google's native data protection capabilities. Material automatically
[detects and classifies sensitive and confidential data](https://material.security/product/files?utm_source=third-party&utm_medium=blog&utm_campaign=20260122-the-hacker-news)
in Google Drive, and enforces file-sharing and data access policies without slowing down collaboration. Risky sharing of sensitive files is flagged, and the system works with each user to self-heal or justify potentially risky sharing before revoking risky access and, when needed, updating labels.

## How secure is your Workspace?

Google Workspace security spans so many domains that it can be difficult to maintain a complete picture of your posture, and this only gets harder as your organization scales and your Workspace evolves. That's why Material built our free Google Workspace Security Scorecard.

Whether you're a security engineer on a small security team scrambling to manage the day-to-day security of your organization, a CISO looking to better understand and report on your posture, or an IT leader responsible for Workspace administration, our quick, 5-minute assessment will not only provide a solid baseline but also actionable recommendations to improve your posture.

> [**Check out the Google Workspace self-assessment now to find out where your gaps are.**](https://material.security/workspace-security-scorecard?utm_source=third-party&utm_medium=blog&utm_campaign=20260122-the-hacker-news)

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.