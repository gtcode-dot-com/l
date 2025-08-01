---
title: "INFRA RATE LIMITER"
description: "Documentation for INFRA_RATE_LIMITER from the Foundation repository."
weight: 240
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

# Infrastructure - Rate Limiter

This document provides a detailed breakdown of how the `foundation` library integrates the `Hammer` rate limiting library. It explains the design choices, the abstraction layers, and how developers can use the feature effectively.

## Overview

The standard `Hammer` integration pattern involves installing the `Hammer` backend and making direct calls to its API for rate limiting operations. The `foundation` library abstracts this process within the **`RateLimiter`** module to provide validation, observability, and a more user-friendly configuration format.

The `foundation` library adheres to this pattern but provides a robust abstraction layer through its `Infrastructure` and `RateLimiter` modules. This abstraction offers several advantages:

- **Centralized Control:** Simplifies management of rate limiting across the application.
- **Entity-Based Limiting:** Provides independent rate limiting buckets per entity and operation.
- **Standardized Errors:** Converts `Hammer`'s responses into the `Foundation.Error` struct for consistent error handling.
- **Observability:** Automatically emits telemetry events for rate limiting decisions and exceptions.

## The Integration in Detail

### 1. Rate Limiter Architectural Context

This diagram shows how the `RateLimiter` module fits within the overall Foundation architecture. It illustrates its role as a wrapper around the `Hammer` library and its interactions with the `Infrastructure` facade, the `HammerBackend` (which uses ETS), and the `TelemetryService`.

```mermaid
graph TD
    subgraph "Client Application"
        Client["Client Code"]
    end

    subgraph "Foundation Library"
        Facade["Foundation.Infrastructure"]
        RateLimiter["Foundation.Infrastructure.RateLimiter"]
        Telemetry["Foundation.Services.TelemetryService"]
        
        subgraph "Hammer Integration"
            HammerBackend["RateLimiter.HammerBackend (use Hammer)"]
            ETS["ETS Table (Hammer State)"]
        end
    end
    
    Client -- "execute_protected(...)" --> Facade
    Facade -- "check_rate(...)" --> RateLimiter
    
    RateLimiter -- "calls" --> HammerBackend
    HammerBackend -- "reads/writes to" --> ETS
    
    RateLimiter -- "emits :request_allowed / :request_denied" --> Telemetry
    
    style Client fill:#e9ecef,stroke:#333,stroke-width:1px,color:#000
    style Facade fill:#cce5ff,stroke:#333,stroke-width:2px,color:#000
    style RateLimiter fill:#d1ecf1,stroke:#333,stroke-width:2px,color:#000
    style Telemetry fill:#f8d7da,stroke:#333,stroke-width:1px,color:#000
    style HammerBackend fill:#fff3cd,stroke:#333,stroke-width:1px,color:#000
    style ETS fill:#e2e3e5,stroke:#333,stroke-width:1px,color:#000
```

### 2. Logical Flow of `check_rate`

This flowchart details the internal decision-making process of the `RateLimiter.check_rate/5` function. It visualizes how an incoming request is processed, how the underlying `Hammer` library is invoked, and how different outcomes (allow, deny, exception) are handled and reported.

```mermaid
flowchart TD
    Start["Start check_rate(entity_id, operation, limit, window, metadata)"] --> A["build_rate_key(entity_id, operation)"]
    A --> B{Key Generation Successful?}
    B -- "No (Invalid Input)" --> B_Fail["Create :validation_failed Error"]
    B_Fail --> EndError["Return {:error, Error.t()}"]
    
    B -- "Yes" --> C["try...rescue block"]
    
    subgraph "Hammer Interaction"
        C --> D["HammerBackend.hit(key, window, limit, 1)"]
        D --> E{Result?}
        E -- "{:allow, count}" --> F["Emit :request_allowed Telemetry"]
        F --> G["Return :ok"]
        
        E -- "{:deny, _limit}" --> H["Create :rate_limit_exceeded Error"]
        H --> I["Emit :request_denied Telemetry"]
        I --> EndError
    end
    
    subgraph "Exception Handling"
        C -- "rescue exception" --> J["Create :rate_limiter_exception Error"]
        J --> K["Emit :rate_limiter_exception Telemetry"]
        K --> EndError
    end

    G --> EndSuccess["Return :ok"]

    style Start fill:#cce5ff,stroke:#333,stroke-width:2px,color:#000
    style A fill:#e2e3e5,stroke:#333,stroke-width:1px,color:#000
    style D fill:#e2e3e5,stroke:#333,stroke-width:1px,color:#000
    style B fill:#fff3cd,stroke:#333,stroke-width:1px,color:#000
    style E fill:#fff3cd,stroke:#333,stroke-width:1px,color:#000
    style F fill:#d1ecf1,stroke:#333,stroke-width:1px,color:#000
    style I fill:#d1ecf1,stroke:#333,stroke-width:1px,color:#000
    style K fill:#d1ecf1,stroke:#333,stroke-width:1px,color:#000
    style G fill:#d4edda,stroke:#333,stroke-width:1px,color:#000
    style EndSuccess fill:#d4edda,stroke:#333,stroke-width:2px,color:#000
    style H fill:#f8d7da,stroke:#333,stroke-width:1px,color:#000
    style J fill:#f8d7da,stroke:#333,stroke-width:1px,color:#000
    style B_Fail fill:#f8d7da,stroke:#333,stroke-width:1px,color:#000
    style EndError fill:#f5c6cb,stroke:#333,stroke-width:2px,color:#000
```

## End-to-End Workflow

This sequence diagram demonstrates how the rate limiter handles concurrent requests from two different entities (`user_A` and `user_B`). It clearly shows that each entity has its own independent rate-limiting bucket within the shared ETS backend, preventing one user's activity from affecting another's.

```mermaid
sequenceDiagram
    participant user_A as "Client A (user1)"
    participant user_B as "Client B (user2)"
    participant RL as "RateLimiter"
    participant HB as "HammerBackend"
    participant ETS as "ETS Table"
    
    Note over user_A, ETS: Scenario Limit: 2 requests / window
    
    user_A->>+RL: check_rate("user1", :api, 2, 60000)
    RL->>+HB: hit("...:user1:api", ...)
    HB->>+ETS: update_counter("...:user1:api")
    ETS-->>-HB: count = 1
    HB-->>-RL: {:allow, 1}
    RL-->>-user_A: :ok
    
    user_B->>+RL: check_rate("user2", :api, 2, 60000)
    RL->>+HB: hit("...:user2:api", ...)
    HB->>+ETS: update_counter("...:user2:api")
    Note right of ETS: Separate bucket for user2
    ETS-->>-HB: count = 1
    HB-->>-RL: {:allow, 1}
    RL-->>-user_B: :ok

    user_A->>+RL: check_rate("user1", :api, 2, 60000)
    RL->>+HB: hit("...:user1:api", ...)
    HB->>+ETS: update_counter("...:user1:api")
    ETS-->>-HB: count = 2
    HB-->>-RL: {:allow, 2}
    RL-->>-user_A: :ok

    user_A->>+RL: check_rate("user1", :api, 2, 60000)
    RL->>+HB: hit("...:user1:api", ...)
    HB->>+ETS: get_counter("...:user1:api")
    Note right of ETS: Limit for user1 reached (count=2)
    ETS-->>-HB: count = 2
    HB-->>-RL: {:deny, 2}
    RL-->>-user_A: {:error, Error(rate_limit_exceeded)}
    
    user_B->>+RL: check_rate("user2", :api, 2, 60000)
    RL->>+HB: hit("...:user2:api", ...)
    HB->>+ETS: update_counter("...:user2:api")
    Note right of ETS: user2 bucket is independent
    ETS-->>-HB: count = 2
    HB-->>-RL: {:allow, 2}
    RL-->>-user_B: :ok
```

## Comparison Summary

This table summarizes how `foundation` implements the standard `Hammer` patterns.

| `Hammer` Documentation Pattern | `foundation` Library Implementation |
| :------------------------------ | :---------------------------------- |
| Direct calls to `Hammer` backend functions. | Rate limiting operations are abstracted through the **`RateLimiter.check_rate/5`** function. |
| Manual error handling for rate limit violations. | Standardized error handling with **`Foundation.Error`** structs for consistent responses. |
| Manual telemetry implementation for observability. | Automatic telemetry emission for `:request_allowed`, `:request_denied`, and `:rate_limiter_exception` events. |
| Entity-specific rate key management. | Automatic rate key generation using **`build_rate_key/2`** with entity and operation context. |

By using these abstractions, `foundation` provides a more integrated, observable, and developer-friendly way to leverage the power of `Hammer`'s rate limiting capabilities.