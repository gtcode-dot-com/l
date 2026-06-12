---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-12T21:44:30.850354+00:00'
exported_at: '2026-06-12T21:44:35.785444+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/ire-identifies-another-lotuslite-specimen
structured_data:
  about: []
  author: ''
  description: Project Ire examined a timely malware sample and determined its intent
    through reverse engineering—identifying LOTUSLITE characteristics even as most
    major EDR tools did not detect it.
  headline: Ire identifies another LOTUSLITE specimen
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/ire-identifies-another-lotuslite-specimen
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Ire identifies another LOTUSLITE specimen
updated_at: '2026-06-12T21:44:30.850354+00:00'
url_hash: dd008cb894a8038bd6be56d243a46bcf23c16170
---

![Project Ire | | three white line icons on an abstract purple background | greater than / less than icon, search icon, shield icon](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/06/ProjectIre-BlogHeroFeature-1400x788-1.jpg)

## At a glance

* Project Ire identifies a LOTUSLITE variant that shares TTPs (tools, tactics, procedures) with the public family but none of its indicators of compromise (IOC).
* The LLM-driven agent produces a function-by-function behavioral report on the sample without any user interaction to determine whether it is malicious.
* The binary names a threat actor in cleartext; the agent declines to attribute and instead focuses on statically analyzing the behaviors.

We pointed
[Project Ire](https://www.microsoft.com/en-us/research/project/project-ire/)
, Microsoft’s autonomous malware-classification agent, at a malware sample—blind—and asked for a verdict. The sample is a variant of LOTUSLITE, a Windows DLL backdoor recently documented by Acronis. Our copy’s hash isn’t in their IOC list, and as of June 4, most major EDRs (CrowdStrike Falcon, SentinelOne, Sophos, Trellix, Palo Alto, ESET) still don’t flag it as malware. Ire produced a function-by-function behavioral report—install routine, C2 packet layout, command IDs, persistence mechanism, obfuscation—that lines up with Acronis’s published analysis. One decompiler-based run, no human priors.

This is what behavioral, agentic reverse engineering can achieve when signature matching and manual inspections fall short. Variants that share TTPs but not indicators of compromise (IOC) get caught instead of slipping past signature lists. Novel malware classification is a domain with no automatic validator, requiring in-depth investigation and holistic understanding of the software’s behaviors to surface and determine intent. Ire operates without context: no origin metadata, no telemetry, no analyst prompt. It invokes decompilers and binary-analysis tools, builds an auditable chain of evidence, and reaches a malicious-or-benign verdict.

Acronis’s Threat Research Unit (TRU)
[published a writeup
(opens in new tab)](https://www.acronis.com/en/tru/posts/lotuslite-targeted-espionage-leveraging-geopolitical-themes/)
on LOTUSLITE, a DLL backdoor delivered through a politically themed ZIP, sideloaded through a renamed Tencent KuGou launcher. They attribute it to Mustang Panda at moderate confidence based on infrastructure overlap and the loader/DLL split. Hunting on VirusTotal for samples whose behavior matched the report, we surfaced one whose SHA-256 doesn’t appear in Acronis’s IOC list.

The sample:
[47e51e82229e80a387c3cb100d39d3705e6360bbf9bfa1601dbc484e8d02e653
(opens in new tab)](https://www.virustotal.com/gui/file/47e51e82229e80a387c3cb100d39d3705e6360bbf9bfa1601dbc484e8d02e653)
. When we picked it up on May 28, VirusTotal showed 1 of 72 vendors flagging it.

![A screenshot of a 253 KB sample on VirusTotal taken on May 28, 2026 showing that only one of 72 vendors flagged this as malicious. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/06/detections_initial.png)


Figure 1. File Sample 47e51e82229e80a387c3cb100d39d3705e6360bbf9bfa1601dbc484e8d02e653 detection state on VirusTotal on May 28, 2026.

A week later, that rose to 7 of 70. The cluster: Microsoft Trojan:Win32/Malgent!MSR, Kaspersky HEUR:Trojan-Dropper.Win32.Dorifel.gen, Rising Dropper.Dorifel!8.31E (CLOUD), Cynet (score 100), Elastic (moderate confidence), Kingsoft, TrendMicro-HouseCall. With Microsoft now flagging, VT’s popular threat label has shifted to dropper.dorifel / malgent. CrowdStrike Falcon, SentinelOne, Sophos, Trellix, Palo Alto, and ESET still miss it. VT lists the file type as pedll (PE DLL) and the filename as SmartPrintScreen.Print.

![A screenshot of the same 253KB sample on June 4, 2026 showing that 7 of 70 security vendors have identified this sample as malicious: Cynet, Kaspersky, Microsoft, TrendMicro-HouseCall, Elastic, Kingsoft, Rising, and Acronis (Static MIL). ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/06/detections_later.png)


Figure 2. File Sample 47e51e82229e80a387c3cb100d39d3705e6360bbf9bfa1601dbc484e8d02e653 detection state on VirusTotal on June 4, 2026.

We analyzed the sample with Ire, using only its decompiler-based tools through a single tool call. Ire’s verdict was “malicious”; you can review the complete report
[on Github
(opens in new tab)](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fproject-ire%2Fblob%2Fmain%2Freports%2F47e51e82229e80a387c3cb100d39d3705e6360bbf9bfa1601dbc484e8d02e653.md&amp;data=05%7C02%7Csmithsarah%40microsoft.com%7Cabbc5bb6be7e4ddca50b08dec7d70737%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C639167923516521150%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=rr4gCWnGCAHITM4ARAtVXqu66UzUVqByMacq%2BsOmNQ8%3D&amp;reserved=0)
.

## On Ire’s calibration

One noteworthy observation in
[Ire’s report
(opens in new tab)](https://github.com/microsoft/project-ire/blob/main/reports/47e51e82229e80a387c3cb100d39d3705e6360bbf9bfa1601dbc484e8d02e653.md)
is worth highlighting first. Ire flagged the nfapi::nf\_unRegisterDriver and NetFilter naming as suspicious but explicitly did not claim active packet interception. The function in question writes the Run key; it does not install a driver. This is where LLM-driven analysis can go wrong: suggestive strings can steer the verdict. A function called nf\_unRegisterDriver sounds like it does kernel-level work, and a less thorough agent would write that into the report. Downstream defenders would then chase a phantom, building detection rules for behavior that may or may not be there. Ire flagged the misleading name and considered the behavior as one piece of the evidence during its final adjudication of malice.

## Comparing the two reports

|  | Acronis specimen | Our sample |
| --- | --- | --- |
| Sample type | loader EXE + kugou.dll | the malicious DLL itself: AMPV.dll (VT type pedll) |
| Install dir | C:\ProgramData\Technology360NB\ | C:\ProgramData\SmartPrint\ |
| Installed exe | DataTechnology.exe | SmartPrintScreen.exe |
| Run-key value | Lite360 | DadaBank |
| Marker arg | –DATA | –DaDaBar |
| C2 magic | 0x8899AABB | 0xB2EBCFDF |
| Lure | politically themed ZIP, Venezuela-themed launcher | fake “PDF corrupted” message box |
| Mustang Panda link | infra and TTP overlap, moderate confidence (Acronis’s call) | not independently assessed; binary contains the literal string BelievemeIamMustang-Panda |

Comparing Ire’s output with Acronis’ report, the sample we analyzed matches the behavioral profile of the LOTUSLITE family of malware. Both show a loader/DLL split, HTTPS C2 carrying a custom binary protocol with a magic DWORD, interactive shell over pipes, directory enumeration, file primitives, chunked upload, HKCU persistence, and traffic camouflaged as Google and Microsoft services. The surface details differ—filenames, paths, magic value—but the underlying behaviors align. Ire correctly identified this sample as part of the same family of malware because of the behaviors it was able to identify through decompilation and reverse engineering, not on string match alone.

Because the sample is a DLL (pedll per VT), the sample’s install routine reads differently than it might look at first. The DLL copies two files into C:\ProgramData\SmartPrint\: the loader EXE that sideloaded it (its host process, obtained via GetModuleFileName(NULL), written as SmartPrintScreen.exe) and itself (AMPV.dll, the analyzed sample). The Run key points at the loader with –DaDaBar. On the next logon, the loader runs and sideloads AMPV.dll from the install path. This is the same Acronis-identified pattern but with different filenames.

This also explains the binary’s strange export surface. The DLL exports a long list of banking and QR-themed names (Query\_Bank, BankSepah\_Iran, BankToman\_BMI, BankofChina, qrBankInit, JpgSymbolToBMP, and others), most of which resolve to a message box or ExitProcess. The shape suggests a hijacked banking/QR SDK shell, repurposed so the host EXE can call any one of those exports via GetProcAddress and reach the LOTUSLITE entry point. Acronis names theirs DataImporterMain. The Ire report does not surface a matching entry-point name, but it identifies that the behavioral shape is the same.

Acronis attributes the malware family to Mustang Panda at moderate confidence based on infrastructure and TTPs we don’t have access to, while our sample directly contains a literal actor-name string “BelievemeIamMustang-Panda” with no obfuscation. A string isn’t direct proof of authorship; it could be a developer artifact, a trophy, or a deliberate plant. While we are not making an attribution call, we note that the binary names the same actor that Acronis named through other means, and we leave the question open. Another consideration to make for this finding: a string like this can function as adversarial input to LLM-driven analysis, biasing the verdict.

Spotlight: AI-POWERED EXPERIENCE

## Microsoft research copilot experience

Discover more about research at Microsoft through our AI-powered experience

Opens in a new tab

## Why this matters

Ire statically reverse-engineers binaries and identifies the behavior from the function to the system level to describe what the software does and determine a verdict. The verdict of this sample came from a single Ire run because of the specific detail Ire was able to surface: function roles, packet layout, command IDs, persistence registry keys, and decoy strings. Ire never named LOTUSLITE in its report or chain of evidence. The family mapping is ours, after the fact, comparing Ire’s report against Acronis report. Ire described the behavior precisely enough to make the mapping straightforward of this sample to LOTUSLITE.

Stay up to date on the latest findings and other interesting sample detections from Project Ire by following along on our
[project page](https://www.microsoft.com/en-us/research/project/project-ire/)
.

Opens in a new tab