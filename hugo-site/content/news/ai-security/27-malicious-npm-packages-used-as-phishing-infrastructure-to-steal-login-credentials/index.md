---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-29T12:15:14.367663+00:00'
exported_at: '2025-12-29T12:15:16.893881+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/27-malicious-npm-packages-used-as.html
structured_data:
  about: []
  author: ''
  description: Researchers uncovered 27 malicious npm packages used over five months
    to host phishing pages that steal credentials from targeted organizations.
  headline: 27 Malicious npm Packages Used as Phishing Infrastructure to Steal Login
    Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/27-malicious-npm-packages-used-as.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 27 Malicious npm Packages Used as Phishing Infrastructure to Steal Login Credentials
updated_at: '2025-12-29T12:15:14.367663+00:00'
url_hash: e1cce26ad8d151579fef0f7031a8a3c37daeb138
---

Cybersecurity researchers have disclosed details of what has been described as a "sustained and targeted" spear-phishing campaign that has published over two dozen packages to the npm registry to facilitate credential theft.

The activity, which involved uploading 27 npm packages from six different npm aliases, has primarily targeted sales and commercial personnel at critical infrastructure-adjacent organizations in the U.S. and Allied nations, according to Socket.

"A five-month operation turned 27 npm packages into durable hosting for browser-run lures that mimic document-sharing portals and Microsoft sign-in, targeting 25 organizations across manufacturing, industrial automation, plastics, and healthcare for credential theft," researchers Nicholas Anderson and Kirill Boychenko
[said](https://socket.dev/blog/spearphishing-campaign-abuses-npm-registry)
.

The names of the packages are listed below -

* adril7123
* ardril712
* arrdril712
* androidvoues
* assetslush
* axerification
* erification
* erificatsion
* errification
* eruification
* hgfiuythdjfhgff
* homiersla
* houimlogs22
* iuythdjfghgff
* iuythdjfhgff
* iuythdjfhgffdf
* iuythdjfhgffs
* iuythdjfhgffyg
* jwoiesk11
* modules9382
* onedrive-verification
* sarrdril712
* scriptstierium11
* secure-docs-app
* sync365
* ttetrification
* vampuleerl

Rather than requiring users to install the packages, the end goal of the campaign is to repurpose npm and package content delivery networks (CDNs) as hosting infrastructure, using them to deliver client-side HTML and JavaScript lures impersonating secure document-sharing that are embedded directly in phishing pages, following which victims are redirected to Microsoft sign-in pages with the email address pre-filled in the form.

The use of package CDNs offers several benefits, the foremost being the ability to turn a legitimate distribution service into infrastructure that's resilient to takedowns. In addition, it makes it easy for attackers to switch to other publisher aliases and package names, even if the libraries are pulled.

The packages have been found to incorporate various checks on the client side to challenge analysis efforts, including filtering out bots, evading sandboxes, and requiring mouse or touch input before taking the victims to threat-actor-controlled credential harvesting infrastructure. The JavaScript code is also obfuscated or heavily minified to make automated inspection more difficult.

Another crucial anti-analysis control adopted by the threat actor relates to the use of honeypot form fields that are hidden from view for real users, but are likely to be populated by crawlers. This step acts as a second layer of defense, preventing the attack from proceeding further.

Socket said the domains packed into these packages overlap with adversary-in-the-middle (AitM) phishing infrastructure associated with
[Evilginx](https://thehackernews.com/2025/05/russian-hackers-breach-20-ngos-using.html)
, an open-source phishing kit.

This is not the first time npm has been transformed into phishing infrastructure. Back in October 2025, the software supply chain security firm
[detailed](https://thehackernews.com/2025/10/175-malicious-npm-packages-with-26000.html)
a campaign dubbed Beamglea that saw unknown threat actors uploading 175 malicious packages for credential harvesting attacks. The latest attack wave is assessed to be distinct from Beamglea.

"This campaign follows the same core playbook, but with different delivery mechanics," Socket said. "Instead of shipping minimal redirect scripts, these packages deliver a self-contained, browser-executed phishing flow as an embedded HTML and JavaScript bundle that runs when loaded in a page context."

What's more, the phishing packages have been found to hard-code 25 email addresses tied to specific individuals, who work in account managers, sales, and business development representatives in manufacturing, industrial automation, plastics and polymer supply chains, healthcare sectors in Austria, Belgium, Canada, France, Germany, Italy, Portugal, Spain, Sweden, Taiwan, Turkey, the U.K., and the U.S.

It's currently unknown how the attackers obtained the email addresses. But given that many of the targeted firms convene at major international trade shows, such as Interpack and K-Fair, it's suspected that the threat actors may have pulled the information from these sites and combined it with general open-web reconnaissance.

"In several cases, target locations differ from corporate headquarters, which is consistent with the threat actor's focus on regional sales staff, country managers, and local commercial teams rather than only corporate IT," the company said.

To counter the risk posed by the threat, it's essential to enforce stringent dependency verification, log unusual CDN requests from non-development contexts, enforce phishing-resistant multi-factor authentication (MFA), and monitor for suspicious post-authentication events.

The development comes as Socket said it observed a steady rise in destructive malware across npm, PyPI, NuGet Gallery, and Go module indexes using techniques like delayed execution and remotely-controlled kill switches to evade early detection and fetch executable code at runtime using standard tools such as wget and curl.

"Rather than encrypting disks or indiscriminately destroying files, these packages tend to operate surgically," researcher Kush Pandya
[said](https://socket.dev/blog/2025-report-destructive-malware-in-open-source-packages)
.

"They delete only what matters to developers: Git repositories, source directories, configuration files, and CI build outputs. They often blend this logic into otherwise functional code paths and rely on standard lifecycle hooks to execute, meaning the malware may never need to be explicitly imported or invoked by the application itself."