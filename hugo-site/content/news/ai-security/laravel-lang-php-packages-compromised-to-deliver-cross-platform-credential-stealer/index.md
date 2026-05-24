---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-24T00:20:02.959946+00:00'
exported_at: '2026-05-24T00:20:05.129084+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
structured_data:
  about: []
  author: ''
  description: Laravel-Lang compromise tagged 700+ versions on May 22–23, 2026, triggering
    PHP stealers that exfiltrate credentials.
  headline: Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential
    Stealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential
  Stealer
updated_at: '2026-05-24T00:20:02.959946+00:00'
url_hash: a0b13b56f7a46d509ef2c25f0744d7f64d87720f
---

**

Ravie Lakshmanan
**

May 23, 2026

Supply Chain Attack / Malware

Cybersecurity researchers have flagged a fresh software supply chain attack campaign that has targeted multiple PHP packages belonging to Laravel-Lang to deliver a comprehensive credential-stealing framework.

The affected packages include -

* laravel-lang/lang
* laravel-lang/http-statuses
* laravel-lang/attributes
* laravel-lang/actions

"The timing and pattern of the newly published tags point to a broader compromise of the Laravel Lang organization's release process, rather than a single malicious package version," Socket
[said](https://socket.dev/blog/laravel-lang-compromise)
. "The tags were published in rapid succession on May 22 and May 23, 2026, with many versions appearing only seconds apart."

More than 700 versions associated with these packages have been identified, indicating automated mass tagging or republishing. It's suspected that the attacker may have managed to obtain access to organization-level credentials, repository automation, or release infrastructure.

The core malicious functionality is located in a file named "src/helpers.php" that's embedded into the version tags. It's mainly designed to fingerprint the infected host and contact an external server ("flipboxstudio[.]info") to retrieve a PHP-based cross-platform payload that runs on Windows, Linux, and macOS.

"The attacker added src/helpers.php to the autoload.files map in each compromised package," StepSecurity
[said](https://www.stepsecurity.io/blog/laravel-lang-supply-chain-attack)
. "Because every Laravel application calls require \_\_DIR\_\_.'/vendor/autoload.php' on startup, and because Symfony, PHPUnit, and most other PHP frameworks do the same, the payload runs the moment any consumer of the package boots. No class instantiation, no method call, no special trigger is required."

According to Aikido Security, the dropper delivers a Visual Basic Script launcher on Windows and runs it via cscript. On Linux and macOS, it executes the stealer payload via exec().

"Because this file ['src/helpers.php'] is registered in the composer.json under autoload.files, the backdoor is executed automatically on every PHP request handled by the compromised application," Socket explained.

"The script generates a unique per-host marker (an MD5 hash combining the directory path, system architecture, and inode) to ensure the payload only triggers once per machine. This prevents redundant executions and helps the malware remain undetected after the initial run."

The stealer is equipped to harvest a wide range of data from compromised systems and exfiltrate it to the same server. This includes -

* IAM roles and instance identity documents by querying cloud metadata endpoints
* Google Cloud application default credentials
* Microsoft Azure access tokens and service principal profiles
* Kubernetes Service Account tokens and Helm registry configurations
* Authentication tokens for DigitalOcean, Heroku, Vercel, Netlify, Railway and Fly.io
* HashiCorp Vault tokens
* Tokens and configurations from Jenkins, GitLab Runners, GitHub Actions, CircleCI, TravisCI, and ArgoCD
* Seed phrases and files associated with cryptocurrency wallets (Electrum, Exodus, Atomic, Ledger Live, Trezor, Wasabi, and Sparrow) and extensions (MetaMask, Phantom, Trust Wallet, Ronin, Keplr, Solflare, and Rabby)
* Browser history, cookies, and login data from Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, and Opera by using a Base64-encoded embedded Windows executable that bypass Chromium's app-bound encryption (
  [ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)
  ) protections
* Local vaults and browser extension data for 1Password, Bitwarden, LastPass, KeePass, Dashlane, and NordPass
* PuTTY/WinSCP saved sessions
* Windows Credential Manager dumps
* WinSCP saved sessions
* RDP files
* Session tokens associated with applications like Discord, Slack, and Telegram
* Data from Microsoft Outlook, Thunderbird, and popular FTP clients (FileZilla, WinSCP, and CoreFTP)
* Configuration and credential files containing Docker auth tokens, SSH private keys, Git credentials, shell history files, database history files, Kubernetes cluster configurations, .env files, wp-config.php, and docker-compose.yml
* Environment variables loaded into the PHP process
* Source control credentials from global and local .gitconfig files, .git-credentials, and .netrc files
* VPN configuration and saved login files for OpenVPN, WireGuard, NetworkManager, and commercial VPNs such as NordVPN, ExpressVPN, CyberGhost, and Mullvad

"The fetched payload is a ~5,900 line PHP credential stealer, organised into fifteen specialist collector modules," Aikido researcher Ilyas Makari
[said](https://www.aikido.dev/blog/supply-chain-attack-targets-laravel-lang-packages-with-credential-stealer)
. "After collecting everything it can find, it encrypts the results with AES-256 and sends them to flipboxstudio[.]info/exfil. It then deletes itself from the disk to limit forensic evidence."