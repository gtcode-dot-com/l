---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T16:53:31.950402+00:00'
exported_at: '2026-09-26T16:53:33.554978+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html
structured_data:
  about: []
  author: ''
  description: Mirage2FA targets Microsoft 365, with 48% of targeted emails potentially
    compromised and 9,000+ potential session-theft events.
  headline: Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365
    Login Flows
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login
  Flows
updated_at: '2026-09-26T16:53:31.950402+00:00'
url_hash: 02168dcbba55cff42f2e74d2b0e1af99f8eb417b
---

Thousands of companies have been affected by the Mirage2FA campaign from 2024 to 2026. The commercial phishing-as-a-service toolkit targets Microsoft 365 accounts by abusing legitimate login flows and bypassing two-factor authentication.

According to
[ANY.RUN](https://any.run/?utm_source=the+hacker+news&amp;utm_medium=article&amp;utm_campaign=mirage+usa&amp;utm_content=landing&amp;utm_term=250826)
research, 48% of targeted email addresses were potentially compromised. Most of the affected companies are US-based.

## Mirage2FA Campaign Scope and Impact

By stealing passwords and session cookies, attackers can gain access to authenticated Microsoft 365 sessions and SSO-connected services. This creates significant identity-related risks for companies, potentially exposing corporate email, trusted business accounts, and other sensitive data.

Once an authenticated Microsoft 365 session is hijacked, a path for impersonation, fraud, and further compromise is created.

|  |
| --- |
|  |
| Key takeaways about Mirage2FA by ANY.RUN |

The campaign has a broad geographic and corporate reach. Apart from the United States accounting for 63.7% of the total victims, Mirage2FA activity was also observed in India, Singapore, the United Kingdom, Canada, Saudi Arabia, South Africa, and other countries.

Overall, Mirage2FA activity is potentially linked to 4,532 unique organization email domains. Technology, manufacturing, and education were among the most targeted industries.

A major part of the risk for affected companies comes from session theft. ANY.RUN’s research uncovered more than 9,000 potential compromise events involving cookie and password theft, SSO logins, and 2FA bypass.

Findings from ANY.RUN research show how AiTM attacks can exploit gaps in authentication and session management even when two-factor authentication is in place.

The impact can also extend beyond the initially compromised account. Follow-on access, SSO-connected apps, and other internal workflows can increase the attack radius, further increasing containment costs.

Another costly factor is that impact goes beyond password theft, as attackers gain access to the corporate environment or Microsoft 365 services through hijacked user sessions, making it harder to take swift measures.

## How to Reduce Mirage2FA Risk in Your Company

Organizations can reduce exposure by strengthening authentication, detecting campaign behavior, and treating session theft as an identity incident.

### Detect Attacks Earlier with Deeper Analysis

|  |
| --- |
|  |
| Mirage2FA analysis in ANY.RUN’s Interactive Sandbox |

Seamlessly integrating sandboxing into existing workflows helps SOC teams safely investigate suspicious content and identify phishing behavior before it leads to account compromise.

|  |  |
| --- | --- |
| **Enterprise Security Tip** | **How ANY.RUN Helps** |
| Analyze suspicious attachments and URLs in isolation. | [Interactive Sandbox](https://www.google.com/url?q=https://any.run/features/?utm_source%3Dthe%2Bhacker%2Bnews%26utm_medium%3Darticle%26utm_campaign%3Dmirage%2Busa%26utm_content%3Dfeatures%26utm_term%3D250826&amp;sa=D&amp;source=editors&amp;ust=1787661766357777&amp;usg=AOvVaw1qjaNQ-9L_RQ0aSRdQhRvn) exposes redirects, scripts, WebSocket activity, and fake Microsoft 365 login pages. |
| Move beyond traditional MFA. Use phishing-resistant authentication and stronger session controls. | Sandbox analysis helps identify attacks designed to bypass traditional authentication controls. |

These measures help security teams detect Mirage2FA activity earlier, investigate its wider scope, and limit the impact of session theft.

Lower the cost of account compromise with early detection with ANY.RUN.

Detect threats in 14 sec and cut MTTR by 21 mins per case.

[Integrate ANY.RUN in your SOC](https://any.run/enterprise/?utm_source=the+hacker+news&amp;utm_medium=article&amp;utm_campaign=mirage+usa&amp;utm_content=enterprise+sales&amp;utm_term=250826#contact-sales)

### Uncover the Infrastructure Behind Campaigns

Mirage2FA activity should be investigated beyond individual IOCs. Recurring loaders, encoded data, suspicious WebSocket activity, and related infrastructure can help reveal connections to a wider campaign.

|  |
| --- |
|  |
| ANY.RUN’s Threat Intelligence Feeds: how they work and what impact they bring |

Session theft should be treated as an identity incident. Teams should revoke compromised sessions and tokens and investigate activity tied to the affected identity rather than relying on a password reset alone.

Integration of real-time
[Threat Intelligence Feeds](https://any.run/threat-intelligence-feeds/?utm_source=the+hacker+news&amp;utm_medium=article&amp;utm_campaign=mirage+usa&amp;utm_content=ti+feeds&amp;utm_term=250826)
provides fresh malicious indicators that complement behavioral detections as attacker infrastructure changes. Analysts can then use
[Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=the+hacker+news&amp;utm_medium=article&amp;utm_campaign=mirage+usa&amp;utm_content=ti+lookup&amp;utm_term=250826)
to pivot from suspicious URLs, domains, IPs, and files to related infrastructure and activity.

Turn isolated IOCs into actionable intelligence backed by threat data from 16,000+ organizations.

[Explore ANY.RUN](https://any.run/plans-ti/?utm_source=the+hacker+news&amp;utm_medium=article&amp;utm_campaign=mirage+usa&amp;utm_content=ti+plans+sales&amp;utm_term=250826#contact-sales)

## Conclusion

Mirage2FA shows how phishing has evolved beyond credential theft. By hijacking Microsoft 365 sessions, attackers can bypass conventional MFA and gain access through trusted user identities.

With thousands of organizations affected, particularly in the US, businesses need to prioritize phishing-resistant authentication, behavioral detection, and response procedures designed for session theft.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.