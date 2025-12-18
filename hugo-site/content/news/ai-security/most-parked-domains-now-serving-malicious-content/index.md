---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-18T00:03:24.607332+00:00'
exported_at: '2025-12-18T00:03:28.089917+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2025/12/most-parked-domains-now-serving-malicious-content
structured_data:
  about: []
  author: ''
  description: Most Parked Domains Now Serving Malicious Content
  headline: Most Parked Domains Now Serving Malicious Content
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2025/12/most-parked-domains-now-serving-malicious-content
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Most Parked Domains Now Serving Malicious Content
updated_at: '2025-12-18T00:03:24.607332+00:00'
url_hash: d74c24b60ff88ea7feab2c4dff78913e5daa15d3
---

Direct navigation — the act of visiting a website by manually typing a domain name in a web browser — has never been riskier: A new study finds the vast majority of “parked” domains — mostly expired or dormant domain names, or common misspellings of popular websites — are now configured to redirect visitors to sites that foist scams and malware.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/ic3org.png)

A lookalike domain to the FBI Internet Crime Complaint Center website, returned a non-threatening parking page (left) whereas a mobile user was instantly directed to deceptive content in October 2025 (right). Image: Infoblox.

When Internet users try to visit expired domain names or accidentally navigate to a lookalike “typosquatting” domain, they are typically brought to a placeholder page at a domain parking company that tries to monetize the wayward traffic by displaying links to a number of third-party websites that have paid to have their links shown.

A decade ago, ending up at one of these parked domains came with a relatively small chance of being redirected to a malicious destination: In 2014, researchers
[found](https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-alrwais.pdf)
(PDF) that parked domains redirected users to malicious sites less than five percent of the time — regardless of whether the visitor clicked on any links at the parked page.

But in a series of experiments over the past few months, researchers at the security firm
**Infoblox**
say they discovered the situation is now reversed, and that malicious content is by far the norm now for parked websites.

“In large scale experiments, we found that over 90% of the time, visitors to a parked domain would be directed to illegal content, scams, scareware and anti-virus software subscriptions, or malware, as the ‘click’ was sold from the parking company to advertisers, who often resold that traffic to yet another party,” Infoblox researchers wrote in
[a paper published today](https://blogs.infoblox.com/threat-intelligence/parked-domains-become-weapons-with-direct-search-advertising/)
.

Infoblox found parked websites are benign if the visitor arrives at the site using a virtual private network (VPN), or else via a non-residential Internet address. For example,
**Scotiabank.com**
customers who accidentally mistype the domain as
**scotaibank[.]com**
will see a normal parking page if they’re using a VPN, but will be redirected to a site that tries to foist scams, malware or other unwanted content if coming from a residential IP address. Again, this redirect happens just by visiting the misspelled domain with a mobile device or desktop computer that is using a residential IP address.

According to Infoblox, the person or entity that owns scotaibank[.]com has a portfolio of nearly 3,000 lookalike domains, including
**gmai[.]com**
, which demonstrably has been configured with its own mail server for accepting incoming email messages. Meaning, if you send an email to a Gmail user and accidentally omit the “l” from “gmail.com,” that missive doesn’t just disappear into the ether or produce a bounce reply: It goes straight to these scammers. The report notices this domain also has been leveraged in multiple recent business email compromise campaigns, using a lure indicating a failed payment with trojan malware attached.

Infoblox found this particular domain holder (betrayed by a common DNS server — torresdns[.]com) has set up typosquatting domains targeting dozens of top Internet destinations, including
**Craigslist**
,
**YouTube**
,
**Google**
,
**Wikipedia**
,
**Netflix**
,
**TripAdvisor**
,
**Yahoo**
,
**eBay**
, and
**Microsoft**
. A defanged list of these typosquatting domains is
[available here](https://krebsonsecurity.com/wp-content/uploads/2025/12/torresdns.txt)
(the dots in the listed domains have been replaced with commas).

**David Brunsdon**
, a threat researcher at Infoblox, said the parked pages send visitors through a chain of redirects, all while profiling the visitor’s system using IP geolocation, device fingerprinting, and cookies to determine where to redirect domain visitors.

“It was often a chain of redirects — one or two domains outside the parking company — before threat arrives,” Brunsdon said. “Each time in the handoff the device is profiled again and again, before being passed off to a malicious domain or else a decoy page like Amazon.com or Alibaba.com if they decide it’s not worth targeting.”

Brunsdon said domain parking services claim the search results they return on parked pages are designed to be relevant to their parked domains, but that almost none of this displayed content was related to the lookalike domain names they tested.

[![](https://krebsonsecurity.com/wp-content/uploads/2025/12/scotaibank.png)](https://krebsonsecurity.com/wp-content/uploads/2025/12/scotaibank.png)

Samples of redirection paths when visiting scotaibank dot com. Each branch includes a series of domains observed, including the color-coded landing page. Image: Infoblox.

Infoblox said a different threat actor who owns
**domaincntrol[.]com**
— a domain that differs from GoDaddy’s name servers by a single character — has long taken advantage of typos in DNS configurations to drive users to malicious websites. In recent months, however, Infoblox discovered the malicious redirect only happens when the query for the misconfigured domain comes from a visitor who is using Cloudflare’s DNS resolvers (1.1.1.1), and that all other visitors will get a page that refuses to load.

The researchers found that even variations on well-known government domains are being targeted by malicious ad networks.

“When one of our researchers tried to report a crime to the FBI’s
**Internet Crime Complaint Center**
(IC3), they accidentally visited ic3[.]org instead of ic3[.]gov,” the report notes. “Their phone was quickly redirected to a false ‘Drive Subscription Expired’ page. They were lucky to receive a scam; based on what we’ve learnt, they could just as easily receive an information stealer or trojan malware.”

The Infoblox report emphasizes that the malicious activity they tracked is not attributed to any known party, noting that the domain parking or advertising platforms named in the study were not implicated in the malvertising they documented.

However, the report concludes that while the parking companies claim to only work with top advertisers, the traffic to these domains was frequently sold to affiliate networks, who often resold the traffic to the point where the final advertiser had no business relationship with the parking companies.

Infoblox also pointed out that recent policy changes by
**Google**
may have inadvertently increased the risk to users from direct search abuse. Brunsdon said
**Google Adsense**
previously defaulted to allowing their ads to be placed on parked pages, but that in early 2025 Google implemented a default setting that had their customers
[opt-out by default](https://www.msn.com/en-us/news/technology/google-ads-to-remove-parked-domain-placements-by-default/ar-AA1zwYcS?apiversion=v2&noservercache=1&domshim=1&renderwebcomponents=1&wcseo=1&batchservertelemetry=1&noservertelemetry=1#:~:text=drives%20up%20CPCs-,Google%20Ads%20is%20making%20a%20major%20change%20to%20its%20Search,actively%20developed%2C%20starting%20March%2019.&text=SmartAsset-,Details:,their%20account's%20Content%20suitability%20settings)
on presenting ads on parked domains — requiring the person running the ad to voluntarily go into their settings and turn on parking as a location.