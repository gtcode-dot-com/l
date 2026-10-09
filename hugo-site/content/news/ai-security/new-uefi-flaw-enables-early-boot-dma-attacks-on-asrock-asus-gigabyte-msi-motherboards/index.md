---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-20T12:03:12.888224+00:00'
exported_at: '2025-12-20T12:03:15.236137+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/new-uefi-flaw-enables-early-boot-dma.html
structured_data:
  about: []
  author: ''
  description: UEFI firmware flaws in certain ASRock, ASUS, GIGABYTE, and MSI motherboards
    allow early-boot DMA attacks before OS security loads.
  headline: New UEFI Flaw Enables Early-Boot DMA Attacks on ASRock, ASUS, GIGABYTE,
    MSI Motherboards
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/new-uefi-flaw-enables-early-boot-dma.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New UEFI Flaw Enables Early-Boot DMA Attacks on ASRock, ASUS, GIGABYTE, MSI
  Motherboards
updated_at: '2025-12-20T12:03:12.888224+00:00'
url_hash: c574a8c7ad95bb04f9a5ebc9046994b2197262c9
---

**

Dec 19, 2025
**

Ravie Lakshmanan

Firmware Security / Vulnerability

Certain motherboard models from vendors like ASRock, ASUSTeK Computer, GIGABYTE, and MSI are affected by a security vulnerability that leaves them susceptible to early-boot direct memory access (
[DMA](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)
) attacks across architectures that implement a Unified Extensible Firmware Interface (
[UEFI](https://uefi.org/home)
) and input–output memory management unit (
[IOMMU](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit)
).

UEFI and IOMMU are designed to enforce a security foundation and prevent peripherals from performing unauthorized memory accesses, effectively ensuring that DMA-capable devices can manipulate or inspect system memory before the operating system is loaded.

The vulnerability, discovered by Nick Peterson and Mohamed Al-Sharifi of Riot Games in certain UEFI implementations, has to do with a discrepancy in the DMA protection status. While the firmware indicates that DMA protection is active, it fails to configure and enable the IOMMU during the critical boot phase.

"This gap allows a malicious DMA-capable Peripheral Component Interconnect Express (PCIe) device with physical access to read or modify system memory before operating system-level safeguards are established," the CERT Coordination Center (CERT/CC)
[said](https://kb.cert.org/vuls/id/382314)
in an advisory.

"As a result, attackers could potentially access sensitive data in memory or influence the initial state of the system, thus undermining the integrity of the boot process."

Successful exploitation of the vulnerability could allow a physically present attacker to enable pre-boot code injection on affected systems running unpatched firmware and access or alter system memory via DMA transactions, much before the operating system kernel and its security features are loaded.

The vulnerabilities that enable a bypass of early-boot memory protection are listed below -

* **[CVE-2025-14304](https://www.cve.org/CVERecord?id=CVE-2025-14304)**
  (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting ASRock, ASRock Rack, and ASRock Industrial motherboards using Intel 500, 600, 700, and 800 series chipsets
* **[CVE-2025-11901](https://www.cve.org/CVERecord?id=CVE-2025-11901)**
  (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting ASUS motherboards using Intel Z490, W480, B460, H410, Z590, B560, H510, Z690, B660, W680, Z790, B760, and W790 series chipsets
* **[CVE-2025-14302](https://www.cve.org/CVERecord?id=CVE-2025-14302)**
  (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting GIGABYTE motherboards using Intel Z890, W880, Q870, B860, H810, Z790, B760, Z690, Q670, B660, H610, W790 series chipsets, and AMD X870E, X870, B850, B840, X670, B650, A620, A620A, and TRX50 series chipsets (Fix for TRX50 planned for Q1 2026)
* **[CVE-2025-14303](https://www.cve.org/CVERecord?id=CVE-2025-14303)**
  (CVSS score: 7.0) - A protection mechanism failure vulnerability affecting MSI motherboards using Intel 600 and 700 series chipsets

[![Cybersecurity](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://thehackernews.uk/zscaler-ai-event-d)

With impacted vendors releasing firmware updates to correct the IOMMU initialization sequence and enforce DMA protections throughout the boot process, it's essential that end users and administrators apply them as soon as they are available to stay protected against the threat.

"In environments where physical access cannot be fully controlled or relied on, prompt patching and adherence to hardware security best practices are especially important," CERT/CC said. "Because the IOMMU also plays a foundational role in isolation and trust delegation in virtualized and cloud environments, this flaw highlights the importance of ensuring correct firmware configuration even on systems not typically used in data centers."