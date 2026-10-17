---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-17T22:10:36.719481+00:00'
exported_at: '2026-10-17T22:10:37.435785+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
structured_data:
  about: []
  author: ''
  description: Attackers used a compromised ConnectWise Cloud Backup credential for
    unauthorized sign-ins across 173 Microsoft 365 tenants.
  headline: Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft
    365 Tenants
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft
  365 Tenants
updated_at: '2026-10-17T22:10:36.719481+00:00'
url_hash: b3dabcb4d0c0986ad73ee47e5e64823262340c59
---

Cybersecurity researchers are sounding the alarm related to an active campaign in which
[unknown threat actors](https://www.reddit.com/r/msp/comments/1x7gw61/cwskykick_breach/)
are
[abusing](https://www.reddit.com/r/msp/comments/1x7wbwf/connectwise_skykick_update/)
a compromised Microsoft 365 (M365) credential belonging to ConnectWise Cloud Backup (formerly SkyKick) to gain unauthorized access to customers' M365 environments.

[ConnectWise Cloud Backup](https://www.connectwise.com/platform/bcdr/cloud-backup)
is a cloud-based backup and recovery service built for managed service providers (MSPs) to secure their clients' Microsoft 365 or Google Workspace data. To accomplish its tasks, the application is granted broad access to mailboxes, OneDrive, SharePoint, Teams, and directory data in every tenant on which it's installed.

Huntress said it has observed confirmed unauthorized sign-ins within 173 partner/customer tenants using the compromised vendor credential. The incident impacts every organization that has the app installed, and the credential works against every tenant the app is consented in.

"The app's credential is in hostile hands," security researcher Jonathan Semon
[said](https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access)
. "It was used to obtain Microsoft Graph tokens in customer tenants from 144.172.64[.]128 on October 15, between 06:13 and 08:34 UTC. The actor moved through tenants in sorted GUID order, a few seconds apart, which points to a script working from a target list."

In the observed attackers, the adversary has been observed authenticating to the app using their own tooling, in a manner analogous to the backup service, and obtains tokens with the app's existing permissions. Given that the app has extensive permissions to access customer data, an attacker in possession of the tokens can read mailboxes, files, and directory data the backup service can.

Huntress said the same IP address engaged in password spraying against four law firm tenants on October 13 and 14, 2026, although it said it detected no successful user sign-ins in its telemetry.

In at least one partner tenant, the cybersecurity company said it found a separate ConnectWise app assigning itself Global Administrator privileges and adding credentials to other trusted applications within this environment, thereby opening a pathway to other privileged apps within customer environments. This effectively extends the risk beyond the vendor account.

"The ConnectWise Cloud Management app for Microsoft Teams (application ID 24205314-2b89-4e07-a2a4-579e898a5640) added itself to the Global Administrator role, then ran a Python script (User-Agent Python-urllib/3.12) that modified two other applications in the tenant: an MSP management application, and Huntress's own application (Huntress Security Platform), adding new client secrets to both," Semon explained.

"The two applications that received new secrets are trusted, privileged tools. Adding a credential to an MSP management application can extend access beyond the one tenant, because those applications are often consented into the MSP's customers' tenants. A credential on a security tool's application gives the holder whatever that tool is permitted to do."

Todyl, in a similar analysis, said it detected an unauthorized party authenticating to Microsoft Graph as the ConnectWise Cloud Backup application.

"The access inherited the app's existing consent, which permits read/write access to mail and attachments (full mailbox access through Exchange Web Services), OneDrive and SharePoint files, and Teams chats, including the ability to restore data," Nicholas Koken, Todyl's head of Detection Engineering,
[said](https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app)
.

"Revoking user sessions does not end this access. Disabling the app in a tenant stops new tokens from being issued there, though tokens already issued stay valid for up to 90 minutes. Any tenant where the app is still enabled stays exposed until ConnectWise rotates the credential."

In response to the incident, ConnectWise
[has taken the step](https://www.connectwise.com/company/trust/advisories)
of closing Cloud Backup application access until further notice. The company said it has found no evidence that Cloud Backup partner backup data has been compromised. It has also shared the following steps to look for indicators of compromise -

* In the Microsoft Entra Admin Center, navigate to Monitoring → Sign-in logs, select the Service principal sign-ins tab, and filter by Application ID 506e08f9-6e9a-4da4-942b-a099a03644ae.
* The default User sign-ins tab will not display the required information.
* In the IP address column, review authentication activity originating from IP addresses outside expected Microsoft/Azure ranges. The application's normal egress has been identified as Azure private IPv6.
* Suspicious IP address: 144.172.64[.]128

"The backup service needs broad access to do its job, and an attacker using its credentials will inherit that level of access for every tenant where the app is installed," Huntress explained.

"Depending on the permissions in the tenant, that can include mailboxes, OneDrive and SharePoint files, Teams data, and directory information, much of it belonging to your clients. Some of that access, such as directory reads through Microsoft Graph, leaves no audit trail, which is why we suggest acting now instead of waiting for proof of access. The full potential impact depends on the permissions in play in each tenant."

Users are recommended to disable the application until ConnectWise confirms all credentials have been reset, enable Microsoft Graph activity logs, audit for any new credentials added since October 13, 2026, and check Entra audit logs for ConnectWise or SkyKick applications adding themselves to a directory role.

The development comes as Google's Mandiant and Google Threat Intelligence Group, along with ManageEngine Threat Analysis Lab,
[detailed](https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html)
an "ephemeral supply chain tampering" of the update infrastructure belonging to AOMEI Backupper, a data backup, disk cloning, and disaster recovery software, to bypass traditional security defenses and deliver malware such as CROSSROAD and SHINYROAD.

"The threat actor conducted repeated, short-burst configuration tampering against AOMEI origin servers," Google said. "Each tampering window remained active for only five to ten minutes before reverting to authentic versions. During the brief tampering windows, the threat actor modified the update settings file on the update server to redirect the software to download a malicious ZIP package from attacker-controlled servers instead of legitimate updates."

The ZIP archive contains CROSSROAD, an initial downloader responsible for environment validation and staging follow-on payloads. It's also designed to establish scheduled task-based persistence to deploy SHINYROAD, a modular backdoor framework for covert command-and-control, via DLL sideloading.

The software supply chain compromise campaign, which occurred between April and July 2026, has been attributed to a previously undocumented threat cluster codenamed UNC7017. The activity marks the first time that such a compromise has played out in brief intervals instead of maintaining a persistent, static modification on the servers.

The campaign is assessed to have impacted organizations spanning a wide range of sectors, including IT services, telecommunications, higher education, and related entities in Australia, Brazil, India, Pakistan, Portugal, Singapore, South Africa, Spain, Switzerland, Türkiye, and the U.S.

### An Active Supply Chain Attack

In a post on X, Microsoft
[said](https://x.com/MsftSecIntel/status/2111358888125878426)
it's tracking an "active supply chain attack in which a threat actor compromised the trusted OAuth App of the backup application ConnectWise Cloud Backup (AppId: 506e08f9-6e9a-4da4-942b-a099a03644ae), formerly SkyKick Backup, to obtain access tokens across customer tenants."

The tech giant said the threat actor likely abused permissions previously granted by customers to the application, including highly privileged permissions like Directory.ReadWrite.All.

"On October 15, 2026, we observed broad successful service principal authentication originating from the IP address 144.172.64[.]128," it added. "Follow-on activity included Microsoft Graph API reconnaissance and attempts to add additional credentials on the related service principal in target tenants to maintain direct access as a backdoor."

Microsoft is recommending that security teams review service principal sign-ins from unrecognized IP addresses, app credential changes, and OAuth grant activity associated with the aforementioned OAuth AppId.

ConnectWise, in a
[separate advisory](https://status.connectwise.com/)
, confirmed it has identified unauthorized access to application identities within the ConnectWise Cloud Backup environment. It has shut off Cloud Backup application access while its "investigation and remediation efforts remain ongoing."

Listed below are the application IDs the threat actor has abused as part of the activity -

* ConnectWise Cloud Backup - 506e08f9-6e9a-4da4-942b-a099a03644ae
* ConnectWise Cloud Management - 2399d300-6fca-4e6a-a686-399fefe75b83
* ConnectWise Cloud Management - MS Teams - 24205314-2b89-4e07-a2a4-579e898a5640
* ConnectWise Cloud Management - Exchange Online - b78f6a77-d4e5-46fb-87e5-d1648bd02519
* ConnectWise Cloud Management - MS Graph - 0de14c77-b9b0-4137-9360-34878a929827
* ConnectWise Cloud Management - Partner Center - 412dcf96-176d-4b3a-a1b0-4981ad66971e
* ConnectWise Cloud Management - SharePoint Online - b2b55f5b-7758-4719-8d8f-88ae172e6bdb

"When it comes to early exploitation and post-exploitation behaviors, we've observed what might be an affinity towards alphabetical targeting (our most interesting victims start with 'A')," Huntress said. "Although all tenants should be scrutinized, this pattern is worth sharing for prioritization."

*(This is a developing story. Please check back for more details.)*

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.