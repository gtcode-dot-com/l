---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T01:36:02.392477+00:00'
exported_at: '2026-06-11T01:36:03.769011+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/new-frost-attack-lets-websites-track.html
structured_data:
  about: []
  author: ''
  description: FROST uses JavaScript and OPFS SSD timing to identify websites at 88.95%
    F1, exposing cross-browser privacy leaks.
  headline: New FROST Attack Lets Websites Track What Sites and Apps You Open via
    SSD Timing
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/new-frost-attack-lets-websites-track.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New FROST Attack Lets Websites Track What Sites and Apps You Open via SSD Timing
updated_at: '2026-06-11T01:36:02.392477+00:00'
url_hash: c3f13d24a06d0e7145c81d8eafac2fb4a1e8aae0
---

A malicious website can work out which sites you visit and which apps you open, using nothing but JavaScript and the timing of your SSD. The attack, called
**FROST**
, needs no native code, no extension, and no permission prompt.

You open the page, leave the tab sitting there, and it watches the drive for contention in the background.

Researchers at Graz University of Technology built it and described it in
[a new paper](https://hannesweissteiner.com/pdfs/frost.pdf)
set to appear at DIMVA 2026. It abuses a storage feature present in every major desktop browser, and the underlying timing channel works on both macOS and Linux.

SSD timing attacks are not new. Last year the same group published
[Secret Spilling Drive](https://www.ndss-symposium.org/ndss-paper/secret-spilling-drive-leaking-user-behavior-through-ssd-contention/)
, which read user behavior off a drive by watching how reads slow down when something else is using it. The catch was that it needed native code on the machine, through a low-level interface like Linux's io\_uring. FROST drops that requirement. It runs inside the browser sandbox, which turns a local attack into a remote one.

You no longer have to be on the machine to pull it off.

The same Graz lab has done this before. Its
[SnailLoad attack](https://thehackernews.com/2024/06/new-snailload-attack-exploits-network.html)
inferred the sites and videos a victim loaded from network latency alone, no JavaScript at all.

## How FROST Attack Works

The way in is the
[Origin Private File System](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system)
, or OPFS, a storage feature browsers added in 2023 so web apps like in-browser editors and IDEs can keep files on disk. OPFS gives each origin its own sandboxed slice of the file system, and because that slice is walled off, it skips the permission prompt a page normally needs to reach your files. No dialog, no click. A site can just start writing.

Normally the operating system hides disk timing behind the page cache, serving repeated reads from memory so they never touch the drive.

FROST gets around this by creating a file larger than the machine's RAM. The cache cannot hold all of it, so reads keep landing on the SSD. On Chrome and Safari, OPFS can grow to 60% of disk space, far more than enough; Firefox caps each origin lower, though an attacker can spread the load across multiple origins to get past that.

The attacker's code then reads random 4 kB chunks of that file in a loop, and times each read with performance.now(). Browsers blunt their timers by default to make this kind of measurement harder, but the attacker sharpens the resolution back up by switching on cross-origin isolation, which it can do freely on its own page.

When you open a site or launch an app on the same drive, that activity competes with the attacker's reads, and the timing shifts measurably. A neural network trained on those traces identifies the site or app.

The accuracy is the uncomfortable part. On a Mac, against the top 50 websites, FROST identified the site being visited with an F1 score of 88.95% in a closed-world test, and held at 86.95% in an open-world test that added 300 sites it had never seen. For ten native, pre-installed macOS apps, it reached 95.83%. The team also built a covert channel on the same signal, moving data from a cooperating native app to the malicious page at 661.63 bit/s on Linux and 719.27 bit/s on macOS through OPFS. The native attack was faster at its best, but that is a lot of data for code stuck inside a browser sandbox.

While the timing channel also works on Linux, the team ran the full classifier only on macOS, so those fingerprinting numbers are a macOS result. FROST also only picks up activity on the same disk as its OPFS file.

A single-drive laptop puts everything on that disk; a multi-drive workstation hides whatever runs on a separate drive, though app startups that touch the home directory tend to leak anyway.

## What You Can Do

Not much, for now. Google, Mozilla, and Apple were all told before publication. Google's Chromium team does not treat fingerprinting as a security vulnerability. Apple called it out of scope but left room for a mitigation later. Mozilla acknowledged it and has shipped nothing. There is no CVE, and no public evidence that the technique has been used in the wild.

That leaves the defenses thin. The measurement only runs while the attacker's page is open, so closing the tab ends that run. Watching your browser's storage for an unexplained multi-gigabyte file is another tell, though browsers do not make OPFS usage easy to see.

On Linux, systems running profile-sync-daemon, a utility that keeps the browser profile in RAM, are incidentally protected against the zero-click version, because OPFS writes never reach the SSD. The weaker variant, where a page uses a file-picker dialog to get you to select a large file yourself, still works.

The fixes that would actually close it sit with the browser makers: capping OPFS size so the file fits in memory and generates no contention, throttling high-resolution timers while OPFS is in use, or putting a permission prompt in front of it. Each costs something in speed or usability, which is part of why none of them has happened.

The real disagreement is whether a website quietly learning what you do on your own machine is a bug or a feature working as designed. The researchers' real concern is structural: browsers keep handing web apps near-native access to the hardware, and near-native access brings near-native leakage with it. FROST is one API. The pattern is the thing to watch.