---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-28T12:00:09.270860+00:00'
exported_at: '2025-11-28T12:00:11.553432+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/ms-teams-guest-access-can-remove.html
structured_data:
  about: []
  author: ''
  description: Attackers exploit Teams guest access and unprotected external tenants
    to bypass Microsoft Defender safeguards
  headline: MS Teams Guest Access Can Remove Defender Protection When Users Join External
    Tenants
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/ms-teams-guest-access-can-remove.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MS Teams Guest Access Can Remove Defender Protection When Users Join External
  Tenants
updated_at: '2025-11-28T12:00:09.270860+00:00'
url_hash: ff2f2dd156d49e4403f81baa26b2d0ead39f0da9
---

**

Nov 28, 2025
**

Ravie Lakshmanan

Email Security / Enterprise Security

Cybersecurity researchers have shed light on a cross-tenant blind spot that allows attackers to bypass Microsoft Defender for Office 365 protections via the
[guest access](https://learn.microsoft.com/en-us/microsoftteams/guest-experience)
feature in Teams.

"When users operate as guests in another tenant, their protections are determined entirely by that hosting environment, not by their home organization," Ontinue security researcher Rhys Downing
[said](https://www.ontinue.com/resource/blog-microsoft-chat-with-anyone-understanding-phishing-risk/)
in a report.

"These advancements increase collaboration opportunities, but they also widen the responsibility for ensuring those external environments are trustworthy and properly secured."

The development comes as Microsoft has begun rolling out a new feature in Teams that allows users to chat with anyone via email, including those who don't use the enterprise communications platform, starting this month. The change is expected to be globally available by January 2026.

"The recipient will receive an email invitation to join the chat session as a guest, enabling seamless communication and collaboration," Microsoft
[said](https://mc.merill.net/message/MC1182004)
in its announcement. "This update simplifies external engagement and supports flexible work scenarios."

In the event the recipient already uses Teams, they are notified via the app directly in the form of an external message request. The feature is enabled by default, but organizations can turn it off using the TeamsMessagingPolicy by
[setting](https://learn.microsoft.com/en-us/powershell/module/microsoftteams/set-csteamsmessagingpolicy)
the "UseB2BInvitesToAddExternalUsers" parameter to "false."

That said, this setting only prevents users from sending invitations to other users. It does not stop them from receiving invitations from external tenants.

At this stage, it's worth mentioning that
[guest access](https://learn.microsoft.com/en-us/microsoftteams/guest-access)
is different from
[external access](https://learn.microsoft.com/en-us/microsoftteams/communicate-with-users-from-other-organizations)
, which allows users to find, call, and chat with people who have Teams but are outside of their organizations.

The "fundamental architectural gap" highlighted by Ontinue stems from the fact that
[Microsoft Defender for Office 365 protections](https://learn.microsoft.com/en-us/defender-office-365/mdo-support-teams-about)
for Teams may not apply when a user accepts a guest invitation to an external tenant. In other words, by entering the other tenant's security boundary, the user is subjected to security policies where the conversation is hosted and not where the user's account lives.

What's more, it opens the door to a scenario where the user can become an unprotected guest in a malicious environment that's dictated by the attacker's security policies.

In a hypothetical attack scenario, a threat actor can create "protection-free zones" by disabling all safeguards in their tenants or avail licenses that lack certain options by default. For instance, the attacker can spin up a malicious Microsoft 365 tenant using a low-cost license such as Teams Essentials or Business Basic that doesn't come with Microsoft Defender for Office 365 out of the box.

Once the unprotected tenant is set up, the attacker can then conduct reconnaissance of the target organization to gather more information and initiate contact via Teams by entering a victim's email address, causing Teams to send an automated invitation to join the chat as a guest.

Perhaps the most concerning aspect of the attack chain is that the email lands on the victim's mailbox, given that the message originates from Microsoft's own infrastructure, effectively bypassing SPF, DKIM, and DMARC checks. Email security solutions are unlikely to flag the email as malicious, as it's legitimately from Microsoft.

Should the victim end up accepting the invitation, they are granted guest access in the attacker's tenant, where all subsequent communication takes place. The threat actor can send phishing links or distribute malware-laced attachments by taking advantage of the lack of Safe Links and Safe Attachments scans.

"The victim's organization remains completely unaware," Downing said. "Their security controls never triggered because the attack occurred outside their security boundary."

To safeguard against this line of attack, organizations are recommended to restrict B2B collaboration settings to only allow guest invitations from trusted domains, implement cross-tenant access controls, restrict external Teams communication if not required, and train users to watch out for unsolicited Teams invites from external sources.

The Hacker News has reached out to Microsoft for comment, and we will update the story if we hear back.