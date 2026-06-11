---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T02:00:15.469520+00:00'
exported_at: '2026-06-11T02:00:17.062355+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html
structured_data:
  about: []
  author: ''
  description: Microsoft released fixes for 206 vulnerabilities across its software
    portfolio, including 39 Critical flaws and three publicly disclosed zero-days.
  headline: Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical
    RCE Bugs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical
  RCE Bugs
updated_at: '2026-06-11T02:00:15.469520+00:00'
url_hash: 9c811d88186cc88778159e88f25937f53b242b65
---

Microsoft on Tuesday released fixes for a record
[206 security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun)
impacting its software portfolio, including three flaws that have been publicly disclosed at the time of release.

Of the 206 flaws, 39 are rated Critical, and 167 are rated Important in severity. This includes 63 privilege escalation, 56 remote code execution, 30 information disclosure, 27 spoofing, 20 security feature bypass, seven denial-of-service, and three tampering vulnerabilities.

The patches also include two non-Microsoft CVEs, a privilege escalation vulnerability impacting Windows Kernel (
[CVE-2025-10263](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-10263)
) and a UEFI Secure Boot
[security feature bypass](https://kb.cert.org/vuls/id/616257)
(
[CVE-2026-8863](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-8863)
). They are in addition to more than 350 security flaws that Google has addressed in Chromium, which is used in Microsoft's Edge browser.

Topping the list of fixes is
[CVE-2026-45657](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45657)
(CVSS score: 9.8), a use-after-free flaw affecting Windows Kernel that could result in remote code execution.

"An attacker could exploit this vulnerability by sending specially crafted network traffic to a vulnerable Windows system," Microsoft said. "If successful, the malicious network packets could trigger a flaw in how the Windows kernel processes certain TCP/IP data, potentially allowing the attacker to run code with system-level privileges without needing to sign in or interact with a user."

Other important vulnerabilities of note are listed below -

* [CVE-2026-47291](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47291)
  (CVSS score: 9.8) - An integer overflow or wraparound flaw in Windows HTTP.sys that allows an unauthorized attacker to execute code over a network.
* [CVE-2026-44815](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815)
  (CVSS score: 9.8) - A stack-based buffer overflow vulnerability in Windows DHCP Client that allows an unauthorized attacker to execute code over a network.

"This flaw needs no credentials or user action and can turn network traffic into a full system compromise," Alex Vovk, CEO and co-founder of Action1,
[said](https://www.action1.com/patch-tuesday/patch-tuesday-june-2026/)
about CVE-2026-44815. "An attacker could send specially crafted network traffic to a system configured for DHCP services."

"Successful exploitation could allow unauthorized code execution over the network with high impact to confidentiality, integrity, and availability. This vulnerability creates serious risk because DHCP is a core network function. Successful exploitation could lead to server compromise, malware deployment, data theft, service disruption, and movement deeper into the network. Systems handling DHCP traffic should be treated as high-priority patch targets."

Microsoft has also released patches to address
[CVE-2026-45585](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585)
(CVSS score: 6.8), a Windows BitLocker security feature bypass vulnerability for which a proof-of-concept (PoC) exploit called
[YellowKey](https://thehackernews.com/2026/05/microsoft-releases-mitigation-for.html)
was released by security researcher Chaotic Eclipse (aka Nightmare-Eclipse) last month.

CVE-2026-45585 is one of several secure feature bypasses that the Windows makers has addressed this month -

"A successful attacker could bypass the BitLocker Device Encryption feature on the system storage device," Microsoft said in its advisories for the three issues. "An attacker with physical access to the target could exploit this vulnerability to gain access to encrypted data."

According to security researcher Will Dormann, CVE-2026-50507 is
[assessed](https://infosec.exchange/@wdormann/116699350092887103)
to be a fix for a BitLocker bypass dubbed
[bitskrieg](https://x.com/jonasLyk/status/2062768028090007773)
that grants full access to encrypted data. It's worth noting that CVE-2026-50507, along with CVE-2026-49160 and CVE-2026-45586, are listed as publicly disclosed zero-days.

* [CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)
  (CVSS score: 7.8) - Windows Collaborative Translation Framework (CTFMON) privilege escalation vulnerability
* [CVE-2026-49160](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-49160)
  (CVSS score: 7.5) - HTTP.sys denial-of-service vulnerability

CVE-2026-49160 is related to
[HTTP2/Bomb](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html)
, an
[attack technique](https://github.com/califio/publications/tree/main/MADBugs/http2-bomb)
that can be used to knock web servers offline in seconds. In tests conducted by Calif, an IIS server was found to exhaust 64 GB RAM in about 45 seconds. To mitigate the attack, Microsoft has introduced a new "MaxHeadersCount" registry setting to limit the number of headers in HTTP/2 and HTTP/3 requests.

"Limiting HTTP headers can help protect systems and servers from excessive memory use, high CPU consumption, and denial-of-service attacks," Microsoft
[said](https://support.microsoft.com/en-us/topic/control-the-maximum-number-of-http-2-and-http-3-request-headers-in-windows-clients-and-servers-084da156-7a99-4abf-b759-f973c35eded3)
. "Because HTTP/2 (HPACK) or HTTP/3 (QPACK) header compression is used and more complex protocol processing, enforcing a header limit such as MaxHeadersCount can help maintain performance and reliability."

On the other hand, CVE-2026-45586 is suspected to be a fix for a zero-day privilege escalation exploit that Chaotic Eclipse released under the name
[GreenPlasma](https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html)
.

Lastly, the June 2026 update also plugs
[MiniPlasma](https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html)
, a separate vulnerability disclosed by Chaotic Eclipse as an incomplete fix for CVE-2020-17103, which was originally addressed by Microsoft in December 2020.

"To comprehensively address the vulnerability identified by CVE-2020-17103 and recently publicly referred to as 'MiniPlasma,' Microsoft recommends installing the June 2026 updates for your Windows operating systems," the tech giant
[said](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103)
in an update to its advisory.

The increasing number of patches has been attributed to the use of artificial intelligence (AI)-assisted vulnerability discovery approaches, a trend that Microsoft said will continue in the foreseeable future.

"Pandora's proverbial box has been opened, and as more advanced AI models become available, we expect the norm to continue upward across the board, not just for Patch Tuesday," Satnam Narang, senior staff research engineer at Tenable, said in a statement.

Dustin Childs, head of threat awareness at TrendAI's Zero Day Initiative (ZDI), described the massive set of Microsoft vulnerabilities as a testament to how AI is supercharging flaw discovery at an uncontrollable scale.

"The current number of CVEs shipped by Microsoft this year exceeds the total number of CVEs shipped in all of 2018," Childs said. "It is extraordinary that Microsoft can produce so many patches in a single month, and I expect many testers are wondering what quality issues may exist."

The patches come as Chaotic Eclipse released a PoC exploit for yet another Microsoft Defender zero-day named
[RoguePlanet](https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html)
, characterizing it as a
[race condition](https://deadeclipse666.blogspot.com/2026/06/rogueplanet-quick-history.html)
that could be used to spawn a Windows command prompt with SYSTEM privileges.