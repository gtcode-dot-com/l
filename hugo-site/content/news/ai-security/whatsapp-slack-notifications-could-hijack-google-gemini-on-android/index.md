---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T02:14:53.058264+00:00'
exported_at: '2026-06-09T02:14:55.112572+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/whatsapp-slack-notifications-could.html
structured_data:
  about: []
  author: ''
  description: Poisoned Android notifications could hijack Google Gemini’s voice assistant
    without a malicious app.
  headline: WhatsApp, Slack Notifications Could Hijack Google Gemini on Android
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/whatsapp-slack-notifications-could.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: WhatsApp, Slack Notifications Could Hijack Google Gemini on Android
updated_at: '2026-06-09T02:14:53.058264+00:00'
url_hash: 0f05c67ffdb5a4ebd181267b84f352e626e88ddb
---

**

Swati Khandelwal
**

Jun 03, 2026

Vulnerability / Artificial Intelligence

A single poisoned notification from WhatsApp, Slack, SMS, Signal, Instagram, or Messenger could have hijacked Google Gemini's voice assistant on Android and made it open a victim's connected windows, fake a message from their boss, push the phone into a Zoom call, or quietly poison its long-term memory.

No malicious app on the phone is required. The assistant just had to treat a hostile notification as useful context.

The research,
[published](https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/)
by SafeBreach's Or Yair, follows the team's earlier "
[Invitation Is All You Need](https://thehackernews.com/2025/08/weekly-recap-nfc-fraud-curly-comrades-n.html#:~:text=Google%20Address%20Promptware%20Attack)
" work, which pulled off similar tricks through malicious Google Calendar invites. After that, Google
[hardened Gemini](https://blog.google/security/mitigating-prompt-injection-attacks/)
against indirect prompt injection.

Yair found a way around the new defenses. Google has since patched it, SafeBreach lists no CVE for the issue, and there is no evidence that the technique was ever used in the wild.

On Android, Gemini's
[Utilities feature](https://support.google.com/gemini/answer/15235441)
can read and reply to your notifications, including ones from apps like WhatsApp. It isn't available on iOS or the web, which keeps this vector Android-only. Yair found the agent that reads those notifications treats their text as instructions it can act on. So anything that can push a notification to a phone can deliver a payload, an attack surface Yair called "
**effectively infinite**
."

At minimum, that lets an attacker rewrite what Gemini says, including faking a message from a named contact. Spoken aloud while you drive and don't look at the screen, "your manager asked you to upload the docs to this Drive folder" is hard to second-guess. The blind version is worse: the payload fires after Gemini has loaded real notifications, so it can grab the first real sender name in the queue and pin the fake message on them.

Faking output is one thing. Firing real tools, like opening a window or launching an app, is what Google's post-"Invitation" mitigations were built to stop. Yair's read, from black-box testing: when a "Yes" authorizes a sensitive action, a check weighs both the user's reply and Gemini's last output to decide whether that "Yes" makes sense. Inject a delayed instruction out of nowhere, and Gemini refused, every time.

So the bypass, which Yair named
**Fake Context Alignment**
, runs two illusions at once: a legitimate-looking authorization for the security check, a harmless exchange for the human.

* **Obfuscated.**
  Gemini asks the real authorization question in a language the victim doesn't speak, say Chinese ("Do you want to open the window?"), then follows in English with something innocuous like "Is that all you needed?" The user shrugs off the foreign phrase as a glitch, says "Yes," and the backend ties that "Yes" to the Chinese question.
* **Muted.**
  Gemini's text-to-speech skips hyperlinks hidden behind clickable text. So the malicious question gets buried in a link the assistant never reads aloud. Gemini says, "I'm sorry, I had an error, are you there?" while the screen silently shows "Do you want to open the window?" The driver says "Yes," the check sees the on-screen text, and the windows open.

Combine the two, a Chinese authorization prompt hidden inside a muted link, and you get a payload that sounds like a normal English exchange while clearing Google's newest checks.

Past the authorization gate, the impacts matched the earlier research and then went further:

* **Smart home control**
  through Google Home: connected windows, boilers, and lights.
* **Tracking and downloads.**
  Opening URLs to geolocate a victim by IP or push file downloads.
* **Crossing into other apps.**
  In the demo, Yair set a safe-looking domain to redirect to a Zoom app link, and Gemini followed it without prompting, forcing the phone to join a meeting and stream video. By his account, it worked because Gemini trusted the domain after it had served clean content, then followed the later redirect. SafeBreach stresses its own domain never redirected to Zoom; the redirect ran on a local server on the test device.
* **Memory poisoning,**
  which the earlier calendar technique never managed. Fake Context Alignment simulates consent, so Gemini persistently saved an attacker-chosen fact. In the demo, it stored the victim's name as "Danny." Because that memory is account-level, the poisoned fact isn't stuck on the phone; it follows the victim wherever they use Gemini on that account.
* **Persistence**
  via scheduled actions, such as a recurring task to read the victim's recent messages every day at 8 PM.

SafeBreach reported the findings to Google's Vulnerability Reward Program on August 17, 2025. Google treated it as a high priority and confirmed on November 14, 2025, that content-classifier improvements mitigated the notification injections and the Delayed Tool Invocation bypass.

Because the fix is server-side, there is no app update to chase. The only control users have is whether Gemini reads notifications at all: disconnect the Utilities app in Gemini's Connected Apps settings, or turn off the Google app's "Notification read, reply &amp; control" permission on Android.