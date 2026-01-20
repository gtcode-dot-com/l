---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-20T20:15:13.126123+00:00'
exported_at: '2026-01-20T20:15:15.284127+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html
structured_data:
  about: []
  author: ''
  description: North Korean hackers abuse Visual Studio Code task files in fake job
    projects to deploy backdoors, spyware, and crypto miners on developer systems.
  headline: North Korea-Linked Hackers Target Developers via Malicious VS Code Projects
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: North Korea-Linked Hackers Target Developers via Malicious VS Code Projects
updated_at: '2026-01-20T20:15:13.126123+00:00'
url_hash: 51331f1ca4b2fdbff5e58ef0485a7334081f6e55
---

The North Korean threat actors associated with the long-running
**[Contagious Interview](https://thehackernews.com/2025/11/north-korean-hackers-deploy-197-npm.html)**
campaign have been observed using malicious Microsoft Visual Studio Code (VS Code) projects as lures to deliver a backdoor on compromised endpoints.

The latest finding demonstrates continued evolution of the new tactic that was first discovered in December 2025, Jamf Threat Labs said.

"This activity involved the deployment of a backdoor implant that provides remote code execution capabilities on the victim system," security researcher Thijs Xhaflaire
[said](https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code/)
in a report shared with The Hacker News.

First
[disclosed](https://thehackernews.com/2025/12/north-korea-linked-actors-exploit.html)
by OpenSourceMalware last month, the attack essentially involves instructing prospective targets to clone a repository on GitHub, GitLab, or Bitbucket, and launch the project in VS Code as part of a supposed job assessment.

The end goal of these efforts is to abuse
[VS Code task configuration files](https://code.visualstudio.com/docs/debugtest/tasks)
to execute malicious payloads staged on Vercel domains, depending on the operating system on the infected host. The task is configured such that it runs every time that file or any other file in the project folder is opened in VS Code by setting the "runOn: folderOpen" option. This ultimately leads to the deployment of BeaverTail and InvisibleFerret.

Subsequent iterations of the campaign have been
[found](https://opensourcemalware.com/blog/contagious-interview-malicious-dictionary)
to conceal sophisticated multi-stage droppers in task configuration files by disguising the malware as harmless spell-check dictionaries as a fallback mechanism in the event the task is unable to retrieve the payload from the Vercel domain.

Like before, the obfuscated JavaScript embedded with these files is executed as soon as the victim opens the project in the integrated development environment (IDE). It establishes communication with a remote server ("ip-regions-check.vercel[.]app") and executes any JavaScript code received from it. The final stage delivered as part of the attack is another heavily obfuscated JavaScript.

Jamf said it discovered yet another change in this campaign, with the threat actors using a previously undocumented infection method to deliver a backdoor that offers remote code execution capabilities on the compromised host. The starting point of the attack chain is no different in that it's activated when the victim clones and opens a malicious Git repository using VS Code.

"When the project is opened, Visual Studio Code prompts the user to trust the repository author," Xhaflaire explained. "If that trust is granted, the application automatically processes the repository's tasks.json configuration file, which can result in embedded arbitrary commands being executed on the system."

"On macOS systems, this results in the execution of a background shell command that uses nohup bash -c in combination with curl -s to retrieve a JavaScript payload remotely and pipe it directly into the Node.js runtime. This allows execution to continue independently if the Visual Studio Code process is terminated, while suppressing all command output."

The JavaScript payload, hosted on Vercel, contains the main backdoor logic to establish a persistent execution loop that harvests basic host information and communicates with a remote server to facilitate remote code execution, system fingerprinting, and continuous communication.

In one case, the Apple device management firm said it observed more JavaScript instructions being executed roughly eight minutes after the initial infection. The newly downloaded JavaScript is designed to beacon to the server every five seconds, run additional JavaScript, and erase traces of its activity upon receiving a signal from the operator. It's suspected that the script may have been generated using an artificial intelligence (AI) tool owing to the presence of inline comments and phrasing in the source code.

Threat actors with ties to the Democratic People's Republic of Korea (DPRK) are known to specifically go after software engineers, particular those working in cryptocurrency, blockchain, and fintech sectors, as they often tend to have privileged access to financial assets, digital wallets, and technical infrastructure.

Compromising their accounts and systems could allow the attackers unauthorized access to source code, intellectual property, internal systems, and siphon digital assets. These consistent changes to their tactics are seen as an effort to achieve more success in their cyber espionage and financial goals to support the heavily-sanctioned regime.

The development comes as Red Asgard
[detailed](https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure)
its investigation into a malicious repository that has been found to use a VS Code task configuration to fetch obfuscated JavaScript designed to drop a full-featured backdoor named
[Tsunami](https://thehackernews.com/2025/11/north-korean-hackers-turn-json-services.html)
(aka TsunamiKit) along with an XMRig cryptocurrency miner.

Another analysis from Security Alliance last week has also
[laid out](https://radar.securityalliance.org/vs-code-tasks-abuse-by-contagious-interview-dprk/)
the campaign's abuse of VS Code tasks in an attack where an unspecified victim was approached on LinkedIn, with the threat actors claiming to be the chief technology officer of a project called Meta2140 and sharing a Notion[.]so link contains a technical assessment and a URL to a Bitbucket repository hosting the malicious code.

Interestingly, the attack chain is engineered to fallback to two other methods: installing a
[malicious npm dependency](https://thehackernews.com/2025/11/north-korean-hackers-deploy-197-npm.html)
named "
[grayavatar](https://www.npmjs.com/package/grayavatar?activeTab=versions)
" or running JavaScript code that's responsible for retrieving a sophisticated Node.js controller, which, in turn, runs five distinct modules to log keystrokes, take screenshots, scans the system's home directory for sensitive files,
[substitute wallet addresses](https://thehackernews.com/2025/03/new-massjacker-malware-targets-piracy.html)
copied to the clipboard, credentials from web browsers, and establish a persistent connection to a remote server.

The malware then proceeds to set up a parallel Python environment using a stager script that enables data collection, cryptocurrency mining using XMRig, keylogging, and the deployment of AnyDesk for remote access. It's worth noting that the Node.js and Python layers are referred to as BeaverTail and InvisibleFerret, respectively.

These findings indicate that the state-sponsored actors are experimenting with multiple delivery methods in tandem to increase the likelihood of success of their attacks.

"This activity highlights the continued evolution of DPRK-linked threat actors, who consistently adapt their tooling and delivery mechanisms to integrate with legitimate developer workflows," Jamf said. "The abuse of Visual Studio Code task configuration files and Node.js execution demonstrates how these techniques continue to evolve alongside commonly used development tools."