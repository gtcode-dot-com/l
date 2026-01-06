---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-09T12:03:07.752792+00:00'
exported_at: '2025-12-09T12:03:10.144186+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/stac6565-targets-canada-in-80-of.html
structured_data:
  about: []
  author: ''
  description: Sophos reports STAC6565 targeting nearly 40 victims, with 80% of attacks
    hitting Canadian firms and involving QWCrypt ransomware.
  headline: STAC6565 Targets Canada in 80% of Attacks as Gold Blade Deploys QWCrypt
    Ransomware
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/stac6565-targets-canada-in-80-of.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: STAC6565 Targets Canada in 80% of Attacks as Gold Blade Deploys QWCrypt Ransomware
updated_at: '2025-12-09T12:03:07.752792+00:00'
url_hash: cc7b08f15947033c33eb776c84c30733cec98787
---

Canadian organizations have emerged as the focus of a targeted cyber campaign orchestrated by a threat activity cluster known as
**STAC6565**
.

Cybersecurity company Sophos
[said](https://news.sophos.com/en-us/2025/12/05/sharpening-the-knife-gold-blades-strategic-evolution/)
it investigated almost 40 intrusions linked to the threat actor between February 2024 and August 2025. The campaign is assessed with high confidence to share overlaps with a hacking group known as
[Gold Blade](https://thehackernews.com/2025/03/redcurl-shifts-from-espionage-to.html)
, which is also tracked under the names Earth Kapre, RedCurl, and Red Wolf.

The financially motivated threat actor is believed to be
[active since late 2018](https://thehackernews.com/2021/11/redcurl-corporate-espionage-hackers.html)
, initially targeting entities in Russia, before expanding its focus to entities in Canada, Germany, Norway, Russia, Slovenia, Ukraine, the U.K., and the U.S. The group has a history of using phishing emails to conduct commercial espionage.

However, recent attack waves have found RedCurl to have engaged in ransomware attacks using a bespoke malware strain dubbed
[**QWCrypt**](https://thehackernews.com/2025/03/redcurl-shifts-from-espionage-to.html)
. One of the notable tools in the threat actor's arsenal is RedLoader, which sends information about the infected host to a command-and-control (C2) server and executes PowerShell scripts to collect details related to the compromised Active Directory (AD) environment.

"This campaign reflects an unusually narrow geographic focus for the group, with almost 80% of the attacks targeting Canadian organizations," Sophos researcher Morgan Demboski said. "Once focused primarily on cyber espionage, Gold Blade has evolved its activity into a hybrid operation that blends data theft with selective ransomware deployment via a custom locker named QWCrypt."

Other prominent targets include the U.S., Australia, and the U.K., with services, manufacturing, retail, technology, non-governmental organizations, and transportation sectors hit the hardest during the time period.

The group is said to be operating under a "hack-for-hire" model, carrying out tailored intrusions on behalf of clients, while deploying ransomware on the side to monetize the intrusions. Although a
[2020 report](https://www.group-ib.com/media-center/press-releases/red-curl/)
from Group-IB raised the possibility of it being a Russian-speaking group, there are currently no indications to confirm or deny this assessment.

Describing RedCurl as a "professionalized operation," Sophos said the threat actor stands apart from other cybercriminal groups owing to its ability to refine and evolve its tradecraft, as well as mount discreet extortion attacks. That said, there is no evidence to suggest it's state-sponsored or politically motivated.

The cybersecurity company also pointed out that the operational tempo is marked by periods of no activity, followed by sudden spikes in attacks using improved tactics, indicating that the hacking group could be using the downtime to refresh its toolset.

STAC6565 begins with spear-phishing emails targeting human resources (HR) personnel to trick them into opening malicious documents disguised as resumes or cover letters. Since at least November 2024, the activity has leveraged legitimate job search platforms like Indeed, JazzHR, and ADP WorkforceNow to upload the weaponized resumes as part of a job application process.

"As recruitment platforms enable HR staff to review all incoming resumes, hosting payloads on these platforms and delivering them via disposable email domains not only increases the likelihood that the documents will be opened but also evades detection by email-based protections," Demboski explained.

In one incident, a fake resume uploaded to Indeed has been found to redirect users to a booby-trapped URL that ultimately led to the deployment of QWCrypt ransomware by means of a RedLoader chain. At least three different RedLoader delivery sequences have been observed in September 2024, March/April 2025, and July 2025. Some aspects of the delivery chains were
[previously detailed](https://thehackernews.com/2025/03/redcurl-shifts-from-espionage-to.html)
by Huntress, eSentire, and Bitdefender.

The major change observed in July 2025 concerns the use of a ZIP archive that's dropped by the bogus resume. Present within the archive is a Windows shortcut (LNK) that impersonates a PDF. The LNK file uses "rundll32.exe" to fetch a renamed version of "ADNotificationManager.exe" from a WebDAV server hosted behind a Cloudflare Workers domain.

The attack then launches the legitimate Adobe executable to sideload the RedLoader DLL (named "srvcli.dll" or "netutils.dll") from the same WebDAV path. The DLL proceeds to connect to an external server to download and execute the second-stage payload, a standalone binary that's responsible for connecting to a different server and retrieving the third-stage standalone executable alongside a malicious DAT file and a renamed 7-Zip file.

Both stages rely on Microsoft's Program Compatibility Assistant ("pcalua.exe") for payload execution, an approach seen in previous campaigns as well. The only difference is that the format of the payloads transitioned in April 2025 to EXEs instead of DLLs.

"The payload parses the malicious .dat file and checks internet connectivity. It then connects to another attacker-controlled C2 server to create and run a .bat script that automates system discovery," Sophos said. "The script unpacks Sysinternals AD Explorer and runs commands to gather details such as host information, disks, processes, and installed antivirus (AV) products."

The results of the execution are packaged into an encrypted, password-protected 7-Zip archive and transferred to a WebDAV server controlled by the attacker. RedCurl has also been observed using RPivot, an open-source reverse proxy, and Chisel SOCKS5 for C2 communications.

Another tool used in the attacks is a customized version of the Terminator tool that leverages a signed
[Zemana](https://thehackernews.com/2024/04/akira-ransomware-gang-extorts-42.html)
AntiMalware driver to kill antivirus-related processes via what's called a Bring Your Own Vulnerable Driver (BYOVD) attack. In at least one case in April 2025, the threat actors renamed both the components before distributing them via SMB shares to all servers in the victim environment.

Sophos also noted that a majority of these attacks were detected and mitigated before the installation of QWCrypt. However, three of the attacks – one in April and two in July 2025 – led to a successful deployment.

"In the April incident, the threat actors manually browsed and collected sensitive files, then paused activity for over five days before deploying the locker," it added. "This delay may suggest the attackers turned to ransomware after trying to monetize the data or failing to secure a buyer."

The QWCrypt deployment scripts are tailored to the target environment, often containing a victim-specific ID in the file names. The script, once launched, checks whether the Terminator service is running before taking steps to disable recovery and execute the ransomware on endpoint devices across the network, including the organization's hypervisors.

In the last stage, the script runs a cleanup batch script to delete existing shadow copies and every PowerShell console history file to inhibit forensic recovery.

"Gold Blade's abuse of recruitment platforms, cycles of dormancy and bursts, and continual refinement of delivery methods demonstrate a level of operational maturity not typically associated with financially motivated actors," Sophos said. "The group maintains a comprehensive and well-organized attack toolkit, including modified versions of open-source tooling and custom binaries to facilitate a multi-stage malware delivery chain."

The disclosure comes as Huntress said it has noticed a huge spike in ransomware attacks on hypervisors, jumping from 3% in the first half of the year to 25% so far in the second half, primarily driven by the Akira group.

"Ransomware operators deploy ransomware payloads directly through hypervisors, bypassing traditional endpoint protections entirely. In some instances, attackers leverage built-in tools such as OpenSSL to perform encryption of the virtual machine volumes, avoiding the need to upload custom ransomware binaries,"
[wrote](https://www.huntress.com/blog/hypervisor-defenses-against-ransomware-targeting-esxi)
researchers Anna Pham, Ben Bernstein, and Dray Agha.

"This shift underscores a growing and uncomfortable trend: attackers are targeting the infrastructure that controls all hosts, and with access to the hypervisor, adversaries dramatically amplify the impact of their intrusion."

Given the heightened focus of threat actors on hypervisors, it's advised to use local ESXi accounts, enforce multi-factor authentication (MFA), implement a strong password policy, segregate the hypervisor's management network from production and general user networks, deploy a jump box to audit admin access, limit access to the control plane, and restrict ESXi management interface access to specific administrative devices.