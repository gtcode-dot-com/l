---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-17T02:15:15.378797+00:00'
exported_at: '2026-04-17T02:15:17.619698+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32904
structured_data:
  about: []
  author: ''
  description: 'Lumma Stealer infection with Sectop RAT (ArechClient2), Author: Brad
    Duncan'
  headline: Lumma Stealer infection with Sectop RAT (ArechClient2), (Fri, Apr 17th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32904
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Lumma Stealer infection with Sectop RAT (ArechClient2), (Fri, Apr 17th)
updated_at: '2026-04-17T02:15:15.378797+00:00'
url_hash: a97653d657351511a6e2a12bcf552f3bb467da41
---

***Introduction***

This diary provides indicators from a
[Lumma Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.lumma)
infection that was followed by
[Sectop RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.sectop_rat)
(ArechClient2). I searched for cracked versions of popular copyright-protected software, and I downloaded the initial malware after following the results of one such search. This is a common distribution technique for various families of malware, and I often find Lumma Stealer this way.

In this case, the initial malware for Lumma Stealer was delivered as a password-protected 7-zip archive. The extracted malware is an inflated Windows executable (EXE) file at 806 MB. The EXE is padded with null-bytes (0x00), a technical which increases the EXE size while allowing the compressed archive file to be much smaller. The password-protected archive and inflated EXE file are designed to avoid detection.

***Images from the infection***

[![](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-01.jpg)](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-01a.jpg)

*Shown above: Example of a page with instructions to download the initial malware file.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-02.jpg)](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-02a.jpg)

*Shown above: Traffic from the infection filtered in Wireshark.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-03.jpg)](https://isc.sans.edu/diaryimages/images/2026-04-17-ISC-diary-image-03a.jpg)

*Shown above: Sectop RAT persistent on an infected Windows host.*

***Indicators of Compromise***

Example of download link from the site advertising cracked versions of copyright-protected software:

hxxps[:]//incolorand[.]com/how-visual-patch-enhances-ui-consistency-across-releases/?utm\_source={CID}&utm\_term=Adobe%20Premiere%20Pro%20(2026)%20Full%20v26.0.2%20Espa%C3%B1ol%20[Mega]&utm\_content={SUBID1}&utm\_medium={SUBID2}

Example of URL for page with the file download instructions:

hxxps[:]//mega-nz.goldeneagletransport[.]com/Adobe\_Premiere\_Pro\_%282026%29\_Full\_v26.0.2\_Espa%C3%B1ol\_%5BMega%5D.zip?c=ABUZ4WkRgQUA\_YUCAFVTFwASAAAAAACh&s=360721

Example of URL for file download from site above site impersonating MEGA:

hxxps[:]//arch.primedatahost3[.]cfd/auth/media/JvWcFd5vUoYTrImvtWQAASTh/Adobe\_Premiere\_Pro\_(2026)\_Full\_v26.0.2\_Espa%C3%B1ol\_%5BMega%5D.zip

Downloaded file:

Extracted malware:

* SHA256 hash:
  4849f76dafbef516df91fecfc23a72afffaf77ade51f805eae5ad552bed88923
* File size: 806,127,604 bytes
* File name:
  appFile.exe
* File type: PE32 executable (GUI) Intel 80386, for MS Windows
* File description: Inflated Windows EXE file for Lumma Stealer, padded with null-bytes

Deflated malware:

Lumma Stealer command and control (C2) domains from Triage sandbox analysis:

* cankgmr[.]cyou
* carytui[.]vu
* decrnoj[.]club
* genugsq[.]best
* longmbx[.]click
* mushxhb[.]best
* pomflgf[.]vu
* strikql[.]shop
* ulmudhw[.]shop

Follow-up malware:

Example of Sectop RAT C2 traffic from an infected Windows host:

* hxxp[:]//91.92.241[.]102:9000/wmglb
* hxxp[:]//91.92.241[.]102:9000/wbinjget?q=66B553A8B94CE37C16F4EBC863D51FCC
* tcp[:]//91.92.241[.]102:443/
  - encoded or otherwise encrypted traffic (not HTTPS/TLS)

---

Bradley Duncan

brad [at] malware-traffic-analysis.net