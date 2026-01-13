---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-13T20:15:13.394063+00:00'
exported_at: '2026-01-13T20:15:16.901758+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/long-running-web-skimming-campaign.html
structured_data:
  about: []
  author: ''
  description: Magecart web skimming campaign active since 2022 stealing credit card
    and personal data from compromised e-commerce checkout pages.
  headline: Long-Running Web Skimming Campaign Steals Credit Cards From Online Checkout
    Pages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/long-running-web-skimming-campaign.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Long-Running Web Skimming Campaign Steals Credit Cards From Online Checkout
  Pages
updated_at: '2026-01-13T20:15:13.394063+00:00'
url_hash: e363613ad12884edf179bcc1dcee31f152a68e11
---

**

Jan 13, 2026
**

Ravie Lakshmanan

Web Security / Data Theft

Cybersecurity researchers have discovered a major web skimming campaign that has been active since January 2022, targeting several major payment networks like American Express, Diners Club, Discover, JCB Co., Ltd., Mastercard, and UnionPay.

"Enterprise organizations that are clients of these payment providers are the most likely to be impacted," Silent Push
[said](https://www.silentpush.com/blog/magecart/)
in a report published today.

Digital skimming attacks refer to a category of client-side attacks in which bad actors compromise legitimate e-commerce sites and payment portals to inject malicious JavaScript code that's capable of stealthily harvesting credit card information and other personal information when unsuspecting users attempt to make a payment on checkout pages.

These attacks are classified under an umbrella term called
[Magecart](https://thehackernews.com/2025/02/cybercriminals-exploit-onerror-event-in.html)
, which initially referred to a coalition of cybercriminal groups that targeted e-commerce sites using the Magento software, before diversifying to other products and platforms.

Silent Push said it discovered the campaign after analyzing a suspicious domain linked to a now-sanctioned bulletproof hosting provider Stark Industries (and its parent company PQ.Hosting), which has since
[rebranded](https://thehackernews.com/2025/09/ukrainian-network-fdn3-launches-massive.html)
to THE[.]Hosting, under the control of the Dutch entity WorkTitans B.V., is a sanctions evasion measure.

The domain in question, cdn-cookie[.]com, has been found to host highly obfuscated JavaScript payloads (e.g., "recorder.js" or "tab-gtm.js") that are loaded by web shops to facilitate credit card skimming.

The skimmer comes with features to evade detection by site administrators. Specifically, it checks the Document Object Model (DOM) tree for an element named "
[wpadminbar](https://developer.wordpress.org/reference/classes/wp_admin_bar/)
," a reference to a toolbar that appears in WordPress websites when logged-in administrators or users with appropriate permissions are viewing the site.

In the event the "wpadminbar" element is present, the skimmer initiates a self-destruct sequence and removes its own presence from the web page. An attempt to execute the skimmer is made every time the web page's DOM is modified, a standard behavior that occurs when users interact with the page.

That's not all. The skimmer also checks to see if Stripe was selected as a payment option, and if so, there exists an element called "wc\_cart\_hash" in the browser's
[localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
, which it creates and sets to "true" to indicate that the victim has already been successfully skimmed.

The absence of this flag causes the skimmer to render a fake Stripe payment form that replaces the legitimate form through user interface manipulations, thereby tricking the victims into entering their credit card numbers, along with the expiration dates and Card Verification Code (CVC) numbers.

"As the victim entered their credit card details into a fake form instead of the real Stripe payment form, which was initially hidden by the skimmer when they initially filled it out, the payment page will display an error," Silent Push said. "This makes it appear as if the victim had simply entered their payment details incorrectly."

The data stolen by the skimmer extends beyond payment details to include names, phone numbers, email addresses, and shipping addresses. The information is eventually exfiltrated by means of an HTTP POST request to the server "lasorie[.]com."

Once the data transmission is complete, the skimmer erases traces of itself from the checkout page, removing the fake payment form that was created and restoring the legitimate Stripe input form. It then sets "wc\_cart\_hash" to "true" to prevent the skimmer from being run a second time on the same victim.

"This attacker has advanced knowledge of WordPress's inner workings and integrates even lesser-known features into their attack chain," Silent Push said.