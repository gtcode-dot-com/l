---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:19:51.085337+00:00'
exported_at: '2026-11-15T07:19:53.289161+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/silentair-hijacks-asian-telecom.html
structured_data:
  about: []
  author: ''
  description: SilentAir used compromised Asian telecom equipment to intercept calls,
    texts, and 2FA codes, targeting mainly Taiwan, Enea reports.
  headline: SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and
    Spy on Taiwanese Users
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/silentair-hijacks-asian-telecom.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and Spy
  on Taiwanese Users
updated_at: '2026-11-15T07:19:51.085337+00:00'
url_hash: d030547d1ad319e1be60b0b610578a4836330417
---

A newly identified spying group used hacked equipment inside Asian mobile operators to intercept the calls and texts of selected people, mostly in Taiwan.

**Enea**
, a telecom and cybersecurity software company based in Stockholm, found the group's attack sources in at least six Asian countries and named it SilentAir this week. It assessed with high confidence that
**SilentAir**
is a state-level actor, but linked its activity to China only with low confidence.

The company has told the operators where it found SilentAir sources. It said SilentAir has been disrupted for now but could return. The report does not say whether those operators have cleaned up the hacked equipment.

Mobile operators use the SS7 and Diameter protocols to exchange signaling messages that route calls and texts and enable roaming. This traffic crosses a shared network called the
**IPX**
, which runs on a high level of trust between operators. SilentAir sent its attacks into the IPX from the hacked equipment.

For interception, SilentAir sent the target's home network an UpdateLocation message, or its Diameter equivalent. The message claimed that the hacked equipment was now serving the target's phone. If the home network accepted it, calls and texts for that person would be diverted to the attackers.

Some of these attacks worked. For some targets, the company observed two-factor authentication (2FA) codes being intercepted immediately after the diversion took effect. That points to an attempt to break into other accounts registered to those people.

The report gives no similar evidence for voice calls, and it does not say whether any account was taken over.

Interception made up 18.3% of the attacks the company saw from SilentAir. For a typical surveillance company, the kind of firm behind most signaling attacks, the share was 2.1% in the company's earlier research.

Some targets were political and government VIPs in their own countries. In rare cases, SilentAir equipment in several countries worked together against such targets, which the company said points to a single controller.

The attacks came in bursts, from one or a few subscribers to several thousand over a month, with gaps of up to several months or longer between bursts.

Outside Taiwan, targets were mostly in other Southeast and East Asian networks, and at times in East Africa, Central Asia, the Middle East, and Europe. People using the hacked operators' own networks may also have been targeted, but the company could not see that traffic.

The company spotted SilentAir by studying attacks on the links between operators. Since early 2025, it has tracked unusual attacks, mostly over SS7 and sometimes Diameter, from some Asian operators that would not normally send attacks. Later analysis found suspicious activity even earlier.

The networks hosting SilentAir handled follow-up messages for diverted targets in odd and inconsistent ways, according to the company's
[technical report](https://www.enea.com/insights/the-enemy-within-tracking-liminal-panda-and-silentair-through-mobile-networks/)
. That left two explanations: someone outside was faking those networks' signaling addresses, or equipment inside each network had been taken over.

The company then saw equipment inside one operator both send and receive attack commands, which confirmed the second explanation. That equipment behaved exactly like SilentAir sources in other networks.

Detecting and blocking the attacks was hard at first because the attackers understood mobile networks and signaling defenses well. After the attacks were contained, the company recovered traces of unauthorized access. It could not analyze the malware it believes SilentAir used.

The report does not name the countries, the operators, or any of the targets. In some countries, SilentAir attacks came from more than one operator.

SilentAir also sent silent SMS on a very large scale, mainly to subscribers in Taiwan. These are texts that the phone does not display or alert on.

During the day, most silent SMS went to subscribers on other networks, such as Southeast Asian networks. One of their main uses appears to have been checking whether a diversion had worked, the company said.

If the test text reached the hacked equipment instead of the phone, the attackers knew they were getting that person's texts.

Most silent SMS went out at night, and most of those went to people in Taiwan. The company said the purpose of those messages is not confirmed. They may be a bulk check that earlier diversions were still in place, since phones are least likely to re-register to their real location at night.

The silent texts carried spam-like motivational or promotional lines, often in English. The company believes the text was a disguise. If an operator along the way stripped a message's silent setting, the recipient would see it as spam and ignore it.

The company's low-confidence link to China rests on several signs. SilentAir focused on Taiwan and did not target Chinese networks or subscribers.

Its tracking and interception attacks also followed a working day in UTC+8, which is China Standard Time. They started at 9 a.m., almost stopped on weekends, and paused or slowed around Chinese holidays.

The company also considered a link to
**Liminal Panda**
, a group behind
[earlier telecom intrusions](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html)
. It called the link possible but unconfirmed and does not tie the two groups together for now.

In several hacked operators, SilentAir attacks happened during a known Liminal Panda infection. At other times, the two showed no sign of working together. They also went after operators in the same part of Asia, though Liminal Panda has no known focus on Taiwan.

SilentAir's behavior also partly matches that of SCTPE, a little-known Linux trojan that runs in the kernel and is designed to send and receive SS7 and Diameter traffic.

Singapore's Infocomm Media Development Authority (IMDA) has described the same tool in a
[government advisory](https://www.imda.gov.sg/assets/23f23bba-57ca-42b6-92f8-90e207bf8c46.pdf)
. There, the tool is called
**SIGweaver**
. The agency said CrowdStrike identified it on January 21 and links it to Liminal Panda with moderate confidence.

But Enea said SilentAir answered messages it had not sent itself, which the known SCTPE program cannot do. SilentAir's operational security also seemed far better than Liminal Panda's.

Separately, the company's GTP firewall has detected Liminal Panda activity at several customer operators since the first quarter of this year. The company blocked the group's GTPDoor traffic there and saw Liminal Panda infections, or strong signs of them, in at least 5 to 10 operators.

The
[GTPDoor backdoor](https://thehackernews.com/2024/02/gtpdoor-linux-malware-targets-telecoms.html)
, first documented on February 27, 2024, hides commands within GTP-C, the protocol that establishes mobile data connections between networks. The company also found evidence of a new version that hides commands in GTP-U, the part of GTP that carries users' data. GTP-U traffic is harder to inspect, though the company believes the new version serves mainly as a backup.

### What Enea Recommends for Operators

The company said any attacker could reuse these techniques, and it told operators to:

* Deploy GTP-C and GTP-U firewalls and configure them to share information with their SS7 and Diameter firewalls.
* Go beyond the industry's basic recommendations for signaling security.
* Treat the whole IPX as untrusted.
* Add detection for signaling protocols inside their own networks.
* Connect signaling security with the rest of their IT security.

The report does not advise people whose calls and texts may be targeted.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.