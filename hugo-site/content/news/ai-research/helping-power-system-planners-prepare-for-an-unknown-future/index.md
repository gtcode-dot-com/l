---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-04T00:03:19.685852+00:00'
exported_at: '2025-12-04T00:03:21.957091+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/helping-power-system-planners-prepare-unknown-future-1203
structured_data:
  about: []
  author: ''
  description: Macro, a new modeling tool developed by the MIT Energy Initiative,
    enables energy system planners to explore options for developing infrastructure
    to support decarbonized, reliable, and low-cost power grids.
  headline: Helping power-system planners prepare for an unknown future
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/helping-power-system-planners-prepare-unknown-future-1203
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Helping power-system planners prepare for an unknown future
updated_at: '2025-12-04T00:03:19.685852+00:00'
url_hash: ac3bdd188ef201a6ce12a9f8021e796bb92a18fc
---

A new computer modeling tool developed by an MIT Energy Initiative (MITEI) research team will help infrastructure planners working in the electricity and other energy-intensive sectors better predict and prepare for future needs and conditions as they develop plans for power generation capacity, transmission lines, and other necessary infrastructure. The tool could reduce the amount of time this planning takes and help ensure that the power grid can continue to provide customers with efficient, reliable, and low-cost electricity that meets emissions and regulatory standards. The tool was developed as part of a philanthropically supported research project through MITEI, in collaboration with Princeton University and New York University.

Macro, the new tool, is specially designed for utility planners, regulators, and researchers who are trying to understand how electricity grids and other energy sectors might evolve given new technologies and policies or different ways of using electricity and energy-intensive commodities, explains MITEI research scientist Ruaridh Macdonald. By entering details about available generating units, projected demand, costs, possible new technologies, and potential policy constraints, planners can investigate various options for the design and operation of future infrastructure that will minimize prices and maximize value for everyone. In particular, unlike traditional models, Macro accounts for co-dependencies between industrial sectors.

With further development, Macro will enable policymakers to explore — in real time — the impacts of potential policy options on outcomes ranging from carbon emissions to grid reliability to commodity prices, and more.

**Utility planners’ growing challenge and previous MIT models**

The demand for electricity is now skyrocketing, due in part to the increasing use of artificial intelligence and the electrification of everything from vehicles to buildings. As a result, more power generation and transmission will be required. Thousands of wind and solar energy projects are now coming online, but those units can’t be counted on to generate electricity all the time, so complementary power sources and storage facilities are needed. In addition, energy consumers such as data centers, manufacturing centers, and hospitals have strict reliability requirements that must be met. Further complicating the planner’s task is the commitment to reducing, or even eliminating, carbon emissions.

Macro builds on a history of capacity expansion models (CEMs), including GenX and DOLPHYN, that have been developed by MITEI researchers to help utilities plan for the future. GenX was designed in 2017 to support decision-making related to power system investment, as well as real-time grid operation, and to examine the impacts of possible policy initiatives on those decisions. DOLPHYN, released in 2021, has the same core structure as GenX but with additional sectors added on, including production of hydrogen, biofuels, and more.

However, Macdonald; Jesse Jenkins, one of the creators of GenX and now a professor at Princeton University; and Dharik Mallapragada, one of the creators of DOLPHYN and now a professor at New York University, realized that they needed to build larger and higher-resolution models than GenX or DOLPHYN are capable of in order to get more accurate answers about the impacts of policies and new technologies.

**Introducing Macro**

Macdonald, Jenkins, and Mallapragada, alongside Princeton collaborators Filippo Pecci and Luca Bonaldo, came up with a new architecture that provides the needed extended capabilities. In building Macro, they and their teams developed a set of four core components that can be combined to describe the energy system for any industrial process. “The components each describe basic actions in an energy system: transfer, storage, transformation, and entering or exiting the network,” explains Macdonald. “Because the components are not sector-specific, we are able to use them to build networks of electricity, commodity, and data systems.” With Macro, users can focus on specific areas of the economy, for example, for interregional transfer of electricity or commodities. This flexibility has led other research groups to begin using Macro for their own projects. “In fact, we already have some people looking at cement production and production of certain chemicals,” says Macdonald.

Moreover, with Macro the user can break a problem into smaller pieces. Most software used for this type of modeling is designed to run on one computer. “With Macro’s new architecture, we can easily decompose a large problem into many small problems, which we can run on separate computers,” says Macdonald. That makes Macro well-suited to running on modern high-performance computing clusters. It also provides an added benefit when it comes to power system planning. Certain aspects of expansion — for example, transmission — are too complex to be solved using conventional optimization methods, so most CEMs assume certain approximations. But with Macro, the transmission piece can be separated from the rest of the problem and solved separately using AI techniques, generating a more accurate solution that can then be fed into the overall model.

In addition, Macro’s developers placed great emphasis on ease of use. They developed a “taxonomy” of potential users and simplified the workflow of each group as much as possible. Most users just want to plug in their data using Excel and other tools they are familiar with, do an analysis of some problem, and get an answer. Others are modelers who want to add a new technology or policy; those people might need to write some added computer code — but not much. Finally, there are developers who want to add new features or large elements to the model and will need to do a lot of coding. “We’ve structured things in Macro so that life is a lot easier for the first two groups of users, at the cost of it being a bit harder for the developers,” says Macdonald. The team is now developing a graphical interface for the model so most people won’t ever have to use code. “They’ll just interact with it like they do with most software they use.”

**Future plans: Using Macro to guide policymaking — in real time**

Christopher Knittel, the George P. Shultz Professor at the MIT Sloan School of Management, plans to use Macro to design energy policy. His vision is inspired by the experience of Professor John Sterman of MIT Sloan, who led the development of the global climate simulator “En-ROADS,” as well as a system dynamics model that performs quick but approximate analyses, enabling users to try out — in real-time — different approaches to reducing carbon emissions.

As with the global climate simulator, using Macro to perform a complete analysis of a proposed policy can take days. But there are techniques for creating an “emulator” that could generate an approximate result in a matter of seconds. In his role as director of the “Enabling New Policy Approaches” mission of the MIT Climate Project, Knittel is exploring the possibility of supporting a “flagship project” to build an emulator to go on top of the full Macro model that could run in real time. Knittel and his team would then meet with select policymakers and invite them to use Macro to see how various policy steps would affect global temperatures, greenhouse gas concentrations, energy prices, sea-level rise, and so on.

In using the emulator “you lose some accuracy or some capabilities of the full Macro model,” Knittel notes, so he envisions letting members of Congress start by running the emulator to design a policy. “Then, before the legislator actually drafts the bill, the academic team would run the full Macro model to confirm the accuracy of the results from the emulator,” says Knittel. “That exercise could help convince policymakers what policy levers they should be pulling.”

Macro has been released as open-source software, freely available for research and commercial purposes. It has been tested by collaborators in the United States, South Korea, India, and China. Several of those teams are developing country and regional models for others to make use of in their work.