---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-11T00:03:08.174617+00:00'
exported_at: '2025-12-11T00:03:10.800311+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/three-pcie-encryption-weaknesses-expose.html
structured_data:
  about: []
  author: ''
  description: Three PCIe IDE flaws in PCIe 5.0+ allow stale or incorrect data handling,
    fixed by updated PCIe 6.0 guidance.
  headline: Three PCIe Encryption Weaknesses Expose PCIe 5.0+ Systems to Faulty Data
    Handling
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/three-pcie-encryption-weaknesses-expose.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Three PCIe Encryption Weaknesses Expose PCIe 5.0+ Systems to Faulty Data Handling
updated_at: '2025-12-11T00:03:08.174617+00:00'
url_hash: 60607584675e7961d97fb759c1577a16e361836e
---

**

Dec 10, 2025
**

Ravie Lakshmanan

Hardware Security / Vulnerability

Three security vulnerabilities have been disclosed in the Peripheral Component Interconnect Express (PCIe) Integrity and Data Encryption (
[IDE](https://pcisig.com/PCI%20Express/ECN/Base/IntegrityandDataEncryption_A)
) protocol specification that could expose a local attacker to serious risks.

The flaws impact PCIe Base Specification Revision 5.0 and onwards in the protocol mechanism introduced by the IDE Engineering Change Notice (ECN), according to the PCI Special Interest Group (
[PCI-SIG](https://en.wikipedia.org/wiki/PCI-SIG)
).

"This could potentially result in security exposure, including but not limited to, one or more of the following with the affected PCIe component(s), depending on the implementation: (i) information disclosure, (ii) escalation of privilege, or (iii) denial of service," the consortium
[noted](https://pcisig.com/PCIeIDEStandardVulnerabilities)
.

PCIe is a widely used high-speed standard to connect hardware peripherals and components, including graphics cards, sound cards, Wi-Fi and Ethernet adapters, and storage devices, inside computers and servers. Introduced in PCIe 6.0, PCIe IDE is designed to secure data transfers through encryption and integrity protections.

The
[three IDE vulnerabilities](https://kb.cert.org/vuls/id/404544)
, discovered by Intel employees Arie Aharon, Makaram Raghunandan, Scott Constable, and Shalini Sharma, are listed below -

* **[CVE-2025-9612](https://nvd.nist.gov/vuln/detail/CVE-2025-9612)**
  (Forbidden IDE Reordering) – A missing integrity check on a receiving port may allow re-ordering of PCIe traffic, leading the receiver to process stale data.
* **[CVE-2025-9613](https://nvd.nist.gov/vuln/detail/CVE-2025-9613)**
  (Completion Timeout Redirection) – Incomplete flushing of a completion timeout may allow a receiver to accept incorrect data when an attacker injects a packet with a matching tag.
* **[CVE-2025-9614](https://nvd.nist.gov/vuln/detail/CVE-2025-9614)**
  (Delayed Posted Redirection) – Incomplete flushing or re-keying of an IDE stream may result in the receiver consuming stale, incorrect data packets.

PCI-SIG said that successful exploitation of the aforementioned vulnerabilities could undermine the confidentiality, integrity, and security objectives of IDE. However, the attacks hinge on obtaining physical or low-level access to the targeted computer's PCIe IDE interface, making them low-severity bugs (CVSS v3.1 score: 3.0/CVSS v4 score: 1.8).

"All three vulnerabilities potentially expose systems implementing IDE and Trusted Domain Interface Security Protocol (TDISP) to an adversary that can breach isolation between trusted execution environments," it said.

In an advisory released Tuesday, the CERT Coordination Center (CERT/CC) urged manufacturers to follow the updated PCIe 6.0 standard and apply the Erratum #1 guidance to their IDE implementations.
[Intel](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01409.html)
and
[AMD](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7056.html)
have published their own alerts, stating the issues impact the following products -

* Intel Xeon 6 Processors with P-cores
* Intel Xeon 6700P-B/6500P-B series SoC with P-Cores.
* AMD EPYC 9005 Series Processors
* AMD EPYC Embedded 9005 Series Processors

"End users should apply firmware updates provided by their system or component suppliers, especially in environments that rely on IDE to protect sensitive data," CERT/CC said.