---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:14:00.199313+00:00'
exported_at: '2026-11-15T07:14:01.554378+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html
structured_data:
  about: []
  author: ''
  description: FBI says North Korea-linked FaceStealer stole over $400 million in
    crypto using fake video calls; U.S. authorities seized its infrastructure.
  headline: FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using
    Deepfake Video Calls
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using Deepfake
  Video Calls
updated_at: '2026-11-15T07:14:00.199313+00:00'
url_hash: c6e1d6a772717416facf3ae1dbb05fd43d6efc89
---

The U.S. Federal Bureau of Investigation (FBI) has established that threat actors tied to the Democratic People's Republic of Korea (DPRK aka North Korea) have stolen more than $400 million worth of cryptocurrency as part of a social engineering scheme codenamed
**FaceStealer**
in the last 18 months.

As part of a coordinated set of actions announced by the U.S. government, the cloud-based infrastructure used to pull off the
["hard-to-detect" campaign](https://www.fbi.gov/investigate/cyber/facestealer-cryptocurrency-theft-scheme)
has been seized.

In tandem, the U.S. Department of Justice (DoJ) has announced the court-authorized seizure and restraint of more than $1.2 billion worth of cryptocurrency recently
[stolen](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html)
by the North Korea-linked TraderTraitor actors following the hack of cryptocurrency exchange Binance. The plundered digital assets are used to fund Pyongyang's illicit weapons program, the DoJ added.

"The North Korean regime relies on proceeds from large-scale cryptocurrency theft to fund its illicit weapons program, stealing billions of dollars in recent years,"
[said](https://www.justice.gov/opa/pr/justice-department-announces-actions-disrupt-north-koreas-massive-theft-cryptocurrency)
FBI Cyber Branch Operations Director Brett Leatherman in a statement.

"North Korean cyber actors have used the FaceStealer scheme to aggressively target individuals in the cryptocurrency and Web3 sectors through deceptive social engineering tactics, resulting in the theft of more than $400 million in the last 18 months."

According to the Justice Department, FaceStealer relies on surreptitiously recorded videos and deepfakes to facilitate cryptocurrency theft. Some aspects of the activity dovetail with a campaign documented by Kaspersky under the name
[GhostCall](https://thehackernews.com/2025/10/researchers-expose-ghostcall-and.html)
in October 2025.

The activity is linked to a prolific North Korea-linked
[financially motivated](https://thehackernews.com/2026/02/dprk-operatives-impersonate.html)
threat cluster
[tracked](https://thehackernews.com/2026/04/drift-loses-285-million-in-durable.html)
as
**[BlueNoroff](https://www.picussecurity.com/resource/blog/bluenoroff-group-the-financial-cybercrime-arm-of-lazarus)**
, which is also known by the cryptonyms APT38, CageyChameleon, CryptoCore, DangerousPassword, Nickel Gladstone, Sapphire Sleet, Stardust Chollima, and UNC1069.

The campaign involves luring targets with invitations to video meetings delivered from stolen accounts belonging to prior victims. Targets who join the meeting have their video stream recorded, while simultaneously serving an authentic, prerecorded webcam video of a previous victim or victims known to the target to build trust.

"The North Korean hackers also use super intelligence (SI) to develop deepfake videos of well-known and influential individuals often in the cryptocurrency and web3 industries that make the FaceStealer scheme even more effective," the DoJ said. "Here again, they use the deepfake videos in the meetings with targets to gain the target's trust."

A few seconds into the meeting, a mock technical error is presented to the victim, claiming that they cannot be heard, and they are provided a link to address the non-existent issue. The fix is a ClickFix-style lure that's designed to install malware on the victim's workstation and steal cryptocurrency, as well as abuse the target's privileges to other computer infrastructure.

In an extensive report shared with The Hacker News in July 2026, JUMPSEC
[revealed](https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html)
how the social engineering operation is built atop a phishing kit designed to impersonate videoconferencing platforms like Zoom and Microsoft Teams. The cybersecurity company has characterized FaceStealer as a victim acquisition platform that involves using compromised trusted contacts as a pathway to fuel a self-propagating attack chain via Telegram.

This includes hijacking social media and communications accounts such as Telegram, LinkedIn, Slack, and Discord for extended periods of time, and then accessing the victim's contact list to target the victim's personal and professional circles.

The
[entire attack](https://www.ic3.gov/CSA/2026/261112.pdf)
plays out as follows -

* **Compromise a victim:**
  This involves harvesting cryptocurrency wallets, seed phrases, and other valuable access; hijacking their Telegram account or other communication app and locking them out; gaining access to their contacts and chat histories; and secretly recording them during the video chat.
* **Exploit the victim's Telegram account:**
  The attacker impersonates the victim and sends tailored messages to other contacts on their behalf, proposing a Zoom or Teams meeting under the pretext of discussing an investment opportunity.
* **Set up the meeting:**
  Should the target express interest, the attacker sends a Calendly invite via Telegram to schedule the video meeting. Shortly before the scheduled meeting time, the victim's Telegram account is used to send a typosquatted link that masquerades as a meeting URL for Zoom ("uu01webzoom[.]us") or Teams ("teams.livemeet[.]us").
* **Exploit recorded videos:**
  When the target joins the fake Zoom meeting, the attacker plays an already recorded webcam video of the trusted contact and plays other videos, either recorded or deepfake videos, to give the impression that there are multiple participants in the meeting. In addition, headshot images generated using OpenAI ChatGPT are used as static avatar placeholders on the fake calls.
* **Trick the target into infecting themselves:**
  The attacker sends a message to the target, claiming there is an audio issue or some other technical error (e.g., a deprecated Zoom SDK), and urges them to click on a link to apply an update to address the problem. Alternatively, it can take the form of running a script or copying and pasting malicious code into the command line or Terminal. This results in the deployment of malware that can capture sensitive data from the compromised device, effectively turning the target into the next victim.
* **Repeat the cycle:**
  With the victim now compromised, the attacker gains control of their device and social media accounts to propagate the attack to their contacts.

Attacks mounted by BlueNoroff are known to specifically single out individuals working in the cryptocurrency and Web3 industries, along with individuals involved in the development and maintenance of open-source software.

The goal is to obtain access to the developers' devices and the software repository accounts they control to facilitate software supply chain attacks. Notably, the FaceStealer scheme was put to use in
[targeting](https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html)
the maintainer of the popular Axios npm package earlier this year to push a trojanized version that
[delivered](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)
a cross-platform remote access trojan (RAT).

More than 900 victim webcam video recordings used by the threat actors to impersonate victims in follow-on attacks have been seized by the FBI. The agency said it's "aware of several other attempts by North Korean hackers to target software developers, maintainers, and software libraries with significant download volume."

In a report published in April 2026, Arctic Wolf said the targeted social engineering campaign had targeted over 400 victims across more than 20 countries, with most of them concentrated in the U.S., Singapore, the U.K., Hong Kong, South Korea, and the U.A.E.

|  |
| --- |
|  |
| Deepfake video production pipeline (credit: Arctic Wolf) |

"A full 80% of identified targets operate directly in cryptocurrency/blockchain finance (54%) or adjacent finance and investment sectors (26%)," the cybersecurity company
[noted](https://arcticwolf.com/resources/blog/bluenoroff-uses-clickfix-fileless-powershell-and-ai-generated-zoom-meetings-to-target-web3-sector/)
at the time. "CEOs and founders alone account for 45% of the target set – nearly half. This underscores BlueNoroff's singular operational focus: individuals with access to cryptocurrency assets, wallet infrastructure, exchange platforms, or investment decision-making authority."

The activity has since expanded in scope, with 677 targets identified across 58 countries. More than 80% of the targets are founders and C-suite executives. Besides introducing new lure themes such as a fake Chrome PDF Viewer update, the campaign incorporates generative AI technology from ChatGPT, Google, SpaceXAI Grok, and Wondershare AI Content Generator (AIGC) to supply the attackers with artwork, avatars, and convincing synthetic participant videos.

"Upstream, reconnaissance has both widened and become more deliberate," the company
[added](https://arcticwolf.com/resources/blog/still-in-the-meeting-bluenoroff-six-months-on/)
. "Lure material has been scraped not just from profile photos and prior victims' webcam streams, but from YouTube interviews and conference talks, which are screen-recorded by the actor. This allows them to capture a specific person's likeness and voice – a founder perhaps, or a CEO – and then create fake meeting footage without having to directly compromise the target themselves."

|  |
| --- |
|  |
| BlueNoroff's updated attack flow (credit: Arctic Wolf) |

Each new victim offers a pathway to further the attack. The cyclic modus operandi still remains the beating heart of the social engineering operation.

"Combined with their new fake media generation capabilities to produce varied and credible lure content, this presents a significant escalation in BlueNoroff's efforts to compromise high-value individuals who control funds, signing keys, sensitive information, authenticated communications, and trusted professional relationships," Arctic Wolf said.

### From FaceStealer to Contagious Interview

It's worth emphasizing here that the FaceStealer campaign is distinct from
[ClickFake Interview](https://thehackernews.com/2025/04/lazarus-group-targets-job-seekers-with.html)
, an iteration of
[Contagious Interview](https://thehackernews.com/2026/09/contagious-interview-campaign.html)
that also employs ClickFix-style tactics to trigger the execution of malware as part of recruitment-themed campaigns.

Like FaceStealer, this involves the attackers approaching prospective targets by posing as recruiters on platforms like LinkedIn and sharing a "technical assessment" designed to run malware. In a post shared on LinkedIn, Alina Krasavina, an engineering manager at Delivery Hero, detailed how she was targeted in October 2026 by two fake recruiters on the same day, 13 minutes apart.

"The first one sent a 'technical assessment': a Next.js project of 113 files. At the end of next.config.js, after 204 spaces, there was a backdoor," Krasavina
[said](https://www.linkedin.com/pulse/we-trained-engineers-run-strangers-code-alina-krasavina-8fy2f/)
. "The second one didn't send any ZIP. On a video call, a 'Member of Technical Staff' asked me to share my whole screen, download a repo, and run it. When I said no, he told me it was 'a requirement to continue.' After the call, I wrote to the recruiter and asked for another interview format. About a minute later she blocked me."

"The two attacks were built in opposite ways. The first one put the effort into the code and almost none into the recruiter. The second one put it into the people, and I never even saw its code."

According to a joint cybersecurity advisory published by cybersecurity and intelligence agencies from Japan, the U.S., Australia, and Germany in late September 2026, the long-running campaign is estimated to have compromised at least 30,000 devices located in 100 countries.

The attacks experiment with multiple delivery methods to convince victims to run malicious code -

Last month, Sophos disclosed that an employee's corporate macOS device had been compromised in mid-September 2026 after they cloned a public code repository presented as a job interview coding assignment and opened it as a workspace in VS Code.

"The repository contained a weaponized VS Code workspace settings file that replaced the editor's integrated terminal profile," the cybersecurity company
[said](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)
. "When a terminal opened in the workspace, the modified profile silently downloaded and ran a multi-stage payload."

The payload in question is BeaverTail, a JavaScript loader that's used to deliver a Python backdoor referred to as InvisibleFerret. Both malware families are
[attributed](https://thehackernews.com/2023/11/north-korean-hackers-pose-as-job.html)
to Contagious Interview.

Sophos said the malware ran in memory on the device for about 26 hours, right from its execution on September 14, 2026, until it was rebooted a day later. The incident did not affect any of its products or services, or customer data or their systems, it added.

What's more, recent research from JFrog has
[uncovered](https://research.jfrog.com/post/accurasofthire-fake-interview/)
that the threat actors linked to the campaign have even set up a decoy company named AccuraSoftHire, complete with a careers site, client testimonials, a LinkedIn page, job ads on mainstream boards, and verified recruiters in an attempt to lend credibility and ultimately deceive candidates into running malware through a rigged take-home test and a video verification step.

"Our research shows these lures are built to pass the checks people rely on: a professional website, a LinkedIn page, job ads on mainstream boards and recruiters with LinkedIn's verified badge," Guy Korolevski, senior security researcher at JFrog Security Research, said in a statement shared with The Hacker News.

"Developers and other employees with system access can't be expected to catch that on their own, so employers need to set the rules. Interview assignments with downloads should only ever run in a disposable virtual machine, never on a work laptop. Security teams should also warn employees about downloading unknown files, even from a source they think they can trust. Developers can also check when a recruiter’s profile was created and whether the company's location is the same on every page."

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.