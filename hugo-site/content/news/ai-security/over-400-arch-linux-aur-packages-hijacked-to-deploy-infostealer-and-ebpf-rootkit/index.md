---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-12T21:33:11.520382+00:00'
exported_at: '2026-06-12T21:33:12.820445+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html
structured_data:
  about: []
  author: ''
  description: Attackers hijacked 400+ Arch Linux AUR packages to run a Rust credential
    stealer, with optional eBPF rootkit support on root systems.
  headline: Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF
    Rootkit
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit
updated_at: '2026-06-12T21:33:11.520382+00:00'
url_hash: 2ce336af4a908f70cabfb1f20963a3174e4e3b55
---

Attackers took over more than 400 packages in the Arch User Repository (AUR) this week and rewrote their build scripts to install a credential stealer on any machine that built them.

The malware is a Rust binary built to harvest developer secrets. When it lands with root, it can also load an eBPF rootkit to hide itself. The AUR is Arch Linux's community package collection, and it is separate from the official Arch repositories, which were not affected.

If you installed or updated an AUR package on or after June 11, check it against the current affected-package lists before trusting the host. The list of names is large, still growing, and not yet complete.

This attack goes after the trust model, not a software flaw. The compromised packages kept their names, their histories, and the trust that came with them. Only the build instructions changed.

The trap sat in the recipe, leaving the package itself looking exactly like the software users meant to install. No exploit, no zero-day, and no sign Arch's own systems were breached.

The attackers adopted abandoned packages, edited the build files, and let users run the payload for them. Sonatype, which named the campaign
[Atomic Arch](https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency)
, found them going after orphaned projects: packages whose maintainers had walked away, leaving them open for anyone to adopt.

They also spoofed git commit metadata so the changes looked like they came from a long-standing maintainer, an account an Arch Linux Trusted User later confirmed was never compromised.

Once a package was adopted, its PKGBUILD or .install script was edited to run npm install atomic-lockfile during the build, pulling the malicious npm package alongside a couple of legitimate ones for cover. That package, atomic-lockfile@1.4.2, carries a preinstall hook that runs a bundled Linux ELF named deps. Build the package, and the binary runs.

Confirmed examples reported to the Arch mailing list include the alvr and premake-git packages.

## What the malware does

Independent researcher Whanos
[reverse-engineered](https://ioctl.fail/preliminary-analysis-of-aur-malware/)
the deps payload and describes a Rust credential stealer aimed at developer workstations and build systems. It collects:

* Cookies, tokens, and local storage from Chromium-based browsers (Chrome, Edge, Brave, and many more)
* Session data from Electron apps, including Slack, Discord, and Microsoft Teams
* GitHub, npm, and HashiCorp Vault tokens, plus OpenAI/ChatGPT bearer material and account metadata
* SSH keys, known\_hosts, and shell histories
* Docker and Podman credentials and VPN profiles

Stolen files go out over HTTP to temp.sh. Command and control runs through a Tor onion service via a local loopback proxy.

For persistence, it installs a systemd service with Restart=always. With root it copies itself under /var/lib/ and writes a unit under /etc/systemd/system/; as a normal user it uses the home directory and a per-user unit under ~/.config/systemd/user/. Either way, it wants to come back.

Early write-ups oversold the eBPF rootkit. It is optional, and it only loads when the binary already has root and the right capability. It is not used to gain privileges. When it does activate, it hides the malware's own processes, process names, and socket inodes from standard tools, using pinned BPF maps named hidden\_pids, hidden\_names, and hidden\_inodes, and it kills attempts to attach a debugger.

That changes the cleanup advice. Removing the AUR package is not enough once the payload has run. A package manager can remove the files it knows about. It cannot prove the machine is clean after a rootkit-capable payload has had a chance to execute.

The binary also stages a second file tied to monero-wallet-gui that the analysis flags as a possible, unanalyzed cryptominer. An eBPF rootkit bolted onto a smash-and-grab stealer is unusual, and it is why this one is worth more than a shrug.

## Scope, and a second wave

Sonatype's first write-up counted more than 20 hijacked packages. Within a day, community trackers and the Arch
[aur-general thread](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/FGXPCB3ZVCJIV7FX323SBAX2JHYB7ZS4/)
had cataloged over 400, with one master list compiled by grepping the AUR git mirror, putting it around 408, and consolidated lists climbing higher.

The atomic-lockfile npm package itself showed only 134 weekly downloads on
[Socket](https://socket.dev/npm/package/atomic-lockfile)
before it was pulled from the registry, so the real exposure is the AUR build path rather than npm installs.

A second wave used bun install js-digest, pushed from a separate set of accounts that community trackers link to the same npm publisher as atomic-lockfile. Its payload is a different binary, a separate ELF by its hash, that the community also flagged as malicious.

How far this wave has spread is still being counted. Early breakdowns listed a few dozen packages, while later grep-based searches of the AUR mirror returned much higher numbers that may include churn as commits are removed. Either way, it is not a footnote to the first wave, so check for both atomic-lockfile and js-digest.

## What to do now

Arch maintainers are resetting the malicious commits, banning the accounts, and asking users to keep reporting suspect packages in the mailing-list thread.

Treat the published affected-package list as incomplete. On your end:

* Check any AUR package installed or updated on or after June 11 against the community package lists and detection scripts, which compare your foreign packages against the known-bad set. Grep recent build history and caches for npm install atomic-lockfile, bun install js-digest, and the payload path src/hooks/deps.
* If a flagged package ran, treat the host as credential-compromised. Rotate everything the stealer touches: browser sessions, SSH keys, GitHub and npm tokens, Slack, Teams and Discord sessions, Vault tokens, Docker and Podman credentials, and any cloud keys.
* Hunt for persistence. Check for unknown systemd services (both system units and ~/.config/systemd/user/) and unexpected files under /var/lib/. Inspect /sys/fs/bpf/ for the maps hidden\_pids, hidden\_names, and hidden\_inodes. Review outbound connections to Tor and to upload services.
* If the package ran as root, assume the rootkit is present and reinstall from trusted media. There is no way to trust the system otherwise.
* Going forward, read the PKGBUILD and any .install hooks before you build, especially for packages recently adopted or suddenly active after long dormancy. If you do not understand the build instructions, do not install the package.

For detection, the main payload's SHA-256 is 6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b; the full indicator set, including the onion C2 host, is in the ioctl.fail analysis.

The same adoption tactic hit an abandoned
[PDF-viewer package back in 2018](https://thehackernews.com/2018/07/arch-linux-aur-malware.html)
; the 2026 version just scaled it up, part of a broader run of supply-chain attacks that hijack orphaned projects to inherit trust rather than typosquatting to trick users. The affected list is still incomplete, and no CVE has been assigned; Sonatype tracks the campaign as Sonatype-2026-003775 (CVSS 8.7).

The attack worked because the AUR still trusts a package's name and history over who is maintaining it now. A recently adopted package, or one that suddenly sprouts new install hooks, now deserves the same suspicion as a package from a stranger.