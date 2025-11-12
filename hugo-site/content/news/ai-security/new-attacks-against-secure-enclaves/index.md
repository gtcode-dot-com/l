---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-12T18:25:57.349822+00:00'
exported_at: '2025-11-12T18:26:03.311082+00:00'
feed: https://www.schneier.com/feed/atom/
source_url: https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html
structured_data:
  about: []
  author: ''
  description: 'Encryption can protect data at rest and data in transit, but does
    nothing for data in use. What we have are secure enclaves. I’ve written about
    this before: Almost all cloud services have to perform some computation on our
    data. Even the simplest storage provider has code to copy bytes from an internal
    storage system and deliver them to the user. End-to-end encryption is sufficient
    in such a narrow context. But often we want our cloud providers to be able to
    perform computation on our raw data: search, analysis, AI model training or fine-tuning,
    and more. Without expensive, esoteric techniques, such as secure multiparty computation
    protocols or homomorphic encryption techniques that can perform calculations on
    encrypted data, cloud servers require access to the unencrypted data to do anything
    useful...'
  headline: New Attacks Against Secure Enclaves
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New Attacks Against Secure Enclaves
updated_at: '2025-11-12T18:25:57.349822+00:00'
url_hash: b0925dd4c94240de2d8448d153d51080088a5950
---

## New Attacks Against Secure Enclaves

Encryption can protect data at rest and data in transit, but does nothing for data in use. What we have are secure enclaves. I’ve
[written about](https://www.schneier.com/academic/archives/2023/12/decoupling-for-security.html)
this before:

> Almost all cloud services have to perform some computation on our data. Even the simplest storage provider has code to copy bytes from an internal storage system and deliver them to the user. End-to-end encryption is sufficient in such a narrow context. But often we want our cloud providers to be able to perform computation on our raw data: search, analysis, AI model training or fine-tuning, and more. Without expensive, esoteric techniques, such as secure multiparty computation protocols or homomorphic encryption techniques that can perform calculations on encrypted data, cloud servers require access to the unencrypted data to do anything useful.
>
> Fortunately, the last few years have seen the advent of general-purpose, hardware-enabled secure computation. This is powered by special functionality on processors known as trusted execution environments (TEEs) or secure enclaves. TEEs decouple who runs the chip (a cloud provider, such as Microsoft Azure) from who secures the chip (a processor vendor, such as Intel) and from who controls the data being used in the computation (the customer or user). A TEE can keep the cloud provider from seeing what is being computed. The results of a computation are sent via a secure tunnel out of the enclave or encrypted and stored. A TEE can also generate a signed attestation that it actually ran the code that the customer wanted to run.

Secure enclaves are critical in our modern cloud-based computing architectures. And, of course, they have
[vulnerabilities](https://arstechnica.com/security/2025/10/new-physical-attacks-are-quickly-diluting-secure-enclave-defenses-from-nvidia-amd-and-intel/)
:

> The most recent attack, released Tuesday, is known as TEE.fail. It defeats the latest TEE protections from all three chipmakers. The low-cost, low-complexity attack works by placing a small piece of hardware between a single physical memory chip and the motherboard slot it plugs into. It also requires the attacker to compromise the operating system kernel. Once this three-minute attack is completed, Confidential Compute, SEV-SNP, and TDX/SDX can no longer be trusted. Unlike the Battering RAM and Wiretap attacks from
> [last month](https://arstechnica.com/security/2025/09/intel-and-amd-trusted-enclaves-the-backbone-of-network-security-fall-to-physical-attacks/)
> —which worked only against CPUs using DDR4 memory—TEE.fail works against DDR5, allowing them to work against the latest TEEs.

Yes, these attacks require physical access. But that’s exactly the threat model secure enclaves are supposed to secure against.

Tags:
[cloud computing](https://www.schneier.com/tag/cloud-computing/)
,
[data protection](https://www.schneier.com/tag/data-protection/)
,
[hardware](https://www.schneier.com/tag/hardware/)
,
[physical security](https://www.schneier.com/tag/physical-security/)

[Posted on November 10, 2025 at 7:04 AM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html)
•
[8 Comments](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html#comments)