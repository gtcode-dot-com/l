---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T20:05:06.666485+00:00'
exported_at: '2026-09-26T20:05:07.855332+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access
structured_data:
  about: []
  author: ''
  description: We found and reported a bug in Provenance Blockchain, a public proof-of-stake
    chain built on Cosmos SDK, that lets any user grant themselves admin control over
    marker accounts without holding a single token.
  headline: State divergence enables unauthorized access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access
  publisher:
    logo: /favicon.ico
    name: GTCode
title: State divergence enables unauthorized access
updated_at: '2026-09-26T20:05:06.666485+00:00'
url_hash: e8b3d9b3f77c9b1cfcef229a254f1a16cc123027
---

We found and reported a bug in Provenance Blockchain, a public proof-of-stake chain built on
[Cosmos SDK](https://docs.cosmos.network/)
, that lets any user grant themselves admin control over marker accounts without holding a single token. Provenance covers a range of financial services, including on-chain tokenized loans, private equity tokens, bridged assets, and asset registries. Our bug affected 82 markers representing live financial assets on mainnet.

We found the bug, which affects versions before 1.28.0, in March 2026, and reported it to Provenance on April 1. It was mitigated in
[PR #2627](https://github.com/provenance-io/provenance/pull/2627)
(commit
[c81fd65](https://github.com/provenance-io/provenance/commit/c81fd65f8ad48de42d5a6d68e761a0851c7e72c4)
), which shipped in v1.28.0 on May 1, 2026, and fixed in
[PR #2734](https://github.com/provenance-io/provenance/pull/2734)
, which shipped in v1.29.0 on June 8, 2026.

## What is a marker?

The marker module is Provenance’s core primitive for fungible tokens. Chain participants can issue a new asset on Provenance by submitting a
`MsgAddMarkerRequest`
transaction; the chain creates a dedicated account for that asset, called a marker. Each marker is a special account type that controls:

* A
  **denomination**
  (e.g.,
  `uusd.trading`
  ,
  `cusd.deposit`
  ,
  `cguaranteedrateomni`
  )
* An
  **access control list**
  governing who can mint, burn, withdraw, deposit, or administer the token
* A
  **supply field**
  recording the canonical token count
* An
  **escrow balance**
  (the marker account can hold any asset, not just its own denomination)

Markers are either
`supply_fixed`
(the supply field is enforced as a hard cap) or non-fixed (the bank module is the source of truth; the supply field is informational). This distinction is central to the bug.

## The bug: An access check anyone can pass

[`AddAccess`](https://github.com/provenance-io/provenance/blob/488b8a73e292043910aaf0ec485fac961b5e2c97/x/marker/keeper/msg_server.go#L139-L159)
is the Cosmos SDK message handler that processes requests to modify a marker’s access control list. It checks whether the caller is authorized using three conditions, any one of which is sufficient:

1. The caller is the marker’s designated manager and the marker is in
   `Finalized`
   state.
2. The caller already holds
   `ACCESS_ADMIN`
   on the marker.
3. **The caller controls 100% of the marker’s circulating supply.**

```
case types.StatusFinalized, types.StatusActive:
    if !(caller.Equals(m.GetManager()) &amp;&amp; m.GetStatus() == types.StatusFinalized) &amp;&amp;
        !m.AddressHasAccess(caller, types.Access_Admin) &amp;&amp;
        !k.accountControlsAllSupply(ctx, caller, m) {
        return fmt.Errorf("%s is not authorized to make access list changes against finalized/active %s marker",
            caller, m.GetDenom())
    }
```

Figure 1: Authorization check in
`keeper.AddAccess`
(
[`x/marker/keeper/marker.go#L94–L100`](https://github.com/provenance-io/provenance/blob/488b8a73e292043910aaf0ec485fac961b5e2c97/x/marker/keeper/marker.go#L94-L100)
)

Condition 3 is implemented by
`accountControlsAllSupply`
:

```
func (k Keeper) accountControlsAllSupply(
    ctx sdk.Context,
    caller sdk.AccAddress,
    m types.MarkerAccountI,
) bool {
    balance := k.bankKeeper.GetBalance(ctx, caller, m.GetDenom())
    supply := m.GetSupply()                                         // ← bug
    return supply.Equal(sdk.NewCoin(m.GetDenom(), balance.Amount))
}
```

Figure 2: The vulnerable
`accountControlsAllSupply`
function (
[`x/marker/keeper/marker.go#L866–L875`](https://github.com/provenance-io/provenance/blob/488b8a73e292043910aaf0ec485fac961b5e2c97/x/marker/keeper/marker.go#L866-L875)
)

The
`m.GetSupply`
function reads the supply field stored directly on the marker struct. For non-fixed supply markers that were activated with zero supply, that field
**always stays zero**
. The live circulating count lives in the bank module, and non-fixed markers never write back to the marker struct after minting.

So for any non-fixed supply marker, the authorization check reduces to the following:

```
supply  = Coin{denom, 0}   // stored marker field, always 0
balance = Coin{denom, 0}   // attacker holds no tokens
0 == 0  →  true
```

Figure 3: Authorization check result for a non-fixed supply marker when the caller holds no tokens

The check intended to restrict access to 100%-of-supply holders becomes unconditionally true for any caller with zero balance.

## Exploitation: Two transactions to mint or drain

An attacker sends a single
`MsgAddAccessRequest`
transaction:

```
{
  "denom": "uusd.trading",
  "administrator": "&lt;attacker_address&gt;",
  "access": [
    {
      "address": "&lt;attacker_address&gt;",
      "permissions": ["ACCESS_ADMIN", "ACCESS_MINT", "ACCESS_WITHDRAW"]
    }
  ]
}
```

Figure 4:
`MsgAddAccessRequest`
granting the attacker admin, mint, and withdraw permissions on a target marker

No existing tokens are needed for exploitation. The authorization check passes immediately via the broken condition 3. From there, the attacker has two paths:

* `MsgMintRequest`
  : to mint new tokens of the marker’s denom and send them to any address
* `MsgWithdrawRequest`
  : to drain any assets held in the marker’s escrow balance

The whole attack is two transactions: one to gain permissions, and one more to act on them.

## Impact: What was at risk

At the time of discovery,
**82 active markers**
on Provenance mainnet had a stored supply of 0 while carrying real circulating supply or escrowed assets, every one of them exploitable. These markers span multiple independent parties on the chain, not a single application.

**Escrow withdrawal**
was the most direct path. Among the affected markers, those holding nhash (Provenance’s base token) in escrow accounted for roughly 30 × 10
15
nhash, or around
**$500,000 at HASH prices at the time of discovery**
. The three largest markers are shown below:

| Marker | Owner | Escrowed nhash |
| --- | --- | --- |
| `grant0051` | Provenance Foundation grant program | 19,230,770,000,000,000 |
| `provenance.validator.incentive.program` | Chain validator incentive fund | 8,561,225,000,000,000 |
| `grant0077` | Provenance Foundation grant program | 2,486,556,736,909,250 |

The three markers shown above are all chain governance programs operated by the Provenance Foundation: one holds validator rewards, and two hold community grant funds.

**Supply inflation**
was a broader but more constrained vector. The 74 vulnerable markers spanned bridged stablecoins and wrapped assets (
`uusd.trading`
,
`uusdc.figure.se`
,
`nbtc.figure.se`
), consortium deposits (
`cusd.deposit`
), tokenized mortgage participations (
`cguaranteedrateomni`
,
`chomebridgeomni`
), and yield tokens (
`nuva.ylds`
,
`uylds.fcc`
). An attacker with
`ACCESS_MINT`
on any of these could issue arbitrary new tokens of that denom. The practical harm depended on the token type. For restricted tokens with KYC requirements, it was primarily a solvency and integrity threat; for non-restricted coin-type markers, it was a more direct inflation risk.

We confirmed the affected markers and their balances by querying mainnet via the Provenance CLI and the public REST API.

## The fix: Read live supply, and guard against zero

[PR #2627](https://github.com/provenance-io/provenance/pull/2627)
shipped the mitigation, which adds a check against zero supply:

```
if supply.Amount.IsNil() || supply.Amount.IsZero() {
  return false
}
```

Figure 5: The fix (
[`x/marker/keeper/marker.go`](https://github.com/provenance-io/provenance/pull/2627/changes#diff-bc1ca0afea7f4545a016207811d6f040977cf4ccbd57245b5373f7d4e5adfa40R872)
in PR #2627)

This blocked the attack we reported. All 82 affected markers had a stored supply of 0, and a zero-supply marker now fails the check outright.

It did not fix the divergence. The comparison still read the stale field, so it still passed whenever that field was non-zero and the caller’s balance happened to match it.

[PR #2734](https://github.com/provenance-io/provenance/pull/2734)
shipped the full fix, which changes one line:

```
// Before: reads stale stored field, always 0 for non-fixed markers
supply := m.GetSupply()

// After: reads live circulating supply from the bank module
supply := k.bankKeeper.GetSupply(ctx, m.GetDenom())
```

Figure 6: The one-line fix (
[`x/marker/keeper/marker.go`](https://github.com/provenance-io/provenance/pull/2734/changes#diff-bc1ca0afea7f4545a016207811d6f040977cf4ccbd57245b5373f7d4e5adfa40R898)
in PR #2734)

Both sides of the comparison now come from the bank module, so there is no stale field left to diverge.

## Authorization must fail from the default state

The root cause of this issue was state desynchronization. The marker struct and the bank module both represent the token supply, but only the bank module is kept current for non-fixed markers. The authorization check read from the wrong one.

The check wasn’t just wrong; it was bypassable by default because of the zero-equality shortcut. Because the stale field was always 0, the comparison
`0 == 0`
was always true. An access control check that compares against a value that is always the same as the attacker’s default state is trivially bypassable.

Switching to the live bank supply alone doesn’t fully close the hole. A freshly deployed marker with no tokens minted yet also has live supply of zero, so an attacker could self-grant admin by targeting it before it’s funded. The fix handles this with an explicit zero-guard:
`accountControlsAllSupply`
returns false whenever live supply is zero, regardless of balance.

The broader pattern: an authorization predicate must never be satisfiable from the attacker’s default state. A check of the form
`balance == supply`
hands access to everyone when supply can be zero, whether because the state is stale or the marker is simply unfunded.

Two things would have caught this before it went live. First, the access-list authorization model was never specified. Writing the rule down forces both questions that point straight at the bug: which supply, and what happens when it’s zero? Second, the property is easy to state:
`accountControlsAllSupply`
should only return true when live supply is positive and the caller holds all of it. A property-based test or fuzzer that generates random sequences of marker operations, such as minting, transferring, and creating empty markers, and checks this property after each step would find both failure modes automatically.