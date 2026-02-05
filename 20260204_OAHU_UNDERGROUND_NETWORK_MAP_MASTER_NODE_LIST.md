# OAHU UNDERGROUND — NETWORK MAP: MASTER NODE LIST

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

**BF-1 — Warren Luke**
Type: Person (banker / civic leader)
Role: Chairman, Hawaii National Bank. Federal Reserve Bank of San Francisco, Hawaii branch director.
Board positions: Dozens across banking, education, philanthropy, civic governance (Punahou, Red Cross, Pacific Forum, etc.)
First appears: Issue 1
Key edges: BF-2, BF-3, ED-1, NP-1, NP-2, NP-3 (board seats); JD-1 (father-in-law); PO-1 (father); ME-1 (Punahou co-trustee with ME-2)

**BF-2 — Hawaii National Bank**
Type: Institution
Role: Only nationally chartered bank founded by a local Chinese-American family in Hawaii. Luke family flagship.
Founded: 1960 (Damon Tract acquisition 1956)
First appears: Issue 1
Key edges: BF-1 (chairman); RE-1 (founding land); BF-4 (subsidiaries); JD-1 (disclosed holdings via JD-3); ME-3 (former employee)

**BF-3 — Federal Reserve Bank of San Francisco (Hawaii branch)**
Type: Institution
Role: Federal Reserve regional branch
First appears: Issue 1
Key edges: BF-1 (director)

**BF-4 — HNB Subsidiaries & Luke-Affiliated Entities**
Type: Institution cluster
Role: Financial entities in which JD-1 holds disclosed interests
First appears: Issue 1
Key edges: BF-2 (parent); JD-1 (disclosed holdings >$2M per JD-3)

### Real Estate / Land

**RE-1 — Damon Tract**
Type: Property
Role: Land acquired by Luke family, 1956. Foundation of banking enterprise.
First appears: Issue 1
Key edges: BF-1 (acquired by); BF-2 (led to founding of)

### Education

**ED-1 — Punahou School**
Type: Institution
Role: Hawaii's most elite private school. Board of trustees = apex social network node.
First appears: Issue 1
Key edges: BF-1 (trustee); ME-2 (trustee, 2007–2019, concurrent with BF-1)

### Nonprofit / Philanthropy

**NP-1 — American Red Cross (Hawaii chapter)**
Type: Institution
First appears: Issue 1
Key edges: BF-1 (board)

**NP-2 — Pacific Forum**
Type: Institution (think tank / policy)
First appears: Issue 1
Key edges: BF-1 (board)

**NP-3 — Luke Family Hospital & Foundation Boards**
Type: Institution cluster
Role: Hospital boards, charitable foundations — the civic legitimacy layer of the Luke capital stack.
First appears: Issue 1
Key edges: BF-1 (founder/board); JD-2 (board roles, bridge between Luke philanthropy and Loo legal career)

### Judiciary / Legal

**JD-1 — Wilson Loo**
Type: Person (judge / attorney)
Role: Per diem judge. Attorney in private practice.
First appears: Issue 1
Key edges: BF-1 (son-in-law); BF-2, BF-4 (disclosed financial holdings >$2M); JD-2 (spouse); JD-3 (financial disclosures filed with); OV-1 (both Loos served in oversight ecosystem); JD-5 (Dec 2, 2022 hearing — Issue 4)

**JD-2 — Janice Luke Loo**
Type: Person (bridge node)
Role: Daughter of BF-1. Spouse of JD-1. Hospital and foundation board positions.
First appears: Issue 1
Key edges: BF-1 (daughter); JD-1 (spouse); NP-3 (board roles); OV-1 (served within oversight ecosystem)

**JD-3 — State Ethics Commission (financial disclosures)**
Type: Institution
Role: Repository for financial disclosure filings. Wilson Loo's disclosures filed here.
First appears: Issue 1 (Evidence Locker source document)
Key edges: JD-1 (filer); BF-2, BF-4 (disclosed interests)

---

## ISSUE 2 NODES (The Blind Spots)

### Oversight

**OV-1 — Commission on Judicial Conduct**
Type: Institution
Role: Body that polices judicial conduct in Hawaii. Confidential proceedings. 90-day jurisdictional window. 3+ year reporting lag.
First appears: Issue 1 (mentioned); Issue 2 (detailed)
Key edges: JD-1, JD-2 (both served within ecosystem); OV-2 (90-day rule); JD-5 (complaint filed re: Dec 2 incident — Issue 4)

**OV-2 — 90-Day Jurisdictional Window**
Type: Rule / structural mechanism (not an entity — rendered on map as a constraint annotation on OV-1)
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
Key edges: ME-2 (founder); ME-3 (contributor); BF-1 (Luke family on donor list); ED-1 (Punahou trustee overlap between ME-2 and BF-1); JD-3 (hosts disclosure database but produces no investigation)

**ME-2 — Pierre Omidyar**
Type: Person (media / philanthropy)
Role: eBay founder. Founded Civil Beat. Punahou trustee 2007–2019, concurrent with BF-1.
First appears: Issue 3
Key edges: ME-1 (founder); ED-1 (trustee, overlapping with BF-1); NP-5 (Omidyar 'Ohana Fund)

**ME-3 — Ryan Ozawa**
Type: Person (bridge node)
Role: Former Hawaii National Bank information security officer. Current Civil Beat contributor.
First appears: Issue 3
Key edges: BF-2 (former ISO); ME-1 (contributor)

### Nonprofit / Philanthropy (additions)

**NP-4 — Hawaii Leadership Forum**
Type: Institution
First appears: Issue 3
Key edges: PO-1 (Cathy Luke involvement); NP-5 (governance chain)

**NP-5 — Omidyar ʻOhana Fund**
Type: Institution (foundation)
First appears: Issue 3
Key edges: ME-2 (Omidyar); NP-4 (governance chain with Hawaii Leadership Forum)

**NP-6 — Kōkua Hawaii Foundation**
Type: Institution
Role: North Shore conservation network.
First appears: Issue 3
Key edges: NP-7 (Luke Center connection); RE-1 (North Shore land/conservation)

**NP-7 — Luke Center**
Type: Institution
First appears: Issue 3
Key edges: BF-1 (Luke family); NP-6 (Kōkua connection); ED-1 (educational/institutional overlap)

### Political / Government

**PO-1 — Cathy Luke**
Type: Person (political)
Role: State legislator. Daughter of Warren Luke.
First appears: Issue 3
Key edges: BF-1 (daughter); NP-4 (Hawaii Leadership Forum); NP-5 (governance chain)

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

*No new network nodes in Issue 5. The issue is about synthesizing the existing map and presenting the full evidence file.*

---

## COMPLETE NODE REGISTRY

| ID | Name | Type | Domain | Introduced |
|------|------|------|--------|------------|
| BF-1 | Warren Luke | Person | Banking | Issue 1 |
| BF-2 | Hawaii National Bank | Institution | Banking | Issue 1 |
| BF-3 | Fed Reserve (Hawaii branch) | Institution | Banking | Issue 1 |
| BF-4 | HNB Subsidiaries / Luke entities | Cluster | Banking | Issue 1 |
| RE-1 | Damon Tract | Property | Real Estate | Issue 1 |
| ED-1 | Punahou School | Institution | Education | Issue 1 |
| NP-1 | American Red Cross (Hawaii) | Institution | Nonprofit | Issue 1 |
| NP-2 | Pacific Forum | Institution | Nonprofit | Issue 1 |
| NP-3 | Luke Hospital & Foundation boards | Cluster | Nonprofit | Issue 1 |
| JD-1 | Wilson Loo | Person | Judiciary | Issue 1 |
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
| NP-7 | Luke Center | Institution | Nonprofit | Issue 3 |
| PO-1 | Cathy Luke | Person | Political | Issue 3 |
| JD-6 | Audrey Stanley | Person | Judiciary | Issue 4 |
| OV-3 | Office of Disciplinary Counsel | Institution | Oversight | Issue 4 |
| PO-2 | FBI | Institution | Government | Issue 5 |

*JD-5 teased in Issue 1 prologue, fully introduced Issue 4.

---

## EDGE TYPES (legend for map connections)

| Edge Symbol | Relationship Type | Example |
|-------------|-------------------|---------|
| ── (solid) | Board / governance seat | BF-1 → ED-1 (trustee) |
| ── (solid) | Employment / role | ME-3 → BF-2 (former ISO) |
| ═══ (double) | Family / marriage | BF-1 ═══ JD-2 (father–daughter) |
| ═══ (double) | Family / marriage | JD-1 ═══ JD-2 (spouses) |
| ┄┄ (dashed) | Financial interest (disclosed) | JD-1 ┄┄ BF-2 (>$2M holdings) |
| ┄┄ (dashed) | Donor relationship | BF-1 ┄┄ ME-1 (Luke family donor) |
| ●●● (dotted) | Governance chain | NP-4 ●●● NP-5 (HLF → Omidyar fund) |
| ▸ (arrow) | Complaint / filing | JD-5 ▸ OV-1 (complaint filed) |

---

## MAP BUILD SEQUENCE (what the reader sees each issue)

**Issue 1:** BF-1, BF-2, BF-3, BF-4, RE-1, ED-1, NP-1, NP-2, NP-3, JD-1, JD-2, JD-3
→ Two clusters (Luke banking + Loo judiciary), one marriage edge connecting them.

**Issue 2:** Add OV-1, OV-2, JD-4
→ Oversight node appears. Reader sees that the Loo positions touch the body that polices judges.

**Issue 3:** Add ME-1, ME-2, ME-3, NP-4, NP-5, NP-6, NP-7, PO-1
→ Media cluster appears. Punahou edge now bridges banking and media. Donor edge from Luke family to Civil Beat. Map connects banking → judiciary → oversight → media.

**Issue 4:** Add JD-5, JD-6, OV-3
→ Courtroom event node. Stanley enters. ODC enters. The map now has a specific incident anchored inside the structure.

**Issue 5:** Add PO-2. All edges visible. Full map.
→ The reader has built the complete network one issue at a time. Final spread shows everything.
