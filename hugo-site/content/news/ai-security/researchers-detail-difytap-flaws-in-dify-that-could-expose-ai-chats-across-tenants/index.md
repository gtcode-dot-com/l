---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:51:08.199346+00:00'
exported_at: '2026-06-23T03:51:10.702045+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html
structured_data:
  about: []
  author: ''
  description: Four DifyTap flaws could expose private AI chats and files across Dify
    tenants; three are fixed in version 1.14.2.
  headline: Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across
    Tenants
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across
  Tenants
updated_at: '2026-06-23T03:51:08.199346+00:00'
url_hash: c63ab8f2419e5c1cd7af45be9c95d83743b0480d
---

**

Ravie Lakshmanan
**

Jun 22, 2026

AI Security / Vulnerability

Cybersecurity researchers have disclosed details of four vulnerabilities in
[Dify](https://dify.ai/)
, an open-source agentic workflow platform with more than
[146,000 GitHub stars](https://github.com/langgenius/dify)
, that could allow attackers to stealthily read artificial intelligence (AI) conversions from other customers' applications without requiring authentication.

The vulnerabilities have been collectively codenamed
**DifyTap**
by Zafran Security.

"Two were critical severity, two required no authentication, and three carried cross-tenant impact on Dify's multi-tenant cloud service, allowing one customer's data to be exposed to another," researchers Ido Shani and Gal Zaban
[said](https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps)
.

The security defects could have allowed attackers to read private AI chats from other customers' applications, creating a covert exfiltration channel for every message and model response.

They also made it possible to traverse Dify's internal Plugin Daemon API from unauthenticated requests and trigger cross-tenant internal API calls, as well as preview documents uploaded by other tenants and leak files across users within a tenant by attaching another user's file unique identifier.

Separately, Zafran said it also discovered that Dify's file parsing stack relied on a version of PDFium, an open-source C++ library for PDF rendering, that was vulnerable to
[CVE-2024-5846](https://nvd.nist.gov/vuln/detail/CVE-2024-5846)
(CVSS score: 8.8), a two-year-old use-after-free bug that could allow a remote attacker to potentially exploit heap corruption via a crafted PDF file.

The remaining vulnerabilities are listed below -

* **[CVE-2026-41947](https://nvd.nist.gov/vuln/detail/CVE-2026-41947)**
  (CVSS score: 9.1) - An authorization bypass vulnerability that allows authenticated editor users to set and enable trace configurations for any application regardless of tenant ownership.
* **[CVE-2026-41948](https://nvd.nist.gov/vuln/detail/CVE-2026-41948)**
  (CVSS score: 9.4) - A path traversal vulnerability that allows authenticated users to manipulate requests forwarded to the Plugin Daemon's internal REST API by exploiting insufficient URL path sanitization and access internal, private endpoints.
* **[CVE-2026-41949](https://nvd.nist.gov/vuln/detail/CVE-2026-41949)**
  (CVSS score: 7.5/5.9) - An authorization bypass vulnerability in the file preview endpoint ("/console/api/files/{file\_id}/preview") that allows any authenticated user to read up to 3,000 characters of any uploaded document across all tenants and workspaces using only the file's UUID.
* **[CVE-2026-41950](https://nvd.nist.gov/vuln/detail/CVE-2026-41950)**
  (CVSS score: 6.5) - An authorization bypass vulnerability that allows authenticated users to read the full contents of files uploaded by other users within the same tenant by supplying an arbitrary file UUID in the files array of a chat-messages request.

The missing tenant ownership checks can be exploited to redirect all messages and responses from victim applications to an attacker-controlled LLM trace provider. It's worth noting that anyone can freely register for a Dify account.

"Consequently, an attacker can configure their own tracing for any application they can access as a client, which includes all publicly accessible applications," the researchers explained. "This allows an attacker to create a persistent exfiltration channel for all messages and responses sent in the application."

Following responsible disclosure, all vulnerabilities barring CVE-2026-41948 have been addressed in
[version 1.14.2](https://github.com/langgenius/dify/releases/tag/1.14.2)
, which was shipped last month. A fix for the pending flaw is expected to be made available in the next release of Dify.

"DifyTap demonstrates where the challenge lies in vulnerability visibility, particularly in container images, where differences between deployments can create visibility gaps that traditional scanners cannot detect," the company
[said](https://www.linkedin.com/posts/zafran-labs-has-disclosed-difytap-%F0%9D%97%B3%F0%9D%97%BC%F0%9D%98%82-share-7474558469791014912-vqrq/)
.