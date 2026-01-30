---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-30T12:15:15.629812+00:00'
exported_at: '2026-01-30T12:15:18.383805+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/01/30/celebrating-our-2025-open-source-contributions
structured_data:
  about: []
  author: ''
  description: "\n                Trail of Bits engineers contributed over 375 merged
    pull requests to more than 90 open-source projects in 2025, including significant
    work on Sigstore rekor-monitor, the Rust compiler and Clippy, pyca/cryptography's
    ASN.1 API, hevm performance optimizations, PyPI Warehouse, and pwndbg.\n            "
  headline: Celebrating our 2025 open-source contributions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/01/30/celebrating-our-2025-open-source-contributions
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Celebrating our 2025 open-source contributions
updated_at: '2026-01-30T12:15:15.629812+00:00'
url_hash: 35f94f1b20004c14d33833ed7ffceca17d89e63e
---

Last year, our engineers submitted over
**375 pull requests**
that were merged into non–Trail of Bits repositories, touching more than
**90 projects**
from cryptography libraries to the Rust compiler.

This work reflects one of our driving values: “share what others can use.” The measure isn’t whether you share something, but whether it’s actually useful to someone else. This principle is why we publish
[handbooks](https://github.com/trailofbits/publications?tab=readme-ov-file#guides-and-handbooks)
, write blog posts, and release tools like
[Claude skills](https://github.com/trailofbits/skills)
,
[Slither](https://github.com/crytic/slither)
,
[Buttercup](https://github.com/trailofbits/buttercup)
, and
[Anamorpher](https://github.com/trailofbits/anamorpher)
.

But this value isn’t limited to our own projects; we also share our efforts with the wider open-source community. When we hit limitations in tools we depend on, we fix them upstream. When we find ways to make the software ecosystem more secure, we contribute those improvements.

Most of these contributions came out of client work—we hit a bug we were able to fix or wanted a feature that didn’t exist. The lazy option would have been forking these projects for our needs or patching them locally. Contributing upstream instead takes longer, but it means the next person doesn’t have to solve the same problem. Some of our work is also funded directly by organizations like the OpenSSF and Alpha-Omega, who we collaborate with to make things better for everyone.

## Key contributions

* [**Sigstore rekor-monitor**](https://github.com/sigstore/rekor-monitor)
  : rekor-monitor verifies and monitors the Rekor transparency log, which records signing events for software artifacts. With funding from OpenSSF, we’ve been
  [getting rekor-monitor ready for production use](https://blog.trailofbits.com/2025/12/12/catching-malicious-package-releases-using-a-transparency-log/)
  . We contributed over 40 pull requests to the Rekor project this year, including
  [support for custom certificate authorities](https://github.com/sigstore/rekor-monitor/pull/764)
  and
  [support for the new Rekor v2](https://github.com/sigstore/rekor-monitor/pull/705)
  . We also
  [added identity monitoring](https://github.com/sigstore/rekor-monitor/pull/751)
  for
  [Rekor v2](https://github.com/sigstore/rekor-tiles)
  , which lets package maintainers configure monitored certificate subjects and issuers and then receive alerts whenever matching entries appear in the log. If someone compromises your release process and signs a malicious package with your identity, you’ll know.
* [**Rust compiler**](https://github.com/rust-lang/rust)
  **and
  [rust-clippy](https://github.com/rust-lang/rust-clippy)**
  : Clippy is Rust’s official linting tool, offering over 750 lints to catch common mistakes. We contributed over 20 merged pull requests this year. For example, we
  [extended the
  `implicit_clone`
  lint to handle
  `to_string()`
  calls](https://github.com/rust-lang/rust-clippy/pull/14177)
  , which let us deprecate the redundant
  `string_to_string`
  lint. We
  [added replacement suggestions to
  `disallowed_methods`](https://github.com/rust-lang/rust-clippy/pull/13669)
  so that teams can suggest alternatives when flagging forbidden API usage, and we
  [added path validation for
  `disallowed_*`
  configurations](https://github.com/rust-lang/rust-clippy/pull/14397)
  so that typos don’t silently disable lint rules. We also
  [extended the
  `QueryStability`
  lint to handle
  `IntoIterator`
  implementations](https://github.com/rust-lang/rust/pull/139345)
  in rustc, which catches nondeterminism bugs in the compiler. The motivation came from a real issue we spotted: iteration order over hash maps was leaking into rustdoc’s JSON output.
* [**pyca/cryptography**](https://github.com/pyca/cryptography)
  : pyca/cryptography is Python’s most widely used cryptography library, providing both high-level recipes and low-level interfaces to common algorithms. With funding from Alpha-Omega, we landed 28 pull requests this year. Our work was aimed at adding
  [a new ASN.1 API](https://github.com/pyca/cryptography/pull/13325)
  , which lets developers define ASN.1 structures using Python decorators and type annotations instead of wrestling with raw bytes or external schema files. Read more in our blog post “
  [Sneak peek: A new ASN.1 API for Python](https://blog.trailofbits.com/2025/04/18/sneak-peek-a-new-asn.1-api-for-python/)
  .”
* [**hevm**](https://github.com/ethereum/hevm)
  : hevm is a Haskell implementation of the Ethereum Virtual Machine. It powers both the symbolic and concrete execution in Echidna, our smart contract fuzzer. We contributed 14 pull requests this year, mostly focused on performance: we
  [added cost centers to individual opcodes to ease profiling, optimized memory operations, and made stack and program counter operations strict](https://github.com/ethereum/hevm/pull/803)
  , which got us double-digit percentage improvements on concrete execution benchmarks. We also implemented cheatcodes like
  [`toString`](https://github.com/ethereum/hevm/pull/838)
  to improve hevm’s compatibility with Foundry.
* [**PyPI Warehouse**](https://github.com/pypi/warehouse)
  : Warehouse powers the Python Package Index (PyPI), which serves over a billion package downloads per day. We continued our long-running collaboration with PyPI and Alpha-Omega, shipping
  [project archival support](https://blog.trailofbits.com/2025/01/30/pypi-now-supports-archiving-projects/)
  so that maintainers can signal when packages are no longer actively maintained. We also
  [cut the test suite runtime by 81%](https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/)
  , from 163 to 30 seconds, even as test coverage grew to over 4,700 tests.
* [**pwndbg**](https://github.com/pwndbg/pwndbg)
  : pwndbg is a GDB and LLDB plugin that makes debugging and exploit development less painful. Last year, we
  [packaged LLDB support for distributions](https://github.com/pwndbg/pwndbg/pull/3195)
  and
  [improved decompiler integration](https://github.com/pwndbg/pwndbg/pull/3548)
  . We also contributed pull requests to other tools in the space, including pwntools, angr, and Binary Ninja’s API.

A merged pull request is the easy part. The hard part is everything maintainers do before and after: writing extensive documentation, keeping CI green, fielding bug reports, explaining the same thing to the fifth person who asks. We get to submit a fix and move on. They’re still there a year later, making sure it all holds together.

Thanks to everyone who shaped these contributions with us, from first draft to merge. See you next year.

## Trail of Bits’ 2025 open-source contributions

### AI/ML

* Repo: majiayu000/litellm-rs
* Repo: mlflow/mlflow
* Repo: simonw/llm
* Repo: sst/opencode

### Cryptography

* Repo: C2SP/x509-limbo
* Repo: certbot/josepy
* Repo: pyca/cryptography
* Repo: tamarin-prover/tamarin-prover

### Languages and compilers

* Repo: airbus-cert/tree-sitter-powershell
* Repo: cdisselkoen/llvm-ir
* Repo: hyperledger-solang/solang
* Repo: llvm/clangir
* Repo: rust-lang/rust

### Libraries

* Repo: alex/rust-asn1
* Repo: bytecodealliance/wasi-rs
* Repo: cargo-public-api/cargo-public-api
* Repo: di/id
* Repo: di/pip-api
* Repo: fardream/go-bcs
* Repo: frewsxcv/rust-crates-index
* Repo: luser/strip-ansi-escapes
* Repo: psf/cachecontrol
* Repo: tafia/quick-xml

### Tech infrastructure

* Repo: Homebrew/homebrew-core
* Repo: NixOS/nixpkgs
* Repo: google/oss-fuzz
* Repo: microsoft/vcpkg
* Repo: microsoft/vcpkg-tool

* Repo: AFLplusplus/AFLplusplus
* Repo: advanced-security/monorepo-code-scanning-action
* Repo: github/codeql
* Repo: oli-obk/ui\_test
* Repo: pypa/abi3audit
* Repo: rust-fuzz/cargo-fuzz
* Repo: rust-lang/cargo
* Repo: rust-lang/rust-clippy
* Repo: rust-lang/rustup
* Repo: zizmorcore/zizmor

### Blockchain software

* Repo: anza-xyz/agave
* Repo: argotorg/hevm
* Repo: hellwolf/solc.nix
* Repo: rappie/fuzzer-gas-metric-benchmark

* Repo: Gallopsled/pwntools
* Repo: Vector35/binaryninja-api
* Repo: angr/angr
* Repo: angr/angrop
* Repo: frida/frida-gum
* Repo: jonpalmisc/screenshot\_ninja
* Repo: pwndbg/pwndbg
* Repo: quarkslab/quokka

* Repo: pygments/pygments
* Repo: quarkslab/bgraph

### Packaging ecosystem/supply chain

* Repo: Homebrew/.github
* Repo: Homebrew/actions
* Repo: Homebrew/brew
* Repo: Homebrew/brew-pip-audit
* Repo: Homebrew/brew.sh
* Repo: Homebrew/homebrew-cask
* Repo: Homebrew/homebrew-command-not-found
* Repo: PyO3/maturin
* Repo: conda/schemas
* Repo: ossf/wg-securing-software-repos
* Repo: pypa/gh-action-pip-audit
* Repo: pypa/gh-action-pypi-publish
* Repo: pypa/packaging.python.org
* Repo: pypa/pip-audit
* Repo: pypa/twine
* Repo: pypi/pypi-attestations
* Repo: pypi/warehouse
* Repo: python/peps
* Repo: sigstore/architecture-docs
* Repo: sigstore/community
* Repo: sigstore/cosign
* Repo: sigstore/fulcio
* Repo: sigstore/gh-action-sigstore-python
* Repo: sigstore/protobuf-specs
* Repo: sigstore/rekor
* Repo: sigstore/rekor-monitor
* Repo: sigstore/rekor-tiles
* Repo: sigstore/sigstore
* Repo: sigstore/sigstore-conformance
* Repo: sigstore/sigstore-go
* Repo: sigstore/sigstore-python
* Repo: sigstore/sigstore-rekor-types
* Repo: synacktiv/DepFuzzer
* Repo: wolfv/ceps

### Others

* Repo: AzureAD/microsoft-authentication-extensions-for-python
* Repo: SchemaStore/schemastore
* Repo: google/gvisor
* Repo: oli-obk/cargo\_metadata
* Repo: ossf/alpha-omega
* Repo: rustsec/advisory-db