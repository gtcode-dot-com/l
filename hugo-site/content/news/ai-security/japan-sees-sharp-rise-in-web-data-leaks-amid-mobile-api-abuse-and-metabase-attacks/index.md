---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T19:08:04.448570+00:00'
exported_at: '2026-10-08T19:08:05.837014+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/japan-sees-sharp-rise-in-web-data-leaks.html
structured_data:
  about: []
  author: ''
  description: JPCERT/CC links Japan's recent data leaks to mobile API abuse and known
    software flaws, including an exploited Metabase SQL injection bug.
  headline: Japan Sees Sharp Rise in Web Data Leaks Amid Mobile API Abuse and Metabase
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/japan-sees-sharp-rise-in-web-data-leaks.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Japan Sees Sharp Rise in Web Data Leaks Amid Mobile API Abuse and Metabase
  Attacks
updated_at: '2026-10-08T19:08:04.448570+00:00'
url_hash: e23311ff0ce108d3497a0b0d3a25d4a13c96ea47
---

Attackers behind a string of personal data leaks at Japanese organizations have abused APIs for mobile apps and targeted known software flaws, the JPCERT Coordination Center (JPCERT/CC) said.

The Tokyo-based center, which takes incident reports, based its
[October 8, 2026 alert](https://www.jpcert.or.jp/at/2026/at260030.html)
on those reports and other information. The alert names no attacker and no affected organization.

JPCERT/CC called what it knows "limited and fragmentary" in the alert, translated here from Japanese. It said its account does not mean the same method was used in every incident.

Besides consumer apps, the systems hit include business intelligence (BI) tools and employee-facing management systems that their operators did not expect the public to reach. Data stored in them leaked in some cases.

For defenders, the alert includes eight source IP addresses, five User-Agent strings, and a list of API controls, including access controls on every endpoint, public or not.

The only product it names as a target is
**Metabase**
, a BI tool with a known flaw that attackers have exploited. Metabase has urged users to upgrade to at least the
[minimum safe releases](https://www.metabase.com/blog/security-focused-release-announcement-2026-08-12)
in a list last updated August 14. Those releases are newer than the first fix for that flaw.

The leaks have come one after another around September 2026. The attacks behind them are separate from ransomware and other routine incidents, lead to leaks of large amounts of personal data, and may be increasing, JPCERT/CC said.

JPCERT/CC gave no count. One comes from the Security Research Center of Japanese company Macnica, in an
[analysis published October 7](https://security.macnica.co.jp/blog/2026/10/web-incidents2026.html)
that the alert cites.

Macnica counted 119 incidents made public this year through October 6 in which personal data was stolen or leaked through web systems run by organizations in Japan. It counted 84 in all of 2025 and 62 in 2024, and 81 of this year's 119 came in July or later.

The count covers only incidents that Macnica judged similar to the current series. It leaves out ransomware and cases Macnica ties to other attack groups. Of the 81 made public since July, 65 gave too little detail to tell how the attackers got in.

The targets have spread from online shops to member services, business systems and customer support. Recent cases include a library's catalog search and a tourist train's seat booking system.

Two cases show the scale. Park24 said on September 28 that a third party obtained data on
[about 6.6 million accounts](https://www.park24.co.jp/news/2026/09/20260928-1.html)
from the web system of its Times Car car-sharing service. A day later, it said
[that identity documents](https://www.park24.co.jp/news/2026/09/20260929-1.html)
, such as driver's license images, had leaked from about 1.6 million accounts.

Monogatari Corporation, which runs the Yakiniku King restaurant chain, said 10,788,963 records leaked from the member system of its Yakiniku King app,
[INTERNET Watch reported](https://internet.watch.impress.co.jp/docs/news/2145813.html)
on October 5. Both companies said at the time that the cause was still under investigation.

Macnica also found 99 similar cases in 13 other countries and regions, mostly from July to September, including 30 in South Korea, 11 in France and 8 in Poland. It does not know whether Japan is the only target, and said disclosure laws and practices differ by country.

### How the Attackers Get In

JPCERT/CC's alert describes three patterns. The first is unauthorized requests to the management APIs behind an app. In some cases, those requests rewrote information.

JPCERT/CC has received multiple reports of three ways attackers do this:

* They analyze a publicly released smartphone app to find its API endpoints and keys.
* They attack internal APIs that cannot be used through the app's screens. Reported actions include changing a user's privileges, creating unauthorized accounts, comparing how the server answers when a header is added or removed or a malformed authentication token is sent, and finding account details through blind NoSQL injection.
* They use API keys stolen when another system was compromised.

Macnica's post reports the same method, in a part based on incident response and log analysis. In some cases, attackers took API keys from a smartphone app and called the API in a way that looked like normal use.

The attackers search each site and its APIs for any flaw that allows them to obtain data. The flaws include APIs that return more data than necessary, APIs with excessive privileges, member functions accessible to anonymous users, logic errors, and session management faults.

Attacks on weak admin-screen passwords and exploitation of known flaws were also confirmed in some cases.

The second pattern is a possibility JPCERT/CC raises. Instead of relying on a single flaw shared by all targets, attackers may scan each target for a range of known flaws and attempt to exploit them. They may also be trying attacks that exploit poor system management, such as stealing configuration and backup files.

### The Metabase Flaw and Which Versions to Run

The third pattern is exploitation of
[CVE-2026-72898](https://nvd.nist.gov/vuln/detail/CVE-2026-72898)
, an SQL injection flaw in Metabase, an open-source BI tool that companies connect to their databases.

The flaw was
[exploited as a zero-day](https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html)
against Metabase's own cloud service, the company said on August 6. It carries a CVSS score of 10.0. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added it to its Known Exploited Vulnerabilities catalog on August 11.

An attacker needs no account to exploit it. The flaw allows SQL injection into Metabase's own application database, which can give administrator access. From there, the attacker could steal the stored credentials for connected databases and read or export their data.

JPCERT/CC
[warned about the flaw](https://www.jpcert.or.jp/at/2026/at260023.html)
on August 14. Its new alert adds three source IP addresses that were abused from early August to early September, as well as two User-Agent examples. The alert does not say which organizations the requests from those addresses hit.

Attacks continued after the fix was out.
[AhaSlides said](https://ahaslides.com/ja/blog/security-incident-notice-september-2026/)
a third party exploited the flaw in its Metabase and had access from August 12 to September 7.

Metabase's
[August 6 security update](https://www.metabase.com/blog/security-update-6-aug-2026)
fixed CVE-2026-72898. The company published
[another critical advisory](https://github.com/metabase/metabase/security/advisories/GHSA-r495-55cx-fjh7)
on August 11, covering issues it says it found itself. It then raised the
[lowest release it calls safe](https://www.metabase.com/blog/security-focused-release-announcement-2026-08-12)
for each version.

The table shows both for the open-source builds. Metabase numbers the enterprise builds of the August 6 fixes 1.x instead of 0.x.

| Version | Release That Fixes CVE-2026-72898 | Metabase's Minimum Safe Release |
| --- | --- | --- |
| 63 | 0.63.5 | 0.63.13 |
| 62 | 0.62.9 | 0.62.16 |
| 61 | 0.61.11 | 0.61.18 |
| 60 | 0.60.17 | 0.60.24 |
| 59 | 0.59.21 | 0.59.28 |
| 58 | 0.58.24 | 0.58.31 |

Versions below 58 are not affected by CVE-2026-72898, and Metabase has already patched its cloud service.

Operators who cannot upgrade yet can block the /api/session/reset\_password endpoint as a temporary measure. Metabase gives that workaround for CVE-2026-72898. The August 11 advisory tells users to upgrade.

A server is likely compromised if its logs show a POST /api/session/reset\_password request that returned 400, followed by a GET /api/user/current request that returned 200, Metabase said.

Where the reset endpoint was reachable from the internet, Metabase lists six steps to take after upgrading:

1. Revoke all active user sessions.
2. Review API keys and delete any you do not recognize.
3. Review administrator accounts for unexpected changes.
4. Rotate the credentials for every connected database.
5. Review data warehouse logs for signs of unauthorized access.
6. Review Metabase activity and query history for unexpected activity.

### What Is Not Established

Neither JPCERT/CC nor Macnica names the person or group behind the activity or says one group is responsible.

In Macnica's assessment, the attackers try any public web system that holds personal data, regardless of who runs it. They may be reusing a method that worked on one target against others, and in some cases share source IP addresses.

No use of AI-discovered zero-day flaws in common software has been confirmed so far.

"What is actually happening is activity that broadly probes for and exploits more basic flaws in areas such as access permissions, configuration and authentication, as well as known vulnerabilities," the Macnica post said, in a translation from Japanese.

No logs or traces prove that AI was used. The post's author still thinks AI use is hard to rule out, because checking this many sites by hand is not realistic.

Neither account says which public breach used which method, because neither names an affected organization.

### Indicators and Checks

JPCERT/CC published the source addresses and User-Agent examples below. The addresses were abused in the periods shown and may be in normal use now.

**API abuse, around September 2026**

* **IP**
  : 3.112.252[.]14
* **IP**
  : 54.95.112[.]6
* **IP**
  : 69.10.51[.]162
* **IP**
  : 172.86.91[.]7
* **IP**
  : 210.149.87[.]120
* **User-Agent**
  : curl/7.88.1
* **User-Agent**
  : python-requests/2.34.2
* **User-Agent**
  : Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36

**Metabase exploitation, early August to early September 2026**

* **IP**
  : 213.163.202[.]171
* **IP**
  : 221.216.140[.]49
* **IP**
  : 221.216.140[.]129
* **User-Agent**
  : python-requests/2.33.1
* **User-Agent**
  : Metabase-GHSA-vwf4/2.0

Macnica lists 210.149.87[.]120 and 69.10.51[.]162 as the first to check. They may include VPN exit addresses that normal users share, so a request from one of them is not proof of an attack. Heavy traffic or many errors from them calls for a detailed log review.

For logs, Macnica suggests going back about a month and looking for:

* Heavy API traffic from a single IP address
* Sudden rises in error responses such as 403, 404, and 503
* Requests for files or API functions that do not exist
* Far more requests than usual, even when the server answers 200
* Use of admin functions that ordinary users are not allowed, or suspicious command execution
* Access to admin functions from unusual IP addresses
* High database load or heavy session use at the same time as a rise in traffic
* More errors in database logs
* More login attempts

For APIs, JPCERT/CC recommends six controls and points to OWASP guidance such as the
[OWASP API Security Top 10](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
for details:

* Limit the number of requests per unit of time to stop repeated and bulk calls.
* Set separate rate or usage limits on functions that are costly or easy to abuse, such as login, password reset, SMS sending, and search.
* Enforce access control on every API endpoint, including non-public ones, and accept only permitted users and HTTP methods.
* Give API users and tokens only the privileges they need.
* Set an expiry on API tokens and avoid long-lived ones.
* Be able to revoke quickly any token that is no longer needed or may have leaked.

Macnica adds two checks. Secret API keys and database credentials should not be built into a shipped app or browser code, because minifying or obfuscating the code does not hide them. Vulnerability tests should cover admin functions, which are often left out.

JPCERT/CC's general advice includes limiting access by region, where a service is used in one region, disabling unnecessary admin functions on the internet, and deleting data past its retention period.

The center said it will update the alert as it learns more about causes and methods.

### Privacy Regulator Issues Its Own Alert

Japan's Personal Information Protection Commission issued
[its own alert](https://www.ppc.go.jp/files/pdf/261007_alert_dataleakage.pdf)
on October 7 to businesses that handle personal data. It pointed to cases in which widely used services were hit by unauthorized access, with large volumes of personal data leaked or possibly leaked. It reminded businesses to check whether the personal data they hold is still needed.

The commission's
[guidance on leaks from unauthorized access](https://www.ppc.go.jp/files/pdf/261007_warning.pdf)
, revised the same day, includes a case study on API abuse. In it, an attacker logs in to a smartphone app or web service, rewrites request parameters, and gets other users' data.