---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-12T08:03:56.699000+00:00'
exported_at: '2025-12-12T08:04:00.318390+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2025/12/sms-phishers-pivot-to-points-taxes-fake-retailers
structured_data:
  about: []
  author: ''
  description: SMS Phishers Pivot to Points, Taxes, Fake Retailers
  headline: SMS Phishers Pivot to Points, Taxes, Fake Retailers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2025/12/sms-phishers-pivot-to-points-taxes-fake-retailers
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: SMS Phishers Pivot to Points, Taxes, Fake Retailers
updated_at: '2025-12-12T08:03:56.699000+00:00'
url_hash: b6341b686646e46a0915b9d8f3bc2fcd5bdf3c33
---

China-based phishing groups blamed for non-stop scam SMS messages about a supposed wayward package or unpaid toll fee are promoting a new offering, just in time for the holiday shopping season: Phishing kits for mass-creating fake but convincing e-commerce websites that convert customer payment card data into mobile wallets from Apple and Google. Experts say these same phishing groups also are now using SMS lures that promise unclaimed tax refunds and mobile rewards points.

Over the past week, thousands of domain names were registered for scam websites that purport to offer
**T-Mobile**
customers the opportunity to claim a large number of rewards points. The phishing domains are being promoted by scam messages sent via Apple’s iMessage service or the functionally equivalent RCS messaging service built into Google phones.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/tmobpoints-smish.png)

An instant message spoofing T-Mobile says the recipient is eligible to claim thousands of rewards points.

The website scanning service
**urlscan.io**
[shows](http://urlscan.io/result/019a609e-8dda-7612-a4b1-a6fe2c0bff6d)
thousands of these phishing domains have been deployed in just the past few days alone. The phishing websites will only load if the recipient visits with a mobile device, and they ask for the visitor’s name, address, phone number and payment card data to claim the points.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/tmob-points-site.png)

A phishing website registered this week that spoofs T-Mobile.

If card data is submitted, the site will then prompt the user to share a one-time code sent via SMS by their financial institution. In reality, the bank is sending the code because the fraudsters have just attempted to enroll the victim’s phished card details in a mobile wallet from Apple or Google. If the victim also provides that one-time code, the phishers can then
[link the victim’s card to a mobile device that they physically control](https://krebsonsecurity.com/2025/02/how-phished-data-turns-into-apple-google-wallets/)
.

Pivoting off these T-Mobile phishing domains in urlscan.io reveals a similar scam targeting
**AT&T**
customers:

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/att-smish.png)

An SMS phishing or “smishing” website targeting AT&T users.

**Ford Merrill**
works in security research at
[SecAlliance](https://www.secalliance.com/)
, a
[CSIS Security Group](https://www.csis.com/)
company. Merrill said multiple China-based cybercriminal groups that sell phishing-as-a-service platforms have been using the mobile points lure for some time, but the scam has only recently been pointed at consumers in the United States.

“These points redemption schemes have not been very popular in the U.S., but have been in other geographies like EU and Asia for a while now,” Merrill said.

A review of other domains flagged by urlscan.io as tied to this Chinese SMS phishing syndicate shows they are also spoofing U.S. state tax authorities, telling recipients they have an unclaimed tax refund. Again, the goal is to phish the user’s payment card information and one-time code.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/dctaxphish.png)

A text message that spoofs the District of Columbia’s Office of Tax and Revenue.

## CAVEAT EMPTOR

Many SMS phishing or “smishing” domains are quickly flagged by browser makers as malicious. But Merrill said one burgeoning area of growth for these phishing kits — fake e-commerce shops — can be far harder to spot because they do not call attention to themselves by spamming the entire world.

Merrill said the same Chinese phishing kits used to blast out package redelivery message scams are equipped with modules that make it simple to quickly deploy a fleet of fake but convincing e-commerce storefronts. Those phony stores are typically advertised on
**Google**
and
**Facebook**
, and consumers usually end up at them by searching online for deals on specific products.

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/fake-ecom.png)

A machine-translated screenshot of an ad from a China-based phishing group promoting their fake e-commerce shop templates.

With these fake e-commerce stores, the customer is supplying their payment card and personal information as part of the normal check-out process, which is then punctuated by a request for a one-time code sent by your financial institution. The fake shopping site claims the code is required by the user’s bank to verify the transaction, but it is sent to the user because the scammers immediately attempt to enroll the supplied card data in a mobile wallet.

According to Merrill, it is only during the check-out process that these fake shops will fetch the malicious code that gives them away as fraudulent, which tends to make it difficult to locate these stores simply by mass-scanning the web. Also, most customers who pay for products through these sites don’t realize they’ve been snookered until weeks later when the purchased item fails to arrive.

“The fake e-commerce sites are tough because a lot of them can fly under the radar,” Merrill said. “They can go months without being shut down, they’re hard to discover, and they generally don’t get flagged by safe browsing tools.”

Happily, reporting these SMS phishing lures and websites is one of the fastest ways to get them properly identified and shut down.
**Raymond Dijkxhoorn**
is the CEO and a founding member of
[SURBL](https://www.surbl.org/)
, a widely-used blocklist that flags domains and IP addresses known to be used in unsolicited messages, phishing and malware distribution. SURBL has created a website called
[smishreport.com](https://smishreport.com)
that asks users to forward a screenshot of any smishing message(s) received.

“If [a domain is] unlisted, we can find and add the new pattern and kill the rest” of the matching domains,
**Dijkxhoorn**
said. “Just make a screenshot and upload. The tool does the rest.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/12/smishreport.png)

The SMS phishing reporting site smishreport.com.

Merrill said the last few weeks of the calendar year typically see a big uptick in smishing — particularly package redelivery schemes that spoof the
**U.S. Postal Service**
or commercial shipping companies.

“Every holiday season there is an explosion in smishing activity,” he said. “Everyone is in a bigger hurry, frantically shopping online, paying less attention than they should, and they’re just in a better mindset to get phished.”

## SHOP ONLINE LIKE A SECURITY PRO

As we can see, adopting a shopping strategy of simply buying from the online merchant with the lowest advertised prices can be a bit like playing Russian Roulette with your wallet. Even people who shop mainly at big-name online stores
[can get scammed](https://krebsonsecurity.com/2017/04/how-cybercrooks-put-the-beatdown-on-my-beats/)
if they’re not wary of too-good-to-be-true offers (think third-party sellers on these platforms).

If you don’t know much about the online merchant that has the item you wish to buy, take a few minutes to investigate its reputation. If you’re buying from an online store that is brand new, the risk that you will get scammed increases significantly. How do you know the lifespan of a site selling that must-have gadget at the lowest price? One easy way to get a quick idea is to run
[a basic WHOIS search](http://whois.domaintools.com/krebsonsecurity.com "http://whois.domaintools.com/krebsonsecurity.com")
on the site’s domain name. The more recent the site’s “created” date, the more likely it is a phantom store.

If you receive a message warning about a problem with an order or shipment, visit the e-commerce or shipping site directly, and avoid clicking on links or attachments — particularly missives that warn of some dire consequences unless you act quickly. Phishers and malware purveyors typically seize upon some kind of emergency to create a false alarm that often causes recipients to temporarily let their guard down.

But it’s not just outright scammers who can trip up your holiday shopping: Often times, items that are advertised at steeper discounts than other online stores make up for it by charging way more than normal for shipping and handling.

So be careful what you agree to: Check to make sure you know how long the item will take to be shipped, and that you understand the store’s return policies. Also, keep an eye out for hidden surcharges, and be wary of blithely clicking “ok” during the checkout process.

Most importantly, keep a close eye on your monthly statements. If I were a fraudster, I’d most definitely wait until the holidays to cram through a bunch of unauthorized charges on stolen cards, so that the bogus purchases would get buried amid a flurry of other legitimate transactions. That’s why it’s key to closely review your credit card bill and to quickly dispute any charges you didn’t authorize.