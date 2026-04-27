---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-27T14:15:14.560683+00:00'
exported_at: '2026-04-27T14:15:16.803439+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32926
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Update 008 - 26-Day Pause Ends with
    Three Concurrent Compromises (Checkmarx KICS, Bitwarden CLI Cascade, xinference
    PyPI), CanisterSprawl npm Worm Identified, and Tier 1 Coverage Returns, Author:
    Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Update 008 - 26-Day Pause Ends with Three
    Concurrent Compromises (Checkmarx KICS, Bitwarden CLI Cascade, x...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32926
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Update 008 - 26-Day Pause Ends with Three Concurrent
  Compromises (Checkmarx KICS, Bitwarden CLI Cascade, xinference PyPI), CanisterSprawl
  npm Worm Identified, and Tier 1 Coverage Returns, (Mon, Apr 27th)'
updated_at: '2026-04-27T14:15:14.560683+00:00'
url_hash: 66a870ade09bc792a20c3584e7656a9fffcd5aa6
---

This update succeeds
[TeamPCP Supply Chain Campaign Update 007](https://isc.sans.edu/diary/TeamPCP+Supply+Chain+Campaign+Update+007+Cisco+Source+Code+Stolen+via+TrivyLinked+Breach+Google+GTIG+Tracks+TeamPCP+as+UNC6780+and+CISA+KEV+Deadline+Arrives+with+No+Standalone+Advisory/32880/)
, published April 8, 2026, which left the campaign in credential-monetization mode following the Cisco source code theft via Trivy-linked credentials, Google GTIG's formal designation of the operators as UNC6780 (with their credential stealer named SANDCLOCK), and the lapsed CISA KEV remediation deadline for CVE-2026-33634 with no standalone federal advisory. The Sportradar publication deadline flagged in Update 007 (approximately April 10 to 11) lapsed without a public CipherForce dump, and CipherForce's leak infrastructure has remained offline. Twelve days after Update 007, the technical compromise picture changed sharply across the W17 window (April 20 through April 26).

The most significant development of the week was the end of TeamPCP's 26-day supply chain compromise pause, with three concurrent package compromises landing across npm, PyPI, and Docker Hub between April 21 and 22. The Checkmarx KICS Docker Hub repository was compromised on April 22 (claimed by TeamPCP via @pcpcats), the xinference PyPI package was poisoned the same day with a TeamPCP marker that the group publicly denied, and a self-propagating npm worm tracked as CanisterSprawl was identified by Socket and StepSecurity beginning April 21. The KICS Docker compromise then cascaded into a downstream compromise of @bitwarden/cli version 2026.4.0 the same evening when Bitwarden's Dependabot automation pulled the malicious checkmarx/kics:latest image into the Bitwarden CI/CD pipeline. Reporting suggests the campaign has visibly returned to its technical-discovery and active-compromise phase after spending most of April in credential-monetization mode; analysts assess the operators retain full operational capability despite the prior month's monetization failures.

## Dated event log

* 2026-04-20: ADT filed a Form 8-K with the SEC disclosing unauthorized access to certain cloud-based environments first identified the same day, with ShinyHunters subsequently posting a leak-site claim of over 10 million records and a 2026-04-27 publication deadline. The intrusion was attributed to a vishing attack against an ADT employee's Okta single sign-on account, which is a different access vector than the Trivy credential trove and therefore is NOT a confirmed TeamPCP supply chain campaign event; it is logged here only because ShinyHunters has been documented in prior updates as part of the TeamPCP-affiliated extortion ecosystem and remained operationally active during the target week. Source: BleepingComputer,
  <https://www.bleepingcomputer.com/news/security/adt-confirms-data-breach-after-shinyhunters-leak-threat/>
  and Help Net Security,
  <https://www.helpnetsecurity.com/2026/04/27/adt-systems-data-breach/>
* 2026-04-21: Socket and StepSecurity began identifying a self-propagating npm supply chain worm tracked as CanisterSprawl, embedded across at least 16 malicious package versions across the @automagik, pgserve, @fairwords, and @openwebconcept publisher namespaces (initial publisher ties to Namastex Labs and associated accounts). The worm executes via npm postinstall hook, harvests roughly 40 credential categories via regex sweep, and exfiltrates to a dual-channel endpoint that includes an Internet Computer Protocol (ICP) canister, the same C2 architecture pattern used by TeamPCP's CanisterWorm. Socket and StepSecurity assess the lineage as TeamPCP-style without making a definitive same-actor attribution. The worm is cross-ecosystem, jumping from npm to PyPI if it discovers a PyPI publish token on the infected host. Source: Socket,
  <https://socket.dev/blog/namastex-npm-packages-compromised-canisterworm>
  and The Hacker News,
  <https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html>
* 2026-04-22: At approximately 12:35 UTC a threat actor authenticated to Docker Hub using valid Checkmarx publisher credentials and pushed malicious images to the official checkmarx/kics repository. Five existing tags (latest, v2.1.20, v2.1.20-debian, alpine, debian) were overwritten to malicious digests, and two new tags (v2.1.21, v2.1.21-debian) were created. The poisoned KICS binary retained legitimate scanning behavior and added a covert telemetry path that exfiltrated infrastructure-as-code scan output (which routinely contains credentials, tokens, and internal topology) to attacker-controlled infrastructure at hxxps://audit.checkmarx[.]cx/v1/telemetry with User-Agent "KICS-Telemetry/2.0". The dangerous Docker Hub window was 14:17:59 UTC to 15:41:31 UTC. Trojanized cx-dev-assist (versions 1.17.0 and 1.19.0) and ast-results (versions 2.63.0 and 2.66.0) VS Code and Open VSX extensions were also identified, which silently downloaded a second-stage mcpAddon.js payload from a backdated commit in the official Checkmarx GitHub repository and executed it via the Bun runtime without integrity verification. Source: BleepingComputer,
  <https://www.bleepingcomputer.com/news/security/new-checkmarx-supply-chain-breach-affects-kics-analysis-tool/>
  and Socket,
  <https://socket.dev/blog/checkmarx-supply-chain-compromise>
  and Checkmarx,
  <https://checkmarx.com/blog/checkmarx-security-update-april-22/>
* 2026-04-22: TeamPCP claimed responsibility for the Checkmarx KICS compromise via the @pcpcats X account, posting "Thank you OSS distribution for another very successful day at PCP inc." shortly after Socket and Checkmarx coordinated public disclosure. This is the second documented Checkmarx compromise by TeamPCP within sixty days; the prior incident in March affected the kics-github-action and ast-github-action GitHub Actions tags. Source: Dark Reading,
  <https://www.darkreading.com/application-security/checkmarx-kics-code-scanner-widening-supply-chain>
* 2026-04-22: Three consecutive xinference PyPI releases (versions 2.6.0, 2.6.1, and 2.6.2) were published from a bot account with a malicious base64-encoded payload injected directly into
  **init**
  .py, executing automatically on package import. The payload swept AWS credentials, Google Cloud configurations, Kubernetes tokens, environment variables, SSH keys, API keys, and database credentials, exfiltrating to hxxps://whereisitat[.]lucyatemysuperbox[.]space/. xinference has approximately 600,000 cumulative downloads. The payload contains the comment "# hacked by teampcp" and is structurally similar to prior TeamPCP campaigns (double base64 encoding, detached subprocess on import, exhaustive credential sweep), but TeamPCP publicly denied involvement via their X account and characterized the attack as a copycat using TeamPCP's name and tooling. Source: StepSecurity,
  <https://www.stepsecurity.io/blog/teampcp-injects-two-stage-credential-stealer-into-xinference-pypi-package>
  and JFrog,
  <https://research.jfrog.com/post/xinference-compromise/>
  and OX Security,
  <https://www.ox.security/blog/xinference-allegedly-hacked-by-teampcp-malicious-package-in-pypi/>
* 2026-04-22: @bitwarden/cli version 2026.4.0 was published to npm with malicious code in bw1.js between 5:57 PM and 7:30 PM ET, with approximately 334 downloads before detection and removal. The compromise occurred when Bitwarden's Dependabot-driven CI/CD automation pulled the malicious checkmarx/kics:latest Docker image into the Bitwarden build pipeline during the dangerous Docker Hub window, demonstrating cascading impact from the KICS compromise to a downstream consumer through trusted automation. The malicious payload contained the string "Shai-Hulud: The Third Coming" along with Dune-themed identifiers (atreides, fremen, sandworm, sardaukar) and exfiltrated GitHub tokens, npm tokens, SSH material, AWS/GCP/Azure secrets, GitHub Actions secrets, and AI tooling configuration files to public GitHub repositories created under victim accounts. Bitwarden released version 2026.4.1 (a re-release of 2026.3.0) and stated that no end-user vault data was accessed. Source: The Hacker News,
  <https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html>
  and SecurityWeek,
  <https://www.securityweek.com/bitwarden-npm-package-hit-in-supply-chain-attack/>
  and JFrog,
  <https://research.jfrog.com/post/bitwarden-cli-hijack/>
* 2026-04-23: GitGuardian published a synthesis piece framing the three concurrent compromises (Checkmarx KICS, xinference, CanisterSprawl/pgserve) as a "no off season" demonstration, noting all three campaigns shared the same operational objective of harvesting CI/CD and developer-environment credentials and that two of the three were claimed by or attributed to TeamPCP. Source: GitGuardian,
  <https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/>
* 2026-04-23: Dark Reading published "Checkmarx KICS Code Scanner Targeted in Widening Supply Chain Hit", reintroducing TeamPCP into Tier 1 mainstream coverage for the first time during the April monetization phase. SecurityWeek, BleepingComputer, The Hacker News, and Cybernews all carried original Tier 1 reporting on the Checkmarx and Bitwarden incidents this week. Source: Dark Reading,
  <https://www.darkreading.com/application-security/checkmarx-kics-code-scanner-widening-supply-chain>
  and SecurityWeek,
  <https://www.securityweek.com/bitwarden-npm-package-hit-in-supply-chain-attack/>
  and Cybernews,
  <https://cybernews.com/security/checkmarx-popular-tools-spread-credential-stealing-malware/>
* 2026-04-24: Docker published a vendor blog post ("Trivy, KICS, and the shape of supply chain attacks so far in 2026") describing the platform's internal monitoring detection of the KICS push, the half-hour-from-push detection window, and the coordinated response with Socket and Checkmarx. This is the first time Docker has provided a public retrospective on a TeamPCP-related compromise from the platform-side perspective. Source: Docker,
  <https://www.docker.com/blog/trivy-kics-and-the-shape-of-supply-chain-attacks-so-far-in-2026/>
* 2026-04-24: OX Security and Endor Labs published deeper analyses of the Bitwarden CLI compromise. OX Security highlighted the "Shai-Hulud: The Third Coming" tag and the Dune-themed exfiltration repository naming, suggesting overlap between the TeamPCP operator set and the prior Shai-Hulud npm worm campaigns of late 2025; Endor Labs documented the Dependabot pivot in detail. Source: OX Security,
  <https://www.ox.security/blog/shai-hulud-bitwarden-cli-supply-chain-attack/>
  and Endor Labs,
  <https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack>

## Themes and trends

* The supply chain pause ended decisively. Prior weekly and daily updates documented an approximately 26-day gap from the Telnyx PyPI disclosure (March 27) without new package compromises, and the W16 weekly characterized the campaign as being in a "credential monetization phase" rather than active compromise. The April 21 to 22 cluster of three new compromises across three different ecosystems (npm, PyPI, Docker Hub) ends that pause and demonstrates the operators retained the access, the publishing-credential foothold, and the operational tempo to mount synchronized multi-ecosystem operations. The KICS compromise specifically used valid Checkmarx publisher credentials, which suggests the credential-theft pipeline from prior campaigns has produced reusable access into vendor publishing infrastructure beyond the originally compromised ecosystems.
* Cascading impact from one compromise to another is now empirically demonstrated. The Bitwarden CLI compromise was not a separate intrusion: it was a downstream consequence of the KICS Docker image push, propagated through Bitwarden's trusted Dependabot automation. Reporting suggests this is the first documented case in this campaign of a compromise of one popular developer tool automatically poisoning the build pipeline of another popular developer tool through ordinary dependency-update automation. Analysts assess this validates a long-flagged theoretical risk: in a supply chain campaign where security tooling is the target, automated pull-through compromises will compound exponentially with the popularity and trust of each compromised artifact.
* The "TeamPCP claims one, denies the other" pattern is analytically significant. In the same 24 hour window, TeamPCP explicitly took credit for Checkmarx (via the @pcpcats account, with taunting language) but explicitly denied the xinference compromise that bore its branding marker. Both attacks share TeamPCP's operational signature (double base64 encoding, detached subprocess on import, exhaustive credential sweep). Reporting suggests three possible explanations: (1) genuine copycat or splinter actor reusing leaked TeamPCP tooling; (2) deliberate false flag by TeamPCP intended to muddy attribution; or (3) operational discipline whereby TeamPCP claims compromises it considers high-prestige (a security vendor) and disowns those it considers low-prestige or unprofitable (an inference framework with low corporate footprint). Analysts assess explanation (1) is most likely given the simultaneous scaling of the broader extortion ecosystem (Vect, ShinyHunters, CanisterSprawl), but cannot rule out the others.
* Tier 1 coverage returned in force after six quiet weeks. BleepingComputer, Dark Reading, SecurityWeek, The Hacker News, and Cybernews all published original TeamPCP-related reporting during the target week, ending the longest dry spell since the campaign began. The catalyst was new technical compromise events rather than victim disclosures, consistent with the W16 analyst observation that mainstream coverage of this campaign is driven by novel compromises rather than ongoing extortion activity.
* Vect's leak site went quiet despite prior projections. The W16 weekly identified a 9 day 8 hour negotiation countdown on the Guesty listing that placed expected publication around April 24. Monitoring of ransomware.live during the target week shows Vect's victim count remained at 25, with no new TeamPCP-tagged listings and no public publication of Guesty or S&P Global data through April 26. Reporting suggests one of three possibilities: (1) negotiations are progressing privately, (2) Vect is conserving public output while TeamPCP regains technical operational focus, or (3) the publishing infrastructure once again hit a disruption. Analysts assess this is the third consecutive lapsed Vect-or-CipherForce monetization deadline (after ShinyHunters/Cisco approximately April 3 and CipherForce/Sportradar approximately April 10 to 11), which is now a robust pattern.

## Watch items

* xinference attribution resolution. Vendor analyses from JFrog, OX Security, StepSecurity, and Mend disagree on whether xinference is genuine TeamPCP, a copycat, or a deliberate false flag. The next coherent statement from Mandiant or GTIG (which formally tracks TeamPCP as UNC6780) will likely settle the question and is worth monitoring; absent that, watch for additional compromises bearing the same operator marker that TeamPCP either claims or denies, which would clarify the discipline-versus-copycat hypothesis.
* Cascading downstream impact through Dependabot or similar automation. The Bitwarden CLI compromise is the first documented automation-pivoted cascade in this campaign. Watch for additional disclosed cases in the coming week, particularly from organizations whose CI/CD pipelines pulled checkmarx/kics during the April 22 14:17:59 UTC to 15:41:31 UTC window. Endor Labs and StepSecurity have published detection guidance; victim disclosures are likely to materialize on a 3 to 14 day delay as organizations complete forensic review of their own April 22 build artifacts.
* CanisterSprawl ecosystem jump. Socket and StepSecurity flagged that CanisterSprawl jumps to PyPI when it discovers a PyPI publish token. Watch for the first confirmed PyPI compromise that shares CanisterSprawl indicators (ICP canister C2, postinstall execution pattern, the specific 40-category regex sweep), which would convert the cross-ecosystem capability from theoretical to demonstrated.
* CISA standalone advisory or emergency directive. CISA has not issued a dedicated TeamPCP advisory in the 35 days since adding CVE-2026-33634 to the KEV catalog. Three concurrent compromises affecting Checkmarx, Bitwarden, Xorbits xinference, and Namastex Labs in a single 48 hour window during a sitting federal civilian remediation cycle creates additional pressure for a standalone advisory. Watch for any CISA, FBI, or Five Eyes joint product responsive to W17 events.
* Vect publication or formal de-escalation. With three consecutive lapsed Vect-or-CipherForce monetization deadlines, watch for either a delayed public Guesty or S&P Global data dump or a formal Vect statement on the leak site. Continued silence into W18 increasingly favors the hypothesis that the TeamPCP-affiliated extortion arm is operationally constrained rather than tactically patient.

## Source index

### Tier 1 (major security publications)

### Tier 2 (vendor threat intelligence)

### Tier 3 (government or institutional)

* No new dedicated CISA, FBI, NCSC, ACSC, CCCS, BSI, or Singapore CSA advisories have been reported for TeamPCP-related activity during the target week based on monitoring of the listed sources. The CISA KEV entry for CVE-2026-33634 from late March remains the only US federal action and was not updated this week. CERT-EU has not issued a follow-on bulletin to the European Commission disclosure. No Five Eyes joint advisory has been identified. The supply chain attacks on April 21 to 22 were sufficiently public to generate Tier 1 coverage; the absence of a corresponding CISA standalone advisory or emergency directive is itself a continuing signal.

### Tier 4 (social and dark web signal)