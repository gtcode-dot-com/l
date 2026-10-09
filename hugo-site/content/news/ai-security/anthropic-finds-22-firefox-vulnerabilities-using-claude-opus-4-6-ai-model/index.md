---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-09T23:27:02.717134+00:00'
exported_at: '2026-03-09T23:27:04.679366+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html
structured_data:
  about: []
  author: ''
  description: Anthropic’s Claude Opus 4.6 AI found 22 Firefox vulnerabilities, including
    14 high severity, helping Mozilla patch flaws in Firefox 148.
  headline: Anthropic Finds 22 Firefox Vulnerabilities Using Claude Opus 4.6 AI Model
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Anthropic Finds 22 Firefox Vulnerabilities Using Claude Opus 4.6 AI Model
updated_at: '2026-03-09T23:27:02.717134+00:00'
url_hash: 90b28db64afccfc07c4db9fb88c28b5e731e7da9
---

**

Ravie Lakshmanan
**

Mar 07, 2026

Browser Security / Artificial Intelligence

Anthropic on Friday said it
[discovered](https://www.anthropic.com/news/mozilla-firefox-security)
22 new security vulnerabilities in the Firefox web browser as part of a security partnership with Mozilla.

Of these, 14 have been classified as high, seven have been classified as moderate, and one has been rated low in severity. The issues were addressed in
[Firefox 148](https://www.firefox.com/en-US/firefox/148.0/releasenotes/)
, released late last month. The
[vulnerabilities](https://www.mozilla.org/en-US/security/advisories/mfsa2026-13/)
were identified over a two-week period in January 2026.

The artificial intelligence (AI) company said the number of high-severity bugs identified by its Claude Opus 4.6 large language model (LLM) represents "almost a fifth" of all high-severity vulnerabilities that were patched in Firefox in 2025.

Anthropic said the LLM detected a use-after-free bug in the browser's JavaScript after "just" 20 minutes of exploration, which was then validated by a human researcher in a virtualized environment to rule out the possibility of a false positive.

"By the end of this effort, we had scanned nearly 6,000 C++ files and submitted a total of 112 unique reports, including the high- and moderate-severity vulnerabilities mentioned above," the company said. "Most issues have been fixed in Firefox 148, with the remainder to be fixed in upcoming releases."

The AI upstart said it also fed its Claude model access to the entire list of vulnerabilities submitted to Mozilla and tasked the AI tool with developing a practical exploit for them.

Despite carrying out the test several hundred times and spending about $4,000 in API credits, the company said Claude Opus 4.6 was able to turn the security defect into an exploit only in two cases.

This behavior, the company added, signaled two important aspects: the cost of identifying vulnerabilities is cheaper than creating an exploit for them, and the model is better at finding issues than at exploiting them.

"However, the fact that Claude could succeed at automatically developing a crude browser exploit, even if only in a few cases, is concerning," Anthropic emphasized, adding the exploits only worked within the confines of its testing environment, which has had some security features like sandboxing intentionally stripped off.

A crucial component incorporated into the process is a task verifier to determine if the exploit actually works, giving the tool real-time feedback as it explores the codebase in question and allowing it to iterate its results until a successful exploit is devised.

One such exploit Claude wrote was for
[CVE-2026-2796](https://nvd.nist.gov/vuln/detail/CVE-2026-2796)
(CVSS score: 9.8), which has been
[described](https://red.anthropic.com/2026/exploit/)
as a just-in-time (JIT) miscompilation in the JavaScript WebAssembly component.

The disclosure comes weeks after the company
[released](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html)
Claude Code Security in a limited research preview as a way to fix vulnerabilities using an AI agent.

"We can't guarantee that all agent-generated patches that pass these tests are good enough to merge immediately," Anthropic said. "But task verifiers give us increased confidence that the produced patch will fix the specific vulnerability while preserving program functionality—and therefore achieve what's considered to be the minimum requirement for a plausible patch."

Mozilla, in a coordinated announcement, said the AI-assisted approach has discovered 90 other bugs, most of which have been fixed. These consisted of assertion failures that overlapped with issues traditionally found through fuzzing and distinct classes of logic errors that the fuzzers failed to catch.

"The scale of findings reflects the power of combining rigorous engineering with new analysis tools for continuous improvement," the browser maker
[said](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)
. "We view this as clear evidence that large-scale, AI-assisted analysis is a powerful new addition to security engineers' toolbox."