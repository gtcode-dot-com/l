---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-21T00:36:18.265877+00:00'
exported_at: '2026-11-21T00:36:19.873549+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33526
structured_data:
  about: []
  author: ''
  description: 'A phishing page interested in MX records, Author: Jan Kopriva'
  headline: A phishing page interested in MX records, (Tue, Nov 17th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33526
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A phishing page interested in MX records, (Tue, Nov 17th)
updated_at: '2026-11-21T00:36:18.265877+00:00'
url_hash: 981ecaa72b959899215993679f3a21d55dab55e4
---

I’ve mentioned before in some of my diaries that it can be instructive to look at what appear to be “generic” phishing messages in detail from time to time, since some of them might prove not to be as generic as they initially appear. I came across a good example of this while going over phishing messages delivered to our handler inbox over the past few weeks, when a message that, at first glance, appeared to be a fairly ordinary attempt at stealing e-mail credentials turned out to lead to a page interested in collecting a little more information than just the victim's password.

As you can see, the original message was not especially noteworthy on its own, being a spin on the usual “your password will expire today” approach…

[![](https://isc.sans.edu/diaryimages/images/26-11-17-phish.png)](https://isc.sans.edu/diaryimages/images/26-11-17-phish.png)

The link pointed to an HTML page hosted on Google Cloud Storage, with the recipient's e-mail address included in the URL fragment:

hxxps[:]//storage[.]googleapis[.]com/alx2/03/1a/we.html#[recipient\_e-mail\_address]

After opening the link, the recipient would be presented with a generic login form, personalized using the domain part of their e-mail address. The page also attempted to use a screenshot of the legitimate website of the recipient's organization as its background, which it retrieved using the thum.io service. This didn't work quite as intended for isc.sans.edu, since the screenshot service returned an error message instead of the requested image. However, when I modified the URL to contain an e-mail address from another domain, the resulting page looked considerably more convincing.

[![](https://isc.sans.edu/diaryimages/images/26-11-17-site1.png)](https://isc.sans.edu/diaryimages/images/26-11-17-site1.png)

[![](https://isc.sans.edu/diaryimages/images/26-11-17-site2.png)](https://isc.sans.edu/diaryimages/images/26-11-17-site2.png)

Looking at the source code revealed a couple of layers of URL-encoding and additional JavaScript obfuscation. Once these were removed, the page turned out to contain a fairly typical credential-harvesting kit, which supported multiple languages and attempted to collect not just the submitted password, but also the visitor's public IP address, geographic location, browser information and language. This information, along with a timestamp, was supposed to be sent to the attacker using the Telegram Bot API.

Such extensive collection of information is not particularly unusual. In fact, another phishing page that I examined recently collected a similarly extensive set of information and also sent it to the attacker using Telegram. In the present case, however, one additional field included in the information sent to the attacker caught my attention – it was labeled "MX Record".

A closer look at the corresponding code revealed that the JavaScript actually performed a DNS-over-HTTPS query for MX records associated with the victim's e-mail domain, using Google's public DNS service. The relevant parts of the code (slightly simplified and reformatted for readability) looked as follows:

```
...
const response = await fetch(
    "https://dns.google/resolve?name=" + domain + "&amp;type=MX"
);
const data = await response.json();
return data.Answer.map(answer =&gt; answer.data).join("\n");
...
```

The retrieved records were then included in the message containing the stolen credentials:

```
...
message += "MX Record : " + await getMXRecord(domain) + "\n";
...
```

The use of MX records in phishing is certainly not new. For example, Infoblox documented a phishing-as-a-service operation called Morphing Meerkat in March 2025, which used DNS-over-HTTPS queries for MX records to identify victims' e-mail service providers and dynamically select appropriate phishing templates[
[1](https://www.infoblox.com/blog/threat-intelligence/a-phishing-tale-of-doh-and-dns-mx-abuse/)
].

In the present case, however, the MX records weren't used to customize the phishing page. Instead, the lookup was performed as part of the credential collection process, and its results were included in the information sent to the attacker.

Of course, MX records are publicly available, and there is nothing preventing an attacker from looking them up independently. Nevertheless, including them with each set of stolen credentials would help the attacker automatically identify the e-mail infrastructure used by the targeted organization, which could be useful for further attacks or for prioritizing the collected credentials.

Whether the threat actor behind this particular phishing actually used the collected MX records in this (or any) way is impossible to say. Still, having the phishing page perform a little additional reconnaissance on the victim's organization, and including the results with the stolen credentials, seems like a noteworthy detail in an otherwise fairly ordinary phishing kit…

[1]
&lt;https://www.infoblox.com/blog/threat-intelligence/a-phishing-tale-of-doh-and-dns-mx-abuse/&gt;

-----------

Jan Kopriva

[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)

[Nettles Consulting](https://www.nettles.cz/)