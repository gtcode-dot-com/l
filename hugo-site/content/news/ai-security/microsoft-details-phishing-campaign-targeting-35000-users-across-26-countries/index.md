---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-05T08:15:15.374422+00:00'
exported_at: '2026-05-05T08:15:17.654383+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html
structured_data:
  about: []
  author: ''
  description: Microsoft disclosed a credential theft campaign targeting 35,000+ users
    at 13,000+ organizations across 26 countries.
  headline: Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries
updated_at: '2026-05-05T08:15:15.374422+00:00'
url_hash: c770a3b5aae9a20eca6c60606adc12926cc7f801
---

Microsoft has disclosed details of a large-scale credential theft campaign that has leveraged a combination of code of conduct-themed lures and legitimate email services to direct users to attacker-controlled domains and steal authentication tokens.

The multi-stage campaign, observed between April 14 and 16, 2026, targeted more than 35,000 users across over 13,000 organizations in 26 countries, with 92% of the targets located in the U.S. The majority of phishing emails were directed against healthcare and life sciences (19%), financial services (18%), professional services (11%), and technology and software (11%) sectors.

"The lures in this campaign used polished, enterprise-style HTML templates with structured layouts and preemptive authenticity statements, making them appear more credible than typical phishing emails and increasing their plausibility as legitimate internal communications," the Microsoft Defender Security Research Team and Microsoft Threat Intelligence
[said](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/)
.

"Because the messages contained accusations and repeated time-bound action prompts, the campaign created a sense of urgency and pressure to act."

The email messages used in the campaign employ lures related to code of conduct reviews, using display names like "Internal Regulatory COC," "Workforce Communications," and "Team Conduct Report." Subject lines associated with these emails include "Internal case log issued under conduct policy" and "Reminder: employer opened a non-compliance case log."

"At the top of each message, a notice stated that the message had been 'issued through an authorized internal channel' and that links and attachments had been 'reviewed and approved for secure access,' reinforcing the email's purported legitimacy," Microsoft explained.

It's assessed that the emails are sent from a legitimate email delivery service. The messages also come with a PDF attachment that purportedly gives additional information about the conduct review, luring victims to click on a link within the document to initiate the credential harvesting flow.

The attack chain has been found directing victims through multiple rounds of CAPTCHA and intermediate pages that are designed to lend the scheme a veneer of legitimacy, at the same time keeping out automated defenses.

Ultimately, it ends with a sign-in experience that leverages adversary‑in‑the‑middle (AiTM) phishing tactics to harvest Microsoft credentials and tokens in real-time, effectively allowing the threat actors to bypass multi-factor authentication (MFA). The final destination, per Microsoft, depends on whether the malicious flow was triggered from a mobile device or a desktop system.

### Phishing Trends in 2026

The disclosure comes as Microsoft's analysis of the email threat landscape between January and March 2026 revealed that QR code phishing emerged as the fastest-growing attack vector, while CAPTCHA-gated phishing evolved "rapidly" across payload types. In all, the tech giant said it detected about 8.3 billion email-based phishing threats.

Of these, nearly 80% were link-based, where large HTML and ZIP files accounted for a huge chunk of the malicious payloads distributed via phishing emails. The end goal of a vast majority of these attacks was credential harvesting, with malware delivery declining to a mere 5-6% by the end of the quarter.

Microsoft also said the operators of the Tycoon 2FA phishing-as-a-service (PhaaS) platform have attempted to shift hosting providers and domain registration patterns following a
[coordinated disruption operation](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html)
in March 2026.

"Toward the end of March, we saw Tycoon 2FA moving away from Cloudflare as a hosting service and now hosts most of its domains across a variety of alternative platforms, suggesting the group is attempting to find replacement services that offer comparable anti-analysis protections," it
[added](https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/)
.

In a report published back in February, Palo Alto Networks Unit 42
[highlighted](https://unit42.paloaltonetworks.com/qr-codes-as-attack-vector/)
how threat actors are abusing QR codes as URL shorteners to disguise malicious destinations, in-app deep links to steal account credentials, and bypass app store security by linking to direct downloads of malicious apps.

Data from Microsoft shows a massive surge in QR code phishing during the three-month time period, as attack volumes jumped from 7.6 million in January to 18.7 million in March, representing a 146% increase. One notable development observed in late March was the use of QR codes embedded directly in email bodies.

Business email compromise (BEC) scams, on the other hand, exhibited more fluctuations, crossing more than 4 million in attack volume in March 2026, up from over 3.5 million in January and more than 3 million in February. Collectively, 10.7 million BEC attacks were recorded.

Two noteworthy campaigns observed during Q1 2026 are below -

* A large, sustained campaign between February 23 and February 25, 2026, that sent more than 1.2 million messages to users at more than 53,000 organizations in 23 countries, using 401(k)-, payment-, and invoice-themed lures to serve an SVG attachment. Opening the file directed the victims to a CAPTCHA check, successfully completing which, they were shown a fake sign-in page to compromise their accounts.
* A massive campaign on March 17, 2026, that involved more than 1.5 million confirmed malicious messages sent to over 179,000 organizations across 43 countries. The activity accounted for 7% of all malicious HTML attachments observed in the month. When opened, the HTML file redirected victims to an initial phishing page that screened the visitor before routing them to the final destination: a phishing page that presented a CAPTCHA challenge before serving a fraudulent sign‑in page.

"Interestingly, although messages in this campaign shared common tooling, structure, and delivery characteristics, the infrastructure hosting the final phishing payload was linked to multiple different PhaaS providers," Microsoft said. "Most observed phishing endpoints were associated with Tycoon 2FA, while additional activity was linked to
[Kratos](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html)
(formerly Sneaky 2FA) and
[EvilTokens](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html)
infrastructure."

The findings coincide with the emergence of phishing and BEC campaigns that abuse Amazon Simple Email Service (
[SES](https://aws.amazon.com/ses/)
) as a delivery vector to bypass SPF, DKIM, and DMARC checks, and facilitate credential theft via phony sign-in pages. These attacks often work by gaining access to Amazon SES through
[leaked AWS access keys](https://www.repost.aws/articles/ARoBXj63rWSt2Ww7XKlVV72g/how-aws-responds-to-exposed-credentials-and-how-you-can-protect-your-account)
.

"The insidious nature of Amazon SES attacks lies in the fact that attackers aren't using suspicious or dangerous domains; instead, they are leveraging infrastructure that both users and security systems have grown to trust," Kaspersky
[said](https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/)
.

"By weaponizing this service, attackers avoid the effort of building dubious domains and mail infrastructure from scratch. Instead, they hijack existing access keys to gain the ability to blast out thousands of phishing emails. These messages pass email authentication, originate from IP addresses that are unlikely to be blocklisted, and contain links to phishing forms that look entirely legitimate."