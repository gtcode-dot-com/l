---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-12T08:03:56.453780+00:00'
exported_at: '2025-12-12T08:04:00.322672+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2025/12/microsoft-patch-tuesday-december-2025-edition
structured_data:
  about: []
  author: ''
  description: Microsoft Patch Tuesday, December 2025 Edition
  headline: Microsoft Patch Tuesday, December 2025 Edition
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2025/12/microsoft-patch-tuesday-december-2025-edition
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Patch Tuesday, December 2025 Edition
updated_at: '2025-12-12T08:03:56.453780+00:00'
url_hash: 25ed28355a85a10280f071a9bb4afd60e4bebf81
---

**Microsoft**
today pushed updates to fix at least 56 security flaws in its
**Windows**
operating systems and supported software. This final Patch Tuesday of 2025 tackles one zero-day bug that is already being exploited, as well as two publicly disclosed vulnerabilities.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

Despite releasing a lower-than-normal number of security updates these past few months, Microsoft patched a whopping 1,129 vulnerabilities in 2025, an 11.9% increase from 2024. According to
**Satnam Narang**
at
**Tenable**
, this year marks the second consecutive year that Microsoft patched over one thousand vulnerabilities, and the third time it has done so since its inception.

The zero-day flaw patched today is
[CVE-2025-62221](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62221)
, a privilege escalation vulnerability affecting
**Windows 10**
and later editions. The weakness resides in a component called the “
**Windows Cloud Files Mini Filter Driver**
” — a system driver that enables cloud applications to access file system functionalities.

“This is particularly concerning, as the mini filter is integral to services like OneDrive, Google Drive, and iCloud, and remains a core Windows component, even if none of those apps were installed,” said
**Adam Barnett**
, lead software engineer at
**Rapid7**
.

Only three of the flaws patched today earned Microsoft’s most-dire “critical” rating: Both
[CVE-2025-62554](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62554)
and
[CVE-2025-62557](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62557)
involve
**Microsoft Office**
, and both can exploited merely by viewing a booby-trapped email message in the Preview Pane. Another critical bug —
[CVE-2025-62562](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62562)
— involves
**Microsoft Outlook**
, although Redmond says the Preview Pane is not an attack vector with this one.

But according to Microsoft, the vulnerabilities most likely to be exploited from this month’s patch batch are other (non-critical) privilege escalation bugs, including:

–
[CVE-2025-62458](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62458)
— Win32k

–
[CVE-2025-62470](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62470)
— Windows Common Log File System Driver

–
[CVE-2025-62472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62472)
— Windows Remote Access Connection Manager

–
[CVE-2025-59516](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59516)
— Windows Storage VSP Driver

–
[CVE-2025-59517](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59517)
— Windows Storage VSP Driver

**Kev Breen**
, senior director of threat research at
**Immersive**
, said privilege escalation flaws are observed in almost every incident involving host compromises.

“We don’t know why Microsoft has marked these specifically as more likely, but the majority of these components have historically been exploited in the wild or have enough technical detail on previous CVEs that it would be easier for threat actors to weaponize these,” Breen said. “Either way, while not actively being exploited, these should be patched sooner rather than later.”

One of the more interesting vulnerabilities patched this month is
[CVE-2025-64671](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-64671)
, a remote code execution flaw in the
**Github Copilot Plugin for Jetbrains**
AI-based coding assistant that is used by Microsoft and GitHub. Breen said this flaw would allow attackers to execute arbitrary code by tricking the large language model (LLM) into running commands that bypass the guardrails and add malicious instructions in the user’s “auto-approve” settings.

CVE-2025-64671 is part of a broader, more systemic security crisis that security researcher
**Ari Marzuk**
has branded
[IDEsaster](https://maccarita.com/posts/idesaster/)
(IDE  stands for “integrated development environment”), which encompasses more than 30 separate vulnerabilities reported in nearly a dozen market-leading AI coding platforms, including
**Cursor**
,
**Windsurf**
,
**Gemini CLI**
, and
**Claude Code**
.

The other publicly-disclosed vulnerability patched today is
[CVE-2025-54100](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54100)
, a remote code execution bug in
**Windows Powershell**
on Windows Server 2008 and later that allows an unauthenticated attacker to run code in the security context of the user.

For anyone seeking a more granular breakdown of the security updates Microsoft pushed today, check out the roundup at the
[SANS Internet Storm Center](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20December%202025/32550)
. As always, please leave a note in the comments if you experience problems applying any of this month’s Windows patches.