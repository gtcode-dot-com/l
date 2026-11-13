---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-13T19:23:48.874403+00:00'
exported_at: '2026-11-13T19:23:52.012067+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/new-ai-copilot-helps-engineers-design-better-structures-1113
structured_data:
  about: []
  author: ''
  description: MIT researchers are making algorithmic designs more collaborative with
    a system that acts like an AI copilot for engineers. As the algorithm is generating
    the structure, it presents regions to the human designer for feedback.
  headline: New AI “copilot” helps engineers design better structures
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/new-ai-copilot-helps-engineers-design-better-structures-1113
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New AI “copilot” helps engineers design better structures
updated_at: '2026-11-13T19:23:48.874403+00:00'
url_hash: 606399e29c9ee7e90e0ce6fa5828edcccd9078b2
---

The system asks humans for feedback to increase trust in machine-generated designs for buildings and bridges.

The use of algorithms to design structures has led to new parts optimized for ultralight aircraft, high-bandwidth antennas, and F1 racing cars.

But the best algorithmic design techniques still require lots of computation and time: Users only see the final design after it’s complete, after which they often must start the design process all over again to make changes. That process also makes it harder to trust that the final designs are structurally sound.

MIT researchers are making algorithmic designs more collaborative with a system that acts like an AI copilot. As the algorithm is generating the structure, it presents regions to the human designer for feedback.

In an open-access
[*Communications Engineering paper*](https://www.nature.com/articles/s44172-026-00818-x)
describing the system, the researchers showed it led to more easily manufacturable structures with higher buckling loads while adding only 15 seconds to the total design time compared to all-algorithmic approaches.

The researchers believe the approach, which uses a design technique known as topology optimization, could make algorithmic design more accessible and manufacturable for a broader class of design engineers.

“Right now, the human doesn’t have any agency or control over the design process as it’s playing out,” explains lead author Dat Ha PhD ’26, a recent MIT civil and environmental engineering doctoral student who is now a structural designer at LeMessurier. “For these really complex designs, we wanted to also tap into our brain, which is the most complex machine there is, to solve these design problems in a way that’s more practical to industry.”

Joining Ha on the paper are Ferdous Alam, a former MIT postdoc who is now an assistant professor at Georgia Tech; Markus Buehler, the MIT Jerry McAfee (1940) Professor of Engineering; Faez Ahmed, MIT associate professor of mechanical engineering; and senior author Josephine Carstensen, MIT associate professor of civil and environmental engineering.

**Bringing a human in the loop**

Topology optimization is one of the most advanced and promising algorithmic design techniques. It uses formal optimization techniques to iteratively fill in the space given for a design in a way that maximally achieves the stated goals. For most applications, the process requires a lot of computation and time. When it’s finally done, the designs can be impractical to build or have other issues the engineer didn’t consider. For instance, some designs might have eight or more beam connections at a single point, which would be difficult to make in the real world.

“Engineers are always very skeptical of computer programs, especially if they give you very weird-looking or unexpected designs,” Ha says. “On paper, topology optimization is really powerful and can achieve great, high-performing designs, but its black box nature has made it less widely adopted in industry.”

Topology optimization has gotten traction in the automotive and aerospace industries, but it’s been used less to design buildings or bridges, partly because design engineers need to know they can trust the output.

“A big limiting factor has been that the design engineer has very little influence over how the design evolves and therefore can’t control undesirable features,” Carstensen explains. “The lack of control and lack of ownership also inhibits its use.”

To address those problems, the researchers made topology optimization more collaborative in an approach that Carstensen compares to having a design copilot.

Prior attempts at adding human judgment slowed things down dramatically. The researchers’ new system uses machine learning to quickly identify the most likely regions of an algorithmic design that a human would want to change. To train the machine-learning model, the researchers created a synthetic dataset of probable human feedback to thousands of designs that critiqued things like aesthetics, performance criteria, and manufacturability.

“We thought if we could create a record of where humans have made changes to these programs, then perhaps there’s a pattern to those choices, which is not very different from other types of machine-learning approaches,” Ha says.

Carstensen sees the system as bringing together the best of algorithmic and human design approaches.

“The idea is to tap into the brains of the designers and get them to infuse their domain knowledge as the design evolves,” Carstensen says.

In demonstrations, the researchers showed their human-in-the-loop approach improved manufacturability and linear buckling load by 39 percent while only modestly increasing the total design time.

Right now, the approach only allows users to make structures within identified regions thicker or thinner, but they hope to add other options for modification in future versions.

“The hope is that by addressing these hurdles, we open up topology optimization to a much wider audience, not only in industry but also to researchers and students in academia,” Carstensen says.

**From designs to structures**

The researchers see their approach complementing AI only-approaches to design.

“We are arguing there’s room for both,” Carstensen says. “If you are in a discipline that has a lot of computational resources, you can use the other approach. But if you really need the human input, you can use this collaborative approach.”

Adding human input also serves to increase trust.

“In some settings, the humans need to make the final decisions before advancing the final design,” Carstensen says. “By involving humans, we can get higher-performing designs to the real world to create higher-performing structures. Because it’s not just about designing good artifacts; it’s about creating good artifacts that humans will actually accept and make.”

The work was supported, in part, by the MathWorks Engineering Fellowship Fund, TATA Steel, and the MIT Generative AI Impact Consortium.