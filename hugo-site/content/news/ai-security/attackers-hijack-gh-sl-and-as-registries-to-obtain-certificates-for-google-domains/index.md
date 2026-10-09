---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T01:03:54.033009+00:00'
exported_at: '2026-10-08T01:03:55.972103+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html
structured_data:
  about: []
  author: ''
  description: Attackers hijacked .gh, .sl, and .as registries and obtained 12 unauthorized
    certificates for Google and YouTube domains.
  headline: Attackers Hijack .gh, .sl, and .as Registries to Obtain Certificates for
    Google Domains
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attackers Hijack .gh, .sl, and .as Registries to Obtain Certificates for Google
  Domains
updated_at: '2026-10-08T01:03:54.033009+00:00'
url_hash: b9f5e1afc2dd31df6a62ebd1e3587bd93b17f538
---

Attackers compromised three country-code top-level domains (ccTLDs) and obtained unauthorized HTTPS certificates for several Google domains, Google
[said on October 6](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)
.

Google's own systems were not breached, but any domain ending in .gh (Ghana), .sl (Sierra Leone) or .as (American Samoa) was put at risk. With such a certificate, an attacker could pose as the real site over an encrypted connection and read the private data sent to it.

Chrome blocked the unauthorized certificates for Google's domains through
[CRLSets](https://www.chromium.org/Home/chromium-security/crlsets/)
, its way of quickly blocking certificates in emergencies, Google said. The company also worked with the certificate authorities (CAs) that issued the certificates to have them revoked, a step meant to protect people using other browsers and apps.

Google did not name the domains.
[Certificate Transparency](https://certificate.transparency.dev/howctworks/)
(CT) logs are the public record of certificates issued by CAs. They show at least 12 certificates issued between September 22 and 27 for Google and YouTube names under the three ccTLDs, including google.com.gh, google.sl and google.as.

A CA issues a certificate once the applicant shows control of the domain, for example by adding a record to the domain's DNS. The attackers changed authoritative DNS records during the hijacks, and Google has no reason to believe the CAs did anything wrong, the company said.

### What Certificate Logs Show

The Hacker News found the certificates on October 7 through two CT search services, ctlogs.dev and Cert Spotter. The 12 certificates are for seven domains. Let's Encrypt issued 11 of them and ZeroSSL issued one.

The certificates were recorded in the logs on three days, one ccTLD at a time: .gh on September 22, .sl on September 25, and .as on September 27.

All 12 are domain-validated certificates, issued after a check that the applicant controls the domain. In the records reviewed, which go back to at least September 10, every other certificate for google.com.gh, google.sl and google.as came from Google Trust Services, Google's own CA.

"Yes, certificates for Google and YouTube were issued, and have been revoked," Matthew McPherrin, a Let's Encrypt staff member,
[wrote on the CA's community forum](https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941/2)
on October 7, in reply to a user who asked whether Let's Encrypt certificates were issued during the hijacks.

Only a small set of Google and YouTube names was searched, so the total may be higher. Google said CT data also pointed to other organizations it believes were hit by the same attacks, including well-known global brands and widely used online services. It did not name them.

| # | Names on Certificate | Issuer | First Logged | Revoked |
| --- | --- | --- | --- | --- |
| 1 | `*.youtube.com.gh` , `youtube.com.gh` | Let's Encrypt | Sep 22, 11:03 | Sep 26, 02:41 |
| 2 | `*.google.com.gh` , `google.com.gh` | Let's Encrypt | Sep 22, 11:59 | Sep 26, 02:41 |
| 3 | `*.google.sl` , `google.sl` | Let's Encrypt | Sep 25, 04:36 | Oct 1, 19:36 |
| 4 | `google.sl` , `www.google.sl` | Let's Encrypt | Sep 25, 04:36 | Oct 1, 19:36 |
| 5 | `google.com.sl` , `www.google.com.sl` | ZeroSSL | Sep 25, 04:51 | Sep 26, 14:56 |
| 6 | `*.google.com.sl` , `google.com.sl` | Let's Encrypt | Sep 25, 04:51 | Oct 1, 19:36 |
| 7 | `www.youtube.sl` , `youtube.sl` | Let's Encrypt | Sep 25, 06:06 | Oct 1, 19:36 |
| 8 | `*.youtube.sl` , `youtube.sl` | Let's Encrypt | Sep 25, 06:07 | Oct 1, 19:36 |
| 9 | `google.as` , `www.google.as` | Let's Encrypt | Sep 27, 03:33 | Oct 1, 19:18 |
| 10 | `*.google.as` , `google.as` | Let's Encrypt | Sep 27, 03:43 | Oct 1, 19:18 |
| 11 | `google.as` , `www.google.as` | Let's Encrypt | Sep 27, 04:17 | Oct 1, 19:18 |
| 12 | `*.youtube.as` , `youtube.as` | Let's Encrypt | Sep 27, 04:37 | Oct 1, 19:18 |

### What the Response Covers

On October 7, Cert Spotter's records showed all 12 certificates as revoked. The two .gh certificates and the ZeroSSL certificate were revoked on September 26, and the other nine on October 1.

The shortest gap between a certificate's first log entry and its revocation was about a day and a half. The longest was nearly a week. The first .as certificate was recorded on September 27, about a day after the .gh certificates were revoked.

Google said it learned of the hijacks the week before its October 6 post and acted immediately. It did not give dates for the hijacks or for its own actions.

Google also blocked in Chrome the certificates it found for other organizations, and it contacted those organizations where it could.

Chrome users do not need to do anything, Google said. Domain owners should not rely on the browser to protect their users.

Because DNS hijacks are complex, "we cannot guarantee that our analysis identified every affected domain," the Chrome Secure Web and Networking Team wrote, adding that Chrome's blocks do not reliably protect people who use other browsers.

Google's post does not say whether any of the certificates was used to pose as a Google site or read users' data. It does not name the attackers, say how the ccTLDs were compromised, or say whether they have been secured.

### What Domain Owners Should Do

Google gave domain owners two steps to take. The rules that CAs follow allow a third.

* Watch CT logs for every domain you own, including parked domains and regional ccTLD names.
  [CT monitoring services](https://certificate.transparency.dev/monitors/)
  send an alert when a certificate is issued for a domain. Anyone who runs a domain under .gh, .sl or .as should review recent log entries for certificates they did not request.
* Publish a strict
  [CAA record](https://datatracker.ietf.org/doc/html/rfc8659)
  . A CAA record is a DNS record that names the CAs allowed to issue certificates for a domain, and a CA must check it before issuing. Google recommends
  [tying the record to your own account](https://www.rfc-editor.org/rfc/rfc8657.html)
  at the CA, which works only if the CA supports that option.
* Report a certificate you did not request to the CA that issued it. Under the
  [Baseline Requirements](https://cabforum.org/working-groups/server/baseline-requirements/documents/CA-Browser-Forum-TLS-BR-2.3.1.pdf)
  that CAs follow, anyone can file a Certificate Problem Report, and the CA must investigate and report its first findings within 24 hours.

A CAA record cannot stop a certificate from being issued while a DNS hijack is under way. An attacker who can remove the record or insert a false one could still get a certificate, the CAA standard says.

The record matters once the owner has control of DNS again. CAs are allowed to reuse a completed domain check for later certificates, so an attacker who passed the check during a hijack could request more certificates after it ends, Google said. A strict CAA record blocks that.

The Baseline Requirements let a CA reuse a domain check for up to 200 days. The limit falls to 100 days in March 2027 and to 10 days in March 2029, under a schedule that the CA/Browser Forum, a group of CAs and browser makers,
[approved in April 2025](https://thehackernews.com/2025/04/thn-weekly-recap-ios-zero-days-4chan.html)
.

Let's Encrypt, which issued 11 of the 12 certificates,
[said in December 2025](https://thehackernews.com/2025/12/threatsday-bulletin-wi-fi-hack-npm-worm.html)
that it reuses a domain check for 30 days and plans to cut that to 7 hours by 2028.

Each of the seven domains carried a strict CAA record on October 7. Google Public DNS returned a record naming only pki.goog, the domain of Google Trust Services, for every one of them.

### Certificate Fingerprints

Each certificate in the table can be looked up in a CT search service by its SHA-256 fingerprint. The numbers match the table rows.

1. **SHA-256**
   :
   `0357032e1214ae11d7da8e00f6b89fb7694e240b17d05f2f47feaf43e96aa7d8`
2. **SHA-256**
   :
   `8886ca2b71501a6729f1ae868bd7d7b9b53c5cb6b5c7d851d041db4d6206945d`
3. **SHA-256**
   :
   `986d36b1c68c3e800596c4680dd6c67c42118955e08b472f641793c59dcd347b`
4. **SHA-256**
   :
   `2e1f6d7f24650b0720636efe48f2ccf59704ee6f11ffa52b5a4c4afcc474fe91`
5. **SHA-256**
   :
   `e1667fe4e4ea98427960ea2eda7c53af1246ec58ac22282a6877d394a0957065`
6. **SHA-256**
   :
   `e1e4fd74f673f1df9c039ae6424b36868a0475a043abea2dedd1f6f12a365ebf`
7. **SHA-256**
   :
   `5b7c491c8784eb438b1634981f1ea6333d3557431268233c2a7a92173ca17122`
8. **SHA-256**
   :
   `a10d3b5dbc142d040e6ae772ab41dc44b0e94659237709d1241fdefdd36f7b35`
9. **SHA-256**
   :
   `491f453d208bbb7923626c208df93c95fdfae3b78b738b996c8dafda9d00619a`
10. **SHA-256**
    :
    `798079c762496d26ce99d3a9113cb24715e31ec8a69a6cdcffa70f5001e19df0`
11. **SHA-256**
    :
    `607afd2745b84c4332e028262937be35f25316aadf584340269d23a3dbcd37ef`
12. **SHA-256**
    :
    `b7ea8c77695cf9791a9d45f17c33ebb9bd5f68d4c96df6f56136dc6a834576d2`