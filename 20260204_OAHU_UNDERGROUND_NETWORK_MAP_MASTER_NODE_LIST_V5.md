# OAHU UNDERGROUND — NETWORK MAP: MASTER NODE LIST (v5)

## Changes from v1

1. **Family tree corrected.** Janice Luke Loo is Warren Luke's *sister*, not daughter. Both are children of K.J. Luke (founder, Hawaii National Bank). Wilson Loo is Warren's brother-in-law, not son-in-law. K.J. Luke added as progenitor node BF-0.
2. **Edge type split.** Solid line now distinguishes governance/board (──) from employment/role (──▶). Prevents readers from conflating trustee power with staff positions.
3. **BF-4 absorbed into BF-2 description.** Luke-affiliated entities (K.J.L. Associates, K.J.L. Inc., Loyalty Enterprises, Hawaii National Bancshares) are listed as disclosed interests in Wilson Loo's filings rather than a separate node. Net result with BF-0 addition: 28 nodes.
4. **Financial edge overload fixed.** New `asset_origin` edge type (╌╌) for historical acquisitions, distinct from `financial_disclosed` (┄┄) for current Ethics Commission filings.
5. **BF-2 semantic precision.** "Luke-affiliated entities disclosed alongside HNB-related interests" — no corporate parentage asserted.
6. **OV-1 role labels.** "Served within oversight ecosystem" → "Commission member" with verification flag.
7. **NP-7 reclassified as Cluster.** K.J. Luke Foundation and Luke Center may be distinct entities; grouped by namesake.

## Changes in v4

8. **JD-3 canonical name standardized.** "Hawaiʻi State Ethics Commission (Financial Disclosure Program)" as printed node label. "Ethics Commission filing" as Source_Code shorthand throughout.
9. **OV-1 uncertainty rendering convention.** "Served (title/date TBD)" as on-map label until verified. Exact title/date moves to Evidence Locker once confirmed. No greyed edges — transparency over hedging.
10. **Complaint arrow (▸) visual distinction.** Distinguished from employment arrow (──▶) in style guide: complaint arrows render in a distinct weight or color. Convention documented in edge legend.
11. **Issue 1 edge-table subset appended.** Drawing spec for center spread — only rows where both endpoints are Issue 1 nodes.

## Changes in v5

12. **Administrative edge type added (⋯▷).** `JD-1 → JD-3` was previously `Edge_Type = filing`, but the legend reserved **▸** for "Complaint / filing." This created an ambiguity: a financial disclosure filing and a misconduct complaint both rendering as the same arrow type would invite misreading. **Fix:** new `administrative` edge type (⋯▷ — thin dotted line with small open arrowhead) for routine regulatory filings (financial disclosures, annual reports). **▸** is now reserved exclusively for adversarial filings (complaints to CJC, ODC, FBI). Edge legend, production edge table, and Issue 1 subset updated accordingly.
13. **Research pack appended.** Public-record source list (web-verified) and records-to-pull checklist for each issue, aligned to bible + node/edge system. Source_Code values in edge tables now traceable to specific URLs.

---

## Node ID Scheme

Prefix = domain. Number = sequence within domain. Stable across all issues — once assigned, never changes.

| Prefix | Domain |
|--------|--------|
| BF | Banking & Finance |
| RE | Real Estate / Land |
| ED | Education |
| NP | Nonprofit / Philanthropy |
| JD | Judiciary / Legal |
| OV | Oversight |
| ME | Media |
| PO | Political / Government |

People are nodes. They carry the prefix of their primary domain but connect across domains — that's the point.

---

## ISSUE 1 NODES (The Map)

### Banking & Finance

**BF-0 — K.J. Luke (deceased, Nov 2000)**
Type: Person (founder / progenitor)
Role: "Hawaii's millionaire schoolteacher." Founded Hawaii National Bank (1960). Acquired Damon Tract with Clarence T.C. Ching (1956). Built the Luke real estate and banking empire. Father of Warren Luke (BF-1) and Janice Luke Loo (JD-2).
First appears: Issue 1 (cold open)
Key edges: BF-1 (son); JD-2 (daughter); BF-2 (founded); RE-1 (acquired, 1956 — historical origin, not current disclosure); NP-7 (K.J. Luke Foundation named after him)

**BF-1 — Warren K.K. Luke**
Type: Person (banker / civic leader)
Role: Chairman and CEO, Hawaii National Bank. Federal Reserve Bank of San Francisco, Hawaii branch director. Dozens of board positions spanning banking, education, philanthropy, civic governance (Punahou, Red Cross, Pacific Forum, etc.)
First appears: Issue 1
Key edges: BF-0 (son of); JD-2 (sister); JD-1 (brother-in-law); BF-2 (chairman/CEO); BF-3 (director); ED-1 (trustee); NP-1, NP-2, NP-3 (board seats); ME-2 (concurrent Punahou trustee, 2007–2019); PO-1 (father of Cathy Luke)

**BF-2 — Hawaii National Bank**
Type: Institution
Role: Only nationally chartered bank founded by a local Chinese-American family in Hawaii. Luke family flagship. Founded 1960.
Luke-affiliated entities disclosed alongside HNB-related interests in JD-1's financial filings: K.J.L. Associates (industrial/commercial property, >$1M), K.J.L. Inc. (commercial property, 20,885 shares), Loyalty Enterprises Ltd. (property rental), Hawaii National Bancshares Inc. (holding company, 67 shares combined). These entities are related to the Luke family business structure; their exact corporate relationship to HNB is not asserted here. Total disclosed Luke-family interests held by JD-1: >$2M.
First appears: Issue 1
Key edges: BF-0 (founded by); BF-1 (chairman/CEO); RE-1 (founding land); JD-1 (disclosed holdings >$2M); ME-3 (former employee)

**BF-3 — Federal Reserve Bank of San Francisco (Hawaii branch)**
Type: Institution
Role: Federal Reserve regional branch.
First appears: Issue 1
Key edges: BF-1 (director)

### Real Estate / Land

**RE-1 — Damon Tract**
Type: Property
Role: 233-acre tract near Honolulu airport. Acquired by K.J. Luke and Clarence T.C. Ching, 1956, for $4.5M ($100K down). Cornerstone of Luke family wealth. Acquisition was controversial — sparked protests re: Hawaiian Aeronautics Commission interests.
First appears: Issue 1 (cold open)
Key edges: BF-0 (acquired by); BF-2 (led to founding of)

### Education

**ED-1 — Punahou School**
Type: Institution
Role: Hawaii's most elite private school. Board of trustees = apex social network node.
First appears: Issue 1
Key edges: BF-1 (trustee); ME-2 (trustee, 2007–2019, concurrent with BF-1); JD-2 (alumna; retired English teacher)

### Nonprofit / Philanthropy

**NP-1 — American Red Cross (Hawaii chapter)**
Type: Institution
First appears: Issue 1
Key edges: BF-1 ── (board)

**NP-2 — Pacific Forum**
Type: Institution (think tank / policy)
First appears: Issue 1
Key edges: BF-1 ── (board)

**NP-3 — REHAB Hospital of the Pacific / REHAB Hospital Foundation**
Type: Institution cluster
Role: Hospital and associated foundation. Janice is Vice-Chair of Foundation. Wilson is Director of Hospital. Both are 25–29 year supporters per donor acknowledgments.
First appears: Issue 1
Key edges: JD-2 ── (board, since 1990; Foundation Vice-Chair); JD-1 ── (Director)

**NP-8 — Mamoru and Aiko Takitani Foundation**
Type: Institution
Role: Scholarship/education foundation. Janice is President. Wilson is Director ($1,000–$10,000 compensation).
First appears: Issue 1
Key edges: JD-2 ── (President); JD-1 ── (Director, compensated)

### Judiciary / Legal

**JD-1 — Wilson M.N. Loo**
Type: Person (judge / attorney)
Role: Per diem judge since 1995. Attorney in private practice (simultaneous). Son-in-law of BF-0 (K.J. Luke). Brother-in-law of BF-1 (Warren Luke).
First appears: Issue 1
Key edges: BF-0 (son-in-law); BF-1 (brother-in-law); JD-2 (spouse); BF-2 (disclosed financial holdings >$2M in Luke entities); JD-3 (financial disclosures filed with — administrative); OV-1 (served — title/date TBD; exact role to be confirmed against Commission records and published in Evidence Locker upon verification); NP-3, NP-8 (board roles); JD-5 (Dec 2, 2022 hearing — Issue 4)

**JD-2 — Janice Luke Loo**
Type: Person (bridge node)
Role: Daughter of K.J. Luke (BF-0). Sister of Warren Luke (BF-1). Spouse of Wilson Loo (JD-1). Retired Punahou English teacher. Stanford Education / Columbia Klingenstein Fellow. Extensive philanthropic board positions.
First appears: Issue 1
Key edges: BF-0 (daughter); BF-1 (sister); JD-1 (spouse); ED-1 (alumna, retired teacher); NP-3 (board, Vice-Chair of Foundation); NP-8 (President); NP-7 (K.J. Luke Foundation); OV-1 (served — title/date TBD; exact role to be confirmed against Commission records and published in Evidence Locker upon verification)

**JD-3 — Hawaiʻi State Ethics Commission (Financial Disclosure Program)**
Type: Institution
Role: Repository for judicial financial disclosure filings. Wilson Loo's annual disclosures filed here. Canonical source for disclosed financial interests.
First appears: Issue 1 (Evidence Locker source document)
Key edges: JD-1 (filer — administrative edge); BF-2 (disclosed interests)

---

## ISSUE 2 NODES (The Blind Spots)

### Oversight

**OV-1 — Commission on Judicial Conduct**
Type: Institution
Role: Body that polices judicial conduct in Hawaii. Confidential proceedings. 90-day jurisdictional window. 3+ year reporting lag.
First appears: Issue 1 (mentioned); Issue 2 (detailed)
Key edges: JD-1 (served — title/date TBD), JD-2 (served — title/date TBD); OV-2 (90-day rule); JD-5 (complaint filed re: Dec 2 incident — Issue 4)

**OV-2 — 90-Day Jurisdictional Window**
Type: Rule / structural mechanism (rendered on map as a constraint annotation on OV-1)
Role: Commission rule: complaints filed after 90 days cannot be acted upon regardless of merit.
First appears: Issue 2
Key edges: OV-1 (rule of); JD-5 (applied to — Issue 4)

### Judiciary / Legal (additions)

**JD-4 — Per Diem Judge System**
Type: Structural mechanism (rendered on map as annotation on judiciary cluster)
Role: Attorneys serve as judges part-time, return to private practice. Structural conflict of interest by design.
First appears: Issue 2
Key edges: JD-1 (operates within); JD-6 (operates within — Issue 4)

**JD-5 — Dec 2, 2022 Hearing**
Type: Event node
Role: The injunction hearing. Audio-only record. Sealed case. Central incident of the series.
First appears: Issue 1 (prologue teaser); Issue 4 (full treatment)
Key edges: JD-1 (presiding); OV-1 (complaint filed); OV-2 (90-day rule applied)

*Appellate record references (not nodes — cited in body text):*
- Lockey case (published opinion)
- Rego case (published opinion)
- Noga case (published opinion)

---

## ISSUE 3 NODES (The Zone of Politeness)

### Media

**ME-1 — Honolulu Civil Beat**
Type: Institution (investigative newsroom)
Role: Hawaii's primary investigative journalism outlet. Founded by ME-2. Maintains Loo financial disclosures in public database. Received dossier early 2025 — interest, then silence.
First appears: Issue 3
Key edges: ME-2 (founder); ME-3 ──▶ (contributor); BF-1 ┄┄ (Luke family on donor list); ED-1 (Punahou trustee overlap between ME-2 and BF-1); JD-3 (hosts disclosure database but produces no investigation)

**ME-2 — Pierre Omidyar**
Type: Person (media / philanthropy)
Role: eBay founder. Founded Civil Beat. Punahou trustee 2007–2019, concurrent with BF-1.
First appears: Issue 3
Key edges: ME-1 (founder); ED-1 ── (trustee, overlapping with BF-1); NP-5 (Omidyar ʻOhana Fund)

**ME-3 — Ryan Ozawa**
Type: Person (bridge node)
Role: Former Hawaii National Bank information security officer. Current Civil Beat contributor.
First appears: Issue 3
Key edges: BF-2 ──▶ (former ISO — employment); ME-1 ──▶ (contributor — employment)

### Nonprofit / Philanthropy (additions)

**NP-4 — Hawaii Leadership Forum**
Type: Institution
First appears: Issue 3
Key edges: PO-1 (Cathy Luke involvement); NP-5 ●●● (governance chain)

**NP-5 — Omidyar ʻOhana Fund**
Type: Institution (foundation)
First appears: Issue 3
Key edges: ME-2 (Omidyar); NP-4 ●●● (governance chain with Hawaii Leadership Forum)

**NP-6 — Kōkua Hawaii Foundation**
Type: Institution
Role: North Shore conservation network.
First appears: Issue 3
Key edges: NP-7 (Luke Center connection)

**NP-7 — K.J. Luke–Named Institutions (Foundation + Luke Center)**
Type: Cluster (may be distinct entities; grouped here by namesake association)
Role: Named after K.J. Luke (BF-0). Educational and community focus. Exact corporate relationship between Foundation and Center not asserted.
First appears: Issue 3
Key edges: BF-0 (namesake); BF-1 (Luke family); JD-2 (board); NP-6 (Kōkua connection)

### Political / Government

**PO-1 — Cathy Luke**
Type: Person (political)
Role: State legislator. Daughter of Warren Luke (BF-1).
First appears: Issue 3
Key edges: BF-1 (daughter); NP-4 (Hawaii Leadership Forum); NP-5 ●●● (governance chain)

---

## ISSUE 4 NODES (December Second)

### Judiciary / Legal (additions)

**JD-6 — Audrey Stanley**
Type: Person (attorney / per diem judge)
Role: Former public defender. Had knowledge of a specific threat against the author. Relayed a coercive offer. Now serves as per diem judge.
First appears: Issue 4
Key edges: JD-4 (now per diem judge); JD-5 (connected to Dec 2 events); OV-3 (subject of draft ODC complaint — not yet filed)

### Oversight (additions)

**OV-3 — Office of Disciplinary Counsel (ODC)**
Type: Institution
Role: Handles attorney misconduct complaints.
First appears: Issue 4 (mentioned); Issue 5 (detailed)
Key edges: JD-6 (Stanley is subject of draft complaint — not yet filed)

---

## ISSUE 5 NODES (The Record)

### Government / Federal

**PO-2 — FBI**
Type: Institution
Role: Federal complaint filed July 2025.
First appears: Issue 5
Key edges: JD-5 (complaint filed with FBI re: Dec 2 incident and related conduct)

*No new network nodes in Issue 5. The issue synthesizes the existing map and presents the full evidence file.*

---

## COMPLETE NODE REGISTRY

| ID | Name | Type | Domain | Introduced |
|------|------|------|--------|------------|
| BF-0 | K.J. Luke (d. 2000) | Person | Banking | Issue 1 |
| BF-1 | Warren K.K. Luke | Person | Banking | Issue 1 |
| BF-2 | Hawaii National Bank | Institution | Banking | Issue 1 |
| BF-3 | Fed Reserve (Hawaii branch) | Institution | Banking | Issue 1 |
| RE-1 | Damon Tract | Property | Real Estate | Issue 1 |
| ED-1 | Punahou School | Institution | Education | Issue 1 |
| NP-1 | American Red Cross (Hawaii) | Institution | Nonprofit | Issue 1 |
| NP-2 | Pacific Forum | Institution | Nonprofit | Issue 1 |
| NP-3 | REHAB Hospital / Foundation | Cluster | Nonprofit | Issue 1 |
| NP-8 | Takitani Foundation | Institution | Nonprofit | Issue 1 |
| JD-1 | Wilson M.N. Loo | Person | Judiciary | Issue 1 |
| JD-2 | Janice Luke Loo | Person | Judiciary | Issue 1 |
| JD-3 | Hawaiʻi State Ethics Commission | Institution | Judiciary | Issue 1 |
| OV-1 | Commission on Judicial Conduct | Institution | Oversight | Issue 2 |
| OV-2 | 90-Day Jurisdictional Window | Rule | Oversight | Issue 2 |
| JD-4 | Per Diem Judge System | Structure | Judiciary | Issue 2 |
| JD-5 | Dec 2, 2022 Hearing | Event | Judiciary | Issue 1* |
| ME-1 | Honolulu Civil Beat | Institution | Media | Issue 3 |
| ME-2 | Pierre Omidyar | Person | Media | Issue 3 |
| ME-3 | Ryan Ozawa | Person | Media | Issue 3 |
| NP-4 | Hawaii Leadership Forum | Institution | Nonprofit | Issue 3 |
| NP-5 | Omidyar ʻOhana Fund | Institution | Nonprofit | Issue 3 |
| NP-6 | Kōkua Hawaii Foundation | Institution | Nonprofit | Issue 3 |
| NP-7 | K.J. Luke–Named Institutions | Cluster | Nonprofit | Issue 3 |
| PO-1 | Cathy Luke | Person | Political | Issue 3 |
| JD-6 | Audrey Stanley | Person | Judiciary | Issue 4 |
| OV-3 | Office of Disciplinary Counsel | Institution | Oversight | Issue 4 |
| PO-2 | FBI | Institution | Government | Issue 5 |

28 nodes total. *JD-5 teased in Issue 1 prologue, fully introduced Issue 4.

---

## EDGE TYPES (legend for map connections)

| Edge Symbol | Relationship Type | Example |
|-------------|-------------------|---------|
| ── (solid line) | Governance / board / trustee | BF-1 ── ED-1 (Punahou trustee) |
| ──▶ (solid arrow) | Employment / staff role | ME-3 ──▶ BF-2 (former ISO) |
| ═══ (double line) | Family: parent–child | BF-0 ═══ BF-1 (father–son) |
| ═══ (double line) | Family: sibling | BF-1 ═══ JD-2 (brother–sister) |
| ═══ (double line) | Family: spouse | JD-1 ═══ JD-2 (married) |
| ┄┄ (dashed) | Financial interest (current, disclosed) | JD-1 ┄┄ BF-2 (>$2M in Luke holdings) |
| ┄┄ (dashed, labeled) | Donor relationship | BF-1 ┄┄ ME-1 (Luke family donor) |
| ╌╌ (short dash) | Asset origin / historical acquisition | BF-0 ╌╌ RE-1 (acquired, 1956) |
| ●●● (dotted) | Governance chain | NP-4 ●●● NP-5 (HLF → Omidyar fund) |
| ⋯▷ (thin dotted, open arrow) | Administrative filing | JD-1 ⋯▷ JD-3 (financial disclosure filer) |
| ▸ (arrow, distinct weight/color) | Complaint / adversarial filing | JD-5 ▸ OV-1 (complaint filed) |

**Note on financial edges:** Dashed (┄┄) edges represent *current disclosed financial interests* sourced from Ethics Commission filings. Short-dash (╌╌) edges represent *historical asset origins* — land acquisitions, founding events — that explain how the network was built but do not assert current holdings. These are visually and semantically distinct on the map.

**Note on arrow types:** Three arrow types exist and must be visually distinguishable:
- **Employment arrows (──▶):** Same line weight as governance edges. Direction indicates "employed by."
- **Administrative arrows (⋯▷):** Thin dotted line with small open arrowhead. Used for routine regulatory filings — financial disclosures, annual reports — where the filer submits to a repository. Not adversarial. Direction indicates "files with."
- **Complaint arrows (▸):** Lighter weight or distinct color (e.g., red or grey). Used exclusively for adversarial filings — misconduct complaints, federal complaints. Direction indicates "complaint filed against/with."

The graphic designer should ensure these three arrow types cannot be confused at a glance. The critical distinction: **⋯▷** (administrative) = "I submit my paperwork here"; **▸** (complaint) = "I am alleging misconduct here."

**Family edge labels** (printed alongside double lines to distinguish relationship type):

| Label | Meaning |
|-------|---------|
| P–C | Parent–child |
| SIB | Sibling |
| SP | Spouse |

---

## FAMILY TREE (reference — not printed on map, used for internal verification)

```
K.J. Luke (BF-0, d. 2000)
├── Warren K.K. Luke (BF-1) — Chairman/CEO, Hawaii National Bank
│   └── Cathy Luke (PO-1) — State legislator
└── Janice Luke Loo (JD-2) — née Luke; Punahou teacher, philanthropist
    ═══ married ═══ Wilson M.N. Loo (JD-1) — per diem judge, attorney
```

Wilson Loo is BF-0's son-in-law and BF-1's brother-in-law.
Cathy Luke is JD-2's niece.

---

## MAP BUILD SEQUENCE (what the reader sees each issue)

**Issue 1:** BF-0, BF-1, BF-2, BF-3, RE-1, ED-1, NP-1, NP-2, NP-3, NP-8, JD-1, JD-2, JD-3
→ The Luke dynasty (progenitor → bank → boards) and the Loo judicial node. Family edges: BF-0 ═══ BF-1 (parent–child), BF-0 ═══ JD-2 (parent–child), BF-1 ═══ JD-2 (siblings), JD-1 ═══ JD-2 (spouses). Financial edge: JD-1 ┄┄ BF-2 (disclosed holdings). Administrative edge: JD-1 ⋯▷ JD-3 (disclosure filer). Reader sees two domains — banking/philanthropy and judiciary — joined by marriage and money.

**Issue 2:** Add OV-1, OV-2, JD-4
→ Oversight node appears. Reader sees that the Loo positions touch the body that polices judges. Structural mechanism annotations (90-day window, per diem system) explain *how* accountability gaps work.

**Issue 3:** Add ME-1, ME-2, ME-3, NP-4, NP-5, NP-6, NP-7, PO-1
→ Media cluster appears. Punahou edge now bridges banking and media (BF-1 ── ED-1 ── ME-2, concurrent trustees). Employment arrow: ME-3 ──▶ BF-2 (former bank employee now media contributor). Donor edge: BF-1 ┄┄ ME-1. Map connects banking → judiciary → oversight → media. Cathy Luke adds a political node connecting to philanthropy chain.

**Issue 4:** Add JD-5, JD-6, OV-3
→ Courtroom event node anchored inside the structure. Stanley enters the per diem system. ODC enters as potential complaint recipient. The map now has a specific incident surrounded by all the enabling conditions. Complaint arrows (▸) appear for the first time: JD-5 ▸ OV-1 (complaint filed with CJC), OV-3 ⋯ JD-6 (Stanley subject of draft ODC complaint — not yet filed).

**Issue 5:** Add PO-2. All edges visible. Full map.
→ FBI node. Complaint arrow: JD-5 ▸ PO-2 (complaint filed with FBI). The reader has built the complete network one issue at a time. Final spread shows everything. The Minimum Clarifying Record Set (from the series bible) can be cross-referenced to specific nodes and edges on the map.

---

## PRODUCTION EDGE TABLE (internal CSV schema for consistent redrawing)

Maintain as a spreadsheet. One row per edge. The map can be redrawn every issue without drift.

| From_ID | To_ID | Edge_Type | Role_Label | Date_Range | Source_Code |
|---------|-------|-----------|------------|------------|-------------|
| BF-0 | BF-1 | family_parent_child | father–son | — | obituary, bank history |
| BF-0 | JD-2 | family_parent_child | father–daughter | — | obituary, bank history |
| BF-0 | BF-2 | governance | founder | 1960 | bank founding records |
| BF-0 | RE-1 | asset_origin | acquired | 1956 | land records, news archive |
| BF-1 | JD-2 | family_sibling | brother–sister | — | public bios |
| BF-1 | BF-2 | employment | chairman/CEO | current | bank filings |
| BF-1 | BF-3 | governance | director | — | Fed roster |
| BF-1 | ED-1 | governance | trustee | incl. 2007–2019 | Punahou trustee roster |
| BF-1 | NP-1 | governance | board | — | org roster |
| BF-1 | NP-2 | governance | board | — | org roster |
| BF-1 | ME-1 | donor | family donor | — | Civil Beat donor list |
| BF-1 | PO-1 | family_parent_child | father–daughter | — | public record |
| JD-1 | JD-2 | family_spouse | married | — | public record |
| JD-1 | BF-2 | financial_disclosed | >$2M holdings | per disclosure | Ethics Commission filing |
| JD-1 | JD-3 | administrative | disclosure filer | annual | Ethics Commission filing |
| JD-1 | NP-3 | governance | director | — | REHAB records |
| JD-1 | NP-8 | governance | director (compensated) | — | Takitani records |
| JD-1 | OV-1 | governance | served (title/date TBD) | — | Commission records (TBV) |
| JD-2 | ED-1 | employment | teacher (retired) | — | Punahou records |
| JD-2 | NP-3 | governance | board; Foundation Vice-Chair | since 1990 | REHAB records |
| JD-2 | NP-8 | governance | president | — | Takitani records |
| JD-2 | NP-7 | governance | board | — | foundation records |
| JD-2 | OV-1 | governance | served (title/date TBD) | — | Commission records (TBV) |
| ME-2 | ME-1 | governance | founder | — | Civil Beat records |
| ME-2 | ED-1 | governance | trustee | 2007–2019 | Punahou trustee roster |
| ME-2 | NP-5 | governance | — | — | foundation records |
| ME-3 | BF-2 | employment | former ISO | — | UH Alumni Q&A |
| ME-3 | ME-1 | employment | contributor | current | Civil Beat bylines |
| PO-1 | NP-4 | governance | — | — | org records |
| NP-4 | NP-5 | governance_chain | HLF → Omidyar fund | — | Omidyar Fellows / ProPublica 990 |
| NP-7 | NP-6 | governance_chain | Luke Center → Kōkua | — | Kōkua team page |
| JD-5 | OV-1 | complaint | filed | post-Dec 2022 | Commission correspondence |
| OV-2 | JD-5 | rule_applied | 90-day invoked | — | Commission response |
| JD-6 | JD-4 | employment | per diem judge | current | judiciary roster |
| JD-5 | PO-2 | complaint | complaint filed with FBI | July 2025 | FBI receipt |
| OV-3 | JD-6 | complaint_target | subject of draft complaint (not yet filed) | — | ODC filing (draft) |

---

## ISSUE 1 EDGE-TABLE SUBSET (center spread drawing spec)

Only rows where **both endpoints** are Issue 1 nodes: BF-0, BF-1, BF-2, BF-3, RE-1, ED-1, NP-1, NP-2, NP-3, NP-8, JD-1, JD-2, JD-3.

This subset is the complete drawing spec for the Issue 1 center spread. No edges outside this set should appear on the Issue 1 map.

| From_ID | To_ID | Edge_Type | Role_Label | On-Map Label | Source_Code |
|---------|-------|-----------|------------|--------------|-------------|
| BF-0 | BF-1 | family_parent_child | father–son | P–C | obituary, bank history |
| BF-0 | JD-2 | family_parent_child | father–daughter | P–C | obituary, bank history |
| BF-0 | BF-2 | governance | founder | "founded (1960)" | bank founding records |
| BF-0 | RE-1 | asset_origin | acquired | "acquired (1956)" | land records, news archive |
| BF-1 | JD-2 | family_sibling | brother–sister | SIB | public bios |
| BF-1 | BF-2 | employment | chairman/CEO | "Chairman/CEO" | bank filings |
| BF-1 | BF-3 | governance | director | "Director" | Fed roster |
| BF-1 | ED-1 | governance | trustee | "Trustee" | Punahou trustee roster |
| BF-1 | NP-1 | governance | board | "Board" | org roster |
| BF-1 | NP-2 | governance | board | "Board" | org roster |
| JD-1 | JD-2 | family_spouse | married | SP | public record |
| JD-1 | BF-2 | financial_disclosed | >$2M holdings | ">$2M disclosed" | Ethics Commission filing |
| JD-1 | JD-3 | administrative | disclosure filer | "filer" | Ethics Commission filing |
| JD-1 | NP-3 | governance | director | "Director" | REHAB records |
| JD-1 | NP-8 | governance | director (compensated) | "Director ($)" | Takitani records |
| JD-2 | ED-1 | employment | teacher (retired) | "Teacher (ret.)" | Punahou records |
| JD-2 | NP-3 | governance | board; Foundation Vice-Chair | "Vice-Chair" | REHAB records |
| JD-2 | NP-8 | governance | president | "President" | Takitani records |

**18 edges.** This is the complete Issue 1 map.

**Nodes not yet connected (appear in Issue 1 roster but have no Issue 1–internal edges):**
- None. All 13 Issue 1 nodes have at least one internal edge.

**Visual clustering guidance for designer:**
- Left cluster: BF-0, BF-1, BF-2, BF-3, RE-1 (Luke banking/land core)
- Right cluster: JD-1, JD-2, JD-3 (Loo judiciary core)
- Top bridge: ED-1 (Punahou — connects BF-1 as trustee, JD-2 as teacher)
- Bottom satellites: NP-1, NP-2, NP-3, NP-8 (civic/philanthropic roles — radiate from both clusters)
- Central spine: the family edges (BF-0 ═══ BF-1, BF-0 ═══ JD-2, BF-1 ═══ JD-2, JD-1 ═══ JD-2) plus the financial edge (JD-1 ┄┄ BF-2) plus the administrative edge (JD-1 ⋯▷ JD-3)

---

## RESEARCH PACK: SOURCES + PULLS, ISSUE BY ISSUE

Public-record source list (web-verified) plus records-to-pull checklist for each issue, aligned to bible + node/edge system.

---

### Issue 1 — The Map

#### Primary public sources to cite

| Source | Node/Edge Served | URL |
|--------|-----------------|-----|
| Wilson M.N. Loo financial disclosure (long form, 2021) | JD-1, BF-2 (disclosed interests + officerships) | https://www.courts.state.hi.us/wp-content/uploads/2022/08/LooWilson2021FDS.pdf |
| Civil Beat Disclosures page for Wilson Loo | JD-1 (public database mirror; reader entry point) | https://disclosures.civilbeat.org/disclosures/wilson-loo/ |
| K.J. Luke / Damon Tract origin story (233 acres, $4.5M, $100K down) | BF-0, RE-1 (historical anchor) | https://archives.starbulletin.com/2000/11/15/news/story5.html |
| HNB opening-day mythology (10,000 firecrackers; ~$6.25M deposits) | BF-2 (founding myth texture, not proof of anything else) | https://generations808.com/banking-family-style/ |
| Punahou trustee overlap (Warren Luke tenure + retirement; Omidyar trustee since 2007; Omidyar trustee emeritus 2021) | BF-1 ── ED-1, ME-2 ── ED-1 | https://bulletin.punahou.edu/warren-k-k-luke-62-and-duncan-macnaughton-62-retire/ |
| Luke Center funded by K.J. Luke family, opened 2004 | NP-7 (bridge node for Issue 3) | https://www.punahou.edu/luke-center-for-public-service |
| Takitani Foundation board listing Janice Luke Loo as President | JD-2 ── NP-8 | https://takitanifoundation.org/board-of-directors/ |
| REHAB Foundation donor acknowledgement ("Honorable Wilson & Janice Luke Loo") | JD-1 ── NP-3, JD-2 ── NP-3 (philanthropy layer) | https://www.rehabhospital.org/sites/default/files/documents/REACH_Spring2017.pdf |

#### Records to pull now

- Download and archive **exact PDFs** for Evidence Locker: Loo 2021 FDS, Takitani board page PDF/screenshot, REHAB REACH PDFs.
- Pull Punahou pages into archive bundle:
  - Omidyar K–1 Neighborhood page: https://www.punahou.edu/archives-facilities-detail?pk=158068
  - Warren Luke retirement bulletin: https://bulletin.punahou.edu/warren-k-k-luke-62-and-duncan-macnaughton-62-retire/

---

### Issue 2 — The Blind Spots

#### Primary public sources to cite

| Source | Node/Edge Served | URL |
|--------|-----------------|-----|
| Commission on Judicial Conduct (CJC) FAQ | OV-1 (90-day post-service jurisdiction cutoff; attorney complaints → ODC) | https://www.courts.state.hi.us/courts/judicial_conduct/commission_on_judicial_conduct |
| RSCH Rule 8.2(b) language (90 days) | OV-2 (black-letter rule citation) | https://www.courts.state.hi.us/wp-content/uploads/2025/10/rsch.htm |
| CJC Annual Report 2020–2021 (PDF) | OV-1 (complaint volume stats + structure/mandate language) | https://www.courts.state.hi.us/wp-content/uploads/2022/03/COJC_AnnualRpt-20-21.pdf |
| OIP opinion on CJC records / UIPA applicability | OV-1 (why you can't FOIA your way out of confidentiality) | https://oip.hawaii.gov/f22-02/ |
| Rules of the District Courts (Rule 25.1: Recording of testimony/proceedings) | JD-5 (record exists / how to obtain transcript) | https://www.courts.state.hi.us/wp-content/uploads/2024/09/rdch_ada.pdf |
| Hawaiʻi Court Records Rules (HCRR) | JD-5 (defines "court records" incl. audio/video recordings) | https://www.courts.state.hi.us/wp-content/uploads/2025/01/hcrr.pdf |
| Judiciary form: Request for Audio/Video of Court Proceedings | JD-5 (operationalizes "how to request audio" workflow) | https://www.courts.state.hi.us/wp-content/uploads/2016/03/2FP509.pdf |
| First Circuit Per Diem Judges roster page | JD-4 (grounds per diem model discussion in current practice) | https://www.courts.state.hi.us/courts/district/first_circuit |
| Per Diem Judge Opportunities page | JD-4 (describes program at judiciary level) | https://www.courts.state.hi.us/courts/district/perdiem/per_diem |

#### Records to pull for Issue 2

- Archive **current RSCH / CJC rule text** and the annual report PDF (version control matters).
- Archive HCRR + the audio/video request form (these are your Issue 4 "why it's unprovable / why it's sealed" mechanics).

---

### Issue 3 — The Zone of Politeness

#### Primary public sources to cite

| Source | Node/Edge Served | URL |
|--------|-----------------|-----|
| Civil Beat "Our Supporters" page (Karen Luke / Warren Luke / Theresa Luke / Corey Luke entries, on-page as of Jan 8 2026) | BF-1 ┄┄ ME-1 (donor edge) | https://www.civilbeat.org/about/our-supporters/ |
| Warren Luke trustee since 1988 / retirement note | BF-1 ── ED-1 | https://bulletin.punahou.edu/warren-k-k-luke-62-and-duncan-macnaughton-62-retire/ |
| Omidyar trustee since 2007 (Punahou archives facilities page) | ME-2 ── ED-1 | https://www.punahou.edu/archives-facilities-detail?pk=158068 |
| Omidyar stepped down / trustee emeritus 2021 | ME-2 ── ED-1 (date range) | https://bulletin.punahou.edu/pierre-omidyar-84-named-trustee-emeritus/ |
| Ryan Ozawa UH Alumni Q&A (mentions ISO role at Hawaii National Bank) | ME-3 ──▶ BF-2 (employment bridge) | https://uhalumni.org/system/story/qa-with-ryan-ozawa-find-meaning-in-any-job |
| Civil Beat author page for Ryan Ozawa | ME-3 ──▶ ME-1 (contributor relationship) | https://www.civilbeat.org/author/ryan-ozawa/ |
| Hawaiʻi Leadership Forum governance (Cathy Luke + Pierre Omidyar as directors) | PO-1 ── NP-4, NP-4 ●●● NP-5 | https://projects.propublica.org/nonprofits/organizations/454910317 |
| Funding chain (HLF receives funding from Omidyar ʻOhana Fund at Hawaiʻi Community Foundation) | NP-4 ●●● NP-5 | https://omidyarfellows.org/news/hawaii-leadership-forum-welcomes-new-cohort-of-omidyar-fellows/ |
| Luke Center → Kōkua bridge (Heather Williams bio: "pivotal role" in Luke Center creation) | NP-7 ●●● NP-6 | https://kokuahawaiifoundation.org/our-team/ |
| Luke Center funded by K.J. Luke family, opened April 2004 | NP-7 | https://www.punahou.edu/luke-center-for-public-service |

#### Records to pull for Issue 3

- Screenshot/print-to-PDF the **exact donor list segment** containing the Luke names (freeze even if Civil Beat updates the page).
- Export the ProPublica HLF director list (or the 990 PDF linked there) and archive it.

---

### Issue 4 — December Second

#### Primary public sources to cite (verifiable scaffolding)

| Source | Node/Edge Served | URL |
|--------|-----------------|-----|
| Hawaiʻi Court Records Rules (HCRR) | JD-5 (how recordings are treated as court records) | https://www.courts.state.hi.us/wp-content/uploads/2025/01/hcrr.pdf |
| Judiciary form: Request for Audio/Video of Court Proceedings | JD-5 (request workflow) | https://www.courts.state.hi.us/wp-content/uploads/2016/03/2FP509.pdf |
| CJC FAQ + RSCH 8.2(b) | OV-1, OV-2 (jurisdiction constraint) | https://www.courts.state.hi.us/courts/judicial_conduct/commission_on_judicial_conduct |
| Audrey Stanley's public financial disclosure (2024) | JD-6 (appointment date + role context) | https://www.courts.state.hi.us/wp-content/uploads/2025/05/StanleyAudrey2024FDS.pdf |
| First Circuit Per Diem roster | JD-6 ── JD-4 (shows current per diem judges incl. Stanley) | https://www.courts.state.hi.us/courts/district/first_circuit |

#### Records to pull (Issue 4 "paper trail" kit)

- Court records division: **whether audio exists and whether it's sealed** (your own request trail is the artifact). Use the request form workflow as "show your work."
- CJC: you likely won't get complaint details (confidentiality), but log **what you asked, when, and what they responded** (Silence Index ritual).

---

### Issue 5 — The Record

#### Primary public sources (procedural + verification framework)

Everything from Issues 1–4, plus:

| Source | Node/Edge Served | URL |
|--------|-----------------|-----|
| ODC complaint process (how to file; forms; mailing requirement) | OV-3 | https://dbhawaii.org/how-to-file-a-complaint-with-the-odc/ |
| ODC complaint form instructions | OV-3 | https://dbhawaii.org/wp-content/uploads/251208-Complaint-Form-Instructions-1.pdf |
| Filing a complaint (Judiciary page) | OV-3 | https://www.courts.state.hi.us/legal_references/attorneys/filing_a_complaint |
| OIP opinion: CJC records not UIPA-disclosable | OV-1 (confidentiality framework) | https://oip.hawaii.gov/f22-02/ |

#### How to structure the "Minimum Clarifying Record Set"

Tie each of your seven items to **node IDs** (JD-3, OV-1, court records division, ME-1, etc.) so readers can literally jump between:
- "What record would settle this?" → "Who holds it?" → "Where it sits on the map?"

---

### Optional Issue 6 — Reform

#### Public sources for "this is changeable"

| Source | Relevance | URL |
|--------|-----------|-----|
| Judiciary documents about proposed/ongoing rule changes around RSCH Rule 8 / Rule 15 etc. | Reform framework | https://www.courts.state.hi.us/wp-content/uploads/2024/10/2024.10.25-MemoCCRO-RSCH-8-15-FDS-RCJC-for-posting-1.pdf |
| HCRR + District Court recording rules (what exists today; what could be amended) | Status quo baseline | https://www.courts.state.hi.us/wp-content/uploads/2025/01/hcrr.pdf |

---

## SOURCE_CODE CATALOG

Canonical Source_Code values used in edge tables, mapped to full citations. Ensures citation consistency across all five issues.

| Source_Code | Full Citation | Primary URL |
|-------------|--------------|-------------|
| obituary, bank history | K.J. Luke obituary, Honolulu Star-Bulletin, Nov 15 2000 | https://archives.starbulletin.com/2000/11/15/news/story5.html |
| bank founding records | Generations 808, "Banking, Family Style" (HNB founding narrative) | https://generations808.com/banking-family-style/ |
| land records, news archive | Star-Bulletin archive (Damon Tract acquisition, 1956) | https://archives.starbulletin.com/2000/11/15/news/story5.html |
| bank filings | Hawaii National Bank corporate filings | **TBV** — verify against FDIC/OCC/SEC/DCCA records |
| Fed roster | Federal Reserve Bank of San Francisco, board/director listings | **TBV** — verify against FRBSF public records |
| Punahou trustee roster | Punahou Bulletin: Warren Luke retirement; Omidyar K-1 Neighborhood; Omidyar trustee emeritus | https://bulletin.punahou.edu/warren-k-k-luke-62-and-duncan-macnaughton-62-retire/ ; https://www.punahou.edu/archives-facilities-detail?pk=158068 ; https://bulletin.punahou.edu/pierre-omidyar-84-named-trustee-emeritus/ |
| Punahou records | Punahou School employee/alumni records | **TBV** — verify against school directory/archival records |
| org roster | Various organization board listings | URL per entity (see individual node citations) |
| Ethics Commission filing | Wilson Loo 2021 FDS (long form) | https://www.courts.state.hi.us/wp-content/uploads/2022/08/LooWilson2021FDS.pdf |
| REHAB records | REHAB Hospital Foundation REACH publication (Spring 2017) | https://www.rehabhospital.org/sites/default/files/documents/REACH_Spring2017.pdf |
| Takitani records | Takitani Foundation board of directors page | https://takitanifoundation.org/board-of-directors/ |
| foundation records | K.J. Luke Foundation / Luke Center for Public Service | https://www.punahou.edu/luke-center-for-public-service |
| Commission records (TBV) | Commission on Judicial Conduct — to be verified | https://www.courts.state.hi.us/courts/judicial_conduct/commission_on_judicial_conduct |
| Civil Beat records | Honolulu Civil Beat organizational records | https://www.civilbeat.org/about/our-supporters/ |
| Civil Beat donor list | Civil Beat "Our Supporters" page | https://www.civilbeat.org/about/our-supporters/ |
| Civil Beat bylines | Civil Beat author page: Ryan Ozawa | https://www.civilbeat.org/author/ryan-ozawa/ |
| UH Alumni Q&A | UH Alumni interview with Ryan Ozawa (mentions HNB ISO role) | https://uhalumni.org/system/story/qa-with-ryan-ozawa-find-meaning-in-any-job |
| ProPublica 990 | ProPublica Nonprofit Explorer: Hawaii Leadership Forum | https://projects.propublica.org/nonprofits/organizations/454910317 |
| Omidyar Fellows | Omidyar Fellows: HLF welcomes new cohort | https://omidyarfellows.org/news/hawaii-leadership-forum-welcomes-new-cohort-of-omidyar-fellows/ |
| Kōkua team page | Kōkua Hawaii Foundation: Our Team (Heather Williams bio) | https://kokuahawaiifoundation.org/our-team/ |
| CJC annual report | CJC Annual Report 2020–2021 | https://www.courts.state.hi.us/wp-content/uploads/2022/03/COJC_AnnualRpt-20-21.pdf |
| RSCH | Rules of the Supreme Court of Hawaiʻi (Rule 8.2(b)) | https://www.courts.state.hi.us/wp-content/uploads/2025/10/rsch.htm |
| OIP opinion | Office of Information Practices, opinion F22-02 (CJC records) | https://oip.hawaii.gov/f22-02/ |
| HCRR | Hawaiʻi Court Records Rules | https://www.courts.state.hi.us/wp-content/uploads/2025/01/hcrr.pdf |
| audio request form | Judiciary Form 2FP509: Request for Audio/Video | https://www.courts.state.hi.us/wp-content/uploads/2016/03/2FP509.pdf |
| RDCH | Rules of the District Courts of Hawaiʻi (Rule 25.1) | https://www.courts.state.hi.us/wp-content/uploads/2024/09/rdch_ada.pdf |
| judiciary roster | First Circuit Per Diem Judges roster | https://www.courts.state.hi.us/courts/district/first_circuit |
| per diem program | Per Diem Judge Opportunities | https://www.courts.state.hi.us/courts/district/perdiem/per_diem |
| Stanley FDS | Audrey Stanley 2024 Financial Disclosure Statement | https://www.courts.state.hi.us/wp-content/uploads/2025/05/StanleyAudrey2024FDS.pdf |
| ODC filing | Disciplinary Board of Hawaiʻi: How to file a complaint (author's complaint in draft) | https://dbhawaii.org/how-to-file-a-complaint-with-the-odc/ |
| ODC form instructions | ODC Complaint Form Instructions | https://dbhawaii.org/wp-content/uploads/251208-Complaint-Form-Instructions-1.pdf |
| judiciary complaint page | Hawaiʻi State Judiciary: Filing a Complaint | https://www.courts.state.hi.us/legal_references/attorneys/filing_a_complaint |
| Commission correspondence | CJC correspondence (author's complaint trail) | — (author's records) |
| Commission response | CJC response re: 90-day rule application | — (author's records) |
| FBI receipt | FBI complaint receipt, July 2025 | — (author's records) |
| public record | Public biographical records | Per-node basis (news archives, official bios, etc.) |
| public bios | Published biographical information | Per-node basis (news archives, official bios, etc.) |
| RSCH reform memo | Judiciary memo re: proposed RSCH Rule 8/15 changes (Oct 2024) | https://www.courts.state.hi.us/wp-content/uploads/2024/10/2024.10.25-MemoCCRO-RSCH-8-15-FDS-RCJC-for-posting-1.pdf |

---

## RAW LINK BUNDLE (copy/paste for archival)

```text
Issue 1 core:
https://www.courts.state.hi.us/wp-content/uploads/2022/08/LooWilson2021FDS.pdf
https://disclosures.civilbeat.org/disclosures/wilson-loo/
https://archives.starbulletin.com/2000/11/15/news/story5.html
https://generations808.com/banking-family-style/
https://bulletin.punahou.edu/warren-k-k-luke-62-and-duncan-macnaughton-62-retire/
https://www.punahou.edu/archives-facilities-detail?pk=158068
https://bulletin.punahou.edu/pierre-omidyar-84-named-trustee-emeritus/
https://takitanifoundation.org/board-of-directors/
https://www.rehabhospital.org/sites/default/files/documents/REACH_Spring2017.pdf
https://www.punahou.edu/luke-center-for-public-service

Issue 2 core:
https://www.courts.state.hi.us/courts/judicial_conduct/commission_on_judicial_conduct
https://www.courts.state.hi.us/wp-content/uploads/2025/10/rsch.htm
https://www.courts.state.hi.us/wp-content/uploads/2022/03/COJC_AnnualRpt-20-21.pdf
https://oip.hawaii.gov/f22-02/
https://www.courts.state.hi.us/wp-content/uploads/2025/01/hcrr.pdf
https://www.courts.state.hi.us/wp-content/uploads/2016/03/2FP509.pdf
https://www.courts.state.hi.us/wp-content/uploads/2024/09/rdch_ada.pdf
https://www.courts.state.hi.us/courts/district/first_circuit
https://www.courts.state.hi.us/courts/district/perdiem/per_diem

Issue 3 core:
https://www.civilbeat.org/about/our-supporters/
https://uhalumni.org/system/story/qa-with-ryan-ozawa-find-meaning-in-any-job
https://www.civilbeat.org/author/ryan-ozawa/
https://projects.propublica.org/nonprofits/organizations/454910317
https://omidyarfellows.org/news/hawaii-leadership-forum-welcomes-new-cohort-of-omidyar-fellows/
https://kokuahawaiifoundation.org/our-team/
https://www.punahou.edu/luke-center-for-public-service

Issue 4/5 core:
https://www.courts.state.hi.us/wp-content/uploads/2025/05/StanleyAudrey2024FDS.pdf
https://www.courts.state.hi.us/courts/district/first_circuit
https://dbhawaii.org/how-to-file-a-complaint-with-the-odc/
https://dbhawaii.org/wp-content/uploads/251208-Complaint-Form-Instructions-1.pdf
https://www.courts.state.hi.us/legal_references/attorneys/filing_a_complaint

Optional Issue 6:
https://www.courts.state.hi.us/wp-content/uploads/2024/10/2024.10.25-MemoCCRO-RSCH-8-15-FDS-RCJC-for-posting-1.pdf
```
