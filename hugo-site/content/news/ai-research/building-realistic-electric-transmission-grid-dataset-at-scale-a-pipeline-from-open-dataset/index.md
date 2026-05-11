---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-11T02:29:10.734490+00:00'
exported_at: '2026-05-11T02:29:14.852382+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/building-realistic-electric-transmission-grid-dataset-at-scale-a-pipeline-from-open-dataset
structured_data:
  about: []
  author: ''
  description: Microsoft Research is excited to release an open dataset of approximate
    transmission topology of the U.S. power grid derived from publicly available data.
    The ability to study transmission-level power grid behavior is essential for modern
    power systems research. Analyses of congestion, transmission expansion, demand...
  headline: 'Building realistic electric transmission grid dataset at scale: a pipeline
    from open dataset'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/building-realistic-electric-transmission-grid-dataset-at-scale-a-pipeline-from-open-dataset
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Building realistic electric transmission grid dataset at scale: a pipeline
  from open dataset'
updated_at: '2026-05-11T02:29:10.734490+00:00'
url_hash: dd078afc8b5ba1118ce645acf2b4f2a8f12b64c8
---

![Three minimalist white line icons on a blue-to-green gradient background: a connected globe with signal waves (left), a map location pin (center), and a lightbulb with rays (right), representing connectivity, location, and ideas.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/GridSage-BlogHeroFeature-1400x788-1-scaled.jpg)

## At a glance

* We construct geographically grounded, electrically coherent power grid models entirely from publicly available data and release a dataset spanning 48 U.S. states and multi-state interconnections.
* The models support AC optimal power flow (AC‑OPF) analysis, enabling physics-based study of congestion, capacity, and demand siting without restricted data.
* We demonstrate applications including transmission expansion potential, targeted line upgrades, and placement of large datacenter loads.

**Microsoft Research is excited to release an open dataset of approximate transmission topology of the U.S. power grid derived from publicly available data.**

The ability to study transmission-level power grid behavior is essential for modern power systems research. Analyses of congestion, transmission expansion, demand growth, and system resilience all depend on network models with realistic topology, electrical parameters, and geographic grounding.

In most of the world, including the United States, realistic transmission-level grid data is classified as critical infrastructure information and subject to strict access controls. These restrictions exist for good reasons, but the resulting lack of realistic grid models is increasingly exacerbating the challenges power systems face. Decisions about where new load can be added – and how additional transmission assets can be deployed to support it – are often gated behind lengthy and opaque processes that can take years. For researchers developing new tools and algorithms, access typically requires long approval cycles, strict non-redistribution agreements, or costly commercial licenses.

Spotlight: Microsoft research newsletter

## Microsoft Research Newsletter

Stay connected to the research community at Microsoft.

Opens in a new tab

As a result, many are left choosing between small “toy” networks with dozens of buses, or synthetic models that do not correspond to real infrastructure. This lack of realistic, shareable models is particularly limiting for data-driven and AI-based approaches, which require large volumes of physically plausible grid data for training and evaluation methods for grid analysis and planning.

Against this backdrop, a natural question arises:

**Can we meaningfully understand how the U.S. power grid responds to modern stresses – and facilitate the development of actionable solutions for the system – using only open data?**

In this work, we introduce an open-data-derived pipeline for constructing large-scale, transmission-level power grid models that realistically approximate existing networks without relying on proprietary or restricted datasets. We provide an open dataset derived from this process, consisting of transmission-level models spanning 48 U.S. states as well as interconnection-scale networks, ranging in size from small systems with as few as 11 buses to the full Eastern Interconnection grid connecting 21,697 buses. The pipeline has been validated across the continental United States, where sufficient open geographic, energy, and demographic data are available, and is designed to generalize to other regions with comparable public data sources.

Using only publicly accessible datasets, the pipeline produces geographically grounded, electrically coherent transmission models at state, multi-state, and interconnection scales. These models preserve the geographic structure of transmission corridors, substations, and generators inferred from open data, while explicitly accounting for uncertainty where detailed operational parameters are unavailable through transparent feasibility reporting.

Importantly, these are not toy networks or abstract benchmarks. The resulting models support alternating current optimal power flow (AC-OPF) analysis across a wide range of scales, enabling physics-based investigation of questions such as where transmission capacity is physically constrained; where new demand can be absorbed; and how infrastructure changes propagate through realistic network layouts – using only open data.

In this post, we describe the approach at a high level and highlight the system level questions it enables.

## How the pipeline works

The pipeline turns publicly available geographic and energy data into transmission-level grid models that are geographically grounded and usable for power flow analysis.

The starting point is
[OpenStreetMap
(opens in new tab)](https://www.openstreetmap.org/)
, which encodes the physical layout of transmission corridors, substations, and power plants. This geographic skeleton is then augmented with open datasets describing generation capacity, fuel mix, demand, and operational boundaries (including U.S. EIA energy statistics and U.S. Census data), allowing the models to go beyond topology and represent how electricity is produced and consumed.

The key test is solvability. In power system analysis, solving optimal power flow (OPF) problems is a practical check on whether a network description is electrically coherent and practically relevant. OPF determines how generation can be dispatched to meet demand while respecting physical constraints such as transmission line capacities, voltage limits, and generator capabilities. Many inferred or synthetic networks fail this test outright: the topology may appear roughly correct, but other important engineering parameters are not.

Crucially, this approach moves beyond small benchmark or “toy” networks. In particular, we solve AC-OPF across the entire Eastern Interconnection, spanning 36 states and more than 20,000 buses, derived exclusively from public data sources. This demonstrates that open-data-derived models can produce convergent AC-OPF solutions at a continental scale.

To be clear, these models are not exact replicas of the operational grid, nor are they intended for market forecasting or real-time operational decision making by power balancing authorities. Electrical parameters are estimated from standard engineering references, parallel circuits are approximated rather than exhaustively enumerated, and demand is allocated using public proxies derived from open data.

The goal is to produce structurally and electrically realistic models that preserve geographic structure and scale from individual states to large multi-region systems using only open data. Full methodological details, validation results, and limitations are described in a
[companion research paper.](https://www.microsoft.com/en-us/research/publication/building-power-grid-models-from-open-data-a-complete-pipeline-from-openstreetmap-to-optimal-power-flow/)

## Why this matters for today’s energy challenges

Access to solvable, geographically grounded grid models unlocks questions that have become increasingly urgent as the energy system evolves, driven by large-scale datacenters, AI workloads, renewable generation, and extreme weather events. We illustrate these capabilities with concrete analyses on models derived from our pipeline.

### Where can new transmission physically fit?

Before asking how much new capacity the grid needs, planners must first ask where more wires are even possible. Transmission corridors have a physical limit on how many circuits they can carry: each circuit requires three conductors, and most tower structures accommodate one to three circuits (three to nine conductors). Beyond that, adding capacity typically requires acquiring entirely new rights-of-way – which is expensive, legally complex, and often politically infeasible in urban areas.

Because our models preserve the geographic structure of real transmission corridors from OpenStreetMap, we can count the number of parallel circuits along each path and visualize where the grid is already physically saturated.

![Transmission corridor density across the contiguous United States, showing most corridors carry a single circuit with denser multi-circuit regions near major cities. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/fig1a_continental_us_circuit_density-1024x545.png)

![Zoomed view of California showing dense multi-circuit corridors near urban areas and lower-density radial lines in rural regions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/fig1b_continental_us_circuit_density_california-scaled.png)


*Figure 1. Across the contiguous United States (top), the model identifies 31,488 distinct transmission corridors. The overwhelming majority (27,506) carry a single circuit (green), making parallel lines easier. The roughly 4,000 corridors in orange through red already carry two or more parallel circuits, with the densest packing ten circuits (30 conductors) onto a single path. Zooming into California (bottom), the pattern becomes more discernable. The red corridor north of Sacramento and the orange clusters around the Bay Area and LA basin show where the grid is already physically dense, while the long green radials across the Mojave and into Nevada still have room to grow.*

Identifying where the grid is physically boxed in, regardless of generation or demand, is not an optimization problem. It is a spatial feasibility question that geographically grounded models are uniquely positioned to answer.

### What if we add capacity where it is needed most?

In dense urban areas, adding new traditional transmission lines is often impractical. The combination of tightly packed buildings, roadways, and complex underground infrastructure leaves little room to establish rights-of-way for high-voltage lines. Alternative power‑transmission solutions are sometimes explored to support urban grid expansion. For example, high-temperature superconducting (HTS) cable systems offer an order-of-magnitude higher ampacity for a given cross-section, enabling the transfer of large amounts of power at lower voltages and simplifying permitting requirements.

Short point-to-point superconducting power links have already been demonstrated in U.S. cities: Columbus, Ohio, Albany, New York, Long Island, New York (decommissioned), and Chicago (operational).

To explore what such connections might accomplish, we modeled two hypothetical HTS links in the Massachusetts grid, each connecting a substation northwest of Boston to load centers closer to the city. We then re-solved AC-OPF and compared the results to the unmodified baseline.

![Baseline transmission line loading in Massachusetts showing one line exceeding its thermal limit and others operating near capacity. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/fig2a_hts_baseline_congestion_corridor-1024x565.png)

![Transmission line loading after adding two superconducting links, with no overloads. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/fig2b_hts_scenario_congestion_corridor-1024x565.png)


*Figure 2. In the baseline (top), one transmission line exceeds its thermal rating (≥100%, dark red) and two more operate above 90%. After adding two HTS links (bottom, dashed lines), every line in the network drops below 90% loading. The energy price falls 42%, from $22.7/MWh to $13.1/MWh, as generation that was previously bottlenecked behind constrained corridors becomes deliverable.*

This is precisely the kind of insight that publicly available price data cannot provide. Wholesale electricity prices reflect whether congestion exists, but not how close the system is to congestion nor how power flows change when new assets are added. A line operating at 95% of its thermal limit and one at 50% look identical in market data – until one of them reaches capacity. Physics-based models expose that margin directly, making it possible to evaluate interventions before they are built.

### Where should new demand go?

Rapid growth in electricity demand raises a question that existing market signals answer poorly: where on the network can new consumption be absorbed without triggering congestion?

Wholesale electricity prices reflect marginal generation costs, current congestion patterns in the transmission grid, and transmission losses, which are typically small – but they do not capture how close the system is to its limits. Siting decisions based solely on price therefore miss the physical margin that determines whether new demand can be served without infrastructure upgrades.

To illustrate this, we placed the same hypothetical 500 MW datacenter at two locations in the Maryland grid and re-solved AC-OPF for each (locations were chosen arbitrarily and do not reflect Microsoft’s datacenter portfolio or expansion plans). The two sites are plausible alternatives from a market perspective, with similar population density, comparable electricity prices, and proximity to major load centers:

* Site A (Baltimore area): a substation in the Baltimore metropolitan region, near an existing generation complex and dense transmission infrastructure
* Site B (Washington, DC suburbs): a substation in Montgomery County, serving a similarly dense suburban area within the Washington–Baltimore corridor

Despite these similarities, the physical outcomes differ. Adding the datacenter at Site A pushes a nearby transmission line into thermal overload, while placing the same load at Site B is absorbed by the existing network without violating line limits. The two sites are less than 50 miles apart, yet one would require transmission reinforcement and the other would not.

![Datacenter placement near Baltimore causing a transmission line to exceed its thermal limit. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/fig3a_dc_siteA_congestion_md-scaled.png)

![Datacenter placement near Washington DC that is absorbed without violating transmission line limits. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/fig3b_dc_siteB_congestion_md-1024x565.png)


*Figure 3. Placing the datacenter near Baltimore (top) pushes one transmission line into overload (≥100%) and raises the energy price from $24.6/MWh (baseline) to $28.6/MWh (+16.1%). The same load placed near the DC suburbs (bottom) keeps all lines below 95% and raises the price to $26.4/MWh (+7.4%). The Baltimore site yields a price $2.1/MWh higher – a difference that, across the 500 MW load, amounts to roughly $9,100 per hour or ~$80 million per year.*

This distinction – largely invisible in price data – emerges directly from a more direct first-principle transmission-level power flow analysis. It highlights why geographically grounded, physics-based models are necessary for demand-siting decisions in a stressed grid.

## Looking ahead

This work shows that it is possible to study transmission-level grid behavior at realistic scales without access to restricted infrastructure data. By grounding models in real geography and making uncertainty explicit, open-data-derived grids can support analyses that are difficult or impossible with small benchmarks or purely synthetic networks.

While the examples here focus on the United States, the approach generalizes to other regions where comparable open data is available. More broadly, we see this capability as an enabling layer: a way to improve the study of congestion, feasibility, and system stress – whether for planning studies, scenario analysis, or data-driven methods that require realistic grid structure.

We are releasing an open dataset of grid models spanning 48 U.S. states and six multi-state interconnections, ranging from small systems with tens of buses to continental-scale networks. All models can be solved under AC-OPF, with controlled relaxations applied when necessary to account for uncertainty in open data inputs. These models are solved for both peak and off-peak demand conditions, enabling consistent analysis across a range of operating scenarios.

This post is the first in a two-part series. In the second post, we introduce GridSFM, a learning-based AC-OPF surrogate trained on these grid models. We show how it predicts a full AC operating point in milliseconds, classifies feasibility for fast screening at planning scale, and serves as a warm-start seed that accelerates downstream numerical solvers.

Opens in a new tab