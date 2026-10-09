---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-08T21:48:36.161775+00:00'
exported_at: '2026-01-08T21:48:39.701003+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32606
structured_data:
  about: []
  author: ''
  description: 'A phishing campaign with QR codes rendered using an HTML table, Author:
    Jan Kopriva'
  headline: A phishing campaign with QR codes rendered using an HTML table, (Wed,
    Jan 7th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32606
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: A phishing campaign with QR codes rendered using an HTML table, (Wed, Jan 7th)
updated_at: '2026-01-08T21:48:36.161775+00:00'
url_hash: 32232599aded7bbb49081d22f4d589ce4ddb06d3
---

Malicious use of QR codes has long been ubiquitous, both in the real world as well as in electronic communication. This is hardly surprising given that a scan of a QR code can lead one to a phishing page as easily as clicking a link in an e-mail.

No more surprising is that vendors of security technologies have, over time, developed mechanisms for detecting and analyzing images containing QR codes that are included in e-mail messages[
[1](https://www.proofpoint.com/us/blog/email-and-cloud-threats/malicious-qr-code-detection-takes-giant-leap-forward)
,
[2](https://www.cloudflare.com/learning/security/what-is-quishing/)
]. These security mechanisms make QR code-based phishing less viable. However, due to the “cat and mouse” nature of cybersecurity, threat actors continually search for ways of bypassing various security controls, and one technique that can be effective in bypassing QR code detection and analysis in e-mail messages was demonstrated quite well in a recent string of phishing messages which made it into our inbox.

The technique in question is based on the use of imageless QR codes rendered with the help of an HTML table. While it is not new by any stretch[
[3](https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20villages/DEF%20CON%2032%20-%20Adversary%20Vilage%20-%20Melvin%20Langvik%20-%20Evading%20Modern%20Defenses%20When%20Phishing%20with%20Pixels.pdf)
], it is not too well-known, and I therefore consider it worthy of at least this short post.

Samples of the aforementioned phishing messages I have access to have been sent out between December 22nd and December 26th, and all of them had the same basic layout consisting of only a few lines of text along with the QR code.

[![](https://isc.sans.edu/diaryimages/images/26-01-07-message.png)](https://isc.sans.edu/diaryimages/images/26-01-07-message.png)

Although it looks quite normal (except perhaps for being a little “squished”), the QR code itself was – as we have indicated above – displayed not using an image but rather with the help of an HTML table made up of cells with black and white background colors, as you can see from the following code.

```
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="180" height="180" align="center">
	<tr height="4">
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		...
```

Links encoded in all QR codes pointed to subdomains of the domain lidoustoo[.]click, and except for the very first sample from December 22nd, which pointed to onedrive[.]lidoustoo[.]click, all the URLs had the following structure:

```
hxxps[:]//<domain from recipient e-mail><decimal or hexadecimal string>[.]lidoustoo[.]click/<alphanumeric string>/$<recipient e-mail>
```

While the underlying technique of rendering QR codes using HTML tables is – as we’ve mentioned – not new, its appearance in a real-world phishing campaign is a useful reminder that many defensive controls still implicitly rely on assumptions about how malicious content is represented… And these assumptions might not always be correct.

It is also a good reminder that purely technical security controls can never stop all potentially malicious content – especially content that has a socio-technical dimension – and that even in 2026, we will have to continue improving not just the technical side of security, but also user awareness of current threat landscape.

[1]
<https://www.proofpoint.com/us/blog/email-and-cloud-threats/malicious-qr-code-detection-takes-giant-leap-forward>

[2]
<https://www.cloudflare.com/learning/security/what-is-quishing/>

[3]
<https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20villages/DEF%20CON%2032%20-%20Adversary%20Vilage%20-%20Melvin%20Langvik%20-%20Evading%20Modern%20Defenses%20When%20Phishing%20with%20Pixels.pdf>

-----------

Jan Kopriva

[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)

[Nettles Consulting](https://www.nettles.cz/)