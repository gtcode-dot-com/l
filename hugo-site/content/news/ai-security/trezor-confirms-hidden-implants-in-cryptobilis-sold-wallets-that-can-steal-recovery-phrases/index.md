---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:14:00.522093+00:00'
exported_at: '2026-11-15T07:14:01.551872+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/trezor-confirms-hidden-hardware.html
structured_data:
  about: []
  author: ''
  description: Trezor confirms recovery phrase-stealing implants in three CryptoBilis-sold
    Safe 5 wallets and says firmware 2.13.1 blocks known implants.
  headline: Trezor Confirms Hidden Implants in CryptoBilis-Sold Wallets That Can Steal
    Recovery Phrases
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/trezor-confirms-hidden-hardware.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trezor Confirms Hidden Implants in CryptoBilis-Sold Wallets That Can Steal
  Recovery Phrases
updated_at: '2026-11-15T07:14:00.522093+00:00'
url_hash: 79815295aaa35652286ebd378799329196965407
---

**

Swati Khandelwal
**

Nov 13, 2026

Cryptocurrency / Supply Chain

Three
**Trezor Safe 5**
wallets bought from the reseller
**CryptoBilis**
contain an implant, an extra circuit board that can copy their recovery phrases, hardware wallet maker Trezor said yesterday.

The implant reads the phrase from the wallet's screen and sends it over the mobile network to a server controlled by the attackers. The company examined one of the wallets in its lab, identified the other two from photos their owners sent, and has had no reports of lost funds.

A firmware update released earlier this week, version 2.13.1, stops the implants found so far from capturing anything on wallets that run it, the company said, but “the update can’t protect a wallet backup that was captured before it.”

The company has not changed its advice to anyone who bought a Trezor from CryptoBilis since March, including from the reseller's stores on Tokopedia and Shopee:

* Move your funds to a new wallet with a new recovery phrase. Restoring the old phrase on another wallet does not solve the problem.
* Do not set up an unused wallet from the reseller, and never type an existing recovery phrase into one.
* Keep the wallet and contact Trezor Support, which offers a new Trezor wallet to anyone who bought from the reseller since March. Contact Support too if you are not sure where your wallet came from.
* Do not weigh or open the wallet to check it. Neither is a reliable test.
* Never share your recovery phrase, as the company will never ask for it. Scammers may pose as the company to offer replacements or refunds.

Version 2.13.1 was released for the Safe 7, Safe 5, Safe 3 and Model T, according to the company's
[firmware changelog](https://trezor.io/other/product-updates/trezor-firmware-changelog-all-versions-and-release-dates)
. The company will not publish technical details that could help attackers or put customers at risk, it said in an
[investigation update](https://trezor.io/blog/news/our-cryptobilis-investigation-what-we-found-and-what-weve-changed)
.

Its engineers extracted and analyzed the implant's firmware from the first wallet it reported. The implant sits between the Safe 5's main board and its screen and changes nothing on the wallet itself, including its firmware and Secure Element, the company found.

The implant copies the recovery phrase when the wallet shows it during backup creation, and when someone types it in to restore an existing wallet to the device. It also copies a passphrase if one appears on the screen. It encrypts the data before sending it, and if it cannot connect, it keeps the data and tries again until it succeeds.

The
[company first warned of a suspected implant on October 30](https://thehackernews.com/2026/10/trezor-warns-of-suspected-hardware.html)
, two days after a buyer reported it and before its lab had seen the wallet.

CryptoBilis served as an official reseller for the company's wallets in Southeast Asia until October 9, when the company removed it. That was the day Ledger, another hardware wallet maker, began investigating losses of funds among the reseller's customers.

Ledger later confirmed an
[unauthorized implant](https://thehackernews.com/2026/10/ledger-finds-unauthorized-hardware.html)
in a wallet the reseller sold. Attackers had fitted genuine Ledger devices with hidden components designed to capture the recovery phrase during setup, then drained wallets in a single coordinated operation, Ledger said in an
[incident statement](https://www.ledger.com/blog-response-hardware-implant-attack)
.

Trezor says the implants in its wallets work the same way as those found in Ledger devices, adapted to the Safe 5's display. It has not said who fitted the implants or where in the supply chain that happened.

The three wallets were bought between August 20 and September 23. So far the company has found implants only in Safe 5 wallets sold by the reseller, and none in wallets from its other resellers or in its other models.

After the October reports, it asked people who bought a Trezor from the reseller to get in touch, and 48 have done so. It is checking their wallets in its lab or from photos of the insides, and has not said how many it has checked so far.

The company says none of the three owners has lost funds. Trezor wallets are self-custodial, so it cannot see anyone's balance.

The company says it has cut its reseller network by about 80%, dropping trustworthy partners that posed no immediate threat but did not fit its stricter new rules. It first announced the reduction on October 13 in a
[post on X](https://x.com/Trezor/status/2110000774314873020)
, more than two weeks before the first report of an implant in one of its own wallets.

In a
[partner letter](https://x.com/Dantoshi/status/2110000117856248141)
that day, it told the dropped resellers that they would get no new stock, could sell what they had until January 1, 2027, and would then be removed from its list of authorized sellers.

It is still investigating. It will post an update if it confirms an implant outside the reseller's wallets or the Safe 5, receives a report of lost funds linked to the implants, or releases new protections.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.