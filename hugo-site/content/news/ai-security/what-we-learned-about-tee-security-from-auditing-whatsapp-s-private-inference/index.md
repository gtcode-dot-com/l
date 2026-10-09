---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T02:15:15.254973+00:00'
exported_at: '2026-04-08T02:15:19.127200+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference
structured_data:
  about: []
  author: ''
  description: Our audit of WhatsApp’s new “Private Inference” feature shows that
    trusted execution environments (TEEs) aren't a silver bullet.
  headline: What we learned about TEE security from auditing WhatsApp's Private Inference
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference
  publisher:
    logo: /favicon.ico
    name: GTCode
title: What we learned about TEE security from auditing WhatsApp's Private Inference
updated_at: '2026-04-08T02:15:15.254973+00:00'
url_hash: 20ef0c5ef4ca23a53c36aab2c029dc89ec519e28
---

WhatsApp’s new “Private Inference” feature represents one of the most ambitious attempts to combine end-to-end encryption with AI-powered capabilities, such as message summarization. To make this possible, Meta built a system that processes encrypted user messages inside trusted execution environments (TEEs), secure hardware enclaves designed so that not even Meta can access the plaintext. Our
[now-public audit](https://github.com/trailofbits/publications/blob/master/reviews/2025-08-meta-whatsapp-privateprocessing-securityreview.pdf)
, conducted before launch, identified several vulnerabilities that compromised WhatsApp’s privacy model, all of which Meta has patched. Our findings show that TEEs aren’t a silver bullet: every unmeasured input and missing validation can become a vulnerability, and to securely deploy TEEs, developers need to measure critical data, validate and never trust any unmeasured data, and test thoroughly to detect when components misbehave.

## The challenge of using AI with end-to-end encryption

WhatsApp’s Private Processing attempts to resolve a fundamental tension: WhatsApp is end-to-end encrypted, so Meta’s servers cannot read, alter, or analyze user messages. However, if users also want to opt in to AI-powered features like message summarization, this typically requires sending plaintext data to servers for computationally expensive processing. To solve this, Meta uses TEEs based on AMD’s SEV-SNP and Nvidia’s confidential GPU platforms to process messages in a secure enclave where even Meta can’t access them or learn meaningful information about the message contents.

The stakes in WhatsApp are high, as vulnerabilities could expose millions of users’ private messages. Our review identified 28 issues, including eight high-severity findings that could have enabled attackers to bypass the system’s privacy guarantees. The following sections explore noteworthy findings from the audit, how they were fixed, and the lessons they impart.

## Key lessons for TEE deployments

### Lesson 1: Never trust data outside your measurement

In TEE systems, an “attestation measurement” is a cryptographic checksum of the code running in the secure enclave; it’s what clients check to ensure they’re interacting with legitimate, unmodified software. We discovered that WhatsApp’s system loaded configuration files containing environment variables
*after*
this fingerprint was taken (issue TOB-WAPI-13 in the report).

This meant that a malicious insider at Meta could inject an environment variable, such as
`LD_PRELOAD=/path/to/evil.so`
, forcing the system to load malicious code when it started up. The attestation would still verify as valid, but the attacker’s malicious code would be running inside, potentially violating the system’s security or privacy guarantees by, for example, logging every message being processed to a secret server.

Meta fixed this by strictly validating environment variables: they can now contain only safe characters (alphanumeric plus a few symbols like dots and dashes), and the system explicitly checks for dangerous variables like
`LD_PRELOAD`
. Every piece of data your TEE loads must either be part of the measured boot process or be treated as potentially hostile.

### Lesson 2: Do not trust data outside your measurement (have we already mentioned this?)

ACPI tables are configuration data that inform an operating system about the available hardware and how to interact with it. We found these tables weren’t included in the attestation measurement (TOB-WAPI-17), creating a backdoor for attackers.

Here’s why this matters: a malicious hypervisor (the software layer that manages virtual machines) could inject fake ACPI tables defining malicious “devices” that can read and write to arbitrary memory locations. When the secure VM boots up, it processes these tables and grants the fake devices access to memory regions that should be protected. An attacker could use this to extract user messages or encryption keys directly from the VM’s memory, and the attestation report will still verify as valid and untampered.

Meta addressed this by implementing a custom bootloader that verifies ACPI table signatures as part of the secure boot process. Now, any tampering with these tables will change the attestation measurement, alerting clients that something is wrong.

### Lesson 3: Correctly verify security patch levels

AMD regularly releases security patches for its SEV-SNP firmware, fixing vulnerabilities that could allow attackers to compromise the secure environment. The WhatsApp system did check these patch levels, but it made an important error: it trusted the patch level that the firmware
*claimed*
to be running (in the attestation report), rather than verifying it against AMD’s cryptographic certificate (TOB-WAPI-8).

An attacker who had compromised an older, vulnerable firmware could simply lie about their patch level. Researchers have publicly demonstrated attacks that can extract encryption keys from older SEV-SNP firmware versions. An attacker could use these published techniques against WhatsApp users to exfiltrate secret data while the client incorrectly believes it’s connected to a secure, updated system.

Meta’s solution was to validate patch levels against the VCEK certificate’s X.509 extensions. These extensions are cryptographically signed data from AMD that can’t be forged by compromised firmware.

### Lesson 4: Attestations need freshness guarantees

Before our review, when a client connected to the Private Processing system, the server would generate an attestation report proving its identity, but this report didn’t include any timestamp or random value from the client (TOB-WAPI-7). This meant that an attacker who compromised a TEE once could save its attestation report and TLS keys, then replay them indefinitely.

Achieving a one-time compromise of a TEE is typically much more feasible and much less severe than a persistent compromise affecting each individual session. For example, consider an attacker who can extract TLS session keys through a side channel attack or other vulnerability. For a single attack, the impact tends to be short-lived, as the forward security of TLS makes the exploit impactful for only a single TLS session. However, without freshness, that single success becomes a permanent backdoor because the TEE’s attestation report from that compromised session can be replayed indefinitely. In particular, the attacker can now run a fake server anywhere in the world, presenting the stolen attestation to clients who will trust it completely. Every WhatsApp user who connects would send their messages to the attacker’s server, believing it’s a secure Meta TEE.

Meta addressed this issue by including the TLS
`client_random`
nonce in every attestation report. Now each attestation is tied to a specific connection and can’t be replayed.

### How Meta fixed the remaining issues

Before their launch, Meta resolved 16 issues completely and partially addressed four others. The remaining eight unresolved issues are low- and informational-severity issues that Meta has deliberately not addressed. Meta provided a justification for each of these decisions, which can be reviewed in appendix F of our
[audit report](https://github.com/trailofbits/publications/blob/master/reviews/2025-08-meta-whatsapp-privateprocessing-securityreview.pdf)
. In addition, they’ve implemented broader improvements, such as automated build pipelines with provenance verification and published authorized host identities in external logs.

## Beyond individual vulnerabilities: Systemic challenges in TEE deployment

While Meta has resolved these specific issues, our audit revealed the need to solve more complex challenges in securing TEE-based systems.

**Physical security matters:**
The AMD SEV-SNP threat model doesn’t fully protect against advanced physical attacks. Meta needed to implement additional controls around which CPUs could be trusted (TOB-WAPI-10). If you are interested in a more detailed discussion on physical attacks targeting these platforms, check out our
[webinar](https://watch.getcontrast.io/register/trail-of-bits-after-wiretap-and-battering-ram-what-changes-for-tee-based-blockchain-infrastructure)
, which discusses recently published physical attacks targeting both AMD SEV-SNP and Intel’s SGX/TDX platforms.

**Transparency requires reproducibility:**
For external researchers to verify the system’s security, they need to be able to reproduce and examine the CVM images. Meta has made progress in this area, but achieving full reproducibility remains challenging, as issue TOB-WAPI-18 demonstrates.

**Complex systems need comprehensive testing:**
Many of the issues we found could have been caught with
[negative testing](https://en.wikipedia.org/wiki/Negative_testing)
, specifically testing what happens when components misbehave or when malicious inputs are provided.

## The path forward for securely deploying TEEs

Can TEEs enable privacy-preserving AI features? Our audit suggests the answer is
*yes, but only with rigorous attention to implementation details*
. The issues we found weren’t fundamental flaws in the TEE model but rather implementation and deployment gaps that a determined attacker could exploit. These are subtle flaws that other TEE deployments are likely to replicate.

This audit shows that while TEEs provide strong isolation primitives, the large host-guest attack surface requires careful design and implementation. Every unmeasured input, every missing validation, and every assumption about the execution environment can become a vulnerability. Your system is only as secure as your TEE implementation and deployment.

For teams building on TEEs, our advice is clear: engage security reviewers early, invest in comprehensive testing (especially negative testing), and remember that security in these systems comes from getting hundreds of details right, not just the big architectural decisions.

The promise of confidential computing is compelling. But, as this audit shows, realizing that promise requires rigorous attention to security at every layer of the stack.

*For more details on the technical findings and Meta’s fixes, see our
[full audit report](https://github.com/trailofbits/publications/blob/master/reviews/2025-08-meta-whatsapp-privateprocessing-securityreview.pdf)
. If you’re building systems with TEEs and want to discuss security considerations, we offer free office hours sessions where we can share insights from our extensive experience with these technologies.*