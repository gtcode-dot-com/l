---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-14T00:03:12.633949+00:00'
exported_at: '2025-12-14T00:03:15.237855+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem
structured_data:
  about: []
  author: ''
  description: "\n                A retrospective on the $100M Balancer hack that
    occurred in November 2025, including long-term, strategic guidance on how to avoid
    similar bugs.\n            "
  headline: Balancer hack analysis and guidance for the DeFi ecosystem
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Balancer hack analysis and guidance for the DeFi ecosystem
updated_at: '2025-12-14T00:03:12.633949+00:00'
url_hash: d52e4d0f10a05e95d48a64f240bcc953c451eb7e
---

## TL;DR

* The root cause of the hack was a rounding direction issue that had been present in the code for many years.
* When the bug was first introduced, the threat landscape of the blockchain ecosystem was significantly different, and arithmetic issues in particular were not widely considered likely vectors for exploitation.
* As low-hanging attack paths have become increasingly scarce, attackers have become more sophisticated and will continue to hunt for novel threats, such as arithmetic edge cases, in DeFi protocols.
* Comprehensive invariant documentation and testing are now essential; the simple rule “rounding must favor the protocol” is no longer sufficient to catch edge cases.
* This incident highlights the importance of both targeted security techniques, such as developing and maintaining fuzz suites, and holistic security practices, including monitoring and secondary controls.

## What happened: Understanding the vulnerability

On November 3, 2025, attackers exploited a vulnerability in Balancer v2 to drain more than $100M across nine blockchain networks. The attack targeted a number of Balancer v2 pools, exploiting a rounding direction error. For a detailed root cause analysis, we recommend reading
[Certora’s blog post](https://www.certora.com/blog/breaking-down-the-balancer-hack)
.

Since learning of the attack on November 3, Trail of Bits has been working closely with the Balancer team to understand the vulnerability and its implications. We independently confirmed that Balancer v3 was not affected by this vulnerability.

## The 2021 audits: What we found and what we learned

In 2021, Trail of Bits conducted three security reviews of Balancer v2. The commit reviewed during the first audit, in April 2021, did not have this vulnerability present; however, we did uncover a variety of other similar rounding issues using
[Echidna](https://github.com/crytic/echidna)
, our smart contract fuzzer. As part of the
[report](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2021-04-02.pdf)
, we wrote an appendix (appendix H) that did a deep dive on how rounding direction and precision loss should be managed in the codebase.

In October 2021, Trail of Bits conducted a security review of Balancer’s Linear Pools (
[report](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2021-10-08.pdf)
). During that review, we identified issues with how Linear Pools consumed the Stable Math library (documented as finding TOB-BALANCER-004 in our report). However, the finding was marked as “undetermined severity.”

At the time of the audit, we couldn’t definitively determine whether the identified rounding behavior was exploitable in the Linear Pools as they were configured. We flagged the issue because we found similar ones in the first audit, and we recommended implementing comprehensive fuzz testing to ensure the rounding directions of all arithmetic operations matched expectations.

We now know that the Composable Stable Pools that were hacked on Monday were exploited using the same vulnerability that we reported in our audit. We performed a security review of the Composable Stable Pools in September 2022; however, the Stable Math library was explicitly out of scope (see the Coverage Limitations section in the
[report](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2022-09-02.pdf)
).

The above case illustrates the difficulty in evaluating the impact of a precision loss or rounding direction issue. A precision loss of 1 wei in the wrong direction may not seem significant when a fuzzer first identifies it, but in a particular case, such as a low-liquidity pool configured with specific parameters, the precision loss may be substantial enough to become profitable.

## 2021 to 2025: How the ecosystem has evolved

When we audited Balancer in 2021, the blockchain ecosystem’s threat landscape was much different than it is today. In particular, the industry at large did not consider rounding and arithmetic issues to be a significant risk to the ecosystem. If you look back at the
[biggest crypto hacks of 2021](https://www.auditone.io/blog-posts/biggest-crypto-hacks-2021-and-how-to-avoid-them)
, you’ll find that the root causes were different threats: access control flaws, private key compromise (phishing), and front-end compromise.

[Looking at 2022](https://blockworks.co/news/the-nine-largest-crypto-hacks-in-2022)
, it’s a similar story; that year in particular saw enormous hacks that drained several cross-chain bridges, either through private key compromise (phishing) or traditional smart contract vulnerabilities. To be clear, during this period, more DeFi-specific exploits, such as oracle price manipulation attacks, also occurred. However, these exploits were considered a novel threat at the time, and other DeFi exploits (such as those involving rounding issues) had not become widespread yet.

Although these rounding issues were not the most severe or widespread threat at the time, our team viewed them as a significant, underemphasized risk. This is why we reported the risk of rounding issues to Balancer (
[TOB-BALANCER-004](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2021-10-08.pdf)
), and we reported a similar issue in our
[2021 audit of Uniswap v3](https://github.com/trailofbits/publications/blob/master/reviews/UniswapV3Core.pdf)
. However, we have had to make our own improvements to account for this growing risk; for example, we’ve since tightened the ratings criteria for ​​our
[Codebase Maturity evaluations](/2023/07/14/evaluating-blockchain-security-maturity/)
. Where Balancer’s Linear pools were rated “Moderate” in 2021, we now rate codebases without comprehensive rounding strategies as having
[“Weak” arithmetic maturity](https://secure-contracts.com/development-guidelines/code_maturity.html?highlight=rounding#moderate)
.

Moving into 2023 and 2024, these DeFi-specific exploits, particularly rounding issues, became more widespread. In 2023,
[Hundred Finance protocol was completely drained](https://blog.hundred.finance/15-04-23-hundred-finance-hack-post-mortem-d895b618cf33)
due to a rounding issue. This same vulnerability was exploited several times in various protocols, including
[Sonne Finance](https://blog.hundred.finance/15-04-23-hundred-finance-hack-post-mortem-d895b618cf33)
, which was one of the biggest hacks of 2024. These broader industry trends were also validated in our client work at the time, where we continued to identify severe rounding issues, which is why
[we open-sourced roundme](https://x.com/thetrustx/status/1731876403627352247)
, a tool for human-assisted rounding direction analysis, in 2023.

Now, in 2025, arithmetic and correct precision are as critical as ever. The flaws that led to the biggest hacks of 2021 and 2022, such as private key compromise, continue to occur and remain a significant risk. However, it’s clear that several aspects of the blockchain and DeFi ecosystems have matured, and the attacks have become more sophisticated in response, particularly for major protocols like Uniswap and Balancer, which have undergone thorough testing and auditing over the last several years.

## Preventing rounding issues in 2025

In 2025, rounding issues are as critical as ever, and the most robust way to protect against them is the following:

### Invariant documentation

DeFi protocols should invest resources into documenting all the invariants pertaining to precision loss and rounding direction. Each of these invariants must be defended using an informal proof or explanation. The canonical invariant “rounding must favor the protocol” is insufficient to capture edge cases that may occur during a multi-operation user flow. It is best to begin documenting these invariants during the design and development phases of the product and using code reviews to collaborate with researchers to validate and extend this list. Tools like
[roundme](https://github.com/crytic/roundme)
can be used to identify the rounding direction required for each arithmetic operation to uphold the invariant.

![Image showing Appendix H from our 2021 Balancer v2 review](/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/balancer_image2_hu_9a6d481ae3e57815.webp)


Figure 1: Appendix H from our October 2021 Balancer v2 review

Here are some great resources and examples that you can follow for invariant testing your system:

### Comprehensive unit and integration tests

The invariants captured should then drive a comprehensive testing suite. Unit and integration testing should lead to 100% coverage. Mutation testing with solutions like
[slither-mutate](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
and
[necessist](https://github.com/trailofbits/necessist)
can then aid in identifying any blind spots in the unit and integration testing suite. We also wrote a blog post earlier this year on
[how to effectively use mutation testing](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
.

Our work for
[CAP Labs in 2025](https://github.com/trailofbits/publications/blob/master/reviews/2025-05-caplabs-coveredagentprotocol-securityreview.pdf)
contains extensive guidance in Appendix D on how to design an effective test suite that thoroughly unit, integration, and fuzz tests the system’s invariants.

![Image showing Appendix D for 2024 CAP Labs review](balancer_image1.png)


Figure 2: Appendix D from our
[2025 CAP Labs Covered Agent Protocol review](https://github.com/trailofbits/publications/blob/master/reviews/2025-05-caplabs-coveredagentprotocol-securityreview.pdf)

### Comprehensive invariant testing with fuzzing

Once all critical invariants are documented, they need to be validated with strong fuzzing campaigns. In our experience, fuzzing is the most effective technique for this type of invariant testing.

To learn more about how fuzzers work and how to leverage them to test your DeFi system, you can read the documentation for our fuzzers,
[Echidna](https://secure-contracts.com/program-analysis/echidna/index.html)
and
[Medusa](https://secure-contracts.com/program-analysis/medusa/docs/src/index.html)
.

### Invariant testing with formal verification

Use formal verification to obtain further guarantees for your invariant testing. These tools can be very complementary to fuzzing. For instance, limitations or abstractions from the formal model are great candidates for in-depth fuzzing.

## Four Lessons for the DeFi ecosystem

This incident offers essential lessons for the entire DeFi community about building and maintaining secure systems:

**1. Math and arithmetic are crucial in DeFi protocols**

See the
[above section](#preventing-rounding-issues-in-2025)
for guidance on how to best protect your system.

**2. Maintain your fuzzing suite and inform it with the latest threat intelligence**

While smart contracts may be immutable, your test suite should not. A common issue we have observed is that protocols will develop a fuzzing suite but fail to maintain it after a certain point in time. For example, a function may round up, but a future code update may require this function to now round down. A well-maintained fuzzing suite with the right invariants would aid in identifying that the function is now rounding in the wrong direction.

Beyond protections against code changes, your test suite should also evolve with the latest threat intelligence. Every time a novel hack occurs, this is intelligence that can improve your own test suite. As shown in the
[Sonne Finance](https://blog.hundred.finance/15-04-23-hundred-finance-hack-post-mortem-d895b618cf33)
incident, particularly for these arithmetic issues, it’s common for the same bugs (or variants of them) to be exploited many times over. You should get in the habit of revisiting your test suite in response to every novel incident to identify any gaps that you may have.

**3. Design a robust monitoring and alerting system**

In the event of a compromise, it is essential to have automated systems that can quickly alert on suspicious behavior and notify the relevant stakeholders. The system’s design also has significant implications for its ability to react effectively to a threat. For example, whether the system is pausable, upgradeable, or fully decentralized will directly impact what can be done in case of an incident.

**4. Mitigate the impact of exploits with secondary controls**

Even high-assurance software like DeFi protocols has to accept some risks, but these risks must not be accepted without secondary controls that mitigate their impact if they are exploited. Earlier this year, we wrote about using secondary controls to mitigate private key risk in
[Maturing your smart contracts beyond private key risk](/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/)
, which explains how controls such as rate limiting, time locks, pause guardians, and other secondary controls can reduce the risk of compromise and the blast radius of a hack via an unrecognized type of exploit.