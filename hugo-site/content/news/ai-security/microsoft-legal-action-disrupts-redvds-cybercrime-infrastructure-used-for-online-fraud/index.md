---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-15T10:15:12.739261+00:00'
exported_at: '2026-01-15T10:15:15.126753+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/microsoft-legal-action-disrupts-redvds.html
structured_data:
  about: []
  author: ''
  description: Microsoft shut down RedVDS, a crimeware subscription service used for
    phishing and BEC fraud, linked to $40M U.S. losses and 191,000 affected orgs.
  headline: Microsoft Legal Action Disrupts RedVDS Cybercrime Infrastructure Used
    for Online Fraud
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/microsoft-legal-action-disrupts-redvds.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Legal Action Disrupts RedVDS Cybercrime Infrastructure Used for Online
  Fraud
updated_at: '2026-01-15T10:15:12.739261+00:00'
url_hash: 6b35016a61d7ae6e33c382f5a7b135753be4b60e
---

Microsoft on Wednesday announced that it has taken a "
[coordinated legal action](https://www.noticeofpleadings.net/redvds/index.html)
" in the U.S. and the U.K. to disrupt a cybercrime subscription service called
**RedVDS**
that has allegedly fueled millions in fraud losses.

The effort, per the tech giant, is part of a broader law enforcement effort in collaboration with law enforcement authorities that has allowed it to confiscate the malicious infrastructure and take the illicit service ("redvds[.]com") offline.

"For as little as US $24 a month, RedVDS provides criminals with access to disposable virtual computers that make fraud cheap, scalable, and difficult to trace,"
[said](https://blogs.microsoft.com/on-the-issues/2026/01/14/microsoft-disrupts-cybercrime/)
Steven Masada, assistant general counsel of Microsoft's Digital Crimes Unit. "Since March 2025, RedVDS‑enabled activity has driven roughly US $40 million in reported fraud losses in the United States alone."

Crimeware-as-a-service (CaaS) offerings have increasingly become a lucrative business model, transforming cybercrime from what once was an exclusive domain that required technical expertise into an underground economy where even inexperienced and aspiring threat actors can carry out complex attacks quickly and at scale.

These turnkey services span a wide spectrum of modular tools, ranging from phishing kits to stealers to ransomware, effectively contributing to the professionalization of cybercrime and emerging as a catalyst for sophisticated attacks.

Microsoft said RedVDS was advertised as an online subscription service that provides cheap and disposable virtual computers running unlicensed software, including Windows, so as to empower and enable criminals to operate anonymously and send high‑volume phishing emails, host scam infrastructure, pull off business email compromise (BEC) schemes, conduct account takeovers, and facilitate financial fraud.

Specifically, it served as a hub for purchasing unlicensed and inexpensive Windows-based Remote Desktop Protocol (RDP) servers with full administrator control and no usage limits through a feature-rich user interface. RedVDS, besides providing servers located in Canada, the U.S., France, the Netherlands, Germany, Singapore, and the U.K., also offered a reseller panel to create sub-users and grant them access to manage the servers without having to share access to the main site.

An FAQ section on the website noted that users can leverage its Telegram bot to manage their servers from within the Telegram app instead of having to log in to the site. Notably, the service did not maintain activity logs, making it an attractive choice for illicit use.

According to snapshots captured on the Internet Archive, RedVDS was advertised as a way to "increase your productivity and work from home with comfort and ease." The service, the maintainers said on the now-seized website, was first founded in 2017 and operated on Discord, ICQ, and Telegram. The website was launched in 2019.

"RedVDS is frequently paired with generative AI tools that help identify high‑value targets faster and generate more realistic, multimedia message email threads that mimic legitimate correspondences," the company said, adding it "observed attackers further augment their deception by leveraging face-swapping, video manipulation, and voice cloning AI tools to impersonate individuals and deceive victims."

|  |
| --- |
|  |
| RedVDS tool infrastructure |

Since September 2025, attacks fueled by RedVDS are said to have led to the compromise or fraudulent access of more than 191,000 organizations worldwide, underscoring the prolific reach of the service.

The Windows maker, which is tracking the developer and maintainer of RedVDS under the moniker Storm-2470,
[said](https://www.microsoft.com/en-us/security/blog/2026/01/14/inside-redvds-how-a-single-virtual-desktop-provider-fueled-worldwide-cybercriminal-operations/)
it has identified a "global network of disparate cybercriminals" leveraging the infrastructure provided by the criminal marketplace to strike multiple sectors, including legal, construction, manufacturing, real estate, healthcare, and education in the U.S., Canada, U.K., France, Germany, Australia, and countries with substantial banking infrastructure targets.

|  |
| --- |
|  |
| RedVDS attack chain |

Some of the notable threat actors include, Storm-2227, Storm-1575, Storm-1747, and phishing actors who used the
[RaccoonO365](https://thehackernews.com/2025/09/raccoono365-phishing-network-shut-down.html)
phishing kit prior to its disruption in September 2025. The infrastructure was specifically used to host a toolkit comprising both malicious and dual-use software -

* Mass spam/phishing email tools like SuperMailer, UltraMailer, BlueMail, SquadMailer, and Email Sorter Pro/Ultimate
* Email address harvesters like Sky Email Extractor to scrape or validate large numbers of email addresses
* Privacy and OPSEC tools like Waterfox, Avast Secure Browser, Norton Private Browser, NordVPN, and ExpressVPN
* Remote access tools like AnyDesk

One threat actor is said to have used the provisioned hosts to programmatically (and unsuccessfully) send emails via Microsoft Power Automate (Flow) using Excel, while other RedVDS users leveraged ChatGPT or other OpenAI tools to craft phishing lures, gather intelligence about organizational workflows to conduct fraud, and distribute phishing messages designed to harvest credentials and take control of victims' accounts.

|  |
| --- |
|  |
| RedVDS offerings |

The end goal of these attacks is to mount highly convincing BEC scams, permitting the threat actors to inject themselves into legitimate email conversations with suppliers and issue fraudulent invoices to trick targets into transferring funds to a mule account under their control.

Interestingly, its Terms of Service prohibited customers from using RedVDS for sending phishing emails, distributing malware, transferring illegal content, scanning systems for security vulnerabilities, or engaging in denial-of-service (DoS) attacks. This suggests the threat actors' apparent effort to limit or escape liability.

Microsoft further said it "identified attacks showing thousands of stolen credentials, invoices stolen from target organizations, mass mailers, and phish kits, indicating that multiple Windows hosts were all created from the same base Windows installation."

"Additional investigations revealed that most of the hosts were created using a single computer ID, signifying that the same Windows Eval 2022 license was used to create these hosts. By using the stolen license to make images, Storm-2470 provided its services at a substantially lower cost, making it attractive for threat actors to purchase or acquire RedVDS services."

The virtual Windows cloud servers were generated from a single Windows Server 2022 image, through RDP. All identified instances used the same computer name, WIN-BUNS25TD77J. It's assessed that Storm-2470 created one Windows virtual machine (VM) and repeatedly cloned it without changing the system identity.

The cloned Windows instances are created on demand using Quick Emulator (QEMU) virtualization technology combined with VirtIO drivers, with an automated process copying the master virtual machine (VM) image onto a new host every time a server is ordered in exchange for a cryptocurrency payment. This strategy made it possible to spin up fresh RDP hosts within minutes, allowing cybercriminals to scale their operations.

"Threat actors used RedVDS because it provided a highly permissive, low-cost, resilient environment where they could launch and conceal multiple stages of their operation," Microsoft said. "Once provisioned, these cloned Windows hosts gave actors a ready‑made platform to research targets, stage phishing infrastructure, steal credentials, hijack mailboxes, and execute impersonation‑based financial fraud with minimal friction.