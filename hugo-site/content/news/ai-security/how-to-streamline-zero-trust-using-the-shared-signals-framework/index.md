---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-10T00:03:08.192516+00:00'
exported_at: '2025-12-10T00:03:10.587276+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/how-to-streamline-zero-trust-using.html
structured_data:
  about: []
  author: ''
  description: Zero Trust workflows strengthened as Tines converts Kolide device issues
    into SSF-compliant CAEP events for Okta.
  headline: How to Streamline Zero Trust Using the Shared Signals Framework
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/how-to-streamline-zero-trust-using.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How to Streamline Zero Trust Using the Shared Signals Framework
updated_at: '2025-12-10T00:03:08.192516+00:00'
url_hash: 4f3f9dea2b26f76ba340f899a74adc4767763265
---

Zero Trust helps organizations shrink their attack surface and respond to threats faster, but many still struggle to implement it because their security tools don't share signals reliably. 88% of organizations admit they've suffered significant challenges in trying to implement such approaches, according to
[Accenture](https://www.accenture.com/content/dam/accenture/final/accenture-com/document-3/State-of-Cybersecurity-report.pdf)
**.**
When products can't communicate, real-time access decisions break down.

The Shared Signals Framework (SSF) aims to fix this with a standardized way to exchange security events. Yet adoption is uneven. For example, Kolide Device Trust doesn't currently support SSF.

Scott Bean, Senior IAM and Security Engineer at MongoDB, proposed a way to solve the problem, giving teams an easy and intuitive way to operationalize SSF across their environment.

In this guide, we'll share an overview of the
[workflow](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
, plus step-by-step instructions for getting it up and running.

## The problem – IAM tools don't support SSF

A core requirement of Zero Trust is continuous, reliable signals about user and device posture. But many tools don't support SSF for Continuous Access Evaluation Protocol (CAEP), making it hard to share or act on these signals.

Teams often face three challenges:

* Tools lack native SSF support
* Signals require enrichment or correlation
* Managing SSF endpoints and token handling adds overhead

Without this interoperability, organizations struggle to apply consistent policies — and in cases like Kolide Device Trust, critical device events never reach systems like Okta.

## The solution – a SSF transmitter that turns Kolide issues into CAEP events

Because SSF is built on HTTPS requests, the OpenID standard works with Tines' HTTP Action.

Scott developed a new
[workflow](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
[integrating Kolide Device Trust with Tines](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
, enabling it to send SSF signals to Okta. If a device is non-compliant, Kolide sends a message to the workflow via webhook. Tines enriches the signal, makes sure it can be linked to a user, builds a Security Event Token (SET), and then sends it to Okta.

In this way, Tines acts as the connective tissue that makes SSF work across the distributed IT environment, even if individual tools don't natively support the standard.

Tines can:

* **Receive signals from Kolide (and tools like it)**
  via webhook when a device becomes non-compliant
* **Enrich and correlate those signals**
  (e.g., map device to user)
* **Generate and sign SETs**
  that meet the SSF specification
* **Deliver them to Okta (and other identity providers)**
  to enforce Zero Trust
* **Host required SSF metadata endpoints**
  using API path prefixes, giving consuming systems a standards-compliant place to fetch keys and decrypt tokens

All of which makes Zero Trust enforcement faster, more reliable, and much easier to operationalize. IT teams are empowered with continuous, real-time risk assessment of devices, faster response to threats, and more flexible policy orchestration. And end users get the benefit of automated remediation, which helps to optimize productivity and minimize IT intervention.

If you want to go deeper into identity modernization, the
[Tines IAM guide](https://www.tines.com/access/guide/unlocking-it-agility-with-automation-and-orchestration-iam/?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
explores how teams are unifying device trust, access decisions, and least-privilege enforcement with automation. Scott's workflow is one of several real-world patterns inside.

## Workflow overview

### **Required tools:**

* **Tines**
  – workflow orchestration and AI platform
* **Kolide**
  – device trust and posture monitoring
* **Okta**
  – identity platform receiving CAEP events

### **Required credentials:**

* Tines API Key - `Team` Scoped with the `Editor` role
* Kolide API Key - Read Only
* Kolide Webhook Signing Secret

### **Required resources:**

Okta domain, such as example.okta.com, example.oktapreview.com, or a branded domain.

**How it works:**

The workflow creates a proof-of-concept SSF transmitter that can be registered with Okta and sends device compliance change CAEP events (sent as SETs), based on issues generated in Kolide. There are three elements:

**1. Generate and store SET signing keys**
(SETs are signed JSON Web Tokens):

* Creates an RSA key pair and converts it to JWK format.
* Publishes the public key for SSF receivers to validate SET signatures.
* Stores the private JWK keyset as a Tines secret.

**2. Expose SSF transmitter API**

SSF receivers (like Okta) need:

* a .well-known/sse-configuration endpoint describing the transmitter
* a JWK endpoint exposing the public key used to verify SET signatures
* a webhook trigger acts as the SSF API surface
* logic returns the .well-known config
* logic returns the JWKs

Once this is live, teams can register a new SSF receiver in Okta under:

* Security → Device Integrations → Receive shared signals

And create a new stream using the API's URL and the new `.well-known` endpoint

**3. Create, sign and send of SETs from Kolide events**

* Receives Kolide
  **issue**
  events via webhook and validates them using the signing secret.
* Fetches device and user metadata from Kolide.
* Builds a SET for a
  **Device Compliance Change**
  CAEP event.
* Signs the SET with the stored private key using the JWT\_SIGN formula.
* Sends the signed token to Okta's security-events endpoint.

This delivers real-time device-compliance updates to Okta so access policies can respond immediately.

## Configuring the workflow — a step-by-step guide

You can build and run this entire workflow using
[Tines Community Edition](https://www.tines.com/get-started/?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
.

**1. Log into Tines or create a new account.**

**2. Navigate to the
[pre-built workflow](https://www.tines.com/library/stories/1329793/?name=integrate-kolide-device-trust-with-okta-using-the-shared-signals-framework?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
in the library.**
Select import. This should take you straight to your new pre-built workflow.

**3. Gather the required credentials**

* Tines API Key (team-scoped with Editor role)
* Kolide API Key (read-only)
* Kolide Webhook Signing Secret

These ensure authenticated calls to Kolide and secure webhook validation.

**4. Collect your required resources**

You'll need an Okta tenant domain, such as:

* example.oktapreview.com
* example.okta.com
* or your custom Okta brand domain

This domain is used when sending signed SETs to Okta's security-events endpoint.

**Note:**
In the example provided, Scott set up as a `push` rather than a `poll` provider as tokens are sent based off of inbound webhooks, so there's no need to store state
**.**

**5. Generate your SET signing keys**

* Use the Generate JWK keyset action to create RSA keys
* Convert both public and private keys to JWK format (two event transforms)
* Store the resulting keyset using a Tines secret

This is required before Okta will accept and verify your SETs.

**6. Publish the SSF transmitter API**

The SSF API webhook contains two branches:

* .well-known endpoint
  + Trigger: well-known
  + Event transform: returns the SSF configuration declaring the transmitter's capabilities
* JWKS endpoint
  + Trigger: JWKs
  + Event transform: returns the public JWKs so Okta can verify signatures

Once live, Okta can register this transmitter as a shared signals sender.

**7. Connect Kolide and process device issues**

The Kolide integration flow follows these steps:

* Webhook: Kolide webhook – receives issue opened/resolved events
* Get device details – fetches metadata for the device involved
* Device has a user – branching logic to confirm a user is associated
* Get user details – look up user metadata for the CAEP payload

Depending on whether the issue is new or resolved:

* Build SET – construct the CAEP device\_compliance\_change event
* Sign SET – use the RSA private key stored earlier to produce an SSF-compliant SET
* Send SET – send the final signed token to Okta's security-events endpoint

As soon as Okta receives and verifies the SET, the associated user risk level updates.

## Bringing it all together

SSF exists to help security tools speak the same language, delivering continuous insight into risk and device posture. But when key tools don't support the standard, gaps open up, and access policies lag behind real-world changes.

Tines bridges these gaps by enabling new intelligent workflows. They ensure that even tools that don't support SSF can send information in the same standardized way. By using Tines to generate, sign, and deliver compliance signals in real time, you get the benefits of SSF even when the source tool wasn't built for it.

If you'd like to try this workflow yourself, you can spin it up in minutes with a
[free Tines account](https://www.tines.com/get-started/?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
. And if you want to see how device posture fits into a broader identity strategy,
[this guide to modern IAM workflows](https://www.tines.com/access/guide/unlocking-it-agility-with-automation-and-orchestration-iam/?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-Dec9)
offers practical patterns and real-world workflows like Scott's you can start building on today.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.