---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-09T23:27:02.347495+00:00'
exported_at: '2026-03-09T23:27:04.681920+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html
structured_data:
  about: []
  author: ''
  description: OpenAI launches Codex Security AI agent that scanned 1.2M commits,
    finding 792 critical and 10,561 high-severity vulnerabilities in open-source projec
  headline: OpenAI Codex Security Scanned 1.2 Million Commits and Found 10,561 High-Severity
    Issues
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Codex Security Scanned 1.2 Million Commits and Found 10,561 High-Severity
  Issues
updated_at: '2026-03-09T23:27:02.347495+00:00'
url_hash: 8e8ecbeefb89973eafa73cf47b293532ef5976f3
---

**

Ravie Lakshmanan
**

Mar 07, 2026

DevSecOps / Artificial Intelligence

OpenAI on Friday began rolling out
**Codex Security**
, an artificial intelligence (AI)-powered security agent that's designed to find, validate, and propose fixes for vulnerabilities.

The feature is available in a research preview to ChatGPT Pro, Enterprise, Business, and Edu customers via the Codex web with free usage for the next month.

"It builds deep context about your project to identify complex vulnerabilities that other agentic tools miss, surfacing higher-confidence findings with fixes that meaningfully improve the security of your system while sparing you from the noise of insignificant bugs," the company
[said](https://openai.com/index/codex-security-now-in-research-preview/)
.

Codex Security represents an evolution of
[Aardvark⁠](https://thehackernews.com/2025/10/openai-unveils-aardvark-gpt-5-agent.html)
, which OpenAI unveiled in private beta in October 2025 as a way for developers and security teams to detect and fix security vulnerabilities at scale.

Over the last 30 days, Codex Security has scanned more than 1.2 million commits across external repositories over the course of the beta, identifying 792 critical findings and 10,561 high-severity findings. These include vulnerabilities in various open-source projects like OpenSSH⁠, GnuTLS⁠, GOGS⁠, Thorium⁠, libssh, PHP, and Chromium, among others. Some of them have been listed below -

* GnuPG - CVE-2026-24881, CVE-2026-24882
* GnuTLS - CVE-2025-32988, CVE-2025-32989
* GOGS - CVE-2025-64175, CVE-2026-25242
* [Thorium](https://www.cisa.gov/resources-tools/resources/thorium)
  - CVE-2025-35430, CVE-2025-35431, CVE-2025-35432, CVE-2025-35433, CVE-2025-35434, CVE-2025-35435, CVE-2025-35436

According to the AI company, the latest iteration of the application security agent leverages the reasoning capabilities of its frontier models and combines them with automated validation to minimize the risk of false positives and deliver actionable fixes.

OpenAI's scans on the same repositories over time have demonstrated increasing precision and declining false positive rates, with the latter falling by more than 50% across all repositories.

In a statement shared with The Hacker News, OpenAI said Codex Security is designed to improve signal-to-noise by grounding vulnerability discovery in system context and validating findings before surfacing them to users.

Specifically, the agent works in three steps: it analyzes a repository to get a handle on the project's security-relevant structure of the system and generates an editable threat model that captures what it does and where it's most exposed.

Once the system context is built, Codex Security uses it as a foundation to identify vulnerabilities and classifies findings based on their real-world impact. The flagged issues are pressure-tested in a sandboxed environment to validate them.

"When Codex Security is configured with an environment tailored to your project, it can validate potential issues directly in the context of the running system," OpenAI said. "That deeper validation can reduce false positives even further and enable the creation of working proofs-of-concept, giving security teams stronger evidence and a clearer path to remediation."

The final stage involves the agent proposing fixes that best align with the system behavior so as to reduce regressions and make them easier to review and deploy.

News of Codex Security comes weeks after Anthropic launched
[Claude Code Security](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html)
to help users scan a software codebase for vulnerabilities and suggest patches.