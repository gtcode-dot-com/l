---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-01T01:10:11.754894+00:00'
exported_at: '2026-06-01T01:10:13.506559+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html
structured_data:
  about: []
  author: ''
  description: Malicious Sicoob.Sdk stole PFX certificates and client IDs via NuGet
    downloads, enabling API impersonation and payment abuse risks.
  headline: Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target
    Cloud Secrets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious Sicoob NuGet Steals Banking Credentials as npm Packages Target Cloud
  Secrets
updated_at: '2026-06-01T01:10:11.754894+00:00'
url_hash: c7e7f0c00e8f99951bfc00c9d4d69027553f16cb
---

Cybersecurity researchers have discovered a malicious NuGet package that masquerades as a C# software development kit for Sicoob, one of Brazil's largest cooperative financial systems, to siphon client IDs and PFX certificates.

According to
[Socket](https://socket.dev/blog/malicious-nuget-package-impersonates-sicoob-sdk)
, versions 2.0.0 through 2.0.4 of "
[Sicoob.Sdk](https://www.nuget.org/packages/Sicoob.Sdk)
" contain functionality to exfiltrate sensitive information, including PFX certificates that are used to authenticate businesses with the Sicoob banking network in order to automate banking operations, such as processing instant payments and generating dynamic Pix QR codes. The package is estimated to have been downloaded nearly 500 times.

"When a developer instantiates SicoobClient with a client ID, a PFX file path, and a PFX password, the package reads the PFX file from disk, Base64-encodes its contents, and sends the supplied client ID, PFX password, and encoded PFX data to a hardcoded third-party Sentry endpoint," security researcher Kirill Boychenko said.

In addition, the package is designed to capture raw Boleto API responses via a separate Sentry path.
[Boleto](https://en.wikipedia.org/wiki/Boleto)
is a popular cash payment method in Brazil for making online and offline purchases. This can potentially expose sensitive transaction details, payment status, amounts, due dates, identifiers, and payer or payee data.

As a result, the stolen data could open the door to severe risks, as it can be abused by the threat actor to impersonate the victim's Sicoob banking API integration, Socket added. Following responsible disclosure, the package has been blocked by NuGet. The profile behind the package, named "sicoob," has also listed 11 other NuGet packages that have collectively racked up about 6,000 downloads.

The application security company also said the package was surfaced by Google Search AI Mode as a legitimate C# library for interacting with Sicoob banking APIs, thereby amplifying the malicious package to unsuspecting developers who may be searching for it.

Another important aspect of the attack is the source-to-package mismatch between the
[linked GitHub repository](https://github.com/Sicoob-Cooperativa)
and the artifact distributed via NuGet. It's suspected that the GitHub repository is designed to lend a veneer of legitimacy to the operation by keeping it clean, while the malicious data-stealing functionality is introduced only in the package uploaded to the registry.

What's more, the compromise of Sicoob API authentication material can also pose indirect risks to end users, as it could leak downstream financial data or enable payment abuse.

Organizations that have installed "Sicoob.Sdk" are recommended to immediately remove the package, treat PFX material as compromised, replace exposed PFX certificates, rotate PFX passwords, and change or disable affected client IDs where applicable. It's also advised to audit Sicoob authentication and API logs for signs of unusual activity.

The development coincides with the
[discovery](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/)
of 14 malicious npm packages that typosquat well-known OpenSearch, ElasticSearch, DevOps, and environment-configuration libraries to harvest AWS credentials, HashiCorp Vault tokens, npm tokens, and CI/CD pipeline secrets from the host environment using a purpose-built credential harvester that's launched through a preinstall hook.

Per the Microsoft Defender Security Research Team, the packages were published by a single threat actor named "vpmdhaj" ("a39155771@gmail.com") on May 28, 2026. The names of the packages are below -

* @vpmdhaj/devops-tools
* @vpmdhaj/elastic-helper
* @vpmdhaj/opensearch-setup
* @vpmdhaj/search-setup
* app-config-utility
* elastic-opensearch-helper
* env-config-manager
* opensearch-config-utility
* opensearch-security-scanner
* opensearch-setup
* opensearch-setup-tool
* search-cluster-setup
* search-engine-setup
* vpmdhaj-opensearch-setup

The findings are the latest in a staggering spate of supply chain attack campaigns that have targeted the npm ecosystem over the past few days -

* [164 malicious npm packages](https://safedep.io/oob-moika-tech-dependency-confusion-campaign/)
  across five scoped namespaces containing a postinstall payload that downloads second-stage JavaScript, spawns it as a detached process, and sends the victim's environment variables ("process.env") to "oob.moika[.]tech/report."
* [141 malicious npm packages](https://safedep.io/malicious-npm-terminal3airport-proxy-adware-spam/)
  published between May 7 and 27, 2026, that abuse npm as free static hosting for an ad-monetized web proxy targeting students, serving popunder ads to those who land these pages through search results or shared links.
* A malicious npm package called "
  [forge-jsxy](https://safedep.io/malicious-forge-jsxy-npm-rat-evolution/)
  " that's capable of keylogging, clipboard monitoring, .env scanning, shell history exfiltration, host inventory, remote filesystem access, screenshot capture, and cryptocurrency wallet scanning. "Forge-jsxy" is assessed to be a continuation of the "
  [forge-jsx](https://thehackernews.com/2026/04/threatsday-bulletin-290m-defi-hack.html#supply-chain-malware-surge)
  " campaign that came to light late last month.
* [176 malicious npm packages](https://www.sonatype.com/blog/inside-a-176-package-npm-campaign-built-to-beat-your-internal-dependencies)
  that employ
  [dependency confusion](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html)
  by using a high version number ("99.99.99") to distribute a postinstall script with capabilities to fingerprint the host and download a platform-specific JavaScript payload, which then conducts additional reconnaissance, exfiltrates credentials and other valuable developer secrets, and downloads and runs a second-stage binary.

In a newly published report, Sonatype said threat actors have outgrown classic typosquatting techniques, moving beyond obvious misspellings to using names that appear convincing in legitimate developer workflows so as to steal data and drop malicious payloads. This, in turn, transforms a routine install step into a risk-prone pathway for reconnaissance, credential theft, and follow-on compromise.

Popular brandjacking techniques include prefix or suffix addition, dependency confusion, version mimicry, embedded target terms, altered scopes or namespaces, and names that resemble the function of a legitimate package.

"'Typosquatting' is now too narrow a label for what this analysis captures," the supply chain security company
[said](https://www.sonatype.com/resources/research/beyond-typosquatting-attacks)
. "The broader pattern is manufactured legitimacy: attackers designing package names to look plausible, useful, and operationally routine inside modern software ecosystems."

These incidents have also unfolded against a series of software supply chain compromises that have been linked to
[TeamPCP](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
(aka Replicating Marauder and UNC6780), which has become a force to be reckoned with by poisoning popular developer tooling across npm, PyPI, Docker Hub, and Packagist in a worm-like fashion.

"Replicating Marauder was not just inserting malicious code into packages, but also exploiting automation, inherited trust, and ordinary CI/CD workflows to push compromise further downstream," BlueVoyant researcher Michael Warren
[said](https://www.bluevoyant.com/blog/how-replicating-marauder-rewired-the-supply-chain-playbook)
.

"This was the point where the campaign most clearly demonstrated that one poisoned dependency or container image could trigger compromise in an unrelated organization's release pipeline. The tactical shift turned isolated software poisoning into a reproducible method for victim-to-victim expansion."

### Update

The campaign that published 164 malicious npm packages across five scoped namespaces to distribute a JavaScript payload has expanded to 179 packages, with a third npm account other than
[mr.4nd3r50n](https://www.npmjs.com/~mr.4nd3r50n)
and
[pik-libs](https://www.npmjs.com/~pik-libs)
,
[t-in-one](https://www.npmjs.com/~t-in-one)
, identified as having pushed 12 more packages across three new scopes.

"Every package in this wave carries the same postinstall hook, reports to the same oob.moika[.]tech host, and authenticates with the same hard-coded secret l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1," SafeDep
[said](https://safedep.io/oob-moika-tech-dependency-confusion-campaign/#update-third-account-and-an-obfuscated-variant)
. "That value had previously appeared only across the mr.4nd3r50n and pik-libs accounts. Its reuse on a third account ties all three to one operator."

It's worth noting that "l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1" refers to the hard-coded X-Secret HTTP header value sent on every outbound C2 request from all three accounts, acting as a single-operator attribution marker. The identified packages and users have since been taken down by npm.

Microsoft, which also published details of the same campaign, the activity is designed to push packages that mirror real internal corporate namespaces, leveraging dependency confusion to push an obfuscated JavaScript dropper for environment fingerprinting and credential reconnaissance.

"The payload runs silently during npm install and operates in 'reconnaissance-only' mode, collecting system information, hostnames, environment variables, and developer context," the Windows maker
[said](https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/)
. "The architecture includes a RECON\_ONLY flag that can be toggled server-side for full exploitation in follow-on attacks."

"Key capabilities observed in the campaign include automatic execution through npm lifecycle hooks, obfuscator.io-style anti-analysis techniques, platform-specific payload delivery (Windows, macOS, Linux), continuous integration and continuous delivery (CI/CD) environment detection and bypass, cache-based deduplication to evade repeated-execution monitoring, and a two-phase attack design (reconnaissance now, exploitation later)."

*(The story was updated after publication on May 31, 2026, to include additional details of the campaign shared by SafeDep and Microsoft.)*