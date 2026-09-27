---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-27T18:35:32.902995+00:00'
exported_at: '2026-09-27T18:35:35.409207+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html
structured_data:
  about: []
  author: ''
  description: Alby warns a critical Hub flaw could let attackers take over internet-exposed
    wallets; versions 1.19.0 and later are not affected.
  headline: Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed
    Bitcoin Wallets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin
  Wallets
updated_at: '2026-09-27T18:35:32.902995+00:00'
url_hash: b4d6dd696d134483f05f45a1755279f9bfd2dc66
---

Bitcoin wallet company Alby has
[warned of a critical flaw](https://x.com/getAlby/status/2097574956049498150)
in Alby Hub that could have let an attacker take over a wallet and send its funds, but only where the owner had made the Hub reachable from the internet.

Alby Hub is a self-hosted Lightning wallet, meaning the owner runs it on their own computer or server, and it holds their bitcoin. The flaw affects versions v1.7.0 through v1.18.5, all released before August 2025, and Alby said one user has been affected so far.

Versions v1.19.0 and later do not have the flaw. The first release with that fix was published on August 29, 2025, so a Hub updated to any release published since then is not affected.

Alby is telling anyone still on an older build to stop outside access to the Hub's management interface first, which is the web page used to control the wallet. The next step is to update to
[v1.24.0](https://github.com/getAlby/hub/releases)
, the current release.

The company has not said what the flaw is. It said it would publish full details later, in line with responsible disclosure practices, and thanked researchers who reported other issues that were fixed in the latest release.

Alby said that, to its knowledge, one user has been affected, and did not say whether that user lost money. It said the user reported the details to the company.

| Version | Status |
| --- | --- |
| `v1.7.0` to `v1.18.5` | Affected, where the Hub was reachable from the internet |
| `v1.19.0` and later | Not affected |
| `v1.24.0` | Current release. Alby recommends it even for people who are not affected |

### What to Do Now

1. Check the version your Hub is running.
2. If it is v1.18.5 or older, stop the Hub being reachable from outside your own network first. In a Docker setup, that means the port is published as 127.0.0.1:8080:8080 and not 8080:8080. On a cloud server, it means the firewall rule for port 8080 allows your own address rather than any address.
3. Update to v1.24.0.
4. If your Hub ran an affected version
   **and**
   was reachable from the internet, change your unlock password after the update and contact security@getalby.com.

Alby has not said whether updating alone ends any access an attacker already had to an exposed Hub. Its advice to change the unlock password applies to exactly that group, and no published source explains what the change is meant to undo.

### How a Hub Ends Up on the Internet

Alby Hub is built to sit on a private network. Its web interface requires a login, and
[the project's own documentation](https://github.com/getalby/hub)
now warns owners not to put it on the public internet because the server listens on every network connection the machine has, rather than only on the machine itself.

That warning is new. It arrived in a documentation
[change merged on September 7](https://github.com/getAlby/hub/pull/2580)
, whose own description says several of the setup guides had described the server as "running on localhost when it actually listens on all network interfaces."

The same change switched the project's Docker file from publishing port 8080 to every address to publishing it only to the machine itself.

Before that, the guide for running Alby Hub on a Linux server said the Hub runs on localhost and recommended a reverse proxy for anyone who wanted to make it public. The README shipped with the oldest and the newest affected release did not carry that warning, and neither does the one in the current release.

As of September 9, the day of the warning, Alby's own guides for running a Hub on a cloud server still described a setup open to the internet.

Its
[DigitalOcean guide](https://getalby.com/alby-hub/cloud/digitalocean)
tells the reader to keep the server's public address switched on, because it is "needed so you can open Alby Hub in your browser," and then to open the Hub at that address.

Its
[Hetzner guide](https://getalby.com/alby-hub/cloud/hetzner)
walks through creating a firewall rule for port 8080 with the source set to "Any IPv4 and Any IPv6, or your own IP address for better security," and its example Docker file publishes the port to every address.

### An Earlier Takeover on an Exposed Hub

This is not the first Alby Hub taken over after being left open. In November 2025, replying to a user whose Hub had been emptied,
[Alby said](https://damus.io/nevent1qqsy66aynuese7y5f43aaqhvulz8g4297gl0v7tk7qcltfxjqtp22cgdwyee4)
the machine was "reachable publicly on the clearnet, so it could be accessed from the outside."

By Alby's account, that was a different problem, not this flaw: the Hub's setup had never been finished, so no unlock password existed yet, and the attacker completed the setup themselves.

After that case,
[a change to Umbrel's app](https://github.com/getumbrel/umbrel-apps/pull/4028)
put Alby Hub behind Umbrel's own login, which had been switched off for it until then. Umbrel's app store now installs v1.24.0, and Alby's own Umbrel listing installs v1.21.4, both newer than the fixed version, though that describes what those stores install today rather than what any given Hub is running.

Two questions the warning leaves open matter to whole groups of users. It tells people to check the installed version, which does not indicate whether Alby Cloud has already handled it for them. It also names v1.7.0 as the start of the affected range without saying where that leaves the releases before it, which go back to v1.0.2.

The Hacker News has put both questions to Alby, along with the question of what the password change is meant to undo.