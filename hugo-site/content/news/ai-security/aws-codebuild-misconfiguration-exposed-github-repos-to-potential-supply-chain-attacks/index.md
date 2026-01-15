---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-15T22:15:13.217615+00:00'
exported_at: '2026-01-15T22:15:15.507078+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/aws-codebuild-misconfiguration-exposed.html
structured_data:
  about: []
  author: ''
  description: A misconfigured AWS CodeBuild webhook allowed bypass of actor ID checks,
    risking takeover of four AWS GitHub repositories before fixes in Sep 2025.
  headline: AWS CodeBuild Misconfiguration Exposed GitHub Repos to Potential Supply
    Chain Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/aws-codebuild-misconfiguration-exposed.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: AWS CodeBuild Misconfiguration Exposed GitHub Repos to Potential Supply Chain
  Attacks
updated_at: '2026-01-15T22:15:13.217615+00:00'
url_hash: 0567b5c2c108857066b72af6a9bfb84b443b0ec7
---

A critical misconfiguration in Amazon Web Services (AWS)
[CodeBuild](https://aws.amazon.com/codebuild/)
could have allowed complete takeover of the cloud service provider's own GitHub repositories, including its AWS JavaScript SDK, putting every AWS environment at risk.

The vulnerability has been codenamed
**CodeBreach**
by cloud security company Wiz. The issue was fixed by AWS in September 2025 following responsible disclosure on August 25, 2025.

"By exploiting CodeBreach, attackers could have injected malicious code to launch a platform-wide compromise, potentially affecting not just the countless applications depending on the SDK, but the Console itself, threatening every AWS account," researchers Yuval Avrahami and Nir Ohfeld
[said](https://www.wiz.io/blog/wiz-research-codebreach-vulnerability-aws-codebuild)
in a report shared with The Hacker News.

The flaw, Wiz noted, is the result of a weakness in the continuous integration (CI) pipelines that could have enabled unauthenticated attackers to breach the build environment, leak privileged credentials like GitHub admin tokens, and then use them to push malicious changes to the compromised repository – creating a pathway for supply chain attacks.

Put differently, the issue undermines
[webhook filters](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook.html)
introduced by AWS to ensure that only certain events trigger a CI build. For example, AWS CodeBuild can be configured such that a build is triggered only when code changes are committed to a specific branch or when a GitHub or GitHub Enterprise Server account ID (aka ACTOR\_ID or actor ID) matches the regular expression pattern. These filters serve to secure against untrusted pull requests.

The misconfiguration impacted the following AWS-managed open source GitHub repositories, which are configured to run builds on pull requests -

* aws-sdk-js-v3
* aws-lc
* amazon-corretto-crypto-provider
* awslabs/open-data-registry

The four projects, which implemented an ACTOR\_ID filter, suffered from a "fatal flaw" in that they failed to include two characters to ensure – namely the start ^ and end $ anchors – necessary to yield an exact regular expression (regex) match. Instead, the regex pattern allowed any GitHub user ID that was a superstring of an approved ID (e.g., 755743) to bypass the filter and trigger the build.

Because GitHub assigns numeric user IDs sequentially, Wiz said it was able to predict that the new user IDs (currently 9-digits long) would "eclipse" a trusted maintainer's six-digit ID approximately every five days. This insight, coupled with the use of
[GitHub Apps](https://docs.github.com/en/apps/overview)
to automate app creation (which, in turn, creates a corresponding bot user), made it possible to generate a target ID (e.g., 226755743) by triggering hundreds of new bot user registrations.

Armed with the actor ID, an attacker can now trigger a build and obtain the GitHub credentials of the aws-sdk-js-v3 CodeBuild project, a Personal Access Token (PAT) belonging to the aws-sdk-js-automation user, which has full admin privileges over the repository.

The attacker can weaponize this elevated access to push code directly to the main branch, approve pull requests, and exfiltrate repository secrets, eventually setting the stage for supply chain attacks.

"The above repositories' configured regular expressions for AWS CodeBuild webhook filters intended to limit trusted actor IDs were insufficient, allowing a predictably acquired actor ID to gain administrative permissions for the affected repositories," AWS
[said](https://aws.amazon.com/security/security-bulletins/2026-002-AWS/)
in an advisory released today.

"We can confirm these were project-specific misconfigurations in webhook actor ID filters for these repositories and not an issue in the CodeBuild service itself."

Amazon also said it remediated the identified issues, along with implementing additional mitigations, such as credential rotations and steps to secure the build processes that contain GitHub tokens or any other credentials in memory. It further emphasized that it found no evidence of CodeBreach having been exploited in the wild.

To mitigate such risks, it's essential that untrusted contributions does not trigger privileged CI/CD pipelines by enabling the new
[Pull Request Comment Approval](https://docs.aws.amazon.com/codebuild/latest/userguide/pull-request-build-policy.html)
build gate, use
[CodeBuild-hosted runners](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner.html)
to manage build triggers via GitHub workflows, ensure regex patterns in webhook filters are anchored, generate a unique PAT for each CodeBuild project, limit the PAT's permissions to the minimum required, and consider using a dedicated unprivileged GitHub account for CodeBuild integration.

"This vulnerability is a textbook example of why adversaries target CI/CD environments: a subtle, easily overlooked flaw that can be exploited for massive impact," Wiz researchers noted. "This combination of complexity, untrusted data, and privileged credentials creates a perfect storm for high-impact breaches that require no prior access."

This is not the first time CI/CD pipeline security has attracted scrutiny. Last year, research from Sysdig
[detailed](https://www.sysdig.com/blog/insecure-github-actions-found-in-mitre-splunk-and-other-open-source-repositories)
how insecure GitHub Actions workflows associated with the
[pull\_request\_target trigger](https://thehackernews.com/2025/04/spotbugs-access-token-theft-identified.html)
could be exploited to leak the privileged GITHUB\_TOKEN and gain unauthorized access to dozens of open-source projects by using a single pull request from a fork.

A similar
[two-part](https://orca.security/resources/blog/pull-request-nightmare-github-actions-rce/)
[analysis](https://orca.security/resources/blog/pull-request-nightmare-part-2-exploits/)
from Orca Security found insecure pull\_request\_target in projects from Google, Microsoft, NVIDIA, and other Fortune-500 companies that could have allowed attackers to run arbitrary code, exfiltrate sensitive secrets, and push malicious code or dependencies to trusted branches. The phenomenon has been dubbed pull\_request\_nightmare.

"By abusing misconfigured workflows triggered via pull\_request\_target, adversaries could escalate from an untrusted forked pull request into remote code execution (RCE) on GitHub-hosted or even self-hosted runners," security researcher Roi Nisimi noted.

"GitHub Actions workflows that use the pull\_request\_target should never checkout untrusted code without an appropriate validation. Once they do, they are at risk of a full compromise."