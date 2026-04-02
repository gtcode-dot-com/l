---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T14:15:14.520710+00:00'
exported_at: '2026-04-02T14:15:17.320287+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/the-state-of-trusted-open-source-report.html
structured_data:
  about: []
  author: ''
  description: AI-driven development increased CVEs by 145% from Dec 2025–Feb 2026,
    accelerating remediation and reshaping software supply chain security.
  headline: The State of Trusted Open Source Report
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/the-state-of-trusted-open-source-report.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The State of Trusted Open Source Report
updated_at: '2026-04-02T14:15:14.520710+00:00'
url_hash: 216e4b0eaf2d53000e75267df9b7378e7bb1b4b0
---

In
[December 2025](https://www.chainguard.dev/unchained/the-state-of-trusted-open-source-december-2025)
, we shared the first-ever
*The State of Trusted Open Source*
report, featuring insights from our product data and customer base on open source consumption across our catalog of container image projects, versions, images, language libraries, and builds. These insights shed light on what teams pull, deploy, and maintain day to day, alongside the vulnerabilities and remediation realities these projects face.

Fast forward a few months, and software development is accelerating at a pace that most didn’t see coming. AI is increasingly embedded across the development lifecycle, from code generation to infrastructure automation, as models become more advanced and better at meeting the demands of modern work. This shift is expanding what teams can build and how quickly they can ship.

It is also reshaping the security landscape.

Before diving into the numbers, it’s important to explain how we perform this analysis. We examined over 2,200 unique container image projects, 33,931 total vulnerability instances, and 377 unique CVEs from December 1, 2026, through February 28, 2026. When we use terms like “top 20 projects” and “long tail projects” (as defined by images outside of the top 20), we’re referring to real usage patterns observed across our customer portfolio and in production pulls.

In this report, we noticed a few new themes that point to this shift. These themes built on the trends from our last report, ultimately showcasing the impact of increased AI-driven development both in the types of container images being used and in the number of CVEs being discovered and remediated:

* **Python and PostgreSQL growth reflects AI-driven development:**
  Python remains the most popular image (72.1% of all customers use it), and PostgreSQL saw a 73% increase in usage quarter-over-quarter, underscoring the growing adoption of a modern AI stack across various use cases.
* **The modern platform stack is becoming increasingly standardized:**
  Across Chainguard customers, language ecosystem images account for more than half of the top 25 images used in production.
* **Chainguard Base is becoming a foundation for developer tooling:**
  The
  [chainguard-base](https://images.chainguard.dev/directory/image/chainguard-base/versions)
  image, a minimal distroless base image without any toolchain or apps, was the 5th most-used Chainguard image, as customers use it as a sort of “utility belt” for their specific use cases (over 75% of Chainguard customers customize at least one image).
* **AI is accelerating software development and vulnerability discovery:**
  We applied over 300% more fixes in Chainguard Containers and saw a 145% increase in vulnerabilities from last quarter, signaling the use of AI to push more code and discover more CVEs.
* **The long tail continues to define real-world risk:**
  96% of the vulnerabilities found and remediated in Chainguard Containers occurred outside of the top 20 most popular projects—this is consistent with the findings from December.
* **Compliance continues to drive adoption of trusted open source:**
  We saw the same themes from December present here, underscored by a FIPS-compliant variant of a Chainguard container image entering the top 10 images by customer count for the first time.

## **Usage: What teams actually run in production**

We identified multiple themes centered on the prevalence of AI in code generation across regions and industries. This prevalence leads to greater adoption of the Python language ecosystem and adjacent technologies on the usage side.

### **Most popular images: Python and PostgreSQL growth reflect AI-driven development**

#### **PostgreSQL usage grew 73% quarter-over-quarter**

The images that saw the strongest growth this quarter closely align with the technologies driving AI adoption.

Python remains the most widely deployed image across Chainguard customers. When combining FIPS (
[Federal Information Processing Standards](https://edu.chainguard.dev/chainguard/fips/understanding-fips/)
) and non-FIPS variants,
**72.1% of Chainguard customers are using a Python image**
. This reflects Python’s role as the default language for machine learning, data pipelines, and automation. What was once concentrated in experimentation environments is now moving into production systems across industries.

Node continues to anchor application infrastructure, with 60.7% of Chainguard customers utilizing it in their environments. Together, Python and Node define the dominant runtime layer for modern applications.

The most notable change this quarter is in databases.
**PostgreSQL usage grew by 73% quarter over quarter**
, the largest increase among widely deployed images.

This growth aligns with broader trends in AI workloads. PostgreSQL is increasingly used as a foundation for vector search and retrieval-augmented generation, supported by extensions that enable embedding storage and similarity queries. As AI moves into production, databases are evolving alongside application runtimes.

### **The modern platform stack is converging**

#### **Over 50% of the most popular images are language ecosystems**

This quarter, the data showed that production environments are converging around a consistent set of foundational components.

**Language ecosystems account for more than half of the top 25 images used across customers**
. Python (72.1% of all customers), Node (60.7%), Java (44.4%), Go (42.8%), and .NET (27%) continue to define the runtime layer, with growth across each ecosystem.

Outside of runtimes, teams are standardizing on a familiar set of cloud-native components. Traffic management tools such as nginx and service mesh components remain widely deployed. Monitoring systems built around Prometheus continue to expand. Deployment workflows are increasingly anchored in GitOps tools such as ArgoCD and kubectl.

The result is a layered architecture that is broadly consistent across organizations. A small number of runtimes, a shared set of operational components, and a large and highly variable long tail of supporting dependencies.

Standardization is happening at the platform level, even as application-specific variation continues to grow.

### **Chainguard Base is becoming a foundation for developer tooling**

#### **Chainguard-base was the 5th most-deployed image by customer count**

[Chainguard Base](https://images.chainguard.dev/directory/image/chainguard-base/versions)
is a minimal distroless base image without any toolchain or applications. It is designed to provide a secure foundation that teams can extend with only the components they need.

This quarter, it was the
**5th-most-deployed image by customer count**
, used by 36.3% of customers across FIPS and non-FIPS variants.

Its role becomes clearer when looking at customization patterns. Across all customized repositories, 95% include added packages, and
**more than three-quarters of customers customize at least one image**
.

When organizations customize Chainguard Containers, the most frequently added packages are developer and operational utilities such as curl, bash, jq, git, and cloud tooling. These are not full application stacks. They are the tools needed to build, debug, and operate software.

This demonstrates a consistent pattern: teams use Chainguard Base as a secure starting point, then layer in the exact tooling required for their workflows. It is serving as a flexible foundation for CI/CD pipelines, debugging environments, and internal platform tooling.

As platform engineering practices mature, the need for secure, customizable base environments is becoming more pronounced. Chainguard Base is emerging as a core building block in that model.

## **CVEs: AI is accelerating software development and vulnerability discovery**

### **Over 300% more fix instances this quarter**

Just as we observed on the usage side with the increase in Python and PostgreSQL container images, AI is also changing the speed at which vulnerabilities surface.

In the previous report, we tracked 154 unique CVEs and 10,100 fix instances across Chainguard Containers. This quarter, that number rose to 377 unique CVEs and 33,931 fix instances (
**a 145% increase in unique vulnerabilities and over 300% more fixes applied compared to last quarter**
).

This increase reflects two parallel forces: 1) development is becoming faster and more distributed, which increases the number of dependencies entering production environments; and 2) vulnerability discovery is accelerating as researchers and attackers use automation and AI-assisted techniques to analyze code at scale.

The result is a tighter feedback loop between development and security. More code is being written, more dependencies are being introduced, and more vulnerabilities are being identified across the ecosystem.

What stands out is not only the increase in volume, but the Chainguard Factory’s ability to respond to it.
**Median remediation time held essentially flat at 2.0 days compared to 1.96 days last quarter, despite the much higher volume**
. High-severity vulnerabilities continued to be resolved quickly, with 97.9% fixed within one week.

The pace of discovery is increasing. The expectation for response is keeping up.

## **The long tail continues to define real-world risk**

### **96% of CVEs occur outside the most popular images**

While core infrastructure is becoming more standardized, most of the software supply chain lives outside the most visible components. Let us explain: the median customer sources about 74% of their images from the long tail of the catalog (images outside the top 20 in popularity). This reflects the reality that production environments extend far beyond a small set of widely used images.

Security risk follows the same pattern.

This quarter,
**96.2% of CVE instances occurred outside the top 20 most widely used images**
. This is consistent with the previous report, which found that nearly all vulnerabilities were concentrated in long-tail projects.

The implication is straightforward: the images that teams interact with most frequently represent only a small portion of their actual exposure. The majority of vulnerabilities exist in dependencies that are less visible, less frequently updated, and often not directly owned by application teams.

Even across severity levels, the distribution holds. Critical, High, Medium, and Low vulnerabilities all follow the same pattern, with the overwhelming majority (96.18% on average) occurring outside the top 20 images. Attackers know what is popular, so they tend to look for vulnerable areas that are outside most users' top-of-mind.

As development accelerates and dependency graphs expand, managing the long tail becomes the central challenge of software supply chain security.

## **Compliance is reshaping adoption patterns**

Regulatory requirements are increasingly influencing how organizations build and deploy software.

This quarter marks the first time a FIPS-compliant Chainguard image (
[python-fips](https://images.chainguard.dev/directory/image/python-fips/versions)
) has reached the top 10 by customer count, even when FIPS and non-FIPS variants are combined into a single metric. This milestone reflects a broader shift toward compliance-driven adoption.

FIPS adoption is increasing across multiple runtimes. Python FIPS, Node FIPS, and nginx FIPS images all saw growth in customer counts over the quarter.

Overall,
**42% of customers now run at least one FIPS image in production**
.

This reflects the growing influence of frameworks such as FedRAMP, PCI DSS, SOC 2, and the EU Cyber Resilience Act. Compliance is no longer limited to a subset of industries. It is becoming a baseline requirement for software that operates in regulated environments.

As a result, secure and compliant images are moving from optional to expected.

## **A secure foundation for the AI era**

The data from this quarter points to a clear trend. Software ecosystems are expanding. The number of unique images in use grew by 18%, reflecting broader adoption and more diverse workloads. At the same time, vulnerability discovery increased significantly, with a
**145% rise in unique CVEs**
and a 3x increase in fixes.

Despite that growth, Chainguard’s remediation performance remained stable. Median fix times held steady, and high-severity vulnerabilities continued to be resolved quickly. This combination matters. It shows that it is possible to scale both coverage and responsiveness simultaneously.

As AI continues to accelerate development, the volume of code and dependencies will grow. The challenge for security teams is not simply to keep up with that growth, but to manage it in a way that maintains consistency and trust. The organizations that succeed will be those that treat security as part of the development system itself, rather than as a layer applied afterward.

At Chainguard, we recognize the challenges that security and engineering teams face as AI technology becomes increasingly ubiquitous. We recently announced products such as
[Chainguard Agent Skills](https://www.chainguard.dev/unchained/introducing-chainguard-agent-skills)
and
[Chainguard Actions](https://www.chainguard.dev/unchained/introducing-chainguard-actions)
to address this problem directly. As development speeds up, organizations must address hidden attack vectors throughout the software development lifecycle. The trusted open source we offer creates a secure-by-default foundation you can build on.

*Ready to learn more about how Chainguard can protect your open source artifacts?
[Get in touch](https://www.chainguard.dev/contact)
with our team today.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.