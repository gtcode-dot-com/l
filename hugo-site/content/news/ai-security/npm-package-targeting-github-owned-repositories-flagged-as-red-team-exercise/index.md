---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T00:50:01.094731+00:00'
exported_at: '2025-11-13T00:50:03.643050+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/researchers-detect-malicious-npm.html
structured_data:
  about: []
  author: ''
  description: Veracode exposes npm package "@acitons/artifact" stealing GitHub tokens
    via build scripts.
  headline: Researchers Detect Malicious npm Package Targeting GitHub-Owned Repositories
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/researchers-detect-malicious-npm.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Detect Malicious npm Package Targeting GitHub-Owned Repositories
updated_at: '2025-11-13T00:50:01.094731+00:00'
url_hash: a6a80c4301b6d58034f0eb674cc569ced1aa0ace
---

**

Nov 11, 2025
**

Ravie Lakshmanan

Software Supply Chain / Malware

Cybersecurity researchers have discovered a malicious npm package named "@acitons/artifact" that typosquats the legitimate "
[@actions/artifact](https://github.com/actions/toolkit/blob/main/packages/artifact)
" package with the intent to target GitHub-owned repositories.

"We think the intent was to have this script execute during a build of a GitHub-owned repository, exfiltrate the tokens available to the build environment, and then use those tokens to publish new malicious artifacts as GitHub," Veracode
[said](https://www.veracode.com/blog/malicious-npm-package-targeting-github-actions/)
in an analysis.

The cybersecurity company said it observed six versions of the package – from 4.0.12 to 4.0.17 – that incorporated a post-install hook to download and run malware. That said, the latest version
[available for download](https://www.npmjs.com/package/@acitons/artifact?activeTab=versions)
from npm is 4.0.10, indicating that the threat actor behind the package,
[blakesdev](https://www.npmjs.com/~blakesdev)
, has removed all the offending versions.

The package was first uploaded on October 29, 2025, and has since accrued 31,398 weekly downloads. In total, it has been
[downloaded 47,405 times](https://npm-stat.com/charts.html?package=%40acitons%2Fartifact)
, according to data from npm-stat. Veracode also said it identified another npm package named "8jfiesaf83" with similar functionality. It's no longer available for download, but it appears to have been
[downloaded 1,016 times](https://npm-stat.com/charts.html?package=8jfiesaf83)
.

Further analysis of one of the malicious versions of the package has revealed that the postinstall script is configured to download a binary named "harness" from a now-removed
[GitHub account](https://github.com/jmasdg)
. The binary is an obfuscated shell script that includes a check to prevent execution if the time is after 2025-11-06 UTC.

It's also designed to run a JavaScript file named "verify.js" that checks for the presence of certain GITHUB\_ variables that are set as part of a GitHub Actions workflow, and exfiltrates the collected data in encrypted format to a text file hosted on the "app.github[.]dev" subdomain.

"The malware was only targeting repositories owned by the GitHub organization, making this a targeted attack against GitHub," Veracode said. "The campaign appears to be targeting GitHub's own repositories as well as a user y8793hfiuashfjksdhfjsk which exists but has no public activity. This user account could be for testing."

### Update

In a statement shared with The Hacker News, a GitHub spokesperson said the identified packages were part of a "tightly controlled exercise" conducted by GitHub's Red Team.

"GitHub takes security seriously and regularly tests its security posture through rigorous, realistic Red Team exercises to ensure resilience against current threat actor techniques. At no point were GitHub systems or data at risk," the spokesperson added.

*(The story was updated after publication with a response from GitHub stating it was a red teaming exercise from the Microsoft-owned subsidiary.)*