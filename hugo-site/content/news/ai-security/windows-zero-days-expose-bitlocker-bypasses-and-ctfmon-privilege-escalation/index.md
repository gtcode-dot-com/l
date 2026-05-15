---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-15T02:03:12.240431+00:00'
exported_at: '2026-05-15T02:03:15.506662+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html
structured_data:
  about: []
  author: ''
  description: YellowKey bypasses BitLocker via WinRE USB FsTx files, exposing Windows
    11 and Server 2022/2025 systems.
  headline: Windows Zero-Days Expose BitLocker Bypasses And CTFMON Privilege Escalation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Windows Zero-Days Expose BitLocker Bypasses And CTFMON Privilege Escalation
updated_at: '2026-05-15T02:03:12.240431+00:00'
url_hash: c7358f7b20ab0f616e88fbdba8f1244fe2507876
---

An anonymous cybersecurity researcher who disclosed three Microsoft Defender vulnerabilities has returned with two more zero-days involving a BitLocker bypass and a privilege escalation impacting Windows Collaborative Translation Framework (CTFMON).

The
[security defects](https://deadeclipse666.blogspot.com/2026/05/two-more-public-disclosures-it-will.html)
have been codenamed
**[YellowKey](https://github.com/Nightmare-Eclipse/YellowKey)**
and
**[GreenPlasma](https://github.com/Nightmare-Eclipse/GreenPlasma)**
, respectively, by the researcher, who goes by the online aliases Chaotic Eclipse and Nightmare-Eclipse.

The researcher described
[YellowKey](https://x.com/weezerOSINT/status/2054299771817660433)
as "one of the most insane discoveries I ever found," likening the BitLocker bypass to functioning as a backdoor, as the bug is present only in the Windows Recovery Environment (
[WinRE](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference)
), a built-in framework designed to troubleshoot and repair common unbootable operating system issues.

YellowKey affects Windows 11 and Windows Server 2022/2025. At a high level, it involves copying specially crafted "FsTx" files on a USB drive or the EFI partition, plugging the USB drive into the target Windows computer with BitLocker protections turned on, rebooting into WinRE, and triggering a shell by holding down the CTRL key.

"I think it will take a while even for MSRC to find the real root cause of the issue. I just never managed to understand why this vulnerability is sooo well hidden," the researcher
[explained](https://deadeclipse666.blogspot.com/2026/05/were-doing-silent-patches-now-huh-also.html)
. "Second thing is, no, TPM+PIN does not help, the issue is still exploitable regardless."

Security researcher Will Dormann, in a
[post](https://infosec.exchange/@wdormann/116565129854382214)
shared on Mastodon, said, "I was able to reproduce [YellowKey] with a USB drive attached," adding, "it looks like Transactional NTFS bits on a USB Drive are able to delete the winpeshl.ini file on ANOTHER DRIVE (X:). And we get a cmd.exe prompt, with BitLocker unlocked instead of the expected Windows Recovery environment."

"While the
[TPM-only BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/countermeasures)
bypass is indeed interesting, I think the buried lede here is that a \System Volume Information\FsTx directory on one volume has the ability to modify the contents of another volume when it is replayed," Dormann pointed out. "To me, this in and of itself sounds like a vulnerability."

The second vulnerability flagged by Chaotic Eclipse is a case of privilege escalation security that could be exploited to obtain a shell with SYSTEM permissions. It arises as a result of what has been described as Windows CTFMON arbitrary section creation.

The released proof-of-concept (PoC) is incomplete and lacks the necessary code to obtain a full SYSTEM shell. In its current form, the exploit can allow an unprivileged user to create arbitrary memory section objects within directory objects writable by SYSTEM, potentially enabling manipulation of privileged services or drivers that implicitly trust those paths, as a standard user does not have write access to the locations.

The development comes nearly a month after the researcher
[published](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html)
three Defender zero-days dubbed BlueHammer, RedSun, and UnDefend after allegedly expressing dissatisfaction with Microsoft's handling of the vulnerability disclosure process. The shortcomings have since come under active exploitation in the wild.

While BlueHammer was officially assigned the identifier CVE-2026-33825 and patched by Microsoft last month, Chaotic Eclipse said the tech giant appears to have "silently" addressed RedSun without issuing any advisory.

"I hope you at least attempt to resolve the situation responsibly, I'm not sure what type of reaction you expected from me when you threw more gas on the fire after BlueHammer," the researcher said. "The fire will go as long as you want, unless you extinguish it or until there nothing left to burn."

Chaotic Eclipse also promised a "big surprise" for Microsoft, coinciding with the next Patch Tuesday release in June 2026.

When reached for comment, a Microsoft spokesperson had previously told The Hacker News that it "has a customer commitment to investigate reported security issues and update impacted devices to protect customers as soon as possible," and that it supports coordinated vulnerability disclosure, which the company said "helps ensure issues are carefully investigated and addressed before public disclosure."

### BitLocker Downgrade Attack Uncovered

The development comes as French cybersecurity company Intrinsec detailed an
[attack chain](https://github.com/garatc/BitUnlocker)
against BitLocker that leverages a boot manager downgrade by exploiting
[CVE-2025-48804](https://thehackernews.com/2025/07/microsoft-patches-130-vulnerabilities.html)
(CVSS score: 6.8) to bypass the encryption protection on fully patched Windows 11 systems in under five minutes.

"The principle is as follows: the boot manager loads the System Deployment Image (SDI) file and the WIM referenced by it, and verifies the integrity of the legitimate WIM," Intrinsec
[said](https://www.intrinsec.com/en/contournement-bitlocker-la-realite-des-downgrade-attacks/)
.

"However, when a second WIM is added to the SDI with a modified blob table, the boot manager checks the first (legitimate) WIM while simultaneously booting from the second (controlled by the attacker). This second WIM contains a WinRE image infected with 'cmd.exe,' which executes with the decrypted BitLocker volume."

While fixes released by Microsoft in July 2025 plugged this security defect in July 2025, security researcher Cassius Garat said the problem lies in the fact that Secure Boot only verifies a binary's signing certificate, not its version. As a result, a vulnerable version of "bootmgfw.efi" that does not contain the patch and is signed with the trusted PCA 2011 certificate can be used to get around BitLocker safeguards.

It's worth noting that Microsoft
[plans to retire](https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html)
the old PCA 2011 certificates next month. "And as long as it is not revoked, even an old, vulnerable boot manager can be loaded without triggering an alert," Intrinsec noted. To pull off the attack, a bad actor needs to have physical access to the target machine.

To counter the risk, it's essential to enable a
[BitLocker PIN](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/countermeasures#preboot-authentication)
at startup for
[preboot authentication](https://www.intrinsec.com/en/contournement-bitlocker-alternative-tpm-sniffing/)
and migrate the boot manager to the
[CA 2023 certificate](https://support.microsoft.com/en-us/topic/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023-24932-41a975df-beb2-40c1-99a3-b3ff139f832d)
and revoke the old PCA 2011 certificate.