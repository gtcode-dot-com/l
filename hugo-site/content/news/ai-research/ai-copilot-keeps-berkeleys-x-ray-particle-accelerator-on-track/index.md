---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-17T12:15:27.683830+00:00'
exported_at: '2026-01-17T12:15:30.363014+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator
structured_data:
  about: []
  author: ''
  description: In the rolling hills of Berkeley, California, an AI agent is supporting
    high-stakes physics experiments at the Advanced Light Source (ALS) particle accelerator.
    Researchers at the Lawrence Berkeley National Laboratory ALS facility recently
    deployed the Accelerator Assistant, a large language model (LLM)-driven system
    to keep X-ray research on track. The Accelerator Assistant — powered by  Read
    Article
  headline: AI Copilot Keeps Berkeley’s X-Ray Particle Accelerator on Track
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: AI Copilot Keeps Berkeley’s X-Ray Particle Accelerator on Track
updated_at: '2026-01-17T12:15:27.683830+00:00'
url_hash: 69ad5c33d922d09ab4b62a14dfb7a1e4f10d81ea
---

In the rolling hills of Berkeley, California, an AI agent is supporting high-stakes physics experiments at the Advanced Light Source (ALS) particle accelerator.

Researchers at the Lawrence Berkeley National Laboratory ALS facility recently deployed the Accelerator Assistant, a large language model (LLM)-driven system to keep X-ray research on track.

The Accelerator Assistant — powered by an NVIDIA H100 GPU harnessing CUDA for accelerated inference — taps into institutional knowledge data from the ALS support team and routes requests through Gemini, Claude or ChatGPT. It writes Python and solves problems, either autonomously or with a human in the loop.

This is no small task. The ALS particle accelerator sends electrons traveling near the speed of light in a 200-yard circular path, emitting ultraviolet and X-ray light, which is directed through 40 beamlines for 1,700 scientific experiments per year. Scientists worldwide use this process to study materials science, biology, chemistry, physics and environmental science.

![](https://blogs.nvidia.com/wp-content/uploads/2026/01/paticleaccel.jpg)

At the ALS, beam interruptions can last minutes, hours or days, depending on the complexity, halting concurrent scientific experiments in process. And much can go wrong: the ALS control system has more than 230,000 process variables.

“It’s really important for such a machine to be up, and when we go down, there are 40 beamlines that do X-ray experiments, and they are waiting,” said Thorsten Hellert, staff scientist from the Accelerator Technology and Applied Physics Division at Berkeley Lab and lead author of a
[research paper](https://arxiv.org/pdf/2509.17255)
on the groundbreaking work.

VIDEO

Until now, facility staff troubleshooting issues have had to quickly identify the areas, retrieve data and gather the right personnel for analysis under intense time pressure to get the system back up and running.

“The novel approach offers a blueprint for securely and transparently applying large language model-driven systems to particle accelerators, nuclear and fusion reactor facilities, and other complex scientific infrastructures,” said Hellert.

The research team demonstrated that the Accelerator Assistant can autonomously prepare and run a multistage physics experiment, cutting setup time and reducing efforts by 100x.

## **Applying Context Engineering Prompts to Accelerator Assistant**

The ALS operators interact with the system through either a command line interface or Open WebUI, which enables interaction with various LLMs and is accessible from control room stations, as well as remotely. Under the hood, the system uses Osprey, a framework developed at Berkeley Lab to apply agent-based AI safely in complex control systems.

Each user is authenticated and the framework maintains personalized context and memory across sessions, and multiple sessions can be managed simultaneously. This allows users to organize distinct tasks or experiments into separate threads. These inputs are routed through the Accelerator Assistant, which makes connections to the database of more than 230,000 process variables, a historical database archive service and Jupyter Notebook-based execution environments.

“We try to engineer the context of every language model call with whatever prior knowledge we have from this execution up to this point,” said Hellert.

Inference is done either locally — using Ollama, which is an open-source tool for running LLMs with a personal computer, on an H100 GPU node located within the control room network — or externally with the CBorg gateway, which is a lab-managed interface that routes requests to external tools such as ChatGPT, Claude or Gemini.

The hybrid architecture balances secure, low-latency, on-premises inference with access to the latest foundation models. Integration with EPICS (Experimental Physics and Industrial Control System) enables operator-standard safety constraints for direct interaction with accelerator hardware. EPICS is a distributed control system used in large-scale scientific facilities such as particle accelerators. Engineers can write Python code in Jupyter Notebook that can communicate with it.

Basically, conversational input is turned into a clear natural language task description for objectives without redundancy. External knowledge such as personalized memory tied to users, documentation and accelerator databases are integrated to assist with terminology and context.

“It’s a large facility with a lot of specialized expertise,” said Hellert. “Much of that knowledge is scattered across teams, so even finding something simple — like the address of a temperature sensor in one part of the machine — can take time.”

## **Tapping Accelerator Assistant to Aid Engineers, Fusion Energy Development**

Using the Accelerator Assistant, engineers can start with a simple prompt describing their goal. Behind the scenes, the system draws on carefully prepared examples and keywords from accelerator operations to guide the LLM’s reasoning.

“Each prompt is engineered with relevant context from our facility, so the model already knows what kind of task it’s dealing with,” said Hellert.

Each agent is an expert in that field, he said.

Once the task is defined, the agent brings together its specialized capabilities — such as finding process variables or navigating the control system — and can automatically generate and run Python scripts to analyze data, visualize results or interact safely with the accelerator itself.

“This is something that can save you serious time — in the paper, we say two orders of magnitude for such a prompt,” said Hellert.

Looking ahead, Hellert aims to have the ALS engineers put together a wiki that documents the many processes that go on to support the experiments. These documents could help the agents run the facilities autonomously — with a human in the loop to approve the course of action.

“On these high-stakes scientific experiments, even if it’s just a TEM microscope or something that might cost $1 million, a human in the loop can be very important,” said Hellert.

The work has already expanded beyond ALS as part of the DOE’s Genesys mission, with the framework being deployed across U.S. particle accelerator facilities. Next up, Hellert just began collaborating with engineers at the
[ITER](https://www.iter.org/)
fusion reactor — the world’s largest — in France for implementing the framework for use in the fusion reactor facility. He also has a collaboration in the works with the Extremely Large Telescope ELT, in northern Chile.

## **Benefiting Humanity: Scientific Impact of Experiments Supported by ALS**

Beyond optimizing the accelerator and other industrial operations, the work at the ALS directly enables scientific breakthroughs with global impact. The facility’s stable X-ray beams underpin research in health, climate resilience and planetary science.

During the COVID-19 pandemic, ALS researchers helped characterize a rare antibody that could neutralize SARS-CoV-2. Structural biology experiments at Beamline 4.2.2 revealed how six molecular loops of the antibody latch onto and disable the viral spike protein. The findings supported the rapid development of a therapeutic that remained effective through multiple variants.

ALS science also contributes to climate-focused research. Metal-organic frameworks (MOFs) — a class of porous materials capable of capturing water or carbon dioxide from air — were extensively studied across several ALS beamlines. These experiments supported foundational work that ultimately led to the 2025 Nobel Prize in Chemistry, recognizing the transformative potential of MOFs for sustainable water harvesting and carbon management.

In planetary science, ALS measurements of samples returned from NASA’s OSIRIS-REx mission helped trace the chemical history of asteroid Bennu. X-ray analyses provided evidence that such asteroids carried water and molecular precursors of life to early Earth, deepening our understanding of the origins of the planet’s habitable conditions.