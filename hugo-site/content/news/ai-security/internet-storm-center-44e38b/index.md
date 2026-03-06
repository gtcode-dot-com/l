---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-06T22:15:17.302613+00:00'
exported_at: '2026-03-06T22:15:19.729975+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32766
structured_data:
  about: []
  author: ''
  description: 'Want More XWorm?, Author: Xavier Mertens'
  headline: Want More XWorm&#x3f;, (Wed, Mar 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32766
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Want More XWorm&#x3f;, (Wed, Mar 4th)
updated_at: '2026-03-06T22:15:17.302613+00:00'
url_hash: 44e38bbe4128ea69a72bd888c599a4e5da7cf7fe
---

And another XWorm[
[1](https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm)
] wave in the wild! This malware family is not new and heavily spread but delivery techniques always evolve and deserve to be described to show you how threat actors can be imaginative! This time, we are facing another piece of multi-technology malware.

Here is a quick overview:

![](https://isc.sans.edu/diaryimages/images/isc-20260304-1.png)

The Javascript is a classic obfuscated one:

![](https://isc.sans.edu/diaryimages/images/isc-20260304-2.png)

No need to try to analyze it, just let it run in a sandbox and see its magic. It will drop a PowerShell script in a temporary directory (“C:\Temp\ps\_5uGUQcco8t5W\_1772542824586.ps1
*”).*
This loader will decode (Base64 + XOR) another payload that invokes another piece of PowerShell in memory:

![](https://isc.sans.edu/diaryimages/images/isc-20260304-3.png)

Because the last payload is XOR-encrypted, it is not obfuscated and easy to understand. The DLL exports a function called “ProcessHollowing” (nice name, btw) and acts as a loader. It inject the XWorm client in the .Net compiler process…

Here is the extracted config:

```
{
    "c2": [
        "204[.]10[.]160[.]190:7003"
    ],
    "attr": {
        "install_file": "USB.exe"
    },
    "keys": [
        {
            "key": "aes_key",
            "kind": "aes.plain",
            "value": "XAorWEAzx4+ic89KWd910w=="
        }
    ],
    "rule": "Xworm",
    "mutex": [
        "Cqu1F0NxohroKG5U"
    ],
    "family": "xworm",
    "version": "XWorm V6.4"
}
```

Do you recognize the C2 IP address? It's the same as the one detected in my latest diary![
[2](https://isc.sans.edu/diary/Fake%20Fedex%20Email%20Delivers%20Donuts!/32754)
]

And some IOC's:

| File | SHA256 |
| --- | --- |
| Inv-4091-CBM-4091-CUSTOM-Packing\_List.js | 5140b02a05b7e8e0c0afbb459e66de4d74f79665c1d83419235ff0cdcf046e9c |
| ps\_5uGUQcco8t5W\_1772542824586.ps1 | 5a3d33efaaff4ef7b7d473901bd1eec76dcd9cf638213c7d1d3b9029e2aa99a4 |
| MAD.dll | af3919de04454af9ed2ffa7f34e4b600b3ce24168f745dba4c372eb8bcc22a21 |
| payload.exe (XWorm) | 58e38fffb78964300522d89396f276ae0527def8495126ff036e57f0e8d3c33b |

[1]
<https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm>

[2]
<https://isc.sans.edu/diary/Fake%20Fedex%20Email%20Delivers%20Donuts!/32754>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)