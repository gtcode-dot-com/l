---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T22:13:50.562517+00:00'
exported_at: '2026-05-14T22:13:53.276499+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html
structured_data:
  about: []
  author: ''
  description: Three node-ipc versions contain stealer/backdoor code, exposing developer
    and cloud secrets to exfiltration.
  headline: Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets
updated_at: '2026-05-14T22:13:50.562517+00:00'
url_hash: fc0b2667dc50b932a58a0ce91e5b5628f133f30d
---

Cybersecurity researchers are sounding the alarm about what has been described as "malicious activity" in newly published versions of node-ipc.

According to
[Socket](https://socket.dev/blog/node-ipc-package-compromised)
and
[StepSecurity](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)
, three different versions of the npm package have been
[confirmed](https://socket.dev/supply-chain-attacks/node-ipc)
as malicious -

* node-ipc@9.1.6
* node-ipc@9.2.3
* node-ipc@12.0.1

"Early analysis indicates that node-ipc@9.1.6, node-ipc@9.2.3, and node-ipc@12.0.1 contain obfuscated stealer/backdoor behavior," Socket said.

"The malware appears to fingerprint the host environment, enumerate and read local files, compress and chunk collected data, wrap the payload in a cryptographic envelope, and attempt exfiltration through a network endpoint selected via DNS/address logic."

StepSecurity said the heavily obfuscated payload is triggered when the package is required at runtime, and attempts to exfiltrate a broad set of developer and cloud secrets to an external command-and-control (C2) server.

This includes 90 categories of credentials, including Amazon Web Services, Google Cloud, Microsoft Azure, SSH keys, Kubernetes tokens, GitHub CLI configs, Claude AI and Kiro IDE settings, Terraform state, database passwords, shell history, and more. The harvested data is then compressed into a GZIP archive and transmitted to the "sh.azurestaticprovider[.]net" domain.

The three versions were published by an account named "atiertant," which has no connection to the package's original author, "riaevangelist." Although "atiertant" appears in the maintainer list, the account has no prior publish history in connection with the node-ipc package. The previous update to the package was in August 2024.

The fact that the dormant, high-download package was compromised after a 21-month gap indicates that either the "atiertant" credentials were newly compromised, or the account was specifically added as a maintainer to publish the malicious versions.

What's notable about the activity is that it does not rely on any npm lifecycle hooks such as preinstall, install, or postinstall scripts, instead appending the malicious payload as an Immediately Invoked Function Expression (
[IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
) to the end of "node-ipc.cjs." This, in turn, causes the malware to fire unconditionally on every require('node-ipc').

The oddity doesn't end there, for the payload performs a SHA-256 fingerprint check and compares it against a hard-coded hash assembled from eight obfuscated table fragments embedded in the code, before proceeding with system enumeration and comprehensive credential harvesting.

"This means 12.0.1 is entirely inert on any machine whose primary module path does not hash to the target value," StepSecurity researcher Sai Likhith said. "The attacker knows exactly which project or developer is being targeted and pre-computed the hash of their entry point before publishing. The 9.x versions do not have this gate and will execute the full payload on any system that loads them."

The malware also incorporates a second exfiltration channel besides issuing an HTTPS POST to the fake Azure domain containing the compressed stolen data. This involves encoding chunks of the archive as a DNS TXT record after overriding the system's DNS resolver with Google Public DNS to sidestep local DNS-based security controls.

"It first resolves sh.azurestaticprovider.net using 1.1.1.1 (primary) or 8.8.8.8 (fallback) to obtain the C2 IP," StepSecurity said. "Then it re-targets the resolver directly at the C2 IP for all exfiltration queries."

"The direct-to-C2 DNS sink is a notable anti-detection technique. Because the exfiltration queries never touch public DNS resolvers, there is no observable bt.node.js activity in public DNS logs. Organizations relying solely on DNS logging through corporate resolvers would not see this traffic."

This is not the first time the npm package has incorporated malicious functionality. In March 2022, the maintainer of the package
[deliberately introduced](https://thehackernews.com/2022/03/popular-npm-package-updated-to-wipe.html)
destructive capability to versions 10.1.1 and 10.1.2 by overwriting files on systems located in Russia or Belarus as a form of protest following Russia's military invasion of Ukraine.

Two subsequent versions – 11.0.0 and 11.1.0 – included the "peacenotwar" dependency, which was also published by the same maintainer as a "non-violent protest against Russia's aggression."

"The latest incident appears to involve a suspicious republishing or reintroduction of malicious code into versions of a known package, rather than a typosquatting attempt," Socket said.

Users are advised to remove the compromised node-ipc versions and re-install a known clean version (9.2.1 and 12.0.0), assume compromise and rotate credentials and secrets, audit npm publish activity for any packages accessible with the rotated tokens, and review workflow run logs for suspicious activity, audit cloud logs to check if any unauthorized actions were performed by IAM identities whose credentials were available during the compromised window, and block egress traffic to the C2 domain.