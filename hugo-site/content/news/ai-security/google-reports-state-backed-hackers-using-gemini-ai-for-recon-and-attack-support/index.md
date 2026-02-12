---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-12T19:31:02.589510+00:00'
exported_at: '2026-02-12T19:31:06.500714+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html
structured_data:
  about: []
  author: ''
  description: Google finds nation-state hackers abusing Gemini AI for target profiling,
    phishing kits, malware staging, and model extraction attacks.
  headline: Google Reports State-Backed Hackers Using Gemini AI for Recon and Attack
    Support
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Reports State-Backed Hackers Using Gemini AI for Recon and Attack Support
updated_at: '2026-02-12T19:31:02.589510+00:00'
url_hash: b9e620c1d14d430dfa5dcb2a74b2e92350dd0b38
---

**

Ravie Lakshmanan
**

Feb 12, 2026

Cyber Espionage / Artificial Intelligence

Google on Thursday said it observed the North Korea-linked threat actor known as
**UNC2970**
using its generative artificial intelligence (AI) model Gemini to conduct reconnaissance on its targets, as various hacking groups
[continue](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html)
to weaponize the tool for accelerating various phases of the cyber attack life cycle, enabling information operations, and even conducting model extraction attacks.

"The group used Gemini to synthesize OSINT and profile high-value targets to support campaign planning and reconnaissance," Google Threat Intelligence Group (GTIG)
[said](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use)
in a report shared with The Hacker News. "This actor's target profiling included searching for information on major cybersecurity and defense companies and mapping specific technical job roles and salary information."

The tech giant's threat intelligence team characterized this activity as a blurring of boundaries between what constitutes routine professional research and malicious reconnaissance, allowing the state-backed actor to craft tailored phishing personas and identify soft targets for initial compromise.

[UNC2970](https://thehackernews.com/2024/09/north-korean-hackers-target-energy-and.html)
is the moniker assigned to a North Korean hacking group that overlaps with a cluster that's tracked as Lazarus Group, Diamond Sleet, and Hidden Cobra. It's best known for orchestrating a long-running campaign codenamed
[Operation Dream Job](https://thehackernews.com/2025/10/north-korean-hackers-lure-defense.html)
to target aerospace, defense, and energy sectors with malware under the guise of approaching victims under the pretext of job openings.

GTIG said UNC2970 has "consistently" focused on defense targeting and impersonating corporate recruiters in their campaigns, with the target profiling
[including](https://cloud.google.com/blog/topics/threat-intelligence/threats-to-defense-industrial-base)
searches for "information on major cybersecurity and defense companies and mapping specific technical job roles and salary information."

UNC2970 is far from the only threat actor to have misused Gemini to augment their capabilities and move from initial reconnaissance to active targeting at a faster clip. Some of the other hacking crews that have integrated the tool into their workflows are as follows -

* **UNC6418**
  (Unattributed), to conduct targeted intelligence gathering, specifically seeking out sensitive account credentials and email addresses.
* **[Temp.HEX or Mustang Panda](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)**
  (China), to compile a dossier on specific individuals, including targets in Pakistan, and to gather operational and structural data on separatist organizations in various countries.
* **[APT31 or Judgement Panda](https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html)**
  (China), to automate the analysis of vulnerabilities and generate targeted testing plans by claiming to be a security researcher.
* **[APT41](https://thehackernews.com/2025/09/china-linked-apt41-hackers-target-us.html)**
  (China), to extract explanations from open-source tool README.md pages, as well as troubleshoot and debug exploit code.
* **UNC795**
  (China), to troubleshoot their code, conduct research, and develop web shells and scanners for PHP web servers.
* **[APT42](https://thehackernews.com/2025/11/iranian-hackers-launch-spearspecter-spy.html)**
  (Iran), to facilitate reconnaissance and targeted social engineering by crafting personas that induce engagement from the targets, as well as develop a Python-based Google Maps scraper, develop a SIM card management system in Rust, and research the use of a proof-of-concept (PoC) for a WinRAR flaw (
  [CVE-2025-8088](https://thehackernews.com/2026/01/google-warns-of-active-exploitation-of.html)
  ).

Google also said it detected a malware called HONESTCUE that leverages Gemini's API to outsource functionality generation for the next-stage, along with an AI-generated phishing kit codenamed COINBAIT that's built using Lovable AI and masquerades as a cryptocurrency exchange for credential harvesting. Some aspects of COINBAIT-related activity have been attributed to a financially motivated threat cluster dubbed UNC5356.

"HONESTCUE is a downloader and launcher framework that sends a prompt via Google Gemini's API and receives C# source code as the response," it said. "However, rather than leveraging an LLM to update itself, HONESTCUE calls the Gemini API to generate code that operates the 'stage two' functionality, which downloads and executes another piece of malware."

The fileless secondary stage of HONESTCUE then takes the generated C# source code received from the Gemini API and uses the legitimate .NET
[CSharpCodeProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.csharp.csharpcodeprovider)
framework to compile and execute the payload directly in memory, thereby leaving no artifacts on disk.

Google has also called attention to a recent wave of ClickFix campaigns that leverage the public sharing feature of generative AI services to host realistic-looking instructions to fix a common computer issue and ultimately deliver information-stealing malware. The activity was
[flagged](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html#ai-chat-guides-spread-stealers)
in December 2025 by Huntress.

Lastly, the company said it identified and disrupted model extraction attacks that are aimed at systematically querying a proprietary machine learning model to extract information and build a substitute model that mirrors the target's behavior. In a large-scale attack of this kind, Gemini was targeted by over 100,000 prompts that posed a series of questions aimed at replicating the model's reasoning ability across a broad range of tasks in non-English languages.

Last month, Praetorian devised a PoC extraction attack where a replica model achieved an accuracy rate of 80.1% simply by sending a series of 1,000 queries to the victim's API and recording the outputs and training it for 20
[epochs](https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/)
.

"Many organizations assume that keeping model weights private is sufficient protection," security researcher Farida Shafik
[said](https://www.praetorian.com/blog/stealing-ai-models-through-the-api-a-practical-model-extraction-attack/)
. "But this creates a false sense of security. In reality, behavior is the model. Every query-response pair is a training example for a replica. The model’s behavior is exposed through every API response."