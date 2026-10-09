---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-26T00:00:07.739143+00:00'
exported_at: '2025-11-26T00:00:10.009681+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/jackfix-uses-fake-windows-update-pop.html
structured_data:
  about: []
  author: ''
  description: Fake Windows update lures using ClickFix deliver multi-stage PowerShell
    malware via adult-site malvertising.
  headline: JackFix Uses Fake Windows Update Pop-Ups on Adult Sites to Deliver Multiple
    Stealers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/jackfix-uses-fake-windows-update-pop.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: JackFix Uses Fake Windows Update Pop-Ups on Adult Sites to Deliver Multiple
  Stealers
updated_at: '2025-11-26T00:00:07.739143+00:00'
url_hash: a0743897934d0a27ea785ef12fc108e587cdd0cb
---

Cybersecurity researchers are calling attention to a new campaign that's leveraging a combination of
[ClickFix](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html)
lures and fake adult websites to deceive users into running malicious commands under the guise of a "critical" Windows security update.

"Campaign leverages fake adult websites (xHamster, PornHub clones) as its phishing mechanism, likely distributed via malvertising," Acronis
[said](https://www.acronis.com/en/tru/posts/fake-adult-websites-pop-realistic-windows-update-screen-to-deliver-stealers-via-clickfix/)
in a new report shared with The Hacker News. "The adult theme, and possible connection to shady websites, adds to the victim's psychological pressure to comply with sudden 'security update' installation."

[ClickFix-style attacks](https://thehackernews.com/2025/09/new-filefix-variant-delivers-stealc.html)
have surged over the past year, typically tricking users into running malicious commands on their own machines using prompts for technical fixes or completing CAPTCHA verification checks. According to
[data](https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/)
from Microsoft, ClickFix has become the most common initial access method, accounting for 47% of attacks.

The latest campaign displays highly convincing fake Windows update screens in an attempt to get the victim to run malicious code, indicating that attackers are moving away from the traditional robot-check lures. The activity has been codenamed
**JackFix**
by the Singapore-based cybersecurity company.

Perhaps the most concerning aspect of the attack is that the phony Windows update alert hijacks the entire screen and instructs the victim to open the Windows Run dialog, press Ctrl + V, and hit Enter, thereby triggering the infection sequence.

It's assessed that the starting point of the attack is a fake adult site to which unsuspecting users are redirected via malvertising or other social engineering methods, only to suddenly serve them an "urgent security update." Select iterations of the sites have been found to include developer comments in Russian, hinting at the possibility of a Russian-speaking threat actor.

"The Windows Update screen is created entirely using HTML and JavaScript code, and pops up as soon as the victim interacts with any element on the phishing site," security researcher Eliad Kimhy said. "The page attempts to go full screen via JavaScript code, while at the same time creating a fairly convincing Windows Update window composed of a blue background and white text, reminiscent of Windows' infamous blue screen of death."

What's notable about the attack is that it heavily leans on obfuscation to conceal ClickFix-related code, as well as blocks users from escaping the full-screen alert by disabling the Escape and F11 buttons, along with F5 and F12 keys. However, due to faulty logic, users can still press the Escape and F11 buttons to get rid of the full screen.

The initial command executed is an MSHTA payload that's launched using the legitimate mshta.exe binary, which, in turn, contains JavaScript designed to run a PowerShell command to retrieve another PowerShell script from a remote server. These domains are designed such that directly navigating to these addresses redirects the user to a benign site like Google or Steam.

"Only when the site is reached out to via an irm or iwr PowerShell command does it respond with the correct code," Acronis explained. "This creates an extra layer of obfuscation and analysis prevention."

|  |
| --- |
|  |
| UAC request to grant attackers admin privileges |

The downloaded PowerShell script also packs in various obfuscation and anti-analysis mechanisms, one of which is the use of garbage code to complicate analysis efforts. It also attempts to elevate privileges and creates Microsoft Defender Antivirus exclusions for command-and-control (C2) addresses and paths where the payloads are staged.

To achieve privilege escalation, the malware uses the
[Start-Process cmdlet](https://powershellcommands.com/start-process-powershell-verb-runas)
in conjunction with the "-Verb RunAs" parameter to launch PowerShell with administrative rights and continuously prompts for permission until it's granted by the victim. Once this step is successful, the script is designed to drop additional payloads, such as simple remote access trojans (RATs) that are programmed to contact a C2 server, presumably to drop more malware.

The PowerShell script has also been observed to serve up to eight different payloads, with Acronis describing it as the "most egregious example of spray and pray." These include Rhadamanthys Stealer, Vidar Stealer 2.0, RedLine Stealer, Amadey, as well as other unspecified loaders and RATs.

"If only one of these payloads manages to run successfully, victims risk losing passwords, crypto wallets, and more," Kimhy said. "In the case of a few of these loaders -- the attacker may choose to bring in other payloads into the attack, and the attack can quickly escalate further."

The disclosure comes as Huntress
[detailed](https://www.huntress.com/blog/clickfix-malware-buried-in-images)
a multi-stage malware execution chain that originates from a ClickFix lure masquerading as a Windows update and deploys stealer malware like Lumma and Rhadamanthys by concealing the final stages within an image, a technique known as steganography.

Like in the case of the aforementioned campaign, the ClickFix command copied to the clipboard and pasted into the Run dialog uses mshta.exe to run a JavaScript payload that's capable of running a remotely-hosted PowerShell script directly in memory.

The PowerShell code is used to decrypt and launch a .NET assembly payload, a loader dubbed Stego Loader that serves as a conduit for the execution of
[Donut](https://github.com/TheWover/donut)
-packed shellcode hidden within an embedded and encrypted PNG file. The extracted shellcode is then injected into a target process to ultimately deploy Lumma or Rhadamanthys.

Interestingly, one of the domains listed by Huntress as being used to fetch the PowerShell script ("securitysettings[.]live") has also been flagged by Acronis, suggesting these two activity clusters may be related.

"The threat actor often changes the URI (/tick.odd, /gpsc.dat, /ercx.dat, etc.) used to host the first mshta.exe stage," security researchers Ben Folland and Anna Pham said in the report.

"Additionally, the threat actor moved from hosting the second stage on the domain securitysettings[.]live and instead hosted on xoiiasdpsdoasdpojas[.]com, although both point to the same IP address 141.98.80[.]175, which was also used to deliver the first stage [i.e., the JavaScript code run by mshta.exe]."

ClickFix has become hugely successful as it relies on a simple yet effective method, which is to entice a user into infecting their own machine and bypassing security controls. Organizations can defend against such attacks by training employees to better spot the threat and disabling the Windows Run box via Registry changes or
[Group Policy](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
.