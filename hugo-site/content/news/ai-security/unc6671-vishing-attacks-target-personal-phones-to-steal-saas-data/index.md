---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-09T09:50:06.995571+00:00'
exported_at: '2026-08-09T09:50:08.399991+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html
structured_data:
  about: []
  author: ''
  description: UNC6671 uses vishing and AitM phishing to steal cloud credentials and
    MFA tokens, then exfiltrate data from Microsoft 365, Okta, and other SaaS apps.
  headline: UNC6671 Vishing Attacks Target Personal Phones to Steal SaaS Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: UNC6671 Vishing Attacks Target Personal Phones to Steal SaaS Data
updated_at: '2026-08-09T09:50:06.995571+00:00'
url_hash: 547060d28e7488d5422452d2ee0feb63b1403f7c
---

A
[recent wave](https://www.reuters.com/legal/government/major-wall-street-hedge-funds-targeted-attempted-cyberattacks-bloomberg-news-2026-08-05/)
of
[cyber attacks](https://www.bloomberg.com/news/articles/2026-08-05/major-hedge-funds-targeted-in-wave-of-attempted-cyberattacks)
targeting financial services, private equity, and professional services has been attributed to a data extortion group known as
**[UNC6671](https://thehackernews.com/2026/01/mandiant-finds-shinyhunters-using.html)**
.

"UNC6671 continues to rely on voice phishing (vishing) to target enterprise employees, posing as IT help desk staff facilitating mandatory, urgent security migrations. Significantly, the threat actor often contacts employees via their personal mobile devices," Google Threat Intelligence Group (GTIG) and Mandiant
[said](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments)
in a report.

These calls are designed to trick victims into spoofed login portals where adversary-in-the-middle (AitM) infrastructure intercepts credentials and multi-factor authentication (MFA) tokens. The threat actors then leverage the captured data to establish session persistence and deploy automated Python and PowerShell scripts for data exfiltration from enterprise cloud environments and SaaS applications, including Microsoft 365 and Okta.

According to the tech giant, UNC6671 has diversified its operations across multiple extortion brands including Redact,
[Pink](https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html#:~:text=Pink%2C%20a%20New%20Com%2DAffiliated%20Actor)
(aka CL-CRI-1147), Helix, and
[Falcon](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-07-15-CL-CRI-1182-activity.txt)
(aka CL-CRI-1182). UNC6671 was previously said to have operated under the
[BlackFile](https://unit42.paloaltonetworks.com/cyber-extortion-economy/)
(aka CL-CRI-1116) brand, targeting organizations via vishing and SSO compromise, before it was retired on May 11, 2026.

A timeline of some of the major events is as follows -

* Early January 2026 - UNC6671 emerges
* February 6, 2026 - BlackFile Data Leak Site (DLS) launches
* Late April 2026 - BlackFile DLS site goes offline
* May 11, 2026 - BlackFile DLS site briefly comes back online to share a message that it's shutting down the brand "under this name"
* May 19, 2026 - Redact operators state on their new DLS site "all operations under the BlackFile name have been officially and permanently ceased"
* May 31, 2026 - Pink DLS site launches
* June 27, 2026 - Redact claims that the original BlackFile brand had been compromised and hijacked by a former associate, who allegedly carried out unsanctioned extortion campaigns under their name

UNC6671 was first documented by Google in January 2026 as one of the threat clusters leveraging tradecraft traditionally associated with a financially motivated hacking group known as ShinyHunters (aka Bling Libra). Despite the similarities, it's assessed that the operations are acting independently of each other. The threat actor is known for maintaining a high operational cadence, targeting dozens of organizations in North America, Australia, and the U.K.

"These compromises are not the result of a security vulnerability in vendor products or infrastructure," the company
[noted](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)
at the time. "Instead, this campaign continues to highlight the effectiveness of social engineering and underscores the critical importance of organizations moving toward phishing-resistant MFA to protect their SaaS and identity platforms."

Cybersecurity company CrowdStrike, which is tracking the umbrella collective as Cordial Spider,
[characterized](https://thehackernews.com/2026/05/cybercrime-groups-using-vishing-and-sso.html)
the group as conducting rapid data theft and extortion campaigns by impersonating IT during vishing calls and creating a false sense of urgency centered around themes related to account issues or security updates to lead victims to fraudulent AitM pages that capture their authentication data and active session tokens in real time.

These credentials are then used to access the organization's identity provider (IdP), offering a "single point entry" into various SaaS applications. In tandem, the threat actors are known to establish persistence by registering adversary-controlled MFA devices to compromised accounts, but not before removing existing MFA devices.

"By abusing the trust relationship between the IdP and connected services, the adversaries bypass the need to compromise individual SaaS apps and instead move laterally across the victim's entire SaaS ecosystem with a single authenticated session," CrowdStrike said.

In an analysis of Pink's operations published in June 2026, SOCRadar described the group as focused on Big Game Hunting using tailored Okta and Microsoft Entra ID phishing kits, access gates to block sandboxes and researchers, and Cloudflare and DDoS-Guard for hosting and Tucows and Nicenic for domain registration.

"By combining vishing-driven social engineering with gated phishing infrastructure, they have demonstrated their intent to subvert modern security measures, including MFA and passkey authentication," the cybersecurity company
[said](https://socradar.io/blog/pink-data-extortion-group-phishing-kits/)
.

Some of the other notable tactics adopted by the threat actors include -

* Using credential harvesting panels hosted on generic root domains that purport to be related to passkeys, MFA, or SSO, while appending victim-specific subdomains to enable targeted voice phishing campaigns (e.g., passkeyhelpdesk[.]com, setupsso[.]com, and idokta[.]com). Some of these domains have been simultaneously used to target two entirely separate victims, each claimed by Falcon and Helix.
* Calling employees on their personal mobile numbers by spoofing the legitimate help desk phone number and directing them to a fake AitM phishing page.
* Relying on compromised email accounts to initiate password resets for non-SSO enterprise applications and systematically delete password-reset confirmations and security alerts for defense evasion.

Complementing these new techniques is a shift in the threat actor's targeting footprint: from large enterprises in the manufacturing, real estate, healthcare, and insurance sectors during April and May 2026, to technology, transportation, and hospitality firms in June 2026, and then to high-value financial and legal organizations in July 2026.

Google noted that UNC6671's adoption of multiple public extortion brands is likely an attempt to monetize their operations, compartmentalize negotiations, and frustrate tracking efforts. Between January 7 and May 12, 2026, Google said it tracked over $10.6 million in Bitcoin payments to wallets associated with the group.

Initial ransom demands reach north of $3 million, although the extortion operators opt for reductions between 50% and 75% of the initial ransom demand during negotiations. In more than 53% of tracked cases during the time period, the threat actors are said to have settled for an average of $750,000.

To counter the threat, organizations are recommended to enforce phishing-resistant MFA, integrate SaaS applications and cloud platforms with SSO, implement session controls, restrict authentication to trusted network sources, require corporate-managed devices for access, monitor IdP logs for suspicious MFA registration events, and deploy security tooling to alert if corporate password hashes are entered into unauthorized domains.

The findings demonstrate how modern extortion groups operate like decentralized corporate networks, using shared infrastructure across multiple public-facing brands to manage negotiations and insulate their operations.

"Regardless of whether this activity reflects a fractured threat group, outsourced extortion negotiators, or a broader affiliate network, the initial infection vector leveraged and goals of these campaigns are consistent," Google said.

Over the past year, a
[series of vishing campaigns](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)
has exhibited overlapping tradecraft with ShinyHunters-style activity to break into Salesforce instances, establish persistent access, and exfiltrate data by taking advantage of trusted OAuth relationships and supply chain compromise through trusted workflows and integrations such as
[Salesloft](https://thehackernews.com/2025/09/salesloft-takes-drift-offline-after.html)
,
[Gainsight](https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html)
, and
[Klue](https://thehackernews.com/2026/06/salesforce-disables-klue-app.html)
.

The disclosure comes as Bridewell documented an unsuccessful vishing campaign in which threat actors made an unsolicited call to an employee's personal device and attempted to redirect them to what's believed to be a fraudulent Okta login page under the pretext of accessing an internal incident ticket.

"When the employee attempted to redirect the caller to the official Service Desk, the caller refused, insisting they had been specifically routed to the employee directly, and offered an 'alternate way' to access the same ticket," security researcher Joshua Penny
[said](https://www.bridewell.com/insights/blogs/detail/vishing-call-to-a-shared-com-ecosystem)
. "On attempting this alternate access, the destination was blocked by existing security controls before any credential entry could occur."

"The employee informed the caller he would gather more information before proceeding; the caller disconnected and made no further contact."

It's believed that the attack is either the work of ShinyHunters or a threat actor operating a shared phishing-kit infrastructure consistent with Scattered LAPSUS$ Hunters (
[SLH](https://thehackernews.com/2026/02/slh-offers-5001000-per-call-to-recruit.html)
) tradecraft. It's worth pointing out that Google has also raised the possibility that the different groups operating under UNC6671 could be affiliates, splinter crews, or groups using the same underlying phishing infrastructure.

"The intrusion operators driving initial access and cloud data exfiltration could remain the same core group of actors, while the extortion and negotiation phases are outsourced to different actors," it added.

### Update

In a post shared on its data leak site, Falcon has claimed it's an exclusive Redact affiliate and that it's not associated with, or connected to, UNC6671. "We share no operators, infrastructure, tooling, negotiation channels, or proceeds with any group other than Redact," it added.

When reached for comment, a Google spokesperson told The Hacker News said it's aware of these claims, but said it had nothing further to share at this time.

*(The story was updated after publication to include the latest developments.)*