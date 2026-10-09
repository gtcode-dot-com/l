---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-05T01:05:13.713313+00:00'
exported_at: '2026-03-05T01:05:15.432766+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/google-develops-merkle-tree.html
structured_data:
  about: []
  author: ''
  description: Google is testing Merkle Tree Certificates in Chrome to enable quantum-resistant
    HTTPS, reduce TLS handshake data & launch a new root store by 2027.
  headline: Google Develops Merkle Tree Certificates to Enable Quantum-Resistant HTTPS
    in Chrome
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/google-develops-merkle-tree.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Develops Merkle Tree Certificates to Enable Quantum-Resistant HTTPS
  in Chrome
updated_at: '2026-03-05T01:05:13.713313+00:00'
url_hash: 53acdbfb71193bbb6c34cbafabfa5ee98261c8ae
---

**

Ravie Lakshmanan
**

Mar 02, 2026

Cryptography / Browser Security

Google has announced a new program in its Chrome browser to ensure that HTTPS certificates are secure against the
[future risk](https://thehackernews.com/2026/01/threatsday-bulletin-new-rces-darknet.html#post-quantum-shift-accelerates)
posed by
[quantum computers](https://thehackernews.com/2025/02/google-cloud-kms-adds-quantum-safe.html)
.

"To ensure the scalability and efficiency of the ecosystem, Chrome has no immediate plan to add traditional
[X.509 certificates](https://en.wikipedia.org/wiki/X.509)
containing post-quantum cryptography to the
[Chrome Root Store](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.md)
," the Chrome Secure Web and Networking Team
[said](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html)
.

"Instead, Chrome, in collaboration with other partners, is developing an
[evolution](https://drive.google.com/file/d/1KQXAGBHXR4S_prwFrZlyfA6DrpvfJwuJ/view)
of HTTPS certificates based on
[Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/)
(MTCs), currently in development in the PLANTS working group."

As Cloudflare explains, MTC is a
[proposal](https://blog.cloudflare.com/bootstrap-mtc/)
for the next generation of the Public Key Infrastructure (PKI) used to secure the internet that aims to reduce the number of public keys and signatures in the TLS handshake to the bare minimum required.

Under this model, a Certification Authority (CA) signs a single 'Tree Head' representing potentially millions of certificates, and the 'certificate' sent to the browser is a lightweight proof of inclusion in that tree, Google said.

In other words, MTCs facilitate the adoption of post-quantum algorithms without having to incur additional bandwidth associated with classical X.509 certificate chains. The approach, the company added, decouples the security strength of the corresponding cryptographic algorithm from the size of the data transmitted to the user.

"By shrinking the authentication data in a TLS handshake to the absolute minimum, MTCs aim to keep the post-quantum web as fast and seamless as today's internet, maintaining high performance even as we adopt stronger security," Google said.

The tech giant said it's already experimenting with MTCs with real internet traffic and that it plans to gradually expand the rollout in three distinct phases by the third quarter of 2027 -

* **Phase 1**
  (In progress) - Google is conducting a feasibility study in collaboration with Cloudflare to evaluate the performance and security of TLS connections relying on MTCs.
* **Phase 2**
  (Q1 2027) - Google plans to invite Certificate Transparency (CT)
  [Log](https://certificate.transparency.dev/logs/)
  operators with at least one "
  [usable](https://googlechrome.github.io/CertificateTransparency/log_states.html)
  " log in Chrome before February 1, 2026, to participate in the initial bootstrapping of public MTCs.
* **Phase 3**
  (Q3 2027) - Google will finalize the requirements for onboarding additional CAs into the new Chrome Quantum-resistant Root Store (CQRS) and corresponding Root Program that only supports MTCs.

"We view the adoption of MTCs and a quantum-resistant root store as a critical opportunity to ensure the robustness of the foundation of today's ecosystem," Google said. By designing for the specific demands of a modern, agile, internet, we can accelerate the adoption of post-quantum resilience for all web users.