---
date: '2025-11-12'
description: The unified observability layer for the AI Control Plane, delivering
  full-fidelity tracing for AI agent reasoning, tool calls, and state transitions.
docs_url: https://hexdocs.pm/aitrace/
hex_url: https://hex.pm/packages/aitrace
highlights:
- 'Latest release: v0.1.0'
- 'Recent downloads: 1198'
- 'All-time downloads: 1198'
- 'Maintainers: nshkrdotcom'
repo_url: https://github.com/nshkrdotcom/AITrace
slug: aitrace
stage: Active
tags:
- MIT
- Hex.pm
title: Aitrace
version: 0.1.0
installation:
  - method: "Mix.exs"
    command: |
      def deps do
        [
          {:aitrace, "~> 0.1.0"}
        ]
      end
    note: "Then run `mix deps.get`"
  - method: "Hex"
    command: "mix hex.package fetch aitrace"
usage: |
  ```elixir
  # Basic usage example for AITrace
  alias AITrace.Core

  # Start tracing an AI agent interaction
  {:ok, trace_id} = AITrace.start_trace(%{
    agent_id: "agent-001",
    session_id: "session-123"
  })

  # Record tool calls and reasoning steps
  AITrace.log_event(trace_id, %{
    type: :tool_call,
    tool: "web_search",
    input: "latest AI research"
  })

  # Complete the trace
  AITrace.end_trace(trace_id)
  ```
releases:
  - version: "0.1.0"
    date: "2025-11-12"
    notes: "Initial release - Full-fidelity tracing for AI agent reasoning"
---

## About Aitrace

The unified observability layer for the AI Control Plane, delivering full-fidelity tracing for AI agent reasoning, tool calls, and state transitions.

## Package Information

- Latest release: v0.1.0
- Recent downloads: 1198
- All-time downloads: 1198
- Maintainers: nshkrdotcom

## Installation

Add `aitrace` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {'aitrace', "~> 0.1.0"}\n  ]
end
```

Then run:

```bash
mix deps.get
```

## Documentation

Full documentation is available at [https://hexdocs.pm/aitrace/](https://hexdocs.pm/aitrace/).

## Source Code

The source code is available on GitHub: [https://github.com/nshkrdotcom/AITrace](https://github.com/nshkrdotcom/AITrace).

