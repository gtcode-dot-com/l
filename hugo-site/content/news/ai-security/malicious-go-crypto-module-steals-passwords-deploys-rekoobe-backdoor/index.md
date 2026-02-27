---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-27T18:15:14.430245+00:00'
exported_at: '2026-02-27T18:15:16.655036+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/malicious-go-crypto-module-steals.html
structured_data:
  about: []
  author: ''
  description: A fake Go module posing as golang.org/x/crypto captures terminal passwords,
    installs SSH persistence, and delivers the Rekoobe Linux backdoor.
  headline: Malicious Go Crypto Module Steals Passwords, Deploys Rekoobe Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/malicious-go-crypto-module-steals.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious Go Crypto Module Steals Passwords, Deploys Rekoobe Backdoor
updated_at: '2026-02-27T18:15:14.430245+00:00'
url_hash: 0b72b85096ba5bac2c35c6468c50d8e07aba0b5b
---

**

Ravie Lakshmanan
**

Feb 27, 2026

Malware / Linux Security

Cybersecurity researchers have disclosed details of a malicious Go module that's designed to harvest passwords, create persistent access via SSH, and deliver a Linux backdoor named Rekoobe.

The Go module, github[.]com/xinfeisoft/crypto, impersonates the legitimate "golang.org/x/crypto" codebase, but injects malicious code that's responsible for exfiltrating secrets entered via terminal password prompts to a remote endpoint, fetches a shell script in response, and executes it.

"This activity fits namespace confusion and impersonation of the legitimate golang.org/x/crypto subrepository (and its GitHub mirror github.com/golang/crypto)," Socket security researcher Kirill Boychenko
[said](https://socket.dev/blog/malicious-go-crypto-module-steals-passwords-and-deploys-rekoobe-backdoor)
. "The legitimate project identifies go.googlesource.com/crypto as canonical and treats GitHub as a mirror, a distinction the threat actor abuses to make github.com/xinfeisoft/crypto look routine in dependency graphs."

Specifically, the backdoor has been placed within the "ssh/terminal/terminal.go" file, so that every time a victim application invokes ReadPassword() – a function supposedly meant to read input like passwords from a terminal – it causes that information to capture interactive secrets.

The main responsibility of the downloaded script is to function as a Linux stager, appending a threat actor's SSH key to the "/home/ubuntu/.ssh/authorized\_keys" file, set iptables default policies to ACCEPT in an attempt to loosen firewall restrictions, and retrieve additional payloads from an external server while disguising them with the .mp5 extension.

Of the two payloads, one is a helper that tests internet connectivity and attempts to communicate with an IP address ("154.84.63[.]184") over TCP port 443. The program likely functions as a recon or loader, Socket noted.

The second downloaded payload has been assessed to be Rekoobe, a
[known](https://thehackernews.com/2022/06/new-syslogk-linux-rootkit-lets.html)
[Linux trojan](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html)
that has been detected in the wild
[since at least 2015](https://vms.drweb.com/virus/?i=7754026&lng=en)
. The
[backdoor](https://intezer.com/blog/linux-rekoobe-operating-with-new-undetected-malware-samples/)
is
[capable](https://blog.techevo.uk/analysis/linux/2024/11/30/rekoobe-apt31-linux-backdoor.html)
of receiving commands from an attacker-controlled server to download more payloads, steal files, and execute a reverse shell. As recently as August 2023, Rekoobe has been put to use by Chinese nation-state groups like
[APT31](https://thehackernews.com/2023/08/chinas-apt31-suspected-in-attacks-on.html)
.

While the package
[still remains listed](https://pkg.go.dev/github.com/xinfeisoft/crypto)
on pkg.go.dev, the Go security team has taken steps to block the package as malicious.

"This campaign will likely repeat because the pattern is low-effort and high-impact: a lookalike module that hooks a high-value boundary (ReadPassword), uses GitHub Raw as a rotating pointer, then pivots into curl | sh staging and Linux payload delivery," Boychenko said.

"Defenders should anticipate similar supply chain attacks targeting other 'credential edge' libraries (SSH helpers, CLI auth prompts, database connectors) and more indirection through hosting surfaces to rotate infrastructure without republishing code."