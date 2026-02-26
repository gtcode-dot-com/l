---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T14:15:15.116523+00:00'
exported_at: '2026-02-26T14:15:17.699009+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/expert-recommends-prepare-for-pqc-right.html
structured_data:
  about: []
  author: ''
  description: Quantum Computers won’t be available for another decade. Why worry
    about them now, then? A cryptography expert explains. 
  headline: 'Expert Recommends: Prepare for PQC Right Now'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/expert-recommends-prepare-for-pqc-right.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Expert Recommends: Prepare for PQC Right Now'
updated_at: '2026-02-26T14:15:15.116523+00:00'
url_hash: b3e82bd66cd9bbe477664e25ebec376b8ba70ec2
---

**

The Hacker News
**

Feb 26, 2026

Encryption / Data Protection

## **Introduction: Steal It Today, Break It in a Decade**

Digital evolution is unstoppable, and though the pace may vary, things tend to fall into place sooner rather than later. That, of course, applies to adversaries as well. The rise of ransomware and cyber extortion generated funding for a complex and highly professional criminal ecosystem. The era of the cloud brought general availability of almost infinite amounts of storage. So there is literally nothing that stops criminals from stealing and trafficking heaps of data, be it encrypted or not.

Patient adversaries are employing a "Harvest Now, Decrypt Later" (HNDL) strategy. They are quietly accumulating encrypted data with the intention of decrypting it later using quantum computers. Any data requiring long-term security, such as trade secrets or classified designs, is vulnerable because its lifespan will inevitably outlive its current encryption. Therefore, it is crucial that organizations begin planning their PQC migration now, ensuring that data encrypted today remains secure against future quantum-enabled decryption attacks.

## **The Quantum Waiting Game**

Cryptography is the backbone of digital trust, but the looming era of quantum computing threatens its foundations.

Harnessing quantum physics, future quantum machines will effortlessly break the mathematical encryption schemes that protect data today. Current prototypes
[1]
are not quite there yet because they fundamentally lack the scale and error-correction capability required to successfully execute complex quantum algorithms. However, the prospect of a mature, cryptographically relevant quantum computer (CRQC) is alarming. Such a machine could likely break modern encryption in a matter of minutes, likely by 2030 to 2035.

To combat the looming quantum computing threat, our cryptography must evolve immediately. This is why Post-Quantum Cryptography (PQC)
[2]
is being introduced as a solution. PQC provides new cryptographic algorithms designed to withstand attacks from both today's classical computers and future quantum machines.

## **A Step-by-Step Guide to Future-Proofing with PQC**

PQC migration is a complex process that spans the entire organization and potentially reaches deep into its security architecture. This massive transition is complicated by the current state of industry planning. There is still a lack of consensus in technical literature regarding common steps or uniform terminology for migration strategies. Without a common language, companies find it difficult to effectively compare, adopt, or coordinate the most suitable migration strategies.

Our research concludes that the following strategy offers an effective, universal framework that can be adapted to suit any organization.
[3, 4, 5, 6, 7, 8, 9]

## Security Navigator 2026 is Here - Download Now

The newly released
[**Security Navigator 2026**](https://www4.orangecyberdefense.com/security-navigator-26-thn2)
offers critical insights into current digital threats, documenting 139,373 incidents and 19,053 confirmed breaches. More than just a report, it serves as a guide to navigating a safer digital landscape.

#### What's Inside?

* 📈 In-Depth Analysis: Statistics from CyberSOC, Vulnerabilitiy scanning, Pentesting, CERT, Cy-X and Ransomware observations from Dark Net surveillance.
* 🔮 Future-Ready: Equip yourself with security predictions and stories from the field.
* 🧠 Stories from security practitioners across the world.
* 👁️ Security deep-dives: Get briefed on emerging trends related to Generative AI, Operational Technology and post-quantum cryptography.

Stay one step ahead in cybersecurity. Your essential guide awaits!

[🔗
**Get Your Copy Now**](https://www4.orangecyberdefense.com/security-navigator-26-thn2)

At this stage, it is important to emphasize that a migration team must be established for each migration. This team should consist of cryptography and cybersecurity experts and managers from the software system or infrastructure being migrated. The team will drive the migration process forward and ensure its completion.

* **Step 1 (Preparation):**
  This phase establishes the scope and leadership for the PQC migration process. Key activities include assessing the relevance and urgency of PQC, appointing a program lead, aligning stakeholders on clear goals, and initiating conversations with vendors to determine migration needs.
* **Step 2 (Diagnosis):**
  This phase involves a thorough evaluation of the current cybersecurity posture to establish a comprehensive security baseline. Key activities include documenting all cryptographic assets, categorizing data based on their confidential lifespan, identifying suppliers of cryptographic tools to evaluate their PQC readiness, and conducting a formal risk assessment to generate a prioritized asset list based on principles such as Mosca's theorem
  [12]
  .
* **Step 3 (Planning):**
  Once the urgency and scope are determined, this phase focuses on the "how" and "when“. It focuses on the migration strategy, creating a comprehensive business and technical plan and timeline based on the urgency and scope determined in previous steps. Key activities involve appointing a dedicated migration manager to oversee the process and conducting a comprehensive cost estimate for the entire migration.
* **Step 4 (Execution):**
  This critical phase involves executing the plan to establish a quantum-safe environment through careful technical implementation. Key activities include maintaining backward compatibility via a hybrid cryptographic approach, implementing recommended PQC primitives for key exchange and signatures, adjusting key sizes, and integrating cryptographic agility to ensure rapid adaptation with minimal service disruption.
* **Step 5 (Continuous Monitoring and Update):**
  This final phase focuses on continuous vigilance after migration, recognizing the dynamic cryptographic landscape. Key activities include routinely reviewing and updating the cryptographic inventory, conducting regular reviews of emerging threats to PQC schemes, performing proactive security audits and vulnerability assessments, and staying updated on the latest PQC advances to ensure timely system and software updates.

## **Addressing Key Challenges: A Practical Checklist**

To ensure a successful PQC migration, organizations must proactively identify and mitigate key obstacles that could hinder progress. They must recognize that the transition involves navigating three interdependent categories of challenges.

* **Organizational challenges:**
  These non-technical obstacles relate to people, strategic planning, internal governance, and coordination across the wider ecosystem, often complicated by a lack of urgency or qualified personnel.
* **PQC challenges:**
  These stem directly from the immaturity of the new technology. Although we now have initial standards, such as ML-KEM and its implementation in protocols like TLS, a lack of standardization for a complete suite of algorithms and uncertainty in selecting and testing reliable PQC solutions remain major hurdles. The main issue is the lack of specific implementation guidelines, such as how to effectively deploy hybridization or agility mechanisms.
* **Code and Documentation challenges:**
  These are technical hurdles caused by the inherent rigidity of existing IT infrastructure (legacy systems), the need for extensive code modification, and the complexity of implementing secure cryptographic changes.

The following breaks down the major obstacles to a successful PQC migration and offers solutions for each. Each obstacle falls under one of the previously established challenge categories. See references
[71]
and
[11]
for a more comprehensive discussion of additional obstacles.

* **Lack of Urgency and Business Case (Organizational):**

+ **Problem:**
  The quantum threat seems distant, making it challenging to establish a sense of urgency and budget approval from leadership.
+ **Solution:**
  Organizations can use tools like Mosca's Theorem
  [12]
  to quantify their vulnerability and take inventory of cryptographic assets to improve current cybersecurity regardless of the quantum timeline.

* **Internal Knowledge and Skills Deficit (Organizational):**
  + **Problem:**
    Lack of internal knowledge about quantum-based threats, and shortage of qualified personnel to implement new PQC solutions.
  + **Solution:**
    Launch training initiatives for IT and management. Engage external PQC consultants to design the strategy and knowledge transfer.
* **Internal Governance and Planning (Organizational):**
  + **Problem:**
    Absence of PQC governance and a fully articulated transition plan, leading to ineffective task prioritization and operational inefficiencies.
  + **Solution:**
    Appoint a PQC migration manager or steering committee to mandate a cryptographic inventory for risk-based migration prioritization.
* **Ecosystem and Coordination Failures (Organizational):**
  + **Problem:**
    Lack of ecosystem engagement, unclear governance, and limited collaboration hamper the PQC transition.
  + **Solution:**
    Proactively manage vendor relationships and join industry forums to share knowledge, collaborate, and influence standards development.
* **Regulatory Voids (Organizational):**
  + **Problem:**
    Existing regulations (e.g. NIS2 and DORA) mandate the use of state-of-the-art cryptography while new PQC-specific laws are pending.
  + **Solution:**
    Adopt recent PQC standards proactively for critical systems to meet the "state-of-the-art" requirement. Leverage EUCC certification and monitor ETSI/OpenSSL for implementation guidance.
* **Uncertain Selection Criteria (PQC):**
  + **Problem:**
    Organizations struggle to decide between an all-at-once or phased hybrid approach to replacing PQC, as they lack clear criteria.
  + **Solution:**
    Default to a hybrid PQC model to gain operational knowledge, and minimize complications before committing to a full replacement strategy.
* **Security and Reliability Concerns (PQC):**
  + **Problem:**
    Uncertainty about the maturity and security of PQC algorithms, organizations must balance present-day protection and future resilience.
  + **Solution:**
    Use a hybrid PQC approach with a staged rollout. Begin with non-critical areas before expanding to ensure the solution is stable and reliable.

* **Rigidity of Legacy Systems (Code and Documentation):**
  + **Problem:**
    Legacy systems inflexibility. This is exacerbated in resource-constrained devices, e.g. IoT and smart cards, which lack the memory and power necessary for larger PQC keys and intense computations.
  + **Solution:**
    Replace hardware to accommodate PQC demands. If this is not feasible, implement lightweight, optimized PQC libraries.
* **Ecosystem Interdependency (Code and Documentation):**
  + **Problem:**
    The interconnected nature of the Public Key Infrastructure (PKI) means that a PQC transition affects all involved parties, including standards bodies, hardware/software vendors, and certificate authorities (CAs).
  + **Solution:**
    Collaborate with suppliers and CAs, participate in industry and regulatory groups (e.g., NIST, CISA, ENISA, ETSI, ANSSI, NCSC and BSI), and map all third-party component dependencies.
* **Lack of Certified and Approved Components (Code and Documentation):**
  + **Problem:**
    Limited availability of certified components (eg HSMs) from vendors, especially in regulated sectors such as finance and government.
  + **Solution**
    : During procurement, organizations must mandate FIPS 140-3 or EUCC validation for PQC-capable hardware, while beginning software-level migration (e.g., TLS/SSH) in parallel.
* **Lack of Agility (Code and Documentation):**
  + **Problem:**
    Current systems are cryptographically inflexible. This makes adapting to new threats or evolving standards slow and complex due to the need for intricate code changes.
  + **Solution:**
    Prioritize cryptographic agility by designing new systems that allow for algorithm swapping via simple configuration and centralized key and certificate support.

## **Key Takeaways**

* **Urgency of Migration:**
  Act immediately! The deadline is now. The time for waiting for CRQC is over. Organizations must start preparing and migrating their data immediately to ensure long-term security.
* **Establish Foundational Priorities: Strategic efforts must focus on developing a clear, actionable strategy for planning and executing the PQC transition smoothly.**
* **Foster United Collaboration**
  : The PQC transition demands a unified effort to address the collective security challenge. This requires actively sharing lessons learned and collaborating across industries, governments, and academia.
* **Embed Hybrid Cryptography and Cryptographic Agility:**
  The ability to rapidly and seamlessly combine, modify or swap cryptographic primitives must be adopted as the cornerstone of the new security posture to adapt to future advances in quantum-safe standards.
* **Acknowledge Interdependent Challenges:**
  The success of any PQC migration hinges on recognizing that the transition involves navigating several interdependent categories of challenges.

This is just an excerpt of the many topics covered in the
[Security Navigator 2026](https://www4.orangecyberdefense.com/security-navigator-26-thn2)
. For more in-depth articles on the use and abuse of Generative AI, Hacktivism and cybercrime, Vulnerability management and Cyber Extortion, as well as CyberSOC statistics and security predictions, you should check out the full report! Head over to the download page and get a copy.

**Note:**
*This article was expertly written and contributed by Mohammed Meziani, Senior Security Consultant at Orange Cyberdefense.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.