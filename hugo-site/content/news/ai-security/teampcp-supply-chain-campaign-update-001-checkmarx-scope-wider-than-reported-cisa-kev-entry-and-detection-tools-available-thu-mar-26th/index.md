---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:58:53.259439+00:00'
exported_at: '2026-04-02T04:58:58.480821+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32834
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Update 001 - Checkmarx Scope Wider
    Than Reported, CISA KEV Entry, and Detection Tools Available, Author: Kenneth
    Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Update 001 - Checkmarx Scope Wider Than
    Reported, CISA KEV Entry, and Detection Tools Available, (Thu, Mar...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32834
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Update 001 - Checkmarx Scope Wider Than Reported,
  CISA KEV Entry, and Detection Tools Available, (Thu, Mar 26th)'
updated_at: '2026-04-02T04:58:53.259439+00:00'
url_hash: a1b9bbaa9c486767cb6f7eee6b262d3a2d831697
---

This is the first update to the TeamPCP supply chain campaign threat intelligence report,
["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
(v3.0, March 25, 2026). That report covers the full campaign from the February 28 initial access through the March 24 LiteLLM PyPI compromise. This update covers developments since publication.

The most significant new finding since the report's publication: the scope of the Checkmarx
`ast-github-action`
compromise was substantially larger than publicly reported.

Checkmarx's official security advisory stated that "all older versions have been permanently deleted" but did not quantify how many tags were affected. This ambiguity allowed the security community to anchor on a single confirmed version — v2.3.28 — as the extent of the compromise. Sysdig's analysis characterized it as "Checkmarx/ast-github-action/2.3.28: (possibly more)." Even Wiz, which assessed that "it is likely all tags were impacted," only observed the single tag directly.

An independent security researcher who was working this incident firsthand at a Checkmarx customer has now provided primary evidence that
**all 91 published tags**
were overwritten — every version from v0.1-alpha through v2.3.32. The evidence is publicly visible in the
[GitHub activity log](https://github.com/Checkmarx/ast-github-action/activity)
, which shows 91 tag deletions performed during Checkmarx's remediation between 19:09 and 19:16 UTC on March 23, 2026.

Three of the malicious commits are still visible on GitHub:

Each malicious commit follows an identical pattern: the legitimate Docker-based
`action.yml`
was replaced with a composite action that executes a credential-stealing
`setup.sh`
before delegating to the legitimate Checkmarx action at pinned SHA
`327efb5d`
. Each commit was individually crafted with a version-appropriate backdated timestamp and fake commit message (e.g., "2.0.30: PR #"). The attacker did not reuse a single malicious commit across multiple tags — they created individual poisoned commits for individual versions.

**The impact of this under-reporting is material.**
Organizations that searched their CI/CD logs only for
`[email protected]`
would have missed compromised runs referencing any of the other 90 poisoned tags. The credential stealer executed regardless of which tag version was referenced.

**Recommended action:**
Search your CI/CD workflow logs for ANY reference to
`checkmarx/ast-github-action`
that executed between 12:58 and 19:16 UTC on March 23, 2026. If found, treat all secrets accessible to that workflow as compromised and rotate immediately. The only safe version is v2.3.33, released during remediation.

For comparison, the companion
`kics-github-action`
received accurate "all 35 tags" reporting from the outset, largely because
[GitHub Issue #152](https://github.com/Checkmarx/kics-github-action/issues/152)
was filed publicly with the title "Malware injected in all Git Tags." No equivalent public issue was filed for
`ast-github-action`
.

## CISA Adds CVE-2026-33634 to Known Exploited Vulnerabilities Catalog

CISA has added
[CVE-2026-33634](https://www.cve.org/CVERecord?id=CVE-2026-33634)
(CVSS 9.4) to the Known Exploited Vulnerabilities (KEV) catalog, confirming active exploitation. Federal agencies are required to remediate by
**April 3, 2026**
. All organizations using Trivy,
`trivy-action`
, or
`setup-trivy`
should verify they are running safe versions:

* **Trivy binary:**
  ≥ v0.69.2
* **trivy-action:**
  v0.35.0 (or pin to SHA
  `57a97c7e7821a5776cebc9bb87c984fa69cba8f1`
  )
* **setup-trivy:**
  v0.2.6 (re-released clean)

## PyPI Quarantine Lifted; LiteLLM Freezes All Releases

PyPI lifted its quarantine of the LiteLLM package on March 25 at 20:15 UTC. Malicious versions 1.82.7 and 1.82.8 have been yanked. However, BerriAI has announced they are
[pausing all new LiteLLM releases](https://docs.litellm.ai/blog/security-update-march-2026)
pending a complete supply chain security review. Google's Mandiant has been engaged for forensic analysis. The last known-safe version is v1.82.6.rc.2.

Any installation of LiteLLM v1.82.7 or v1.82.8 should be treated as compromised — rotate all credentials that were present as environment variables, in configuration files, or in Kubernetes secrets on the affected system.

Two community-developed detection tools are now available:

* **[jthack/litellm-vuln-detector](https://github.com/jthack/litellm-vuln-detector)**
  — Scans for malicious
  `.pth`
  files, persistence backdoors (
  `~/.config/sysmon/sysmon.py`
  , systemd user services), exfiltration domains (
  `models.litellm.cloud`
  ), and attacker Kubernetes pods (
  `node-setup-*`
  in
  `kube-system`
  ).
* **[Community detection gist](https://gist.github.com/sorrycc/30a765b9a82d0d8958e756b251828a19)**
  — Checks for compromised LiteLLM versions and TeamPCP indicators.

Run these against your CI/CD runners, developer workstations, and any systems where LiteLLM was installed during the March 24 exposure window.

## Additional Intelligence

**TeamPCP Telegram statement:**
The threat actor posted to their Telegram channel: "These companies were built to protect your supply chains yet they can't even protect their own... we're gonna be around for a long time stealing terrabytes [sic] of trade secrets with our new partners."
[Socket.dev](https://socket.dev/blog/teampcp-targeting-security-tools-across-oss-ecosystem)
characterizes this as confirmation that TeamPCP is deliberately and systematically targeting security tools as a strategy.

**Wiz publishes third analysis:**
Wiz Research published
["Three's a Crowd: TeamPCP Trojanizes LiteLLM"](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign)
, confirming LiteLLM is present in 36% of cloud environments they monitor. This is the third Wiz blog post covering the campaign arc (Trivy, KICS, LiteLLM).

**RSA Conference timing:**
Analysts assess that TeamPCP may have deliberately timed the LiteLLM attack to coincide with RSA Conference, when many security teams had reduced staffing. This assessment, reported by
[CSO Online](https://www.csoonline.com/article/4149938/trivy-supply-chain-breach-compromises-over-1000-saas-environments-lapsus-joins-the-extortion-wave.html)
, is based on temporal correlation and has not been confirmed by the threat actor or forensic evidence.

**Parallel campaign — ForceMemo:**
[SecurityWeek reports](https://www.securityweek.com/forcememo-python-repositories-compromised-in-glassworm-aftermath/)
a separate campaign ("ForceMemo") using credentials stolen via GlassWorm VS Code extensions to force-push malicious code into approximately 150 GitHub Python repositories. This is NOT TeamPCP but demonstrates the breadth of the current supply chain threat landscape.

## Watch Items

* Named victim breach disclosures — expected imminently given active extortion
* Expansion to RubyGems,
  [crates.io](http://crates.io)
  , or Maven Central — predicted by
  [Endor Labs](https://www.endorlabs.com/learn/teampcp-isnt-done)
  but not yet confirmed
* Aqua Security promised additional findings by end of day March 26
* CISA standalone advisory — KEV entry issued, but no dedicated advisory document yet

The full campaign report is available at
[sans.org/white-papers/when-security-scanner-became-weapon](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
. A SANS Emergency Webcast is scheduled at
[sans.org/webcasts/when-security-scanner-became-weapon](https://www.sans.org/webcasts/when-security-scanner-became-weapon)
.