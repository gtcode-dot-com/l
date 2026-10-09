---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T21:15:16.252374+00:00'
exported_at: '2026-10-07T21:15:17.449005+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html
structured_data:
  about: []
  author: ''
  description: Google temporarily stops OSS VRP product vulnerability reports after
    a surge in automated submissions, most of which it says are invalid.
  headline: Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated
    Reports
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated
  Reports
updated_at: '2026-10-07T21:15:16.252374+00:00'
url_hash: 32fa12f768afd40e582eafa0be46d05cb6dc20db
---

**

Swati Khandelwal
**

Oct 06, 2026

Vulnerability / Open Source

Google has stopped accepting product vulnerability reports through its bug bounty program for its open-source software.

The change, in effect since October 1, means researchers can no longer submit security flaws in the code of projects such as Go, Angular, and Protocol Buffers there for a reward. Reports about supply chain compromises are still accepted, and reports filed before October 1 are not affected.

Google called the stop temporary in a
[post on X](https://x.com/GoogleVRP/status/2105689195180179605)
on October 1 and said it was due to "a significant rise in automated submissions, the vast majority of which are not valid."

The post gave no figures. It did not say whether the submissions were produced with AI tools.

The
[rules of the program](https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules#product-vulnerabilities)
, called the Open Source Software Vulnerability Reward Program (OSS VRP), now carry a notice of the stop. It commits Google to an update in the first quarter of 2027 while it reworks this part of the program.

Neither the post nor the notice gives a date for accepting product vulnerability reports again.

Under the rules, a product vulnerability is a design or implementation flaw in Google's open source software. It must substantially affect the confidentiality or integrity of user data in software built with that code. Examples include memory corruption in file format parsers and path traversal.

The program sorts projects into four tiers based on their sensitivity. Only the top two, called flagship and important, had rewards listed for product vulnerabilities.

The same change that added the notice
[removed those listed amounts](https://github.com/google/bughunters/commit/f8bf23ad82928bfa728214f20dc0af4fa13e310f)
: $500 to $7,500 for flagship projects and $101 to $3,133.7 for important ones. It was published to Google's public GitHub copy of the rules on September 30, a day before the X post.

[Google's list](https://github.com/google/bughunters/blob/main/oss-repository-tier/README.md)
of tiered repositories, last updated in mid-September, names 26 flagship repositories and 47 important ones. The flagship tier includes Go, Angular, Flutter, Bazel, and Protocol Buffers.

Supply chain compromises, which are flaws that could let someone tamper with a project's source code or published packages, keep their listed rewards. So do other security issues, such as leaked credentials that give write access.

| Category | Flagship | Important | Standard |
| --- | --- | --- | --- |
| Supply chain compromises | $3,133.7 to $31,337 | $1,337 to $13,337 | $500 to $3,133.7 |
| Product vulnerabilities | None (was $500 to $7,500) | None (was $101 to $3,133.7) | None |
| Other security issues | $1,000 | $500 | None |

The fourth tier, for low-priority projects, has no listed rewards.

### Where Reports Can Go Now

Google's notice names three routes for researchers:

* **Cloud VRP:**
  Product vulnerability reports may still be accepted for some Google Cloud repositories that affect Google Cloud products, but the notice does not name them. Under the
  [Cloud VRP rules](https://bughunters.google.com/about/rules/google-friends/cloud-vulnerability-reward-program-rules)
  , a flaw in an open source repository maintained by Google Cloud that affects Cloud products is rated at most IT3b. That is the tier for acquisitions and lower-priority products, and the cap applies unless Google's product list says otherwise.
* **Patch rewards:**
  The
  [Patch Rewards Program](https://bughunters.google.com/about/rules/open-source/patch-rewards-program-rules)
  pays $100 to $15,000 for security patches to the projects it covers, not for vulnerability reports. The project's maintainers must accept a patch and remain in place for one month before it can be submitted. A patch that fixes only a single vulnerability is reviewed on a case-by-case basis.
* **Other reward programs:**
  Google asks researchers to check whether a flaw affects something covered by one of its other reward programs and to submit it there. The OSS VRP rules also encourage reporting flaws in projects closely tied to Google Cloud or AI products to the Cloud VRP or the AI VRP.

The notice does not say whether Google will still take product vulnerability reports without a reward.

Some project policies point to other channels. Go
[takes security reports by email](https://go.dev/doc/security/policy)
to its own security team. A
[security policy in Google's GitHub organization](https://github.com/google/.github/blob/master/SECURITY.md)
sends reporters to Google's vulnerability reporting address, g.co/vulnz.

[Angular's security policy](https://github.com/angular/angular/blob/main/SECURITY.md)
, as of October 6, says Angular is part of the OSS VRP, sends vulnerability reports to Google's Bug Hunters site, and names no other channel.

### Earlier Limits on Low-Quality Reports

Google
[launched the OSS VRP](https://thehackernews.com/2022/08/google-launches-new-open-source-bug.html)
in August 2022. In March 2026, it
[began requiring stronger proof](https://bughunters.google.com/blog/ossvrp-rule-updates-2026)
for reports in some tiers to filter out low-quality ones. A patch already merged into the project is one accepted form of proof.

[InfoWorld reported](https://www.infoworld.com/article/4148197/stop-using-ai-to-submit-bug-reports-says-google.html)
at the time that the program's team was concerned about the low quality of some AI-generated submissions, many of which included invented details about how a vulnerability could be triggered.

Separately, the Go project added a section on reports generated by large language models (LLMs) to its security policy in early September. It asks reporters not to send such reports without reviewing and filtering them first.

The policy says LLMs are good at finding real security bugs and just as good at reporting ones that do not exist. Reporters who forward large amounts of unfiltered LLM output will not be credited for their findings.