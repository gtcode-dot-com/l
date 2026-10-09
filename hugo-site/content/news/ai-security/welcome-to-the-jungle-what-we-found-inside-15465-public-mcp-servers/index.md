---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T21:15:15.918213+00:00'
exported_at: '2026-10-07T21:15:17.456993+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/welcome-to-jungle-what-we-found-inside.html
structured_data:
  about: []
  author: ''
  description: OX found no marketplace vetting across 15,465 indexed MCP servers,
    including expired domains and hosts routed through consumer tunnels.
  headline: 'Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/welcome-to-jungle-what-we-found-inside.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers'
updated_at: '2026-10-07T21:15:15.918213+00:00'
url_hash: a47789abd95458c6009e5b953bfaf452120be1e9
---

**

The Hacker News
**

Oct 06, 2026

Supply Chain / Artificial Intelligence

In 2024, MCP (Model Context Protocol) set out to become the USB-C of AI: one standard for connecting models, agents, and IDEs to tools and data. The protocol delivered. Thousands of developers built servers, and enterprises plugged them into agent workflows.

The ecosystem around it fell short. Earlier this year, our team
[at OX Security](https://www.ox.security/)
,  traced critical vulnerabilities in Anthropic's MCP source code, downloaded more than 150 million times. This time, we looked at what people actually install: community-published servers across the most popular MCP marketplaces. We found no guardrails and no review. Security is a recommendation, not a policy.

### **A Marketplace With No Bouncer**

In 2012, Google ran Bouncer, an automated scanner that checked Android apps for malware before they reached users. It wasn't perfect: researchers
[slipped malware past it](https://www.forbes.com/sites/andygreenberg/2012/05/23/researchers-say-they-snuck-malware-app-past-googles-bouncer-android-market-scanner/)
. But it existed. MCP marketplaces have no equivalent. Anyone can write a server, push it, and publish it.

Even a review wouldn't close the gap. At RSAC and OWASP last year, we presented "In GitHub We Trust: 10 Ways You Can Get Pwned," on how developers over-trust what they see in a repository. MCP repeats that mistake. Remote MCP servers can run backend code that differs entirely from what their public repository shows. Code review tells you what the developer published, not what the server runs.

### **Where Does Your Data Go?**

Over the past decade, enterprises built strict governance to adopt public cloud safely: data residency rules, Zero Trust boundaries, granular IAM, and supply chain audits. MCP connections often sit outside all of it.

To measure the gap, we analyzed 15,465 publicly indexed MCP servers across 5 MCP registries, deduplicated to 5,095 unique hostnames.

* **Hosted outside the US:**
  15.6% of hostnames resolve to infrastructure outside the United States, including 19 in China and 18 in Russia. An agent connected to these servers may send data to jurisdictions the security team never approved.
* **Running on personal machines:**
  0.45% route traffic through consumer tunneling services, mainly ngrok-free. These publicly listed servers run from personal machines and, likely, home networks.
* **Dangling domains:**
  2.3% no longer resolve. Six sit on expired domains that anyone can register for $4 to $12 a year. A new owner would inherit an established server identity, along with requests from any agent still configured to call it.

Location can also change. An operator could launch a server on a clean US IP address and later route traffic somewhere else.

**The full report covers our methodology, a prompt-injection proof of concept, and the threat scenarios behind each finding.
[Download "15,465 MCP Servers, 0 Governance"](https://www.ox.security/ebooks/15465-mcp-servers-0-governance/)**

### **Trust Is the Attack Surface**

The protocol isn't the problem. The trust we hand it is. Until marketplaces add vetting, code signing, and origin verification, the enterprise has to do that work.

**It's still a jungle out there. Make sure you're not the prey.**

**[Get the full report, "15,465 MCP Servers, 0 Governance"](https://www.ox.security/ebooks/15465-mcp-servers-0-governance/)**

**Want to go further?**
Join our live webinar, "
[The AI Attack Surface Is Already in Your Cloud](https://www.ox.security/webinars/how-ai-is-changing-the-threats-and-expectations-of-cloud-security-tools/)
," on October 13 at 12:00 PM ET. Latio founder and CEO James Berthoty and OX Field CTO Chris Lindsey will cover how AI is reshaping cloud threats and what security teams should do about it.
**[Register](https://www.ox.security/webinars/how-ai-is-changing-the-threats-and-expectations-of-cloud-security-tools/)**

**Note:**
*This article has been expertly written and contributed by Moshe Siman Tov Bustan, Security Research Team Lead, OX Security.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.