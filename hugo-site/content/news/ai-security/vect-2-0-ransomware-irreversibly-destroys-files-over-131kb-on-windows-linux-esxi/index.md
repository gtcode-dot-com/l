---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-28T16:15:13.732947+00:00'
exported_at: '2026-04-28T16:15:15.910568+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html
structured_data:
  about: []
  author: ''
  description: VECT 2.0 destroys files over 131KB due to nonce flaw, launched December
    2025, making ransom payments useless.
  headline: VECT 2.0 Ransomware Irreversibly Destroys Files Over 131KB on Windows,
    Linux, ESXi
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: VECT 2.0 Ransomware Irreversibly Destroys Files Over 131KB on Windows, Linux,
  ESXi
updated_at: '2026-04-28T16:15:13.732947+00:00'
url_hash: 536360ab9ac93b1817a274626fa164b8590563a5
---

Threat hunters are warning that the cybercriminal operation known as
**VECT 2.0**
acts more like a wiper than a ransomware due to a critical flaw in its encryption implementation across Windows, Linux, and ESXi variants that renders recovery impossible even for the threat actors.

The fact that VECT's locker
[permanently destroys large files](https://research.checkpoint.com/2026/vect-ransomware-by-design-wiper-by-accident/)
rather than encrypting them means even victims who opt to pay the ransom cannot get their data back, as the decryption keys are discarded by the malware during the time encryption occurs.

"VECT is being marketed as ransomware, but for any file over 131KB – which is most of what enterprises actually care about – it functions as a data destruction tool," Eli Smadja, group manager at Check Point Research, said in a statement shared with The Hacker News.

"CISOs need to understand that in a VECT incident, paying is not a recovery strategy. There is no decrypter that can be handed over, not because the attackers are unwilling, but because the information required to build one was destroyed the moment their software ran. The focus has to be on resilience: offline backups, tested recovery procedures, and rapid containment – not negotiation."

[VECT](https://www.halcyon.ai/ransomware-alerts/emerging-ransomware-group-vect)
(now rebranded as VECT 2.0) is a ransomware-as-a-service (RaaS) scheme that first
[launched](https://www.cyfirma.com/news/weekly-intelligence-report-03-april-2026/)
its affiliate program in December 2025. On its dark website, the group displays the message "Exfiltration / Encryption / Extortion," highlighting its triple-threat business model.

According to an analysis
[published](https://www.dsci.in/files/content/advisory/2026/threat-report-feb-2026.pdf)
by the Data Security Council of India (DSCI) last month, a $250 entry fee, payable in Monero (XMR), is required for new affiliates. The fee is waived for applicants from the Commonwealth of Independent States (CIS) countries, indicating an attempt to recruit individuals from the region.

In recent weeks, the group has established a formal partnership with the BreachForums cybercrime marketplace and the
[TeamPCP](https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html)
hacking group, in a move aimed at further lowering the barrier to entry for ransomware operators and incentivizing affiliates to launch attacks by weaponizing previously stolen data.

"The convergence of large-scale supply chain credential theft, a maturing RaaS operation, and mass dark web forum mobilization represents an unprecedented model of industrialized ransomware deployment," Dataminr
[noted](https://thehackernews.com/2026/04/weekly-recap-vercel-hack-push-fraud.html#:~:text=Vect%20Partners%20with%20BreachForums%20and%20TeamPCP)
earlier this month.

While the collaboration may be a sign of what's to come, its data leak site currently lists only two victims, both of which are said to have been compromised via the TeamPCP supply chain attacks. What's more, contrary to the group's initial claims of using ChaCha20-Poly1305
[AEAD](https://developers.google.com/tink/aead)
for encryption, Check Point's analysis has found that it uses a weaker, unauthenticated cipher with no integrity protection.

But it doesn't end there, for the C++-based lockers for all three platforms suffer from a fundamental design flaw that causes any file larger than 131,072 bytes to be permanently and irrecoverably destroyed, as opposed to being encrypted.

"The malware encrypts four independent chunks of each 'large file' using four freshly generated random 12-byte nonces, but appends only the final nonce to the specific encrypted file on disk," Check Point explained. "The first three nonces, each required to decrypt its respective chunk, are generated, used, and silently discarded. They are never stored on disk, in the registry, or transmitted to the operator."

"Because ChaCha20-IETF requires both the 32-byte key and the exact matching 12-byte nonce to reverse each chunk, the first three quarters of every large file are unrecoverable by anyone, including the ransomware operator, who cannot provide a working decryption tool even after ransom payment. Since the vast majority of operationally critical files exceed this 'large-size' threshold, VECT 2.0 functions in practice as a data wiper with a ransomware facade."

The Windows version of the ransomware, besides encrypting files across local, removable, and network-accessible storage, features a comprehensive anti-analysis suite targeting 44 specific security and debugging tools, alongside a safe-mode persistence mechanism and multiple remote-execution script templates for lateral spread.

When "--force-safemode" is active, the locker configures the next boot into Windows Safe Mode and writes its own executable path into the Windows Registry so that it's automatically run on the subsequent Safe Mode boot, where the operating system is launched in a basic state using a limited set of files and drivers.

On top of that, although the Windows variant implements environment detection mechanisms to fly under the radar, they are never invoked, allowing security teams running the artifacts to avoid triggering any evasive response. The ESXi variant, on the other hand, enforces geofencing and anti-debugging checks prior to commencing the encryption step. It also attempts to move laterally using SSH. The Linux version uses the same codebase as the ESXi flavor and implements a subset of its functionality.

The geofencing step verifies if it's running in a CIS country, and if so, exits without encrypting the files. This behavior, per Check Point, is rather unusual as most RaaS programs removed Ukraine from the CIS countries list following Russia's military invasion of the country in early 2022.

"During recent years these checks have been largely removed from ransomware," it added. "VECT including such checks and even adding Ukraine to the list of exclusions is rather uncommon. Check Point Research has two theories regarding this observation: either this code was AI generated, where LLMs were trained with Ukraine being part of CIS or VECT used an old code base for their ransomware."

It's assessed that the operators of VECT are novice actors rather than experienced threat actors, not to mention the possibility that some chunks of code could have been generated with help from an artificial intelligence (AI) tool.

"VECT 2.0 presents an ambitious threat profile with multi-platform coverage, an active affiliate program, supply-chain distribution via the TeamPCP partnership, and a polished operator panel," Check Point concluded. "In practice, the technical implementation falls significantly short of its presentation."