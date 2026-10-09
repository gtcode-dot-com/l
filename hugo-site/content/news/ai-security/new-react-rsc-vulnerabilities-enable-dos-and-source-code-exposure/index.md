---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-14T12:03:14.827677+00:00'
exported_at: '2025-12-14T12:03:17.460706+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/new-react-rsc-vulnerabilities-enable.html
structured_data:
  about: []
  author: ''
  description: React patches three RSC bugs causing DoS and code exposure, urging
    updates to fixed 19.x releases.
  headline: New React RSC Vulnerabilities Enable DoS and Source Code Exposure
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/new-react-rsc-vulnerabilities-enable.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New React RSC Vulnerabilities Enable DoS and Source Code Exposure
updated_at: '2025-12-14T12:03:14.827677+00:00'
url_hash: c2ebc06b03d06ff0cf0d00cd5b789e04f80be147
---

**

Dec 12, 2025
**

Ravie Lakshmanan

Software Security / Vulnerability

The React team has
[released](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)
fixes for two new types of flaws in React Server Components (RSC) that, if successfully exploited, could result in denial-of-service (DoS) or source code exposure.

The team said the issues were found by the security community while attempting to exploit the patches released for CVE-2025-55182 (CVSS score: 10.0), a critical bug in RSC that has since been
[weaponized in the wild](https://thehackernews.com/2025/12/react2shell-exploitation-escalates-into.html)
.

The three vulnerabilities are listed below -

* **[CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184)**
  (CVSS score: 7.5) - A pre-authentication denial of service vulnerability arising from unsafe deserialization of payloads from HTTP requests to Server Function endpoints, triggering an infinite loop that hangs the server process and may prevent future HTTP requests from being served
* **[CVE-2025-67779](https://www.cve.org/CVERecord?id=CVE-2025-67779)**
  (CVSS score: 7.5) - An incomplete fix for CVE-2025-55184 that has the same impact
* **[CVE-2025-55183](https://www.cve.org/CVERecord?id=CVE-2025-55183)**
  (CVSS score: 5.3) - An information leak vulnerability that may cause a specifically crafted HTTP request sent to a vulnerable Server Function to return the source code of any Server Function

However, successful exploitation of CVE-2025-55183 requires the existence of a Server Function that explicitly or implicitly exposes an argument that has been converted into a string format.

The flaws affecting the following versions of react-server-dom-parcel, react-server-dom-turbopack, and react-server-dom-webpack -

* **CVE-2025-55184 and CVE-2025-55183**
  - 19.0.0, 19.0.1 19.1.0, 19.1.1, 19.1.2, 19.2.0 and 19.2.1
* **CVE-2025-67779**
  - 19.0.2, 19.1.3 and 19.2.2

Security researchers RyotaK and Shinsaku Nomura have been credited with reporting the two DoS bugs to the Meta Bug Bounty program, while Andrew MacPherson has been acknowledged for reporting the information leak flaw.

Users are advised to update to
**versions 19.0.3, 19.1.4, and 19.2.3**
as soon as possible, particularly in light of active exploration of CVE-2025-55182.

"When a critical vulnerability is disclosed, researchers scrutinize adjacent code paths looking for variant exploit techniques to test whether the initial mitigation can be bypassed," the React team said. "This pattern shows up across the industry, not just in JavaScript. Additional disclosures can be frustrating, but they are generally a sign of a healthy response cycle."