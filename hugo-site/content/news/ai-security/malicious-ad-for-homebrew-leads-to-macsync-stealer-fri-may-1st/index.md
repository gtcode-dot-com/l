---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-02T04:15:15.037687+00:00'
exported_at: '2026-05-02T04:15:17.919649+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32942
structured_data:
  about: []
  author: ''
  description: 'Malicious Ad for Homebrew Leads to MacSync Stealer, Author: Brad Duncan'
  headline: Malicious Ad for Homebrew Leads to MacSync Stealer, (Fri, May 1st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32942
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious Ad for Homebrew Leads to MacSync Stealer, (Fri, May 1st)
updated_at: '2026-05-02T04:15:15.037687+00:00'
url_hash: 96e24931717df4dc12f63bb73580ed7db9840ece
---

***Introduction***

As macbooks and mac minis become more popular, we're seeing more campaigns targeting these macOS hosts. Malicious ads have popped up in search results that can lead potential victims to pages that present themselves as legitimate malware but instead are malware. This diary presents one such example from a malicious ad for a page that impersonates Homebrew we saw on Thursday, 2026-04-30.

Homebrew is a third-party package manager for macOS, and this page pushes MacSync Stealer malware. As I write this today (2026-05-01), the fake Homebrew page at
hxxps[:]//sites.google[.]com/view/brewpage
is still active.

***Images***

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-01a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-01.png)

*Shown above: Malicious ad in search results leading to fake Homebrew page.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-02a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-02.png)

*Shown above: Information about the advertiser for the malicious ad.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-03a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-03.png)

*Shown above: Fake Homebrew page with script to copy/paste for potential victims to download malware.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-04a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-04.png)

*Shown above: Script from fake Homebrew page pasted to a terminal window on a macOS host.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-05.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-05.png)

*Shown above: After running the script, this popup appears, and it collects the victim's password.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-06.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-06.png)

*Shown above: After running the entering the password, this popup appears for the Terminal app to access the Finder app in macOS.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-07.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-07.png)

*Shown above: This is the final popup that appears after running the script.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-08a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-08.png)

*Shown above: During the infection, MacSync Stealer collects information from the host, temporarily saves it to
/tmp/osalogging.zip
and sends that file to the C2 server.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-09a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-09.png)

*Shown above: Traffic from the infection filtered in Wireshark.*

[![](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-10a.png)](https://isc.sans.edu/diaryimages/images/2026-04-30-image-MacSync-Stealer-image-10.png)

*Shown above: Traffic from the infected host sending the
/tmp/osalogging.zip
file to the C2 server.*

***Indicators of Compromise***

Example of URL from malicious ad:

hxxps[:]//www.google[.]com/aclk?sa=L&

ai=DChsSEwi24vK\_v5aUAxXZS38AHRAFIWAYACICCAIQABoCb2E&

co=1&

gclid=EAIaIQobChMItuLyv7-WlAMV2Ut\_AB0QBSFgEAMYASAAEgKrq\_D\_BwE&

cid=CAASugHkaEZtQvhFJBWvSVo\_oMtlq6lKBxptjJBacaXOdzM28vxFNm3V2vrefacF48NMD0YvBIV9PCmn\_d6X0uiMYDt5bwJYXaT6Lt7Mf3F-Mc3OK-0ugNt4GfcvQ0lOKkP1Sf8WVDXTMPeVMsHE8qxoG43Ta5BRER\_Sre0RfChP39oVqtwRkowlKUUojM12uBAYWvejqokVOa\_j7-uGyN1XrQ1ae6Tfaijfc9OvMC9QKQovm7p0DBitWtBJ\_d4&

cce=1&

sig=AOD64\_2EqeARnVjOoYvCwtJyl1AsolQe7g&q&


adurl&

ved=2ahUKEwjyq-2\_v5aUAxU3g2oFHc28JOUQ0Qx6BAhnEAE

Example of fake Homebrew site URL:

hxxps[:]//sites.google[.]com/view/brewpage?gad\_source=1&

gad\_campaignid=23806351087&

gbraid=0AAAAACJ6-Kb3hWjjAWCyYLIj0YO5oQvtp&

gclid=EAIaIQobChMItuLyv7-WlAMV2Ut\_AB0QBSFgEAMYASAAEgKrq\_D\_BwE

Domain used by C2 server for the MacSync infection:

glowmedaesthetics[.]com

Files from the infection:

SHA256 hash:
[a4fcfecc5ac8fa57614b23928a0e9b7aa4f4a3b2b3a8c1772487b46277125571](https://www.virustotal.com/gui/file/a4fcfecc5ac8fa57614b23928a0e9b7aa4f4a3b2b3a8c1772487b46277125571)

* File size: 225 bytes
* File type: ASCII text, with no line terminators
* File description: Copy/paste script from the fake Homebrew page.

SHA256 hash:
[0d58616c750fc8530a7e90eee18398ddedd08cc0f4908c863ab650673b9819dd](https://www.virustotal.com/gui/file/0d58616c750fc8530a7e90eee18398ddedd08cc0f4908c863ab650673b9819dd)

* File size: 1,448 bytes
* File type: Paul Falstad's zsh script text executable, ASCII text
* File location:
  hxxp[:]//glowmedaesthetics[.]com/curl/63810ee8b478575f3b2c6c46160c1fd338b213c6fc11bb0069dac9bbb7db237d
* File description: Initial download from the copy/paste script

SHA256 hash:
[86d0c50cab4f394c58976c44d6d7b67a7dfbbb813fbcf622236e183d94fd944f](https://www.virustotal.com/gui/file/86d0c50cab4f394c58976c44d6d7b67a7dfbbb813fbcf622236e183d94fd944f)

* File size: 2,647 bytes
* File type: Paul Falstad's zsh script text executable, ASCII text
* File description: Shell script extracted from base64 text in the initial download

---

Bradley Duncan

brad [at] malware-traffic-analysis.net