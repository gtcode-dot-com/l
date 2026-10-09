---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-04T05:11:45.472422+00:00'
exported_at: '2026-06-04T05:11:49.242589+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33024
structured_data:
  about: []
  author: ''
  description: 'Reconstructing an Akira Ransomware Kill Chain from Perimeter and Endpoint
    Logs, Author: Manuel Humberto Santander Pelaez'
  headline: Reconstructing an Akira Ransomware Kill Chain from Perimeter and Endpoint
    Logs, (Wed, May 27th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33024
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Reconstructing an Akira Ransomware Kill Chain from Perimeter and Endpoint Logs,
  (Wed, May 27th)
updated_at: '2026-06-04T05:11:45.472422+00:00'
url_hash: 37327a943963b959c7d14bd87c0ecf038ef506d1
---

Most Akira write-ups focus on the ransom note or the encryption routine. By the time those show up the interesting forensic work is over. The questions that matter to defenders sit earlier. How did they get in. When did they get domain admin. What did they touch before the binary fired. Those answers live in the days before impact. They sit in two log sources that almost never get joined. The perimeter firewall and the Windows event channel.

This diary walks through a recent Akira-attributed intrusion at a mid-sized organization. The reconstruction used only SSLVPN syslog and Windows EVTX exports. No EDR. No memory captures. Every identifier in the post has been anonymized. The event types and sequencing are preserved exactly as observed.

# **The setup**

The environment was a single-site Active Directory forest behind a perimeter NGFW. SSLVPN gave remote access to a small workforce. We started the engagement with the following sources available:

* Firewall syslog covering roughly seven days before the encryption event. Authentication, IPS and traffic categories were retained.
* EVTX exports from both domain controllers and three member servers. Channels covered were Security, System and Microsoft-Windows-PowerShell/Operational.
* The ransom note text file and a sample of encrypted files. Used only to confirm attribution.

No EDR. No PCAP. No proxy logs. This is a representative starting point for many small and mid-sized organizations. It is also why the joinable signal between the firewall and the Windows event channels matters so much.

# **Stage 1: Initial access**

The first useful signal came from the firewall authentication log. We filtered SSLVPN events for the 72 hours before the encryption event. An unambiguous brute-force pattern jumped out. It targeted a single local SSLVPN account. The customer confirmed later that the account had been disabled in Active Directory. It remained provisioned as a local firewall user.

![](https://isc.sans.edu/diaryimages/images/Imagen%201.png)

Two details from Figure 1 deserve a closer look. The brute force was not distributed. Every failure came from a single source IP in a hosting-provider range. One IPS rule or a geo-block would have stopped it. The successful authentication landed inside the ramp. There was no pause to test the credential. The attacker walked straight in once one matched. That is the behavioral fingerprint of credential stuffing against a known target.

Mapping this to the firewall vendor known SSLVPN credential exposure issue is plausible. It is not strictly provable from the logs we had. What is provable is this. The local account had no MFA. It had been deprovisioned in AD but not in the firewall. Its password survived a six-hour online attack.

# **Stages 2 and 3: Discovery and credential access**

Once on the VPN the attacker had a layer-3 path into the user VLAN. The pivot point to internal evidence was the firewall NAT log. It gave us the post-VPN source IP and the relevant time window. We joined that window against the Windows Security channel. The first internal events of interest were EID 4624 logons from the VPN-assigned IP to a jump host. The customer confirmed the jump host was used by legitimate remote administrators.

What followed was textbook discovery activity. All of it was visible in EID 4688 process creation events.

EID 4688  parent: explorer.exe   child: cmd.exe

EID 4688  parent: cmd.exe        child: nltest.exe   /dclist:

EID 4688  parent: cmd.exe        child: net.exe      group "Domain Admins" /domain

EID 4688  parent: cmd.exe        child: net.exe      group "Enterprise Admins" /domain

EID 4688  parent: cmd.exe        child: whoami.exe   /all

EID 4688  parent: cmd.exe        child: &lt;renamed&gt;.exe  (AdFind.exe behavior)

About 24 hours later a cluster of EID 4769 events appeared against three service accounts. All RC4-encrypted. All from the jump host. All inside a 90-second window. That combination is the signature pattern for Kerberoasting. It is also the cheapest detection any AD-joined organization can deploy.

# **Stage 4: Lateral movement**

Lateral movement spread across two days and used RDP almost exclusively. The relevant pattern is the well-known EID 4624 Logon Type 10 cluster. Successful logons originated from the jump host. Targets included the file server, both domain controllers and the backup server. EID 4672 followed each domain-controller logon. The attacker now held domain-level privilege.

Two artifacts from this phase deserve attention. The attacker created a new account in a non-default OU. They added it to a built-in group using its Well-Known SID rather than the localized group name. That is a small but reliable indicator. The operator was scripting for environment portability and not working interactively in the local language.

Several PowerShell sessions ran with the -EncodedCommand flag. Once decoded the contents showed reconnaissance against backup infrastructure and shadow-copy state. That is pre-staging for the impact stage. Worth alerting on by itself.

# **Stages 5 and 6 defense evation and impact**

The final 12 hours collapsed into a rapid sequence. The Security event log on the jump host was cleared. That is EID 1102. Several endpoint protection services were stopped using sc.exe and net stop. We saw this in System EID 7036. A vssadmin delete shadows /all /quiet ran across every reachable host. Encryption followed within minutes. Figure 2 shows the full sequence.

[![](https://isc.sans.edu/diaryimages/images/fig2(1).png)](https://isc.sans.edu/diaryimages/images/fig2(1).png)

The time distribution in Figure 2 matters more than the sequence. The encryption event is what the customer sees. It represents maybe five percent of the total dwell time. The other 95 percent is where defensive opportunity sits. Almost all of it was visible in logs the customer already had.

# **Why joining the sources matter**

Most defenders treat perimeter logs and endpoint event logs as two separate problems handled by two separate teams. Figure 3 shows what that separation costs. Each stage of this intrusion was visible in only one of the two sources at high confidence.

[![](https://isc.sans.edu/diaryimages/images/fig3(1).png)](https://isc.sans.edu/diaryimages/images/fig3(1).png)

An analyst working only the firewall syslog would have caught the brute force and the successful login. Nothing past that. An analyst working only EVTX would have seen anomalous internal behavior with no anchor for the entry point. The joined view turns two partial accounts into one full kill chain. The pivot field is source IP. The axis is normalized time.

The join itself is trivial. The expensive parts are retention and time synchronization. In this engagement the firewall retained seven days of syslog. The Windows event channels had been left at default sizes. EID 4688 had already rolled off the jump host by the time analysis started. Recovery required reaching back into a single off-host log forwarder.

# **Detection and hunting guidance**

Concrete actions any organization can implement immediately. All of them come straight from the patterns above.

* Local SSLVPN accounts. Inventory them. Enforce MFA. Reconcile against the directory of record. A deprovisioned-in-AD-but-not-in-the-firewall account is the most common initial-access pathway in this class of intrusion.
* Authentication failure thresholds. Alert on more than 50 failed SSLVPN authentications from a single source in any one-hour window. The brute force in Figure 1 would have tripped this in 30 minutes.
* EID 4688 process auditing. Enable it on every Windows host. Set the Security log size to at least 1 GB. Default sizes are why discovery activity disappears before responders arrive.
* EID 4769 anomaly detection. Alert on RC4 tickets requested for multiple SPNs in a short window from a single workstation. Cheapest Kerberoasting detection that exists.
* EID 1102 security log cleared. Any occurrence is incident-grade. Forward this event off-host before anything else.
* vssadmin and wmic shadowcopy command-line auditing. Alert on any execution. Legitimate use is rare. Ransomware use is universal.
* Time synchronization. Every host including the firewall should sync to the same authoritative NTP source. Without aligned timestamps any join of perimeter and endpoint evidence becomes guesswork.

# **ATT&amp;CK Mapping**

The full TTP set observed in this intrusion mapped to the following ATT&amp;CK techniques:

|  |  |  |  |
| --- | --- | --- | --- |
| **Stage** | **MITRE ATT&amp;CK ID** | **Technique** | **Primary Evidence** |
| Initial Access | T1078.001 / T1133 | Valid Accounts: Local / External Remote Services | Firewall syslog (auth events) |
| Discovery | T1087, T1482 | Account / Domain Trust Discovery | EID 4688 (nltest.exe, net.exe) |
| Credential Access | T1558.003 | Kerberoasting | EID 4769 (RC4 anomalies) |
| Lateral Movement | T1021.001 | Remote Services: RDP | EID 4624 (Logon Type 10) |
| Defense Evasion | T1070.001, T1562 | Clear Windows Event Logs / Impair Defenses | EID 1102, 7036 |
| Impact | T1486, T1490 | Data Encrypted / Inhibit System Recovery | EID 4688 (vssadmin), file system telemetry |

# **Closing thoughts**

Akira is not a sophisticated adversary. The kill chain reconstructed here is trivial:

* Brute force a forgotten local VPN account.
* Run nltest and net group.
* Roast a service account.
* RDP around.
* Clear logs.
* Delete shadows.
* Encrypt.

Nothing in that sequence is novel. Nothing in it requires advanced detection.

What it requires is the discipline to retain perimeter and endpoint logs long enough to be joined and the willingness to actually join them when something goes wrong.

Every step of this intrusion was visible in logs the organization already owned. The work of incident response was not finding new signal. It was reading signal that had been sitting there the whole time.

**Manuel Humberto Santander Peláez**

**SANS Internet Storm Center - Handler**

**X:**
[@manuelsantander](https://twitter.com/manuelsantander)

**Mastodon:**
[[email protected]](https://infosec.exchange/@manuelsantander)
**email:**