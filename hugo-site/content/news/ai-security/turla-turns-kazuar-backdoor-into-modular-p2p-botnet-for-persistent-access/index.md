---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-15T17:19:49.104547+00:00'
exported_at: '2026-05-15T17:19:53.943061+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html
structured_data:
  about: []
  author: ''
  description: Turla turns Kazuar into a 3-module P2P botnet, enabling stealthy C2,
    resilient tasking, and persistent access.
  headline: Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access
updated_at: '2026-05-15T17:19:49.104547+00:00'
url_hash: 52d77ff8bfbfefcdfd74e66a1f3c9d93bdb4afc1
---

**

Ravie Lakshmanan
**

May 15, 2026

Botnet / Threat Intelligence

The Russian state-sponsored hacking group known as
**[Turla](https://thehackernews.com/2025/07/secret-blizzard-deploys-malware-in-isp.html)**
has transformed its custom backdoor Kazuar into a modular peer-to-peer (P2P) botnet that's engineered for stealth and persistent access to compromised hosts.

Turla, per the U.S. Cybersecurity and Infrastructure Security Agency (CISA), is assessed to be affiliated with Center 16 of Russia's Federal Security Service (FSB). It overlaps with activity traced by the broader cybersecurity community under the names ATG26, Blue Python, Iron Hunter, Pensive Ursa, Secret Blizzard (formerly Krypton), Snake, SUMMIT, Uroburos, Venomous Bear, Waterbug, and WRAITH.

The hacking group is known for its attacks targeting government, diplomatic, and defense sectors in Europe and Central Asia, as well as
[endpoints previously breached by Aqua Blizzard](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html)
(aka Actinium and Gamaredon) to support the Kremlin's strategic objectives.

"This upgrade aligns with Secret Blizzard's broader objective of gaining long-term access to systems for intelligence collection," the Microsoft Threat Intelligence team
[said](https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/)
in a report published Thursday. "While many threat actors rely on increasing usage of native tools (living-off-the-land binaries (LOLBins)) to avoid detection, Kazuar's progression into a modular bot highlights how Secret Blizzard is engineering resilience and stealth directly into their tooling."

A key tool in Turla's arsenal is
[Kazuar](https://thehackernews.com/2024/12/secret-blizzard-deploys-kazuar-backdoor.html)
, a
[sophisticated .NET backdoor](https://thehackernews.com/2023/11/turla-updates-kazuar-backdoor-with.html)
that has been consistently put to use since 2017. The latest findings from Microsoft charts its evolution from a "monolithic" framework into a modular bot ecosystem featuring three distinct component types, each with its own well-defined roles. These changes enable flexible configuration, reduce observable footprint, and facilitate broad tasking.

|  |
| --- |
|  |
| Overview of Kernel, Bridge, and Worker module interactions |

Attacks distributing the malware have been found to rely on droppers like Pelmeni and ShadowLoader to decrypt and launch the modules. The three module types that form the foundation for Kazuar's architecture are listed below -

* **Kernel**
  , which acts as the central coordinator for the botnet by issuing tasks to Worker modules, manages communication with the Bridge module, maintains logs of actions and collected data, performs anti-analysis and sandbox checks, and sets up the environment by means of a configuration that specifies various parameters related to command-and-control (C2) communication, data exfiltration timing, task management, file scanning and collection, and monitoring.
* **Bridge**
  , which acts as a proxy between the leader Kernel module and the C2 server.
* **Worker**
  , which logs keystrokes, hooks Windows events, tracks tasks, and gathers system information, file listings, and Messaging Application Programming Interface (
  [MAPI](https://learn.microsoft.com/en-us/cpp/mfc/mapi)
  ) details.

The Kernel module type exposes three internal communication mechanisms (via Windows Messaging, Mailslot, and named pipes) and three different methods for contacting attacker-controlled infrastructure (via Exchange Web Services, HTTP, and WebSockets). The component also "elects" a single Kernel leader to communicate with the Bridge module on behalf of the other Kernel modules.

|  |
| --- |
|  |
| How the Kernel leader coordinates Worker tasking and uses the Bridge |

"Elections occur over Mailslot, and the leader is elected based on the amount of work (length of time the Kernel module has been running) divided by interrupts (reboots, logoffs, process terminated)," Microsoft explained. "Once a leader is elected, it announces itself as the leader and tells all other Kernel modules to set SILENT. Only the elected leader is not SILENT, which allows the leader Kernel module to log activity and request tasks through the Bridge module."

Another function of the module is to initiate various threads to set up a named pipe channel between Kernel modules for inter-Kernel communications, specify an external communication method, as well as facilitate Kernel-to-Worker and Kernel-to-Bridge communication over Windows messaging or Mailslot.

The end goal of the Kernel is to poll new tasks from the C2 server, parse incoming messages, assign tasks to the Worker, update configuration, and send the results of the tasks back to the server. Furthermore, the module incorporates a task handler that makes it possible to process commands issued by the Kernel leader.

Data collected by the Worker module is then aggregated, encrypted, and written to the malware's working directory, from where it's exfiltrated to the C2 server.

"Kazuar uses a dedicated working directory as a centralized on-disk staging area to support its internal operations across modules," Microsoft said. "This directory is defined through configuration and is consistently referenced using fully qualified paths to avoid ambiguity across execution contexts."

"Within the working directory, Kazuar organizes data by function, isolating tasking, collection output, logs, and configuration material into distinct locations. This design allows the malware to decouple task execution from data storage and exfiltration, maintain operational state across restarts, and coordinate asynchronous activity between modules while minimizing direct interaction with external infrastructure."