---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T17:57:49.292122+00:00'
exported_at: '2026-06-23T17:57:51.922286+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/trump-order-sets-2030-deadline-for.html
structured_data:
  about: []
  author: ''
  description: Federal agencies must shift to post-quantum cryptography by 2030 and
    digital signatures by 2031 under a new Trump order.
  headline: Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/trump-order-sets-2030-deadline-for.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration
updated_at: '2026-06-23T17:57:49.292122+00:00'
url_hash: ab9a2d76bcaf2e5aabc7f231269beda8b07fb1dc
---

**

Swati Khandelwal
**

Jun 23, 2026

Cryptography / Quantum Computing

President Trump signed an
[executive order on June 22](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/)
setting hard deadlines for federal agencies to move high-value assets and high-impact systems to post-quantum cryptography.

Key establishment must move by December 31, 2030; digital signatures by December 31, 2031. EO 14409 leaves national security systems on a separate track.

The deadlines matter because of a threat that does not need a working quantum computer today. Adversaries can collect encrypted U.S. data now and decrypt it later, once a large-scale quantum machine exists, the risk is known as
["harvest now, decrypt later"](https://thehackernews.com/2025/02/google-cloud-kms-adds-quantum-safe.html)
.

The order describes that risk directly and pulls the government's PQC timeline forward by four to five years. The prior government-wide target, set by the 2022 National Security Memorandum 10, ran to 2035.

The two deadlines line up with the standards NIST
[finalized in August 2024](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
. Key establishment uses FIPS 203, the ML-KEM algorithm formerly called CRYSTALS-Kyber.

Digital signatures use FIPS 204 and 205, ML-DSA, and SLH-DSA. The standards have been ready for almost two years. The order is what turns them into a schedule with consequences.

## What agencies have to do, and when

The near-term clock starts fast. Within 30 days, each agency head names a PQC migration lead who reports to the agency CIO and owns the cryptographic inventory and migration plan.

Within 90 days, OMB issues guidance requiring agencies to review their inventories of high-value assets and high-impact systems, plan the migration, and submit that plan.

NIST runs a pilot migration on a subset of its own systems, to be finished by December 31, 2027.

The order reaches past federal networks. The Federal Acquisition Regulatory Council has 180 days to propose a rule giving "covered contractors" until December 31, 2030, to meet NIST's FIPS, including the PQC algorithms.

A second proposed rule, due in 270 days, would fold cryptographic flaws into contractor vulnerability disclosure programs, including tests for missing encryption and for non-FIPS algorithms. Sector Risk Management Agencies and CISA are told to help critical infrastructure operators build their own migration plans, though that part is assistance, not a mandate.

Then there is the inventory angle. Within 270 days, CISA and NIST are to publish the minimum elements for a cryptographic bill of materials, a machine-readable list of the cryptographic assets in a piece of hardware or software.

That is the groundwork for crypto-agility: you cannot swap out weak algorithms on a deadline if you do not know where they are.

## The practical read

For federal teams and the vendors who sell to them, the work is the inventory, and it starts now. Find every place key exchange and signatures happen, flag what is not NIST PQC, and sequence the swap against the 2030 and 2031 dates.

Contractors should expect the FAR clause and a 2030 compliance line once the rule lands. The standards exist. The deadlines now exist. The gating task for almost everyone is knowing what cryptography is running, and where.

A companion order signed the same day,
["Ushering in the Next Frontier of Quantum Innovation,"](https://www.whitehouse.gov/presidential-actions/2026/06/ushering-in-the-next-frontier-of-quantum-innovation/)
pushes the other side of the equation: building the quantum computers that make the migration urgent in the first place.

The teeth are still being written. OMB's 90-day guidance and the FAR rules will decide whether 2030 and 2031 become real procurement pressure or just another federal migration target that slips once the hard work starts.