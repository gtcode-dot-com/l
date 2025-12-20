---
title: "Geometric Publish-Subscribe: Content-Based Routing in Embedding Space for Multi-Agent Systems"
description: "A research proposal for GPS, a communication protocol for multi-agent systems where messages route by semantic similarity rather than topic strings."
date: 2025-12-20
draft: false
author: "GTCode.com Member of Technical Staff"
tags:
  - multi-agent systems
  - publish-subscribe
  - embeddings
  - vector quantization
  - semantic routing
categories:
  - research
  - protocols
math: true
toc: true
meta_description: "Geometric Publish-Subscribe (GPS) protocol specification for content-based routing in embedding space, enabling semantic message routing for multi-agent systems without joint training."
meta_keywords:
  - geometric publish-subscribe
  - GPS protocol
  - multi-agent communication
  - semantic routing
  - vector quantization
  - embedding space
  - content-based routing
  - relevance profiles
sitemap:
  changefreq: monthly
  priority: 0.8
structured_data_webpage:
  type: ScholarlyArticle
  headline: "Geometric Publish-Subscribe: Content-Based Routing in Embedding Space"
  about:
    - multi-agent systems
    - semantic communication
    - publish-subscribe protocols
---

**A Research Proposal**

---

## Abstract

We propose *Geometric Publish-Subscribe* (GPS), a communication protocol for multi-agent systems where messages route by semantic similarity rather than topic strings. Unlike traditional pub/sub (subscribe to "topic_name") or existing semantic routers (embed query → select handler), GPS treats the message payload itself as a quantized embedding and routes to recipients whose *relevance profiles* fall within geometric proximity. The protocol specifies a 64-byte wire format, subscription semantics based on embedding regions, and routing algorithms based on similarity thresholds. To our knowledge, this specific integration—quantized semantic payloads, relevance-profile subscription, and content-based geometric routing—has not been formalized as a general-purpose protocol. This paper specifies the protocol, distinguishes it from prior work, and defines an empirical evaluation comparing GPS against topic-based pub/sub and HTTP+JSON coordination.

---

## 1. Introduction

### 1.1 The Routing Problem in Multi-Agent Systems

Consider $n$ agents that must coordinate. Each agent produces messages and consumes messages relevant to its function. The routing problem: how does message $m$ from agent $A$ reach the appropriate subset of agents $\{B_1, \ldots, B_k\}$?

**Solution 1: Topic-based pub/sub**
```
Agent A publishes to topic "price_updates"
Agents B₁...Bₖ subscribe to "price_updates"
```
Limitation: Topics are discrete strings. If agent $B_j$ cares about "price changes" but subscribed to "market_data", it misses relevant messages. Topic taxonomies require explicit design and maintenance.

**Solution 2: Broadcast + filter**
```
Agent A broadcasts to all agents
Each agent filters locally by relevance
```
Limitation: $O(n)$ message delivery per broadcast. Does not scale.

**Solution 3: Semantic routing (existing)**
```
Human query → embed → compare to route definitions → select handler
```
Limitation: One-way (human → system). Routes queries to handlers, not agents to agents. Handler set is static.

### 1.2 Proposed Solution: Geometric Publish-Subscribe

GPS inverts the semantic routing pattern:

```
Agent A: encode(message) → 64-byte GPS packet with quantized payload q
Router:  for each agent Bⱼ with relevance profile hⱼ:
           if sim(q, hⱼ) > θⱼ: deliver(m, Bⱼ)
```

Key differences from prior work:

| Property | Topic Pub/Sub | Semantic Router | TarMAC | **GPS** |
|----------|---------------|-----------------|--------|---------|
| Subscription unit | String | Route definition | Learned weights | Embedding region |
| Routing decision | String match | Query→handler | Attention (trained) | Geometric similarity |
| Participants | Any | Human→agent | Homogeneous agents | Heterogeneous agents |
| Training required | No | No | Yes (joint) | No (shared codebook) |

The core contribution: **recipients declare regions of semantic space, not topic names**. Messages route by geometric proximity in embedding space.

### 1.3 Scope and Claims

**What we claim:**
- A novel *protocol-level* specification for content-based routing via vector quantization and geometric similarity
- A compact wire format (64 bytes) that preserves semantic content
- Empirical comparison against baselines on latency, bandwidth, and routing quality

**What we do not claim:**
- Invention of semantic communication (Foerster et al., 2016)
- Invention of attention-based message routing (Das et al., 2019)
- Invention of vector quantization (van den Oord et al., 2017)
- Invention of semantic routing for query classification (Aurelio AI, 2024)

### 1.4 Assumptions

| ID | Assumption | Tested in |
|----|------------|-----------|
| A1 | Agents use embeddings from compatible model families | Section 6, Task C |
| A2 | Coordination messages are semantically compressible to 48 bytes | Section 6, RQ2 |
| A3 | Codebook can be pre-trained on representative coordination messages | Section 5.3 |
| A4 | Relevance profiles approximate agent utility functions | Section 6, Task B |

Claims in subsequent sections hold under these assumptions. The evaluation tests A1, A2, and A4 empirically.

---

## 2. Related Work

### 2.1 Emergent Communication in Multi-Agent RL

Foerster et al. (2016) introduced DIAL and RIAL, demonstrating that RL agents learn compressed communication protocols when optimizing shared objectives. Subsequent work refined this:

**CommNet** (Sukhbaatar et al., 2016): Continuous vector communication via mean-pooling. All agents receive averaged messages—no selective routing.

**TarMAC** (Das et al., 2019): Attention-gated targeted messaging. Agents learn to weight messages by relevance. Key limitation: attention weights are learned jointly during training. Agents must share training context.

**LSC** (Sheng et al., 2020): Hierarchical communication topologies learned via neural importance weights. Reduces complexity from $O(n^2)$ to $O(k^2 + kb)$.

**Gap**: These methods require joint training. Heterogeneous agents (different architectures, different training histories) cannot communicate without retraining.

### 2.2 Semantic Routing for LLM Applications

The `semantic-router` library (Aurelio AI, 2024) and similar tools route user queries to appropriate handlers:

```python
Route(name="billing", utterances=["payment issue", "refund request", ...])
Route(name="technical", utterances=["bug report", "error message", ...])

router.route("I need a refund")  # → "billing"
```

**Gap**: This is query classification, not agent-to-agent communication. The route set is static and human-defined. Agents cannot dynamically declare relevance.

### 2.3 Vector Quantization

VQ-VAE (van den Oord et al., 2017) demonstrated that learned codebooks preserve semantic structure while enabling discrete representation. Product quantization (Jégou et al., 2011) achieves further compression by decomposing vectors into subspaces.

**Gap**: VQ is used for compression and retrieval, not as a wire format for inter-agent communication.

### 2.4 Content-Based Publish-Subscribe

Content-based pub/sub systems (Carzaniga et al., 2001) route messages by predicates over message attributes rather than topic strings:

```
subscription: price > 100 AND sector = "tech"
```

**Gap**: Predicates operate on structured fields, not semantic content. A message about "semiconductor shortage impacts" would not match a subscription for "tech sector news" without explicit field mapping.

### 2.5 Summary: The Integration Gap

| Capability | MARL Comm | Semantic Router | VQ | Content Pub/Sub | **GPS** |
|------------|-----------|-----------------|-----|-----------------|---------|
| Agent-to-agent | ✓ | ✗ | ✗ | ✓ | ✓ |
| No joint training | ✗ | ✓ | ✓ | ✓ | ✓ |
| Semantic-native | ✓ | ✓ | ✓ | ✗ | ✓ |
| Dynamic subscription | ✗ | ✗ | N/A | ✓ | ✓ |
| Compressed wire format | ✓ | ✗ | ✓ | ✗ | ✓ |

GPS combines: (1) semantic-native communication from MARL, (2) no-training-required interoperability from semantic routing, (3) compressed format from VQ, (4) dynamic subscription from content-based pub/sub.

---

## 3. Protocol Specification

### 3.1 System Model

A GPS network consists of three logical components:

**Agents**: Processes that send and receive messages. Each agent has a unique identifier and maintains a relevance profile.

**Hubs**: Routing processes that maintain relevance profiles for connected agents and perform similarity-based message routing. A hub may serve one agent (embedded mode) or many agents (centralized mode).

**Codebook**: A shared quantization dictionary mapping high-dimensional embeddings to discrete codes. All agents and hubs in a GPS network must share a compatible codebook.

The protocol is agnostic to the underlying runtime. Implementations may use actors, threads, coroutines, or processes. The specification defines message formats and routing semantics, not execution models.

### 3.2 Message Format

A GPS message $m$ is a 64-byte packet:

$$m = (\tau, \mathbf{q}, \mathbf{r}, \sigma)$$

| Field | Bytes | Description |
|-------|-------|-------------|
| Header $\tau$ | 1 | Type (3b), Priority (3b), Flags (2b) |
| Payload $\mathbf{q}$ | 48 | Quantized semantic content |
| Routing $\mathbf{r}$ | 14 | Source ID (8), Timestamp (4), TTL (2) |
| Checksum $\sigma$ | 1 | CRC-8 |

**Total: 64 bytes** (fits in single cache line on modern architectures)

### 3.3 Payload Encoding

The 48-byte payload is produced by product quantization:

$$\mathbf{q} = \text{PQ}(\mathbf{z}) = \bigoplus_{i=1}^{M} \text{VQ}_i(\mathbf{z}^{(i)})$$

where:
- $\mathbf{z} \in \mathbb{R}^d$ is the source embedding (from any embedding model)
- $\mathbf{z}$ is partitioned into $M$ subvectors $\mathbf{z}^{(i)} \in \mathbb{R}^{d/M}$
- Each subvector is quantized against codebook $C_i$ with $K$ centroids
- $\bigoplus$ denotes concatenation

**Default parameters**: $M = 6$ subquantizers, $K = 256$ centroids per subquantizer (1 byte per code), yielding 6 bytes of codes plus 42 bytes for centroid indices or auxiliary data.

With these parameters, the payload encodes $256^6 \approx 2.8 \times 10^{14}$ distinct semantic points.

**Encoding procedure**:
```
function ENCODE(text, codebook):
    z = embedding_model.embed(text)      // d-dimensional vector
    z_normalized = z / ||z||              // Unit normalize
    q = []
    for i in 1..M:
        subvector = z_normalized[(i-1)*d/M : i*d/M]
        code = argmin_k ||subvector - codebook[i][k]||
        q.append(code)
    return q
```

**Decoding procedure**:
```
function DECODE(q, codebook):
    z_reconstructed = []
    for i in 1..M:
        centroid = codebook[i][q[i]]
        z_reconstructed.append(centroid)
    return concatenate(z_reconstructed)
```

### 3.4 Relevance Profiles

Each agent $j$ maintains a relevance profile $(\mathbf{h}_j, \theta_j)$ where:
- $\mathbf{h}_j \in \mathbb{R}^{d}$ is an embedding representing "what this agent cares about"
- $\theta_j \in [0, 1]$ is the similarity threshold for message delivery

Profiles can be constructed via:

**Static specification**: Embed a description of the agent's role (e.g., "financial analysis and market data")

**Exemplar averaging**: Average embeddings of example messages the agent should receive

**Adaptive learning**: Exponential moving average of messages the agent found useful:
$$\mathbf{h}_j^{(t+1)} = \alpha \cdot \mathbf{h}_j^{(t)} + (1-\alpha) \cdot \mathbf{z}_{\text{received}}$$

### 3.5 Routing Algorithm

When a hub receives message $m$ with payload $\mathbf{q}$:

```
function ROUTE(m, agents):
    z = DECODE(m.payload)
    for agent in agents:
        score = similarity(z, agent.profile)
        if score > agent.threshold:
            DELIVER(m, agent)
            // Optional: adaptive threshold
            agent.threshold = β * agent.threshold + (1-β) * score
```

**Similarity functions** (implementation choice):

Cosine similarity (default):
$$\text{sim}(\mathbf{z}, \mathbf{h}) = \frac{\langle \mathbf{z}, \mathbf{h} \rangle}{\|\mathbf{z}\| \|\mathbf{h}\|}$$

Asymmetric distance (avoids full decode):
$$\text{asym}(\mathbf{q}, \mathbf{h}) = \sum_{i=1}^{M} \|C_i[\mathbf{q}_i] - \mathbf{h}^{(i)}\|_2^2$$

**Complexity**: For $n$ agents with $d$-dimensional profiles, routing is $O(nd)$. With $d = 48$ and optimized SIMD, a single core routes to ~1M agents in ~10ms.

For larger networks, approximate nearest neighbor (ANN) indexing reduces complexity to $O(\log n)$ or $O(1)$ with locality-sensitive hashing.

### 3.6 Codebook Management

Agents must share a compatible codebook to communicate. The protocol defines:

**Codebook fingerprint**: SHA-256 hash of serialized centroids, truncated to 8 bytes.

**Version negotiation**:
1. Agent sends META message with its codebook fingerprint
2. Hub responds with its fingerprint
3. If fingerprints match: proceed
4. If fingerprints differ: hub may provide translation layer or request codebook sync

**Codebook versioning**: MAJOR.MINOR.PATCH
- PATCH: Centroid drift correction (backward compatible)
- MINOR: New centroids added (backward compatible)
- MAJOR: Dimension change or codebook restructure (breaking)

### 3.7 Message Types

| Type | ID | Semantic Role | Use Case |
|------|-----|---------------|----------|
| PERCEPT | 0 | Observation | "API returned 503 error" |
| INTENT | 1 | Goal/request | "Need additional compute resources" |
| BELIEF | 2 | Knowledge assertion | "User prefers formal tone" |
| AFFECT | 3 | State/status | "Operating at high load" |
| COORD | 4 | Coordination primitive | "Acquiring lock on resource X" |
| META | 5 | Protocol control | "Request codebook synchronization" |

Types enable filtering at the wire level before semantic comparison.

---

## 4. Formal Properties

### 4.1 Semantic Fidelity

**Definition 4.1** (Quantization Distortion). For embedding $\mathbf{z}$ and its reconstruction $\hat{\mathbf{z}} = \text{Decode}(\text{PQ}(\mathbf{z}))$:

$$D(\mathbf{z}) = 1 - \frac{\langle \mathbf{z}, \hat{\mathbf{z}} \rangle}{\|\mathbf{z}\| \|\hat{\mathbf{z}}\|}$$

**Definition 4.2** (Semantic Fidelity). For embedding pairs $(\mathbf{z}_1, \mathbf{z}_2)$ and their quantizations $(\mathbf{q}_1, \mathbf{q}_2)$:

$$\phi = \mathbb{E}\left[\frac{\text{sim}(\hat{\mathbf{z}}_1, \hat{\mathbf{z}}_2)}{\text{sim}(\mathbf{z}_1, \mathbf{z}_2) + \epsilon}\right]$$

where $\epsilon = 10^{-6}$ prevents division instability.

Semantic fidelity measures whether quantization preserves *relative* similarity structure—if two messages were similar before quantization, are they still similar after?

**Hypothesis 4.1**: With $M = 6$, $K = 256$, semantic fidelity $\phi > 0.95$ for embeddings from the same model family. *Tested in Section 6, RQ2.*

### 4.2 Bandwidth Efficiency

**Proposition 4.1** (Compression Ratio). For coordination messages with typical JSON payload of $\sim$4KB:

$$\text{Compression ratio} = \frac{|m_{\text{JSON}}|}{|m_{\text{GPS}}|} = \frac{4096}{64} = 64\times$$

This is the raw size ratio. Effective utility depends on whether the 64-byte payload preserves sufficient semantic content for the coordination task (tested in RQ2).

**Proposition 4.2** (Bandwidth Bound). A GPS network with $n$ agents, average message rate $\lambda$ per agent, and average fanout $k$ (recipients per message) consumes:

$$B = n \lambda k \cdot 64 \text{ bytes/second}$$

For $n = 1000$, $\lambda = 10$ msg/s, $k = 5$: $B = 3.2$ MB/s.

### 4.3 Routing Correctness

**Definition 4.3** (Routing Precision/Recall). Given ground-truth relevant set $R^*$ (agents that "should" receive message $m$) and delivered set $R$:

$$\text{Precision} = \frac{|R \cap R^*|}{|R|}, \quad \text{Recall} = \frac{|R \cap R^*|}{|R^*|}$$

**Property 4.1** (Threshold-Precision Tradeoff). For threshold $\theta$:
- Higher $\theta$ → higher precision, lower recall
- Lower $\theta$ → lower precision, higher recall

The adaptive threshold mechanism (Section 3.5) targets operating points based on agent feedback.

**Property 4.2** (Semantic Monotonicity). If $\text{sim}(\mathbf{z}_1, \mathbf{h}) > \text{sim}(\mathbf{z}_2, \mathbf{h})$, then with high probability:
$$\text{sim}(\hat{\mathbf{z}}_1, \mathbf{h}) > \text{sim}(\hat{\mathbf{z}}_2, \mathbf{h})$$

This follows from semantic fidelity (Definition 4.2) and ensures that quantization preserves routing decisions.

---

## 5. Research Questions

**RQ1** (Efficiency): Does GPS achieve lower latency and bandwidth than JSON-over-HTTP for equivalent coordination tasks?

**RQ2** (Fidelity): What semantic fidelity ($\phi$) is achievable with 48-byte payloads across embedding model families (OpenAI, Cohere, open-source)?

**RQ3** (Routing Quality): How does GPS routing precision/recall compare to topic-based pub/sub with manually designed topic taxonomies?

**RQ4** (Heterogeneity): Can agents using different embedding models coordinate via shared codebook without joint training?

**RQ5** (Scalability): How does routing latency scale with agent count under different indexing strategies (linear scan, LSH, HNSW)?

---

## 6. Evaluation Plan

### 6.1 Baselines

| System | Description |
|--------|-------------|
| **HTTP+JSON** | REST API coordination; each message serialized as JSON |
| **Redis Pub/Sub** | Topic-based publish-subscribe via Redis channels |
| **gRPC+Protobuf** | Protocol buffers over gRPC with typed schemas |
| **NATS** | High-performance topic-based messaging |

### 6.2 Benchmark Tasks

**Task A: Information Dissemination**
- Source agent broadcasts messages with varying semantic content
- Recipient agents have defined relevance profiles
- Metric: Delivery latency, bandwidth consumed
- Tests: RQ1, RQ5

**Task B: Semantic Filtering**
- 100 agents with distinct relevance profiles
- Source broadcasts mixed messages (some relevant to each subset)
- Ground truth: human-labeled relevance judgments
- Metric: Precision, recall, F1 vs. topic-based baseline
- Tests: RQ3

**Task C: Cross-Model Coordination**
- Agent group 1: OpenAI embeddings
- Agent group 2: Cohere embeddings
- Agent group 3: open-source (e5-large)
- Must coordinate on shared task via unified codebook
- Metric: Task success rate, semantic fidelity across model boundaries
- Tests: RQ4

**Task D: Fidelity Measurement**
- Corpus of 10,000 message pairs with known similarity scores
- Quantize and measure similarity preservation
- Metric: Semantic fidelity $\phi$, distortion distribution
- Tests: RQ2

### 6.3 Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Latency $T_{99}$ | 99th percentile encode-route-deliver time | < 1ms (single node) |
| Bandwidth $B$ | Bytes per coordination round | < 100 bytes |
| Fidelity $\phi$ | Similarity preservation ratio | > 0.95 |
| Precision $P$ | Relevant deliveries / total deliveries | > 0.90 |
| Recall $R$ | Relevant deliveries / relevant messages | > 0.85 |

### 6.4 Experimental Phases

| Phase | Duration | Focus |
|-------|----------|-------|
| 1: Microbenchmarks | Week 1-2 | Encode/decode latency, similarity computation throughput |
| 2: Single-node | Week 3-4 | 10-1000 agents, Tasks A, B, D |
| 3: Cross-model | Week 5-6 | Task C, codebook translation overhead |
| 4: Scale | Week 7-8 | 10K+ agents, ANN indexing comparison |

---

## 7. Implementation Notes

### 7.1 Reference Implementation

We will provide an open-source reference implementation. The protocol is runtime-agnostic; the reference implementation demonstrates correctness and provides baseline performance numbers.

Implementation requirements for any GPS-compliant system:
- Codebook storage with $O(1)$ centroid lookup
- Concurrent profile updates (relevance profiles may change during routing)
- Atomic message delivery (message delivered to all matching agents or none)

### 7.2 Codebook Construction

To address Assumption A3 (codebook requires representative data):

**Bootstrap from pretrained embeddings**: Initialize centroids via k-means on embeddings from a large text corpus (e.g., 1M sentences from Common Crawl, embedded with target model).

**Domain adaptation**: Fine-tune centroids on domain-specific coordination messages if available.

**Online refinement**: Update centroids via exponential moving average as messages flow through production system.

**Cold-start fallback**: For immediate deployment without representative data, use dimensionality reduction (PCA to 48 dimensions) with degraded fidelity.

### 7.3 Optimizations

**SIMD similarity**: 48-dimensional dot products vectorize efficiently on AVX-512 (single instruction for 16 floats).

**Batch routing**: Collect messages over short window (e.g., 100μs), compute all similarities in single matrix operation.

**Profile indexing**: For $n > 10,000$ agents, build HNSW or IVF index over profiles. Routing becomes approximate nearest neighbor search.

**Asymmetric distance**: Compute similarity directly from quantized codes without full decode, using precomputed centroid-to-profile distances.

---

## 8. Expected Contributions

1. **GPS Protocol Specification**: Formal definition of geometric publish-subscribe with 64-byte wire format, relevance-profile subscription, and similarity-based routing.

2. **Reference Implementation**: Open-source library implementing GPS (language TBD based on target community).

3. **Empirical Evaluation**: Quantitative comparison against topic-based pub/sub and HTTP+JSON on latency, bandwidth, and routing quality.

4. **Cross-Model Interoperability Analysis**: Study of semantic fidelity when agents use different embedding models with shared codebook.

### 8.1 Limitations and Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Quantization loss exceeds 5% | Medium | High | Parameter sweep on $M$, $K$; fallback to larger payloads |
| Routing overhead dominates at small $n$ | High | Medium | Document crossover point; recommend broadcast for $n < 50$ |
| Codebook drift across model versions | Medium | High | Versioning protocol; translation layers |
| Adoption limited by codebook bootstrapping cost | Medium | Medium | Provide pretrained codebooks for common embedding models |

### 8.2 Non-Goals

This work does not address:
- **Security**: Message authentication, encryption, access control (orthogonal to routing)
- **Ordering guarantees**: Causal ordering, total ordering (can layer on top of GPS)
- **Persistence**: Message durability, replay (implementation concern)
- **Discovery**: How agents find hubs (standard service discovery applies)

---

## 9. Ethical Considerations

GPS enables efficient coordination among AI agents. Potential concerns:

**Coordinated manipulation**: Efficient agent coordination could enable large-scale automated influence operations. Mitigation: GPS is a communication primitive, not an autonomy framework; deployment contexts should include appropriate oversight.

**Reduced interpretability**: Semantic routing is less transparent than topic-based routing ("why did agent X receive this message?"). Mitigation: Logging similarity scores and profile matches enables post-hoc analysis.

**Codebook control**: Whoever controls the codebook controls communication compatibility. Mitigation: Publish codebook construction methodology; support federated codebook governance.

---

## 10. Conclusion

Geometric Publish-Subscribe addresses a specific gap in multi-agent communication: how to route messages by semantic content without requiring joint training or manual topic taxonomies.

The protocol combines established techniques:

| Component | Source |
|-----------|--------|
| Vector quantization | van den Oord et al., 2017; Jégou et al., 2011 |
| Attention-based routing concepts | Das et al., 2019 |
| Content-based pub/sub | Carzaniga et al., 2001 |

The synthesis—**subscription by embedding region, message as quantized vector, routing by geometric similarity**—has not been formalized as a general-purpose, runtime-agnostic protocol.

We propose to specify the protocol formally, implement it, evaluate it against standard baselines, and release it as open infrastructure for multi-agent systems.

---

## References

Aurelio AI. (2024). Semantic Router. https://github.com/aurelio-labs/semantic-router

Carzaniga, A., Rosenblum, D. S., & Wolf, A. L. (2001). Design and evaluation of a wide-area event notification service. *ACM Transactions on Computer Systems*, 19(3), 332-383.

Das, A., Gerber, T., Ghosh, D., Hoffman, M., Kakade, S., & Levine, S. (2019). TarMAC: Targeted multi-agent communication. *Proceedings of the 36th International Conference on Machine Learning*.

Foerster, J., Assael, Y., de Freitas, N., & Whiteson, S. (2016). Learning to communicate with deep multi-agent reinforcement learning. *Advances in Neural Information Processing Systems*.

Jégou, H., Douze, M., & Schmid, C. (2011). Product quantization for nearest neighbor search. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 33(1), 117-128.

Sheng, J., Wang, X., Jin, B., & Zhu, J. (2020). Learning structured communication for multi-agent reinforcement learning. *arXiv preprint arXiv:2002.04235*.

Sukhbaatar, S., Szlam, A., & Fergus, R. (2016). Learning multiagent communication with backpropagation. *Advances in Neural Information Processing Systems*.

van den Oord, A., Vinyals, O., & Kavukcuoglu, K. (2017). Neural discrete representation learning. *Advances in Neural Information Processing Systems*.

---

## Appendix A: Wire Format Detail

```
GPS Message (64 bytes)
┌────────────────────────────────────────────────────────────┐
│ Byte 0       │ Type (3b) │ Priority (3b) │ Flags (2b)      │
├────────────────────────────────────────────────────────────┤
│ Bytes 1-48   │ Quantized Payload                           │
│              │ (M subquantizer codes + auxiliary data)     │
├────────────────────────────────────────────────────────────┤
│ Bytes 49-56  │ Source ID (64-bit agent identifier)         │
├────────────────────────────────────────────────────────────┤
│ Bytes 57-60  │ Timestamp (32-bit Unix epoch, seconds)      │
├────────────────────────────────────────────────────────────┤
│ Bytes 61-62  │ TTL (16-bit hop count)                      │
├────────────────────────────────────────────────────────────┤
│ Byte 63      │ CRC-8 checksum                              │
└────────────────────────────────────────────────────────────┘
```

## Appendix B: Codebook File Format

```
GPS Codebook v1
┌────────────────────────────────────────────────────────────┐
│ Header (32 bytes)                                          │
│ ├─ Magic: "GPSCB001" (8 bytes)                             │
│ ├─ Version: MAJOR.MINOR.PATCH (3 bytes)                    │
│ ├─ M: Number of subquantizers (1 byte)                     │
│ ├─ K: Centroids per subquantizer (2 bytes)                 │
│ ├─ D: Total embedding dimension (2 bytes)                  │
│ ├─ Fingerprint: SHA-256 truncated (8 bytes)                │
│ └─ Reserved (8 bytes)                                      │
├────────────────────────────────────────────────────────────┤
│ Centroids (M × K × (D/M) × 4 bytes, float32)               │
└────────────────────────────────────────────────────────────┘
```

## Appendix C: Example Scenarios

**Scenario 1: Financial Analysis Coordination**

Agent A (data collector) observes: "NVDA stock dropped 5% after earnings miss"
- Encodes observation → PERCEPT message
- Payload captures semantic content about: stock, price movement, earnings

Agent B (risk analyst) has profile: "portfolio risk, market volatility, position exposure"
- Profile similarity to message: 0.72
- Threshold: 0.65 → Message delivered

Agent C (NLP summarizer) has profile: "text summarization, document processing"
- Profile similarity to message: 0.31
- Threshold: 0.60 → Message not delivered

**Scenario 2: Adaptive Threshold**

Agent B initially receives many messages (threshold 0.65).
After processing 100 messages, average similarity of received messages: 0.78.
Adaptive threshold rises to 0.73, filtering to higher-relevance content.
Agent B can manually reset threshold if missing important messages.
