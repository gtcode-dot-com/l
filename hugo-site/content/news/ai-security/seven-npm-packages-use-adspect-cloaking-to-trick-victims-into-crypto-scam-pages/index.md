---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-18T16:25:45.102032+00:00'
exported_at: '2025-11-18T16:25:46.460520+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/seven-npm-packages-use-adspect-cloaking.html
structured_data:
  about: []
  author: ''
  description: Malicious npm packages use Adspect cloaking to filter victims and deliver
    crypto-themed redirects.
  headline: Seven npm Packages Use Adspect Cloaking to Trick Victims Into Crypto Scam
    Pages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/seven-npm-packages-use-adspect-cloaking.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Seven npm Packages Use Adspect Cloaking to Trick Victims Into Crypto Scam Pages
updated_at: '2025-11-18T16:25:45.102032+00:00'
url_hash: 054df1370ed2a40a3a99d897a855f5a49ed3fc67
---

**

Nov 18, 2025
**

Ravie Lakshmanan

Malware / Web Security

Cybersecurity researchers have
[discovered](https://socket.dev/blog/npm-malware-campaign-uses-adspect-cloaking-to-deliver-malicious-redirects)
a set of seven npm packages published by a single threat actor that leverages a cloaking service called Adspect to differentiate between real victims and security researchers to ultimately redirect them to sketchy crypto-themed sites.

The malicious npm packages, published by a threat actor named "
[dino\_reborn](https://www.npmjs.com/~dino_reborn)
" between September and November 2025, are listed below. The npm account no longer exists on npm as of writing.

* signals-embed (342 downloads)
* dsidospsodlks (184 downloads)
* applicationooks21 (340 downloads)
* application-phskck (199 downloads)
* integrator-filescrypt2025 (199 downloads)
* integrator-2829 (276 downloads)
* integrator-2830 (290 downloads)

"Upon visiting a fake website constructed by one of the packages, the threat actor determines if the visitor is a victim or a security researcher," Socket security researcher Olivia Brown said.

"If the visitor is a victim, they see a fake CAPTCHA, eventually bringing them to a malicious site. If they are a security researcher, only a few tells on the fake website would tip them off that something nefarious may be occurring."

Of these packages, six of them contain a 39kB malware that incorporates the cloaking mechanism and captures a fingerprint of the system, while simultaneously taking steps to sidestep analysis by blocking developer actions in a web browser, effectively preventing researchers from viewing the source code or launching developer tools.

The packages take advantage of a JavaScript feature called Immediately Invoked Function Expression (
[IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
), which allows the malicious code to be executed immediately upon loading it in the web browser. In contrast, "signals-embed" does not harbor any malicious functionality outright and is designed to construct a decoy white page.

The captured information is sent to a proxy ("association-google[.]xyz/adspect-proxy[.]php") to determine if the traffic source is from a victim or a researcher, and then serve a fake CAPTCHA. Once a victim clicks on the CAPTCHA checkbox, they are taken to a bogus cryptocurrency-related page impersonating services like StandX with the likely goal of stealing digital assets.

However, if the visitors are flagged as potential researchers, a white decoy page is displayed to the users. It also features HTML code related to the display privacy policy associated with a fake company named Offlido.

Adspect, according to its
[website](https://www.adspect.ai/en/)
, advertises a cloud-based service that's
[designed](https://docs.adspect.ai/en/latest/overview.html)
to protect ad campaigns from unwanted traffic, such as click fraud and bots from antivirus companies. It also claims to offer "bulletproof cloaking" and that it "reliably cloaks each and every advertising platform."

It offers three plans: Ant-fraud, Personal, and Professional that cost $299, $499, and $999 per month. The company also claims users can advertise "anything you want," adding it follows a no-questions-asked policy: we do not care what you run and do not enforce any content rules."

"The use of Adspect cloaking within npm supply-chain packages is rare," Socket said. "This is an attempt to merge traffic cloaking, anti-research controls, and open source distribution. By embedding Adspect logic in npm packages, the threat actor can distribute a self-contained traffic-gating toolkit that automatically decides which visitors to expose to real payloads."