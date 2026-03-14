---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-14T05:50:05.592867+00:00'
exported_at: '2026-03-14T05:50:07.467072+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/storm-2561-spreads-trojan-vpn-clients.html
structured_data:
  about: []
  author: ''
  description: Storm-2561 spreads fake VPN installers via SEO poisoning and GitHub
    downloads, stealing enterprise VPN credentials with Hyrax malware.
  headline: Storm-2561 Spreads Trojan VPN Clients via SEO Poisoning to Steal Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/storm-2561-spreads-trojan-vpn-clients.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Storm-2561 Spreads Trojan VPN Clients via SEO Poisoning to Steal Credentials
updated_at: '2026-03-14T05:50:05.592867+00:00'
url_hash: cce9c0b54893216784208df387ec9c717bd0f3c5
---

**

Ravie Lakshmanan
**

Mar 13, 2026

VPN Security / Malware

Microsoft has disclosed details of a credential theft campaign that employs fake virtual private network (VPN) clients distributed through search engine optimization (SEO) poisoning techniques.

"The campaign redirects users searching for legitimate enterprise software to malicious ZIP files on attacker-controlled websites to deploy digitally signed trojans that masquerade as trusted VPN clients while harvesting VPN credentials," the Microsoft Threat Intelligence and Microsoft Defender Experts teams
[said](https://www.microsoft.com/en-us/security/blog/2026/03/12/storm-2561-uses-seo-poisoning-to-distribute-fake-vpn-clients-for-credential-theft/)
.

The Windows maker, which observed the activity in mid-January 2026, has attributed it to
**Storm-2561**
, a threat activity cluster known for propagating malware through SEO poisoning and impersonating popular software vendors since May 2025.

The threat actor's campaigns were
[first documented](https://www.cyjax.com/resources/blog/a-sting-on-bing-bumblebee-delivered-through-bing-seo-poisoning-campaign)
by Cyjax, highlighting the use of SEO poisoning to redirect users searching for software programs from companies like SonicWall, Hanwha Vision, and Pulse Secure (now Ivanti Secure Access) on Bing to fake sites and trick them into downloading MSI installers that deploy the
[Bumblebee loader](https://thehackernews.com/2022/04/cybercriminals-using-new-malware-loader.html)
.

A subsequent iteration of the attack was
[disclosed](https://thehackernews.com/2025/10/weekly-recap-f5-breached-linux-rootkits.html#:~:text=SEO%20Campaign%20Uses%20Fake%20Ivanti%20Installers%20to%20Steal%20Credentials)
by Zscaler in October 2025. The campaign was observed taking advantage of users searching for legitimate software on Bing to propagate a trojanized Ivanti Pulse Secure VPN client via bogus websites ("ivanti-vpn[.]org") that ultimately stole VPN credentials from the victim's machine.

Microsoft said the activity highlights how threat actors exploit trust in search engine rankings and software branding as a social engineering tactic to steal data from users looking for enterprise VPN software. Compounding matters is the abuse of trusted platforms like GitHub to host the installer files.

Specifically, the GitHub repository hosts a ZIP file containing an MSI installer file that masquerades as legitimate VPN software, but sideloads malicious DLL files during installation. The end goal, as before, is to collect and exfiltrate VPN credentials using a variant of an information stealer called Hyrax.

A fake, yet convincing, VPN sign-in dialog is displayed to the user to capture the credentials. Once the information is entered by the victim, they are displayed an error message and are instructed to download the legitimate VPN client this time. In some cases, they are redirected to the legitimate VPN website.

The malware makes use of the
[Windows RunOnce registry key](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)
to set up persistence, so that it's executed automatically every time following a system reboot.

"This campaign exhibits characteristics consistent with financially motivated cybercrime operations employed by Storm-2561," Microsoft said. "The malicious components are digitally signed by 'Taiyuan Lihua Near Information Technology Co., Ltd.'"

The tech giant has since taken down the attacker-controlled GitHub repositories and revoked the legitimate certificate to neutralize the operation.

To counter such threats, organizations and users are advised to implement multi-factor authentication (MFA) on all accounts, exercise caution when downloading software from websites, and make sure that they are authentic.