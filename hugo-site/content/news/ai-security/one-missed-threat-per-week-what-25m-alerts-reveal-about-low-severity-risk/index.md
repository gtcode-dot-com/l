---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-13T04:14:16.775046+00:00'
exported_at: '2026-05-13T04:14:18.092477+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/one-missed-threat-per-week-what-25m.html
structured_data:
  about: []
  author: ''
  description: 1% of low-severity alerts became real breaches across 25M events, exposing
    weekly missed enterprise threats.
  headline: 'One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity
    Risk'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/one-missed-threat-per-week-what-25m.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity Risk'
updated_at: '2026-05-13T04:14:16.775046+00:00'
url_hash: 755765df9ee37bd173eaffe4a99ec638d2ea5c5a
---

The dark secret of enterprise security operations is that defenders have quietly institutionalized the practice of not looking. This is not just anecdotal, but rather backed by a recent report investigating more than 25 million security alerts, including informational and low-severity, across live enterprise environments.

The dataset behind these findings includes 10 million monitored endpoints and identities, 82,000 forensic endpoint investigations including live memory scans, 180 million files analyzed, and telemetry from 7 million IP addresses, 3 million domains and URLs, and over 550,000 phishing emails.

The patterns that emerge from this data tell a consistent story. Threat actors are exploiting the predictable gaps created by constrained, severity-based security operations, and they are doing it systematically. Understanding where those gaps actually live requires looking at the full alert picture, starting with the category most teams have been conditioned to ignore.

## The 1% problem that adds up to one missed breach per week

In this analysis of 25M alerts, nearly 1% of confirmed incidents originated from alerts initially classified as low-severity or informational. On endpoints specifically, that figure climbed to nearly 2%.

At enterprise scale, percentages like these are not noise. The average organization generates approximately 450,000 alerts per year. One percent of that is roughly 54 real threats annually, about one per week, that never get investigated under a traditional SOC or MDR model. Detection did not fail. Triage economics just made investigation impossible.

These are not theoretical risks sitting at the edge of an attacker's wishlist. They are real compromises hiding in the category of alerts that operations teams have been trained to deprioritize.

## EDR "mitigated" does not mean clean

Endpoint findings from the report deserve special attention because they challenge a foundational assumption in most security programs: that EDR remediation can be trusted at face value.

Of the 82,000 alerts that underwent live forensic memory scans, 2,600 had active infections. Of those confirmed compromised endpoints, 51% had already been marked as "mitigated" by the source EDR vendor.

In over half of confirmed endpoint compromises detected through forensic analysis, the EDR had closed the ticket and declared the threat resolved. Without memory-level forensics, those infections remain invisible. The tools most organizations rely on as their endpoint safety net are reporting clean on machines that are not clean.

The malware families found running in memory during these scans include Mimikatz, Cobalt Strike, Meterpreter, and StrelaStealer, not obscure proof-of-concept tools, but the workhorses of active criminal and nation-state operations.

## Phishing has left your email gateway behind

The phishing data in the report reflects a fundamental shift in attacker methodology that most email security architectures are not designed to catch.

Less than 6% of confirmed malicious phishing emails contained attachments. Most relied on links and language. More significantly, attackers have migrated their infrastructure onto platforms that are trusted by default: Vercel, CodePen, OneDrive, and even PayPal's own invoicing system.

One campaign documented in the report uses PayPal's legitimate payment request infrastructure to send threat emails, with callback numbers embedded in the payment notes and Unicode homoglyphs to defeat signature-based detection. The sending domain passes every standard authentication check because the mail genuinely originates from PayPal.

Cloudflare Turnstile CAPTCHA has become a reliable signal of malicious intent: sites using it were consistently more likely to be phishing pages, while Google reCAPTCHA correlated with legitimate infrastructure. Attackers are using the mechanisms built to stop bots to stop automated security scanners instead.

Four new techniques for bypassing email gateways were identified in the data: Base64 payloads hidden inside SVG image files, links embedded in PDF annotation metadata invisible to surface-level scanners, dynamically loaded phishing pages served through legitimate OneDrive shares, and DOCX files concealing archived HTML content containing QR codes. None of these is exotic. They are operational techniques being used at scale.

## Cloud telemetry shows attackers playing long games

Cloud alert data from the report shows a pronounced concentration around defense evasion and persistence tactics, with relatively few high-impact behaviors like lateral movement or privilege escalation appearing in the signal.

Attackers are being both cautious and patient. The dominant pattern is long-term access. Token manipulation, abuse of legitimate cloud features, andobfuscation to avoid triggering higher-severity detections. The goal is to remain present and undetected, not to make noise.

AWS misconfigurations compound this risk quietly. S3 accounts for roughly 70% of all cloud control violations in the dataset, with the most common issues centered on access management, server logging, and cross-account restrictions. These findings rarely trigger alerts. Most are classified as low severity. And they have been repeatedly exploited once attackers establish any foothold, dramatically accelerating what they can do next.

## Why traditional SOCs and MDRs cannot close this gap

This is an operational and capacity problem that technology alone did not solve until recently.

Human analysts do not scale with alert volume. As telemetry expands across endpoint, cloud, identity, network, and SaaS, every SOC eventually hits the same ceiling. The only way to operate within budget is aggressive triage: automate most closures, investigate only what looks critical, and trust that severity labels reflect reality. The 2026 data shows that trust is misplaced at scale.

MDR providers face identical constraints. The human-scaled operating model means approximately 60% of alerts still go unreviewed whether handled in-house or outsourced. Adding more analysts moves the ceiling but does not eliminate it. SOAR platforms give you workflow automation but require your team to design every playbook and still do not replace investigative execution.

The deeper problem is the feedback loop that never closes. When low-severity alerts are never investigated, missed threats never surface. Detection rules that fail to catch real attacks never get corrected. The system does not self-improve because the inputs it would need to improve are never examined.

## What changes when you investigate everything

Investigating all 25 million alerts in the above-cited report required removing the constraint that has historically made full coverage impossible. Specifically, human analyst capacity is the bottleneck. In this dataset,
[Intezer AI SOC](https://intezer.com/)
was used to triage and investigate, with less than 2% of alerts escalated to a human analyst, 98% verdict accuracy, and sub-minute median triage time across the full volume.

The effects of full-coverage investigation are measurable. When every alert receives forensic-grade analysis regardless of severity, triage outcomes are grounded in evidence rather than assumptions about what low-severity labels mean. Early-stage threats that produce only weak initial signals,get surfaced before they progress. Detection engineering also benefits directly, because every investigation generates feedback that can be looped back into rule tuning at the source.

The practical result for human analysts is a shift in where their time is spent. Escalations become less frequent and higher confidence, which means analysts engage at the point of decision rather than spending capacity on discovery and initial classification.

For the broader organization, this translates into a security posture that improves continuously rather than one that holds steady while the threat landscape moves around it.

**To explore the full report and research findings, see the
[2026 AI SOC Report for CISOs by Intezer](https://intezer.com/2026-ai-soc-report-for-cisos/)
.**

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.