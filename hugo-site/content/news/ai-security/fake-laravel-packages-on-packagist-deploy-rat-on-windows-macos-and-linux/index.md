---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-09T18:04:59.995863+00:00'
exported_at: '2026-03-09T18:05:03.227987+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/fake-laravel-packages-on-packagist.html
structured_data:
  about: []
  author: ''
  description: Malicious Packagist Laravel packages install a cross-platform RAT enabling
    remote shell access and system reconnaissance via C2 server.
  headline: Fake Laravel Packages on Packagist Deploy RAT on Windows, macOS, and Linux
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/fake-laravel-packages-on-packagist.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake Laravel Packages on Packagist Deploy RAT on Windows, macOS, and Linux
updated_at: '2026-03-09T18:04:59.995863+00:00'
url_hash: ef84ded6c7ec6f8359e65dde7372dccb9b1e3965
---

**

Ravie Lakshmanan
**

Mar 04, 2026

Threat Intelligence / Application Security

Cybersecurity researchers have
[flagged](https://socket.dev/blog/malicious-packagist-packages-disguised-as-laravel-utilities)
malicious Packagist PHP packages masquerading as Laravel utilities that act as a conduit for a cross-platform remote access trojan (RAT) that's functional on Windows, macOS, and Linux systems.

The names of the
[packages](https://packagist.org/users/nhattuanbl/)
are listed below -

* nhattuanbl/lara-helper (37 Downloads)
* nhattuanbl/simple-queue (29 Downloads)
* nhattuanbl/lara-swagger (49 Downloads)

According to Socket, the package "nhattuanbl/lara-swagger" does not directly embed malicious code, lists "nhattuanbl/lara-helper" as a
[Composer dependency](https://getcomposer.org/doc/00-intro.md)
, causing it to install the RAT. The packages are still available for download from the PHP package registry.

Both lara-helper and simple-queue have been found to contain a PHP file named "src/helper.php," which employs a number of tricks to complicate static analysis by making use of techniques like control flow obfuscation, encoding domain names, command names, and file paths, and randomized identifiers for variable and function names.

"Once loaded, the payload connects to a C2 server at helper.leuleu[.]net:2096, sends system reconnaissance data, and waits for commands -- giving the operator full remote access to the host," security researcher Kush Pandya said.

This includes sending system information and parsing commands received from the C2 server for subsequent execution on the compromised host. The communication occurs over TCP using PHP's
[stream\_socket\_client()](https://www.php.net/manual/en/function.stream-socket-client.php)
. The list of supported commands is below -

* **ping**
  , to send a heartbeat automatically every 60 seconds
* **info**
  , to send system reconnaissance data to the C2 server
* **cmd**
  , to run a shell command
* **powershell**
  , to run a PowerShell command
* **run**
  , to run a shell command in the background
* **screenshot**
  , to capture the screen using imagegrabscreen()
* **download**
  , to read a file from disk
* **upload**
  , to a file on disk and grant it read, write, and execute permissions to all users
* **stop**
  , to the socket, and exit

"For shell execution, the RAT probes disable\_functions and picks the first available method from: popen, proc\_open, exec, shell\_exec, system, passthru," Pandya said. 'This makes it resilient to common PHP hardening configurations."

While the C2 server is currently non-responsive, the RAT is configured such that it retries the connection every 15 seconds in a persistent loop, making it a security risk. Users who have installed the packages are advised to assume compromise, remove them, rotate all secrets accessible from the application environment, and audit outbound traffic to the C2 server.

Besides the aforementioned three packages, the threat actor behind the operation has published three other libraries ("nhattuanbl/lara-media," "nhattuanbl/snooze," and "nhattuanbl/syslog") that are clean, likely in an effort to build credibility and trick users into installing the malicious ones.

"Any Laravel application that installed lara-helper or simple-queue is running a persistent RAT. The threat actor has full remote shell access, can read and write arbitrary files, and receives an ongoing system profile for each connected host," Socket said.

"Because activation happens at application boot (via service provider) or class autoloads (via simple-queue), the RAT runs in the same process as the web application with the same filesystem permissions and environment variables, including database credentials, API keys, and .env contents."