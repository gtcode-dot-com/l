---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-02T12:15:13.312183+00:00'
exported_at: '2026-01-02T12:15:15.589007+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/cybercriminals-abuse-google-cloud-email.html
structured_data:
  about: []
  author: ''
  description: Attackers misused Google Cloud Application Integration to send 9,394
    phishing emails from Google domains, bypassing filters and stealing credentials.
  headline: Cybercriminals Abuse Google Cloud Email Feature in Multi-Stage Phishing
    Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/cybercriminals-abuse-google-cloud-email.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Cybercriminals Abuse Google Cloud Email Feature in Multi-Stage Phishing Campaign
updated_at: '2026-01-02T12:15:13.312183+00:00'
url_hash: 65ff0022b0283b72dcd568884f26d8b0aadba3fc
---

**

Jan 02, 2026
**

Ravie Lakshmanan

Cloud Security / Email Security

Cybersecurity researchers have disclosed details of a phishing campaign that involves the attackers impersonating legitimate Google-generated messages by abusing Google Cloud's
[Application Integration](https://cloud.google.com/application-integration)
service to distribute emails.

The activity, Check Point said, takes advantage of the trust associated with Google Cloud infrastructure to send the messages from a legitimate email address ("noreply-application-integration@google[.]com") so that they can bypass traditional email security filters and have a better chance of landing in users' inboxes.

"The emails mimic routine enterprise notifications such as voicemail alerts and file access or permission requests, making them appear normal and trustworthy to recipients," the cybersecurity company
[said](https://blog.checkpoint.com/research/phishing-campaign-leverages-trusted-google-cloud-automation-capabilities-to-evade-detection/)
.

Attackers have been observed sending 9,394 phishing emails targeting approximately 3,200 customers over a 14-day period observed in December 2025, with the affected organizations located in the U.S., Asia-Pacific, Europe, Canada, and Latin America.

At the heart of the campaign is the abuse of Application Integration's "
[Send Email](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task)
" task, which allows users to send custom email notifications from an integration. Google notes in its support documentation that only a maximum of 30 recipients can be added to the task.

The fact that these emails can be configured to be sent to any arbitrary email addresses demonstrates the threat actor's ability to misuse a legitimate automation capability to their advantage and send emails from Google-owned domains, effectively bypassing
[DMARC and SPF checks](https://thehackernews.com/2025/01/neglected-domains-used-in-malspam-to.html)
.

"To further increase trust, the emails closely followed Google notification style and structure, including familiar formatting and language," Check Point said. "The lures commonly referenced voicemail messages or claims that the recipient had been granted access to a shared file or document, such as access to a 'Q4' file, prompting recipients to click embedded links and take immediate action."

The attack chain is a multi-stage redirection flow that commences when an email recipient clicks on a link hosted on storage.cloud.google[.]com, another trusted Google Cloud service. The effort is seen as another effort to lower user suspicion and give it a veneer of legitimacy.

The link then redirects the user to content served from googleusercontent[.]com, presenting them with a fake CAPTCHA or image-based verification that acts as a barrier by blocking automated scanners and security tools from scrutinizing the attack infrastructure, while allowing real users to pass through.

Once the validation phase is complete, the user is taken to a fake Microsoft login page that's hosted on a non-Microsoft domain, ultimately stealing any credentials entered by the victims.

In response to the findings, Google has blocked the phishing efforts that abuse the email notification feature within Google Cloud Application Integration, adding that it's taking more steps to prevent further misuse.

Check Point's analysis has revealed that the campaign has primarily targeted manufacturing, technology, financial, professional services, and retail sectors, although other industry verticals, including media, education, healthcare, energy, government, travel, and transportation, have been singled out.

"These sectors commonly rely on automated notifications, shared documents, and permission-based workflows, making Google-branded alerts especially convincing," it added. "This campaign highlights how attackers can misuse legitimate cloud automation and workflow features to distribute phishing at scale without traditional spoofing."