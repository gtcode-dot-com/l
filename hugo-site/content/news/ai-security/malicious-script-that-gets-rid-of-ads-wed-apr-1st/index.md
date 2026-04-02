---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T10:15:15.203866+00:00'
exported_at: '2026-04-02T10:15:18.524602+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32854
structured_data:
  about: []
  author: ''
  description: 'Malicious Script That Gets Rid of ADS, Author: Xavier Mertens'
  headline: Malicious Script That Gets Rid of ADS, (Wed, Apr 1st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32854
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious Script That Gets Rid of ADS, (Wed, Apr 1st)
updated_at: '2026-04-02T10:15:15.203866+00:00'
url_hash: 5e84f7219f448f02257030ae231d638338093d89
---

Today, most malware are called “fileless” because they try to reduce their footprint on the infected computer filesystem to the bare minimum. But they need to write something… think about persistence. They can use the registry as an alternative storage location.

But some scripts still rely on files that are executed at boot time. For example, via a “Run” key:

```
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v csgh4Pbzclmp /t REG_SZ /d "\"%APPDATA%\Microsoft\Windows\Templates\dwm.cmd\"" /f >nul 2>&1
```

The file located in %APPDATA% will be executed at boot time.

From the attacker’s point of view, there is a problem: The original script copies itself:

```
copy /Y "%~f0" "%APPDATA%\Microsoft\Windows\Templates\dwm.cmd" >nul 2>&1
```

Just after the copy operation, a PowerShell one-liner is executed:

```
powershell -w h -c "try{Remove-Item -Path '%APPDATA%\Microsoft\Windows\Templates\dwm.cmd:Zone.Identifier' -Force -ErrorAction SilentlyContinue}catch{}" >nul 2>&1
```

PowerShell will try to remove the alternate-data-stream (ADS) “:Zone.Identifier” that Windows adds during file operations. The :Zone.Identifier indicates the source of the file (0 = My Computer, 1 = Local intranet, 2 = Trusted sites, 3 = Internet, 4 = Restricted sites). It's not clear if a "copy" will drop or conserver the ADS. I did not find an official Microsoft documentation but, if you ask to a LLM, it will tell you that they are not preserved. They are wrong!

In my Windows 10 lab, I downloaded a copy of BinaryNinja. An ADS was added to the file. After a copy to "test.ext", the new file has still the ADS!

![](https://isc.sans.edu/diaryimages/images/isc-20260401-1.png)
By removing the ADS, the malicious script makes the file look less suspicious if the system is scanned to search for "downloaded" files (a classic operation performed in DFIR investigations).

For the story, the script will later invoke another PowerShell that will drop a DonutLoader on the victim's computer.

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)