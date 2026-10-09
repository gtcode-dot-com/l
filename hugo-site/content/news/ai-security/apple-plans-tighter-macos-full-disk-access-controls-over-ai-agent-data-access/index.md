---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T05:59:03.075040+00:00'
exported_at: '2026-10-07T05:59:05.646214+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/apple-plans-tighter-macos-full-disk.html
structured_data:
  about: []
  author: ''
  description: Apple plans tighter macOS Full Disk Access controls after AI agent
    use exposed risks to files, messages, mail, and browsing data.
  headline: Apple Plans Tighter macOS Full Disk Access Controls Over AI Agent Data
    Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/apple-plans-tighter-macos-full-disk.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apple Plans Tighter macOS Full Disk Access Controls Over AI Agent Data Access
updated_at: '2026-10-07T05:59:03.075040+00:00'
url_hash: 4a8712355bea80e4868dccc84d2854be88353a93
---

**

Ravie Lakshmanan
**

Oct 05, 2026

Vulnerability / Artificial Intelligence

Apple has announced that it's taking steps to tighten controls around a macOS setting called Full Disk Access (FDA) due to security risks posed by artificial intelligence (AI) agents.

"Some developers are using Full Disk Access in ways that could put users at risk, exposing everything on their systems—including files, mail, messages, and even browsing history – without users' full knowledge and understanding," Apple
[said](https://developer.apple.com/news/?id=p6zjojqw)
in a post. "For communication apps, this can also compromise the privacy of the people users are communicating with."

[Full Disk Access](https://support.apple.com/guide/mac-help/mchlccb25729/mac)
, accessed via Privacy &amp; Security in the Settings app, was introduced by Apple in macOS Mojave (version 10.14), offers users greater control over which applications can access their entire system and data from apps like Mail, Messages, Safari, and Time Machine backups.

Once the setting is enabled for an application, it allows that program to bypass certain security restrictions and read and write to system files that apps are typically restricted from accessing or modifying. This option is essential for apps, such as security tools and backup software, that require deep system access to function properly.

Stating that Full Disk Access largely bypasses controls designed to safeguard users' private data, Apple said it plans to introduce updates to the setting to ensure that this sort of access is granted only with an explicit user action. It's currently not known when the new controls will be rolled out.

"As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially," Apple added. "We are committed to ensuring users clearly understand these risks before granting such access, so they can make informed decisions about their own data and privacy."

Although Apple did not take any specific name, the development appears to be a response to a recent report about how Meta's
[Muse](https://ai.meta.com/muse/)
agentic tool accessed a journalist's private iMessages after
[they](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202)
[granted](https://www.inc.com/jason-aten/meta-keeps-apologizing-for-muse-its-explanations-miss-the-point-entirely/91409363)
it Full Disk Access. Muse is
[advertised](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)
as a "personal AI agent" built along the lines of OpenClaw that runs on a dedicated Linux virtual machine on Meta's cloud.

Meta has since clarified that, for Muse to be able to access a user's private messages, it must have two permissions: have Full Disk Access and have a Messages connector setting in Muse enabled.

"The Messages integration in the Muse Mac app is opt in," Meta CTO David Singleton
[said](https://www.threads.com/@davidsingleton/post/DddI7WtG8ul)
. "Your Muse can only read Messages content if macOS system-level Full Disk Access is granted and the Messages connector is enabled."

Apple's announcement also comes weeks after security researcher Patrick Wardle
[demonstrated](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)
a proof-of-concept (PoC) exploit for a zero-day in Muse's Mac app called not-a-mused that allows any app or terminal command to obtain access to the token that authenticates users to their Muse account.

The now-patched vulnerability "can let an unprivileged local process redirect Muse's dictation traffic and abuse the trust/access granted to the app," Wardle said. "The concern is that Muse may have significantly broader access than ordinary local malware, making it a particularly useful target for privilege/access amplification."

Specifically, a local attacker can exploit an undocumented setting named "endo\_voyager\_dictation\_endpoint" without requiring any special privileges, allowing them to capture dictated audio and prompts, inject malicious prompts, and abuse the access Muse has been granted for other malicious actions.

Wardle has also been
[acknowledged](https://learn.chatgpt.com/docs/changelog#codex-2026-09-25-app)
for reporting
[another vulnerability](https://www.wired.com/story/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data/)
, tracked as
[CVE-2026-100754](https://www.cve.org/CVERecord?id=CVE-2026-100754)
, impacting OpenAI's ChatGPT app for Mac that could have been abused to take over the AI assistant and grant an attacker unauthorized access to chat logs and other data stored by the app.

These findings demonstrate how the
[privileged position](https://www.meta.com/en-gb/help/artificial-intelligence/1047255454427887/)
enjoyed by agentic tools,
[the extensive data they collect](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/)
, and their ability to interact with various parts of the operating system, like writing files to disk, accessing the mic and camera, creating calendar events, sending emails, and monitoring location, can expand the attack surface and open the door for an adversary to abuse this access and steal sensitive data.