---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-12T08:04:13.373293+00:00'
exported_at: '2025-12-12T08:04:15.695042+00:00'
feed: https://research.facebook.com/feed
language: en
source_url: https://engineering.fb.com/2023/04/06/open-source/buck2-open-source-large-scale-build-system
structured_data:
  about: []
  author: ''
  description: Buck2, our extensible, performant, open source build system is designed
    to make your build experience better.
  headline: 'Build faster with Buck2: Our open source build system'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://engineering.fb.com/2023/04/06/open-source/buck2-open-source-large-scale-build-system
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Build faster with Buck2: Our open source build system'
updated_at: '2025-12-12T08:04:13.373293+00:00'
url_hash: b3c33e72f8f752e3a82db78b85c010917c4dd3af
---

* Buck2, our
  [new open source, large-scale build system](https://github.com/facebook/buck2)

  , is now available on GitHub.
* Buck2 is an extensible and performant build system written in Rust and designed to make your build experience faster and more efficient.
* In our internal tests at Meta, we observed that Buck2 completed builds 2x as fast as Buck1.

Buck2, Meta’s open source large-scale build system, is now publicly available via the
[Buck2 website](https://buck2.build/)

and
[the Buck2
GitHub repository](https://github.com/facebook/buck2)

. While it shares some commonalities with other build systems (like
[Buck1](https://engineering.fb.com/2017/11/09/android/rethinking-android-app-compilation-with-buck/)
and
[Bazel](https://engineering.fb.com/2017/06/05/web/dev-tools-scale-2017-recap/)
), Buck2 is a from-scratch rewrite. Buck2 features a complete separation of the core and language-specific rules, with increased parallelism, integration with remote execution and virtual file systems, and a redesigned console output. All of these changes are aimed at helping engineers and developers spend less time waiting, and more time iterating on their code.

Thousands of developers at Meta are already using Buck2 and performing millions of builds per day, with builds completing twice as fast as with Buck1. Our own internal analysis has shown that engineers were able to produce meaningfully more code when their builds were executed by Buck2, and we hope the wider industry will also see benefits.

## Why rebuild Buck?

Build systems stand between a programmer and running their code, so anything we can do to make the experience quicker or more productive directly impacts how effective a developer can be. The goal of Buck2 was to keep what we liked about Buck1 (the core concepts and workflows), draw inspiration from innovations after Buck1 (including
[Bazel](https://bazel.build/)

,
[Adapton](http://adapton.org/)

, and
[Shake](https://shakebuild.com/)

), and focus on speed and enabling new experiences.

Buck2’s design is based on the following principles:

* **The core build system has no knowledge of any language-specific rules.**

  Having the rules separated from the core means that the rules are easier to change and understand. The core of Buck2 is written in Rust, and its language rules (like how to build C++) are written in
  [Starlark](https://github.com/facebookexperimental/starlark-rust)

  . This separation is in contrast to Buck1 (where all rules are written in the core) and Bazel (where C++/Java are written in the core).
* **The build system is powered by a**
  [**single incremental dependency graph**](https://ndmitchell.com/#build_01_jan_2022)

  , avoiding any phases (in contrast to Buck1 or Bazel). This decision eliminates many types of bugs and increases parallelism.
* **The rules API is designed to contain advanced features for performance**

  , along with dynamic (or monadic) dependency features for expressibility. At the same time, these features are carefully restricted to ensure other properties (for example, fast queries or hermeticity) are not harmed.
* **The open source release is almost identical to our internal version**

  . The only pieces swapped out are the toolchains (which point at the internal copies of our compilers) and remote execution (which points at our internal servers)

  —

  both have open source alternatives supplied. We are also releasing all the rules exactly as they are used internally. Furthermore, we have separated some of the logical components into separate crates (e.g.
  [Starlark](https://developers.facebook.com/blog/post/2021/04/08/rust-starlark-library/)

  ,
  [Superconsole](https://developers.facebook.com/blog/post/2022/07/21/superconsole/)

  ,
  [Allocative](https://github.com/facebookexperimental/allocative)

  ,
  [Gazebo](https://developers.facebook.com/blog/post/2021/06/29/rust-nibbles-gazebo-prelude/)

  ) so that they can be used outside Buck2.
* **Buck2 is written to integrate with remote execution**

  , with the ability to run actions on remote machines. We use the same
  [API as Bazel](https://bazel.build/remote/rbe)

  , and have been testing remote execution with
  [Buildbarn](https://github.com/buildbarn)

  and
  [EngFlow](https://www.engflow.com/)

  . While not required (and not really expected for people starting out with the open source version), we are able to efficiently compute recursive digests and send them to remote execution efficiently.
* **Buck2 is written to integrate with virtual file systems**

  , where the entire repository is not all checked out, but fetched on demand as the files are accessed. In particular, we support
  [Sapling-based file systems](https://github.com/facebook/sapling/blob/main/eden/fs/docs/Overview.md)

  . To integrate well, we watch for file notifications (with
  [Watchman](https://facebook.github.io/watchman/)

  ) and request both files and file-digests without direct file operations. The benefit is that we can make virtual file systems as fast as a full checkout, but with the benefits of much faster checkout and much lower disk usage.

The key takeaway from all these improvements is that we have designed Buck2 to be fast. In real world usage, depending on the build, Buck2 is significantly faster than Buck1. If there are no source code changes, Buck2 is almost instant on subsequent builds. If there is a lot of work to do, Buck2 starts executing faster and has greater parallelism. This increase in speed is both a consequence of many of the factors above, but also care and attention.

## The user view

For end users, Buck2 works mostly the same as Buck1 (which, to a first approximation, is fairly similar to Bazel). A user defines targets in a

BUCK

file:

```
rust_binary(
    name = “my_binary”,
    srcs = [“main.rs”],
    deps = [“:my_library”],
)
```

A user can then build with

buck2 build
//:my\_binary

. The value

main.rs

is a source file, and

:my\_library

is a dependency defined in the same

BUCK

file. It’s worth noting that Buck2 is mostly compatible with the

BUCK

files of Buck1.

As well as the increase in speed, there are two major additional user-visible differences compared to Buck1.

First, the console output has been redesigned on top of the
[Superconsole library](https://developers.facebook.com/blog/post/2022/07/21/superconsole/)

, which we specifically developed for Buck2. The console shows a few more details and feels a lot nicer to use:

![](https://engineering.fb.com/wp-content/uploads/2023/03/Buck2-animated-gif.gif)

Second, there is a persistent daemon that maintains a single dependency graph. When you change a

BUCK

file, a dependency, or a source file, we invalidate the appropriate things on the dependency graph, then request the output artifacts per the command line. In Buck1 there are multiple distinct dependency graphs, which result in phases like target graph construction, action graph construction, and then action graph execution. There are also some operations that aren’t performed on the graph. If certain things change in Buck1, then entire graphs are thrown away, rather than the minimum pieces being invalidated. With a single dependency graph, Buck2 is simpler, avoids more redundant work, and avoids explicit phases. Everything on the dependency graph has a key (how it is identified) and a value, along with a function to compute the value from the key and other related keys (following the model in the paper, “
[Build Systems a la Carte”](https://ndmitchell.com/#shake_21_apr_2020)

).

## The rule author view

While the user model follows Buck1 very closely, the approach for rules is completely different. There are lots of rules in Buck, for example

rust\_binary

used above. While a rule in Buck1 was a Java class, baked into Buck1, a rule in Buck2 is entirely decoupled. Buck2 also ships with a “prelude” of rules that implement most of the Buck1 rules.

Buck1 rules were tuned over time, had lots of performance optimizations and powerful features like graph traversal, but those rules were also expected to obey a lot of complex invariants

—

sometimes breaking those rules. For Buck2, the rule API is entirely in Starlark, which forced us to abstract those features as generically reusable APIs, aiming to make them safe, expressive, and performant

—

a tricky balance. We’ll touch on two such examples.

### OCaml dependencies

The dependency structure of the OCaml library is hard to express in Buck1. An OCaml library consists of a number of OCaml files. These must be compiled in dependency order

—

so if

A.ml

uses

B.ml

, you must compile

B.ml

first. Bazel requires the dependency of

A.ml

on

B.ml

to be written explicitly in the

BUCK

file.
![](https://engineering.fb.com/wp-content/uploads/2023/04/Buck2_image1a.png?w=182)
Buck1 and Buck2 both leave that internal dependency implicit and run the tool

ocamldep

to infer it, which requires less maintenance as the structure changes.  What Buck1 did is run

ocamldep

just after parsing the

BUCK

file, which wasn’t really allowed, and it didn’t track dependencies, so if you changed the imports too much Buck1 gave spurious compilation failures. With Buck2, we can use the
[new primitive

dynamic\_output](https://buck2.build/docs/rule_authors/dynamic_dependencies/)

, which lets you run a command, read the output of the file, then wire up the rest of the graph

—

putting in the correct dependencies between the

.ml

files automatically.

### C++ link dependencies

Consider the C++ linking model:

To produce a library, you usually need to link together its build output, along with the transitive closure of the build output of its dependencies. If you simply duplicate the set of dependencies at each layer as you move up the graph, you end up with
*O(n*
*2*
*)*

memory usage. In Buck1, there was custom code in many rules to capture this pattern, relying on the ability to share Java values in memory and for the dependencies to be represented in place within the rule structure (as there was no reified dependency graph). In Buck2, there are much stronger abstraction boundaries, so such reuse has to be made more explicit. Therefore, we
[introduced transitive-sets (tsets)](https://buck2.build/docs/rule_authors/transitive_sets/)

to capture this pattern of sets representing a transitive closure. By making tsets more abstract, we were also able to wire the tset directly into the underlying dependency graph, meaning this representation is efficient in both memory and computation time.

## Try Buck2 now

We’re keen for people to give Buck2 a try, and we would be happy to hear any feedback (
[GitHub issues](https://github.com/facebookincubator/buck2/issues)

are the best way). We expect Buck2 will be most interesting to moderately sized multi-language projects. Visit the
[Buck2 getting started page](https://buck2.build/docs/getting_started/)

for more information.