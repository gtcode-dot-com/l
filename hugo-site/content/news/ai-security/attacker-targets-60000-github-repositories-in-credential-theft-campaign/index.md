---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:22:23.082914+00:00'
exported_at: '2026-11-15T06:22:24.569504+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/attacker-targets-60000-github-repositories-in-credential-theft-campaign
structured_data:
  about: []
  author: ''
  description: An attacker used 4,837 compromised GitHub accounts to probe 61,764
    repositories and deploy a stealer of CI secrets and cloud keys.
  headline: Attacker Targets 60,000 GitHub Repositories in Credential Theft Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/attacker-targets-60000-github-repositories-in-credential-theft-campaign
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attacker Targets 60,000 GitHub Repositories in Credential Theft Campaign
updated_at: '2026-11-15T06:22:23.082914+00:00'
url_hash: 486cd2119a9117eec9745948cbc2daa6fe2d4952
---

**An attacker has tested stolen access to more than 60,000 GitHub repositories and inserted credential-stealing code in thousands of them, several security firms report.**

Aikido Security said the operation, which it calls
[wfx-loot](https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories)
, began on November 10. It identified roughly 4,800 compromised accounts behind probe pull requests submitted to 61,764 repositories.

The requests were used to establish whether the stolen access permitted changes to a repository. “The pull request does nothing by itself,” StepSecurity explained, noting that malware was subsequently deployed in repositories where the permissions and configuration allowed it.

Aikido found signs that the stealer ran in more than 1,800 repositories. SafeDep separately
[counted](https://safedep.io/blog/github-actions-wfx-credential-stealer)
8,093 public repositories that received malicious commits, a figure that does not necessarily indicate successful execution.

“The attacker does not exploit a bug in GitHub Actions,” StepSecurity
[noted](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)
. The intruder instead relies on valid tokens belonging to developer and bot accounts.

The attacker placed the malware in existing or new GitHub Actions workflows, shell scripts run by CI systems, and npm installation hooks. The npm method also poses a risk to developers who install dependencies while the malicious changes are present.

Advertisement. Scroll to continue reading.

The script looks for GitHub tokens, repository secrets, cloud credentials and AI service keys. It also reads GitHub Actions runner process memory and has functionality designed to expand access and establish persistence in AWS and Azure.

The attacker usually reversed the code changes and deleted workflow runs to conceal the activity.

StepSecurity traced 173 probe pull requests to tokens issued to the Fly.io GitHub app. The firm said it could not determine how the tokens were obtained and had no evidence that Fly.io’s infrastructure had been breached.

Affected software releases include a Packagist package and versions of two Go modules.

Aikido identified similarities with October’s
[GhostAction](https://www.securityweek.com/in-other-news-ai-used-in-korean-bank-breaches-poem-guided-botnet-empire-admin-gets-40-years/)
campaign but assessed that the two operations probably involved different actors.

The security firm warned that organizations should assume all accessible secrets were compromised if the malware executed. Organizations have been advised to revoke compromised tokens, rotate exposed secrets, and check for unauthorized cloud changes.

**Related**
:
[Notion Customer Data Compromised in Fireworks AI Hack](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/)

**Related**
:
[500,000 Active Credentials Left Exposed on GitHub](https://www.securityweek.com/500000-active-credentials-left-exposed-on-github/)

**Related**
:
[Meta Says Hackers Took Code, Personal Data of 1,500 in GitHub Breach](https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/)