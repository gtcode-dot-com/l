---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:21:34.061473+00:00'
exported_at: '2026-04-02T04:21:36.302637+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/03/24/spotting-issues-in-defi-with-dimensional-analysis
structured_data:
  about: []
  author: ''
  description: Dimensional analysis from physics can be applied to DeFi smart contracts
    to catch arithmetic and logic bugs by ensuring formulas maintain consistent dimensions
    across tokens, prices, and liquidity calculations. The post demonstrates how explicit
    dimensional annotations in code comments, like those used in Reserve Pr...
  headline: Spotting issues in DeFi with dimensional analysis
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/03/24/spotting-issues-in-defi-with-dimensional-analysis
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Spotting issues in DeFi with dimensional analysis
updated_at: '2026-04-02T04:21:34.061473+00:00'
url_hash: 186b211defef3c59d6ca2115324199ff021a0294
---

Using dimensional analysis, you can categorically rule out a whole category of logic and arithmetic bugs that plague DeFi formulas. No code changes required, just better reasoning!

One of the first lessons in physics is learning to think in terms of
[dimensions](https://en.wikipedia.org/wiki/Dimensional_analysis)
. Physicists can often spot a flawed formula in seconds just by checking whether the dimensions make sense. I once had a teacher who even kept a stamp that said “non-homogeneous formula” for that purpose (and it was used
*a lot*
on students’ work). Developers can use the same approach to spot incorrect arithmetic in smart contracts.

In this post, we’ll start with the basics of dimensional analysis in physics and then apply the same reasoning to real DeFi formulas. We’ll also show you how this can be implemented in practice, using Reserve Protocol as an example. Along the way, we’ll see why developers need to think explicitly about dimensional safety when writing smart contracts, and why the DeFi ecosystem would benefit from tooling that can automatically catch these classes of bugs. Speaking of which, while putting together this post, we actually built a
[Claude plugin](https://github.com/trailofbits/skills/tree/main/plugins/dimensional-analysis)
for this purpose (which we discuss in our
[follow-up post](https://blog.trailofbits.com/2026/03/25/try-our-new-dimensional-analysis-claude-plugin/)
).

## Quantities and dimensions

We will start with two formulas:

$$\textit{Speed} = \textit{distance} + \textit{time}$$$$\textit{Speed} = \frac{\textit{distance}}{\textit{time}}$$

Which of the two formulas is the correct way to calculate the speed of an object? Clearly, it’s the second one, but not just because you’ve memorized the correct formula. The deeper reason lies in
*dimensions*
.

Physics recognizes
**seven fundamental quantities**
: length (meters), mass (grams), time (seconds), electric current (amps), thermodynamic temperature (kelvin), amount of substance (moles), and luminous intensity (candela).

Every other physical concept, like speed, force, or energy, is a
*derived quantity*
, defined in terms of the fundamental ones.

For example, this is how speed is defined:

$$\textit{Speed} = \textit{distance} / \textit{time}$$

And this is how it’s represented in dimensional terms:

$$\textit{Speed}\text{(meters/second)} = \frac{\textit{length}\text{ (meters)}}{\textit{time}\text{ (seconds)}}$$

The golden rule is simple:
**both sides of an equation must have the same dimension.**

And, just as important,
**you can’t add or subtract quantities with different dimensions.**

So if we reason through the incorrect speed formula in terms of dimensions, we’ll get this:

$$\textit{Speed}\text{ (meters/second)} = \frac{\textit{length}\text{ (meters)}}{\textit{time}\text{ (seconds)}} = \textit{length}\text{ (meters)} + \textit{time}\text{ (seconds)}$$

This is clearly nonsense. If dimensions could scream, they would. So we can easily say that this formula can’t be used to calculate anything, speed or otherwise.

Note that even when dimensions check out, you must still use consistent units!

## Dimensional thinking in DeFi

Now let’s shift the lens. Physics deals with meters, seconds, and kilograms, but DeFi has its own “dimensions”: tokens, prices, liquidity, and so on.

Here’s where mistakes start to creep in. Imagine you’re coding
[an AMM](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
and you write this:

$$K = x + y$$

Does that look right? It shouldn’t.

Here, x might represent the number of “token A” and y the number of “token B.” Adding them together is just as meaningless as adding distance and time. They’re different dimensions.

At this point, you might object:
*“Wait, this is exactly how Curve Stable Pools work!”*

And you’d be right. But the key is in the name:
**stable**
. In a stable pool, tokens are designed to maintain near-equal value. Under that assumption, token A and token B are treated as if they were the same “dimension.” This trick makes the formula workable in this special case. But outside of stable pools, blindly adding tokens together is as absurd as writing \(\textit{speed} = \textit{distance} + \textit{time}\). Understanding homogeneous formulas helps you not only find issues but also understand why a formula is structured the way it is.

In physics,
**speed**
is a derived quantity built from the fundamental quantities of
**length**
and
**time**
. DeFi has its own derived quantities:
**liquidity**
, for example, is built from
**token balances**
.

For example, in a Uniswap v3 pool with reserves x and y, liquidity is calculated as follows:

$$\textit{Liquidity} = \sqrt{x \cdot y}$$

Dimensionally, this calculation looks like this:

$$\textit{Liquidity} = \sqrt{[A] \cdot [B]}$$

Here, [A] is a dimension that represents the number of token A, and [B] is a dimension that represents the number of token B.

On its own, “token A × token B” doesn’t have a direct interpretation, just like “meters × seconds” doesn’t. But within the invariant equation \(k = x \cdot y\), the \(x \cdot y\) part defines a
**conserved relationship**
that governs swaps.

k and the liquidity are not base dimensions; they are derived ones, combining the balances of multiple tokens into a single pool-wide property.

## Why some price formulas don’t work

### Example 1

Suppose someone writes this incorrect formula in his protocol:

$$\textit{Price} = \frac{\text{number of token A}}{\textit{liquidity}}$$

We can easily spot the issue with dimensional analysis.

This is an example of a correct and straightforward way to define a price:

$$\text{Price of B in terms of A} = \frac{\text{amount of A}}{\text{amount of B}} = \frac{[A]}{[B]}$$

If the formula \(\textit{Price} = \frac{\text{number of token A}}{\textit{liquidity}}\) were correct, the right side of the equation would have the same dimensions as the correct price definition above.

But dimensionally, the right side of the formula is as follows:

$$\frac{[A]}{\sqrt{[A] \cdot [B]}} = \frac{\sqrt{[A]} \cdot \sqrt{[A]}}{\sqrt{[A] \cdot [B]}} = \sqrt{\frac{[A]}{[B]}}$$

That’s not a price; it’s the
*square root*
of a price. The formula produces something, but it’s not a price.

Consequently, we have different dimensions on the right and left sides of the formula. This means the formula \(\textit{Price} = \frac{\text{number of token A}}{\textit{liquidity}}\) is incorrect. This is discernible without further knowledge of the DEX.

### Example 2

Let’s take another example that is harder to spot without dimensional analysis. Which of these formulas is incorrect?

1. $$K = (\text{number of token A})^2 \cdot \text{Price of B in terms of A}$$
2. $$K = \frac{(\text{number of token A})^2}{\text{Price of B in terms of A}}$$

Here is a tip: K is often defined as \(\text{number of token A} \cdot \text{number of token B}\) .

Dimensionally, this means \(K = [A] \cdot [B]\).

Now that we have the dimensions of the left side of the equation, let’s check if one of the two formulas has the same dimensions on the right side.

1. $$K = [A]^2 \cdot \frac{[A]}{[B]} = \frac{[A]^3}{[B]}$$
2. $$K = \frac{[A]^2}{\frac{[A]}{[B]}} = [A] \cdot [B]$$

So we can see that the first formula can’t be valid, and the second one is dimensionally valid!

### Example 3

For an example in a DeFi context, let’s consider a real vulnerability that we identified during the
[CAP Labs audit](https://github.com/trailofbits/publications/blob/master/reviews/2025-05-caplabs-coveredagentprotocol-securityreview.pdf)
(TOB-CAP-17).

```
function price(address _asset) external view returns (uint256 latestAnswer, uint256 lastUpdated) {
    address capToken = IERC4626(_asset).asset();
    (latestAnswer, lastUpdated) = IOracle(msg.sender).getPrice(capToken);
    uint256 capTokenDecimals = IERC20Metadata(capToken).decimals();
    uint256 pricePerFullShare = IERC4626(_asset).convertToAssets(capTokenDecimals);
    latestAnswer = latestAnswer * pricePerFullShare / capTokenDecimals;
}
```

Figure 1: Price calculation function in CAP

ERC-4626 explicitly expects a
[number of assets as the only input](https://eips.ethereum.org/EIPS/eip-4626#converttoassets)
of the
`convertToAssets`
function. But the CAP Labs implementation sends decimals! That’s exactly the kind of issue that can be identified with a quick dimensional analysis, even without knowing what the codebase does.

## Real-life best practices

Some programming languages make dimensional safety a first-class feature. For instance, F# has a “units of measure” system: you can declare a value as
`float<m/s>`
or
`float<USD/token>`
, and the compiler will reject equations where the units don’t align. It’s enforced at compile time. Solidity lacks this feature, so developers must emulate it through comments and naming conventions.

For example,
[Reserve Protocol’s](https://github.com/reserve-protocol/reserve-index-dtf/blob/436cfde284a7e1be4e70c833e037ff1af7316992/contracts/Folio.sol#L573)
unit comments are a textbook best practice. They codify dimensional reasoning in its codebase. All state variables and parameters are annotated with unit comments that define how values relate. This practice enforces that assignments in code must preserve matching dimensions, often with nearby comments showing unit equivalences. In Reserve Protocol contracts, each variable carries a comment like the one shown in figure 2. In this example, the comment indicates that the price is represented as a 27-decimal fixed-point unit of account per token. Because both the dimension (
`UoA/tok`
) and the numeric scale (
`D27`
) are documented, developers and auditors instantly know what a number represents and how to handle it. This eliminates ambiguity, prevents values with different scales from being mixed, and acts as a guardian against subtle formula bugs.

```
    /// Start a new rebalance, ending the currently running auction
    /// @dev If caller omits old tokens they will be kept in the basket for mint/redeem but skipped in the rebalance
    /// @dev Note that weights will be _slightly_ stale after the fee supply inflation on a 24h boundary
    /// @param tokens Tokens to rebalance, MUST be unique
    /// @param weights D27{tok/BU} Basket weight ranges for the basket unit definition; cannot be empty [0, 1e54]
    /// @param prices D27{UoA/tok} Prices for each token in terms of the unit of account; cannot be empty (0, 1e45]
    /// @param limits D18{BU/share} Target number of baskets should have at end of rebalance (0, 1e27]
    /// @param auctionLauncherWindow {s} The amount of time the AUCTION_LAUNCHER has to open auctions, can be extended
    /// @param ttl {s} The amount of time the rebalance is valid for
    function startRebalance(
```

Figure 2: Example of a comment explaining the dimension of a price in Reserve Protocol smart contracts

This approach is not limited to large or mature protocols. Any smart contract codebase can benefit from explicitly documenting dimensions and units.

Developers should treat dimensional annotations as part of the protocol’s safety model rather than as optional documentation. Clearly labeling whether a variable represents tokens, prices, liquidity shares, or fixed-point scaled values makes code easier to review, safer to modify, and significantly simpler to audit.

When designing a dimensional annotation system, a few general principles can help:

* **Make dimensions explicit and consistent.**
  Decide early how dimensions will be represented (for example,
  `tok`
  ,
  `UoA`
  ,
  `shares`
  , etc.) and apply the convention uniformly across the codebase.
* **Always document scale together with dimension.**
  In DeFi, mismatched decimals are often as dangerous as mismatched dimensions. Including fixed-point precision (such as
  `D18`
  or
  `D27`
  ) alongside dimensional annotations removes ambiguity.
* **Annotate inputs, outputs, and state variables.**
  Dimension safety breaks down if only storage variables are documented, but function parameters and return values are not.
* **Prefer clarity over brevity.**
  Slightly longer variable names or comments are far cheaper than subtle arithmetic bugs.
* **Document conversions explicitly.**
  Whenever values change dimension or scale (for example, shares to assets or tokens to unit of account), adding a short comment explaining the transformation greatly improves auditability.

These conventions require discipline, but they improve dimensional safety in a language that does not natively support it.

## Toward dimensional safety in Solidity

We’ve taken a first step toward automating this kind of analysis with a Claude plugin for dimensional checking, which we’ll introduce in a follow-up post. Beyond that, the ecosystem would benefit from deeper static analysis tooling that blends the semantic capabilities of LLMs. For example, a Slither-based linting or static analysis tool for Solidity could completely infer, propagate, and check “units” and “dimensions” across a codebase, flagging mismatches in the same way that Solidity warns about most incompatible types.

In the meantime, document your protocol’s dimensions and decimals: note in comments what each variable represents, and be explicit about the scale and units of every stored or computed value. These small habits will make your formulas more readable, auditable, and robust.

And try out our new
[Claude plugin](https://github.com/trailofbits/skills/tree/main/plugins/dimensional-analysis)
for dimensional analysis. For more details, see our
[follow-up blog post](https://blog.trailofbits.com/2026/03/25/try-our-new-dimensional-analysis-claude-plugin/)
announcing the plugin.