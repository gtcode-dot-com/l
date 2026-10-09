---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T00:14:30.385218+00:00'
exported_at: '2026-10-04T00:14:39.246216+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
structured_data:
  about: []
  author: ''
  description: In security research, Claude Opus 5 helped chain forum and login flaws
    to take over OpenAI staff accounts and reach an internal repository.
  headline: Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained
    Flaws
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained
  Flaws
updated_at: '2026-10-04T00:14:30.385218+00:00'
url_hash: cc2fd48c518b89fdd196794b30fe53529c5a6992
---

Three researchers at the security firm
**Hacktron**
used Anthropic's Claude Opus 5 to chain two flaws and take over the ChatGPT and Codex accounts of several OpenAI employees, then reach an internal OpenAI code repository.

The chain began with a bug in the software that runs OpenAI's public help forum and moved through a weakness in OpenAI's own login system.

This was security research, not a real-world attack: the team reported the flaws to OpenAI, proved the access with a harmless pull request, and then stopped. From the first look, that internal access took under 72 hours.

OpenAI confirmed a fix about 14 hours after the report, according to Hacktron, and on September 1 paid the team a $6,500 bounty. OpenAI said the award "recognizes the OpenAI-side finding, not the actions against Discourse," the open-source software that runs the forum. Testing the forum itself was outside its bug bounty program.

OpenAI has not publicly described the login flaw, and it confirmed the finding through that fix and payment rather than by detailing the account takeovers.

Hacktron, which describes itself as an AI-assisted security research firm, was careful about what it did and did not do. When one employee's Codex link to OpenAI's code on GitHub was opened, it triggered a single pull request in the internal repository. It did not read any source code, merge or ship anything, or touch customer data.

What the chain could have reached was far larger. Because staff connects other services to ChatGPT and Codex, the team said the same access could in theory have extended to tools such as GitHub, Slack, and email. That wider reach was possible, but not used.

### Why a Forum Bug Reached Staff Accounts

The reason a bug in a public forum could reach staff accounts lies in OpenAI's login system, not in the forum software. OpenAI's forum offers a "Sign in with OpenAI" option, the same single sign-on (SSO) that staff uses elsewhere.

Once the researchers took control of the forum server, the shared login let them take over the ChatGPT and Codex accounts of forum members who worked at OpenAI. The victims did not have to do anything.

[Hacktron said](https://www.hacktron.ai/blog/hacking-openai)
this was an OpenAI identity problem, not a flaw in the forum software: any first- or third-party service using the same sign-on could have granted the same access.

The way in was an image bug. The forum runs on Discourse, and Discourse passes uploaded HEIC and HEIF images to a tool called ImageMagick, which uses the libheif library to read them. A flaw in libheif let a specially crafted image corrupt the forum server's memory.

[Discourse's advisory](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335)
rates the result as remote code execution, scores it 8.8 out of 10, and tracks it as
[CVE-2026-32882](https://nvd.nist.gov/vuln/detail/CVE-2026-32882)
. The public record for the flaw itself is narrower. In libheif's own advisory and in national vulnerability databases, CVE-2026-32882 is an out-of-bounds read that can crash the software or leak nearby memory, not a direct code-execution bug.

That leaked memory helps defeat a common protection called ASLR. The researchers say they combined libheif's memory bugs, with the AI's help, to turn the crash into working code execution on the forum server. Upstream, the flaw was fixed in
[libheif 1.22.0](https://github.com/strukturag/libheif/releases/tag/v1.22.0)
in May 2026.

That fix existed months before the test. But the forum's server image, built on the Debian 12 Linux distribution, still shipped the old, unpatched libheif, version 1.19.7, when the researchers looked in July. The fix and its CVE were already public, but Debian had not yet included them in the packaged version the forum used.

If you run your own Discourse server, this part affects you directly. Rebuild on the latest image to get the patched libheif, because a web-interface update alone may not replace the old library. Sites hosted by Discourse were already patched, and the fixed self-hosted releases are 2026.7.0, 2026.6.1, 2026.5.2, and 2026.1.6.

### How the Researchers Used AI

The researchers used AI to do the hard part. They first tried Claude Opus 4.8, which struggled over several sessions to build a working exploit once a standard memory defense, ASLR, was enabled.

Anthropic released its next model,
[Claude Opus 5](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)
, on the evening of July 24, and in a fresh session it produced a working exploit within hours.

Opus 5 shipped with safeguards meant to stop it from writing exploit code for real targets. The researchers got around them by pointing the model at their own test server, disguised as a capture-the-flag practice target, then letting it run in an automated loop. Even so, they say the work was not hands-off: skilled human direction still mattered, and this was not automated hacking with no one at the controls.

The case fits what researchers and AI companies have described this year: capable AI models are sharply cutting the time and skill that serious offensive work used to take. Anthropic has
[reported](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html)
that criminal and state-backed groups are already using its Claude models to run real intrusions, not just to answer questions.

OpenAI was one target in a wider project Hacktron calls
[HEIF Heist](https://heif-heist.com/)
. Over about two months, the team says, it found the same class of image-decoding flaws in software used by other large companies, at a total cost of under $3,000 in AI usage. It links the campaign to reported bugs in Slack, Meta's products, GitHub Enterprise, and web frameworks such as Next.js.

Those broader claims are backed unevenly. The Next.js flaw is confirmed in Vercel's own advisory, and libheif's maintainers confirmed a working code-execution exploit for the bug tied to Meta. The wider claim of code execution across many applications has not been independently confirmed, a limit
[The Hacker News noted](https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html)
when it first covered the Next.js flaw in August.

The wider campaign used a different model, OpenAI's own GPT-5.6 Sol, for cases where the team knew nothing about the target in advance. Only one company, Shopify, appears to have noticed the activity, the researchers say, even though its image processors crashed repeatedly under thousands of test uploads.

The Hacker News has contacted Hacktron with questions about how the forum code execution was achieved and about the scope of the account access.

### What to Do

The bigger lessons go beyond Discourse. If your service accepts user images and reads HEIC, HEIF, or AVIF files through libheif, an old build could be exposed.

And if a public, lower-trust service shares your single sign-on with internal tools, a break-in on that service can become a break-in everywhere the same login reaches.

* Update libheif to the latest security release (
  [1.23.4](https://github.com/strukturag/libheif/releases/tag/v1.23.4)
  as of early September 2026) or to your distribution's patched build.
* Where you do not need it, turn off decoding of untrusted HEIF and AVIF images, or run image processing inside a locked-down sandbox.
* Limit which services your single sign-on trusts, and require a fresh identity check before sensitive actions rather than trusting an existing session.

There is no sign the OpenAI flaw was used against anyone in the real world. As of mid-September 2026, it was not on the U.S. government's list of vulnerabilities known to be exploited, though that list is not proof either way.

What the available reports do not settle is whether an organization that has already patched should still check for earlier access; on that point, the sources are silent.