---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-27T06:25:15.170215+00:00'
exported_at: '2026-02-27T06:25:18.604390+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/citizen-lab-finds-cellebrite-tool-used.html
structured_data:
  about: []
  author: ''
  description: Citizen Lab and Amnesty link Cellebrite extractions and Predator spyware
    to surveillance of activists and journalists.
  headline: Citizen Lab Finds Cellebrite Tool Used on Kenyan Activist’s Phone in Police
    Custody
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/citizen-lab-finds-cellebrite-tool-used.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Citizen Lab Finds Cellebrite Tool Used on Kenyan Activist’s Phone in Police
  Custody
updated_at: '2026-02-27T06:25:15.170215+00:00'
url_hash: 565a7fefa96377a7a897cfc10b6f848bf51630cd
---

New research from the Citizen Lab has found signs that Kenyan authorities used a commercial
[forensic extraction tool](https://thehackernews.com/2024/12/novispy-spyware-installed-on.html)
manufactured by Israeli company Cellebrite to break into a prominent dissident's phone, making it the latest case of abuse of the technology targeting civil society.

The interdisciplinary research unit at the University of Toronto's Munk School of Global Affairs & Public Policy
[said](https://citizenlab.ca/research/cellebrite-used-on-kenyan-activist-and-politician-boniface-mwangi/)
it found the indicators on a personal phone belonging to Boniface Mwangi, a Kenyan pro-democracy activist who has
[announced plans](https://www.africanews.com/2025/08/27/kenyan-activist-boniface-mwangi-announces-2027-presidential-bid/)
to run for president in 2027.

Specifically, it has emerged that Cellebrite's forensic extraction tools were used on his Samsung phone while it was in police custody following his arrest in July 2025.

The phone was returned to him nearly two months later, in September, at which point Mwangi found that the phone was no longer password-protected and could be unlocked without requiring a password. It's been assessed with high confidence that Cellebrite's technology was used on the phone on or around July 20 and July 21, 2025.

"The use of Cellebrite could have enabled the full extraction of all materials from Mwangi's device, including messages, private materials, personal files, financial information, passwords, and other sensitive information," the Citizen Lab said.

The latest findings follow a
[separate report](https://citizenlab.ca/research/from-protest-to-peril-cellebrite-used-against-jordanian-civil-society/)
released last month, in which the researchers said officials in Jordan likely
[used Cellebrite](https://www.occrp.org/en/news/jordan-used-israeli-tech-to-crack-phones-of-gaza-war-protestors-report)
to extract information from the mobile phones of activists and human rights defenders who had been critical of Israel and spoke out in support of Palestinians in Gaza.

The devices were seized by Jordanian authorities during detentions, arrests, and interrogations, and subsequently returned to them. The documented incidents took place between late 2023 and mid-2025, the Citizen Lab said.

In response to the findings, a spokesperson for Cellebrite
[told](https://www.theguardian.com/world/2026/jan/22/jordan-israeli-spyware-gaza-activists)
The Guardian that the company's technology is used to "access private data only in accordance with legal due process or with appropriate consent to aid investigations legally after an event has occurred."

The two cases add to a
[growing body](https://thehackernews.com/2025/09/weekly-recap-bootkit-malware-ai-powered.html#:~:text=Spyware%20Found%20on%20Phones%20Belonging%20to%20Kenyan%20Filmmakers)
of
[evidence](https://thehackernews.com/2025/02/amnesty-finds-cellebrites-zero-day.html)
documenting the misuse of Cellebrite technology by government clients. It also reflects a broader ecosystem of surveillance abuses by various governments around the world to enable highly-targeted surveillance using mercenary spyware like Pegasus and Predator.

### Predator Spyware Targets Angolan Journalist

The development also coincides with another report from Amnesty International, which discovered evidence that the iPhone belonging to Teixeira Cândido, an Angolan journalist and press freedom advocate, was successfully targeted by Intellexa's
[Predator](https://thehackernews.com/2025/12/intellexa-leaks-reveal-zero-days-and.html)
spyware in May 2024 after he opened an infection link received via WhatsApp.

The iPhone was running iOS 16.2, an outdated version of the operating system with known security issues. It's currently not known what exploit was used to trigger the infection. In multiple reports published last year, Recorded Future
[revealed](https://thehackernews.com/2025/06/apple-zero-click-flaw-in-messages.html)
that it has observed suspected Predator operations in Angola
[dating back to 2024](https://thehackernews.com/2024/09/apple-drops-spyware-case-against-nso.html)
.

"This is the first forensically confirmed case of the Predator spyware being used to target civil society in Angola," the international human rights organization
[said](https://securitylab.amnesty.org/latest/2026/02/journalism-under-attack-predator-spyware-in-angola/)
. "Once the spyware was installed, the attacker could gain unrestricted access to Teixeira Cândido's iPhone."

"The Predator spyware infection appears to have lasted less than one day, with the infection being removed when Teixeira Cândido's phone was restarted in the evening of 4 May 2024. From that time until 16 June 2024, the attackers made 11 new attempts to re-infect the device by sending him new malicious Predator infection links. All of these subsequent attack attempts appear to have failed, likely due to the links simply not being opened."

In a statement shared with The Hacker News, Recorded Future said Amnesty's findings are consistent with what it has previously observed regarding suspected Predator activity in Angola, both in terms of timing and infrastructure.

"Over time, and across different country clusters, we've unsurprisingly seen a steady evolution in Predator-linked infrastructure and tactics," the Mastercard-owned threat intelligence firm said. "For example, domains that were once hosted almost exclusively on virtual private servers, as in this case, have frequently been moved behind content delivery networks to obscure the underlying infrastructure."

According to an analysis published by French offensive security company Reverse Society, Predator is a
[commercial spyware product](https://blog.reversesociety.co/blog/2025/predator-ios-malware-surveillance-framework-part-1)
"built for reliable, long-term deployment" and allows operators to selectively enable or disable modules based on target activity, granting them real-time control over surveillance efforts.

Predator has also been found to incorporate various undocumented anti-analysis mechanisms, including a crash reporter monitoring system for anti-forensics and SpringBoard hooking to suppress recording indicators from victims when the microphone or camera is activated, illustrating the sophistication of the spyware. On top of that, it has explicit checks to avoid running in U.S. and Israeli locales.

Through what Jamf calls "
[surgical API hooking](https://www.jamf.com/blog/predator-spyware-ios-recording-indicator-bypass-analysis/)
" targeting SpringBoard's sensor activity data provider, Predator suppresses only the recording indicators while the device remains fully operational. This subtle approach ensures that the victim's phone works as usual, but they receive no visual warning that surveillance is taking place.

"These findings demonstrate that Predator's operators have granular visibility into failed deployments, [...] enabling them to adapt their approaches for specific targets," Jamf Threat Labs researchers Shen Yuan and Nir Avraham
[said](https://www.jamf.com/blog/predator-spyware-anti-analysis-techniques-ios-error-codes-detection/)
. "This error code system transforms failed deployments from black boxes into diagnostic events."