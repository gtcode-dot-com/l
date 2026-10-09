---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-08T21:44:02.336300+00:00'
exported_at: '2026-01-08T21:44:05.327346+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/the-state-of-trusted-open-source.html
structured_data:
  about: []
  author: ''
  description: Analysis shows most security risk sits in longtail open source images,
    with 98% of CVEs outside top projects & Critical flaws fixed in under 20 hours.
  headline: The State of Trusted Open Source
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/the-state-of-trusted-open-source.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: The State of Trusted Open Source
updated_at: '2026-01-08T21:44:02.336300+00:00'
url_hash: 64f4ef0912f681b0bf79d12858ad901b8ca0b5b9
---

Chainguard, the trusted source for open source, has a unique view into how modern organizations actually consume open source software and where they run into risk and operational burdens. Across a growing customer base and an extensive catalog of over 1800 container image projects, 148,000 versions, 290,000 images, and 100,000 language libraries, and almost half a billion builds, they can see what teams pull, deploy, and maintain day-to-day, along with the vulnerabilities and remediation realities that come hand in hand.

That's why they created
*The State of Trusted Open Source*
, a quarterly pulse on the open source software supply chain. As they analyzed anonymized product usage and CVE data, the Chainguard team noticed common themes around what open source engineering teams are actually building with and the risks associated.

Here's what they found:

* **AI is reshaping the baseline stack:**
  Python led the way as the most popular open source image among Chainguard's global customer base, powering the modern AI stack.
* **Over half of production happens outside of the most popular projects:**
  Most teams may standardize on a familiar set of images, but real-world infrastructure is powered by a broad portfolio that extends far beyond the top 20 most popular, which they refer to in this report as longtail images.
* **Popularity doesn't map to risk:**
  98% of the vulnerabilities found and remediated in Chainguard images occurred outside of the top 20 most popular projects. That means the biggest security burden accumulates in the less-visible part of the stack, where patching is hardest to operationalize.
* **Compliance can be the catalyst for action:**
  Compliance takes many forms today: from SBOM and vulnerability requirements to industry frameworks like PCI DSS, SOC 2, and regulations like the EU's Cyber Resilience Act. FIPS is just one example, focused specifically on U.S. federal encryption standards. Even so, 44% of Chainguard customers run a FIPS image in production, underscoring how frequently regulatory needs shape real-world software decisions.
* **Trust is built on remediation speed:**
  Chainguard eliminated Critical CVEs, on average, in under 20 hours.

Before we dive in, a note on the methodology: This report analyzes 1800+ unique container image projects, 10,100 total vulnerability instances, and 154 unique CVEs tracked from September 1, 2025, through November 30, 2025. When we use terms like "top 20 projects" and "longtail projects" (as defined by images outside of the top 20), we're referring to real usage patterns observed across Chainguard's customer portfolio and in production pulls.

## **Usage: What teams actually run in production**

If you zoom out, today's production container footprint looks exactly like you'd expect: foundational languages, runtimes, and infrastructure components dominate the most popular list.

### **Most popular images: AI is reshaping the baseline stack**

Across all regions, the top images are familiar staples: Python (71.7% of customers), Node (56.5%), nginx (40.1%), go (33.5%), redis (31.4%), followed by JDK, JRE, and a cluster of core observability and platform tooling like Grafana, Prometheus, Istio, cert-manager, argocd, ingress-nginx, and kube-state-metrics.

This indicates that customers operate a portfolio of critical building blocks – including languages, gateways, service mesh, monitoring, and controllers – that collectively form the foundation of their business.

It's not surprising to see Python leading the way globally, as the default glue language for the modern AI stack. Teams typically standardize on Python for model development, data pipelines, and increasingly for production inference services as well.

### **Most popular by region: Similar foundations, different longtail mix**

North America shows a broad and consistent set of default production building blocks: Python (71.7% of customers), Node (56.6%), nginx (39.8%), go (31.9%), redis (31.5%), plus strong penetration of Kubernetes ecosystem components (cert-manager, istio, argocd, prometheus, kube-state-metrics, node-exporter, kubectl). Notably, even utility images like busybox show up meaningfully.

Outside North America, the same core stack appears, but the portfolio spreads differently: Python (72% of customers), Node (55.8%), Go (44.2%), nginx (41.9%), and a noticeable presence of .NET runtimes (aspnet-runtime, dotnet-runtime, dotnet-sdk) and PostgreSQL.

### **The longtail of images is crucial to production, not edge cases**

Chainguard's most popular images represent only 1.37% of all available images and account for roughly half of all container pulls. The other half of production usage comes from everywhere else: 1,436 longtail images that make up 61.42% of the average customer's container portfolio.

In other words, half of all production workloads run on longtail images. These aren't edge cases. They're core to Chainguard's customers' infrastructure. It's relatively straightforward to keep the top handful of images polished, but what trusted open source requires is maintaining that security and velocity across the breadth of what customers actually run.

### **FIPS usage: Compliance is a catalyst for action**

FIPS encryption is an essential technology in the compliance landscape, focused on satisfying U.S. federal encryption requirements. And it offers a useful window into how regulatory pressure drives adoption. In the data, 44% of customers run at least one FIPS image in production.

The pattern is consistent: when working within compliance frameworks like FedRAMP, DoD IL-5, PCI DSS, SOC 2, CRA, Essential Eight or HIPAA, teams need hardened, trusted open source software that mirrors their commercial workloads. The most used FIPS images align with the broader portfolio, simply with cryptographic modules strengthened for audit and verification.

Top FIPS image projects include Python-fips (62% of customers with at least one FIPS image in production), Node-fips (50%), nginx-fips (47.2%), go-fips (33.8%), redis-fips (33.1%), plus platform components like istio-pilot-fips, istio-proxy-fips, and cert-manager variants. Even supporting libraries and crypto foundations show up, such as glibc-openssl-fips.

FIPS is not the whole story, but it illustrates a broader truth: compliance is a universal driver, emphasizing the need for trusted open source across the entire software stack.

## **CVEs: Popularity doesn't map to risk**

When looking across Chainguard's catalog of images, risk is overwhelmingly concentrated outside of the most popular images. Of the CVEs Chainguard remediated in the past three months, 214 occurred in the top 20 images, accounting for only 2% of the total CVEs. Go beyond those top images, and you'll find the other 98% of CVEs Chainguard remediated (10,785 CVE instances). That's 50 times the number of CVEs in the top 20 images!

The largest volume of CVEs are categorized as Medium, but operational urgency often stems from how quickly Critical and High CVEs are addressed, and whether customers can rely on that speed across their entire portfolio, not just the most common images.

## **Trust is built on remediation speed**

For us, trust is measured in time-to-fix, and Chainguard knows this is most important when it comes to Critical CVEs. During the three-month period analyzed, Chainguard's team achieved a less than 20-hour average remediation time for Critical CVEs, with 63.5% of Critical CVEs being resolved within 24 hours, 97.6% within two days, and 100% within three days.

In addition to Critical CVE remediation, the team addressed High CVEs in 2.05 days, Medium CVEs in 2.5 days, and Low CVEs in 3.05 days, notably faster than Chainguard's SLAs (seven days for Critical CVEs and 14 days for high, medium, and low CVEs).

And this speed isn't confined to the most popular packages. For every single CVE remediated in a top 20 image project, they resolved 50 CVEs in less-popular images.

That longtail is where most of your real exposure hides and it can feel hopeless trying to keep up. Most engineering organizations simply can't allocate resources to patch vulnerabilities in packages that fall outside their core stack, but the data makes it clear that you have to secure the "quiet majority" of your software supply chain with the same rigor as your most critical workloads.

## **A new baseline for trusted open source**

Across the data, one takeaway stands out: modern software is powered by a wide, shifting portfolio of open source components, most of which live outside the top 20 most popular images. That's not where developers spend their time, but it's where the bulk of security and compliance risk accumulates.

This creates a concerning disconnect: it's rational for engineering teams to focus on the small set of projects that matter most to their stack, but the majority of exposure sits in the vast set of dependencies they don't have the time to manage.

That's why breadth matters. Chainguard is built to absorb the operational burden of the longtail, providing coverage and remediation at a scale that individual teams can't justify on their own. As open source supply chains grow more complex, Chainguard will continue to track usage patterns and shine a light on where risk truly resides, so you don't have to fight the battle against the longtail alone.

*Ready to get started with the trusted source for open source?
[Contact Chainguard](https://www.chainguard.dev/contact?utm_source=the-hacker-news&utm_medium=paid-social&utm_campaign=THN-Jan26article)
to learn more.*

**Note:**
*This article was expertly written and contributed by Ed Sawma, VP Product Marketing, Sasha Itkis, Product Analyst.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.