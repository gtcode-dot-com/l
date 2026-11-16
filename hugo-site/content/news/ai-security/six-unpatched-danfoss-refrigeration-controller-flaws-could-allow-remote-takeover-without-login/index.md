---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-16T17:56:21.554847+00:00'
exported_at: '2026-11-16T17:56:22.804004+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html
structured_data:
  about: []
  author: ''
  description: Six unpatched flaws in Danfoss AK-SM800A controllers could enable unauthenticated
    takeover; agencies urge operators to remove internet access.
  headline: Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote
    Takeover Without Login
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover
  Without Login
updated_at: '2026-11-16T17:56:21.554847+00:00'
url_hash: 119c79e2a81706346f0c5edb7e024ea45e1f4c24
---

Six flaws in
**Danfoss AK-SM800A**
refrigeration controllers could let a remote attacker take over a controller without logging in, Dutch security consultancy Midnight Blue said earlier this week.

No patch is available, and the researchers say the newest firmware, version 5.4.0, does not fix the flaws.

Government cybersecurity agencies in Belgium, Ireland and Germany told operators this week to take the controllers' management interfaces off the internet.

For a controller left on the internet, updating the firmware, changing default passwords or turning on Strict mode is not enough on its own, the Belgian and Irish agencies said. Strict mode is a login protection that requires encrypted connections and session tokens, but one of the six flaws is in the gateway that enforces it.

The AK-SM800A runs a store's fridges and freezers, and maintenance firms can manage it remotely. Such controllers were targeted in
[attacks in France](https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html)
starting October 11, and in a
[second wave](https://thehackernews.com/2026/11/second-wave-of-cyberattacks-hits.html)
across Europe that began last week. The attacks caused unwanted defrost cycles and destroyed stock.

Germany's federal IT security agency, the BSI, says in a
[security notice](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-306525-1032.pdf?__blob=publicationFile&amp;v=2)
that the AK-SM800A was involved in earlier incidents in which refrigeration units in several countries were tampered with.

The agency has no information about any exploitation of the six new flaws, and neither other agencies nor researchers link the flaws to those incidents.

The researchers examined firmware version 5.3.2, then the newest, and say every version up to and including it is affected.

No CVE identifiers have been assigned. The researchers are keeping technical details private while they work on disclosure with Danfoss, the Danish company that makes the controllers.

The vendor lists software package 5.4.0, dated November, as its newest release for the AK-SM800A. Its
[5.4.0 readme](https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/license-agreement/)
and November update guide cover upgrade steps, and the guide adds a stricter password rule. Neither mentions a fix for any vulnerability.

In a
[follow-up statement](https://www.coolingpost.com/world-news/belgium-warns-of-new-danfoss-controller-vulnerabilities/)
carried by trade publication Cooling Post, the researchers said 5.4.0 does not patch the flaws: "It's not really possible either because according to the file timestamp this firmware was likely built on October 29, before the second wave of cyber attacks and well before our vulnerability reports."

The German agency first said in a press release this week that 5.4.0 was not affected. Later the same day, it changed that in a
[corrected statement](https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/261113_Kuehlgeraete-Danfoss.html)
: it cannot rule out for now that 5.4.0 is affected.

The vendor's
[advisory page](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/)
lists no advisory for the six flaws as of today, and no date for a fix has been published.

Midnight Blue researcher Carlo Meijer found the six flaws in less than an hour of manual review, using firmware the vendor offers for download, and described them in a
[technical write-up](https://www.midnightblue.nl/blog/multiple-rce-danfoss-aksm800a)
.

Five of the flaws are in web request handlers that do not require a login, inside a program that runs as root. Through one of them, the researchers ran code as root on older firmware, version 3.3.0, and they found the same bugs in 5.3.2.

Strict mode closes almost all of the controller's web attack surface to users who have not logged in, including the flaw used in that demonstration. The sixth flaw is in the gateway that enforces Strict mode, a separate program that blocks every request except the login until a user has logged in.

When the researchers ran firmware 5.3.2 in an emulator with Strict mode on, that flaw crashed the gateway. The crash could be turned into code execution with more work, the researchers say, and the gateway lacks basic exploit defenses such as stack canaries.

With code running as root, an attacker could change the controller's settings, start defrost cycles and hide that activity from its logs.

The controllers do not use secure boot, the researchers found, so an attacker could plant code that survives a factory reset and a firmware update. An attacker could also make a controller unusable until it is replaced.

The researchers say the code almost certainly holds more flaws like these, and they call patching flaws one by one or turning on Strict mode "a misallocation of scarce security and personnel resources."

### What Operators Can Do

Removing internet exposure must not wait for a patch, and it is needed even where firmware is current and Strict mode is on, the Centre for Cybersecurity Belgium says.

The
[Belgian advisory](https://ccb.belgium.be/advisories/warning-six-new-danfoss-vulnerabilities-refrigeration-controllers-risk-immediate-action)
and a similar
[Irish advisory](https://www.ncsc.gov.ie/pdfs/2611130306_New_Vulnerabilities_in_Refrigeration_Controllers.pdf)
recommend these steps:

* Find every controller whose management interface can be reached from the internet, including through a 4G or 5G modem, and remove that exposure.
* Give remote access only through a secure VPN or a protected internal network. Allowing only a service company's IP addresses through a firewall is a short-term measure.
* Check temperature setpoints, defrost schedules, alarm settings, user accounts and remote-access settings for changes you did not make.

The German agency adds that anyone who suspects a compromise should change all credentials and check that equipment connected to the controller works properly.

Before cutting off the data a controller sends to its refrigeration service company, operators should check contract and insurance terms, the Belgian advisory says. They should also set up protected remote access so that monitoring can continue.

Danfoss's own
[update guide](https://assets.danfoss.com/documents/latest/615405/BC576633631268en-000105.pdf)
says the AK-SM800A should not be directly reachable from the public internet, adding: “This recommendation applies to all software versions, including those with Strict Mode enabled.”

Ireland's National Cyber Security Centre also advises running the latest supported firmware, changing default passwords and turning on Strict mode, but says operators should not rely on those steps alone.

Danfoss told Cooling Post on October 12 that most units hit in France were either older models that no longer receive updates or current AK-SM800A units running outdated firmware.

The vendor fixed
[earlier flaws](https://thehackernews.com/2026/08/threatsday-gogs-100-rce-n8n-workflow-to.html)
in the AK-SM800A in 2023 and 2025, including login bypass and command injection bugs. Version 5.3.2, which the researchers examined, is newer than all of those fixes.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.