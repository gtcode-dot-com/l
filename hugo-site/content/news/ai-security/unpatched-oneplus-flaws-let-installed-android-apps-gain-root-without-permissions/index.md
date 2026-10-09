---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T04:54:51.428028+00:00'
exported_at: '2026-10-04T04:54:52.710893+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
structured_data:
  about: []
  author: ''
  description: Two unpatched OnePlus flaws let an installed no-permission app gain
    root on stock OxygenOS phones; no real-world exploitation is known.
  headline: Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions
updated_at: '2026-10-04T04:54:51.428028+00:00'
url_hash: 80b6e80c70459df094d34cbd16851611e8812ff8
---

**

Swati Khandelwal
**

Sep 24, 2026

Vulnerability / Mobile Security

A OnePlus 15 running the latest OxygenOS can be rooted by a malicious app the owner installs, one that asks for no special permissions. A researcher, Rasmus Moorats,
[chained two flaws in OnePlus's own software](https://blog.nns.ee/2026/09/24/oneplus-root/)
to gain root access, the highest level of control over an Android phone.

OnePlus told him the same flaws affect many more of its own devices and those of OPPO, though it has not said which.

OnePlus confirmed both flaws in May. In the same reply, the company told Moorats that it alone decides when to make a flaw public and warned that publishing without its permission could result in legal liability. He published on September 24 anyway, when OnePlus had released no fix.

OnePlus set out its position in the reply,
[which Moorats published in full](https://blog.nns.ee/raw/2026-09-24-oneplus-root/2026-05-20-oneplus-email.txt)
. It said a fix was scheduled, but claimed "the exclusive final right of vulnerability disclosure," and told him that even after a fix ships, researchers may not publish full technical details on their own.

The company argued that European cybersecurity rules require makers to accept and fix reports but do not allow researchers to disclose them without the maker's consent. It warned that if he published without permission, OnePlus would "pursue relevant legal liabilities in accordance with applicable laws."

### How the Attack Works

Moorats found the first flaw in a OnePlus service called
**AtlasService**
, which gathers debugging data, runs as root, and accepts calls from any app without checking who is calling.

A crafted call reaches a OnePlus debugging tool that takes the app's text and drops it, unchecked, into a system command. That hands the app root, but only within a restricted system zone called dumpstate, which cannot do everything root normally can.

The second flaw finishes the job. OnePlus ships another service, a hardware helper called olc2, with a command that executes any shell instruction it receives. Its only guard is that the caller must already be root, which the first flaw provides.

This time, the command runs in a zone that grants all low-level Linux privileges, including the ability to load kernel code, giving the app control of the device at the system level.

### Who Is Affected, and What You Can Do

The attack is local. A malicious app has to be installed and running on the phone first, so it cannot be launched over the internet. But once it is there, the app needs no permissions and shows the user no prompt, and it worked on a stock phone Moorats had not modified.

There is no evidence that anyone has used the flaws in a real attack.

Moorats also confirmed the attack on an older OnePlus 12 Pro, and he expects the same problem across OxygenOS 16 in general. OnePlus and OPPO build their phones on shared software, which is why OnePlus's warning covered both.

As of Moorats's disclosure, OnePlus had assigned no CVE and released no fix, and no OnePlus advisory naming the flaws could be found. Until a fix ships, the one practical defense is the thing the attack needs to get started: install apps only from sources you trust, because it cannot run without a malicious app on the phone.

By Moorats's account, the disclosure ran over about five months:

* **April 18, 2026:**
  reported both flaws to OnePlus.
* **May 20:**
  OnePlus confirmed them, claimed sole control over disclosure, and warned of legal liability if he published.
* **June 22:**
  OnePlus gave an update on its fix and asked him to hold off, and he agreed not to publish before September 17.
* **July 20 and September 11:**
  he asked for updates and received no reply.
* **September 24:**
  he published.

Separately, this is not the only recent case of an installed app reaching root on flagship Android phones.

In August, Lukas Maar, a researcher at the security firm Calif,
[showed a different technique](https://calif.io/research/oempocalypse)
that took a no-permission app to root locked phones running the latest firmware from Samsung, Xiaomi, OPPO, OnePlus, and Realme by attacking code the makers add to Android.

OnePlus has also been slow to answer researchers before. In 2025,
[Rapid7 reported](https://www.rapid7.com/blog/post/cve-2025-10184-oneplus-oxygenos-telephony-provider-permission-bypass-not-fixed/)
a separate OxygenOS flaw that let any app read a user's texts, and said OnePlus did not respond until the research was public.