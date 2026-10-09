---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-11T03:42:49.236464+00:00'
exported_at: '2026-06-11T03:42:51.953464+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/nuclear-inspired-cooling-system-ferveret-could-make-data-centers-more-sustainable-0610
structured_data:
  about: []
  author: ''
  description: The startup Ferveret, founded by MIT Associate Professor Matteo Bucci
    and former MIT postdoc Reza Azizian, reduces the energy required to cool chips
    in data centers that power AI.
  headline: Startup’s nuclear-inspired cooling system could make data centers more
    sustainable
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/nuclear-inspired-cooling-system-ferveret-could-make-data-centers-more-sustainable-0610
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Startup’s nuclear-inspired cooling system could make data centers more sustainable
updated_at: '2026-06-11T03:42:49.236464+00:00'
url_hash: 76b0d1e55219f9fbd2e08be8d941cf967657c7a8
---

The rise of artificial intelligence is riding on the back of an enormous data center expansion. Data centers are
[projected](https://www.epri.com/about/media-resources/press-release/trb5wwt7oemdbkaamxrccqkq2ktteae8)
to account for anywhere from 9 to 17 percent of total electricity usage in the U.S. by the end of the decade. Today, around a third of data center electricity is devoted to cooling the chips that run AI models.

That’s the process Ferveret is working to make more efficient. The startup, founded by Reza Azizian, a former MIT postdoc in nuclear engineering, and Matteo Bucci, MIT’s Esther and Harold E. Edgerton Associate Professor in the Department of Nuclear Science and Engineering, is adapting an approach from nuclear reactors to cool chips using no water and significantly less electricity.

The company’s cooling system submerges computer servers in a specialized liquid that absorbs heat much more efficiently than air from a fan. What makes the solution different from other liquid cooling systems are the bubbles: Ferveret’s Adaptive Phase Cooling (APC) solution produces much smaller bubbles at the surface of the server, which detach more frequently, accelerating the heat transfer process.

Ferveret is already testing its solutions with companies including CleanSpark, the data center developer and operator, as well as FuriosaAI, an AI accelerator company, and Switch, one of the largest data center operators in the U.S.

In a recent study in collaboration with the Samueli Computer Science Department at the University of California at Los Angeles, Ferveret found its APC solution led to a 15 percent improvement in computational power efficiency compared to state-of-the-art liquid cooling solutions. By combining those savings with Ferveret’s power control system to optimize operating conditions, the company says it allows data centers to get 35 percent more tokens — small pieces of text or data — from their AI models with the same amount of power.

“Our goal is to make data centers as sustainable as possible and help them use every single watt of power to generate tokens, which are the most useful outputs,” Azizian says. “Our system enables the operation of more powerful chips, it helps data centers waste a lot less energy, and it accomplishes all that with zero water consumption.”

**From nuclear reactors to AI**

Azizian was a postdoc at MIT in 2013 when he met Bucci, who was then a research scientist. They worked on heat transfer in nuclear reactors before Azizian went into industry, where he shifted his focus to cooling chips. Azizian first worked on Microsoft’s HoloLens augmented reality headset and then joined Nvidia, which produces the graphical processing units companies use to train and run the latest AI models. Meanwhile, Bucci continued conducting research at MIT, becoming an assistant professor in 2016.

Azizian walked into his first data center in 2017, where he was struck by the massive, noisy fans that filled the building as they cooled.

“I thought, ‘Holy crap, this is not how you cool facilities,’” Azizian recalls, noting air cooling can still take up 40 percent of the power going into a data center. “It was not an efficient way of doing things, but since it wasn’t hurting the performance, no one cared that the cooling technology was 50 years old.”

Azizian began talking with Bucci about applying their knowledge around optimizing heat transfer in nuclear reactors to data centers. Scientists have spent decades finding better ways to move heat in nuclear reactors.

“Heat transfer determines how much energy you can extract from the reactor core, which translates directly to revenue,” Azizian explains.

The founders started Ferveret in 2021. A lot has changed since Azizian walked into his first data center. Chip companies have packed more and more components onto their chips as the explosion in artificial intelligence has put a premium on squeezing as much computing capacity as possible out of limited power supplies.

That has driven data center operators to use liquid to cool chips — often through a technique known as immersion cooling that submerges chips in liquid. The most effective form of immersion cooling brings the liquid to a boil.

“Liquid is a better heat transfer medium than air. That’s why when you stick your hand into room temperature water it still feels cold,” Bucci explains. “When liquid is boiling, it becomes even better at removing heat because the phase change requires a lot of energy, which is the energy you remove from the chip. That lets you transfer large quantities of heat with minimal temperature differences between the chips and the liquid.”

Unfortunately, boiling liquid adds complexity to the system because it forces operators to capture and reliquefy the bubbles while controlling for pressure, temperature, and fluid inventory.

Ferveret’s system is adapted from a process in nuclear reactors called subcooled boiling. It uses a liquid with a low boiling point and none of the toxic PFAS “forever chemicals” that other approaches rely on. At the surface of the chip, Ferveret’s liquid produces smaller bubbles than other immersion cooling approaches. Those bubbles detach more frequently and quickly recondense in the surrounding liquid, accelerating the bubble-rewetting cycle at the surface of the chip to hasten heat transfer.

Ferveret delivers its APC system in small boxes, each of which houses one server. The founders say their modular systems make it easier to deploy the system and simplify maintenance.

“The physics enable us to get to form factors that weren’t possible in the past,” Azizian says. “Most immersion cooling solutions are large tanks that people submerge the servers in. We have a smaller, modular rack-mounted solution that makes it adaptable to the current infrastructure, so it’s easier for people to deploy our technology.”

Ferveret also offers control software that adjusts the power going to each server in real-time to further improve efficiency.

“We deliver full-stack systems that include the cooling box, the rack, the cooling distribution units, and sensors that measure the temperature and pressure,” Bucci says. “Our software monitors those sensors and optimizes the operating condition inside each box to ensure that energy consumption is minimized in the system.”

**AI with fewer resources**

In addition to helping data centers to run more efficiently, Ferveret is also improving sustainability by making it easier to operate data centers in remote regions with more renewable energy.

“The sun shines in places where you don’t have much water, so the advantage of us being water-free is we allow you to build data centers where you have solar energy but nothing to cool the data center down,” Bucci says. “This technology can help deploy data centers in regions where normally you wouldn’t have the resources to do so, including Africa, the Middle East, and of course parts of America. It’s a huge unlock.”

Ferveret is in talks with the large cloud computing companies known as hyperscalers, and is currently part of Nvidia’s Inception program for startups. The company plans to announce expanded partnerships later this year. From there, the founders plan to quickly scale their technology to help the AI industry continue to grow without further straining the planet.

“The computing industry is facing a huge challenge in the form of access to power, and they have a problem with access to water in many regions,” Azizian says. “That will only become more limiting as the industry grows. The main goal for these data center operators would be to get more tokens from the power they have. We’ve shown we can do that.”