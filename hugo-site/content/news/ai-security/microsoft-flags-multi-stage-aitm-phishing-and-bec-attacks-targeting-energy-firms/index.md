---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-23T10:15:17.351713+00:00'
exported_at: '2026-01-23T10:15:19.559465+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html
structured_data:
  about: []
  author: ''
  description: Microsoft reports a multi-stage AitM phishing and BEC campaign abusing
    SharePoint, inbox rules, and stolen session cookies to target energy orgs.
  headline: Microsoft Flags Multi-Stage AitM Phishing and BEC Attacks Targeting Energy
    Firms
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Flags Multi-Stage AitM Phishing and BEC Attacks Targeting Energy
  Firms
updated_at: '2026-01-23T10:15:17.351713+00:00'
url_hash: c3c1b74d9b8ea400ea9c0a74c5096f3e1477eafd
---

Microsoft has warned of a multi‑stage adversary‑in‑the‑middle (
[AitM](https://thehackernews.com/2023/06/microsoft-uncovers-banking-aitm.html)
) phishing and business email compromise (BEC) campaign targeting multiple organizations in the energy sector.

"The campaign abused SharePoint file‑sharing services to deliver phishing payloads and relied on inbox rule creation to maintain persistence and evade user awareness," the Microsoft Defender Security Research Team
[said](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)
. "The attack transitioned into a series of AitM attacks and follow-on BEC activity spanning multiple organizations."

As part of post-exploitation activity following initial compromise, the unknown attackers have been found to leverage trusted internal identities from the victim to carry out large‑scale intra‑organizational and external phishing in an effort to cast a wide net and widen the scope of the campaign.

The starting point of the attack is a phishing email likely sent from an email address belonging to a trusted organization, which was compromised beforehand. Abusing this legitimate channel, the threat actors sent out messages masquerading as SharePoint document‑sharing workflows to give it a veneer of credibility and trick recipients into clicking on phishing URLs.

Because services like SharePoint and OneDrive are widely used in enterprise environments and the emails originate from a legitimate address, they are unlikely to raise suspicion, allowing adversaries to deliver phishing links or stage malicious payloads. This approach is also called living-off-trusted-sites (
[LOTS](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)
), as it weaponizes the familiarity and ubiquity of such platforms to subvert email‑centric detection mechanisms.

The URL, for its part, redirects users to a fake credential prompt to view the purported document. Armed with access to the account using the stolen credentials and the session cookie, the attackers create inbox rules to delete all incoming emails and mark all emails as read. With this foundation in place, the compromised inbox is used to send phishing messages containing a fake URL designed to conduct credential theft using an AitM attack.

In one case, Microsoft said the attacker initiated a large-scale phishing campaign involving more than 600 emails that were sent to the compromised user's contacts, both within and outside of the organization. The threat actors have also been observed taking steps to delete undelivered and out of office emails, and assure message recipients of the email's authenticity if they raised any concerns. The correspondence is then deleted from the mailbox.

"These techniques are common in any BEC attacks and are intended to keep the victim unaware of the attacker's operations, thus helping in persistence," the Windows maker noted.

Microsoft said the attack highlights the "operational complexity" of AitM, stating password resets alone cannot remediate the threat, as impacted organizations must ensure that they have revoked active session cookies and removed attacker-created inbox rules used to evade detection.

To that end, the company noted that it worked with customers to revoke multi-factor authentication (MFA) changes made by the attacker on the compromised user's accounts and delete suspicious rules created on those accounts. It's currently not known how many organizations were compromised and if it's the work of any known cybercrime group.

Organizations are advised to work with their identity provider to make sure security controls like phishing-resistant MFA are in place, enable
[conditional access policies](https://learn.microsoft.com/azure/active-directory/fundamentals/concept-fundamentals-security-defaults)
, implement
[continuous access evaluation](https://learn.microsoft.com/azure/active-directory/conditional-access/concept-continuous-access-evaluation)
, and use anti-phishing solutions that monitor and scan incoming emails and visited websites.

The attack outlined by Microsoft highlights the
[ongoing trend](https://www.netcraft.com/blog/shared-document-spam-delivers-remote-access-tool)
among threat actors to
[abuse trusted services](https://www.netcraft.com/blog/confluence-svg-rfp-phishing-scam)
such as Google Drive, Amazon Web Services (AWS), and Atlassian's Confluence wiki to redirect to credential harvesting sites and stage malware. This eliminates the need for attackers to build out their own infrastructure as well as makes malicious activity appear legitimate.

The disclosure comes as identity services provider Okta said it detected custom phishing kits that are designed specifically for use in voice phishing (aka vishing) campaigns targeting Google, Microsoft, Okta, and a wide range of cryptocurrency platforms. In these campaigns, the adversary, posing as tech support personnel, calls prospective targets using a spoofed support hotline or company phone number.

The attacks aim to trick users into visiting a malicious URL and hand over their credentials, which are subsequently relayed to the threat actors in real-time via a Telegram channel, granting them unauthorized access to their accounts. The social engineering efforts are well planned, with the attackers conducting reconnaissance on the targets and crafting customized phishing pages.

The kits, sold on an as-a-service basis, come fitted with client-side scripts that make it possible for threat actors to control the authentication flow in the browser of a targeted user in real-time, as they provide verbal instructions and convince them to take actions (e.g., approve push notifications or enter one-time passwords) that would lead to an MFA bypass.

"Using these kits, an attacker on the phone to a targeted user can control the authentication flow as that user interacts with credential phishing pages,"
[said](https://www.okta.com/blog/threat-intelligence/phishing-kits-adapt-to-the-script-of-callers/)
Moussa Diallo, threat researcher at Okta Threat Intelligence. "They can control what pages the target sees in their browser in perfect synchronization with the instructions they are providing on the call. The threat actor can use this synchronization to defeat any form of MFA that is not phishing-resistant."

In recent weeks, phishing campaigns have exploited Basic Authentication URLs (i.e., "username:password@domain[.]com") by placing a trusted domain in the username field, followed by an @ symbol and the actual malicious domain to visually mislead the victim.

"When a user sees a URL that begins with a familiar and trusted domain, they may assume the link is legitimate and safe to click," Netcraft
[said](https://www.netcraft.com/blog/retro-phishing-basic-auth-urls-make-a-comeback-in-japan)
. "However, the browser interprets everything before the @ symbol as authentication credentials, not as part of the destination. The real domain, or the one that the browser connects to, is included after the @ symbol."

Other campaigns have resorted to simple visual deception tricks like using "rn" in place of "m" to conceal malicious domains and deceive victims into thinking they are visiting a legitimate domain associated with companies like Microsoft ("rnicrosoft[.]com"), Mastercard ("rnastercard[.]de"), Marriott ("rnarriotthotels[.]com"), and Mitsubishi ("rnitsubishielectric[.]com"). This is called a
[homoglyph attack](https://thehackernews.com/2025/10/fake-nethereum-nuget-package-used.html)
.

"While attackers often aim at brands that start with the letter M for this technique, some of the most convincing domains come from swapping an internal 'm' with 'rn' inside words," Netcraft's Ivan Khamenka
[said](https://www.netcraft.com/blog/the-lowest-tech-homoglyph-that-wont-die)
. "This technique becomes even more dangerous when it appears in words that organizations commonly use as part of their brand, subdomains, or service identifiers. Terms like email, message, member, confirmation, and communication all contain mid-word m's that users barely process."