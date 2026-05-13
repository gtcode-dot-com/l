---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-13T04:14:15.702094+00:00'
exported_at: '2026-05-13T04:14:18.106639+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/fake-call-history-apps-stole-payments.html
structured_data:
  about: []
  author: ''
  description: 28 fake Google Play apps gained 7.3 million downloads, charging users
    for fake call data and causing financial losses.
  headline: Fake Call History Apps Stole Payments From Users After 7.3 Million Play
    Store Downloads
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/fake-call-history-apps-stole-payments.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake Call History Apps Stole Payments From Users After 7.3 Million Play Store
  Downloads
updated_at: '2026-05-13T04:14:15.702094+00:00'
url_hash: 4cb29afddbd876faa929ac886830874826178463
---

Cybersecurity researchers have discovered fraudulent apps on the official Google Play Store for Android that falsely claimed to offer access to call histories for any phone number, only to trick users into joining a subscription that provided fake data and incurred financial loss.

The 28 apps have collectively racked up more than 7.3 million downloads, with one of them alone accounting for over 3 million downloads, before they were taken down from the official app storefront.The activity, codenamed
**CallPhantom**
by Slovakian cybersecurity company ESET, primarily targeted Android users in India and the broader Asia-Pacific region.

"The offending apps, which we named CallPhantom based on their false claims, purport to provide access to call histories, SMS records, and even WhatsApp call logs for any phone number," ESET security researcher Lukáš Štefanko
[said](https://www.welivesecurity.com/en/eset-research/fake-call-logs-real-payments-how-callphantom-tricks-android-users/)
in a report shared with The Hacker News. "To unlock this supposed feature, users are asked to pay -- but all they get in return is randomly generated data."

The list of identified apps is below -

* Call history : any number deta (calldetaila.ndcallhisto.rytogetan.ynumber)
* Call History of Any Number (com.pixelxinnovation.manager)
* Call Details of Any Number (com.app.call.detail.history)
* Call History Any Number Detail (sc.call.ofany.mobiledetail)
* Call History Any Number Detail (com.cddhaduk.callerid.block.contact)
* Call History Of Any Number (com.basehistory.historydownloading)
* Call History of Any Numbers (com.call.of.any.number)
* Call History Of Any Number (com.rajni.callhistory)
* Call History Any Number Detail (com.callhistory.calldetails.callerids.callerhistory.callhostoryanynumber.getcall.history.callhistorymanager)
* Call History Any Number Detail (com.callinformative.instantcallhistory.callhistorybluethem.callinfo)
* Call History Any Number detail (com.call.detail.caller.history)
* Call History Any Number Detail (com.anycallinformation.datadetailswho.callinfo.numberfinder)
* Call History Any Number Detail (com.callhistory.callhistoryyourgf)
* Call History Any Number (com.calldetails.smshistory.callhistoryofanynumber)
* Call History Any Number Detail  (com.callhistory.anynumber.chapfvor.history)
* Call History of Any Number (com.callhistory.callhistoryany.call)
* Call History Any Number Detail (com.name.factor)
* Call History Of Any Number (com.getanynumberofcallhistory.callhistoryofanynumber.findcalldetailsofanynumber)
* Call History Of Any Number (com.chdev.callhistory)
* Phone Call History Tracker (com.phone.call.history.tracke)
* Call History- Any Number Deta (com.pdf.maker.pdfreader.pdfscanner)
* Call History Of Any Number (com.any.numbers.calls.history)
* Call History Any Number Detail (com.callapp.historyero)
* Call History - Any Number Data (all.callhistory.detail)
* Call History For Any Number (com.easyranktools.callhistoryforanynumber)
* Call History of Numbers (com.sbpinfotech.findlocationofanynumber)
* Call History of Any Number (callhistoryeditor.callhistory.numberdetails.calleridlocator)
* Call History Pro (com.all\_historydownload.anynumber.callhistorybackup)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRH1F1UJlGdmSJUfePA0hYYR1NJe4_aE68GiPU2xdaBA4I48HD4cArAmqKmveG0TivC-bo1zFBePxg_IAEfoeYwTm2EBlz5AWjlPD8AlnJtjw2sMsde6S3VbIJLZHVvE8DNJjQp7oMbpII_e1SdzNyMqG3SUuSv7KODPSa4zfFlFaUiFfH26mS9s03wqc5/s1600/payment.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRH1F1UJlGdmSJUfePA0hYYR1NJe4_aE68GiPU2xdaBA4I48HD4cArAmqKmveG0TivC-bo1zFBePxg_IAEfoeYwTm2EBlz5AWjlPD8AlnJtjw2sMsde6S3VbIJLZHVvE8DNJjQp7oMbpII_e1SdzNyMqG3SUuSv7KODPSa4zfFlFaUiFfH26mS9s03wqc5/s1600/payment.jpg)

At least one of the flagged apps was published under the developer name "Indian gov.in" in an attempt to build a false sense of trust and unsuspecting trick users into downloading it.

However, this trick masks a nefarious motive where victims are asked to make a payment in order to view details of a phone number's call and SMS history. Once the payment is made, users are served entirely fabricated phone numbers and names directly embedded into the source code. Evidence indicates that the activity may have been active
[since at least November 2025](https://www.reddit.com/r/IndiaTech/comments/1on69g4/guys_look_what_i_found_on_playstore/)
.

A second cluster of these apps has been found to prompt users to enter their email address to which the purported details of any phone number would be delivered to. As in the prior case, no data is generated until a payment is made.

The payments either rely on subscriptions via Google Play Store's official billing system or via third-party apps that support Unified Payments Interface (UPI), an instant payment system widely used in India. Ironically, this list includes Google Pay, Walmart-backed PhonePe, and Paytm. A third method includes payment card checkout forms directly inside the apps. The last two approaches are in violation of Google's policy.

In at least one case, the apps implemented an additional trick to convince the user to make a payment. Should they exit the app without making any payment, it displays a deceptive notification claiming that a call history for a certain phone number had been successfully sent to their email address. Clicking on the notification directly takes the user to a subscription screen.

The subscription plans vary across the app, ranging anywhere from about $6 to $80. Users who may have fallen prey to the scam should have had their
[subscriptions canceled](https://support.google.com/googleplay/answer/7018481)
after the apps were removed from the Google Play Store.

What makes this activity notable is that the apps have a simple user interface and do not request any sensitive permissions. And to top it all, they do not even contain any functionality to retrieve call, SMS, or WhatsApp data.

"Users who subscribed via official Google Play billing may be eligible for refunds under Google's refund policies," ESET said. "Purchases made via third‑party payment apps or through direct payment card entry cannot be refunded by Google, leaving users dependent on external payment providers or developers."

The disclosure comes as Group-IB said bad actors have stolen an estimated $2 million from Indonesian users as part of a fraud campaign that involved posing as the country's tax platform, CoreTax, and other trusted brands. The campaign, which began in July 2025, has been linked to a financially motivated threat cluster called
[GoldFactory](https://thehackernews.com/2025/12/goldfactory-hits-southeast-asia-with.html)
.

"The attack chain integrates phishing websites, social engineering (WhatsApp), malicious APK sideloading, and voice phishing (vishing) to achieve full device compromise and unauthorized transfer execution," Group-IB
[said](https://www.group-ib.com/blog/indonesia-tax-impersonation-goldfactory-malware/)
.

At a high level, these attacks involve using social engineering to distribute the fake apps via WhatsApp, which, when installed, deploy Android malware such as
[Gigabud RAT](https://thehackernews.com/2024/02/chinese-hackers-using-deepfakes-in.html)
,
[MMRat](https://thehackernews.com/2023/08/mmrat-android-trojan-executes-remote.html)
, and Taotie that are capable of harvesting sensitive data and downloading additional components. The stolen information is then used to conduct account takeover attacks and financial theft.

"The malware infrastructure supporting this fraud campaign is not limited to a single impersonated service. The same infrastructure has been observed actively abusing more than 16 trusted brands, collectively targeting Indonesia’s broader population of approximately 287 million," Group-IB said.