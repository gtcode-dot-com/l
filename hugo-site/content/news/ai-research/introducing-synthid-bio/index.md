---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-07T04:42:05.200093+00:00'
exported_at: '2026-10-07T04:42:06.982844+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-synthid-bio
structured_data:
  about: []
  author: ''
  description: SynthID Bio is a family of watermarking methods developed specifically
    for synthetic biology to strengthen biosecurity and scientific integrity.
  headline: Introducing SynthID Bio
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-synthid-bio
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing SynthID Bio
updated_at: '2026-10-07T04:42:05.200093+00:00'
url_hash: 396b95f3429cd00be03ab452f9bb2d2a88583950
---

## Strengthening biosecurity and information integrity

Biosecurity relies on layered defenses â think of it like a âSwiss cheeseâ defense model, where multiple independent safety measures work in tandem to cover each otherâs blind spots. Safeguards like model-level mitigations and customer vetting each represent critical layers with potential gaps. As a part of our broader
[vision for bioresilience](https://deepmind.google/blog/our-approach-to-bioresilience/)
, SynthID Bioâs watermarking approach serves as an important, tangible verification layer embedded in the biological design itself.

*âSynthID Bio is an important piece of the puzzle for tracking the provenance of biological designs,â said Sarah Carter, a biosecurity policy expert and Principal at Science Policy Consulting who reviewed the work. âBy linking designs to the model developer, these watermarks empower developers to lead on safety and allow synthesis providers to streamline screening for customers who have used those models.â*

That layer is especially vital to DNA synthesis screening, which sits on the frontlines of biosecurity. Converting digital protein designs into physical molecules requires placing an order with DNA synthesis providers, who screen requests against databases of known threats. For example, historically, an unfamiliar sequence may have been safely assumed to be an undiscovered natural organism. But because AI can create
[entirely new sequences with little resemblance to known hazards,](https://www.science.org/doi/10.1126/science.adu8578)
screeners can no longer make that assumption. Verifying that an unfamiliar order isn't an engineered threat requires exhaustive manual reviews that can stall vital research. Here, SynthID Bio can provide an automated verification signal, proving an order originated from a trusted model with built-in safeguards.

*"AI is expanding what scientists can design, and DNA synthesis companies have an important role in helping that innovation scale responsibly,â said James Diggans, Vice President, Policy and Biosecurity at Twist Bioscience, who provided early feedback on the paper. âFor Twist, watermarking offers a promising new addition to the biosecurity toolbox that could strengthen screening, focus resources on sequences that warrant closer review and make biosecurity more efficient as AI-designed biology continues to advance."*

Similarly, SynthID Bio could help maintain the integrity of databases such as the Protein Data Bank, UniProt, and GenBank. These databases, many of which are open to public submission, play a vital role in scientific advancements â but mislabeled entries can have an
[outsized negative impact in biosecurity decision-making](https://www.nature.com/articles/s41598-023-32481-z)
, a challenge that may only grow with the addition of AI-generated biological data. As a part of the submission process, SynthID Bio could help ensure synthetic entries are properly labeled or flagged for further review.

## Looking ahead

While no single biosecurity intervention is a silver bullet, SynthID Bio brings
[SynthID](https://deepmind.google/models/synthid/)
, our tried and tested watermarking tool, to synthetic biology. Itâs an important first step toward reliably identifying and tracking AI-generated biological sequences and structures.

Moving forward, key challenges include making the watermark more robust against deliberate tampering. SynthID Bio can also be paired with provenance
[metadata](https://www.nti.org/analysis/articles/white-paper-a-proposal-for-biodesign-metadata-exchange-for-use-in-biosecurity/)
approaches â similar to
[C2PA](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/)
for digital media â or
[central repositories of AI-generated biological data](https://www.science.org/doi/10.1126/science.ado1671)
to better identify and track AI-generated proteins.

To match the growing capabilities of frontier AI technology, weâre also researching how to apply watermarking to more complex biological objects. In ongoing work with the
[Hie lab](https://evodesign.org/)
at Stanford University and Arc Institute, we integrated SynthID Bio into Evo 2, an advanced genomic model, to watermark the genome of an
[Evo 2 designed bacteriophage](https://www.science.org/doi/10.1126/science.aec2657)
. Early laboratory testing in bacteria cultures has confirmed these watermarked bacteriophages are functional. We believe this work has the potential to address some of the
[biosecurity risks](https://www.science.org/doi/10.1126/science.aej8512)
associated with genome design and will share more details in a technical manuscript soon.

Realizing the full biosecurity benefits of this work will require community collaboration and further research. As part of our commitment to responsible innovation, we are publishing our
[methods paper](http://www.nature.com/articles/s41586-026-10965-y)
and open-sourcing the code and
*in vitro*
data, and releasing the weights to the research community, so we can build on this work. By working openly with partners across biosecurity, gene synthesis, and policy, we can ensure safety and responsibility keeps pace with AI-driven discovery.

*To reach out about partnering with us on this important topic, please contact us at*
[*synthidbio@google.com*](mailto:synthidbio@google.com)
*with a high level proposal. Please do not disclose any confidential or proprietary information.*