---
title: "09 all 5of5 dev exp op tooling"
description: "Documentation for 09_all_5of5_dev_exp_op_tooling from the Dspex repository."
weight: 282
lastmod: "2025-07-24"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

Of course. Here are the detailed technical specifications for the fifth and final essential component layer: the **Developer Experience & Operational Tooling Layer**.

This document provides the complete design for the components that make the `dspex` platform usable, inspectable, and trustworthy. While the other layers provide the raw power, this layer provides the crucial interfaces, debugging tools, and configuration management that enable scientists and developers to harness that power effectively.

---

### **`12_SPEC_DEV_EXPERIENCE_AND_TOOLING.md`**

# Technical Specification: The Developer Experience & Operational Tooling Layer

## 1. Vision and Guiding Principles

This layer transforms `dspex` from a powerful engine into a complete, usable platform. It is guided by the principle that the value of a complex system is only unlocked through tools that make it transparent, debuggable, and easy to manage.

*   **Introspection is Paramount:** A developer must be able to ask "Why did my program produce this result?" and receive a clear, comprehensive answer. Black boxes are not acceptable.
*   **Trust Through Persistence:** Scientific work requires a permanent record. All experimental results must be durably stored and easily queryable, creating an immutable audit trail of discovery.
*   **Ergonomics for Scientists:** The primary interfaces for debugging and inspection should be in the environments where scientists work, with a strong emphasis on interactive, visual tools like Elixir's Livebook.
*   **Simplicity in Configuration:** The complexity of the platform should be managed through a single, well-documented configuration entry point, not scattered across multiple modules.

## 2. Core Components

This layer consists of three primary components that provide the user-facing tooling and configuration for the entire platform:

1.  **`DSPex.ResultStore`**: A durable, queryable persistence layer for all experimental results.
2.  **`DSPex.TraceViewer`**: An interactive tool for inspecting and debugging the full, end-to-end execution of any trial.
3.  **Centralized Configuration**: A unified approach to configuring the platform via `config/config.exs`.

---

## 3. `DSPex.ResultStore`: The Persistent Scientific Record

The `ResultStore` is a stateful service responsible for the long-term, durable storage of all artifacts generated by the `ExperimentJournal`.

### 3.1. Purpose

*   To provide a single, canonical source of truth for all experimental outcomes.
*   To ensure that the results of scientific work are not lost if the application restarts.
*   To enable querying and analysis of past experiments.
*   To decouple the active, in-memory state of an `ExperimentJournal` from the permanent archival of its results.

### 3.2. Architecture: A Pluggable Backend System

The `ResultStore` will be a `GenServer` that fronts a pluggable storage backend, allowing users to choose the right persistence strategy for their needs.

```elixir
defmodule DSPex.ResultStore do
  @behaviour DSPex.ResultStore.Backend

  # API for the backend
  def init(config)
  def archive_experiment(backend_state, experiment)
  def get_experiment(backend_state, experiment_id)
  def query_experiments(backend_state, filters)
end
```

**Supported Backends:**

1.  **`:ets` (Default, In-Memory):**
    *   **Implementation:** A simple ETS-backed `GenServer`.
    *   **Use Case:** Default for quick tests, examples, and environments where persistence is not required. State is lost on application shutdown.
2.  **`:file` (File-Based):**
    *   **Implementation:** Serializes `Experiment` structs to the filesystem (e.g., using `:erlang.term_to_binary/1`) in a structured directory layout. It will use a DETS table for indexing.
    *   **Use Case:** Suitable for single-node deployments and local development where persistence across restarts is needed without the overhead of a full database.
3.  **`:ecto` (Database):**
    *   **Implementation:** An Ecto-based backend that stores results in a SQL database (PostgreSQL, SQLite).
    *   **Use Case:** The production-grade solution for multi-node deployments, providing robust querying, transactional integrity, and scalability.

### 3.3. Public API (`@spec`)

```elixir
@doc "Starts the ResultStore GenServer with a configured backend."
@spec start_link(opts :: keyword()) :: GenServer.on_start()
def start_link(opts \\ [])

@doc "Archives a completed experiment struct. Called by the ExperimentJournal."
@spec archive_experiment(pid(), DSPex.Evaluation.Experiment.t()) :: :ok | {:error, term()}
def archive_experiment(store_pid, experiment)

@doc "Retrieves a fully detailed experiment record by its ID."
@spec get_experiment(pid(), String.t()) :: {:ok, DSPex.Evaluation.Experiment.t()} | {:error, :not_found}
def get_experiment(store_pid, experiment_id)

@doc """
Queries for experiments based on a set of filters.

Filters can include: by hypothesis, by program name, by date range, etc.
"""
@spec query_experiments(pid(), map()) :: {:ok, list(DSPex.Evaluation.Experiment.t())}
def query_experiments(store_pid, filters \\ %{})
```

---

## 4. `DSPex.TraceViewer`: The Debugging Power-Tool

This is a stateless module that provides functions to load and visualize the results of an experiment, with a primary focus on interactive inspection in Livebook.

### 4.1. Purpose

*   To provide deep insight into the end-to-end execution of a `dspex` program.
*   To solve the critical **cross-language debugging problem** by presenting a unified, interleaved view of Elixir orchestration and Python execution.
*   To be the primary tool for understanding *why* a program produced a certain result or failed.

### 4.2. Architecture: Livebook-First Integration

The `TraceViewer` will be designed to produce rich, interactive `Kino` outputs for an unparalleled debugging experience.

### 4.3. Public API (`@spec`)

```elixir
@doc "Renders a full, interactive view of a completed experiment."
@spec view_experiment(String.t()) :: Kino.Live.t()
def view_experiment(experiment_id)

@doc "Renders a detailed, unified trace for a single trial within an experiment."
@spec view_trial(String.t(), String.t()) :: Kino.Live.t()
def view_trial(experiment_id, trial_id)
```

### 4.4. The Unified Trace Visualization

This is the core innovation of the `TraceViewer`. The `view_trial/2` function will query the `ResultStore`, fetch the raw `TrialResult`, and render an interleaved timeline of events.

**Example `Kino` Output for a `SIMBA-C` Trial:**

```elixir
# In a Livebook cell:
# DSPex.TraceViewer.view_trial("exp_simba_run_123", "trial_87")

# --- Renders the following interactive output ---

# # Unified Trace: Trial 87 (Score: 0.85)

# ### Elixir Orchestration (SIMBA-C)
# * **Timestamp:** `2025-07-22T10:30:01.123Z`
# * **Decision:** Propose new candidate from source program `candidate_42`.
# * **Strategy:** `append_a_rule`
# * **Rationale:** Analyzing high-variance bucket for example `data_point_55`.
# * **Action:** Executing `OfferFeedback` LLM call to generate a new instruction.

# ### Python Execution (gRPC Bridge)
# * **Timestamp:** `2025-07-22T10:30:01.345Z`
# * **Worker:** `snakepit_worker_3`
# * **Program:** `dspy.Predict` (for the OfferFeedback call)
# * **Synchronized Variables:**
#   * `temperature`: 1.0 (from CognitiveConfiguration)

# --- LLM Trace (dspy.Predict) ---
# **Prompt:**
# > You will be given two trajectories...
# > ...
# > worse_program_trajectory: ...
# > better_program_trajectory: ...

# **Response:**
# > module_advice: {"my_rag_pipeline": "When the question is ambiguous,
# > ensure the generated search query is broader to capture more context."}
# --- End LLM Trace ---

# ### Elixir Orchestration (SIMBA-C)
# * **Timestamp:** `2025-07-22T10:30:02.567Z`
# * **Action:** Creating new program configuration `candidate_87`.
# * **Change:** Appending the new rule to the `instructions` variable.

# ### Python Execution (gRPC Bridge) - Evaluation of new candidate
# * **Timestamp:** `2025-07-22T10:30:02.789Z`
# * **Worker:** `snakepit_worker_5`
# * **Program:** `my_rag_pipeline` (Class: `dspy.ChainOfThought`)
# * **Synchronized Variables:**
#   * `instructions`: "Answer questions... **[NEW RULE APPENDED]**"
#   * `demos`: `[%DSPex.Example{...}, ...]`

# --- LLM Trace (dspy.ChainOfThought) ---
# **Prompt:**
# > Given the context, answer the question. Let's think step by step.
# > ...

# **Response:**
# > reasoning: "The new rule suggests a broader query..."
# > answer: "The final answer is..."
# --- End LLM Trace ---

# ### Elixir Orchestration (EvaluationHarness)
# * **Timestamp:** `2025-07-22T10:30:03.999Z`
# * **Metric:** `accuracy`
# * **Result:** `1.0` (Correct)
# * **Final Score:** `0.85`
```

This unified view provides an unprecedented level of observability, directly connecting high-level optimization decisions in Elixir to their low-level execution effects in Python.

---

## 5. Centralized Configuration

This provides a single source of truth for configuring the entire `dspex` platform, making it manageable and transparent.

### 5.1. Purpose

*   To provide a single, well-documented location for all platform-wide settings.
*   To allow users to easily switch between different environments (dev, test, prod).
*   To configure the pluggable backends and other operational parameters.

### 5.2. Location and Structure (`config/config.exs`)

```elixir
# In config/config.exs or config/dev.exs, etc.
import Config

# Main configuration for the DSPex platform
config :dspex,
  # Configure the default state backend for new Contexts.
  # Can be overridden at Context.start_link/1.
  default_state_backend: DSPex.Bridge.State.Local,

  # Configuration for the Scientific Evaluation Framework
  evaluation: [
    # The default pool of harness workers for parallel execution
    harness_pool_size: System.schedulers_online(),

    # The default storage backend for the ResultStore
    result_store_backend: :ets # Other options: :file, :ecto
  ],

  # Path for the ResultStore file backend
  result_store_file_path: "/var/data/dspex_results"


# Configuration for the Snakepit bridge
config :snakepit,
  # Enable the pool of Python workers
  pooling_enabled: true,

  # The adapter that defines how to communicate with Python
  adapter_module: Snakepit.Adapters.GRPCPython,

  # Configuration for the worker pool
  pool_config: [
    pool_size: System.schedulers_online(),
    # Timeouts in milliseconds
    pool_startup_timeout: 15_000,
    worker_init_timeout: 10_000,
    worker_shutdown_grace_period: 2_000
  ],
  
  # gRPC-specific configuration
  grpc_config: [
    base_port: 50051,
    port_range: 100,
    bridge_module: "snakepit_bridge.adapters.dspy_grpc.DSPyGRPCHandler"
  ],

  # Path to the Python executable
  python_path: System.get_env("PYTHON_EXECUTABLE", "python3")
```

## 6. Conclusion

The Developer Experience & Operational Tooling Layer is what makes `dspex` a complete and practical platform. While other layers provide the power, this layer provides the usability, trust, and insight.

*   The **`ResultStore`** ensures that scientific work is never lost.
*   The **`TraceViewer`** provides the critical debugging and introspection capabilities needed to understand complex, cross-language AI systems.
*   The **Centralized Configuration** makes the entire system manageable and easy to deploy.

By implementing these components, we provide developers and scientists with not just an engine, but a complete, well-equipped laboratory for building and understanding the next generation of AI.
