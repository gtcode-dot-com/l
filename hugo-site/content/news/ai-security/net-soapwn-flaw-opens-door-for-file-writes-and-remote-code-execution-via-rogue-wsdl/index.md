---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-11T00:03:08.003283+00:00'
exported_at: '2025-12-11T00:03:10.801803+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/net-soapwn-flaw-opens-door-for-file.html
structured_data:
  about: []
  author: ''
  description: Research shows a .NET proxy design flaw enables file writes and RCE
    through attacker-supplied WSDL in multiple products.
  headline: .NET SOAPwn Flaw Opens Door for File Writes and Remote Code Execution
    via Rogue WSDL
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/net-soapwn-flaw-opens-door-for-file.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: .NET SOAPwn Flaw Opens Door for File Writes and Remote Code Execution via Rogue
  WSDL
updated_at: '2025-12-11T00:03:08.003283+00:00'
url_hash: 4a27cf66942d12daf2449d40d9ad0466a1e8f456
---

**

Dec 10, 2025
**

Ravie Lakshmanan

Enterprise Security / Web Services

New research has uncovered exploitation primitives in the .NET Framework that could be leveraged against enterprise-grade applications to achieve remote code execution.

WatchTowr Labs, which has codenamed the "invalid cast vulnerability"
**SOAPwn**
,
[said](https://labs.watchtowr.com/soapwn-pwning-net-framework-applications-through-http-client-proxies-and-wsdl/)
the issue impacts Barracuda Service Center RMM, Ivanti Endpoint Manager (EPM), and Umbraco 8. But the number of affected vendors is likely to be longer given the widespread use of .NET.

The findings were
[presented today](https://blackhat.com/eu-25/briefings/schedule/#soapwn-pwning-net-framework-applications-through-http-client-proxies-and-wsdl-49018)
by watchTowr security researcher Piotr Bazydlo at the Black Hat Europe security conference, which is being held in London.

SOAPwn essentially allows attackers to abuse Web Services Description Language (WSDL) imports and HTTP client proxies to execute arbitrary code in products built on the foundations of .NET due to errors in the way they handle Simple Object Access Protocol (
[SOAP](https://blog.postman.com/soap-api-definition/)
) messages.

"It is usually abusable through SOAP clients, especially if they are dynamically created from the attacker-controlled WSDL," Bazydlo said.

As a result, .NET Framework
[HTTP client proxies](https://httpwebclientprotocol)
can be manipulated into using file system handlers and achieve arbitrary file write by passing as URL something like "file://<attacker-controlled input>" into a SOAP client proxy, ultimately leading to code execution. To make matters worse, it can be used to overwrite existing files since the attacker controls the full write path.

In a hypothetical attack scenario, a threat actor could leverage this behavior to supply a Universal Naming Convention (
[UNC](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats#unc-paths)
) path (e.g., "file://attacker.server/poc/poc") and cause the SOAP request to be written to an SMB share under their control. This, in turn, can allow an attacker to capture the NTLM challenge and crack it.

That's not all. The research also found that a more powerful exploitation vector can be weaponized in applications that generate HTTP client proxies from WSDL files using the
[ServiceDescriptionImporter](https://learn.microsoft.com/en-us/dotnet/api/system.web.services.description.servicedescriptionimporter)
class by taking advantage of the fact that it does not validate the URL used by the generated HTTP client proxy.

In this technique, an attacker can provide a URL that points to a WSDL file they control to vulnerable applications, and obtain remote code execution by dropping a fully functional ASPX web shell or additional payloads like CSHTML web shells or PowerShell scripts.

Following responsible disclosure in March 2024 and July 2025, Microsoft has opted not to fix the vulnerability, stating the issue stems from either an application issue or behavior, and that "users should not consume untrusted input that can generate and run code."

The findings illustrate how expected behavior in a popular framework can become a potential exploit path that leads to NTLM relaying or arbitrary file writes. The issue has since been addressed in Barracuda Service Center RMM
[version 2025.1.1](https://campus.barracuda.com/product/managedworkplace/doc/93200432/release-notes/)
(
[CVE-2025-34392](https://nvd.nist.gov/vuln/detail/CVE-2025-34392)
, CVSS score: 9.8) and Ivanti EPM
[version 2024 SU4 SR1](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html#ivanti-releases-fix-for-critical-epm-flaw)
(
[CVE-2025-13659](https://nvd.nist.gov/vuln/detail/cve-2025-13659)
, CVSS score: 8.8).

"It is possible to make SOAP proxies write SOAP requests into files rather than sending them over HTTP," Bazydlo said. "In many cases, this leads to remote code execution through webshell uploads or PowerShell script uploads. The exact impact depends on the application using the proxy classes."