---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-08T05:29:42.791093+00:00'
exported_at: '2026-11-08T05:29:44.149922+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html
structured_data:
  about: []
  author: ''
  description: eMudhra plans to exit global SSL/TLS certificates after eight weak
    CA keys were recovered, as Chrome and Firefox withdraw trust in its ECC root.
  headline: eMudhra to Exit Global SSL/TLS Business After 8 Intermediate CA Keys Found
    Easily Guessable
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: eMudhra to Exit Global SSL/TLS Business After 8 Intermediate CA Keys Found
  Easily Guessable
updated_at: '2026-11-08T05:29:42.791093+00:00'
url_hash: f74ce17a74d9601f64ad9e367353a19f2b7c3b35
---

**eMudhra**
, an Indian certificate authority (CA), will withdraw from its global SSL/TLS certificate business,
[its board decided on Thursday](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business)
. The decision came five days after a researcher
[reported recovering the private keys](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html)
of eight of its intermediate CA certificates.

eMudhra said it will replace affected customers' certificates with free ones from partners, though its announcement did not name the partners or provide a date for the exit.

Six of those eight were for website (TLS) certificates. Chrome will stop trusting the eMudhra root certificate above them, emSign ECC Root CA - G3. The change is expected to reach users on the morning of October 27, Pacific time.

On October 20, Mozilla decided to stop trusting the same root in Firefox. Removing a root from a browser also cuts off legitimate certificates issued beneath it.

About 30,800 unexpired certificates chained to that root as of October 21,
[by Chrome's count](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c30)
of public Certificate Transparency (CT) logs. Of those, 99.9% were issued through InCommon, the certificate service Internet2 created for the higher education community. InCommon
[moved the service onto eMudhra's CertiNext platform](https://internet2.edu/incommon-round-up-may-2026)
between April and July this year.

Google has
[told website operators](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)
with certificates under that root that they "must immediately acquire and install a new TLS certificate from another PKI hierarchy included in the Chrome Root Store."

Until the transition is complete, eMudhra said, its G1 RSA root certificates will continue to serve customers. G1 is a separate hierarchy from the ECC root, but Chrome is still deciding whether to keep eMudhra's remaining CA certificates in its root store.

eMudhra will keep its revocation and status services running until every SSL/TLS certificate it issued has expired or been replaced. Its other businesses, including digital signature certificates, eSign and the CertiNext platform InCommon uses, will continue.

The announcement does not mention InCommon, or say whether eMudhra will keep issuing new certificates under G1 until it exits.

eMudhra said the global SSL/TLS business brings in about 1% of its revenue. Data sovereignty and compliance rules make it more complex and costly to run, and some large providers give the certificates away free.

The incident's spread on social media has also brought "scrutiny that is out of proportion to SSL/TLS’s place in our business," the company said.

The researcher reported the weak keys to Apple, Google, Microsoft, Mozilla and eMudhra on October 17. Each private key should have been a huge random number, but all eight were below 256, so anyone could work them out almost instantly.

Chrome and Firefox blocked the six TLS intermediates within hours. No website certificate from them had appeared in CT logs before Chrome's block, so none could have been used against Chrome or other software that requires CT logging, Google said.

eMudhra said it never used the eight to issue certificates to websites or users, and that its systems were not breached.

### What Certificate Holders Can Do

[Cornell has told its certificate holders](https://itservicealerts.hosting.cornell.edu/view/7882)
to request RSA certificates instead of ECC ones, because "RSA certificates use eMudhra's unaffected root and should work." The university counts more than 300 affected certificates of its own.

[The University of Michigan says](https://safecomputing.umich.edu/security-alerts/root-certificate-authorities-distrusted)
InCommon's RSA certificates are not currently affected, but that their root "could become distrusted, too." For now, its main alternative is Let's Encrypt.

eMudhra
[has estimated](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c19)
that about 30,000 certificates need to be moved, and that about 97% of them were issued using ACME, the protocol many servers use to request and renew certificates automatically.

Chrome has told eMudhra that standard ACME clients do not replace certificates outside their renewal window unless they support ACME Renewal Information (ARI) or someone steps in by hand. Moving from the ECC hierarchy to the RSA one may also need changes to client settings.

### Questions Over eMudhra's RSA Root

[Mozilla said on October 20](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c18)
that, for now, it was not removing trust in the G1 root, emSign Root CA - G1.
[At Stanford](https://uit.stanford.edu/service/ssl/emSign)
, InCommon certificates chain to that root through an eMudhra CA called emSign Root TLS CA - G1.

On October 14, eMudhra published a certificate revocation list (CRL) for emSign Root TLS CA - G1. A CRL is the signed list of certificates a CA has revoked. This one's signature does not verify against that CA's own key, the researcher who reported the weak keys
[said in Mozilla's public bug report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c7)
on the incident.

A participant in the same bug report
[said on October 22](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c34)
that the list appears to have been signed with the key of an eMudhra OCSP certificate. OCSP certificates sign answers about whether a certificate has been revoked. The participant wrote that the match "appears to be a case of using the wrong signing key, rather than evidence of another weak key."

Chrome raised the list on October 21, in one of 12 questions it posted to the bug report. It asked which key signed it, and whether eMudhra holds more than one key pair for that CA or for any of its roots.

Chrome also asked whether customers are moving to G1, to another company's CA, or both, and when all of them will have moved, given its planned October 27 removal. eMudhra said on October 20 that G1 was "the only alternative available," and
[the next day](https://emudhra.com/en/post/certificate-security-incident#update-3)
that it is issuing its affected US customers fresh certificates "from an alternate, independently operated, publicly trusted CA hierarchy."

In 2025, eMudhra published invalid CRLs for six of the same intermediates.
[Its incident report at the time](https://bugzilla.mozilla.org/show_bug.cgi?id=1970728#c2)
said it fixed them by "regenerating the CRLs using the appropriate private key associated with each Intermediate CA."

On October 19, eMudhra
[told Mozilla](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11)
that those lists were first signed with the keys it meant to use. When that produced invalid signatures, they were "resigned with flawed keys," the weak keys found this month.

Chrome said that disclosure "raises serious concerns regarding eMudhra's transparency and incident handling" during and after the 2025 incident. It asked why the 2025 report did not mention that two key pairs existed for each of those CAs.

As of 13:31 UTC on Thursday, eMudhra had not answered any of Chrome's questions publicly on the bug report. Its last visible comment there was posted on October 20.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.