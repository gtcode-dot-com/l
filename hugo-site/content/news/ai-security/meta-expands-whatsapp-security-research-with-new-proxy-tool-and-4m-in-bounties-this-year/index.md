---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-19T01:01:25.339547+00:00'
exported_at: '2025-11-19T01:01:27.614376+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/meta-expands-whatsapp-security-research.html
structured_data:
  about: []
  author: ''
  description: Meta expands WhatsApp security research, reveals $4M payouts, new proxy
    tool, and patched high-severity flaws.
  headline: Meta Expands WhatsApp Security Research with New Proxy Tool and $4M in
    Bounties This Year
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/meta-expands-whatsapp-security-research.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Meta Expands WhatsApp Security Research with New Proxy Tool and $4M in Bounties
  This Year
updated_at: '2025-11-19T01:01:25.339547+00:00'
url_hash: 46835e613ecd86cc0694c0f63b22b53fe841a9ef
---

Meta on Tuesday said it has made available a tool called
**WhatsApp Research Proxy**
to some of its long-time bug bounty researchers to help improve the program and more effectively research the messaging platform's network protocol.

The idea is to make it easier to delve into WhatsApp-specific technologies as the application continues to be a
[lucrative attack surface](https://thehackernews.com/2025/08/whatsapp-issues-emergency-update-for.html)
for state-sponsored actors and commercial spyware vendors.

The company also noted that it's setting up a pilot initiative where it's inviting research teams to focus on platform abuse with support for internal engineering and tooling. "Our goal is to lower the barrier of entry for academics and other researchers who might not be as familiar with bug bounties to join our program," it
[added](https://bugbounty.meta.com/blog/15th-anniversary-2025/)
.

The development comes as the social media giant said it has awarded more than
[$25 million in bug bounties](https://engineering.fb.com/2025/02/13/security/looking-back-at-our-bug-bounty-program-in-2024/)
to over 1,400 researchers from 88 countries in the last 15 years, out of which more than $4 million were paid out this year alone for almost 800 valid reports. In all, Meta said it received around 13,000 submissions.

Some of the notable bug discoveries included an incomplete validation bug in WhatsApp prior to v2.25.23.73, WhatsApp Business for iOS v2.25.23.82, and WhatsApp for Mac v2.25.23.83 that could have enabled a user to trigger processing of content retrieved from an arbitrary URL on another user's device. There is no evidence that the issue was exploited in the wild.

Meta also released an operating system-level patch to mitigate the risk posed by a
[vulnerability](https://unity.com/security/sept-2025-01)
tracked as
[CVE-2025-59489](https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/)
(CVSS score: 8.4) that could have allowed malicious applications installed on Quest devices to manipulate Unity applications to achieve arbitrary code execution. Flatt Security researcher RyotaK has been acknowledged for discovering and reporting the flaw.

## Simple WhatsApp Security Flaw Exposes 3.5 Billion Phone Numbers

Lastly, Meta said it added anti-scraping protections to WhatsApp following a
[report](https://github.com/sbaresearch/whatsapp-census)
that detailed a novel method to enumerate WhatsApp accounts at scale across 245 countries and build a dataset containing every user, bypassing the service's rate-limiting restrictions. WhatsApp has about 3.5 billion active users.

The attack takes advantage of a legitimate WhatsApp contact discovery feature that requires users to first determine whether their contacts are registered on the platform. It essentially allows an attacker to compile basic publicly accessible information, along with their profile photos, About text, and timestamps associated with key updates related to the two attributes. Meta said it found no indications that this vector was ever abused in a malicious context.

Interestingly, the study found millions of phone numbers registered to WhatsApp in countries where it's officially banned, including 2.3 million in China and 1.6 million in Myanmar.

"Normally, a system shouldn't respond to such a high number of requests in such a short time – particularly when originating from a single source," Gabriel Gegenhuber, University of Vienna researcher and lead author of the study,
[said](https://www.univie.ac.at/en/news/detail/forscherinnen-entdecken-grosse-sicherheitsluecke-in-whatsapp)
. "This behavior exposed the underlying flaw, which allowed us to issue an effectively unlimited requests to the server and, in doing so, map user data worldwide."

"We had already been working on industry-leading anti-scraping systems, and this study was instrumental in stress-testing and confirming the immediate efficacy of these new defenses," Nitin Gupta, vice president of engineering at WhatsApp, told The Hacker News in a statement.

"Importantly, the researchers have securely deleted the data collected as part of the study, and we have found no evidence of malicious actors abusing this vector. As a reminder, user messages remained private and secure thanks to WhatsApp’s default end-to-end encryption, and no non-public data was accessible to the researchers."

Earlier this year, Gegenhuber et al also
[demonstrated](https://arxiv.org/abs/2411.11194)
another research titled Careless Whisper that showed how delivery receipts can pose significant privacy risks to users, thereby allowing an attacker to send specifically crafted messages that can trigger delivery receipts without their knowledge or consent and extract their activity status.

"By using this technique at high frequency, we demonstrate how an attacker could extract private information, such as following a user across different companion devices, inferring their daily schedule, or deducing current activities," the researchers noted.

"Moreover, we can infer the number of currently active user sessions (i.e., main and companion devices) and their operating system, as well as launch resource exhaustion attacks, such as draining a user's battery or data allowance, all without generating any notification on the target side."

*(The story was updated after publication to include a response from WhatsApp and make it clear that CVE-2025-59489 was patched and issued by Unity.)*