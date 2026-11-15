---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T03:47:44.068414+00:00'
exported_at: '2026-11-15T03:47:46.424270+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex
structured_data:
  about: []
  author: ''
  description: We’re using Codex to reduce the backporting process time from days
    to hours per fix, empowering human patch reviewers to rapidly submit fixes for
    critical software.
  headline: Backporting security fixes at scale with Codex
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Backporting security fixes at scale with Codex
updated_at: '2026-11-15T03:47:44.068414+00:00'
url_hash: c1e9a888a7165ad2d66ed6ec48608a53d7dd67b1
---

Stable Linux releases lack existing security fixes because backporting them is time-consuming and often thankless work. We’re using Codex to reduce the backporting process time from days to hours per fix, empowering human patch reviewers to rapidly submit fixes for critical software like Ubuntu Long Term Support, Fedora, and the Linux kernel. By October 29, our project helped deliver fixes for
[149 distinct CVEs](https://trailofbits.github.io/ptp-linux-stable-cve-dashboard/)
into stable Linux kernel releases, and
[several](https://bugzilla.redhat.com/show_bug.cgi?id=2520165)
[fixes](https://bugzilla.redhat.com/show_bug.cgi?id=2531860)
to Fedora and Ubuntu packages.

Deploying fixes to older software requires multiple steps, including adapting fixes to older code, checking dependencies, and ensuring the fix did not introduce new bugs. A single task (like tracking down a bug in a bad commit) can take
[a week or more](https://lkml.rescloud.iu.edu/hypermail/linux/kernel/2610.1/04212.html)
of effort that no one sees or appreciates.

Our Codex workflow has reduced the human effort required to prepare and review fixes. Excluding project-specific initial setup, preparing and reviewing a straightforward backport takes about 30 minutes of human attention; a more involved case can take around three hours. The workflow’s approach is twofold: agents perform activities like identifying missing fixes, adapting patches, assembling validation evidence, running tests, and preparing submission packets, while engineers review the patches and submit them to maintainers.

Those estimates only cover patch preparation and review; regression testing and maintainer acceptance remain essential. But the reduced human commitment makes a substantial class of neglected security work practical to undertake. The patch backlog is large, but we now have a practical way to work through it.

## Do we have to decide between stability and security?

Software has bugs, and we try to fix them when we can. The first place the fix happens is in the latest version of the software. Unfortunately, that’s often the
*only*
place where the fix happens.

Backporting is the process of getting a fix from the latest source code to older versions. Fixes for big-name, critical bugs are indeed often backported quickly. But for many other bugs, the backporting process never happens. It is easy to understand why: software packaging is often done by volunteers who are already overworked, and backporting is frustrating, thankless work that gets little credit or publicity. For open source projects staffed by teams of volunteers, backports are (understandably) a low priority. As XFS developer Dave Chinner once described, this work is “
[effectively a full time job](https://lists.openwall.net/linux-kernel/2018/03/28/86)
” that simply goes undone without sufficient resources.

The lack of backports is a problem because almost no one runs the latest and greatest version of software that’s been freshly built with today’s code changes. People
*overwhelmingly*
prefer slightly older, more tested software packaged in “long term stable” releases. For example,
[about 95%](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#lts-releases)
of Ubuntu Linux installations are of the Long Term Support (LTS) variety. When looking at installed Linux kernel packages from Debian’s
[popcon](https://popcon.debian.org/)
, the overwhelming majority are based on older stable trees:

![“A Codex-generated graph of recently installed kernel packages from Debian’s popcon”](/2026/11/02/backporting-security-fixes-at-scale-with-codex/backporting_image1_hu_4b767af928294590.webp)


Figure 1: A Codex-generated graph of recently installed kernel packages from Debian’s popcon. The overwhelming majority (about 96%) are older, stable releases, and not the latest kernel series.

Users are faced with a decision: they can either stick with a stable, familiar version of software that has security flaws, or upgrade to a newer version that fixes those flaws but introduces other changes and new features they may not want.

Many people
*purposely*
do not update to new releases; I think this is entirely justified and normal end-user behavior. Just recently, I updated my Mac to macOS 27 and couldn’t use a printer that had worked flawlessly for years (until Codex wrote a new, compatible printer driver). Similar situations effectively require older software.

We should not have to make a choice between stability and security.

## Thousands of known CVEs lack stable-branch fixes

A swarm of cyber-capable AI agents can cut through a network of stable, known-vulnerable software like a hot knife through butter. The scale of the problem is such that the software you are currently running likely contains unfixed security bugs that can be exploited by modern AI agents. As AI-assisted bug hunting makes it easier to identify vulnerabilities in older code, reducing this backlog becomes increasingly important. This is not merely theoretical. A fix for the latest high-profile bug,
[CVE-2026-98432](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf)
(a critical remotely exploitable flaw in the Linux TCP stack), still had not landed in distribution kernels weeks after being patched upstream. That bug is high-profile enough that it will soon be fixed everywhere. But fixes for more obscure bugs never get backported. I saw this during my
[sandbox escape research](/2026/08/26/vms-wont-contain-cyber-capable-agents/)
, and an old vulnerability in stable software was used as a part of the
[recently disclosed OpenAI hack](https://www.hacktron.ai/blog/hacking-openai)
.

Let’s quantify the scale of the missing backport problem. To make counting simple, we can limit ourselves to known bugs (with assigned CVEs) that are patched in the latest release but missing from stable packages. For this example, we’ll look at the Linux kernel, Ubuntu 26.04 LTS and Debian 13 Stable. I’m not singling out those projects—they are all run very well! I’m using them because they have documentation and accounting for unfixed CVEs. Other projects lack this transparency.

Let’s look at the number of outstanding CVEs in the Linux kernel, by stable branch. The table below shows CVEs per supported stable branch that do not have a fix in that branch, but do have it in a newer branch. (Hence, older branches by definition have more unfixed CVEs.) The source is the
[kernel CVE team’s vulns.git](https://kernel.googlesource.com/pub/scm/linux/security/vulns/)
as of September 18, 2026. This is not an exact bug count, as it both over- and under-counts due to several technicalities. It is also not a measure of exploitability. Rather, it’s a measuring stick showing that a substantial amount of known CVEs have not been fixed in stable kernel branches:

| Branch | Unfixed CVEs | % CVEs with an NVD Score | High or Critical Severity |
| --- | --- | --- | --- |
| 5.10.y | 2,006 | 55.8% | 213 (19.0%) |
| 5.15.y | 1,889 | 51.5% | 195 (20.0%) |
| 6.1.y | 1,329 | 43.9% | 99 (17.0%) |
| 6.6.y | 1,012 | 35.6% | 65 (18.1%) |
| 6.12.y | 686 | 22.3% | 21 (13.7%) |
| 6.18.y | 337 | 15.1% | 3 (5.9%) |

The package landscape is not any better. These are non-kernel CVEs reported as open or affected in Debian 13 and Ubuntu 26.04 (raw data via their
[respective](https://security-tracker.debian.org/tracker/data/json)
[bulk](https://github.com/canonical/ubuntu-security-notices)
CVE data feeds, compiled by Codex). These are distro-metadata findings, not individually source-confirmed vulnerabilities. Again, this is not meant to be an exact bug count, but more of a measuring stick indicating how many unfixed vulnerabilities remain in stable software packages:

| Distribution | Source Packages with Unfixed CVEs | Unique CVEs | High or Critical Severity |
| --- | --- | --- | --- |
| Debian 13 | 1,128 | 4,562 | 1,822 (39.9%) |
| Ubuntu 26.04 | 1,028 | 770 | 335 (43.5%) |

## Engineers and AI can accelerate backporting

We realized this was an issue and have been fixing it proactively. First, we started with the equivalent of finding money on the sidewalk: there are bug fixes to known CVEs that apply cleanly to the stable kernel trees, but the fix was just never pulled into the kernel. We used Codex with GPT-5.6 to find these fixes, and asked the maintainers to apply the existing patches. They did, graciously. We then moved on to backporting patches that don’t apply as-is, starting with the most trivial to validate and review, and are slowly moving towards more complex changes. So far 149 CVE fixes in stable trees are currently applied;
[the list on our backport tracker just keeps growing](https://trailofbits.github.io/ptp-linux-stable-cve-dashboard/)
.

We’ve done the same for Linux distributions: we used Codex and GPT-5.6 to identify known vulnerabilities in shipping stable packages, and then backport and validate a fix. We have begun reaching out to Linux distributions with an initial batch of patches.

If you run an open-source project or a Linux distribution and would like help backporting security fixes, please apply at
[trailofbits.com/patch-the-planet](https://trailofbits.com/patch-the-planet)
and we’ll be glad to assist.

The big upside of stable software that does not add features is that we can, in theory, fix bugs before attackers exploit them. So, let’s continue to patch the planet!