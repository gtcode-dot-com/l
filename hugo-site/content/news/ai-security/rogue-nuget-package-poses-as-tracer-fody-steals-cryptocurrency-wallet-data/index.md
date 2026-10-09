---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-17T12:03:16.381702+00:00'
exported_at: '2025-12-17T12:03:18.775330+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/rogue-nuget-package-poses-as-tracerfody.html
structured_data:
  about: []
  author: ''
  description: A fake NuGet package mimicking Tracer.Fody stayed online for years,
    stealing Stratis wallet files and passwords from Windows systems.
  headline: Rogue NuGet Package Poses as Tracer.Fody, Steals Cryptocurrency Wallet
    Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/rogue-nuget-package-poses-as-tracerfody.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Rogue NuGet Package Poses as Tracer.Fody, Steals Cryptocurrency Wallet Data
updated_at: '2025-12-17T12:03:16.381702+00:00'
url_hash: 0658990f23f25c47b2c45699fd6ce40d501d19bf
---

**

Dec 16, 2025
**

Ravie Lakshmanan

Cybersecurity / Cryptocurrency

Cybersecurity researchers have discovered a new malicious NuGet package that typosquats and impersonates the popular .NET tracing library and its author to sneak in a cryptocurrency wallet stealer.

The malicious package, named "
[Tracer.Fody.NLog](https://www.nuget.org/packages/Tracer.Fody.NLog)
," remained on the repository for nearly six years. It was published by a user named "csnemess" on February 26, 2020. It masquerades as "
[Tracer.Fody](https://www.nuget.org/packages/Tracer.Fody)
," which is maintained by "
[csnemes](https://github.com/csnemes/tracer)
." The package continues to remain available as of writing, and has been downloaded at least 2,000 times, out of which 19 took place over the last six weeks for version 3.2.4.

"It presents itself as a standard .NET tracing integration but in reality functions as a cryptocurrency wallet stealer," Socket security researcher Kirill Boychenko
[said](https://socket.dev/blog/malicious-nuget-package-typosquats-popular-net-tracing-library)
. "Inside the malicious package, the embedded Tracer.Fody.dll scans the default Stratis wallet directory, reads \*.wallet.json files, extracts wallet data, and exfiltrates it together with the wallet password to threat actor-controlled infrastructure in Russia at
[176.113.82[.]163](https://www.virustotal.com/gui/ip-address/176.113.82.163/)
."

The software supply chain security company said the threat leveraged a number of tactics that allowed it to elude casual review, including mimicking the legitimate maintainer by using a name that differs by a single letter ("csnemes" vs. "csnemess"), using Cyrillic lookalike characters in the source code, and hiding the malicious routine within a generic helper function ("Guard.NotNull") that's used during regular program execution.

Once a project references the malicious package, it activates its behavior by scanning the default Stratis wallet directory on Windows ("%APPDATA%\\StratisNode\\stratis\\StratisMain"), reads \*.wallet.json files and in-memory passwords, and exfiltrates them to the Russian-hosted IP address.

"All exceptions are silently caught, so even if the exfiltration fails, the host application continues to run without any visible error while successful calls quietly leak wallet data to the threat actor's infrastructure," Boychenko said.

Socket said the same IP address was previously put to use in December 2023 in
[connection](https://x.com/aSteveCleary/status/1730994352132911613)
with another NuGet impersonation attack in which the threat actor published a package named "Cleary.AsyncExtensions" under the alias "stevencleary" and incorporated functionality to siphon wallet seed phrases. The package was so-called to disguise itself as the
[AsyncEx NuGet library](https://github.com/StephenCleary/AsyncEx)
.

The findings once illustrate how malicious typosquats mirroring legitimate tools can stealthily operate without attracting any attention across the open-source repository ecosystems.

"Defenders should expect to see similar activity and follow-on implants that extend this pattern," Socket said. "Likely targets include other logging and tracing integrations, argument validation libraries, and utility packages that are common in .NET projects."