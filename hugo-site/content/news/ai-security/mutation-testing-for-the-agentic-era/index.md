---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T08:15:15.630569+00:00'
exported_at: '2026-04-02T08:15:18.256431+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era
structured_data:
  about: []
  author: ''
  description: Today, we’re announcing MuTON and mewt, two new mutation testing tools
    optimized for agentic use.
  headline: Mutation testing for the agentic era
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mutation testing for the agentic era
updated_at: '2026-04-02T08:15:15.630569+00:00'
url_hash: f49e9ea23a99c10a128c33388668f1a74c473b00
---

Code coverage is one of the most dangerous quality metrics in software testing. Many developers fail to realize that code coverage lies by omission: it measures execution, not verification. Test suites with high coverage can obfuscate the fact that critical functionality is untested as software develops over time. We saw this when mutation testing uncovered a
[high-severity Arkis protocol vulnerability](https://github.com/trailofbits/publications/blob/master/reviews/2024-12-arkis-defi-prime-brokerage-securityreview.pdf)
, overlooked by coverage metrics, that would have allowed attackers to drain funds.

Today, we’re announcing
[MuTON](https://github.com/trailofbits/muton)
and
[mewt](https://github.com/trailofbits/mewt)
, two new mutation testing tools optimized for agentic use, along with a
[configuration optimization skill](https://github.com/trailofbits/skills/tree/main/plugins/mutation-testing)
to help agents set up campaigns efficiently. MuTON provides first-class support for TON blockchain languages (FunC, Tolk, and Tact), while mewt is the language-agnostic core that also supports Solidity, Rust, Go, and more.

The goal of mutation testing is to systematically introduce bugs (mutants) and check if your tests catch them, flagging hot spots where code is insufficiently tested. However, mutation testing tools have historically been slow and language-specific. MuTON and mewt are built to change that. To understand how, it helps to first understand what they’re replacing.

## The regex era

Mutation testing dates to the 1970s, but for a long time, the technique rarely saw much adoption in the blockchain space as a software quality measurement. Testing frameworks are coupled tightly to target languages, making support for new languages expensive.

[Universalmutator](https://agroce.github.io/icse18t.pdf)
changed this with its regex engine. After a commit on March 10, 2018 added Solidity support, the tool gained immediate traction in the blockchain space. We collaborated with the universalmutator team to advance smart contract testing and highlighted the tool in our
[2019 blog post](https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/)
. Despite (or perhaps because of) its elegant approach and compact codebase, universalmutator generated impressive mutant counts, enabling developers to assess test coverage more thoroughly than simpler tools could. Vyper and other language support followed, establishing universalmutator as the leading mutation testing tool for blockchain.

But regex has fundamental limits. Line-based patterns cannot mutate multi-line statements, a critical gap acknowledged by the original paper. More problematic: without mutant prioritization, the tool wastes time on redundant mutations. When commenting a line triggers no test failures, universalmutator still generates and tests every possible variation of that line, dramatically extending campaign runtime. Printing the results to
`stdout`
adds further friction for humans and AI agents reviewing campaigns. Later improvements (including a
[2024 switch to comby](https://agroce.github.io/fse24.pdf)
for better syntactic handling) addressed some pain points, but remaining limitations prompted the development of more focused alternatives.

Between 2019 and 2023, several tools emerged to address them, including our own
[slither-mutate](https://github.com/crytic/slither/blob/master/docs/src/tools/Mutator.md)
solution. Each took a different approach to the core problems of language comprehension, scalability, and test quality.

## slither-mutate: Speed through prioritization

We launched
[slither-mutate](https://github.com/crytic/slither/blob/master/docs/src/tools/Mutator.md)
in August 2022, after our wintern,
[Vishnuram](https://github.com/vishnuram1999)
, brought the concept to life. Because Slither already parsed Solidity’s AST and provided a Python API, the groundwork was laid to generate syntactically valid mutations and implement a cleaner tweak-test-restore cycle (earlier tools polluted repositories with mutated files).

The tool’s key innovation was mutant prioritization: high-severity mutants replace statements with reverts (exposing unexecuted code paths), medium-severity mutants comment out lines (revealing unverified side effects), and low-severity mutants make subtle changes, such as swapping operators. The tool skips lower-severity mutants when higher-severity ones already indicate missing coverage on the same line, dramatically reducing campaign runtime, the biggest obstacle to wider mutation testing adoption. By late 2022, we were deploying slither-mutate across most Solidity audits.

Two limitations remained. First, tight coupling to Solidity meant there was no path to easily support other blockchain languages. Second, dumping results to
`stdout`
persisted as a problem, but adding a database to Slither creates unacceptable friction for the broader Slither user base.

## Introducing MuTON and mewt: The tree-sitter era

MuTON, our newest mutation testing tool, provides first-class support for all three TON blockchain languages: Tolk, Tact, and FunC. We’re grateful to the
[TON Foundation](https://ton.foundation/)
for supporting its development. MuTON is built on mewt, a language-agnostic mutation testing core that also supports Solidity, Rust, and more.

MuTON achieves language comprehension comparable to slither-mutate while supporting multiple languages by using Tree-sitter as its parser. Tree-sitter powers syntax highlighting in modern editors, building a concrete syntax tree that distinguishes language keywords from comments. This allows MuTON to target expressions like if-statements in a well-structured way, handling multi-line statements gracefully. Traditionally, integrating Tree-sitter grammars for new language support takes orders of magnitude longer than writing regex rules, but AI agents paired with
[bespoke skills](https://github.com/trailofbits/mewt/blob/main/.claude/skills/add-language-support/SKILL.md)
invert this calculus, delivering Tree-sitter’s power with regex-like ease of extension.

MuTON stores all mutants and test results in a SQLite database, a quality-of-life improvement that became evident while using slither-mutate but wasn’t feasible to retrofit. Results persist across sessions; campaigns can be paused and resumed without losing progress. If you accidentally close your terminal during a 24-hour campaign, your work survives. Persistent storage also enables flexible filtering and formatting: print only uncaught mutants in specific files, or translate results to SARIF for improved review. This flexibility helps humans and AI agents explore results, triage findings, and hunt for bugs.

## The future of mutation testing

MuTON addresses many historical pain points, but significant friction remains. Three challenges stand between mutation testing and widespread adoption: configuring campaigns for reasonable runtimes, triaging results to separate signal from noise, and generating tests that encode requirements rather than accidents. AI agents, equipped with specialized skills, promise to transform each of these obstacles into routine tasks.

## Optimizing configuration

Performance remains the biggest obstacle to mutation testing. If your test suite takes five minutes and you have 1,000 mutants, that’s 83 hours of unavoidable runtime. Mutation testing tools can’t fix slow tests, but smart configuration can dramatically reduce wasted time. MuTON already gives you powerful options to tune campaigns: target critical components instead of everything, use two-phase campaigns that run fast targeted tests first and then retest uncaught mutants with the full suite, configure per-target test commands so mutations in authentication code only trigger authentication tests, or restrict to high and medium severity mutations when time is tight. These tools work today and deliver real speedups.

But the decision tree branches endlessly: should you split by component or severity? Two-phase or targeted tests? What timeout accounts for incremental recompilation? We’ve released a
[configuration optimization skill](https://github.com/trailofbits/skills/tree/main/plugins/mutation-testing)
that guides AI agents through these choices, measuring your test suite, estimating runtimes, and proposing optimal configurations tailored to your project structure. Try it now—it’s available in our public skills repository and makes the process painless.

## Triaging results

Not all uncaught mutants matter. Mutations that change
`x > 0`
to
`x != 0`
are semantic no-ops when
`x`
is an unsigned integer. A perfect mutator wouldn’t generate such mutations in the first place, but that would require deeper language-specific understanding than Tree-sitter provides. Manual triage traditionally requires slogging through hundreds of results, checking types, and understanding context to extract actionable insights.

MuTON’s database and flexible filtering already make this dramatically easier. Filter by mutation type or specific files to highlight high-value results. More importantly, these filters make AI-assisted triage token-efficient in ways earlier tools dumping raw output to
`stdout`
never could. Even today, asking an agent to review filtered mutation results and summarize true positives delivers 80% of the insights for 1% of the manual work. We’re developing a triage skill that systematically guides agents through result analysis, identifying patterns such as clustered uncaught mutants (a strong bug indicator) versus isolated operator mutations in utility functions (likely false positives or low priority). The skill will help agents flag high-risk areas and explain why specific mutations matter, turning raw results into actionable security insights.

## The promise and peril of mutation-driven test generation

At first glance, using mutation testing to guide AI agents in writing tests seems like an elegant solution: test mutants, find escapees, generate tests to catch them, repeat until coverage is complete. But this naive approach harbors a subtle danger: an uncritical agent doesn’t know whether it’s encoding correct behavior or propagating bugs into your test suite.

When mutation testing reveals that changing
`priority >= 2`
to
`priority > 2`
alters behavior, should the agent write a test asserting that
`priority == 2`
triggers an action? Maybe. Or maybe that’s a bug, and now you’ve corrupted your tests with the same incorrect logic, giving false confidence while doubling your maintenance burden. The real challenge isn’t generating tests that just catch mutants; it’s generating tests that encode requirements rather than implementation accidents.

We believe the solution lies in building agents that are skeptical, that halt and ask questions when they encounter suspicious or ambiguous patterns, and that demand external validation before crystallizing behavior into tests. It’s a subtle problem that balances AI’s strengths with developers’ limited attention, but we’re working on it. Stay tuned.

## Dive in

Ready to test your smart contracts? Install
[MuTON](https://github.com/trailofbits/muton?tab=readme-ov-file#installation)
for TON languages, or
[mewt](https://github.com/trailofbits/mewt?tab=readme-ov-file#installation)
for Solidity, Rust, and more. Run a campaign and discover your blind spots. Found a bug in TON language support? File an issue in MuTON. See room for improvement in the core framework or other languages? Join us in the mewt repository. Both projects are open source and welcome contributions.

Watch our
[skills](https://github.com/trailofbits/skills)
repository for new skills that will guide AI agents through campaign setup and result analysis, transforming mutation testing from a manual slog into a routine part of the development process.