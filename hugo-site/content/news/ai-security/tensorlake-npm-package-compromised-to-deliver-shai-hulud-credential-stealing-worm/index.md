---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T07:01:50.857971+00:00'
exported_at: '2026-10-08T07:01:52.140805+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html
structured_data:
  about: []
  author: ''
  description: Malicious tensorlake npm version 0.5.144 contained a Shai-Hulud worm
    that harvests credentials and can republish compromised packages.
  headline: Tensorlake npm Package Compromised to Deliver Shai-Hulud Credential-Stealing
    Worm
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Tensorlake npm Package Compromised to Deliver Shai-Hulud Credential-Stealing
  Worm
updated_at: '2026-10-08T07:01:50.857971+00:00'
url_hash: 6877a62a0bf960dd7cbbabaea903c2f944188e40
---

**

Ravie Lakshmanan
**

Oct 08, 2026

Artificial Intelligence / Cloud Security

The npm package known as "
[tensorlake](https://www.npmjs.com/package/tensorlake?activeTab=versions)
," a TypeScript software development kit (SDK) for
[Tensorlake](https://www.tensorlake.ai)
applications, sandboxes, and cloud services, was
[compromised](https://github.com/tensorlakeai/tensorlake/issues/1014)
as part of a
[ChainDrop / Shai-Hulud](https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html)
supply chain attack.

The malicious version 0.5.144 "contains obfuscated malware that harvests credentials, exfiltrates secrets, establishes persistence, and executes remotely supplied code," Socket
[said](https://socket.dev/blog/tensorlake-compromise)
. Version 0.5.144 is no longer available for download from the npm package registry.

An analysis of the compromised release shows that it contains a preinstall hook designed to launch a JavaScript file ("package/lib/setup.mjs"), an obfuscated loader that launches the main credential-stealing and self-propagating worm ("package/lib/Math\_Symbol.js") using the Bun runtime.

The stealer malware is designed to harvest credentials across local files, CI environments, Kubernetes, and Vault sources. It also
[drops](https://x.com/OliverAikido/status/2108012888304853260)
the
[HackBrowserData](https://thehackernews.com/2024/12/new-glutton-malware-exploits-popular.html)
binary, exfiltrates the collected data, establishes persistence on the host, and facilitates the execution of remotely-supplied code.

"That combination extends the risk beyond a single stolen API key," Socket said. "Any secrets accessible to the executing process may be exposed, and persistence can retain attacker access after the affected dependency is removed."

The types of data stolen by the malware are below -

* npm tokens
* GitHub tokens
* Amazon Web Services (AWS) credentials and secrets
* HashiCorp Vault
* Kubernetes credentials
* SSH keys
* .env files
* Cryptocurrency wallets
* Messaging app data
* Configuration and MCP files associated with Anthropic Claude, Cursor, Kiro, Windsurf, and Zed

"To propagate, the worm enumerates packages associated with the victim's publishing identity, builds Sigstore provenance, and republishes compromised versions," Socket explained. "Strings referencing a fake Copilot/Dependabot workflow suggest it also plants GitHub Actions workflows."

The malware also makes use of an Ethereum contract to resolve its command-and-control (C2) endpoint ("iseekaigogo[.]com"), with GitHub acting as a fallback mechanism to stage the encrypted stolen data in a public repository with the description "Shai-Hulud: Here We Go Again."

In addition, there exists a "hostage token" component that uses a PowerShell monitor to repeatedly poll "api.github.com/user" using the stolen GitHub token to check if the token is valid. Should the victim take steps to revoke the token, the monitor proceeds to execute an attacker-supplied handler through the "Invoke-Expression" cmdlet to execute PowerShell code designed to likely trigger a destructive routine – a tactic observed in
[earlier Shai-Hulud waves](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
.

According to StepSecurity, the malicious files were pushed to the main branch of tensorlakeai/tensorlake under a maintainer's name, after which the package was released from that same repository. The
[first rogue commit](https://github.com/tensorlakeai/tensorlake/commit/e90c47bbb208e99cac8aa678405b2133f6cb3f52)
took place on October 7, 2026, at 01:20 a.m. UTC. A day later, the repository's release workflow
[published](https://github.com/tensorlakeai/tensorlake/tree/6386121c561e74fec143a138d5cc3d3bbabdfe8c/typescript/lib)
0.5.144 to npm

"The malware also writes .claude/settings.json and .vscode/tasks.json files into repos it can reach, so it runs again when someone opens the project in Claude Code or VS Code," StepSecurity's Ashish Kurmi
[said](https://www.stepsecurity.io/blog/tensorlake-npm-compromised-hostage-token-worm)
.

[ChainDrop](https://thehackernews.com/2026/08/open-vsx-removes-77-malicious-evil-twin.html)
was first documented in early August 2026 in connection with the compromise of hundreds of npm packages, including
[Keyv and Cacheable](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html)
, that were found to contain a Mini Shai-Hulud variant with a self-propagating credential-stealing worm delivered through an obfuscated Bun-based JavaScript payload.

The development extends the supply chain attack to artificial intelligence (AI) agent infrastructure, once again highlighting how threat actors are increasingly
[targeting AI tools and services](https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html)
to extract valuable data from enterprises. Users who have installed the malicious version are advised to remove it immediately and rotate their credentials.