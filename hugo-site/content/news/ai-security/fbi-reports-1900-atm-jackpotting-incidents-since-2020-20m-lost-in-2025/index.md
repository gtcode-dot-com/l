---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-20T16:15:17.586534+00:00'
exported_at: '2026-02-20T16:15:20.221893+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/fbi-reports-1900-atm-jackpotting.html
structured_data:
  about: []
  author: ''
  description: FBI reports 1,900 ATM jackpotting cases since 2020, with $40.73M lost
    to Ploutus malware bypassing bank authorization.
  headline: FBI Reports 1,900 ATM Jackpotting Incidents Since 2020, $20M Lost in 2025
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/fbi-reports-1900-atm-jackpotting.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: FBI Reports 1,900 ATM Jackpotting Incidents Since 2020, $20M Lost in 2025
updated_at: '2026-02-20T16:15:17.586534+00:00'
url_hash: bcc211ebf0c943e81d7f3ebf04a70424d68576c1
---

**

Ravie Lakshmanan
**

Feb 20, 2026

Financial Crime / Banking Security

The U.S. Federal Bureau of Investigation (FBI) has warned of an increase in ATM jackpotting incidents across the country, leading to losses of more than $20 million in 2025.

The agency said 1,900 ATM jackpotting incidents have been reported since 2020, out of which 700 took place last year. In December 2025, the U.S. Department of Justice (DoJ)
[said](https://thehackernews.com/2025/12/us-doj-charges-54-in-atm-jackpotting.html)
about $40.73 million has been collectively lost to jackpotting attacks since 2021.

"Threat actors exploit physical and software vulnerabilities in ATMs and deploy malware to dispense cash without a legitimate transaction," the FBI
[said](https://www.ic3.gov/CSA/2026/260219.pdf)
in a Thursday bulletin.

The jackpotting attacks involve the use of specialized malware, such as Ploutus, to infect ATMs and force them to dispense cash. In most cases, cybercriminals have been observed gaining unauthorized access to the machines by opening an ATM face with widely available generic keys.

There are at least two different ways by which the malware is deployed: Removing the ATM's hard drive, followed by either connecting it to their computer, copying it to the hard drive, attaching it back to the ATM, and rebooting the ATM, or replacing it entirely with a foreign hard drive preloaded with the malware and rebooting it.

Regardless of the method used, the end result is the same. The malware is designed to interact directly with the ATM hardware, thereby getting around any security controls present in the original ATM software.

Because the malware does not require a connection to an actual bank card or customer account to dispense cash, it can be used against ATMs of different manufacturers with little to no code changes, as the underlying Windows operating system is exploited during the attack.

Ploutus was
[first observed](https://thehackernews.com/2025/12/us-doj-charges-54-in-atm-jackpotting.html)
in Mexico in 2013. Once installed, it grants threat actors complete control over an ATM, enabling them to trigger cash-outs that the FBI said can occur in minutes and are harder to detect until after the money is withdrawn.

"Ploutus malware exploits the eXtensions for Financial Services (
[XFS](https://en.wikipedia.org/wiki/CEN/XFS)
), the layer of software that instructs an ATM what to physically do," the FBI explained.

"When a legitimate transaction occurs, the ATM application sends instructions through XFS for bank authorization. If a threat actor can issue their own commands to XFS, they can bypass bank authorization entirely and instruct the ATM to dispense cash on demand."

The agency has outlined a long list of recommendations that organizations can adopt to mitigate jackpotting risks. This includes tightening physical security by installing threat sensors, setting up security cameras, and changing standard locks on ATM devices.

Other measures involve auditing ATM devices, changing default credentials, configuring an automatic shutdown mode once indicators of compromise are detected, enforcing device allowlisting to prevent connection of unauthorized devices, and maintaining logs.