---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-17T06:12:03.679794+00:00'
exported_at: '2026-09-17T06:12:07.043655+00:00'
feed: https://www.bellingcat.com/feed/
language: en
source_url: https://www.bellingcat.com/news/2026/07/30/will-ronaldo-cry-world-cup-fans-bet-billions-through-prediction-markets
structured_data:
  about: []
  author: ''
  description: Users traded on almost 60,000 outcomes, betting on everything from
    the sponsor of the Golden Boot winner to whether Cristiano Ronaldo would shed
    a tear during a Portugal match.
  headline: Will Ronaldo Cry​? World Cup Fans Bet Billions Through Prediction Markets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.bellingcat.com/news/2026/07/30/will-ronaldo-cry-world-cup-fans-bet-billions-through-prediction-markets
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Will Ronaldo Cry​? World Cup Fans Bet Billions Through Prediction Markets
updated_at: '2026-09-17T06:12:03.679794+00:00'
url_hash: 2a217d4cc0cfddf7c2d383cea24f0f1026a66ec9
---

*Cristiano Ronaldo during Portugal’s losing game against Spain earlier this month. Source: Imagn Images via Reuters Connect*

Football fans wagered more than US $14 billion on the FIFA World Cup through prediction markets Polymarket and Kalshi, a Bellingcat analysis has found.

## Support Bellingcat

Your donations directly contribute to our ability to publish groundbreaking investigations and uncover wrongdoing around the world.

On the crypto-based Polymarket, which provides more information about individual trading accounts than its rival American site Kalshi, we also found that just 1% of users collected the vast majority of winnings during the tournament.

Users traded on almost 60,000 outcomes across both sites during the competition, betting on everything from the sponsor of the Golden Boot winner to whether Cristiano Ronaldo would shed a tear during a Portugal match.

The World Cup, held in the US, Canada and Mexico over June and July, was forecast to be the biggest betting event in history, with a predicted $50 billion in wagers.

Unlike traditional sports betting sites, prediction markets resemble stock exchanges where users trade, via an order book, on whether a real-world event will happen. Prices fluctuate based on what the market believes the probability of that event is. The sites charge fees on each sports trade.

*With 48 teams playing 104 games, the World Cup was slated to be the biggest gambling event of all time. Source: Polymarket*

The prediction market industry has faced criticism over its vulnerability to insider trading, potential market manipulation and concerns about fueling unregulated gambling.
*The Wall Street Journal*
also
[reported](https://www.wsj.com/finance/investing/polymarket-kalshi-betting-profits-prediction-markets-eb23ac11)
in May that a small number of individuals using algorithmic trading models were taking home an outsized share of winnings.

This would appear to align with Bellingcat’s World Cup analysis, where a small percentage of accounts made most of the winnings. However, the level of detail we were able to obtain did not allow us to see accounts that had utilised algorithmic methods.

Both
[Polymarket](https://gamma-api.polymarket.com/)
and
[Kalshi](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
make events and volume data available for programmatic extraction – making it useful for open source analysis. Bellingcat’s data analysis examined all 104 matches as well as the World Cup winner event that was hosted on each platform.

On Polymarket, users traded a total of $10 billion ($5.7 billion on individual games and $4.3 billion on which country would win). The largest game on Polymarket was the Spain vs Argentina final ($212 million), followed by the France vs Spain semi-final ($165 million) and the England vs Argentina semi-final ($142 million).

On Kalshi, users traded a total of more than $4.3 billion ($4.1 billion on the games and $200 million on the winner).

Bellingcat’s analysis also found that 1% of Polymarket trading accounts collected 86% of all winnings during the World Cup, and the bottom 50% of winners shared just 0.1% of profits. The typical winning account on Polymarket made $21, while the typical losing account lost $32 (measured by the median, which is less affected by a handful of exceptionally large wins and losses). More than 12% of traders (14,500) who bet on two or more games lost every bet. The Polymarket
[account](https://polymarket.com/@0x2c335066fe58fe9237c3d3dc7b275c2a034a0563-1759935795465)
that won the most across all games made a profit of more than $13 million, while the biggest loser
[lost](https://finance.yahoo.com/markets/crypto/articles/polymarket-trader-loses-over-11-053505616.html)
$11.6 million.

We were unable to run the same win-loss analysis for Kalshi because trading account overviews are not publicly available.

The top teams, by trading volume, across both sites were Argentina ($1.068 billion), Spain ($876 million) and France ($836 million). The top players were Argentina’s Lionel Messi ($40 million), France’s Kylian Mbappé ($36 million) and Norway’s Erling Haaland ($16 million).

## How We Calculated the Volume

Polymarket displays the actual traded volume on its site, the total US dollar amount of shares bought and sold since the market started.

Kalshi does not display the traded volume. Instead, it shows the notional volume, which counts every contract traded at the maximum payout value of $1. This means that a token bought for $0.20 will be presented as $1 extra in a user’s displayed volume. This makes the total monetary volume appear higher on Kalshi’s website. To achieve a fair comparison between both platforms, we implemented a heuristic to reconstruct Kalshi’s markets’ volume. We used the daily average price for each market over their duration and multiplied it by the number of contracts traded on that day, the sum of which gives us the values used in this piece. We applied this formula for the more than 21,000 World Cup markets.

---

*Data scraping was supported by*
[*Oxylabs’ Project 4β*](https://oxylabs.io/project-4beta)
*.*

*Bellingcat is a non-profit and the ability to carry out our work is dependent on the kind support of individual donors. If you would like to support our work, you can do so*
[*here*](https://www.bellingcat.com/donate/)
*. You can also subscribe to our Patreon channel*
[*here*](https://www.patreon.com/bellingcat)
*. Subscribe to our*
[*Newsletter*](https://bellingcat-newsletter.beehiiv.com/?modal=signup)
*and follow us on Bluesky*
[*here*](https://bsky.app/profile/bellingcat.com)
*, Instagram*
[*here*](https://www.instagram.com/bellingcatofficial/)
*, Reddit*
[*here*](https://www.reddit.com/r/bellingcat/)
*and YouTube*
[*here*](https://www.youtube.com/@bellingcatofficial/videos)
*.*