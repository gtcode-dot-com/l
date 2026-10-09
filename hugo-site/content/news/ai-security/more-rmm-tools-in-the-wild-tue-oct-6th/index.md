---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T00:21:47.250191+00:00'
exported_at: '2026-10-08T00:21:48.425307+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33400
structured_data:
  about: []
  author: ''
  description: 'More RMM Tools In the Wild, Author: Xavier Mertens'
  headline: More RMM Tools In the Wild, (Tue, Oct 6th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33400
  publisher:
    logo: /favicon.ico
    name: GTCode
title: More RMM Tools In the Wild, (Tue, Oct 6th)
updated_at: '2026-10-08T00:21:47.250191+00:00'
url_hash: 0ec27457214b311727da2323221d940c37c21433
---

It seems that a trend started… I continue my journey discovering more RMM ("Remote Management &amp; Monitoring") tools abused by threat actors! A few days ago, I wrote a diary[
[1](https://isc.sans.edu/diary/ScreenConnect+Client+Abused+by+Attackers/33388)
] about ScreenConnect used in the wild. Today, I found another one.

Same scenario, it started with a phishing email that delivers a fake PDF invoice to the victim:

![](https://isc.sans.edu/diaryimages/images/isc-20261006-1.png)

When the PDF is opened, it just redirect to a malicious VBS file. Indeed, the PDF contains an “OpenAction” and “URI” keywords, that sounds weird!

```
remnux@remnux:~/files/samples$ pdf-parser.py Transaction\ Receipt\ .pdf -o 3
obj 3 0
Type: /Page
Referencing: 1 0 R, 2 0 R, 4 0 R

  &lt;&lt;
    /Type /Page
    /Parent 1 0 R
    /Resources 2 0 R
    /MediaBox [0 0 595.2799999999999727 841.8899999999999864]
    /Annots
      &lt;&lt;
        /Type /Annot
        /Subtype /Link
        /Rect [0. 841.8899999999999864 595.2799999999999727 71.3010032362460606]
        /Border [0 0 0]
        /A
          &lt;&lt;
            /S /URI
            /URI (hxxps://up-theta-rose.vercel[.]app/adobe_new_update.vbs)
          &gt;&gt;
      &gt;&gt;
    ] /Contents 4 0 R
  &gt;&gt;
```

The URL will be visited thanks to the OpenAction. This is a common trick to avoid writing URLs in email bodies that can be easily detected.

The VBS file is pretty simple and even not obfuscated. It will display another PDF as a decoy: a non-blurred version of the initial attachment.

In parallel, a MSI archive will be downloaded and installed:

```
hxxps://up-theta-rose.vercel[.]app/action1.msi
```

The MSI file contains 4 files that are not reported as malicious by VT:

```
$ sha256sum *
eaff35d250c9b04f51c971e70082740dbfeee5dd846829d541f588ad43378727  a1_7z_dll_file
996b01e15f85e165899630721a141b178a9c372b6e878012180ec9e9d4e7bd06  a1_sas_dll_file
1b19115d5ebdc216e0ab3adf2c643648cfc70a385f4caf0217c679f9f3b20342  action1_remote_exe
941695d20d82dd5d62f74b0111feb23720637202f6c797df2a02e2cb6cb6e8e3  main_service_exe
```

These files belongs to the RMM tool developed by Action1[
[2](https://www.action1.com/remote-access/)
] and are signed with an "Action1 Corporation" certificate that expired in May 2026.

The tool installs itself as a service for persistence ("A1Agent" - "Action1 Agent"), executing C:\Windows\Action1\action1\_agent.exe.

The registy key "HKLM\Software\Action1\Agent" contains the values: CustomerId, Certificate, PrivateKey, MSI &amp; INSTALLDIR.

The CustomerID is: 49b18106-681d-456a-b098-092e2818c09a and is connecting to the Action1 infrastructure via server[.]na-2.action1[.]com.

We are facing here the same behaviour: the threat actor abuse the cloud infrastructure of the company developing the RMM tool, probably using a free/test account.

[Update 15:11 CET]

A second sample reached my mailbox, this take mimicking a DHL document:

![](https://isc.sans.edu/diaryimages/images/isc-20261006-2.png)

The URL in the PDF is similar, it contains a URL (hxxps://update-two-tau[.]vercel[.]app/adobe-ne) pointing to a ZIP archive with an HTA script. It delivers the same MSI file.

[1]
&lt;https://isc.sans.edu/diary/ScreenConnect+Client+Abused+by+Attackers/33388&gt;

[2]
&lt;https://www.action1.com/remote-access/&gt;

Xavier Mertens (@xme)

Senior ISC Handler | SANS Principal Instructor | Freelance Consultant

[Xameco](https://xameco.be)
|
[PGP Key](https://xameco.be/pgpkey.txt)