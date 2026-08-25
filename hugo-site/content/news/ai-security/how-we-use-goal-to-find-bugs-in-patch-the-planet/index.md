---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-25T18:45:00.632920+00:00'
exported_at: '2026-08-25T18:45:03.107215+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet
structured_data:
  about: []
  author: ''
  description: Over the first few weeks of Patch the Planet, our engineers found three
    techniques for using /goal, which hands Codex an open-ended objective and lets
    it work independently toward a success condition.
  headline: How we use /goal to find bugs in Patch the Planet
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How we use /goal to find bugs in Patch the Planet
updated_at: '2026-08-25T18:45:00.632920+00:00'
url_hash: fc361ecb8b8c1f1ae5fa4cee9f80e0f374771d11
---

Codex’s
`/goal`
feature amplifies bug hunting, but getting good results requires the right prompt, the right scope, and the right number of outcomes per run. For
[Patch the Planet](https://trailofbits.com/patch-the-planet)
, our joint initiative with OpenAI to find and fix bugs in open-source software, we pointed Codex at some of the most widely used, heavily audited codebases in the world, like Rust, curl, and zlib. One tool came up again and again in our internal bug-report channels:
`/goal`
, which hands Codex an open-ended objective and lets it work independently toward a success condition. Here are a few highlights:

* `/goal`
  found every Rust bug we submitted, including a soundness hole and a miscompilation now patched in Rust 1.98, from a single variant-analysis pipeline.
* It turned every project’s past CVEs into Semgrep rules that had to fire on the vulnerable version and stay silent on the patched one, then flagged 11 variant hits across multiple projects.
* It uncovered two potential high-severity privilege-escalation bugs in Keycloak’s SAML component during a discovery run.

Over the first few weeks of Patch the Planet, our engineers independently converged on three techniques for using
`/goal`
. We found that getting the most out of
`/goal`
means treating the prompt as a set of specific success criteria, not a set of instructions. (Note that this blog post uses
`/goal`
to refer to goal-based prompting in general. Codex can also set goals for itself through a tool call, and that’s how we recommend everyone use it; we rarely type the slash command ourselves.)

## 1. Let Codex write the goal

The art of using
`/goal`
is prompt design, and we found that Codex knows Codex the best. Internally, our single most repeated
`/goal`
tip was to use Codex to help write each
`/goal`
prompt. We hand Codex threat model files and the context about what we’re looking for, and then tell it to write the goal prompt. As mentioned before,
`/goal`
is a tool Codex can invoke on itself, and a few engineers stopped typing goals by hand entirely.

&gt; $goal-prompt based on threat model write goal to find single critical issue (RCE) exploitable by remote attacker for kubernetes-client. the kubernetes-client is used in normal config, malicious remote users exploits.

Figure 1: A meta-prompt from one of our engineers asking Codex to create a goal prompt. Results are shown in figure 2.

This works because Codex knows the target and its own tendencies better than we can specify up front. It can translate a threat model into concrete, testable success criteria, name the code paths worth prioritizing, and phrase the outcome precisely enough that a run actually converges. A goal written this way tends to be tighter than one we’d write cold, and it takes a fraction of the time.

Letting the model draft the goal also closes a gap we’d otherwise miss. Any outcome you define can be satisfied in ways you didn’t intend, and the model is often the first to spot where the easy outs are.

Now when we ask Codex to draft a goal, we ask it to red-team its own goal by identifying the ways a future model might be lazy in its approach, and to revise the criteria to remove them before the run starts. We also built tooling that makes it easier for Codex to verify its own work. For example, we noticed Codex has a tendency to skip reading the entire codebase even when explicitly asked. We built
[aicov](https://github.com/trailofbits/aicov)
, a tool that tracks what lines of code Codex has actually read, so it can’t “cheat.”

This is an iterative process. As we find more shortcuts a model takes, we exclude them from the next version of the prompt.

## 2. Define the outcome, not the path

A good goal names the outcome, defines it precisely, and then enforces persistence:

&gt; /goal Audit the kubernetes-client repository in this workspace to find exactly one previously unreported critical remote code execution vulnerability reachable in normal/default client configuration by a malicious remote user or server that controls only network/API responses, Kubernetes objects the client legitimately fetches, or other remote data accepted during normal use.
&gt;
&gt; First build a concise threat model of realistic remote attacker entry points and trust boundaries, then prioritize code paths involving deserialization, YAML/JSON/protobuf parsing, dynamic imports/eval/template execution, archive/file extraction, auth redirects, generated client hooks, websocket/exec/attach/port-forward streams, and subprocess or filesystem effects. Do not assume attacker control of local kubeconfig, CLI arguments, environment variables, installed plugins, source code, credentials, privileged cluster/admin access, or prior code execution; explicitly reject findings that rely on those preconditions. Before accepting a candidate, search local known-findings files plus current open issues/PRs for duplicates, then produce a minimal safe proof that demonstrates attacker-controlled code execution or a direct RCE primitive under the stated normal configuration. Stop after one valid critical issue. Write finding to ./findings/ folder.

Figure 2: The prompt created by Codex from figure 1

We found the best philosophy is to
**spend as many tokens as you need defining the outcome, and almost none telling the model how to get there.**

If you want the bug found through fuzzing, “use fuzzing” is as far as you should go. “Build on top of my existing fuzzing harness” or “build a new fuzzing harness” are both worse. There might be an existing harness that’s just as good. A goal that prescribes the path guarantees Codex never takes another one, and you lose the judgment and open-ended problem solving that make
`/goal`
unique.

The outcome side takes more care because it has to be calibrated. If it’s too specific, Codex doesn’t have enough to search and the value of an autonomous
`/goal`
run is unclear. When we fed Codex the exact root cause of a known bug and asked it to find variants, it found nothing. The scope was too narrow. When we cut the input down to a single sentence describing the
*class of bugs*
it should look for based on the known bug, it surfaced numerous bugs. We reported 9 of them, with 3 already fixed and merged upstream.

If an outcome is too vague, the model provides outputs that don’t match what you were looking for. One of the worst
`/goal`
prompts we saw during Patch the Planet was “find bugs in [X].” The model had no way to tell when it was done. It just kept running, surfacing bugs that had no real-world impact, and wasting tokens.

A complete outcome definition also says what doesn’t count as done. The open-source projects in Patch the Planet have some of the most audited code in the world, and more than once
`/goal`
came back with “no bugs found.” We treat that as an intermediate result, not a completion condition, and write persistence into the goal itself.

**The most effective resource for
`/goal`
bug hunting is a
`THREAT_MODEL.md`
file.**
We ended up referencing a threat model file in almost every goal we ran because it precisely defines what valid bugs look like without explaining how to find them. We recommend every open-source project create one.

## 3. Assign one outcome per agent

Putting two competing outcomes in one
`/goal`
prompt results in uneven optimization. We ran into this repeatedly when a goal asked for both bugs and coverage. When we put “find bugs” and “achieve high coverage” in the same prompt, the run ended up doing one of them far better than the other.

This was our experience while using
`/goal`
to audit zlib. Codex kept gravitating to the same part of the codebase, fuzzing the areas the model found first without reaching the rest. Our initial instinct was to fix that in the prompt by adding coverage requirements, but Codex then switched its optimization to coverage, and we saw lackluster vulnerability hunting.

What worked instead was moving coverage out of the prompt entirely. We asked Codex to first identify the five most promising attack surfaces after scouring through the entire codebase. Then we created a separate
`/goal`
session to find bugs in each section. We also added one fully open-ended session alongside them to roam the parts of the codebase the other agents weren’t assigned. This approach worked
[drastically better](https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/)
.

![“Figure 3: Rust maintainers assumed we had a team of engineers working on finding bugs. It was just one engineer with a strong handle on Codex’s /goal.”](/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/goal_ptp_figure_3_hu_2a14b2f59f76ba60.webp)


Figure 3: Rust maintainers assumed we had a team of engineers working on finding bugs. It was just one engineer with a strong handle on Codex's /goal.

One of our engineers, Kevin Valerio, created an automated variant-analysis system for the Rust compiler leveraging
`/goal`
. Every Rust bug we submitted through Patch the Planet came out of it.

1. P-critical is a label created by Rust maintainers to identify bugs that should be prioritized to patch and merge. The pipeline began by downloading every issue tagged P-critical in the rust-lang/rust repository as JSON.
2. An orchestrator reads the issues and spawns a separate agent for each one. One outcome per agent: instead of a single session told to perform variant-analysis on each bug, the orchestrator creates one Codex session per issue, each running an independent task to find a single outcome.
3. Each session runs in Goal mode with a deliberately small prompt to find a security issue with the same root cause as the original bug in P-critical. It receives a one-sentence description of the risk rather than an exact root cause with a full backtrace, so the model can still have the freedom to explore the codebase more.
4. Before any variant hunt begins, a security gate asks whether the source issue is even a real vulnerability and routes it to skip, no\_variant, or bug\_found. We are using that to focus on the most impactful P-critical bugs.
5. Every candidate runs a two-pass false-positive gauntlet. The first judge checks that the bug poses a genuine security risk. The second, a different model entirely, runs a PoC-focused pass and demands that the issue can potentially cause security issues relevant to the Rust threat model. A candidate reaches “validated finding” only if both passes agree.
6. Validated findings pass one last human filter. A duplicate check happens before anything is opened. Only bugs that are confirmed upstream and not already found in GitHub’s issue backlog are drafted for submission.

![“Figure 4: The full workflow Kevin Valerio used to find every bug in Rust”](/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/goal_ptp_figure_4_hu_b6101cf6b22bf7cc.webp)


Figure 4: The full workflow Kevin Valerio used to find every bug in Rust

## Where human judgment is needed

Since its release,
`/goal`
has been a powerful tool for amplifying the bug-hunting work that we do. Codex can create custom security infrastructure that takes a security researcher weeks to build in under a day. It can scour thousands of lines of code faster than any human can.

`/goal`
will faithfully pursue whatever outcome we give the model, which means the run is mostly decided before the model starts. But its effectiveness still depends on an expert knowing where to look, verifying its results count as a reportable finding, and knowing what the maintainers on the other side actually want to see as a valid vulnerability disclosure. Prompt engineering is a large part of it, but you can only write a good prompt if you know exactly what you’re looking for.