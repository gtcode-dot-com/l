---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-03T06:42:40.638376+00:00'
exported_at: '2026-03-03T06:42:42.956291+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/malicious-stripeapi-nuget-package.html
structured_data:
  about: []
  author: ''
  description: Malicious StripeApi.Net package on NuGet mimicked Stripe.net, logged
    180,000 downloads, and stole Stripe API tokens before removal.
  headline: Malicious StripeApi NuGet Package Mimicked Official Library and Stole
    API Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/malicious-stripeapi-nuget-package.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious StripeApi NuGet Package Mimicked Official Library and Stole API Tokens
updated_at: '2026-03-03T06:42:40.638376+00:00'
url_hash: a5532bf71ffd095514dcc49b91852467349fad6f
---

**

Ravie Lakshmanan
**

Feb 26, 2026

Malware / Software Security

Cybersecurity researchers have disclosed details of a new malicious package discovered on the NuGet Gallery, impersonating a library from financial services firm Stripe in an attempt to target the financial sector.

The package, codenamed StripeApi.Net, attempts to masquerade as
[Stripe.net](https://www.nuget.org/packages/Stripe.net)
, a legitimate library from Stripe that has over 75 million downloads. It was uploaded by a user named StripePayments on February 16, 2026. The package is no longer available.

"The NuGet page for the malicious package is set up to resemble the official Stripe.net package as closely as possible," ReversingLabs Petar Kirhmajer
[said](https://www.reversinglabs.com/blog/malicious-nuget-package-targets-stripe)
. "It uses the same icon as the legitimate package and contains a nearly identical readme, only swapping the 'Stripe.net' references to read 'Stripe-net.'"

In a further effort to lend credibility to the typosquatted package, the threat actor behind the campaign is said to have artificially inflated the download count to more than 180,000. But in an interesting twist, the downloads were split across 506 versions, with each version recording about 300 downloads on average.

The package replicates some of the legitimate Stripe package's functionality, but also modifies certain critical methods to collect and transfer sensitive data, including the user's Stripe API token, back to the threat actor. With the rest of the codebases remaining fully functional, it's unlikely to attract any suspicion from unsuspecting developers who may have inadvertently downloaded it.

ReversingLabs said it discovered and reported the package "relatively soon" after it was initially released, causing it to be taken before it could inflict any serious damage.

The software supply chain security company also noted that the activity marks a shift from
[prior campaigns](https://thehackernews.com/2025/10/fake-nethereum-nuget-package-used.html)
that have leveraged
[bogus NuGet packages](https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html)
to target the cryptocurrency ecosystem and facilitate wallet key theft.

"Developers who mistakenly download and integrate a typosquatted library like StripeAPI.net will still have their applications compile successfully and function as intended," Kirhmajer said. "Payments would process normally and, from the developer’s perspective, nothing would appear broken. In the background, however, sensitive data is being secretly copied and exfiltrated by malicious actors."