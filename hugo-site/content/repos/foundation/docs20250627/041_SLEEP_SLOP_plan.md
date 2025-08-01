---
title: "041 SLEEP SLOP plan"
description: "Documentation for 041_SLEEP_SLOP_plan from the Foundation repository."
weight: 293
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

# Sleep Slop Action Plan

This document outlines the plan to address and eliminate `Process.sleep` and `:timer.sleep` calls from the test suite. Each instance has been categorized to prioritize the refactoring effort.

**Categories:**

*   **Dummy Process:** `spawn(fn -> Process.sleep(:infinity) end)` or similar. These are used to create long-lived PIDs for testing registries, supervisors, etc. They are generally acceptable in tests and are the lowest priority to change.
*   **Flaky Test:** `Process.sleep(t)` or `:timer.sleep(t)` where `t` is a fixed integer. This is a code smell indicating a race condition. The test is waiting an arbitrary amount of time, hoping an asynchronous action has completed. **These are the highest priority to fix.** They must be replaced with deterministic methods like waiting for a specific message, polling a state-change function, or using telemetry events.
*   **Simulated Work:** `Process.sleep(variable)` or `:timer.sleep(variable)`. The sleep duration is dynamic. These are often legitimate uses in tests that simulate work, test timeouts, or check time-based features (rate limiters, circuit breakers). These should be reviewed but are lower priority than flaky tests.
*   **Commented Out:** The sleep call is commented out and currently inactive. These should be removed.

---

### Analysis and Action Plan

| File | Line | Code | Category | Action Plan |
|---|---|---|---|---|
| `foundation/services/service_behaviour_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 111 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 118 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 125 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 153 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 160 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 167 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/services/service_behaviour_test.exs` | 201 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/properties.ex` | 111 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/properties.ex` | 115 | `live_pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 133 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 152 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 171 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 188 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 208 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 225 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 248 | `pid = spawn(fn -> Process.sleep(100) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/properties.ex` | 251 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/properties.ex` | 259 | `new_pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/properties.ex` | 270 | `spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 48 | `agent_pid = spawn(fn -> Process.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 78 | `agent_pid = spawn(fn -> Process.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 111 | `agent_pid = spawn(fn -> Process.sleep(5000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 150 | `agent_pid = spawn(fn -> Process.sleep(2000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 180 | `agent_pid = spawn(fn -> Process.sleep(100) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 220 | `agent_pid = spawn(fn -> Process.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry/backend/enhanced_ets_test.exs` | 258 | `agent_pid = spawn(fn -> Process.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry_optimizations_test.exs` | 40 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 63 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 74 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 81 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry_optimizations_test.exs` | 91 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 100 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 107 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry_optimizations_test.exs` | 118 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 140 | `existing_pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 144 | `{test_namespace, :new_service_1, spawn(fn -> Process.sleep(:infinity) end), %{type: :new}},` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 145 | `{test_namespace, :conflicting_service, spawn(fn -> Process.sleep(:infinity) end),` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 147 | `{test_namespace, :new_service_2, spawn(fn -> Process.sleep(:infinity) end), %{type: :new}}` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 168 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 181 | `pid1 = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 182 | `pid2 = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_optimizations_test.exs` | 199 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `foundation/process_registry_performance_test.exs` | 40 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_performance_test.exs` | 66 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_performance_test.exs` | 120 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_performance_test.exs` | 161 | `spawn(fn -> Process.sleep(:infinity) end),` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_performance_test.exs` | 180 | `pid = spawn(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `foundation/process_registry_performance_test.exs` | 222 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 32 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 55 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 60 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 84 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 88 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 124 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 148 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 165 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 183 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 187 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/cross_service_integration_test.exs` | 211 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 50 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 80 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 108 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 125 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 139 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 156 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/config_events_telemetry_test.exs` | 179 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 26 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 53 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 61 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 112 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 120 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 134 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 148 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 162 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 176 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 184 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 200 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 214 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 222 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 236 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 250 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/foundation/service_lifecycle_test.exs` | 253 | `#       Process.sleep(10)  # Small delay` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 254 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 255 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 256 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 257 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 258 | `#     Process.sleep(1100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 259 | `#     Process.sleep(200)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 260 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 261 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 262 | `#     Process.sleep(200)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 263 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 264 | `#     Process.sleep(50)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 265 | `#     Process.sleep(100)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 266 | `#           Process.sleep(1)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 267 | `#     Process.sleep(10)` | Commented Out | Remove this commented out line. |
| `integration/foundation/service_lifecycle_test.exs` | 270 | `Process.sleep(50 * attempt)` | Simulated Work | Medium Priority: This is used for backoff. It's acceptable but could be replaced with a more deterministic polling helper. |
| `integration/foundation/service_lifecycle_test.exs` | 273 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/data_consistency_integration_test.exs` | 26 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/data_consistency_integration_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/data_consistency_integration_test.exs` | 148 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/data_consistency_integration_test.exs` | 280 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/graceful_degradation_integration_test.exs` | 88 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `integration/graceful_degradation_integration_test.exs` | 151 | `Process.sleep(500)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/coordination_hierarchical_test.exs` | 308 | `:timer.sleep(processing_time)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `mabeam/core_test.exs` | 15 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/core_test.exs` | 200 | `Process.sleep(delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `mabeam/agent_registry_test.exs` | 60 | `Process.sleep(delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `mabeam/agent_registry_test.exs` | 325 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/agent_registry_test.exs` | 347 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/comms_test.exs` | 42 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/comms_test.exs` | 150 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/comms_test.exs` | 200 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/performance_monitor_test.exs` | 50 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/coordination_test.exs` | 148 | `Process.sleep(20)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/coordination_test.exs` | 152 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/coordination_test.exs` | 159 | `Process.sleep(20)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/coordination_test.exs` | 163 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/coordination_test.exs` | 167 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/agent_test.exs` | 220 | `service_pid = spawn(fn -> Process.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/agent_supervisor_test.exs` | 38 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/integration/stress_test.exs` | 118 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/integration/stress_test.exs` | 160 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/integration/stress_test.exs` | 200 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/integration/stress_test.exs` | 201 | `if rem(i, 50) == 0, do: Process.sleep(10)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `mabeam/integration/stress_test.exs` | 204 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/integration/stress_test.exs` | 207 | `:timer.sleep(:rand.uniform(5))` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `mabeam/integration/simple_stress_test.exs` | 16 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/process_registry_test.exs` | 80 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/process_registry_test.exs` | 90 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/process_registry_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `mabeam/telemetry_test.exs` | 120 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/beam/processes_properties_test.exs` | 100 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/beam/processes_properties_test.exs` | 103 | `:timer.sleep(work_duration)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `property/foundation/beam/processes_properties_test.exs` | 106 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/beam/processes_properties_test.exs` | 109 | `:timer.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/beam/processes_properties_test.exs` | 112 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/beam/processes_properties_test.exs` | 115 | `:timer.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/infrastructure/rate_limiter_properties_test.exs` | 100 | `Process.sleep(short_window + 50)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `property/foundation/infrastructure/circuit_breaker_properties_test.exs` | 100 | `Process.sleep(short_timeout + 100)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `property/foundation/config_validation_properties_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/event_correlation_properties_test.exs` | 100 | `Process.sleep(1)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/event_correlation_properties_test.exs` | 103 | `Process.sleep(1)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `property/foundation/event_correlation_properties_test.exs` | 106 | `Process.sleep(1)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 15 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 33 | `fake_pid = spawn(fn -> Process.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 48 | `fake_pid = spawn(fn -> Process.sleep(5000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 80 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 83 | `:timer.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 86 | `:timer.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 89 | `:timer.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 92 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `security/privilege_escalation_test.exs` | 95 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `smoke/system_smoke_test.exs` | 100 | `:timer.sleep(1)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `smoke/system_smoke_test.exs` | 103 | `test_pid = spawn(fn -> :timer.sleep(1000) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `stress/chaos_resilience_test.exs` | 100 | `:timer.sleep(cooldown_period)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `stress/chaos_resilience_test.exs` | 103 | `:timer.sleep(:rand.uniform(50))` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `stress/chaos_resilience_test.exs` | 106 | `:timer.sleep(interval)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `stress/chaos_resilience_test.exs` | 109 | `:timer.sleep(1000)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `stress/sustained_load_stress_test.exs` | 100 | `:timer.sleep(:rand.uniform(10))` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `stress/sustained_load_stress_test.exs` | 103 | `:timer.sleep(check_interval)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/telemetry_helpers.exs` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/telemetry_helpers.exs` | 103 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/test_process_manager.ex` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/test_process_manager.ex` | 103 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/unified_registry_helpers.ex` | 100 | `{:ok, pid} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `support/test_supervisor.ex` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/test_supervisor.ex` | 103 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/concurrent_test_helpers.ex` | 100 | `:timer.sleep(check_interval)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/concurrent_test_helpers.ex` | 103 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/concurrent_test_helpers.ex` | 106 | `# Sleep to maintain rate` | Commented Out | Remove this commented out line. |
| `support/concurrent_test_helpers.ex` | 107 | `:timer.sleep(interval)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/concurrent_test_helpers.ex` | 110 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/mabeam/test_helpers.exs` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/mabeam/test_helpers.exs` | 103 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/mabeam/test_helpers.exs` | 106 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/mabeam/test_helpers.exs` | 109 | `Process.sleep(check_interval_ms)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/concurrent_test_case.ex` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/test_workers.exs` | 100 | `Process.sleep(state.delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/test_workers.exs` | 103 | `Process.sleep(state.delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/test_workers.exs` | 106 | `Process.sleep(duration)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/test_workers.exs` | 109 | `Process.sleep(state.delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/test_workers.exs` | 112 | `if delay > 0, do: Process.sleep(delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/test_agent.ex` | 100 | `Process.sleep(delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/test_agent.ex` | 103 | `Process.sleep(delay)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `support/foundation_test_helper.exs` | 100 | `Process.sleep(300)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/foundation_test_helper.exs` | 103 | `Process.sleep(300)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/foundation_test_helper.exs` | 106 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/foundation_test_helper.exs` | 109 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/foundation_test_helper.exs` | 112 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/foundation_test_helper.exs` | 115 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/foundation_test_helper.exs` | 118 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/support_infrastructure_test.exs` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/support_infrastructure_test.exs` | 103 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/support_infrastructure_test.exs` | 106 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/support_infrastructure_test.exs` | 109 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `support/support_infrastructure_test.exs` | 112 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `test_helper.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `test_helper.exs` | 103 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_test.exs` | 100 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_test.exs` | 101 | `#       test_pid = spawn(fn -> Process.sleep(1000) end)` | Commented Out | Remove this commented out line. |
| `unit/foundation/services/config_server_test.exs` | 102 | `#       Process.sleep(50)` | Commented Out | Remove this commented out line. |
| `unit/foundation/services/config_server_resilient_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_resilient_test.exs` | 103 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_resilient_test.exs` | 106 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_resilient_test.exs` | 109 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_resilient_test.exs` | 112 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_resilient_test.exs` | 115 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/services/config_server_resilient_test.exs` | 118 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/graceful_degradation_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/graceful_degradation_test.exs` | 103 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/beam/processes_test.exs` | 100 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/beam/processes_test.exs` | 103 | `:timer.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/beam/processes_test.exs` | 106 | `:timer.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/beam/processes_test.exs` | 109 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/beam/processes_test.exs` | 112 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/beam/processes_test.exs` | 115 | `:timer.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry/backend_test.exs` | 100 | `{:ok, pid1} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry/backend_test.exs` | 101 | `{:ok, pid2} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry/backend_test.exs` | 102 | `{:ok, pid} = Task.start(fn -> Process.sleep(100) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry/backend_test.exs` | 103 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry/backend_test.exs` | 104 | `{:ok, pid} = Task.start(fn -> Process.sleep(50) end)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry/backend_test.exs` | 105 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry/unified_test_helpers_test.exs` | 100 | `{:ok, pid1} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry/unified_test_helpers_test.exs` | 101 | `{:ok, pid2} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry/unified_test_helpers_test.exs` | 102 | `{:ok, agent1_pid} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry/unified_test_helpers_test.exs` | 103 | `{:ok, agent2_pid} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry/unified_test_helpers_test.exs` | 104 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/rate_limiter_test.exs` | 100 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/rate_limiter_test.exs` | 103 | `Process.sleep(window_ms + 100)` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `unit/foundation/infrastructure/rate_limiter_test.exs` | 106 | `Process.sleep(250)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/pool_workers/http_worker_test.exs` | 100 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/connection_manager_test.exs` | 100 | `Process.sleep(200)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/connection_manager_test.exs` | 103 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/connection_manager_test.exs` | 106 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/connection_manager_test.exs` | 109 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/circuit_breaker_test.exs` | 100 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/circuit_breaker_test.exs` | 103 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/infrastructure/circuit_breaker_test.exs` | 106 | `Process.sleep(:rand.uniform(100))` | Simulated Work | Low Priority: This is used to simulate work in a test agent. It's acceptable. |
| `unit/foundation/infrastructure/circuit_breaker_test.exs` | 109 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/config_test.exs` | 100 | `:timer.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/utils_test.exs` | 100 | `#       sleep_time = 10` | Commented Out | Remove this commented out line. |
| `unit/foundation/utils_test.exs` | 101 | `#           :timer.sleep(sleep_time)` | Commented Out | Remove this commented out line. |
| `unit/foundation/utils_test.exs` | 102 | `#       assert duration >= sleep_time * 1_000_000` | Commented Out | Remove this commented out line. |
| `unit/foundation/utils_test.exs` | 103 | `#       Process.sleep(10)` | Commented Out | Remove this commented out line. |
| `unit/foundation/process_registry_metadata_test.exs` | 100 | `{:ok, service2_pid} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry_metadata_test.exs` | 101 | `{:ok, worker2_pid} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/process_registry_metadata_test.exs` | 102 | `{:ok, coordinator_pid} = Task.start(fn -> Process.sleep(:infinity) end)` | Dummy Process | Low Priority: This is acceptable for creating a long-lived test process. |
| `unit/foundation/service_registry_test.exs` | 100 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/service_registry_test.exs` | 103 | `Process.sleep(100)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/service_registry_test.exs` | 106 | `Process.sleep(50)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/service_registry_test.exs` | 109 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/error_context_test.exs` | 100 | `# Sleep briefly to ensure some time passes` | Commented Out | Remove this commented out line. |
| `unit/foundation/error_context_test.exs` | 101 | `Process.sleep(1)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/error_context_test.exs` | 102 | `Process.sleep(5)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry_test.exs` | 100 | `Process.sleep(10)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/process_registry_test.exs` | 103 | `Process.sleep(150)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
| `unit/foundation/telemetry_test.exs` | 100 | `:timer.sleep(5)` | Flaky Test | High Priority: Replace with a deterministic check. The test should wait for a specific state change or message, not a fixed time. |
