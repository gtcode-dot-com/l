---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-13T00:02:29.765005+00:00'
exported_at: '2026-10-13T00:02:35.263461+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html
structured_data:
  about: []
  author: ''
  description: CyberXero's Claude Code-assisted campaign accessed 429 WordPress admin
    panels and exfiltrated over 628,000 records from four Ukrainian organizations.
  headline: CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian
    Records
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian Records
updated_at: '2026-10-13T00:02:29.765005+00:00'
url_hash: d261b6b9e669cf36d547dea5788a9f7e30811bf2
---

Cybersecurity researchers have disclosed details of a two-pronged artificial intelligence (AI)-augmented initial access campaign targeting WordPress sites, e-commerce platforms, and critical infrastructure entities in Ukraine.

The activity, which brings together commodity offensive tools like Cobalt Strike with an AI orchestration layer powered by Anthropic's Claude Code, has been attributed to a Russian-speaking, financially motivated initial access broker codenamed
**CyberXero**
. The threat actor is assessed to be active since at least July 2026.

"The operation runs two pipelines at once: a global, automated campaign against WordPress and e-commerce platforms, and a curated, manual campaign against Ukrainian energy and critical infrastructure," SOCRadar
[said](https://socradar.io/blog/cyberxero-ai-iab-ukraine-critical-infrastructure/)
in a report published last week.

The global campaign specifically focuses on known security flaws like
[wp2shell](https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html)
(CVE-2026-63030 and CVE-2026-60137) and
[CVE-2026-4815](https://www.incibe.es/en/incibe-cert/notices/aviso/multiple-vulnerabilities-support-board-schiocco)
, an SQL injection vulnerability impacting the Support Board WordPress plugin, to seize control of WordPress sites.

The campaign is estimated to have resulted in confirmed exfiltration from four Ukrainian organizations, leading to the harvesting of more than 628,000 records tied to Ukrainian individuals. Other confirmed compromises have occurred in Poland, China, and the Netherlands.

SOCRadar said it discovered the operation after it identified an exposed open directory hosted at "46.21.250[.]135" that leaked the threat actor's live working directory associated with a Linux workstation, including AI session logs, scripts with plaintext tokens, exploitation toolkits, reconnaissance output, AI agent configurations, and exfiltrated victim data. The campaign remains ongoing.

The opportunistic campaign aimed at WordPress and e-commerce platforms is designed for access and payment data, while the second campaign is a lot more targeted and geared towards deep reconnaissance and manual exploitation against Ukrainian energy and utilities, including a heating provider in Kharkiv.

Analysis of the exposed directory shows that a single automated execution scanned 4,708 targets, confirming access to 429 WordPress administration panels, followed by the deployment of 32 web shells in a 61-second window.

The attack architecture is based on a set of eight distinct nodes, including the threat actor's Linux workstation, a provisioning server, monetization infrastructure, payload staging servers, and a scanner that's responsible for identifying targets of interest.

CyberXero is said to have deployed AI in two independent stages of the attack lifecycle -

* Using Claude Code with a cluster of 51 specialized agents for scanning, exploit chaining, reconnaissance, and post-exploitation. It runs on the attacker's primary workstation.
* Connecting
  [PentAGI](https://github.com/vxcontrol/pentagi)
  (short for Penetration testing Artificial General Intelligence), an open-source, self-hosted AI Agent for fully-autonomous penetration testing, to Cobalt Strike through an AI provider API for payload generation and pentest execution. It runs on a Cobalt Strike
  [Team Server](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/welcome_starting-cs-team-server.htm)
  .

To get around model refusals, the threat actor has been observed using context-engineering and session-reset techniques,
[instructing the agent](https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html)
they were running an "authorized pentest on my own infrastructure."

"Model safety controls act on the context of a session, not on the model weights, so a refusal in one session does not carry into the next," SOCRadar explained. "When an agent refused a task, the actor reopened a fresh session, with the authorization framing preloaded and tried again."

"The logs also record genuine refusals that held: across four iterations the model declined to install a backdoor, disable a firewall, move laterally, and deploy a web shell, and in a separate episode it refused a scan four consecutive times and correctly rejected a forged ownership token."

Beyond WordPress and e-commerce exploitation, the campaign involves the exploitation of exposed Redis servers, resulting in the breach of two Chinese entities. Organizations running WordPress, Magento, or PrestaShop, or exposing Redis to the internet, are advised to check for rogue WordPress administrators, WSO web shells, and unexpected entries in ~/.ssh/authorized\_keys on Redis hosts.

"The opportunistic pipeline is global and automated, chasing access volume across e-commerce and WordPress with direct monetization through access sales or payment-data theft," SOCRadar said. "The directed pipeline is selective and geographically concentrated, aiming for deep reconnaissance and manual exploitation at Ukrainian critical infrastructure, with no obvious direct-monetization explanation."

### Operation Master Targets WordPress and PAN GlobalProtect Gateways

The disclosure comes as SOCRadar also
[detailed](https://socradar.io/blog/operation-master-intrusion-monetization-pipeline/)
an end-to-end cybercrime operation dubbed
**Operation Master**
that revolves around compromising enterprise networks, stealing customer and billing databases, offering a subset of the data for sale on underground forums, and repurposing the data for an automated, multi-tenant invoice fraud platform.

|  |
| --- |
|  |
| Operation Master |

Between April and mid-September 2026, the adversary, who goes by the online alias "masterblack" on cybercrime forums, has been observed orchestrating multiple attack campaigns -

* Mass Scanning for Palo Alto Networks PAN OS GlobalProtect gateways and exploiting
  [CVE-2026-0257](https://thehackernews.com/2026/05/pan-os-globalprotect-authentication.html)
  .
* Probing SonicWall SMA VPN, Fortinet, Keycloak, Microsoft Exchange, and Next.js-on-IIS endpoints.
* Collecting public developer documentation and software packages, including Brazilian banking API specs, an energy sector OpenAPI schema, a 3CX web client bundle, and account-creation packages, as part of API Reconnaissance efforts.
* Carrying out automated SQL injection campaigns targeting Brazilian SaaS, CRM, support, education, and financial web applications to steal sensitive data
* Probing ASP.NET applications via \_\_VIEWSTATE SQL injection to target 21 financial organizations.
* Exploiting
  [CVE-2022-28368](https://www.optiv.com/insights/discover/blog/exploiting-rce-vulnerability-dompdf)
  , a remote code execution vulnerability impacting Dompdf.
* Targeting enterprise Microsoft 365 tenants using
  [device-code phishing](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html)
  and password spraying attacks.
* Exploiting
  [CVE-2023-7028](https://thehackernews.com/2024/05/cisa-warns-of-active-exploitation-of.html)
  , an account takeover vulnerability in GitLab, to target an energy company's GitLab instances.
* Brute-forcing WordPress login pages associated with Japanese enterprises by using a dictionary comprising four usernames and 66 passwords.
* Deploying tools like GodPotato, Kerberoast, AS-REProast, Evil-WinRM, and exploits like
  [CVE-2021-4034](https://thehackernews.com/2022/06/cisa-warns-of-active-exploitation-of.html)
  (aka PwnKit),
  [CVE-2024-1086](https://thehackernews.com/2024/05/cisa-alerts-federal-agencies-to-patch.html)
  , and
  [CVE-2020-1938](https://thehackernews.com/2020/02/ghostcat-new-high-risk-vulnerability.html)
  (aka Ghostcat) for privilege escalation, followed by lateral movement to adjacent systems.
* Using DNS tunneling, rclone, and SFTP to exfiltrate data from compromised systems.
* Installing
  [AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
  for command-and-control (C2).

The threat actor has also run an invoice-fraud engine generating over 2.4 million email, SMS, and WhatsApp messages and 622,666 personalized invoice links targeting Brazilian consumers and corporations before going offline in mid-September. The end goal of the campaign is to trick recipients into making Pix payments.

Out of these, the platform has recorded 169,906 target interactions, potentially leading to R$38.9 million worth of fraudulent invoices. In all, the click-tracked short links held a cumulative invoice value of R$150.4 million.

"Operating across multiple countries, the threat actor compromised critical network infrastructure, including VPN gateways via a GlobalProtect authentication bypass (CVE-2026-0257), while concurrently executing advanced web application exploits, deploying the AdaptixC2 framework, and leveraging an AI-assisted development workflow," SOCRadar said.

"Operation Master highlights a dangerous convergence in the modern threat landscape: perimeter exploits long associated with cyber espionage and ransomware are now being systematically industrialized to fuel automated, localized financial fraud ecosystems."

Like in the case of CyberXero, masterblack is also believed to have heavily leaned on AI agents powered by Claude to develop the intrusion code and exfiltration scripts, while the operator focused on designing the fraud panel code and custom AdaptixC2 extenders.

"Recovered refusal transcripts show the operator repeatedly framing offensive development requests as authorized bug bounty or penetration testing activity while requesting functionality consistent with activity observed elsewhere in the operation," SOCRadar said.