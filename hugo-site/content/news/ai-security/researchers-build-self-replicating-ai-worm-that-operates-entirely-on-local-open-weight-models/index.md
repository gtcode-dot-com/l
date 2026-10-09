---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T01:36:01.234769+00:00'
exported_at: '2026-06-11T01:36:03.792665+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html
structured_data:
  about: []
  author: ''
  description: An AI-driven worm using a local open-weight LLM autonomously exploited
    and replicated across 62% of a 33-host test network in 7 days.
  headline: Researchers Build Self-Replicating AI Worm That Operates Entirely on Local,
    Open-Weight Models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Researchers Build Self-Replicating AI Worm That Operates Entirely on Local,
  Open-Weight Models
updated_at: '2026-06-11T01:36:01.234769+00:00'
url_hash: d856d553da2014c0dd26aff1b56d5702bcf0849b
---

University of Toronto researchers have built and tested a proof-of-concept AI-driven computer worm that uses a locally hosted open-weight large language model to reason its way through a network, generate tailored attack strategies for each target it encounters, and replicate itself, all without human intervention and without touching a commercial AI service.

The preprint,
[posted to arXiv](https://arxiv.org/pdf/2606.03811)
on June 2 and currently under peer review, shows why single-CVE patching breaks down when malware can inspect exposed services, read fresh advisories, and generate a new attack path at runtime.

In 15 isolated runs on a deliberately vulnerable 33-host network, the worm identified an average of 31.3 vulnerabilities and gained elevated access on 23.1 hosts, roughly three-quarters of the hosts it actively targeted. It then replicated autonomously to 20.4 of those hosts, or 62% of the full network, over seven days, with no prior knowledge of the network topology and no human input.

Traditional worms ship with a fixed exploit payload chosen at build time. Patch those specific bugs, and the worm stops spreading.

This worm does something different: it uses an open-weight LLM running on a single GPU to generate attack logic at runtime, tailored to whatever it finds on the next target. No pre-encoded exploit chain. No dependency on OpenAI, Anthropic, or any other API that a platform could revoke or rate-limit.

## What the worm actually did

Led by associate professor Nicolas Papernot, the
[CleverHans Lab](https://cleverhans.io/latest-research.html)
team spans the University of Toronto, Vector Institute, University of Cambridge, and ServiceNow. They ran 15 independent experiments on an isolated 33-host network ("FakeCorp") spanning Ubuntu, Debian, Rocky Linux, Alpine, Windows Server 2008 R2, 2019, and 2022, and IoT devices.

Each host had at least one real-world vulnerability. Five of the 33 machines had GPUs. In the main propagation experiments, the worm used a shared GPU inference pool to simulate compute acquired from victim machines. The team separately tested full GPU-tier replication, in which the worm stages a local LLM instance on a compromised GPU host; that succeeded in 68.8% of attempts.

In the tiered design, infected GPU-capable hosts serve as distributed reasoning nodes that provide inference for lower-compute devices on the network that cannot run the model themselves.

Across the 15 runs, the worm gained elevated access on 23.1 hosts and successfully launched a replica on 88% of those. It reached up to seven generations of self-replication, with a mean of 5.1. The setup was intentionally vulnerable: the paper says the test measures autonomous reasoning across realistic individual flaws, not spread through a mostly hardened production network under active endpoint defense.

Exploits across a single run included a chained SambaCry and writable root cron privilege escalation,
[Dirty Pipe](https://thehackernews.com/2022/03/researchers-warn-of-linux-kernel-dirty.html)
,
[PrintNightmare](https://thehackernews.com/2021/07/microsoft-warns-of-critical.html)
,
[Drupalgeddon 2](https://thehackernews.com/2018/06/drupalgeddon2-exploit.html)
,
[Exim RCE](https://thehackernews.com/2026/05/new-exim-bdat-vulnerability-exposes.html)
, blind SQL injection, JWT bypass, Redis escape, and more, not because they were pre-programmed, but because the agent reasoned its way to them from what it found on each host.

The paper's Figure 2 maps the full radial propagation tree across one run, showing six to seven generations of spread across Linux, Windows, and IoT hosts. Individual exploit attempts succeeded about 44% of the time. Most failures came from malformed payload syntax, not flawed logic. Web app exploits and Windows privilege escalation were harder than Linux local escalation and service exploits, a capability ceiling the paper treats as a current model limitation, not a structural defense.

## The patching-window problem

The worm bypassed its own training cutoff by ingesting public advisory text at runtime, successfully exploiting test hosts configured with three vulnerabilities disclosed after the model was trained:

Against those three hosts, the worm reached root in 41 of 67 attempts.

CVE-2026-39987 was disclosed on April 8, 2026. Sysdig observed
[exploitation in honeypots](https://thehackernews.com/2026/05/attackers-use-llm-agent-for-post.html)
9 hours and 41 minutes after that, and separately documented a real-world intrusion where an attacker used an LLM agent for post-exploitation activity after compromising a public Marimo instance. Same old patch gap, now with an agent reading the advisory and trying it at scale.

The relevant parallel to WannaCry is the patch gap, not the blast radius.
[EternalBlue](https://thehackernews.com/2017/04/window-zero-day-patch.html)
had been patched for months before WannaCry struck. The paper is making the same point under a different constraint: an adaptive worm can keep testing new paths while defenders are still validating fixes.

## Zero marginal cost, no central kill switch

Two things make this harder to contain than a traditional worm.

* First, the cost shifts from rented API access to whatever compute the worm can capture. Once a GPU-capable victim infrastructure exists, the attacker no longer pays per attempt.
* Second, because everything runs on open-weight models with no vendor dependency, provider-side controls miss the core problem. Service refusals, rate limiting, account suspension: none of it applies. There is no API key to revoke. Containment has to happen at the network and host layer.

The researchers also observed the worm rewrite its own code on several occasions to bypass local security controls in the test environment, behavior they never coded for.

The current version was deliberately built without stealth features: no encryption, no polymorphic code, no persistence mechanisms, no covering of tracks. A malicious variant with persistence, encrypted payloads, process masquerading, and log cleanup would give defenders fewer of the easy signals this prototype leaves behind.

## Where this fits

This is not the first AI-driven worm research. Morris II (Cohen et al., 2025) showed a self-replicating adversarial prompt spreading across AI email assistants through retrieval-augmented generation, propagation within the AI application layer, not across host infrastructure.

In March 2026,
[ClawWorm](https://arxiv.org/abs/2603.15727)
demonstrated self-replicating attacks across LLM agent ecosystems, hijacking persistent configurations and propagating to agent peers. The Toronto worm is different in kind: the LLM is not the thing being attacked. It is the attack engine being used to compromise ordinary network infrastructure.

Real-world operations are already testing the same boundary. Anthropic said in November 2025 that it disrupted a
[large AI-orchestrated espionage campaign](https://thehackernews.com/2025/11/chinese-hackers-use-anthropics-ai-to.html)
attributed with high confidence to GTG-1002, a Chinese state-sponsored group. Claude Code handled 80-90% of the operation, including reconnaissance, exploit development, credential harvesting, lateral movement, and exfiltration, with humans stepping in at a few decision points.

Google's Threat Intelligence Group
[reported a related shift](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)
in May 2026: what it assessed with high confidence to be the first zero-day exploit developed with AI assistance, found in a criminal group's script ahead of a planned mass exploitation event, alongside malware families that generate their own commands at runtime rather than relying on hardcoded logic. The Toronto work is the lab version of that direction pushed into host-level worm propagation.

The direction is clear enough: less prompting, more delegation, and more of the intrusion handed to the model.

## What should defenders do now?

The behavioral signals this prototype produces give defenders something concrete to hunt for, because the current version does not try to hide.

* **Segment GPU-capable machines aggressively.**
  The worm's design routes LLM inference through any compromised GPU host it can reach. In a flat network, one compromised deep-learning server becomes a reasoning hub for every infected device on the same subnet. Segment GPU infrastructure and apply zero-trust controls to prevent lateral reach to and from those hosts.
* **Treat published advisories as near-term weaponization targets.**
  For internet-facing CVEs, the exploitation window is already measured in hours for some vulnerabilities. Verify exploitability fast, patch internet-facing exposure first, and use compensating controls when deployment cannot happen before the next business cycle.
* **Rotate credentials exposed on any compromised or credibly suspected host.**
  The worm demonstrated systematic credential reuse as a propagation path. Harvested credentials move laterally faster than most detection cycles.
* **Monitor for agent-specific behavioral signals.**
  Non-standard port activity, automated SSH public key injection, and clusters of LLM inference appearing on unexpected endpoints are the observable artifacts this prototype leaves behind. They are the starting point for detection logic.

In the test runs, that combination produced root on fresh vulnerabilities in 41 of 67 attempts and replication to 62% of the network in seven days with no further human input. Once a GPU foothold exists inside a flat network, the cost of mapping and exploiting additional hosts drops to whatever compute the worm can capture, while public advisories become immediate playbooks.

The implementation is not publicly released. The University of Toronto is establishing a vetting process for qualified defensive researchers to request access.