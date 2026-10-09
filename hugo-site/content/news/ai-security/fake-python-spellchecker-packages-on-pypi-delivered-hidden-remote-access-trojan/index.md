---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-28T12:15:13.100833+00:00'
exported_at: '2026-01-28T12:15:15.375641+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/fake-python-spellchecker-packages-on.html
structured_data:
  about: []
  author: ''
  description: Two fake spellchecker packages on PyPI hid a Python RAT in dictionary
    files, activating malware on import in version 1.2.0.
  headline: Fake Python Spellchecker Packages on PyPI Delivered Hidden Remote Access
    Trojan
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/fake-python-spellchecker-packages-on.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fake Python Spellchecker Packages on PyPI Delivered Hidden Remote Access Trojan
updated_at: '2026-01-28T12:15:13.100833+00:00'
url_hash: 478ca009cdb3d515ca931dbc3937bb6eaa46789b
---

**

Ravie Lakshmanan
**

Jan 28, 2026

Supply Chain Security / Malware

Cybersecurity researchers have discovered two malicious packages in the Python Package Index (PyPI) repository that masquerade as spellcheckers but contain functionality to deliver a remote access trojan (RAT).

The packages, named
**spellcheckerpy**
and
**spellcheckpy**
, are no longer available on PyPI, but not before they were collectively downloaded a little over 1,000 times.

"Hidden inside the Basque language dictionary file was a base64-encoded payload that downloads a full-featured Python RAT," Aikido researcher Charlie Eriksen
[said](https://www.aikido.dev/blog/malicious-pypi-packages-spellcheckpy-and-spellcheckerpy-deliver-python-rat)
. "The attacker published three 'dormant' versions first, payload present, trigger absent, then flipped the switch with spellcheckpy v1.2.0, adding an obfuscated execution trigger that fires the moment you import SpellChecker."

Unlike other packages that conceal the malicious functionality within "\_\_init\_\_.py" scripts, the threat actor behind the campaign has been found to add the payload inside a file named "resources/eu.json.gz" that contains Basque word frequencies from the legitimate pyspellchecker package.

While the package appears harmless at first glance, the malicious behavior is triggered when the archive file is extracted using the test\_file() function with the parameters: test\_file("eu", "utf-8", "spellchecker"), causing it to retrieve a Base64-encoded downloader hidden in the dictionary under a key called "spellchecker."

Interestingly, the first three versions of the package only fetched and decoded the payload, but never executed it. However, that changed with the release of spellcheckpy version 1.2.0, published on January 21, 2026, when it gained the ability to run the payload as well.

The first stage is a downloader that's designed to retrieve a Python-based RAT from an external domain ("updatenet[.]work"). It's capable of fingerprinting the compromised host, parsing incoming commands, and executing them. The domain, registered in late October 2025, is associated with 172.86.73[.]139, an IP address managed by RouterHosting LLC (aka Cloudzy), a hosting provider that has a
[history](https://www.halcyon.ai/blog/update-cloudzy-command-and-control-provider-report)
of offering its services to nation-state groups.

This is not the first time fake Python spell-checking tools have been detected in PyPI. In November 2025, HelixGuard
[said](https://thehackernews.com/2025/11/legacy-python-bootstrap-scripts-create.html)
it discovered a malicious package named "spellcheckers" that featured the ability to retrieve and execute a RAT payload. It's suspected that these two sets of attacks are the work of the same threat actor.

The development coincides with the discovery of several malicious npm packages to facilitate data theft and target cryptocurrency wallets -

* flockiali (1.2.3-1.2.6), opresc (1.0.0), prndn (1.0.0), oprnm (1.0.0), and operni, which
  [contain](https://www.aikido.dev/blog/npm-supply-chain-phishing-campaigns)
  a single JavaScript file that, when loaded, serves a fake Microsoft-branded login screen as part of a
  [targeted spear-phishing campaign](https://thehackernews.com/2025/12/27-malicious-npm-packages-used-as.html)
  hitting employees at specific industrial and energy companies located in France, Germany, Spain, the U.A.E, and the U.S. with malicious links

* ansi-universal-ui (1.3.5, 1.3.6, 1.3.7, 1.4.0, 1.4.1), which masquerades as a UI component library but deploys a Python-based stealer dubbed
  [G\_Wagon](https://www.aikido.dev/blog/npm-malware-g-wagon-python-stealer-crypto-wallets)
  that exfiltrates web browser credentials, cryptocurrency wallets, cloud credentials, and Discord tokens to an Appwrite storage bucket

The disclosure also comes as Aikido highlighted the threat associated with
[slopsquatting](https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html)
, wherein artificial intelligence (AI)-powered agents can hallucinate non-existent packages that could then be claimed by a threat actor to push malicious code to downstream users.

In one case highlighted by the supply chain security company, it has been found that a fictitious npm package named "react-codeshift" is referenced by 237 GitHub repositories since it was made up by a large language model in mid-October 2025, with some of them even instructing AI agents to install it.

"How did it spread to 237 repos? Agent skill files. Copy-pasted, forked, translated into Japanese, never once verified," Eriksen
[said](https://www.aikido.dev/blog/agent-skills-spreading-hallucinated-npx-commands)
. "Skills are the new code. They don't look like it. They're Markdown and YAML and friendly instructions. But they're executable. AI agents follow them without asking, 'Does this package actually exist?'"