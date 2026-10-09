---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-05T01:05:11.936403+00:00'
exported_at: '2026-03-05T01:05:15.440899+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32754
structured_data:
  about: []
  author: ''
  description: 'Fake Fedex Email Delivers Donuts!, Author: Xavier Mertens'
  headline: Fake Fedex Email Delivers Donuts&#x21;, (Fri, Feb 27th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32754
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake Fedex Email Delivers Donuts&#x21;, (Fri, Feb 27th)
updated_at: '2026-03-05T01:05:11.936403+00:00'
url_hash: 78b911663d27d7ae47de424061da3685dc53cfc3
---

It’s Friday, let’s have a look at another simple piece of malware to close a busy week! I received a Fedex notification about a delivery. Usually, such emails are simple phishing attacks that redirect you to a fake login page to collect your credentials. Here, it was a bit different:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-1.png)

Nothing really fancy but it is effective and uses interesting techniques. The attached archive called "fedex\_shipping\_document.7z" (SHA256: a02d54db4ecd6a02f886b522ee78221406aa9a50b92d30b06efb86b9a15781f5 ) contains a Windows script (.bat file) with the same filename. This script, not really obfuscated and easy to understand, receiveds a low VT score, only 12/61!

First, il will generate some environment variables and implement persistence through a Run key:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-2.png)

The variable name "!contract" contains the path of a script copy in %APPDATA%\Rail\EXPRESSIO.cmd. The threat actor does not use the classic environment variable format “%VAR%” but “!var!”. This is expanded at execution time, meaning it reflects the current value inside loops and blocks[
[1](https://ss64.com/nt/delayedexpansion.html)
]. It’s enabled via this command

```
setlocal enableDelayedExpansion
```

Simple but nice trick to defeat simple search of "%..%"!

Then a PowerShell one-liner is invoked. The Powershell payload is located in the script (at the end) and Bas64-encoded. A nice trick is that the very first characters of the Base64 payload makes it undetectable by tools like base64dump! PowerShell extracts it through a regular expression:

Once the payload decoded, it is piped to another PowerShell:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-3.png)

The PowerShell implements different behaviors. First, it will create a Mutex on the victim’s computer:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-4.png)

Strange, it seems that some anti-debugging and anti-sandoxing are not completely implemented. By example, the scripts gets the number of CPU cores (a classic) but it’s never tested!

The script waits for the presence of an « explorer » process (which means that a user is logged in) otherwise it exists:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-5.png)

There is a long Base64-encoded variable that contains a payload that has been AES encrypted. The IV and salt are extracted and the payload decrypted. No time to loose, run the script into the Powershell debugger and dump the decrypted data in a file:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-6.png)

The decrypted data is the next stage: a shellcode. This one will be injected into the explorer process and a new thread started:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-7.png)

This behavior is typical to DonutLoader[
[2](https://medium.com/@anyrun/donutloader-malware-overview-00d9e3d79a48)
].

The shell code connects to the C2 server: 204[.]10[.]160[.]190:7003. It's a good old XWorm!

[1]
<https://ss64.com/nt/delayedexpansion.html>

[2]
<https://medium.com/@anyrun/donutloader-malware-overview-00d9e3d79a48>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)