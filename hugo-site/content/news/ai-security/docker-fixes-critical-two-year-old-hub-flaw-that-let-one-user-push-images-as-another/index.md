---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-14T05:07:03.845529+00:00'
exported_at: '2026-10-14T05:07:05.567992+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html
structured_data:
  about: []
  author: ''
  description: Docker fixed a critical Hub account conversion flaw that let transferred
    tokens push images as other users; it found no evidence of exploitation.
  headline: Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images
    as Another
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as
  Another
updated_at: '2026-10-14T05:07:03.845529+00:00'
url_hash: 8187d0f2ac60bf6f6560ef4d27402a712c1a7e2e
---

A flaw in Docker Hub, the registry where container images are published and downloaded, let one user push, pull, or delete images as another user. Docker fixed the flaw on September 30 and says it found no evidence that anyone exploited it.

The flaw was in the feature that
[converts a personal account](https://docs.docker.com/accounts/organization/setup/convert-account/)
into an organization, Docker said in a
[security advisory](https://www.docker.com/blog/docker-hub-security-advisory-cve-2026-105445/)
on October 12. Conversion transferred the account's personal access tokens (PATs) to the user designated as the organization's owner. A PAT is used in place of a password in the registry, and the person who created each token can still use it.

The access was limited to the registry. It did not reach the Docker Hub web interface, and it could not be used to change a password, email address, or two-factor settings, or to take over an account.

Docker tracks the flaw as CVE-2026-105445 and rated it critical. The
[CVE record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/105xxx/CVE-2026-105445.json)
it published on October 13 gives the flaw a CVSS 4.0 score of 9.4.

The flaw was open from August 26, 2024, until the fix, a little over two years. Docker made the fix on Docker Hub itself, so there is no update to install.

Docker Hub cannot move a repository from one account to another. A user instead converts a personal account into an organization that keeps the same name, and must name an existing account as its owner.

Each
[personal access token](https://docs.docker.com/security/access-tokens/personal-access-tokens/)
acts as the account that owns it, at a permission level chosen when the token is created. While the flaw was open, conversion changed the owner recorded for each token and left its secret unchanged.

An attacker could abuse this by creating a token on an account they controlled, converting that account into an organization, and naming another user as its owner. The token would then work at the registry as that user.

The named owner was not asked to confirm the change and was not notified, according to Docker and the researchers who reported the flaw. Docker's conversion page has included the sentence "The new owner receives a notification email" since at least August 2024.

Within the token's permission level, a transferred token could pull, push, or delete images in the named owner's repositories and in organizations the owner could access.

Docker rated the flaw critical because that access "includes publishing images under a legitimate name," it said.

In March and April, attackers used
[stolen publisher credentials](https://www.docker.com/blog/trivy-kics-and-the-shape-of-supply-chain-attacks-so-far-in-2026/)
to push
[malicious Trivy images](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html)
and
[malicious KICS images](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html)
to the publishers' own Docker Hub repositories, according to Docker.

Peter Molnar and Krisztian Hozak of mptrdev.com found the flaw and reported it to Docker, which says it deployed the fix less than four hours after receiving their report. They named the flaw GhostPat.

In their
[technical write-up](https://ghostpat.com/)
, the two say they reproduced the flaw twice on consenting test accounts. They logged in to the registry as the target account, created and pushed to a repository in its namespace, pushed to an organization it belonged to, and pulled its private repositories.

### What Docker's Review Covered

Docker reviewed every account conversion made while the flaw was open and compared them with registry logs and token records. It looked for any token used under more than one identity and examined every push made with a transferred token, about 304,000 in all.

"We found no evidence that the vulnerability was exploited," the company said.

Every one of those pushes went to a repository belonging to the converted organization or to its named owner, according to Docker. In the large majority of cases, both accounts belonged to the same person or team.

Where it could not confirm that one person controlled both accounts, Docker analyzed the highest-risk public images without running them and found no malware or tampering.

Docker's registry logs show when a token is used, not that it exists, so a transferred token that was never used left no record in the logs. For that reason, Docker treated every token transferred by a conversion while the flaw was open as possibly affected, whether or not it had been used.

The advisory reports results for pushes. It does not say what Docker found for pulls or deletions made with transferred tokens, including pulls from private repositories.

### Who Was Notified and What to Check

On October 2, Docker emailed the users whose accounts had received transferred tokens and, separately, the owners of the organizations involved. Each email listed the tokens by description and creation date.

The advisory does not say how many users or tokens that covers, calling the group only a "limited number" of users.

Anyone who did not receive the email was not exposed and has nothing to do, according to Docker.

On October 8, Docker deactivated the transferred tokens it had identified. Tokens that their owners had asked to keep were not deactivated.

Todd Matens, who publishes a Docker Compose linter called compose-lint,
[wrote in a blog post](https://dev.to/tmatens/docker-hubs-access-token-vulnerability-how-signing-let-me-verify-my-images-58i3)
that he received two emails on October 2. One was sent to him as an organization owner and the other to his user account. He rotated his two CI tokens and checked the signatures on his 42 published images, tracing each to the CI run that built it.

Docker advises users to review their tokens, revoke any they do not recognize or no longer use, and use organization access tokens, not one person's PAT, for automation that belongs to an organization.

These details help with those checks:

* Open Account settings, then Personal access tokens. The list shows when each token was created and when it was last used.
* The researchers describe two traces. One is a token you did not create, whatever its name, because whoever creates a token chooses its description. The other is an organization in the account switcher that you do not remember joining.
* [Organization access tokens](https://docs.docker.com/security/access-tokens/organization-access-tokens/)
  require a Docker Team or Docker Business subscription. They are managed by an organization owner, a company owner, or a custom role with that permission, and they do not work with Docker Desktop or Image Access Management.
* Organization owners on those subscriptions can review past pushes in the
  [activity logs](https://docs.docker.com/accounts/organization/activity-logs/)
  , which record pushed tags and can show the token that pushed them. Docker Home, where the logs are viewed, keeps them for 30 days, and older entries are available through the Docker Hub API.

### Docker's Documentation Described the Transfer

Docker's own documentation described the token transfer for about 17 of the roughly 25 months the flaw was open. A
[documentation change](https://github.com/docker/docs/commit/0c89cc74132d74f7aa4afd0e859da2109d4bef59)
on April 22, 2025, added a note to Docker's conversion page. It said that naming a user as organization owner "will ensure any PATs associated with the user's account are transferred to the organization owner."

Docker
[removed the note](https://github.com/docker/docs/commit/1ebe400624597c82a7a32e330315c9aae8d32429)
on September 30, minutes after the time it gives for the fix. The dates come from the public history of Docker's documentation, which The Hacker News reviewed.

Docker says it now requires consent before a user is named an organization owner and notifies that user when this happens. It also records every change in token ownership and reviews other features that change who owns a credential.