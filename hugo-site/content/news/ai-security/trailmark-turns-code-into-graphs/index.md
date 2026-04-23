---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-23T12:15:13.861933+00:00'
exported_at: '2026-04-23T12:15:16.736996+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/04/23/trailmark-turns-code-into-graphs
structured_data:
  about: []
  author: ''
  description: Trailmark turns source code into a security-analysis graph, powering
    eight Claude Code skills for blast radius, taint propagation, and mutation test
    triage.
  headline: Trailmark turns code into graphs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/04/23/trailmark-turns-code-into-graphs
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trailmark turns code into graphs
updated_at: '2026-04-23T12:15:13.861933+00:00'
url_hash: db6e2648d4cbb5d7611ef66a9223e6689cd52a2d
---

We’re open-sourcing
[Trailmark](https://github.com/trailofbits/trailmark)
, a library that parses source code into a queryable call graph of functions, classes, call relationships, and semantic metadata, then exposes that graph through a Python API that Claude skills can call directly. Install it now:

`uv pip install trailmark`

“Defenders think in lists. Attackers think in graphs. As long as this is true, attackers win.” John Lambert’s
[widely cited observation](https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md)
about network security applies just as well to AI-assisted software analysis.

When Claude reasons about a codebase, it reasons about lists: findings from static analyzers, surviving mutants from mutation testing, and line-by-line coverage reports. But the question that actually matters is a graph question:
*can untrusted input reach this code, and what breaks if it’s wrong?*

We built Trailmark to answer that question. It gives Claude a graph to think with instead of a list. We’re also releasing eight Claude Code skills we’ve built on top of it, designed for mutation triage, test vector generation, protocol diagramming, and more.

## When lists fall short

Mutation testing is a great example of a method that benefits from graph-level reasoning. It’s one of the best ways to measure test quality. It makes small changes to your source code (e.g., swapping a
`<`
for
`<=`
, replacing
`+`
with
`-`
) and checks whether your tests catch the difference. Mutants that survive reveal gaps in your test suite that code coverage metrics might miss. The downside is that a mutation testing run on a real codebase can produce hundreds of surviving mutants of varying significance. This is very much a
*list*
.

Some surviving mutants are
*equivalent*
: the mutation doesn’t change the program’s behavior because of structural or mathematical constraints that the mutation testing tool can’t see. Some are in dead code; some are in error message formatting; some are in the finite field arithmetic that underpins every cryptographic operation in your library. A flat list of surviving mutants doesn’t tell you which is which.

We wanted to know whether Claude could use graph-level reasoning about a codebase to automatically triage surviving mutants by security relevance: which are reachable from untrusted input, which affect high-blast-radius functions, and which represent genuine gaps in security-critical code?

## How Trailmark works

Trailmark uses
[tree-sitter](https://tree-sitter.github.io/)
for language-agnostic AST parsing and
[rustworkx](https://www.rustworkx.org/)
for high-performance graph traversal. It operates in three phases:

1. **Parse**
   : Walk a directory, extract functions, classes, call edges, type annotations, cyclomatic complexity, and branch counts from source code.
2. **Index**
   : Load the resulting graph into a rustworkx PyDiGraph with bidirectional ID/index mappings for fast traversal.
3. **Query**
   : Answer questions: callers, callees, all paths between two nodes, attack surface enumeration, and complexity hotspots.

It currently supports 17 languages, including C, Rust, Go, Python, PHP, JavaScript, Solidity, Circom, and Miden Assembly.

The graph is the substrate. The skills are where the analysis happens.

## The skills

The Trailmark plugin ships eight Claude Code skills that use the graph API as their backbone:

| Skill | What it does |
| --- | --- |
| `trailmark` | Build and query a code graph with pre-analysis passes: blast radius, taint propagation, privilege boundaries, and entrypoint enumeration |
| `diagram` | Generate Mermaid diagrams from code graphs: call graphs, class hierarchies, complexity heatmaps, data flow |
| `crypto-protocol-diagram` | Extract protocol message flow from source code or specs (RFCs, ProVerif, Tamarin) into annotated sequence diagrams |
| `genotoxic` | Triage mutation testing results using graph analysis: classify surviving mutants as equivalent, missing test coverage, or fuzzing targets |
| `vector-forge` | Mutation-driven test vector generation: find coverage gaps via mutation testing, then generate Wycheproof-style vectors that close them |
| `graph-evolution` | Compare code graphs at two snapshots to surface security-relevant structural changes that text diffs miss |
| `mermaid-to-proverif` | Convert Mermaid sequence diagrams into ProVerif formal verification models |
| `audit-augmentation` | Project SARIF and weAudit findings onto code graph nodes as annotations, enabling cross-referencing of static analysis results with blast radius and taint data |

Each skill calls the Trailmark Python API directly. When
`genotoxic`
triages a surviving mutant, it queries
`engine.paths_between`
to check reachability from untrusted input. When
`diagram`
generates a complexity heatmap, it calls
`engine.complexity_hotspots`
. The graph is what makes those questions answerable in seconds rather than hours of manual tracing.

Trailmark also ingests SARIF output from static analyzers and
[weAudit](/2024/03/19/read-code-like-a-pro-with-our-weaudit-vscode-extension/)
annotations, mapping external findings onto graph nodes by file and line range. This lets Claude layer static analysis results, audit notes, and mutation testing data onto a single unified graph, then query across all of them.

## What Claude found

We’ve been using these skills internally on several cryptographic libraries, combining graph analysis with language-appropriate mutation testing frameworks. Here’s what the graph let Claude see that flat lists couldn’t.

### Equivalent mutants are the majority in well-tested crypto

When we ran mutation testing against an Ed448 implementation in Go, 45 mutants survived out of 583 covered. A flat list of 45 surviving mutants looks like a serious test gap. But when Claude used the Trailmark call graph (332 nodes, 3,259 call edges) to triage via
`genotoxic`
, 33 of those 45 (73%) were equivalent mutants. The mutations were unobservable because the code’s mathematical structure constrained values more tightly than the explicit bounds checks that were mutated.

For example, nine surviving mutants modified boundary conditions in NAF (non-adjacent form) digit range checks. These look like real bugs in isolation. But the NAF digits are structurally bounded by the
`nonAdjacentForm`
algorithm itself: the values that would trigger the altered boundary can never appear. The graph confirmed these functions were called from specific contexts that made the mutations undetectable.

The 12 genuine gaps were concrete and actionable: a cross-package coverage gap where Go’s coverage profiling attributed execution to the calling package instead of the defining package, a 255-byte context string boundary condition that was never tested, and overflow carry paths in wide-integer parsing that required near-maximum input values that no existing test vector produced.

### Architectural bottlenecks are invisible without a graph

When Claude built a Trailmark graph of
`libhydrogen`
, a compact C cryptographic library, the graph immediately highlighted something that wasn’t obvious from linearly reading the source files: the entire library funnels through a single permutation primitive,
`gimli_core_u8`
, which receives 37 direct calls. Every cryptographic operation (hashing, encryption, key exchange, signatures, and password hashing) depends on this one function.

This isn’t a bug. It’s a deliberate design choice common in lightweight crypto libraries. But it means the blast radius of a flaw in Gimli is total. The graph quantified this: a mutation in
`gimli_core_u8`
affects 100% of the library’s security-critical functionality. Gimli was also eliminated from the NIST Lightweight Cryptography competition. Together, these facts represent the kind of architectural risk that’s invisible in a line-by-line code review. The graph makes it obvious.

### Mutation testing finds what KATs can’t cover

For standardized algorithms like Ed25519 or ML-KEM, known-answer tests (KATs) and projects like
[Wycheproof](https://github.com/google/wycheproof)
provide test vectors that exercise edge cases. But for novel constructions (libhydrogen’s combination of Gimli and Curve25519, for instance), independent KATs don’t exist. No one has published “if you give Gimli-based AEAD this input, you should get this output” vectors, because the construction is unique to this library.

This is where mutation testing fills the gap. It doesn’t need reference implementations or published test vectors. It tests whether
*your*
tests actually constrain
*your*
code’s behavior. The surviving mutants tell you exactly which aspects of the implementation aren’t pinned down by your test suite, regardless of whether anyone else has ever tested that specific construction.

In the RustCrypto/KEMs crates (ML-KEM, X-Wing),
`vector-forge`
found that seven surviving mutants targeted NTT multiplication (mutations like replacing
`*`
with
`+`
in polynomial dot products). These survived because the test suite only exercised NTT through full KEM round-trips. The algebraic properties of NTT were never tested directly. Existing Wycheproof vectors and NIST KATs caught most higher-level issues, but the internal algebraic invariants had no direct coverage.

### Three patterns that showed up everywhere

Across multiple codebases analyzed with Trailmark, the same patterns emerged:

* **Blast radius concentrates in arithmetic modules.**
  In libsodium (1,597 nodes, 9,574 call edges), the ed25519\_ref10 module had the highest blast radius, underpinning Ed25519 signatures, Curve25519 key exchange, Ristretto255, and X-Wing KEM. In ML-KEM, the algebra module had a blast radius of 28; every polynomial and matrix operation depended on its Elem arithmetic. Graph analysis consistently identified these modules as the highest-priority targets for thorough testing.
* **Codec parsers are high-value fuzzing targets that rarely get prioritized.**
  Multiple analyses flagged hex/Base64 decoders and IP address parsers as high-complexity functions with external input exposure. libsodium’s
  `parse_ipv6`
  had a cyclomatic complexity of 18; libhydrogen’s
  `hydro_hex2bin`
  was the most complex function in the entire library, with a cyclomatic complexity of 11. These functions are natural targets for fuzzing, and the graph confirms they’re reachable from untrusted input.
* **Property-based testing is sparse.**
  Across the Rust cryptographic crates we examined, property-based testing was either absent or incomplete. The KEMs crates had zero property-based tests. Barrett reduction in ML-KEM was tested with only five points, even though exhaustive testing over all 11 million values of q = 3329 is computationally feasible. The graph’s blast radius analysis shows where property-based tests would have the greatest impact.

## Connecting the graph to everything else

The graph is most useful when it serves as the connective tissue between other analysis tools. When the constant-time analysis skill flags a function, Trailmark tells Claude its blast radius. When mutation testing produces survivors, Trailmark tells Claude which ones are reachable from untrusted input. When an auditor annotates a finding in weAudit,
`audit-augmentation`
shows what else in the graph is affected.

We use this internally to write targeted fuzzing harnesses. The graph identifies high-complexity functions reachable from external input; mutation testing identifies which of those functions have test gaps; the combination tells Claude exactly where a fuzzing harness will have the highest marginal value.

## Start querying your codebase

Trailmark is open source under
[Apache-2.0](https://github.com/trailofbits/trailmark)
. The library is on PyPI; the skills plugin is in the same repository.

**Install the library**
(required by the skills):

```
uv pip install trailmark
```

**Add the skills to Claude Code:**

```
/plugin marketplace add trailofbits/skills
```

Then select the Trailmark plugin from the menu.

You can also explore the graph directly from the CLI:

```
# Full JSON graph
trailmark analyze path/to/project

# Analyze a specific language
trailmark analyze --language rust path/to/project

# Complexity hotspots
trailmark analyze --complexity 10 path/to/project
```

Or call the Python API to build your own skills on top of the graph:

```
from trailmark.query.api import QueryEngine

engine = QueryEngine.from_directory("path/to/project", language="c")

# What's reachable from this entrypoint?
engine.callees_of("handle_request")

# Call paths from entrypoint to sensitive function
engine.paths_between("handle_request", "crypto_verify")

# Functions with cyclomatic complexity >= 10
engine.complexity_hotspots(10)

# Run pre-analysis (blast radius, taint, privilege boundaries)
engine.preanalysis()
```

The graph API is designed to be called by skills, not just humans. If you’re building Claude Code skills for security analysis, code review, or test generation, Trailmark gives you the structural substrate to ask questions that lists can’t answer.

Seventeen languages. A graph, not a list.
[The code is on GitHub](https://github.com/trailofbits/trailmark)
.