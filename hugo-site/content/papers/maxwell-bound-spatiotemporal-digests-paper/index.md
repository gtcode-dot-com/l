---
title: "Physics-Informed Spatiotemporal Digests: WSTD, OMR-Gated RF Verification, and Residual Security under Learned-Model Attackers"
description: "A research design note proposing Physics-Informed Spatiotemporal Digests, combining a windowed state-and-transition digest with optional OMR-gated RF verification."
date: 2026-04-01
draft: false
author: "GTCode.com Member of the Technical Staff"
tags:
  - media provenance
  - spatiotemporal digests
  - RF verification
  - C2PA
  - security research
categories:
  - research
  - security
math: true
toc: true
---

# Physics-Informed Spatiotemporal Digests: WSTD, OMR-Gated RF Verification, and Residual Security under Learned-Model Attackers

## Abstract

This paper proposes **Physics-Informed Spatiotemporal Digests (PISD)**, a software-only provenance mechanism for media captured on commodity phones. PISD is intentionally split into two contributions with different maturity levels.

The first contribution is a **windowed state-and-transition digest (WSTD)**: a deterministic, fail-open evidence object that compresses a capture interval into ordered per-window state sketches, cross-channel residual sketches, transition sketches, and a chained commitment bound to the media content hash. WSTD is useful **even without any physics oracle**, because it directly targets replay, stitching, and window reordering attacks that a monolithic digest cannot represent.

The second contribution is an **optional receiver-conditioned RF physics oracle** that upgrades registry-based verification into physics-aware verification. Instead of asking only whether Wi-Fi, cellular, and GNSS observations are consistent with public registries or world models, the oracle asks whether the reported **API-visible** RF observations are plausible under a distribution induced by device family, latent pose, location, time, and environment priors. The oracle is presented explicitly as a **research program**, not a finished deployment claim.

The paper formalizes an **observability margin ratio (OMR)** and a **metric-robust OMR bootstrap protocol** for deciding when a physics term should be deployed at all. It incorporates a **staleness-aware, mask-aware registry baseline** that treats incomplete RF maps as uncertainty rather than contradiction. It addresses the **defender–attacker symmetry** directly: if learned physics models become available to both sides, PISD becomes a time-buying mechanism rather than a permanent solution. To quantify that residual value, the paper introduces the notion of **coherence burden**, the negative log success probability of an adaptive generator under the verifier's joint acceptance constraints. It specifies a concrete **C2PA privacy and versioning model** in which the public manifest carries commitments and receipts while the sensitive evidence payload is encrypted, externally stored, and access-controlled.

The paper's central claim is deliberately narrow and defensible: **WSTD is a deployable contribution now; physics-oracle verification should be enabled only where OMR supports it; and software-only provenance must eventually converge with trusted hardware once learned physical-model symmetry collapses the remaining margin.**

---

## 1. Introduction

A recurring question in media provenance is narrow but operationally important:

> *Was this asset plausibly captured at the claimed place and time under real physical conditions?*

On commodity phones, software alone cannot answer that question with cryptographic certainty. There is no trusted path from sensor to verifier, radio observability is coarse, external world models are incomplete, and API-visible readings are several abstraction layers above the underlying physics. The honest output of such a system is therefore **not** a binary “real/fake” oracle. It is an evidence object plus a calibrated probability or confidence score.

A baseline near-term design already exists in the form of a **spatiotemporal digest SDK**: capture a time-ordered sequence of sensor samples during media creation, canonicalize them, hash them, bind them to the content hash, and verify them against public or quasi-public world models such as GNSS ephemerides, meteorological records, geomagnetic models, astronomical tables, and RF registries [1]. That baseline is directionally correct. Its main weakness is not the choice of sensors, but the way RF channels are treated. In the baseline, Wi-Fi, cellular, and parts of GNSS are mostly **registry-matchable** evidence. An attacker may succeed by presenting plausible identifiers and plausible coarse strengths, even when the overall RF scene is not physically coherent.

This paper sharpens the design in three ways.

First, it **separates the digest contribution from the oracle contribution**. The digest object should stand on its own because preserving temporal structure already raises the bar against replay and stitching.

Second, it **recasts the RF oracle as physics-informed rather than Maxwell-bound**. That is more accurate. The verifier does not solve Maxwell’s equations over a city-scale scene; it attempts to learn a distribution over coarse, receiver-side observables conditioned on scene priors.

Third, and most importantly, it **treats the oracle as part of a strategic game**. Everything that makes a learned physical model useful to the verifier also makes it useful to a sophisticated generator. The correct question is therefore not whether the oracle can ever help in a vacuum, but:

> *What residual value remains when the attacker has access to comparable learned models?*

The answer defended here is bounded and conditional. PISD can still help because generating a trace that is jointly consistent across **multiple windows, multiple channels, latent pose hypotheses, sensor-mask dynamics, and optional online challenge randomness** can be harder than scoring one observed trace against a calibrated acceptance region. But that asymmetry narrows over time. PISD should therefore be viewed as a **time-buyer and bar-raiser**, not as a permanent substitute for trusted sensor hardware.

Recent progress in learned electromagnetic forward models makes this question newly practical. Arena Physica’s March 31, 2026 Atlas RF Studio / Heaviside-0 publication reports component-scale forward prediction with weighted magnitude error well under 1 dB and about 13 ms latency per board on its benchmark, for a current scope centered on two-layer 8 mm × 8 mm RF structures [2]. That result is **not** evidence that scene-scale phone verification is solved. It is only a feasibility signal that high-speed learned EM forward operators are now credible enough to motivate a verifier architecture that was previously too expensive to contemplate.

### 1.1 Contributions

This paper makes six concrete contributions.

1. **Windowed state-and-transition digest (WSTD).**  
   A deterministic, chained evidence object that commits both per-window state and transition structure.

2. **Staleness-aware registry-only verifier.**  
   A deployable verifier for WSTD that uses database/world-model likelihoods, temporal likelihoods, and sensor-mask dynamics, while explicitly inflating uncertainty under stale or sparse registries.

3. **OMR and a metric-robust bootstrap protocol.**  
   A formal rule for deciding when physics-based scoring is warranted, plus a minimum viable campaign for estimating that rule before broad deployment.

4. **Receiver-conditioned RF oracle with explicit engineering constraints.**  
   A latent-pose, progressive-particle formulation with conservative hard-contradiction logic, multiple-testing control, and a minimax weight-learning objective.

5. **Residual-security framing under learned-model attackers.**  
   A direct treatment of defender–attacker symmetry via the notion of **coherence burden**, together with concrete mitigations such as online challenge entropy, score coarsening, multi-party corroboration, and hardware roots of trust.

6. **C2PA privacy and versioning path.**  
   A standards-compatible model in which commitments are public, the full payload is encrypted and access-controlled, and schema evolution degrades gracefully.

### 1.2 What this proposal is not

PISD is **not**:

- a hardware root of trust,
- a replacement for remote attestation in the RFC 9334 / RATS sense [3],
- a complete chain-of-custody system,
- a robust detector of post-capture edits beyond content binding,
- a claim that learned physics permanently solves spoofing,
- or a finished deployment specification for a scene-scale Wi-Fi / cellular oracle.

---

## 2. System decomposition and deployment tiers

A central design principle is to separate what is already well specified from what remains research.

| Tier | Mechanism | Additional requirement | What it mainly buys |
|---|---|---:|---|
| **T0** | Content hash + basic metadata | none | weak binding only |
| **T1** | **WSTD + registry/time verification** | public registries / world models | replay and stitching resistance; better scoring than monolithic digests |
| **T2** | **WSTD + GNSS-first oracle** | learned GNSS visibility / C/N0 model | stronger outdoor resistance to A1 GNSS spoofing |
| **T3** | **WSTD + selective Wi-Fi / cell oracle** | city-scale RF maps + device-family priors | stronger resistance to local RF environment spoofing, where observability supports it |
| **T4** | **Hardware-attested PISD** | trusted sensor path / secure hardware | meaningful answer to A4-class compromise |

This decomposition matters because the digest object can be specified and evaluated now, whereas the full RF oracle must be treated as an empirical research program with clear stop conditions.

### 2.1 Threat model

We retain four attacker classes.

- **A1. Over-the-air RF spoofer.**  
  The attacker is physically near the victim and can transmit fake GNSS, Wi-Fi, or cellular signals, or relay real ones [15].

- **A2. Local environmental manipulator.**  
  The attacker can partially control pressure, light, or acoustic context in a bounded area.

- **A3. Stitcher / replay attacker.**  
  The attacker assembles plausible windows from prior captures or repeats a small number of windows with perturbations.

- **A4. Full device-compromise attacker.**  
  The attacker controls the OS, baseband, sensor hub, or firmware and can inject fabricated readings into the software path.

WSTD mainly targets **A3**. The oracle, if it works, mainly targets **A1**. Neither solves **A4**.

### 2.2 Fail-open policy and assurance policy are different things

PISD remains **fail-open** at capture time: if GPS is absent indoors, a scan is throttled, or a sensor is disabled, the SDK still emits evidence with an explicit mask.

That deployability choice must not be confused with a verification policy. A high-assurance verifier is allowed to require a minimum channel set or to down-score suspicious suppression patterns. In other words:

- **capture-time rule:** always emit a digest if possible;
- **verification-time rule:** confidence depends on what was available, what disappeared, and whether the missingness pattern itself is plausible.

This distinction matters because an attacker who can jam or disable a channel can try to reduce the evidence to only the channels they can spoof. The paper makes that trade-off explicit.

---

## 3. The API observability ceiling and OMR-gated deployment

### 3.1 What commodity phone APIs actually expose

A software verifier does not see raw electromagnetic fields. It sees what the mobile OS permits an app to observe. On Android, for example, Wi-Fi APIs expose visible access points and connected-network information, telephony APIs expose serving and neighboring cell information and technology-specific signal metrics, and GNSS APIs expose satellite status and per-satellite observables [5]–[8].

| Channel | Typical API-visible observables | Notes for verification |
|---|---|---|
| **Wi-Fi** | visible AP list from scan results; connected-network RSSI where available [5], [6] | strongest features are often **set membership**, band mix, rank order, and turnover, not exact dBm |
| **Cellular** | serving and neighboring cell identities; LTE/NR metrics such as RSRP/RSRQ/RSSI/SINR when exposed [7] | neighbor-set evolution and handover structure are often more robust than absolute strengths |
| **GNSS** | satellite count, per-satellite C/N0, carrier frequency, constellation identity [8] | strongest outdoor RF channel because ephemerides are public and geometry is precise |
| **Barometric / magnetic / light / audio / IMU** | pressure series, field magnitude / heading change, lux, privacy-preserving audio features, motion summaries | not RF, but important for environment classification and transition plausibility |

This ceiling is not a nuisance detail. It determines whether a physics oracle is worth building.

### 3.2 Observability Margin Ratio (OMR)

To formalize the observability problem, define a channel- and environment-specific **observability margin ratio**:

$$
\mathrm{OMR}_{c,e}^{(d)} = \frac{\mathrm{med}_{(y,\tilde y)\sim (\text{legit},\text{spoof})} d_c(y,\tilde y)}{\mathrm{med}_{(y,y')\sim (\text{legit},\text{legit})} d_c(y,y')}
$$

where:

- $c$ is a channel or feature family,
- $e$ is an environment class,
- $d_c(\cdot,\cdot)$ is a feature-space distance,
- the numerator measures how far attacks typically sit from truthful observations,
- the denominator measures how far truthful observations move under nuisance variation: body blocking, orientation, scan jitter, registry staleness, benign multipath, device heterogeneity, and so on.

Interpretation:

- $\mathrm{OMR}_{c,e}^{(d)} \le 1$: nuisance variation is as large as or larger than spoof deviation; a physics factor is unlikely to help.
- $\mathrm{OMR}_{c,e}^{(d)} > 1$: attacks create extra separation beyond nuisance variation; a physics factor may be justified.

### 3.3 Metric-robust OMR

OMR can be fragile if it depends too heavily on a particular distance definition. The paper therefore uses a **metric-robust OMR**:

$$
\mathrm{OMR}^{\mathrm{rob}}_{c,e} = \inf_{d \in \mathcal D_c} \mathrm{LCB}_{0.95}\left(\mathrm{OMR}_{c,e}^{(d)}\right)
$$

where $\mathcal D_c$ is a family of admissible distances for feature family $c$:

- Jaccard or overlap distance for identifier sets,
- Kendall-$\tau$ or Spearman-footrule distance for ranked sets,
- Wasserstein or histogram distances for binned amplitudes,
- Hamming-like distances for masks and discrete state codes.

**Deployment rule:** enable a physics term for $(c,e)$ only if

$$
\mathrm{OMR}^{\mathrm{rob}}_{c,e} > 1.
$$

This is intentionally conservative. It forces the oracle to clear not just one convenient metric, but the weakest admissible one.

### 3.4 Design priors before measurement

Before any empirical campaign, the following planning priors are reasonable. They are **design priors, not results**.

| Feature family | Use in the digest | Expected nuisance regime | Expected OMR prior |
|---|---|---|---|
| **GNSS satellite set + C/N0 trajectory** | preserve IDs, order, and temporal evolution | moderate outdoors, poor indoors | **highest** outdoors |
| **Wi-Fi AP set / rank order / scan turnover** | preserve set overlap and rank bins | moderate | **medium** in dense urban / indoor |
| **Absolute Wi-Fi RSSI** | keep only coarse bins or ranks | high orientation / body / multipath sensitivity | **low** |
| **Cell-set turnover and handovers** | preserve identities, technology, and sequence | moderate | **medium** |
| **Absolute cellular metrics** | keep coarse bins only | medium-to-high | **low to medium** |
| **Audio ambience embedding** | preserve coarse spectral / modulation structure | scene-dependent | **medium**, potentially high in some structured outdoor settings |
| **Light / baro / magnetic context** | preserve residuals and aligned changes | channel-specific | context-dependent |

The direct implication is that the digest should emphasize **sets, ranks, and transitions** more than exact amplitudes.

### 3.5 Minimum viable OMR bootstrap campaign

OMR cannot guide deployment unless it is measured first. The paper therefore specifies a **minimum viable OMR campaign**.

A practical first campaign should cover at least:

- **4 environment classes:** dense urban outdoor, indoor office / retail, suburban street, rural open sky;
- **3 device families:** a coarse receiver taxonomy such as flagship, mid-range, and budget handset families;
- **3 carry modes:** handheld, pocket / bag, and table / vehicle mount;
- **2 time bands:** day and night / low-light.

A minimal truthful corpus is therefore on the order of:

$$
4 \times 3 \times 3 \times 2 \times 100 \approx 7200 \text{ traces},
$$

which at 10–20 windows per trace yields roughly $7\times10^4$ to $1.4\times10^5$ windows.

A matching attack corpus should include at least:

- GNSS SDR spoofing or replay,
- Wi-Fi AP spoofing with hostapd-class tooling,
- synthetic A3 stitching / replay traces,
- and, where legal and shielded, limited cellular replay / relay experiments.

This is not enough to certify broad deployment. It is enough to answer a narrower question:

> *Which feature families fail to clear the observability bar so obviously that no oracle effort should be spent on them?*

### 3.6 Simulated attacks versus physical attacks

Simulated attacks are useful, but only for bounded purposes.

- They are acceptable to establish **upper bounds on easy spoofability** and to cull features with obviously poor OMR.
- They are **not** sufficient to set production hard-contradiction thresholds for enabled physics channels.
- Final deployment for a channel/environment pair requires at least one **physically executed attack family** in the measurement campaign for that pair.

This keeps OMR from becoming purely circular while remaining honest about what simulations can and cannot tell us.

---

## 4. Windowed state-and-transition digests (WSTD)

### 4.1 Capture windows

Let the capture interval be $[t_0,t_1]$ and partition it into $J$ contiguous windows $W_1,\dots,W_J$ of duration $\Delta$.

For video, $\Delta$ will typically be 0.5–1.0 s. For still images or short clips, $J$ can be small.

Let $\mathcal C$ be the set of channels:

$$
\mathcal C = \{
\text{GNSS},\text{WiFi},\text{Cell},\text{Baro},\text{Mag},\text{Light},\text{Audio},\text{IMU}
\}.
$$

For each channel $c$ and window $W_j$, raw samples are summarized by a deterministic extractor

$$
u_{c,j} = \phi_c\left(\{x_{c,t}\}_{t\in W_j}\right).
$$

### 4.2 Canonicalization function Q

The canonicalization function $Q$ is not an implementation detail. It determines whether two legitimate devices can agree on a reproducible state sketch. The paper therefore specifies the design principles for $Q$.

For a structured feature vector $v = (v_1,\dots,v_R)$, define

$$
Q(v) = \mathrm{CBOR}\left(
q_1(v_1),\dots,q_R(v_R)
\right),
$$

where each field transform $q_r$ is deterministic and versioned.

The rules are:

1. **Stable ordering.**  
   Identifier sets are sorted by a deterministic key: quantized strength bin, then hashed identifier, then band / technology tag.

2. **Binning before hashing.**  
   Numeric amplitudes are clamped and quantized before serialization. The digest should commit to **ordinally meaningful** values, not unstable raw precision.

3. **Keyed identifier protection.**  
   BSSIDs and cell IDs are transformed by keyed hash or HMAC truncation before storage in $P$ unless policy requires plaintext. This reduces long-term linkability.

4. **Explicit nulls and masks.**  
   Missing values are represented by a dedicated symbol $\bot$ and echoed in the sensor mask.

5. **Length-prefixing and domain separation.**  
   Every serialized field includes type tag, schema version, and length so that future parsers can validate bytes even when they do not semantically understand every field.

A practical example is:

- GNSS C/N0 values binned to 2–3 dB buckets,
- Wi-Fi / cell amplitudes binned to coarse levels or represented only by rank,
- BSSID / cell identifiers truncated to 64-bit keyed digests,
- temporal offsets serialized relative to the capture start.

### 4.3 State sketches

A practical per-window state sketch looks like this.

| Channel | Example state sketch |
|---|---|
| **GNSS** | coarse location prior; top-$N$ satellite IDs; C/N0 bins; constellation counts; DOP summary |
| **Wi-Fi** | keyed hashes of top-$N$ BSSIDs; band counts; rank bins; scan cadence; set cardinality |
| **Cellular** | keyed hashes of top-$M$ cell IDs; technology mix; coarse RSRP / RSRQ bins; serving-vs-neighbor counts |
| **Barometric** | mean pressure, slope bin, variance bin |
| **Magnetometer** | field magnitude bin, heading-change summary |
| **Light** | lux histogram, saturation flags |
| **Audio** | privacy-preserving ambience embedding or normalized spectral / modulation bins |
| **IMU** | motion-mode class; jerk histogram; rotation summary |

The per-window canonical state is

$$
z_j = Q\left(
\bigoplus_{c\in \mathcal C} u_{c,j}
\oplus \chi_j
\right),
$$

where $\chi_j$ is a cross-channel residual sketch.

### 4.4 Cross-channel sketch chi_j

The cross-channel sketch $\chi_j$ is specified algorithmically rather than by example. Let

$$
\chi_j = \Psi\left(
u_{\text{Baro},j},
u_{\text{IMU},j},
u_{\text{Mag},j},
u_{\text{Light},j},
u_{\text{Audio},j},
u_{\text{GNSS},j},
u_{\text{WiFi},j},
u_{\text{Cell},j},
m_j
\right),
$$

with deterministic components such as:

$$
\chi_j =
\Big[
\mathrm{bin}(\rho^{\text{baro-z}}_j),\;
\mathrm{bin}(r^{\text{yaw-mag}}_j),\;
\mathrm{bin}(r^{\odot}_j),\;
\mathrm{bin}(r^{\text{aud-move}}_j),\;
\mathrm{bin}(u^{\text{wifi-turn}}_j),\;
\mathrm{bin}(u^{\text{cell-turn}}_j)
\Big],
$$

where:

- $\rho^{\text{baro-z}}_j$ is the within-window alignment between barometric slope and estimated vertical motion,
- $r^{\text{yaw-mag}}_j$ is the residual between inertial yaw change and magnetometer-implied heading change,
- $r^{\odot}_j$ is a light-versus-astronomy residual when light is available,
- $r^{\text{aud-move}}_j$ is a coarse mismatch between acoustic stationarity and inferred motion class,
- $u^{\text{wifi-turn}}_j$ and $u^{\text{cell-turn}}_j$ are set-turnover features.

These are not intended to be perfect physical laws. They are compact, deterministic residuals that make it harder to synthesize unrelated windows without preserving local coherence.

### 4.5 Transition sketches

For $j\ge 2$, define

$$
\delta_j = \Delta(z_{j-1}, z_j),
$$

where $\Delta$ is channel-aware and may include:

- Jaccard turnover of visible transmitter sets,
- rank flips in Wi-Fi / cell ordering,
- handover indicators,
- change in C/N0 structure,
- motion-mode transitions,
- cross-channel lag changes,
- mask transitions.

A real path through one place yields a locally coherent sequence of $(z_j,\delta_j)$ pairs. A stitched trace made from individually plausible windows usually does not.

### 4.6 Sensor masks, mask-pattern scoring, and fail-open semantics

Each window has a sensor mask $m_j \in \{0,1\}^{|\mathcal C|}$ indicating present channels. The system is intentionally **fail-open** at capture time, but the mask is part of both the commitment and the score.

The paper includes an explicit **mask-pattern likelihood**:

$$
L^{(\mathrm{mask})} = -\log p\left(m_{1:J}\mid e, \text{OS policy}, \text{radio policy}, \ell_{1:J}, t_{1:J}\right)
$$

This term allows the verifier to treat patterns such as:

- GNSS disappearing for exactly one mid-capture window outdoors,
- Wi-Fi scans failing in a way inconsistent with OS throttling,
- or all RF channels vanishing while non-RF channels continue normally,

as weak but useful evidence. This does **not** convert fail-open into fail-closed. It simply acknowledges that missingness can itself be informative.

### 4.7 Evidence payload, chaining, and online / offline binding

We distinguish the **payload** from the **commitment**:

$$
P = \{(z_j,\delta_j,m_j)\}_{j=1}^J.
$$

The chained commitment is

$$
d_0 = 0^{256}, \qquad
d_j = H_3\left(
\mathrm{ser}(z_j)\,\|\,\mathrm{ser}(\delta_j)\,\|\,\mathrm{ser}(m_j)\,\|\,d_{j-1}
\right),
$$

with final digest

$$
D = H_3\left(d_J \,\|\, h_{\text{content}} \,\|\, \mathrm{ctx}\right),
$$

where $h_{\text{content}}$ is a content hash and $\mathrm{ctx}$ captures configuration metadata such as window size, schema version, and feature-family IDs.

The binding supports two modes:

$$
\sigma =
\begin{cases}
\mathrm{HMAC}_{K_{\text{sess}}}(D \,\|\, n), & \text{online capture mode}\\[4pt]
\mathrm{Sig}_{sk_{\text{app}}}(D), & \text{offline capture mode}.
\end{cases}
$$

Here:

- $n$ is a verifier nonce or session challenge,
- $K_{\text{sess}}$ is a short-lived verifier-issued session secret,
- $sk_{\text{app}}$ is an application-managed software key for offline mode.

#### Online challenge entropy

One optional refinement: in online mode, the nonce $n$ may also seed bounded randomization of **extra micro-samples** or **window boundary jitter** for channels that permit it within OS limits. Formally, window boundaries or probe slots can be drawn from

$$
\xi_j = \mathrm{PRF}(n,j) \bmod \Delta_{\max},
$$

subject to platform timing constraints.

This does not change the digest format. It changes the attack problem: a precomputed synthetic trace must now match not only the claimed environment, but also a verifier-chosen sampling pattern that is unknown before capture begins.

The evidence object is

$$
E = (P,D,h_{\text{content}},\sigma,\mathrm{meta}).
$$

### 4.8 Why WSTD stands alone

WSTD has standalone value independent of any RF oracle.

- **Against A3**, it preserves local dynamics that a monolithic digest throws away.
- **Against benign ambiguity**, it allows the verifier to discount isolated anomalous windows rather than collapsing an entire capture into one number.
- **Against sensor loss**, it makes missingness explicit through the mask sequence.

A monolithic digest cannot distinguish:

1. a genuine 10-second walk,
2. ten unrelated plausible 1-second segments,
3. a 1-second replayed segment repeated ten times with small perturbations.

WSTD can at least represent the differences.

### 4.9 Concrete payload-size estimate

A practical default budget for one window is:

| Component | Typical bytes / window |
|---|---:|
| RF set / rank sketches (GNSS + Wi-Fi + cell) | 60–90 |
| Baro / mag / light / audio / IMU summaries | 28–56 |
| Cross-channel residual sketch | 8–16 |
| Transition sketch | 24–40 |
| Sensor mask + per-window overhead | 4–8 |
| **Total / window** | **124–210** |

This yields the following capture-size envelope:

| Capture length | Window size | Windows | Typical payload $P$ |
|---|---:|---:|---:|
| 10 s still / short clip | 1.0 s | 10 | **1.2–2.1 KB** |
| 10 s video | 0.5 s | 20 | **2.5–4.2 KB** |
| 30 s clip | 1.0 s | 30 | **3.7–6.3 KB** |

Add 32 bytes for $D$, 32–64 bytes for $\sigma$ depending on mode, and a small metadata header. The result is small enough for C2PA embedding or external assertion storage.

### 4.10 Architecture sketch

```text
 Media bytes ---------------------> content hash h_content ------------------------------┐
                                                                                         │
 Raw sensor streams -> windowing -> state sketches z_j -> transitions δ_j -> payload P  │
                                                                                         │
                               masks m_j + cross-channel residuals χ_j ------------------┤
                                                                                         │
                                       chained digest d_1..d_J -> D --------------------┤
                                                                                         │
                      online nonce / session key OR offline app key -> σ ----------------┘

 Upload:
   asset + E = (P, D, h_content, σ, meta)

 Verifier pipeline:
   1. binding + chain validation
   2. registry / time scoring over WSTD
   3. staleness and mask-pattern adjustment
   4. optional RF physics-oracle scoring
   5. environment-mixture calibration
   6. verdict + protected receipt + optional C2PA assertion
```

---

## 5. Registry-only verification: the deployable baseline

### 5.1 World-model likelihood without a physics oracle

For each channel $c$ and window $j$, the verifier computes a database / world-model negative log-likelihood

$$
\ell^{(\mathrm{db})}_{c,j} = -\log p^{(\mathrm{db})}_c\left(u_{c,j} \mid \ell_j,t_j,e\right)
$$

where:

- $\ell_j$ is the claimed coarse location for window $j$,
- $t_j$ is the time,
- $e$ is a latent environment class.

Examples include:

- GNSS ephemerides from CDDIS / IGS [11],
- meteorological pressure context from GHCNh or equivalent [9],
- geomagnetic priors from WMM2025 [10],
- astronomical priors from JPL Horizons [12],
- cell registries from OpenCelliD [13].

A public-registry-only verifier should treat Wi-Fi and cell databases as **supporting evidence**, not infallible truth. Sparse maps widen uncertainty; they do not create contradictions by themselves.

### 5.2 Registry staleness and coverage-aware uncertainty inflation

Registry staleness is a first-order concern, not a minor detail. The paper therefore models registry reliability explicitly.

Let $a_{c,j}$ be the age of the relevant registry evidence and let $\kappa_{c,e}(\ell_j)\in[0,1]$ be a local coverage factor for the geography and environment. Define a reliability factor

$$
\rho_{c,j} = \exp\left(-\frac{a_{c,j}}{\tau_c}\right)\,\kappa_{c,e}(\ell_j).
$$

Then replace the naïve likelihood with a freshness mixture:

$$
p^{(\mathrm{db}\star)}_c = \rho_{c,j}\, p^{(\mathrm{fresh})}_c + (1-\rho_{c,j})\, p^{(\mathrm{broad})}_c
$$

and correspondingly

$$
\ell^{(\mathrm{db}\star)}_{c,j} = -\log p^{(\mathrm{db}\star)}_c
$$

Interpretation:

- **fresh, well-covered maps** behave like the ordinary registry model;
- **stale or sparse maps** back off toward a broad prior rather than creating a contradiction;
- **geographic inequity** therefore appears as lower confidence and wider intervals, not as systematic false contradiction.

This also limits a staleness-exploitation attack in which the adversary chooses identifiers that are valid only in an old registry snapshot. Such evidence may still gain weak support, but not the strong support of a fresh match.

### 5.3 Temporal likelihood and mask dynamics

WSTD enables a transition likelihood

$$
\ell^{(\mathrm{tmp})}_{c,j} = -\log p^{(\mathrm{tmp})}_c\left(\delta_{c,j}\mid z_{c,j-1:j}, e\right)
$$

This term captures things that a monolithic digest cannot:

- whether set turnover is plausible for the claimed motion,
- whether handovers occur at plausible rates,
- whether barometric change agrees with inertial motion,
- whether light change tracks astronomical expectations,
- whether mask changes follow plausible platform behavior.

We incorporate mask-pattern scoring as its own additive term:

$$
L^{(\mathrm{tmp+mask})}_c = \sum_{j=2}^J \gamma_c \ell^{(\mathrm{tmp})}_{c,j} + \eta_c L^{(\mathrm{mask})}
$$

### 5.4 Environment classification as a latent variable, not a hard pre-score label

A second important design choice is that environment classification is kept **latent** throughout scoring rather than assigned as a hard pre-score label. If thresholds are conditioned on environment class, but the environment class is inferred from the same evidence under verification, the system risks miscalibration under spoofed evidence.

The paper handles this by keeping environment class **latent** throughout scoring. Let $p(e\mid P,M)$ be an environment posterior built from broad cues such as motion class, RF richness level, barometric behavior, audio / light context, and GNSS availability pattern. Then calibration is mixture-based:

$$
s_c = \sum_{e\in\mathcal E} p(e\mid P,M)\,\mathrm{Cal}_{c,e,m}(L_{c,e})
$$

where $m$ is the sensor-mask pattern class.

For hard contradiction logic, the rule is even more conservative. Let $\mathcal E_{0.9}$ be the smallest set of environment classes whose posterior mass is at least 0.9. Then contradiction is declared only if the evidence contradicts **all** plausible environments:

$$
p_c^{\mathrm{hard}} = \max_{e\in\mathcal E_{0.9}} p_{c,e}^{\mathrm{contra}}
$$

A channel is flagged only if $p_c^{\mathrm{hard}} < \varepsilon_c$.

### 5.5 Registry-only channel score

Define the channel loss for registry-only verification as

$$
L^{(\mathrm{reg})}_c = \sum_{j=1}^J \alpha_c \ell^{(\mathrm{db}\star)}_{c,j} + L^{(\mathrm{tmp+mask})}_c
$$

The calibrated channel score is

$$
s^{(\mathrm{reg})}_c = \mathrm{Cal}_c(L^{(\mathrm{reg})}_c; P,M),
$$

and the aggregate registry-only score is

$$
S^{(\mathrm{reg})} = \sum_{c\in\mathcal C} w_c s^{(\mathrm{reg})}_c,
\qquad
\sum_c w_c = 1.
$$

This is the proper deployable baseline that any oracle must beat.

---

## 6. Receiver-conditioned RF oracle

### 6.1 What the oracle is allowed to predict

A strong correction is to state explicitly what the oracle does **not** predict. It does **not** predict raw receive-side fields or handset-internal S-parameters at capture time. Commodity phones do not expose them.

The oracle predicts a distribution over **API-visible RF observations**, such as:

- satellite visibility and C/N0 structure,
- visible AP set, band mix, and rank order,
- serving / neighboring cell set and coarse metric bins,
- short-term evolution of the above across adjacent windows.

This is a weaker target than scene-scale EM truth, but it is the only one relevant to a software-only verifier.

### 6.2 Latent pose and environment marginalization

The prior approach of conditioning the oracle on a single estimated pose creates circularity: pose is inferred from data that are themselves under verification.

To address this, pose and environment remain latent. Let:

- $g_d$ be a device-family receiver prior,
- $q_{1:J}$ be the latent pose trajectory,
- $e$ be an environment class,
- $\mathcal S_j = \mathcal B(\ell_j,t_j,e)$ be the scene prior for window $j$.

The RF observation model is

$$
p_\theta\left(y^{(\mathrm{rf})}_{1:J}\mid \ell_{1:J}, t_{1:J}, g_d\right) = \sum_e p(e\mid P,M) \int p_\theta\left(y^{(\mathrm{rf})}_{1:J}, q_{1:J}\mid e,\ell_{1:J}, t_{1:J}, g_d\right)\,dq_{1:J}
$$

The verifier therefore does **not** commit to a single pose or single environment label before scoring plausibility.

### 6.3 Particle generation, progressive refinement, and budget

Latent-pose marginalization is only useful if the particle set is both plausible and computationally manageable. The paper therefore specifies a progressive schedule.

#### Step 1: coarse carry-mode posterior

Generate a coarse carry-mode posterior over

$$
r \in \{\text{handheld portrait},\ \text{handheld landscape},\ \text{pocket/bag},\ \text{table},\ \text{vehicle mount}\}
$$

from IMU gravity alignment, camera orientation metadata when available, motion class, and short-term magnetometer stability.

#### Step 2: coarse particles

For each likely carry mode, sample a small orientation / attenuation family around its canonical pose. A practical default is:

- **$K_0 = 8$** coarse particles for GNSS-first mode.

#### Step 3: adaptive refinement

If the marginal RF likelihood spread remains large, refine around the top particles using local yaw / pitch / roll perturbations and carry-mode alternatives:

- **$K_1 = 24$** for normal oracle evaluation,
- **$K_{\max} = 64$** as a hard cap.

Stop refinement when the marginal log-likelihood stabilizes:

$$
\Delta_K = \left| \log \sum_{k=1}^{K}\pi_k p(y\mid q^{(k)}) - \log \sum_{k=1}^{K/2}\pi_k p(y\mid q^{(k)}) \right| < \eta
$$

for two successive refinements.

This yields a practical latency discipline:

- GNSS-first oracle: usually $K\in[8,24]$,
- broader Wi-Fi / cell oracle: $K\in[24,64]$ only when justified by OMR.

### 6.4 Per-window physics likelihood

For RF channel $c$ in window $j$,

$$
\ell^{(\mathrm{phy})}_{c,j} = -\log \left( \sum_{k=1}^K \pi_k\, p_{\theta,c}\left(y_{c,j} \mid q_j^{(k)}, \mathcal S_j, g_d, e\right) \right)
$$

where $\pi_k$ are pose-hypothesis weights.

This replaces the earlier geometric-mean combiner with a proper likelihood term.

### 6.5 Weight learning for alpha_c, beta_c, gamma_c

The full channel loss coefficients cannot simply appear by fiat. They are therefore constrained to the probability simplex and learned against held-out truthful data and a library of proxy attacks.

Let

$$
\bar{\ell}_{c,j} = \big(\ell^{(\mathrm{db}\star)}_{c,j}, \ell^{(\mathrm{phy})}_{c,j}, \ell^{(\mathrm{tmp})}_{c,j}\big), \qquad \lambda_c = (\alpha_c,\beta_c,\gamma_c)
$$

with $\lambda_c \in \Delta^2$, the 3-simplex.

Define the channel loss as

$$
L_c = \sum_{j=1}^J \lambda_c^\top \bar{\ell}_{c,j} + \eta_c L^{(\mathrm{mask})}.
$$

Learn $\lambda_c$ by minimizing worst-case calibration loss across a library of attack families $\mathcal A_{\text{proxy}}$:

$$
\lambda_c^\star = \mathrm{argmin}_{\lambda \in \Delta^2} \max_{a\in\mathcal A_{\text{proxy}}} \mathcal L_{\mathrm{NLL}}\left(\lambda; \mathcal D^{\mathrm{legit}}, \mathcal D^{a}\right)
$$

Interpretation:

- if attack coverage is weak, the optimizer stays conservative because it must perform across the available family library;
- if an oracle term is unstable or poorly calibrated, its learned weight naturally falls;
- for tiers without an oracle, set $\beta_c = 0$ by construction.

### 6.6 Full channel score

The calibrated channel score is

$$
s_c = \mathrm{Cal}_c(L_c; P,M),
$$

and the aggregate score remains

$$
S = \sum_{c\in\mathcal C} w_c s_c.
$$

The important shift is not one specific calibration function. It is that the score now arises from **likelihood accumulation, minimax weight learning, and held-out calibration**, rather than an ad hoc geometric mean.

### 6.7 Hard contradictions, critical windows, and multiple testing

Hard-contradiction logic requires careful window selection. The paper makes it explicit.

For channel $c$, define a per-window observability priority

$$
\zeta_{c,j} = f_c\left(\widehat{\mathrm{OMR}}_{c,e}, m_{c,j}, \text{SNR proxy}, \text{coverage quality}\right).
$$

Select the critical window set as the top-$k_c$ windows by $\zeta_{c,j}$ among windows where channel $c$ is present:

$$
\mathcal J^\star_c = \mathrm{TopK}_{j:m_{c,j}=1}(\zeta_{c,j}),
\qquad
k_c \le 5.
$$

For each such window, compute a conservative contradiction p-value by maximizing over plausible environments:

$$
p_{c,j}^{\max} = \max_{e\in\mathcal E_{0.9}} \sum_{k=1}^K \pi_k \Pr\left[\tilde y \text{ at least as extreme as } y_{c,j} \mid q_j^{(k)},\mathcal S_j,g_d,e\right]
$$

Apply Holm-Bonferroni correction across $\mathcal J^\star_c$ to obtain $p_{c}^{\mathrm{Holm}}$.

A hard contradiction is declared only if:

1. $p_c^{\mathrm{Holm}} < \varepsilon_{c,e,m}$, and
2. at least $r_c$ windows in $\mathcal J^\star_c$ have individual $p_{c,j}^{\max} < \varepsilon_0$.

This prevents a single surprising window from causing an irreversible flag while still allowing decisive contradictions when multiple informative windows fail.

### 6.8 What Heaviside-class results do and do not imply

The role of Arena Physica’s result remains deliberately narrow [2].

What it **does** imply:

- learned EM forward operators can achieve useful accuracy in at least one RF domain,
- they can run at latencies that make verifier integration thinkable.

What it **does not** imply:

- that component-scale board prediction solves scene-scale mobile verification,
- that current Atlas RF Studio already predicts urban receive-side phone observables,
- or that phone-specific geometry priors are easy to obtain.

Accordingly, PISD treats the oracle as a staged research program, not as an already available product module.

---

## 7. Data, calibration, device heterogeneity, and maintenance

### 7.1 Truthful labels are not free

Calibration data requirements are deeper than "collect enough windows." Truthful labels do not simply appear.

The paper assumes four possible label sources:

1. **Controlled lab captures.**  
   Clean labels, narrow diversity.

2. **Hardware-attested pilot captures.**  
   Best anchor source where available, but ecosystem-limited.

3. **Cross-device corroborated captures.**  
   Multiple nearby devices or trusted infrastructure agreeing on the event.

4. **Strict T1 bootstrap labels.**  
   Only captures that pass a conservative registry-only verifier with strong consensus margins are allowed into a weakly supervised pool.

The first two sources provide seed labels; the latter two provide scale. The important discipline is that oracle calibration should never be trained indiscriminately on whatever the system itself happens to accept.

### 7.2 Device heterogeneity: receiver families, not per-SKU perfection

The receiver-prior problem is partly technical and partly ecosystem-driven. The paper therefore avoids per-SKU perfection as an assumption.

Instead, devices are mapped into **receiver families** using a coarse descriptor:

- chipset generation,
- radio stack generation,
- form factor / antenna layout proxy,
- public benchmark behavior,
- and observed calibration residuals.

The design target is a taxonomy of roughly **10–20 receiver families**, not hundreds of exact models. Unknown devices fall back to a broad public prior and receive lower confidence until enough truthful captures support family assignment.

This is weaker than OEM-supplied geometry, but it is achievable without requiring handset vendors to disclose proprietary RF structure.

### 7.3 Drift detection and recalibration

Registries change, towers are added or removed, APs are retired, weather baselines shift, and software platforms evolve. Production deployment therefore requires continuous recalibration.

Let $\mathcal R_{c,e}^{\mathrm{ref}}$ be the reference distribution of calibrated residuals for channel $c$ and environment $e$, and let $\mathcal R_{c,e}^{\mathrm{live}}(t)$ be the current live distribution over a recent window. Define a drift statistic such as Kolmogorov–Smirnov distance:

$$
\mathrm{Drift}_{c,e}(t) = D_{\mathrm{KS}}\left(\mathcal R_{c,e}^{\mathrm{ref}}, \mathcal R_{c,e}^{\mathrm{live}}(t)\right)
$$

If $\mathrm{Drift}_{c,e}(t) > \tau_{c,e}^{\mathrm{drift}}$, then the verifier must either:

1. widen uncertainty,
2. retrain the relevant calibrator,
3. or disable the affected oracle factor.

This makes calibration maintenance a first-class system requirement rather than an afterthought.

### 7.4 Data-budget estimates

The following numbers remain **planning assumptions**, not reported results.

| Goal | Order of magnitude | Why |
|---|---:|---|
| **WSTD registry-only calibration** | $10^4$–$10^5$ windows | enough to fit mask- and environment-conditioned calibrators |
| **Minimum viable OMR campaign** | $7\times10^4$–$1.5\times10^5$ windows | enough to reject obviously weak feature families |
| **GNSS-first oracle** | $10^5$–$10^6$ windows across 10–20 receiver families | public ephemerides make labels cheap; captures still need diverse sky views and motion |
| **Selective Wi-Fi / cell oracle** | $10^7+$ windows or strong external RF maps | city-scale variability, drift, and device heterogeneity dominate |
| **Per-device personalization** | 10–100 truthful captures per device | useful as a refinement layer only |

These budgets are one reason the staged program matters: WSTD and GNSS-first are tractable well before a broad Wi-Fi / cell scene oracle.

### 7.5 Latency budget

A realistic warm-cache target is:

| Stage | Target latency |
|---|---:|
| Chain + binding validation | < 1 ms CPU |
| Registry / time model lookup + scoring | 2–10 ms |
| GNSS / baro / magnetic / astronomy eval | 1–5 ms |
| Optional GNSS-first oracle ($K \le 24$) | 10–40 ms accelerator target |
| Optional broader Wi-Fi / cell oracle ($K \le 64$) | 30–120 ms accelerator target |
| Calibration + verdict | < 5 ms |
| **Total registry-only** | **5–25 ms** |
| **Total oracle-augmented** | **20–140 ms** |

These are design targets, not measured production benchmarks.

A simple accelerator cost model remains

$$
\text{accelerator-hours/day} = \frac{N_{\text{ver}} T_{\text{acc}}}{3600}
$$

where $N_{\text{ver}}$ is daily verifications and $T_{\text{acc}}$ is accelerator time per verification. At $N_{\text{ver}}=10^6$ and $T_{\text{acc}}=0.05$ s, this is about 13.9 accelerator-hours/day.

### 7.6 Why GNSS-first remains the right proof of concept

GNSS still has three decisive advantages:

1. **Precise public world model.**  
   Ephemerides and clocks are public from CDDIS / IGS [11].

2. **Better-defined geometry.**  
   Satellite visibility and C/N0 structure are governed by orbital mechanics and line-of-sight constraints more cleanly than urban Wi-Fi / cell multipath.

3. **Likely higher OMR outdoors.**  
   GNSS satellite sets and their evolution under motion are expected to separate truthful and spoofed traces better than raw Wi-Fi RSSI.

The most credible first oracle is therefore:

> **GNSS-first, outdoor-first, registry-backed, likelihood-calibrated, and explicitly receiver-family rather than device-perfect.**

---

## 8. Defender–attacker symmetry and forward-looking risks

### 8.1 The symmetric-oracle problem

Any learned physical model deployed for verification is also useful to a sophisticated attacker.

If the verifier uses a model $\mathcal R_\theta$ to score what RF observations should look like at a claimed location and time, the attacker can attempt to:

1. extract or approximate $\mathcal R_\theta$ through querying or independent training [23], [24];
2. run a comparable model against the target claim;
3. synthesize observations that land inside the verifier’s acceptance region.

The resulting strategic picture is not “physics helps only defenders.” It is:

> **better learned physical models improve both the verifier’s discriminator and the attacker’s generator.**

This is the central reason PISD must be framed as a bounded software-only defense.

### 8.2 Learned-model synthesis of transition sketches

The strongest standalone claim of WSTD is that it makes stitching and replay harder. That claim is true **today**, because synthesizing plausible multi-window transition sketches across channels is materially harder than replaying static snapshots.

But that claim has a shelf life. As learned models of RF propagation, acoustics, atmospheric state, inertial dynamics, and lighting mature, an attacker can increasingly synthesize not only plausible states, but **plausible transitions**:

- Wi-Fi and cell turnover consistent with a fake path,
- GNSS satellite geometry consistent with claimed time,
- pressure drift and motion summaries consistent with claimed movement,
- ambient audio and light changes consistent with scene type,
- and mask patterns consistent with platform behavior.

The adversary then stops being a “stitcher” and becomes a **trajectory generator**. That is the long-term vulnerability of any digest whose main defense is temporal coherence.

### 8.3 Coherence burden: a way to state residual value under adaptive attackers

To answer the question of residual value under adaptive attackers, the paper introduces a deployment-side quantity: **coherence burden**.

Let $c$ denote a claim (location, time, device-family prior, capture policy). Let $U$ denote hidden nuisance variables such as latent pose, online challenge randomness, local multipath realization, and corroboration requirements. Let $\mathcal A(c,U)$ be the verifier’s acceptance region for that claim under those hidden conditions. For an adaptive generator $G_\phi$ that produces candidate evidence $Y \sim G_\phi(c)$, define

$$
\mathrm{CB}_e(G_\phi) = -\log \mathbb E_{(c,U)\sim e} \Pr_{Y\sim G_\phi(c)}\left[Y \in \mathcal A(c,U)\right]
$$

Interpretation:

- low $\mathrm{CB}$ means the attacker often lands inside the acceptance region;
- high $\mathrm{CB}$ means the joint consistency constraints are costly to satisfy.

The **residual value** of the oracle under adaptive attackers is then

$$
\Delta \mathrm{CB}_e = \mathrm{CB}^{\mathrm{WSTD+phy}}_e - \mathrm{CB}^{\mathrm{WSTD+reg}}_e
$$

PISD has a defensible claim only if $\Delta \mathrm{CB}_e > 0$ in environments where deployment is proposed.

This formulation makes the endgame honest:

- if online randomness is zero,
- if the attacker’s generator class becomes rich enough,
- and if there is no corroboration or hardware root,

then $\mathcal A(c,U)$ can become easy enough to hit that $\Delta \mathrm{CB}_e \to 0$.

That is precisely why software-only provenance eventually hits a ceiling.

### 8.4 What residual value can still remain?

Even under gray-box or near-white-box attacker assumptions, some residual value can remain because the attacker’s problem is still a **joint generation problem**:

1. satisfy multiple channels simultaneously,
2. satisfy multiple windows and transition constraints,
3. satisfy latent pose and environment mixtures,
4. satisfy sensor-mask dynamics,
5. and, in online mode, satisfy verifier-chosen sampling randomness.

The verifier, by contrast, evaluates **one observed trace** against a calibrated family of acceptance constraints.

That asymmetry is real, but it is not permanent. The correct claim is therefore:

> **PISD can raise the attacker's coherence burden, sometimes materially, but cannot guarantee durable asymmetry once comparable learned generators exist.**

### 8.5 Practical mitigations against symmetry collapse

The paper therefore recommends several concrete mitigations.

#### 8.5.1 Online challenge entropy

Nonce-seeded scan timing jitter or extra micro-samples force the attacker to respond to conditions not known before capture. This is the software-only analogue of a challenge-response protocol.

#### 8.5.2 Score coarsening and query-rate control

A verification API should not expose raw continuous per-channel scores by default. Doing so accelerates oracle extraction. Safer defaults are:

- coarse verdict bands,
- minimal reason codes,
- rate limiting,
- and anomaly monitoring for search-like querying behavior.

#### 8.5.3 Multi-party corroboration

Requiring corroboration from a second nearby device or trusted infrastructure turns one synthetic trace into a multi-observer consistency problem. This can raise coherence burden faster than single-device oracle refinement alone.

#### 8.5.4 Adversarial training and OOD detection

Where feasible, the oracle should be trained against learned spoof generators and monitored for “too clean” or otherwise synthetic-looking traces. This is not a silver bullet, but it is better than assuming non-adaptive attackers forever.

#### 8.5.5 Hardware roots of trust

Ultimately, the cleanest long-term defense is still a trusted sensor path and hardware attestation. PISD’s strategic value is strongest when seen as a bridge to that future, not as a replacement for it.

### 8.6 Broader forward-looking risk

The strategic problem is not confined to media provenance. As learned models for RF propagation, acoustics, inertial dynamics, weather, and optical rendering mature, **environment-consistent synthetic sensor evidence** becomes cheaper to generate across many domains. The long-term risk is not merely more spoofing. It is erosion of the evidentiary status of “sensor-consistent” digital records unless those records are anchored in hardware or corroborated by independent observers.

That broader claim is not needed for PISD to be useful today. It is needed to avoid overstating what software-only verification can mean five years from now.

---

## 9. C2PA integration, privacy, and versioning

### 9.1 Public commitments versus protected payload

C2PA manifests are public-facing, while WSTD payloads contain location-correlated data that should not be public by default.

The paper therefore splits provenance into two layers:

1. **Public layer (in the C2PA manifest):**
   - digest commitment $D$,
   - schema version,
   - window size,
   - channel summary,
   - protected payload hash,
   - verifier-receipt hash,
   - policy and oracle mode identifiers.

2. **Protected layer (external or encrypted assertion):**
   - full payload $P$,
   - sensitive channel detail,
   - verifier access policy,
   - optional retention metadata.

The verifier validates the public commitment against the protected payload hash; consumers need not see the payload itself.

### 9.2 Online access-control model

For online capture or submission, let $k_P$ be a random payload key. The client stores

$$
C_P = \mathrm{AEAD}_{k_P}(P, \mathrm{AAD}=D \,\|\, h_{\text{content}}),
$$

and wraps $k_P$ to the verifier service using HPKE or an equivalent hybrid public-key scheme:

$$
\widehat{k}_P = \mathrm{HPKE}_{pk_V}(k_P).
$$

The manifest carries:

- $D$,
- $H(C_P)$,
- a URI or opaque handle to the protected blob,
- and a policy identifier.

A verifier with authorization unwraps $k_P$, fetches $C_P$, validates $H(C_P)$, and then evaluates $P$.

This gives a concrete answer to the privacy question: the manifest stays public, the evidence stays verifier-readable only.

### 9.3 Offline capture model

Offline capture has no verifier public key available at creation time. The paper therefore uses a two-step sealing process:

1. At capture time, the client generates local $k_P$ and stores $C_P = \mathrm{AEAD}_{k_P}(P)$ locally or in creator-controlled cloud storage.
2. At submission time, the client re-wraps $k_P$ to the chosen verifier or to a policy gateway, producing $\widehat{k}_P$.

The C2PA manifest can still carry:

- $D$,
- $H(C_P)$,
- and a policy handle,

even before the protected payload is disclosed.

This preserves offline capture without forcing raw location evidence into the manifest.

### 9.4 Privacy controls and regulatory posture

A production deployment should, at minimum:

- minimize raw identifier retention,
- hash or tokenize BSSIDs and cell IDs,
- use short retention windows or explicit TTLs for $C_P$,
- log verifier access,
- require purpose limitation and user disclosure,
- support regional storage and deletion controls,
- and keep raw audio off-device only in transformed, privacy-preserving form.

Nothing in PISD removes the fact that location-adjacent evidence is privacy-sensitive. The goal is to make the standards path concrete enough that privacy is a design constraint rather than a footnote.

### 9.5 Versioning and extensibility

C2PA itself has a versioning model [4], and PISD should align to it.

The paper adopts three rules.

1. **Major version changes** modify commitment semantics or canonicalization and require a new assertion label, e.g. `org.aska.pisd.v4`.

2. **Minor version changes** may add optional channel families or features, provided the canonical serialization remains self-describing and domain-separated.

3. **Future-verifier behavior** is explicitly defined:
   - if the verifier understands the major version, it validates and scores all known fields while ignoring unknown optional ones;
   - if it does **not** understand the major version, it may still validate the claim signature and content binding, but it must return **“binding valid, semantics unsupported.”**

This is important because provenance manifests may persist for years, while verifier software evolves much faster.

### 9.6 Example C2PA embedding

```json
{
  "type": "org.aska.pisd.v1",
  "digest_alg": "sha3-256",
  "schema_version": "1.0.0",
  "window_ms": 1000,
  "channels_summary": ["gnss", "wifi", "cell", "baro", "mag", "imu", "audio"],
  "evidence_commitment": "<base64(D)>",
  "protected_payload_hash": "<base64(H(C_P))>",
  "payload_access": {
    "mode": "external-hpke",
    "ttl_hours": 24,
    "policy_id": "verifier-only-v1"
  },
  "verifier_receipt_hash": "<base64(H(receipt))>",
  "oracle_mode": "none | gnss-first | selective-rf",
  "semantic_status": "full | partial | binding-only"
}
```

This uses C2PA as the public provenance envelope while keeping sensitive evidence under a distinct access policy.

---

## 10. Evaluation roadmap and hypotheses

The evaluation plan is explicitly staged.

### 10.1 H1: WSTD reduces stitching and replay acceptance

Let $FAR^{A3}_{\text{mono},e}$ be the false-accept rate of a monolithic digest under A3 in environment $e$, and let $FAR^{A3}_{\text{WSTD},e}$ be the same rate for WSTD with registry-only scoring. Define

$$
\Delta^{A3}_{e} = FAR^{A3}_{\text{mono},e} - FAR^{A3}_{\text{WSTD},e}
$$

The digest contribution is successful if $\Delta^{A3}_{e} > 0$ where stitching is realistic.

### 10.2 H2: the oracle reduces A1 acceptance where OMR supports it

Let $FAR^{A1}_{\text{reg},e}$ be the false-accept rate of the registry-only WSTD verifier under A1, and let $FAR^{A1}_{\text{phy},e}$ be the corresponding rate with the oracle enabled. Define

$$
\Delta^{A1}_{e} = FAR^{A1}_{\text{reg},e} - FAR^{A1}_{\text{phy},e}
$$

The oracle is worth deploying only if:

1. $\Delta^{A1}_{e} > 0$ by a meaningful margin, and
2. the truthful false-reject penalty
   $$
   \Delta FRR_e = FRR_{\text{phy},e} - FRR_{\text{reg},e}
   $$
   remains acceptable.

### 10.3 H3: deploy physics only where metric-robust OMR supports it

For channel $c$ and environment $e$, enable the physics term only if

$$
\mathrm{OMR}^{\mathrm{rob}}_{c,e} > 1.
$$

This creates a disciplined deployment rule:

- **GNSS outdoors:** likely yes,
- **Wi-Fi set-turnover in dense urban / indoor:** maybe,
- **absolute Wi-Fi RSSI:** likely no,
- **absolute cellular metrics:** only with evidence,
- **indoor GPS-denied spaces:** likely no GNSS physics factor.

### 10.4 H4: residual value under adaptive gray-box attackers is measurable

Let $FAR^{A1,\mathrm{adapt}}_{\text{reg},e}$ and $FAR^{A1,\mathrm{adapt}}_{\text{phy},e}$ be false-accept rates under attackers that optimize against a surrogate of the oracle. Define

$$
\Delta^{A1,\mathrm{adapt}}_e = FAR^{A1,\mathrm{adapt}}_{\text{reg},e} - FAR^{A1,\mathrm{adapt}}_{\text{phy},e}
$$

Equivalently, estimate $\Delta \mathrm{CB}_e$ from Section 8.3.

The oracle has residual value only if $\Delta^{A1,\mathrm{adapt}}_e > 0$ or, equivalently, $\Delta \mathrm{CB}_e > 0$ under the attacker families that approximate the deployment threat.

### 10.5 Stage ordering

The staged roadmap is therefore:

1. **Stage 1:** prove WSTD helps without any oracle.
2. **Stage 2:** run the minimum viable OMR campaign and reject weak feature families.
3. **Stage 3:** build a GNSS-first oracle.
4. **Stage 4:** evaluate adaptive gray-box attacks and estimate coherence burden.
5. **Stage 5:** expand selectively into Wi-Fi / cell feature families whose metric-robust OMR justifies it.

### 10.6 Key ablations

The most informative ablations are:

1. monolithic digest vs WSTD,
2. WSTD registry-only vs WSTD + GNSS-first oracle,
3. single-pose conditioning vs latent-pose marginalization,
4. fixed weights vs minimax-learned weights,
5. global thresholds vs environment-mixture calibration,
6. raw-amplitude-heavy features vs set / rank / transition features,
7. oracle with and without online challenge entropy,
8. oracle with and without score coarsening against model extraction.

---

## 11. Limitations, ethics, and governance

### 11.1 A4 remains the clean failure mode

If the sensor pipeline is malicious and emits fabricated but internally consistent traces, a software verifier cannot fundamentally defeat it. PISD should never be sold as solving that problem.

### 11.2 Geographic and socioeconomic bias

Dense cities with rich infrastructure are easier than rural, maritime, aerial, or conflict-zone settings. Sparse-registry environments yield broader uncertainty and lower confidence. The correct response is uncertainty inflation and policy-aware presentation, not pretending equal confidence everywhere.

### 11.3 Legal and experimental constraints

GNSS spoofing, rogue AP experiments, and especially cellular spoofing can be unlawful outside shielded or licensed environments [15]. Evaluation must be conducted in controlled conditions with appropriate approvals.

### 11.4 Privacy-sensitive channels

RF identifiers, pressure traces, and especially audio-derived features are location-correlated and potentially sensitive. Privacy-preserving transforms, minimal retention, and user-facing disclosure are mandatory deployment requirements, not optional extras.

### 11.5 Software-only provenance has a ceiling

The strongest limitation is strategic rather than algorithmic:

> **If the attacker can run a comparable generator and the system has no hidden entropy, no corroboration, and no trusted hardware, software-only provenance approaches a ceiling.**

PISD is useful precisely because it raises the bar during the window before that ceiling becomes operationally dominant. It should be framed that way.

---

## 12. Conclusion

The strongest result of this paper is conceptual discipline.

The **windowed state-and-transition digest** is a concrete, useful contribution on its own. It creates the right evidence object for software-only provenance because it preserves local dynamics, makes missingness explicit, promotes cross-channel residuals into the digest, and makes replay and stitching meaningfully harder than in a monolithic digest.

The **receiver-conditioned physics oracle** is a second, distinct contribution. It is plausible enough to justify research because fast learned RF forward operators and propagation models now exist [2], [17]–[22], but it remains an empirical bet constrained by the coarse observability of mobile APIs. The right near-term stance is therefore not “physics solves spoofing,” but:

> **Use WSTD now. Measure metric-robust OMR. Build a GNSS-first oracle first. Expand only where empirical separation exists. Treat the whole software-only stack as a time-buyer, not an endpoint.**

That conclusion is deliberately narrow, but strong. It gives the digest mechanism independent value, turns the oracle into a falsifiable research program, introduces a deployment discipline for deciding when physics terms are worth using, and answers the central analytic question directly:

> **PISD's residual value under learned-model attackers is the amount by which it raises the attacker's coherence burden before trusted hardware becomes necessary.**

That is a bounded claim. It is also, at least for now, a useful one.

---

## References

[1] ASKA Program. *ASKA repository documentation on spatiotemporal content verification and auxiliary-memory integrity mechanisms* (see `README.md`, `10.md`, and `13.md`, covering P30, P31, and P34b). GitHub, commit `d99183bfcd8770ef209dd917c4c3701e3e0d96de`, accessed April 2, 2026. https://github.com/nshkrdotcom/ASKA/blob/d99183bfcd8770ef209dd917c4c3701e3e0d96de/README.md ; https://github.com/nshkrdotcom/ASKA/blob/d99183bfcd8770ef209dd917c4c3701e3e0d96de/10.md ; https://github.com/nshkrdotcom/ASKA/blob/d99183bfcd8770ef209dd917c4c3701e3e0d96de/13.md

[2] Christopher Bryant, Tommaso Dreossi, Hao Liu, Nathan Mirman, Noah Kessler, Usman Farman, Daniel Pedraza, Trevor Beaton, Akshay Kumar, Ben Gelb, Mike Frei, Arun Natarajan, and Harish Krishnaswamy. *Introducing Atlas RF Studio: Toward a Foundation Model for Electromagnetics.* Arena Physica research publication, March 31, 2026. https://www.arenaphysica.com/publications/rf-studio

[3] Henk Birkholz, Dave Thaler, Michael Richardson, Ned Smith, and Weiming Pan. *Remote ATtestation procedureS (RATS) Architecture.* RFC 9334, IETF, January 2023. https://www.rfc-editor.org/rfc/rfc9334

[4] Coalition for Content Provenance and Authenticity (C2PA). *Content Credentials: C2PA Technical Specification.* Version 2.3, 2025. https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html

[5] Android Developers. *Wi-Fi scanning overview.* Official developer documentation. https://developer.android.com/develop/connectivity/wifi/wifi-scan

[6] Android Developers. *WifiInfo API reference.* Official developer documentation. https://developer.android.com/reference/android/net/wifi/WifiInfo

[7] Android Developers. *TelephonyManager* and *CellSignalStrength* API references. Official developer documentation. https://developer.android.com/reference/android/telephony/TelephonyManager ; https://developer.android.com/reference/android/telephony/CellSignalStrength

[8] Android Developers. *GnssStatus API reference.* Official developer documentation. https://developer.android.com/reference/android/location/GnssStatus

[9] NOAA National Centers for Environmental Information. *Global Historical Climatology Network-Hourly (GHCNh).* Official dataset page and documentation. https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly ; https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf

[10] NOAA National Centers for Environmental Information and British Geological Survey. *World Magnetic Model 2025 (WMM2025 / WMMHR2025).* Official release and documentation. https://www.ncei.noaa.gov/products/world-magnetic-model

[11] NASA Earthdata. *GNSS data and products* (covering CDDIS-hosted GNSS holdings and products). Official data portal. https://www.earthdata.nasa.gov/data/space-geodesy-techniques/gnss

[12] Jet Propulsion Laboratory Solar System Dynamics Group. *Horizons System.* Official ephemeris service. https://ssd.jpl.nasa.gov/horizons/

[13] OpenCelliD. *Largest Open Database of Cell Towers & Geolocation.* Official service documentation. https://opencellid.org/

[14] Mozilla / Ichnaea project. *Retiring the Mozilla Location Service.* 2024 retirement notice and archive context. https://github.com/mozilla/ichnaea/issues/2065

[15] Nils Ole Tippenhauer, Christina Pöpper, Kasper Bonne Rasmussen, and Srdjan Čapkun. “On the Requirements for Successful GPS Spoofing Attacks.” In *Proceedings of the 18th ACM Conference on Computer and Communications Security (CCS)*, 2011. https://doi.org/10.1145/2046707.2046719

[16] Martin Azizyan, Ionut Constandache, and Romit Roy Choudhury. “SurroundSense: Mobile Phone Localization via Ambience Fingerprinting.” In *Proceedings of ACM MobiCom*, 2009. https://doi.org/10.1145/1614320.1614350

[17] Ron Levie, Çağkan Yapar, Gitta Kutyniok, and Giuseppe Caire. “RadioUNet: Fast Radio Map Estimation With Convolutional Neural Networks.” *IEEE Transactions on Wireless Communications*, 2021. https://doi.org/10.1109/TWC.2021.3054977

[18] Xiaopeng Zhao, Zhenlin An, Qingrui Pan, and Lei Yang. “NeRF2: Neural Radio-Frequency Radiance Fields.” In *Proceedings of ACM MobiCom*, 2023. https://doi.org/10.1145/3570361.3592527

[19] Haofan Lu, Christopher Vattheuer, Baharan Mirzasoleiman, and Omid Abari. “NeWRF: A Deep Learning Framework for Wireless Radiation Field Reconstruction and Channel Prediction.” In *Proceedings of ICML*, 2024. https://proceedings.mlr.press/v235/lu24j.html

[20] Kang Yang, Yuning Chen, and Wan Du. “GWRF: A Generalizable Wireless Radiance Field for Wireless Signal Propagation Modeling.” arXiv preprint arXiv:2502.05708, 2025. https://arxiv.org/abs/2502.05708

[21] Xiucheng Wang, Yuhao Pan, and Nan Cheng. “A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness.” arXiv preprint arXiv:2603.17499, 2026. https://arxiv.org/abs/2603.17499

[22] Stefanos Bakirtzis, Çağkan Yapar, Marco Fiore, Jie Zhang, and Ian Wassell. “Empowering Wireless Network Applications with Deep Learning-based Radio Propagation Models.” arXiv preprint arXiv:2408.12193, 2024. https://arxiv.org/abs/2408.12193

[23] Florian Tramèr, Fan Zhang, Ari Juels, Michael K. Reiter, and Thomas Ristenpart. “Stealing Machine Learning Models via Prediction APIs.” In *USENIX Security Symposium*, 2016. https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer

[24] Varun Chandrasekaran, Kedar Chaudhuri, Ilaria Giacomelli, Somesh Jha, and Songbai Yan. “Exploring Connections Between Active Learning and Model Extraction.” In *USENIX Security Symposium*, 2020. https://www.usenix.org/conference/usenixsecurity20/presentation/chandrasekaran

[25] Rémi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, et al. “Learning Skillful Medium-Range Global Weather Forecasting.” *Science*, 2023. https://doi.org/10.1126/science.adi2336

[26] Ian Price, Alvaro Sanchez-Gonzalez, Ferran Alet, et al. “GenCast: Diffusion-Based Ensemble Forecasting for Medium-Range Weather.” arXiv preprint arXiv:2312.15796, 2023. https://arxiv.org/abs/2312.15796

[27] Andrew F. Luo, Yilun Du, Michael J. Tarr, Joshua B. Tenenbaum, Antonio Torralba, and Chuang Gan. “Learning Neural Acoustic Fields.” In *Advances in Neural Information Processing Systems (NeurIPS)*, 2022. https://papers.nips.cc/paper_files/paper/2022/hash/151f4dfc71f025ae387e2d7a4ea1639b-Abstract-Conference.html

[28] Alexey Kurakin, Ian Goodfellow, and Samy Bengio. “Adversarial Examples in the Physical World.” In *ICLR Workshop*, 2017. https://arxiv.org/abs/1607.02533
