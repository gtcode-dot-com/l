---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-25T18:45:01.768033+00:00'
exported_at: '2026-08-25T18:45:03.087241+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/07/08/mutation-testing-comes-to-daml
structured_data:
  about: []
  author: ''
  description: In April we released Mewt, our open-source mutation-testing engine
    that finds the gaps in your test suite. Today we're expanding it with support
    for DAML, the language Canton Network applications are written in.
  headline: Mutation testing comes to DAML
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/07/08/mutation-testing-comes-to-daml
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mutation testing comes to DAML
updated_at: '2026-08-25T18:45:01.768033+00:00'
url_hash: c7f3ccc1bda7eb7e4198d78d49b4f14007df3d9d
---

In April we released
[Mewt](https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era/)
, our open-source mutation-testing engine that finds the gaps in your test suite. Today we’re expanding it with support for DAML, the language Canton Network applications are written in. Mewt now reads DAML, generates several classes of mutants (including two built for DAML’s authorization primitives), and runs them through your existing test suite to count how many mutants survive. If you want to try it, simply install Mewt from the
[repository](https://github.com/trailofbits/mewt)
, point a
`mewt.toml`
at your project and its test command, and use
`mewt run`
.

For a team shipping DAML to production, that count is what a passing test run is actually worth: it puts a number on how much your suite checks, whereas a green run on its own does not.

## Why DAML’s coverage reports lie

Test coverage is the most reassuring lie in smart-contract development. Hitting 100% line coverage tells you the test runner walked the code; it does not tell you whether any test would fail if that code stopped doing what it is supposed to. We have been grading test harnesses by how many mutants they kill since at least
[2019](https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/)
, and
[our primer on finding the bugs your tests don’t catch](https://blog.trailofbits.com/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
shows how a green suite can still miss the bug that matters.

DAML’s built-in coverage measures execution at the template and choice level: which templates were created and which choices were exercised over the test run. It reports whether each choice was exercised, not what happened inside it. A test that exercises a choice once and asserts nothing about the result reports that choice as covered. The report prints the same green percentage whether the test verifies the outcome or discards it.

## How mutation testing works

Instead of asking whether your tests reached the code, mutation testing grades your tests by sabotaging that code. The engine generates mutants, copies of the code that each carry one small deliberate change: a flipped comparison, a removed branch, a dropped party. It then runs your test suite against each one. A mutant that makes the suite fail is caught; a mutant that passes every test survives. Every survivor is a change your tests let through, and each one is either harmless or a potential bug. The harmless ones are equivalent code no test could distinguish or a branch no execution reaches, and you can set those aside. The rest are a to-do list: each one is a specific test you are missing, a case your suite should check but does not, occasionally with a real bug sitting behind the gap. The primer above describes a real audit where a mutation campaign surfaced a high-severity bug that the project’s tests had missed.

## Mutation testing forces the unhappy path

A DAML contract encodes rights and obligations between named parties: who holds what, who owes what to whom, and who must authorize each step. A party is not an anonymous address. It represents a real organization or person, and the contract is the rulebook for how those parties interact, including which of them can take which action, what each is allowed to see, and what stays private between them.

Authorization is how that rulebook is enforced: who may take which action. It is also easy to get wrong in ordinary ways, such as a typo in a controller clause, a missing party, an extra one left over from a refactor. Every combination type-checks, so nothing rejects it before it ships. A static analyzer can flag suspicious patterns, but it has no way to know which party should hold which authority on your contract. That knowledge lives in your specification, and for most projects, the only executable form of the specification is the test suite. Happy-path tests supply every signature the contract asks for and confirm the transaction succeeds. They never try the negative case—removing a required signature and checking that the ledger rejects the transaction—so they never actually test whether that signature was required at all. If the tests don’t encode that rule, nothing downstream can recover it. Mutation testing is what tells you whether they do.

A green test run tells you your tests passed today. Mutation testing asks the harder question: would your tests catch a mistake, now or after the next code change? Where the answer is no, you have found a test case worth writing.

## What Mewt adds for DAML

Mewt parses every language it supports with a tree-sitter grammar. As of mid-2026, there is no maintained tree-sitter grammar for DAML, so we reused the upstream
`tree-sitter-haskell`
grammar. DAML is Haskell-shaped, but its contract constructs (
`template`
,
`choice`
,
`controller`
, and
`signatory`
) are not Haskell, and the grammar parses them as error-recovered subtrees. That matters less than it sounds. The common mutations still work on DAML’s ordinary expressions, so Mewt swaps arithmetic and comparison operators, flips Booleans, and removes branches just as it does in any other language, with only small adjustments where DAML’s surface syntax differs (DAML writes
`/=`
where most languages write
`!=`
). We got most of the value of a from-scratch grammar without building one.

The new engineering went into DAML’s authorization primitives, where the authorization bugs from the previous section live. Mewt adds two DAML-specific mutations:

* **Controller party swap**
  (CPS in Mewt’s output): replace one party in a
  `controller`
  clause with another party that is in scope at that site.
* **Controller party removal**
  (CPR): drop one party from a multi-party controller list.

Both target the same question: if the set of parties allowed to exercise this choice silently changed, would any test fail? They are a deliberately small starting set aimed at the bug class above, and more DAML-specific mutations are in the pipeline.

Driving a campaign needs no new harness. A short
`mewt.toml`
names the files to mutate and the test command (
`dpm test`
for a Daml 3 project), and
`mewt run`
does the rest, reporting each mutant as caught or surviving. The setup is deliberately small: trying it on your own project costs minutes, and we encourage exactly that.

## What a surviving mutant looks like

Picture a conditional payment between a buyer and a seller: the buyer sets money aside for the goods, and paying it out to the seller requires both parties to sign off. The buyer’s signature is the delivery confirmation. In DAML, that policy is one line: the
`controller`
line on the
`Release`
choice.

```
template ConditionalPayment
  with
    buyer  : Party
    seller : Party
    amount : Decimal
  where
    signatory buyer
    observer seller

    choice Release : ()
      with
        paid : Decimal
      controller buyer, seller
      do
        assert (paid == amount)
```

Figure 1: A payment that requires both the buyer and the seller to approve its release

A typical happy-path test creates the payment and has both parties approve the release. The
`actAs buyer &lt;&gt; actAs seller`
line submits the command with both parties’ authority:

```
testHappyPath : Script ()
testHappyPath = script do
  buyer   &lt;- allocateParty "Buyer"
  seller  &lt;- allocateParty "Seller"
  payment &lt;- submit buyer do
    createCmd ConditionalPayment with
      buyer
      seller
      amount = 100.0
  submit (actAs buyer &lt;&gt; actAs seller) do
    exerciseCmd payment Release with paid = 100.0
  pure ()
```

Figure 2: The happy-path test. It passes, and coverage reports 100%.

The test passes, and by the usual measure the suite looks complete: running
`dpm test`
with coverage reporting enabled shows full coverage.

```
$ dpm test --show-coverage --coverage-ignore-choice Archive
testHappyPath: ok, 0 active contracts, 2 transactions.
- Internal templates:        1 defined, 1 (100.0%) created
- Internal template choices: 1 defined, 1 (100.0%) exercised
```

Figure 3: The coverage report for the happy-path test. Every template is created and every choice is exercised, for 100% coverage.

The
`--coverage-ignore-choice Archive`
flag deserves a word. Every DAML template automatically gets an implicit
`Archive`
choice. It is not part of the business logic under test, so we exclude it for simplicity. With it included, this one-choice template would report 50% even though the test exercises everything we wrote.

Run Mewt on the project and it generates seven mutants. The test suite catches three of them. Four survive. Here is one of the survivors, shown as the diff Mewt reports:

```
     choice Release : ()
       with
         paid : Decimal
-      controller buyer, seller
+      controller seller
       do
         assert (paid == amount)
```

Figure 4: The controller-removal mutant that survives the test suite

Re-run the test suite against this mutant. It still passes, and coverage still reports 100%. The contract claims releasing the buyer’s money requires both parties. The mutant lets the seller release it to themselves without the buyer ever confirming delivery. The tests report green either way. Only a test that tries the
*forbidden*
path, the seller acting alone, expecting the ledger to reject it, can tell the two contracts apart. No such test exists, and the mutation score says so. (The other three survivors tell the same story from different angles: the buyer-alone twin of this mutant, and two mutants that weaken the
`paid == amount`
check to
`&lt;=`
and
`&gt;=`
, which survive because the test only ever pays the exact amount.)

Step back, and this is the whole point of the exercise. Your tests are the executable specification of your code. Here the implementation changed, one required approval instead of two, and the specification did not react. That means the expected behavior was underspecified all along: whether both the buyer and the seller have to sign off, or just one of them, was never actually written down anywhere a machine could check. Every controller combination type-checks, and coverage reports 100% for all of them. The only place “both must sign” can exist in checkable form is a test that expects the weakened contract to fail, and writing that test is exactly what the surviving mutant tells you to do.

## Limitations and what comes next

Mewt is not magic. Two limits are worth knowing before you run your first campaign: not every survivor is a real gap, and a campaign costs time. The roadmap that follows them is where we are taking the work next.

Equivalent mutants exist: some survivors turn out to be semantically identical to the original program, so no test could ever catch them. Few public DAML codebases on GitHub come with a full test suite, so we are glad OpenZeppelin open-sourced its
`canton-stablecoin`
reference implementation. Mewt generated hundreds of mutants for it. We ran the highest-priority ones through the existing test suite, and seven of those survived. Three were equivalent mutants or sat behind a guard that no path reaches, and the other four were genuine missing test cases. None of the survivors we reviewed pointed to a bug. Such a clean result is what you want when you run Mewt on your own code, and triaging them took minutes.

One of those equivalent mutants shows what that means concretely. A helper computed accrued debt:

```
accrueDebt currentDebt lastAccrual now annualRate =
  if currentDebt == 0.0 || annualRate == 0.0 then currentDebt
  else
    let elapsedYears = ...  -- elapsed time as a fraction of a year
    in currentDebt * (1.0 + annualRate * elapsedYears)
```

Figure 5: The accrueDebt helper. Its first-line guard is a shortcut that returns the same value the calculation already produces.

Mewt forced the
`if`
to always take the
`else`
branch. No test failed, and none ever could: when the debt is zero, the formula multiplies by zero and returns zero, and when the rate is zero, it multiplies the debt by one and returns it unchanged. The guard is a shortcut that returns the value the formula already produces, so removing it changes nothing. Mewt suppresses the equivalent mutants it can detect. The rest need a reviewer’s judgment to dismiss.

Campaigns cost time in two places. The machine part: Mewt runs your test suite once per mutant, so the wall-clock cost is roughly the number of mutants times how long one test run takes, plus a rebuild if your project needs one. That is minutes on a small codebase and hours on a large one or a slow suite, so the cadence that works is nightly or weekly rather than per-commit. The human part: someone has to look at the survivors. We are working on that front from several directions at Trail of Bits, including our
[mutation-testing skill](https://github.com/trailofbits/skills/tree/main/plugins/mutation-testing)
that helps configure campaigns for your project, and
[Trailmark](https://blog.trailofbits.com/2026/04/23/trailmark-turns-code-into-graphs/)
with its
`genotoxic`
triage skill. None of these understand DAML yet, but the direction is clear: given the right harness and tools, the time-consuming parts of a campaign can be handed to AI agents. The effort is modest and the payoff is concrete: each genuine survivor is a specific test you can write, and every test you add makes your suite enforce one more guarantee your contracts are supposed to make.

Also on the roadmap: choice-consumption mutations (
`consuming`
vs
`nonconsuming`
) sit cleanly on top of the controller-mutation scaffolding and target a bug class Mewt does not yet reach.

## Dive in

Install Mewt from the
[repository](https://github.com/trailofbits/mewt)
, point a
`mewt.toml`
at your project and its test command, and
`mewt run`
. The quickstart in the README covers the rest. DAML works out of the box. Everything here ran on Daml 3.4 with
`dpm`
, but Mewt just drives whatever test command you configure, so Daml 2 projects using the
`daml`
assistant work the same way.

Mutation testing complements the rest of your security stack, the type checkers, linters, and property tests you already run, rather than replacing any of it.

If you’re building on Canton, we help teams with security reviews of DAML applications and with the way the code gets built: working directly with your engineers on the development process itself.
[Contact us](https://www.trailofbits.com/contact/)
.