---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T02:33:28.517692+00:00'
exported_at: '2026-10-07T02:33:32.161101+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33388
structured_data:
  about: []
  author: ''
  description: 'ScreenConnect Client (Ab)used by Attackers, Author: Xavier Mertens'
  headline: ScreenConnect Client (Ab)used by Attackers, (Thu, Oct 1st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33388
  publisher:
    logo: /favicon.ico
    name: GTCode
title: ScreenConnect Client (Ab)used by Attackers, (Thu, Oct 1st)
updated_at: '2026-10-07T02:33:28.517692+00:00'
url_hash: 66ce984e8054fd0de08c6d2d84cb1dbbae050d67
---

Threat Actors do not always use top-notch techniques or very complex malware to perform their attacks. Sometimes, they just abuse of existing applications...

I received a very simple phishing email:

```
From: contact@mejuri[.]com
To: &lt;redacted&gt;
Subject: EFT Wire Transfer

Paid Invoice Receipt

Dear Customer,
Payment of $5745.65 was Received.
Please click here to view your Order Information in PDF
If this charge wasn't authorized by you, contact our customer service to cancel and
receive an immediate refund.

Digitally Yours,
Customer Support: +1(332)638474823
```

“Click here” is a link pointing to:

```
hxxps://thelittlecupandsaucer[.]com[.]au/ScreenConnect.ClientSetup.exe
```

This email passed all the basic security controls. The link points to a real PE file. Today this attack vector will be blocked by browsers because downloaded an executable is suspicious!

The PE file was unknown on VT so I did a quick analysis of it. It’s a legit application: a ScreenConnect[
[1](https://www.screenconnect.com)
] client preconfigured to call-back a test account operated by the Attacker. Here is the configuration extracted from the PE file:

![](https://isc.sans.edu/diaryimages/images/isc-20261001.png)

|  |  |
| --- | --- |
| **Parameter** | **Value** |
| Relay (h) | instance-v2e3e2-relay.screenconnect.com |
| Port (p) | 443 |
| Instance ID | v2e3e2 (ConnectWise-hosted cloud) |
| Instance key (k) | RSA-2048 public key, blob SHA256 16b1cec1…9b00ead7 |

The PE is signed by ConnectWise, LLC (DigiCert G4 Code Signing CA1). The Authenticode digest matches the signed digest exactly. There's no overlay and nothing appended to or injected into the certificate table, so the signed-but-tampered config trick isn't used here.

Such tools are a gold mine for attackers because they are easy to deploy and trusted by most used! The list of “RMM” (Remote Monitoring and Management) tools is huge. Here is a brief list of the well-known ones;

* ScreenConnect
* AnyDesk
* TeamViewer
* LogMeIn
* Bomgar (BeyondTrust Remote Support)
* Zoho Assist
* Remote utilities like rutserv.exe
* NetSupport Manager
* SimpleHelp

If you want a better overview, check LOLRMM project [
[2](https://lolrmm.io)
] that maintains a list similar to the LOLBAS project!

[1]
[https://www.screenconnect.com](https://www.screenconnect.com/)

[2]
[https://lolrmm.io](https://lolrmm.io/)

Xavier Mertens (@xme)

Senior ISC Handler | SANS Principal Instructor | Freelance Consultant

[Xameco](https://xameco.be)
|
[PGP Key](https://xameco.be/pgpkey.txt)