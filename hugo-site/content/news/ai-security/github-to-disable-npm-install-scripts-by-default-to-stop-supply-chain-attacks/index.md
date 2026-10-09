---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-12T21:33:10.564360+00:00'
exported_at: '2026-06-12T21:33:12.840894+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
structured_data:
  about: []
  author: ''
  description: npm 12 disables install scripts by default, requiring explicit approval
    to reduce dependency-based code execution risks.
  headline: GitHub to Disable npm Install Scripts by Default to Stop Supply Chain
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks
updated_at: '2026-06-12T21:33:10.564360+00:00'
url_hash: f6c292284808b48c029fca5a58d8206473da1216
---

**

Ravie Lakshmanan
**

Jun 11, 2026

Developer Security / Software Supply Chain

GitHub has
[announced](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)
what it said are "breaking changes" coming to npm version 12, one of which turns off install scripts by default to combat software supply chain threats.

The changes aim to combat
[attack techniques](https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html)
that abuse the "npm install" command to trigger the execution of malicious code using npm lifecycle hooks. "Npm install" is used to download and install all the necessary dependencies for a Node.js project. Version 12 is scheduled for release next month.

Describing install-time lifecycle scripts as the "single largest code-execution surface in the npm ecosystem," GitHub
[said](https://github.com/orgs/community/discussions/198547)
the "npm install" command runs scripts from every transitive dependency, as a result of which a single compromised package anywhere in the dependency tree can run arbitrary code on a developer machine or CI runner.

By blocking such behaviours, the idea is to require explicit user approval before code execution is initiated automatically during "npm install" as opposed to being trusted by default. "Making script execution opt-in closes that path while keeping it one command away for the packages you trust," GitHub said.

The changes are listed below -

* npm install will no longer execute preinstall, install, or postinstall scripts from dependencies unless they are explicitly allowed in the project.
* npm install will no longer resolve Git dependencies, either direct or transitive, unless explicitly allowed via --allow-git.
* npm install will no longer resolve dependencies from remote URLs, such as https tarballs, unless explicitly allowed via --allow-remote.

"This includes native node-gyp builds (i.e., a package with a binding.gyp and no explicit install script still gets blocked, because npm runs an implicit node-gyp rebuild for it)," the Microsoft-owned subsidiary said about changes to the default "allowScripts" behavior. "prepare scripts from git, file, and link dependencies are blocked the same way."

By defaulting "--allow-git" to "none," the setting closes out a code execution path where a Git dependency's .npmrc configuration file used could override the Git executable, even with
[--ignore-scripts](https://www.nodejs-security.com/blog/npm-ignore-scripts-best-practices-as-security-mitigation-for-malicious-packages)
, a flag that prevents packages specified in a package.json file from automatically running built-in lifecycle scripts during the installation process.

GitHub recommends that developers prepare for these changes by upgrading to npm 11.16.0 or newer, running the normal install, and reviewing the warnings displayed.

"Use npm approve-scripts --allow-scripts-pending to see which packages have scripts, approve the ones you trust, and commit the updated package.json," it added. "After that, only the scripts you approved keep running once you upgrade. Anything you leave unapproved will stop."

Earlier this year, npm also
[introduced](https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html)
"min-release-age," a setting that tells npm to reject any package version published less than a specified number of days as a safeguard against newly published malicious packages.