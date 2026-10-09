---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-04T00:03:07.738524+00:00'
exported_at: '2025-12-04T00:03:10.715924+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/critical-rsc-bugs-in-react-and-nextjs.html
structured_data:
  about: []
  author: ''
  description: Critical RSC flaws in React and Next.js enable unauthenticated remote
    code execution; users should update to patched versions now.
  headline: Critical RSC Bugs in React and Next.js Allow Unauthenticated Remote Code
    Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/critical-rsc-bugs-in-react-and-nextjs.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Critical RSC Bugs in React and Next.js Allow Unauthenticated Remote Code Execution
updated_at: '2025-12-04T00:03:07.738524+00:00'
url_hash: 6fd2aab019d7b14efc14e82fd405e3093d08b0ca
---

**

Dec 03, 2025
**

Ravie Lakshmanan

Vulnerability / Cloud Security

A maximum-severity security flaw has been disclosed in React Server Components (RSC) that, if successfully exploited, could result in remote code execution.

The vulnerability, tracked as CVE-2025-55182, carries a CVSS score of 10.0.

It allows "unauthenticated remote code execution by exploiting a flaw in how React decodes payloads sent to React Server Function endpoints," the React Team
[said](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)
in an alert issued today.

"Even if your app does not implement any React Server Function endpoints, it may still be vulnerable if your app supports React Server Components."

According to cloud security firm
[Wiz](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182)
, the issue is a case of logical deserialization that stems from processing RSC payloads in an unsafe manner. As a result, an unauthenticated attacker could craft a malicious HTTP request to any Server Function endpoint that, when deserialized by React, achieves execution of arbitrary JavaScript code on the server.

The vulnerability impacts versions 19.0, 19.1.0, 19.1.1, and 19.2.0 of the following npm packages -

* react-server-dom-webpack
* react-server-dom-parcel
* react-server-dom-turbopack

It has been addressed in versions 19.0.1, 19.1.2, and 19.2.1. New Zealand-based security researcher
[Lachlan Davidson](https://lachlan.nz/about)
has been credited with discovering and reporting the flaw on November 29, 2025.

It's worth noting that the vulnerability also
[affects](https://vercel.com/changelog/cve-2025-55182)
Next.js using App Router. The issue has been
[assigned](https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp)
the CVE identifier CVE-2025-66478 (CVSS score: 10.0). It impacts versions >=14.3.0-canary.77, >=15, and >=16. Patched versions are 16.0.7, 15.5.7, 15.4.8, 15.3.6, 15.2.6, 15.1.9, and 15.0.5.

That said, any library that bundles RSC is likely to be affected by the flaw. This includes, but is not limited to, Vite RSC plugin, Parcel RSC plugin, React Router RSC preview, RedwoodJS, and Waku.

Wiz said 39% of cloud environments have instances vulnerable to CVE-2025-55182 and/or CVE-2025-66478. In light of the severity of the vulnerability, it's advised that users apply the fixes as soon as possible for optimal protection.