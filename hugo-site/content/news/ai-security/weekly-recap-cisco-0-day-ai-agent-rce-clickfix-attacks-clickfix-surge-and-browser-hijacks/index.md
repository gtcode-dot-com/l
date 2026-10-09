---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T23:28:48.603030+00:00'
exported_at: '2026-10-03T23:28:50.999020+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/weekly-recap-cisco-0-day-ai-agent-rce.html
structured_data:
  about: []
  author: ''
  description: This week’s recap covers AI agent risks, supply-chain attacks, exposed
    systems, returning malware, weak defaults, and fast-moving exploit paths.
  headline: '⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix
    Surge, and Browser Hijacks'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/weekly-recap-cisco-0-day-ai-agent-rce.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix Surge,
  and Browser Hijacks'
updated_at: '2026-10-03T23:28:48.603030+00:00'
url_hash: 5997c3e8371dff869745fdf86aca3a23d0b9d5f0
---

A browser. A plugin. A package. A login screen. Normal stuff. That is basically the problem this week.

The trouble keeps showing up inside things people already trust: code that takes a bad turn, old payloads coming back, exposed systems, weak checks, fake fixes, and attack paths that look almost too easy. Even the research side is getting messy, with more findings, more automation, and not always more clarity.

Nothing here needs much drama. Just a lot of small doors left open. Here’s what happened.

## **⚡ Threat of the Week**

**[Cisco Warns of Actively Exploited ISE Auth Bypass](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)**
— Cisco warned of a fresh maximum-severity security flaw impacting Identity Services Engine (ISE) that has come under active exploitation. The vulnerability, tracked as CVE-2026-76460 (CVSS score: 10.0), could allow an unauthenticated, remote attacker to bypass authentication. "This vulnerability is due to insufficient authentication control on an API endpoint," Cisco said. "An attacker could exploit this vulnerability by sending a crafted request to an affected API endpoint. A successful exploit could allow the attacker to gain unauthorized access to the affected device by bypassing the web-based management interface."

## **🔔 Top News**

* **[U.S. Seizes NightmareStresser Domains Linked to DDoS Attacks](https://thehackernews.com/2026/09/us-seizes-nightmarestresser-domains.html)**
  — A U.S. court-authorized operation seized two domains associated with NightmareStresser, which offered a distributed denial-of-service (DDoS)-for-hire service. NightmareStresser is assessed to have been used to launch hundreds of thousands of actual or attempted DDoS attacks against victims across the world since 2022. These attacks have targeted educational institutions, government agencies, gaming platforms, and millions of people, the U.S. Justice Department said.
* **[Using Claude to Hack OpenAI](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)**
  — Hacktron said it used Anthropic's Claude Opus 5 to chain two critical vulnerabilities – an SSO misconfiguration in OpenAI's identity infrastructure and a libheif RCE in the
  [Discourse community forum](https://community.openai.com/)
  (
  [CVE-2026-32882](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335)
  ) – to gain unauthorized access to OpenAI employees' ChatGPT accounts and then use them to access internal OpenAI repositories. The issue was fixed 14 hours after responsible disclosure. Upstream, the flaw was fixed in
  [libheif 1.22.0](https://github.com/strukturag/libheif/releases/tag/v1.22.0)
  in May 2026.
* **[Plugin4Shell for 0-Click RCE in AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)**
  — AIR Security demonstrated a flaw called Plugin4Shell, a zero-click remote code execution (RCE) vulnerability that bypasses SHA-pinning verification in four major AI coding agents: Claude Code, OpenAI Codex, GitHub Copilot, and Google Gemini CLI. "In this first-of-its-kind AI supply-chain attack, a trusted plugin is silently swapped for a malicious one and auto-installed past the agent's SHA pinning -- a flaw no marketplace can fix, so users must update their agent," AIR Security said. "It is a plugin SHA-pinning bypass: the agent checks out the exact commit the marketplace pinned but never verifies it landed there, so an attacker who controls the plugin's repo makes the checkout resolve to malicious code while the pin still looks honored. The result is zero-click remote code execution across Claude Code, Codex, GitHub Copilot, and Gemini CLI."
* **[OpenAI Reveals New Misalignment Incidents](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html)**
  — OpenAI disclosed six new instances of "unexpected or concerning model behavior" that took place over the past six months, while sharing a new framework for reporting, tracking, investigating, and disclosing model misalignment in a bid to improve transparency. "As AI systems grow more advanced and more widely deployed, we need to build a broader and better-informed consensus on the progress of alignment research," OpenAI said. "We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer."
* **[KREMLIN Banking Malware Hijacks Chrome and Edge for Credential Theft](https://thehackernews.com/2026/09/kremlin-banking-malware-hijacks-chrome.html)**
  — A previously undocumented Brazilian banking malware operation has been found to deliver a toolkit called KREMLIN. Active since at least May 2025, the threat actor has used lures that impersonate a dozen Brazilian banks and install a malicious browser extension on Google Chrome and Microsoft Edge. "The KREMLIN malware ecosystem employs multi-stage JavaScript loaders, custom C++ installers, and malicious browser extensions to steal credentials, session tokens, and sensitive data," Elastic said. The activity is being tracked as REF9334.

## **‎️‍🔥 Trending CVEs**

Bugs drop weekly, and the gap between a patch and an exploit is shrinking fast. These are the heavy hitters for the week: high-severity, widely used, or already being poked at in the wild.

Check the list, patch what you have, and hit the ones marked urgent first —
[CVE-2026-58138](https://nvd.nist.gov/vuln/detail/cve-2026-58138)
(Orkes Conductor),
[CVE-2026-58704](https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01)
(Google Pixel),
[CVE-2026-90894](https://jfrog.com/blog/parallels-desktop-turns-appliance-install-into-root-shell/)
aka ParaShells (Parallels Desktop),
[CVE-2026-82079](https://www.nintendo.com/security-advisories/assets/pdf/20260910e.pdf)
(Nintendo Switch),
[CVE-2026-89049](https://github.com/aws/amazon-ssm-agent/security/advisories/GHSA-w9jw-h72g-6hxc)
(AWS Systems Manager Agent),
[CVE-2026-43502](https://www.openwall.com/lists/oss-security/2026/09/08/1)
aka ZcopyReaper,
[CVE-2026-80844](https://heyitsas.im/posts/lpe-quartet/)
aka DirtyAH6,
[CVE-2026-81000](https://heyitsas.im/posts/lpe-quartet/)
aka TUNderflow,
[CVE-2026-68121](https://heyitsas.im/posts/lpe-quartet/)
aka PPPoEject,
[CVE-2026-74469](https://heyitsas.im/posts/lpe-quartet/)
aka DiagSpill (Linux kernel),
[CVE-2026-70416, CVE-2025-43936](https://www.dell.com/support/kbdoc/en-in/000505935/dsa-2026-393-security-update-for-dell-objectscale-multiple-vulnerabilities)
(Dell ObjectScale and Elastic Cloud Storage),
[CVE-2026-68488](https://support.plesk.com/hc/en-us/articles/43248932867351-Vulnerability-in-Plesk-s-Backup-Manager-symlink-race-during-restore-allows-root-privilege-escalation)
(Please Backup Manager),
[CVE-2026-56711, CVE-2026-73324](https://www.vulncheck.com/advisories/vlc-media-player-3.0.0-through-3.0.23-heap-out-of-bounds-read-via-unterminated-realrtsp-response-line)
(VLC Media Player),
[CVE-2026-65638](https://support.cpanel.net/hc/en-us/articles/43387915588375-Security-CVE-2026-65638-CSF-Security-Release)
(cPanel ConfigServer Security &amp; Firewall),
[CVE-2026-85982](https://trust.okta.com/security-advisories/stored-cross-site-scripting-xss-in-auth0-ad-ldap-connector-cve-2026-85982/)
,
[CVE-2026-78626](https://trust.okta.com/security-advisories/improper-input-sanitization-in-okta-access-gateway-protected-rules-cve-2026-78626/)
,
[CVE-2026-78623](https://trust.okta.com/security-advisories/improper-handling-of-saml-assertion-attributes-in-okta-access-gateway-advanced-mode-datastores-cve-2026-78623/)
(Okta),
[CVE-2026-0310](https://security.paloaltonetworks.com/CVE-2026-0310)
(Palo Alto Networks PAN-OS),
[CVE-2026-85061](https://github.com/maplibre/maplibre-gl-js/security/advisories/GHSA-jrc7-96c5-q579)
(MapLibre GL JS),
[GHSA-rvhw-4hpw-9vrx](https://github.com/arangodb/arangodb/security/advisories/GHSA-rvhw-4hpw-9vrx)
,
[GHSA-rrgq-978q-36mq](https://github.com/arangodb/arangodb/security/advisories/GHSA-rrgq-978q-36mq)
,
[GHSA-4xhx-8cv5-wh62](https://github.com/arangodb/arangodb/security/advisories/GHSA-4xhx-8cv5-wh62)
,
[GHSA-8v35-895w-232p](https://github.com/arangodb/arangodb/security/advisories/GHSA-8v35-895w-232p)
(ArangoDB),
[CVE-2026-65812](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65812)
(Microsoft Teams for Android),
[CVE-2026-80172, CVE-2026-61410, CVE-2026-80238](https://www.dell.com/support/kbdoc/en-in/000503426/dsa-2026-382-security-update-for-dell-secure-connect-gateway-virtual-edition-multiple-vulnerabilities)
(Dell Secure Connect),
[CVE-2026-18851](https://forums.ivanti.com/s/article/Security-Advisory---Ivanti-Endpoint-Manager-Mobile-CVE-2026-18851)
(Ivanti Endpoint Manager Mobile),
[CVE-2026-91721, CVE-2026-91749, CVE-2026-91726](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0541751186.html)
,
[CVE-2026-93374, CVE-2026-93372](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0194356994.html)
(Google Chrome),
[CVE-2026-92033, from CVE-2026-92005 to CVE-2026-92013, from CVE-2026-92015 to CVE-2026-92020, from CVE-2026-92022 to CVE-2026-92029, from CVE-2026-92034 to CVE-2026-92038](https://www.mozilla.org/en-US/security/advisories/mfsa2026-90/)
(Mozilla Firefox),
[CVE-2026-15315, CVE-2026-15316](https://www.opswat.com/blog/authentication-bypass-and-dos-vulnerabilities-opswat-discovers-cve-2026-15315-cve-2026-15316-in-tp-link-tapo-cameras)
(TP-Link Tapo cameras),
[CVE-2026-82232](https://lists.apache.org/thread/v5zrdqcn0w0v4pk1d22ndt7frcrplo2b)
,
[CVE-2026-77147](https://lists.apache.org/thread/qr464o2lyj3rxp8b0q25ssn0qwjxyrgz)
,
[CVE-2026-73178](https://lists.apache.org/thread/owcdm0stb39mnkpyps0h6yw4gp2olnkj)
(Apache Syncope),
[CVE-2026-76669, CVE-2026-76670, CVE-2026-76672, CVE-2026-76673, CVE-2026-76674](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05135en_us&amp;docLocale=en_US)
(HPE Networking EdgeConnect SD-WAN Gateways and SD-WAN Orchestrator),
[CVE-2026-73693, CVE-2026-73694, CVE-2026-73698, CVE-2026-73699](https://www.vulncheck.com/blog/filerun-delegated-admin-sql-to-object-injection-rce)
(FileRun),
[CVE-2026-39919](https://www.vulncheck.com/advisories/ghostscript-heap-buffer-overflow-via-jpeg-2000-output-adapter)
(Ghostscript),
[CVE-2026-91998](https://www.vulncheck.com/advisories/casdoor-through-4.4.0-cross-organization-user-administration-via-api-mcp)
(Casdoor),
[CVE-2026-91932](https://www.vulncheck.com/advisories/flowise-before-3.1.4-remote-code-execution-via-cwd-parameter)
,
[CVE-2026-91931](https://www.vulncheck.com/advisories/flowise-before-3.1.4-remote-code-execution-via-custom-mcp-npx)
(Flowise),
[CVE-2026-65400, CVE-2026-65414, CVE-2026-65346, CVE-2026-84607, CVE-2026-43790](https://www.thezdi.com/blog/2026/9/16/the-apple-security-update-review-for-september-2026)
(Apple),
[CVE-2026-90999](https://kb.cert.org/vuls/id/212479)
(Sentry Seer),
[CVE-2026-77692, CVE-2026-76163, CVE-2026-19667, CVE-2026-19666, CVE-2026-80274](https://kb.isc.org/docs/aa-00913)
(ISC BIND 9),
[CVE-2026-91843](https://support.checkpoint.com/results/sk/sk1000155)
(Check Point),
[CVE-2026-77179](https://docs.docker.com/security/security-announcements/#docker-sandboxes-0420-security-update-cve-2026-77179-and-cve-2026-79994)
(Docker),
[CVE-2026-81642, CVE-2026-82717](https://nlnetlabs.nl/projects/unbound/security-advisories/)
(Unbound DNS),
[Click2Shell](https://pwn.ai/blog/click2shell)
(WordPress),
[CVE-2026-28326, CVE-2026-28323, CVE-2026-28309, CVE-2026-28306, CVE-2026-28308, CVE-2026-28310, CVE-2026-28314, CVE-2026-28313, CVE-2026-28307, CVE-2026-28305, CVE-2026-28317, CVE-2026-28304, CVE-2026-28312, CVE-2026-28316, CVE-2026-28311, CVE-2026-28302, CVE-2026-28321, CVE-2026-28315](https://www.solarwinds.com/trust-center/security-advisories)
(SolarWinds),
[CVE-2026-89026](https://www.cve.org/CVERecord?id=CVE-2026-89026)
(Issabel Framework),
[CVE-2026-78175](https://www.wordfence.com/blog/2026/09/100000-wordpress-sites-exposed-to-remote-code-execution-via-php-object-injection-vulnerability-found-by-wordfence-argus-in-tutor-lms/)
(Tutor LMS), an
[operating system command injection vulnerability](https://kb.cert.org/vuls/id/280377)
in Dokploy, and a
[pickle deserialization vulnerability](https://kb.cert.org/vuls/id/369093)
in MLflow.

## **🎥 Cybersecurity Webinars**

* [How to Find and Control AI Agents Before Access Gets Out of Hand](https://thehacker.news/ai-agents-governance)
  → AI agents are getting access to apps, data, credentials, and workflows faster than most teams can govern them. The real problem is not adoption — it is knowing which agents exist, what they can reach, and where access has quietly become too broad. This webinar breaks down how to bring AI agents under control without slowing down the teams using them.
* [AI Attacks Move in Minutes. Here's How to Stop Them at Runtime](https://thehacker.news/runtime-identity-security)
  → AI-powered attacks are shrinking the time defenders have to react. By the time a traditional alert is investigated, the attacker may already have moved through the environment. This webinar shows how runtime identity security can make access decisions in real time, block risky activity earlier, and give security teams a better chance against machine-speed attacks.

## **📰 Around the Cyber World**

* **Google Doc Leads to ClickFix Attack**
  — Huntress disclosed details of a
  [ClickFix attack](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
  in which a security researcher was
  [targeted](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)
  in an X exchange by a threat actor posing as a crypto marketing executive. "The threat actor sent a link to a real Google Doc with a custom sidebar designed to trick the recipient into downloading malware: an AMOS infostealer on macOS, or a PowerShell loader chain on Windows," Huntress
  [said](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)
  . "The Google Doc featured a sidebar displaying a fake decryption failure message, with supposed remediation instructions for users of different operating systems, including the option to copy and paste certain commands into the Terminal. This ClickFix lure, and the "manual update" button beside it, are what actually delivered the malware. The sidebar itself was a Google Apps Script bound to the document, so nothing had to be downloaded for it to run." The Apps Script executed client-side in the victim's browser, and collected the victim's public IP address and geolocation and scanned for crypto wallets.
* **Brevo Supply Chain Attack Injects ClickFix Scripts on Customer Sites**
  — Customer engagement platform Brevo
  [fell victim to a supply chain attack](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)
  that led to malicious code being injected into over 100,000 websites. "On 14 September 2026, an attacker used a compromised Brevo Cloudflare API key to deploy a Cloudflare Worker on our account," Brevo said. "For about five and a half hours, the Worker injected a malicious script into pages of brevo.com and sibforms.com and into three JavaScript files that customers embed on their own websites." The script showed selected visitors a fake Cloudflare CAPTCHA prompt that instructed visitors to paste and run a malicious command on their computer, a technique also called ClickFix. Sansec, which
  [shared additional details](https://sansec.io/research/brevo-supply-chain-attack)
  of the attack, said the "attackers piggy-backed on embedded Brevo widgets to install WordPress malware on Brevo customer sites and launch ClickFix attacks against their visitors." In all, the incident served malware to visitors of Brevo's own site and over 100,000 customer sites. The malware featured two components: a malicious WordPress plugin that was installed when site admins visited their own site and a ClickFix overlay that was displayed to everyone browsing a customer site or clicking a link (including the unsubscribe link) in a Brevo-sent campaign email. Earlier this month, Brevo disclosed a
  [separate incident](https://status.brevo.com/incidents/01M266V1CZKJQNGZRNEGFD5CQE/write-up)
  wherein attackers hijacked customer accounts and launched phishing attacks targeting downstream users of Brevo's customers. The attacker "exploited a flaw in the way Brevo handles SAML SSO to gain access to 138 Brevo accounts," Brevo said. "6 of those accounts were used to send phishing emails to the contacts stored there, and for 43 accounts they exported the contacts." Among those impacted were
  [Trezor](https://x.com/trezor/status/2097786518110609620)
  ,
  [CoinTracking](https://x.com/Coin_Tracking/status/2097800407103783325)
  , and
  [BitBox](https://x.com/bitboxswiss/status/2097793026336981079)
  .
* **Cryptocurrency Theft Campaign Abuses Google Visualization API for C2**
  — A new cryptocurrency-stealing campaign has been observed using Google Visualization API for command-and-control (C2), while fetching obfuscated JavaScript from a publicly published Google Sheets document and injecting it into the victim's browser session. "The actors use a variation on ClickFix social engineering," Cisco Talos
  [said](https://blog.talosintelligence.com/clickfix-moves-into-the-browser/)
  . "Instead of convincing targets to run commands against the operating system, they convince targets to paste JavaScript into the Chrome address bar or install it into the
  [Tampermonkey browser extension](https://www.tampermonkey.net/)
  , which also provides persistence." The lure masquerades as leaked vulnerability reports describing non-existent API flaws at cryptocurrency swap services, meaning the campaign is aimed at aspiring cybercriminals who are willing to exploit such vulnerabilities for financial gain. The lures are distributed via Telegram, DarkForums, and paste sites. "The injected script functions as a web skimmer," Talos added. "It hooks the browser's fetch API, replaces cryptocurrency deposit addresses in server responses and the user's clipboard, and displays counterfeit 'bonus' interface elements." The campaign is said to have been
  [ongoing since October 2025](https://bolster.ai/blog/swapzone-profit-trick-web-inject-from-lure-to-live-dom-hijack)
  . A total of 49 BTC wallet addresses have been tied to the campaign, with 24 receiving funds amounting to $10,000 from victims as of early August 2026.
* **Shai-Hulud Resurfaces After 111 Days**
  — Aikido Security said it discovered four npm packages – feishu-docx-mcp@0.3.2, bmc-i18n-extract-cli@1.1.1, blueai-cli@0.7.0, and bmc-translate-utils@1.1.1 – containing the Shai-Hulud worm previously discovered in the
  [attack targeting AntV in May 2026](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)
  . "Four packages is a small number attached to a larger fact: a payload with a known, published, indexed hash sat untouched in nobody's toolchain for over three months and was then republished on a registry that, as of this year, explicitly scans every package before it goes live," Aikido
  [said](https://www.aikido.dev/blog/shai-hulud-npm-resurfaces)
  . "That gap between what registry-level scanning claims to do and what a hash-identical reactivation shows it actually caught is the real story here."
* **Google Debuts AndroidX Security State Libraries**
  — Google announced the stable release of AndroidX Security State version 1.1.0 and Security State Provider version 1.0.0 libraries to bring more transparency into the security posture of an Android device. These libraries provide a "centralized mechanism designed to bring further transparency to the comprehensive security posture and pending updates across the Android ecosystem," Google
  [said](https://android-developers.googleblog.com/2026/09/introducing-androidx-security-state-libraries.html)
  . "Whether you develop security-critical, consumer-facing apps (such as banking, fintech, or healthcare) or Mobile Device Management (MDM) solutions, these libraries enable you to verify the security state of the device per component programmatically. Rather than relying on a coarse, monolithic Security Patch Level (SPL), you can evaluate true component-level protection and whether remediations are actively pending via the androidx.security.state library. For OEMs and Over-The-Air (OTA) client developers, the companion androidx.security.state.provider library allows you to expose update availability via standardized mechanisms."

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBZLC_J3TKElcDQDQ_QNaKd_wp-z6UC50CpSunWOSDGZpeAk4xCMFAp3b_VLrh_nhhNicaP5GFTZx-6hscMi4VexDwlo_nFM4WM90tnI11fBAWiRx3ldDvt4LPlueSy7PDTEO0cBSwZE1dwZyvwgD1D5Y_5JfBG7bHEg1zYXaTZanBi-aOzxgC03hpbCGD/s1600/androidz.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBZLC_J3TKElcDQDQ_QNaKd_wp-z6UC50CpSunWOSDGZpeAk4xCMFAp3b_VLrh_nhhNicaP5GFTZx-6hscMi4VexDwlo_nFM4WM90tnI11fBAWiRx3ldDvt4LPlueSy7PDTEO0cBSwZE1dwZyvwgD1D5Y_5JfBG7bHEg1zYXaTZanBi-aOzxgC03hpbCGD/s1600/androidz.png)

* **Ukrainian Hacker Jailed in Switzerland for Ransomware Attacks**
  — A Zurich court
  [sentenced](https://www.swissinfo.ch/eng/swiss-politics/ukrainian-hacker-jailed-in-switzerland-over-ransomware-attacks/92040952)
  a Ukrainian IT specialist to 12 years and nine months in prison for developing ransomware used in extortion attacks on companies, including Stadler Rail.  The court identified the defendant as the lead developer behind the Lockergoga, MegaCortex, and Nefilim ransomware families, although he claimed that he only worked as a consultant for an unknown client in the field of IT security and that he had been unaware that his software was being used for ransomware attacks. The activity led to $123 million in estimated losses.
* **Surfshark Discloses Security Incident**
  — Surfshark disclosed that unknown threat actors accessed one of its internal test servers after a configuration error exposed it to the internet. "Due to a human error, an internal test server used by our engineering teams was misconfigured in a way that made it reachable from the internet," Surfshark
  [said](https://surfshark.com/blog/security-update-september-2026-incident-report)
  . "It contained parts of the system binaries and internal configurations for certain services. Personal information was never held and accessible from here, VPN traffic and browsing activity are not logged or retained in the first place, and the apps and browser extensions on your devices were not altered in any way." The incident was discovered on August 31, 2026.
* **New Panzer Ransomware Emerges**
  — A ransomware group called
  [Panzer](https://www.ransomware.live/group/Panzer)
  , which emerged in early August 2026, has already claimed 32 victims on its data leak site. The group mainly targeted technology, manufacturing, government, and education sectors in Germany, Indonesia, France, Spain, and Italy. According to
  [CyberXTron](https://cyberxtron.com/resources/blogs/panzer-ransomware-profile-of-an-emerging-double-extortion-operator-8102)
  , "Panzer operates on an 80/20 revenue split, with 80% of ransom proceeds going to the affiliate and 20% retained as a platform fee. The group supports cross-platform builds for Windows, Linux, ESXi, and FreeBSD. Its stated rules prohibit targeting CIS countries and entities involving minors under 18."

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjmJELgIMU4WxjTOB-GdbSJQOffPBog8zO8_6OnSM52UeIusTJ_g7kBTZ9GuiaB1JCClR1lo9AooATvBQd18NkDFfYnkJpPZaQxUmw79WpOyEnviLkDpD1oHzj2z229xRWpH70GNQC5kHbS0PeY8gdC_I-I4rK1baU8m8U4sTwI2TFl868IleYM84rsljr/s1600/panzer.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjmJELgIMU4WxjTOB-GdbSJQOffPBog8zO8_6OnSM52UeIusTJ_g7kBTZ9GuiaB1JCClR1lo9AooATvBQd18NkDFfYnkJpPZaQxUmw79WpOyEnviLkDpD1oHzj2z229xRWpH70GNQC5kHbS0PeY8gdC_I-I4rK1baU8m8U4sTwI2TFl868IleYM84rsljr/s1600/panzer.png)

* **Review of Anthropic's Project Glasswing Ledger**
  — VulnCheck's review of Anthropic's Project Glasswing ledger found that only 202 of 26,153 claimed findings have been addressed after nearly five months, while 245 have been withdrawn and 2 have been marked as duplicates. "Five months into the project, the 202 fixed findings in the ledger span 113 unique projects, resulting in an average of just 1.79 fixed findings per project," VulnCheck's Patrick Garrity
  [said](https://www.vulncheck.com/blog/anthropic-glasswing-receipts)
  . "The ledger has more withdrawn/duplicate findings than fixed vulnerabilities, which makes me question Anthropic's 91.4% true-positive claim." The analysis also showed a significant gap between Claude's severity assessments and those of maintainers: Claude rated 91.5% of findings as critical or high severity, compared with only 51.3% from maintainers.
* **Google Unveils Agent Anomaly Detection**
  — Google unveiled Agent Anomaly Detection in private preview on the Gemini Enterprise Agent Platform, which acts as a "reasoning-based oversight and audit layer" that examines what an agent actually does using its reasoning traces, tool calls, and execution flow across a session. "It reads the logs and OpenTelemetry traces your agents already emit, evaluates that activity to decide whether an agent is operating outside its intended boundaries, and flags behavioral anomalies, suspicious intent, and policy violations," Google
  [said](https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform/)
  .

## **Conclusion**

The lesson this week is pretty basic: trust less, check more. A familiar tool, package, login flow, browser prompt, or cloud setup can still be the weak spot. Old payloads can come back, exposed systems still get found, and "trusted" does not mean "safe."

The other lesson is speed. Attack paths are getting shorter, research is getting faster, and weak defaults do not stay quiet for long. Patch what matters, watch what is exposed, and do not assume the boring stuff is harmless. That is usually where the week starts.