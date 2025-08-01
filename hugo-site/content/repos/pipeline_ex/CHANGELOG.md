---
title: "CHANGELOG"
description: "Documentation for CHANGELOG from the Pipeline ex repository."
weight: 6
lastmod: "2025-07-19"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Async Streaming Support**: Real-time message streaming for all Claude-based steps
  - Message-by-message streaming displays complete messages as they arrive from ClaudeCodeSDK
  - 6 specialized stream handlers: console, simple, debug, file, buffer, and callback
  - Works with all Claude step types (claude, claude_smart, claude_session, etc.)
  - Progressive display of assistant responses, tool uses, and results
  - Memory-efficient processing without buffering entire responses
  - Full mock support for testing without API calls
  - Documentation: ASYNC_STREAMING_MIGRATION_GUIDE.md and examples/STREAMING_GUIDE.md

## [0.0.1] - 2025-01-05

**Maintainer**: NSHkr <ZeroTrust@NSHkr.com>

### Added
- Initial release of Pipeline.ex - AI pipeline orchestration library for Elixir
- Core pipeline execution engine with robust error handling and retries
- Support for Claude (Anthropic) and Gemini (Google) AI providers
- YAML v2 pipeline format with comprehensive features:
  - Multi-step pipelines with conditional execution
  - Advanced prompt templating with variables and transformations
  - Control flow (conditionals, loops, parallel execution)
  - Pipeline composition and inheritance
  - Function calling support for both providers
- Genesis/Meta pipeline system for self-improving pipelines:
  - Pipeline DNA evolution and mutation
  - Fitness evaluation framework
  - Recursive pipeline generation
- Comprehensive testing framework with mocking support
- Extensive documentation including:
  - Complete YAML format v2 reference
  - Architecture documentation
  - Usage guides and patterns
  - Pipeline specifications for various use cases
- Visual pipeline editor specifications (implementation planned)
- Safety features and context management
- Performance optimization with caching and parallel execution

### Features
- **Pipeline Execution**: Robust execution engine with retry logic and error handling
- **Provider Support**: Claude (via Anthropic API) and Gemini (via Google API) integration
- **YAML Configuration**: Declarative pipeline definitions with v2 format
- **Prompt System**: Advanced templating with variables, transformations, and inheritance
- **Control Flow**: Conditionals, loops, parallel execution, and error handling
- **Genesis System**: Self-improving pipelines with evolution capabilities
- **Testing Support**: Built-in test mode with comprehensive mocking
- **Documentation**: Extensive guides, references, and examples

### Known Limitations
- Visual editor GUI not yet implemented (specifications only)
- Limited to Claude and Gemini providers in this release
- Some advanced meta-pipeline features are experimental

[0.0.1]: https://github.com/nshkrdotcom/pipeline_ex/releases/tag/v0.0.1