---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-12T22:51:24.783051+00:00'
exported_at: '2025-11-12T22:54:40.076412+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/new-browser-security-report-reveals.html
structured_data:
  about: []
  author: ''
  description: New 2025 report reveals browsers now drive 32% of corporate data leaks
    through GenAI and extensions.
  headline: New Browser Security Report Reveals Emerging Threats for Enterprises
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/new-browser-security-report-reveals.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New Browser Security Report Reveals Emerging Threats for Enterprises
updated_at: '2025-11-12T22:51:24.783051+00:00'
url_hash: 84bd8b21bbca061c38670fad3d949ab518301000
---

According to the new
*[Browser Security Report 2025](https://go.layerxsecurity.com/browser-security-report-2025?utm_source=THN&utm_campaign=Browser_security_report2025)*
, security leaders are discovering that most identity, SaaS, and AI-related risks converge in a single place, the user's browser. Yet traditional controls like DLP, EDR, and SSE still operate one layer too low.

What's emerging isn't just a blindspot. It's a parallel threat surface: unmanaged extensions acting like supply chain implants, GenAI tools accessed through personal accounts, sensitive data copy/pasted directly into prompt fields, and sessions that bypass SSO altogether.

This article unpacks the key findings from the report and what they reveal about the shifting locus of control in enterprise security.

## **GenAI Is Now the Top Data Exfiltration Channel**

The rise of GenAI in enterprise workflows has created a massive governance gap. Nearly half of employees use GenAI tools, but most do so through unmanaged accounts, outside of IT visibility.

#### **Key stats from the report:**

* **77%**
  of employees paste data into GenAI prompts
* **82%**
  of those pastes come from personal accounts
* **40%**
  of uploaded files contain
  **PII or PCI**
* GenAI accounts for
  **32%**
  of all corporate-to-personal data movement

Legacy DLP tools weren't designed for this. The browser has become the dominant channel for copy/paste exfiltration, unmonitored and policy-free.

## **AI Browsers Are An Emerging Threat Surface**

Another emerging browser-based threat surface is 'agentic' AI browsers, which blend the traditional security risks of browsers with the new concerns over AI usage.

AI browsers like OpenAI's Atlas, Arc Search, and Perplexity Browser are redefining how users interact with the web, merging search, chat, and browsing into a single intelligent experience. These browsers integrate large language models directly into the browsing layer, enabling them to read, summarize, and reason over any page or tab in real time. For users, this means seamless productivity and contextual assistance. But for enterprises, it represents a new and largely unmonitored attack surface: an "always-on co-pilot" that quietly sees and processes everything an employee can, without policy enforcement or visibility into what's being shared with the cloud.

The risks are significant and multifaceted: session memory leakage exposes sensitive data through AI-powered personalization; invisible "auto-prompting" sends page content to third-party models; and shared cookies blur identity boundaries, enabling potential hijacks. With no enterprise-grade guardrails, these AI browsers effectively bypass traditional DLP, SSE, and browser security tools, creating a file-less, invisible path for data exfiltration. As organizations embrace GenAI and SaaS-driven workflows, understanding and addressing this emerging blind spot is critical to preventing the next generation of data leaks and identity compromises.

## **Browser Extensions: The Most Widespread and Least Governed Supply Chain**

99% of enterprise users have at least one extension installed. Over half grant high or critical permissions. Many are either sideloaded or published by Gmail accounts, with no verification, updates, or accountability.

#### **From the telemetry:**

* **26%**
  of extensions are sideloaded
* **54%**
  are published by Gmail accounts
* **51%**
  haven't been updated in over a year
* **6%**
  of GenAI-related extensions are classified as malicious

This isn't about productivity anymore, it's an unmanaged software supply chain embedded in every endpoint.

## **Identity Governance Ends at the IdP. Risk Starts in the Browser.**

The report finds that over two-thirds of logins happen outside of SSO, and nearly half use personal credentials, making it impossible for security teams to know who is accessing what, or from where.

#### **Breakdown:**

* **68%**
  of corporate logins are done without SSO
* **43%**
  of SaaS logins use personal accounts
* **26%**
  of users reuse passwords across multiple accounts
* **8%**
  of browser extensions access users' identities or cookies

Attacks like
**Scattered Spider**
proved this: browser session tokens, not passwords, are now the primary target.

## **SaaS and Messaging Apps Are Quietly Exfiltrating Sensitive Data**

Workflows that once relied on file uploads have shifted toward browser-based pasting, AI prompting, and third-party plugins. Most of this activity now occurs in the browser layer, not the app.

#### **Observed behaviors:**

* **62%**
  of pastes into messaging apps include PII/PCI
* **87%**
  of that happens via non-corporate accounts
* On average, users paste
  **4 sensitive snippets per day**
  into non-corporate tools

In incidents like the
**Rippling/Deel**
leak, the breach didn't involve malware or phishing, it came from unmonitored chat apps inside the browser.

## **Traditional Tools Weren't Built for This Layer**

EDR sees processes. SSE sees network traffic. DLP scans files. None of them inspect what's happening
*inside*
the session, like which SaaS tab is open, what data is being pasted, or which extension is injecting scripts.

Security teams are blind to:

* Shadow AI usage and prompt inputs
* Extension activity and code changes
* Personal vs. corporate account crossovers
* Session hijacking and cookie theft

That's why securing the browser requires a new approach.

## **Session-Native Controls Are the Next Frontier**

To regain control, security teams need browser-native visibility, capabilities that operate at the session level without disrupting user experience.

What this includes:

* Monitoring copy/paste and uploads across apps
* Detecting unmanaged GenAI tools and extensions
* Enforcing session isolation and SSO everywhere
* Applying DLP to non-file-based interactions

A modern browser security platform, like the one outlined in the full report, can provide these controls without forcing users onto a new browser.

## **Read the Full Report to See the Blindspots You're Missing**

The
*[Browser Security Report 2025](https://go.layerxsecurity.com/browser-security-report-2025?utm_source=THN&utm_campaign=Browser_security_report2025)*
offers a data-rich view into how the browser has quietly become the most critical and vulnerable endpoint in the enterprise. With insights from millions of real browser sessions, it maps where today's controls fail and where modern breaches begin.

**[Download the full report](https://go.layerxsecurity.com/browser-security-report-2025?utm_source=THN&utm_campaign=Browser_security_report2025)
to see what traditional controls are missing, and what top CISOs are doing next.**

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.