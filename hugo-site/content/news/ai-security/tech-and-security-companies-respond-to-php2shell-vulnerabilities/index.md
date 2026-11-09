---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-09T03:34:28.935363+00:00'
exported_at: '2026-11-09T03:34:30.371358+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/tech-and-security-companies-respond-to-php2shell-vulnerabilities
structured_data:
  about: []
  author: ''
  description: Cisco, Palo Alto Networks, Fortinet, Red Hat and others have published
    PHP2Shell advisories as governments urge immediate patching.
  headline: Tech and Security Companies Respond to PHP2Shell Vulnerabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/tech-and-security-companies-respond-to-php2shell-vulnerabilities
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Tech and Security Companies Respond to PHP2Shell Vulnerabilities
updated_at: '2026-11-09T03:34:28.935363+00:00'
url_hash: 8bb16884165cb22685bcc97acaadbdd896506600
---

**Tech vendors, cybersecurity companies and government agencies have published advisories, detections and mitigations for the PHP2Shell vulnerabilities, while many software makers are still checking whether their own products are exposed.**

The two
[critical bugs](https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/)
, CVE-2026-109618 and CVE-2026-109619, can let unauthenticated attackers execute code remotely. Wiz, OpenAI and Calif identified them in August, and PHP
[addressed them](https://www.securityweek.com/php2shell-patches-land-as-first-exploitation-attempts-hit-sensors/)
on October 21 with versions 8.5.12, 8.4.27, 8.3.36, and 8.2.35.

PHP pushed out the release one day ahead of the planned disclosure, after the CVE identifiers started circulating online on October 20.

Amazon says the
[first exploitation attempt](https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/)
came on October 17, before the embargo lifted. Hadrian, Patchstack and Cloudflare all detected attack attempts in the hours leading up to the patches. WatchTowr saw mass exploitation soon after the fixes were published, although the PoC exploits in circulation did not achieve code execution.

With PHP built into a wide range of commercial software, appliances and cloud services, companies across the industry have had to check their exposure.

## **Tech vendors check products, update PHP runtimes**

[Cisco’s](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)
advisory names over 30 products and cloud services under review. Among them are Identity Services Engine, Catalyst Center, Catalyst SD-WAN Manager, Expressway, Umbrella, Webex and the AppDynamics PHP Agent. “Currently, no products are known to be affected,” Cisco says.

Advertisement. Scroll to continue reading.

[Cisco Talos](https://blog.talosintelligence.com/two-critical-rces-in-php-core/)
has outlined the Snort coverage for PHP2Shell, including Community Ruleset rules. Based on open source data, the threat intelligence unit estimates that about half of PHP systems won’t get a patch, and it urges anyone on PHP 8.1 or earlier to move to version 8.2 or newer right away.

[Red Hat’s](https://access.redhat.com/security/cve/cve-2026-109619)
assessment is less severe than NVD’s: it scores both bugs 8.1, compared with 9.8, and doesn’t rate them critical. Regarding
[CVE-2026-109618](https://access.redhat.com/security/cve/cve-2026-109618)
, it says that “reliable exploitation requires precise heap manipulation and timing” and notes that “remote code execution is difficult in practice and typically requires non-default behavior”.

On October 21,
[Ubuntu](https://ubuntu.com/blog/php2shell-vulnerability-fixes-available)
shipped fixes for all its supported releases, and
[Debian](https://packages.debian.org/trixie/php8.4-fpm)
addressed the flaws in its bookworm and trixie releases.

[AWS](https://aws.amazon.com/security/security-bulletins/2026-143-aws/)
is addressing the PHP2Shell vulnerabilities in Elastic Beanstalk, WorkMail, Amazon Linux, and Amazon Lightsail.

[Google Cloud](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619)
itself is not vulnerable, but supported PHP runtimes in the App Engine standard environment were updated automatically, and new base images are being rolled out for the company’s serverless PHP services.

Among hosting control panels, cPanel, Plesk and DirectAdmin shipped patches. cPanel and Plesk also released fixed builds for the end-of-life PHP 7.4, 8.0 and 8.1 branches.

[SolarWinds](https://www.solarwinds.com/trust-center/security-advisories/cve-2026-109618-and-cve-2026-109619)
says it has reviewed its products and internet-facing assets. “Pingdom uses PHP, but we have implemented compensating controls to protect the product,” the company says. It has taken the same approach for its PHP-based external website and says customers don’t need to do anything.

## Security firms roll out detections and mitigations

[Palo Alto Networks](https://security.paloaltonetworks.com/CVE-2026-109618)
says upcoming PAN-OS releases will address the issue, and it has shared workarounds and mitigations for customers to apply in the meantime. The company considers the impact on its products high severity, with a CVSS score of 8.7, and says it has no knowledge of attacks against them.

[Fortinet](https://fortiguard.fortinet.com/psirt/FG-IR-26-186)
has confirmed that two dozen of its products, including FortiOS, FortiManager, FortiAnalyzer and FortiWeb, are not impacted. It is still investigating several others.

[Sophos](https://www.sophos.com/en-us/security-advisories/sophos-sa-20261021-php2shell)
found that its MyUTM portal, a legacy licensing service it hosts for the end-of-life SG UTM product, was running a vulnerable PHP version. The company took the portal offline on October 21 and is updating it before bringing it back.

[Broadcom](https://www.security.com/blog-post/php2shell-critical-vulns-cve-2026-109618-109619)
says it has not confirmed any of its Enterprise Security Group products as affected. Its Symantec and Carbon Black offerings provide behavior-based signatures, a file-based detection for related hacking tools, and four application control rules for spotting activity potentially tied to PHP2Shell attacks.

[CrowdStrike](https://www.crowdstrike.com/en-us/blog/crowdstrike-protects-customers-from-php-rce-zero-days/)
says it confirmed through testing that one unauthenticated POST request is enough to make an Apache mod\_php worker start a shell and execute a command chosen by the attacker, with no vulnerable application code required. It has added PHP2Shell detection content to Falcon Next-Gen SIEM.

Cyber insurer
[Coalition](https://www.coalitioninc.com/blog/security-labs/security-alert-critical-php-vulnerabilities)
says it notified some policyholders it knew were running vulnerable PHP versions on October 20, ahead of public disclosure. Between October 20 and 21, its honeypots logged requests matching the patterns used to exploit the flaws.

[Corelight](https://corelight.com/blog/php2shell-detection-before-disclosure)
, one of the organizations involved in the coordinated response, created Zeek and Suricata detections ahead of disclosure and made them available as open source.

[Qualys](https://blog.qualys.com/vulnerabilities-threat-research/2026/10/20/php-announces-critical-security-release-for-two-vulnerabilities)
rolled out a mitigation that switches off PHP’s session upload-progress feature on affected hosts, and
[JFrog](https://research.jfrog.com/post/php2shell-all-you-need-to-know-about-cve-2026-109618-and-cve-2026-109619/)
cautioned that fake PoCs appeared around the time of disclosure.

[Datadog](https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/)
,
[Endor Labs](https://www.endorlabs.com/learn/php2shell-critical-vulnerabilities-in-php-cve-2026-109618-cve-2026-109619)
,
[Huntress](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities)
,
[Patchstack](https://patchstack.com/articles/php-major-vulnerability-alert-10-2026/)
,
[Recorded Future](https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation)
,
[Sansec](https://sansec.io/research/php2shell)
,
[SOCRadar](https://socradar.io/blog/php2shell-cve-2026-109618-cve-2026-109619/)
and
[Tenable](https://www.tenable.com/blog/php2shell-cve-2026-109618-cve-2026-109619-frequently-asked-questions-about-critical-php-remote)
have also published technical analyses and remediation advice.

## Governments warn of hidden PHP, take sites offline

[CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)
called on organizations to patch right away, starting with internet-facing systems, and cautioned that PHP is frequently embedded in other software, so its presence may not be obvious.

The
[UK’s NCSC](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php)
says discovery efforts should cover every PHP installation, not just outdated ones, and that organizations should keep an eye out for updates from vendors of appliances and services that may ship with PHP. It also recommends hunting for backdoors that attackers may have planted before patches or mitigations were applied.

The
[Dutch NCSC](https://github.com/NCSC-NL/php2shell)
is tracking potentially affected software that depends on PHP in a public GitHub repository.

[CERT-EU](https://cert.europa.eu/publications/security-advisories/2026-018/)
urges organizations to update without delay and to isolate internet-facing applications until the fix has been applied and verified. In a joint
[statement](https://www.enisa.europa.eu/news/joint-statement-on-critical-php-vulnerabilities)
with the European Commission, ENISA, Europol and the EU’s network of national incident response teams, it warned that products may be vulnerable even when PHP runs behind the scenes and isn’t obviously in use.

[Canada’s Cyber Centre](https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619)
and
[Germany’s BSI](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-297981-1032.pdf)
have also issued alerts, both urging organizations to install the updates without delay.

Some organizations chose to go offline rather than stay exposed. According to
[Reuters](https://www.reuters.com/technology/websites-taken-offline-over-php-risks-2026-10-21/)
, several government, school and hospital websites in Europe were taken down on October 21.

**Related**
:
[‘Context Bombs’ Cut AI Attack Success by Misleading Agents With Fake Targets](https://www.securityweek.com/context-bombs-cut-ai-attack-success-by-misleading-agents-with-fake-targets/)

**Related**
:
[High-Severity Flaws Exploited in Three Days as Ransomware Dominates Q3: Rapid7](https://www.securityweek.com/high-severity-flaws-exploited-in-three-days-as-ransomware-dominates-q3-rapid7/)