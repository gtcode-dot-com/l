# OAHU UNDERGROUND — NETWORK MAP: MASTER NODE LIST (v2)

## Changes from v1

1. **Family tree corrected.** Janice Luke Loo is Warren Luke's *sister*, not daughter. Both are children of K.J. Luke (founder, Hawaii National Bank). Wilson Loo is Warren's brother-in-law, not son-in-law. K.J. Luke added as progenitor node BF-0.
2. **Edge type split.** Solid line now distinguishes governance/board (──) from employment/role (──▶). Prevents readers from conflating trustee power with staff positions.
3. **BF-4 merged into BF-2 as attribute.** HNB subsidiaries (K.J.L. Associates, K.J.L. Inc., Loyalty Enterprises, Hawaii National Bancshares) are listed as holdings within Wilson Loo's disclosure rather than a separate node. Keeps the map at 27 nodes.

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
Key edges: BF-1 (son); JD-2 (daughter); BF-2 (founded); RE-1 (acquired); NP-7 (K.J. Luke Foundation named after him)

**BF-1 — Warren K.K. Luke**
Type: Person (banker / civic leader)
Role: Chairman and CEO, Hawaii National Bank. Federal Reserve Bank of San Francisco, Hawaii branch director. Dozens of board positions spanning banking, education, philanthropy, civic governance (Punahou, Red Cross, Pacific Forum, etc.)
First appears: Issue 1
Key edges: BF-0 (son of); JD-2 (sister); JD-1 (brother-in-law); BF-2 (chairman/CEO); BF-3 (director); ED-1 (trustee); NP-1, NP-2, NP-3 (board seats); ME-2 (concurrent Punahou trustee, 2007–2019); PO-1 (father of Cathy Luke)

**BF-2 — Hawaii National Bank**
Type: Institution
Role: Only nationally chartered bank founded by a local Chinese-American family in Hawaii. Luke family flagship. Founded 1960.
Holdings disclosed in JD-1's financial filings: K.J.L. Associates (industrial/commercial property, >$1M), K.J.L. Inc. (commercial property, 20,885 shares), Loyalty Enterprises Ltd. (property rental), Hawaii National Bancshares Inc. (holding company, 67 shares combined). Total disclosed Luke-family interests held by JD-1: >$2M.
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
Key edges: BF-0 (son-in-law); BF-1 (brother-in-law); JD-2 (spouse); BF-2 (disclosed financial holdings >$2M in Luke entities); JD-3 (financial disclosures filed with); OV-1 (served within oversight ecosystem); NP-3, NP-8 (board roles); JD-5 (Dec 2, 2022 hearing — Issue 4)

**JD-2 — Janice Luke Loo**
Type: Person (bridge node)
Role: Daughter of K.J. Luke (BF-0). Sister of Warren Luke (BF-1). Spouse of Wilson Loo (JD-1). Retired Punahou English teacher. Stanford Education / Columbia Klingenstein Fellow. Extensive philanthropic board positions.
First appears: Issue 1
Key edges: BF-0 (daughter); BF-1 (sister); JD-1 (spouse); ED-1 (alumna, retired teacher); NP-3 (board, Vice-Chair of Foundation); NP-8 (President); NP-7 (K.J. Luke Foundation); OV-1 (served within oversight ecosystem)

**JD-3 — State Ethics Commission (financial disclosures)**
Type: Institution
Role: Repository for financial disclosure filings. Wilson Loo's disclosures filed here.
First appears: Issue 1 (Evidence Locker source document)
Key edges: JD-1 (filer); BF-2 (disclosed interests)

---

## ISSUE 2 NODES (The Blind Spots)

### Oversight

**OV-1 — Commission on Judicial Conduct**
Type: Institution
Role: Body that polices judicial conduct in Hawaii. Confidential proceedings. 90-day jurisdictional window. 3+ year reporting lag.
First appears: Issue 1 (mentioned); Issue 2 (detailed)
Key edges: JD-1, JD-2 (both served within ecosystem); OV-2 (90-day rule); JD-5 (complaint filed re: Dec 2 incident — Issue 4)

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

**NP-7 — K.J. Luke Foundation / Luke Center**
Type: Institution
Role: Named after K.J. Luke (BF-0). Educational and community focus.
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
Key edges: JD-4 (now per diem judge); JD-5 (connected to Dec 2 events); OV-3 (ODC complaint filed against)

### Oversight (additions)

**OV-3 — Office of Disciplinary Counsel (ODC)**
Type: Institution
Role: Handles attorney misconduct complaints.
First appears: Issue 4 (mentioned); Issue 5 (detailed)
Key edges: JD-6 (complaint filed re: Stanley)

---

## ISSUE 5 NODES (The Record)

### Government / Federal

**PO-2 — FBI**
Type: Institution
Role: Federal complaint filed July 2025.
First appears: Issue 5
Key edges: JD-5 (complaint re: Dec 2 incident and related conduct)

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
| JD-3 | State Ethics Commission | Institution | Judiciary | Issue 1 |
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
| NP-7 | K.J. Luke Foundation / Luke Center | Institution | Nonprofit | Issue 3 |
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
| ┄┄ (dashed) | Financial interest (disclosed) | JD-1 ┄┄ BF-2 (>$2M in Luke holdings) |
| ┄┄ (dashed) | Donor relationship | BF-1 ┄┄ ME-1 (Luke family donor) |
| ●●● (dotted) | Governance chain | NP-4 ●●● NP-5 (HLF → Omidyar fund) |
| ▸ (arrow) | Complaint / filing | JD-5 ▸ OV-1 (complaint filed) |

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
→ The Luke dynasty (progenitor → bank → boards) and the Loo judicial node. Family edges: BF-0 ═══ BF-1 (parent–child), BF-0 ═══ JD-2 (parent–child), BF-1 ═══ JD-2 (siblings), JD-1 ═══ JD-2 (spouses). Financial edge: JD-1 ┄┄ BF-2 (disclosed holdings). Reader sees two domains — banking/philanthropy and judiciary — joined by marriage and money.

**Issue 2:** Add OV-1, OV-2, JD-4
→ Oversight node appears. Reader sees that the Loo positions touch the body that polices judges. Structural mechanism annotations (90-day window, per diem system) explain *how* accountability gaps work.

**Issue 3:** Add ME-1, ME-2, ME-3, NP-4, NP-5, NP-6, NP-7, PO-1
→ Media cluster appears. Punahou edge now bridges banking and media (BF-1 ── ED-1 ── ME-2, concurrent trustees). Employment arrow: ME-3 ──▶ BF-2 (former bank employee now media contributor). Donor edge: BF-1 ┄┄ ME-1. Map connects banking → judiciary → oversight → media. Cathy Luke adds a political node connecting to philanthropy chain.

**Issue 4:** Add JD-5, JD-6, OV-3
→ Courtroom event node anchored inside the structure. Stanley enters the per diem system. ODC enters as complaint target. The map now has a specific incident surrounded by all the enabling conditions.

**Issue 5:** Add PO-2. All edges visible. Full map.
→ FBI node. The reader has built the complete network one issue at a time. Final spread shows everything. The Minimum Clarifying Record Set (from the series bible) can be cross-referenced to specific nodes and edges on the map.

---

## PRODUCTION EDGE TABLE (internal CSV schema for consistent redrawing)

Maintain as a spreadsheet. One row per edge. The map can be redrawn every issue without drift.

| From_ID | To_ID | Edge_Type | Role_Label | Date_Range | Source_Code |
|---------|-------|-----------|------------|------------|-------------|
| BF-0 | BF-1 | family_parent_child | father–son | — | obituary, bank history |
| BF-0 | JD-2 | family_parent_child | father–daughter | — | obituary, bank history |
| BF-0 | BF-2 | governance | founder | 1960 | bank founding records |
| BF-0 | RE-1 | financial | acquired | 1956 | land records, news archive |
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
| JD-1 | JD-3 | filing | disclosure filer | annual | Ethics Commission |
| JD-1 | NP-3 | governance | director | — | REHAB records |
| JD-1 | NP-8 | governance | director (compensated) | — | Takitani records |
| JD-1 | OV-1 | governance | served in ecosystem | — | Commission records |
| JD-2 | ED-1 | employment | teacher (retired) | — | Punahou records |
| JD-2 | NP-3 | governance | board; Foundation Vice-Chair | since 1990 | REHAB records |
| JD-2 | NP-8 | governance | president | — | Takitani records |
| JD-2 | NP-7 | governance | board | — | foundation records |
| JD-2 | OV-1 | governance | served in ecosystem | — | Commission records |
| ME-2 | ME-1 | governance | founder | — | Civil Beat records |
| ME-2 | ED-1 | governance | trustee | 2007–2019 | Punahou trustee roster |
| ME-2 | NP-5 | governance | — | — | foundation records |
| ME-3 | BF-2 | employment | former ISO | — | LinkedIn |
| ME-3 | ME-1 | employment | contributor | current | Civil Beat bylines |
| PO-1 | NP-4 | governance | — | — | org records |
| NP-4 | NP-5 | governance_chain | HLF → Omidyar fund | — | org records |
| NP-7 | NP-6 | governance_chain | Luke Center → Kōkua | — | org records |
| JD-5 | OV-1 | complaint | filed | post-Dec 2022 | Commission correspondence |
| OV-2 | JD-5 | rule_applied | 90-day invoked | — | Commission response |
| JD-6 | JD-4 | employment | per diem judge | current | judiciary roster |
| JD-6 | OV-3 | complaint_target | ODC complaint filed | — | ODC filing |
| PO-2 | JD-5 | complaint | FBI complaint filed | July 2025 | FBI receipt |
