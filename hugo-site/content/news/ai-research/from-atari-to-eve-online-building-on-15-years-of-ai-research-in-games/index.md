---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-27T18:30:19.503225+00:00'
exported_at: '2026-09-27T18:30:23.738541+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games
structured_data:
  about: []
  author: ''
  description: Google DeepMind partners with game developers to build generalist agents
    like SIMA 2 and unlock breakthrough gameplay experiences across persistent worlds.
  headline: 'From Atari to EVE Online: Building on 15 Years of AI Research in Games'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'From Atari to EVE Online: Building on 15 Years of AI Research in Games'
updated_at: '2026-09-27T18:30:19.503225+00:00'
url_hash: e42b7af4138c252fa082a7edb74440c920506e92
---

From Atari to Go to StarCraft, games have driven some of the biggest breakthroughs in AI. Now, weâre partnering with game developers to prototype new gameplay experiences that push the frontiers of both gaming and AI.

Since DeepMindâs foundation in 2010, the constrained yet rich worlds of games have played a critical role in understanding intelligence. They have driven some of our biggest AI breakthroughs, from mastering Atari to helping solve protein structure prediction - and they are still at the heart of what we do.

Gaming is in GDMâs DNA. Demis Hassabis, one of Google DeepMind's founders, is himself a former game developer, as are many of us in the GDM team. Together, we have decades of hands-on experience in game development and a deep respect for the craft of making games.

Weâve always been clear that doing AI research with games requires deep partnership with game developers - like our major new
[research partnership with Fenris Creations](https://fenris.com/news/2026/studio-behind-eve-online-goes-independent-rebrands-as-fenris-creations-enters-research-partnership-with-google-deepmind)
and the EVE Universe that we unveiled earlier this year, and the work weâve done together with acclaimed studios like
[Hello Games](https://hellogames.org/)
,
[Coffee Stain Studios](https://coffeestain.com/)
,
[Foulball Hangover](https://www.foulballhangover.com/)
and others.

## Games as the engine of AI research

Our journey began when a small team trained a deep neural network to play Atari 2600 games directly from raw pixels. The Deep Q-Network (DQN) learned to play 49 different games â from
*Pong*
to
*Breakout*
to
*Space Invaders*
â without any game-specific engineering. The
[2015 Nature paper](https://www.nature.com/articles/nature14236)
on DQN helped catalyze the modern era of deep reinforcement learning.

From there, we attempted to master more complex games, with each milestone producing more capable and general systems.
[AlphaGo](https://deepmind.google/research/breakthroughs/alphago/)
defeated world champion Go player Lee Sae Dol in 2016 â a feat many experts thought was still a decade away.
[AlphaGo Zero](https://www.nature.com/articles/nature24270)
surpassed every previous version by learning entirely from self-play, with no human data at all.
[AlphaZero](https://www.science.org/doi/10.1126/science.aar6404)
generalized this approach to master chess, shogi, and Go with one algorithm, while
[MuZero](https://www.nature.com/articles/s41586-020-03051-4)
learned to play without even knowing the rules. In 2019,
[AlphaStar](https://www.nature.com/articles/s41586-019-1724-z)
reached Grandmaster level in
*StarCraft II*
, navigating real-time complexity and imperfect information.

For each game, AI enriched the playing experience. AlphaGo's famous
[Move 37](https://deepmind.google/research/breakthroughs/alphago/)
was a play so unexpected that professional commentators initially thought it was a mistake, overturning centuries of received wisdom in Go and inspiring experts to explore new strategies. AlphaZero similarly inspired entirely new lines of play in chess. Crucially, the spirit of exploration that succeeded in games had profound impacts for other AI systems:
[AlphaFold](https://deepmind.google/science/alphafold/)
applied these foundations to help solve the 50-year grand challenge of protein structure prediction, a breakthrough which was recognized with the 2024 Nobel Prize in Chemistry.

## From mastering games to understanding them

Our earlier work demonstrated that AI could master any game given a clear objective and enough training. But the real world doesn't come with scores and rule books â which led us to ask a fundamentally different question: can AI understand and interact with any game world the way a person would?

This is the challenge behind
[SIMA](https://deepmind.google/blog/sima-generalist-ai-agent-for-3d-virtual-environments/)
, our Scalable Instructable Multiworld Agent. Rather than optimizing for a high score, SIMA is a generalist agent that âseesâ what a player would see on screen, understands natural language instructions, and acts through ordinary keyboard and mouse controls â requiring no APIs or source code access.

Powered by Gemini, our frontier AI models,
[SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)
acts as an interactive companion capable of real-time reasoning and conversation. It achieves human-like play across complex 3D research environments and video games including
*No Man's Sky*
,
*Valheim*
,
*Hydroneer*
, and more.

For game developers, a truly general gaming agent would unlock AI capabilities that work with existing games â no modifications to the game code required. This could power entirely new gameplay, from AI companions that genuinely understand the game world to Non-Player Characters (NPCs) that adapt and respond in ways that scripted systems never could.

A general gaming agent could also transform how games are made. During development, when the game changes with every commit, such agents could enable truly robust QA testing. Post-launch, when new content is introduced or players behave unpredictably, they could adapt in real time â generalising to new situations without needing to be re-scripted.

To develop SIMA agents safely and responsibly, we've partnered with acclaimed game studios and we are building a growing portfolio of games for AI research. This allows us to challenge our agents with ever more complex tasks that may one day transfer to solving problems in the real world.