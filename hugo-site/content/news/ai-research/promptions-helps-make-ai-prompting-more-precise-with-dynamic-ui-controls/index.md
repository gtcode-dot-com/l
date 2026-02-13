---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T18:30:26.292939+00:00'
exported_at: '2026-02-13T18:30:29.245837+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/promptions-helps-make-ai-prompting-more-precise-with-dynamic-ui-controls
structured_data:
  about: []
  author: ''
  description: 'Promptions helps developers add dynamic, context-aware controls to
    chat interfaces so users can guide generative AI responses. It lets users shape
    outputs quickly without writing long instructions:'
  headline: Promptions helps make AI prompting more precise with dynamic UI controls
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/promptions-helps-make-ai-prompting-more-precise-with-dynamic-ui-controls
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Promptions helps make AI prompting more precise with dynamic UI controls
updated_at: '2026-02-13T18:30:26.292939+00:00'
url_hash: 12f6478b7ca3e5faed61990730f82bb2218c2083
---

![Three white line icons on a blue-to-green gradient background: a hub-and-spoke network symbol on the left, a laptop with a user icon in the center, and a connected group of three user icons on the right.](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/Promptions-BlogHeroFeature-1400x788-1.jpg)

Anyone who uses AI systems knows the frustration: a prompt is given, the response misses the mark, and the cycle repeats. This trial-and-error loop can feel unpredictable and discouraging. To address this, we are excited to introduce
**Promptions**
(
*prompt + options*
), a UI framework that helps developers build AI interfaces with more precise user control.

Its simple design makes it easy to integrate into any setting that relies on added context, including customer support, education, and medicine. Promptions is available under the MIT license on
[Microsoft Foundry Labs
(opens in new tab)](https://labs.ai.azure.com/projects/promptions/)
and GitHub.

## Background

Promptions builds on our research, “
[Dynamic Prompt Middleware: Contextual Prompt Refinement Controls for Comprehension Tasks](https://www.microsoft.com/en-us/research/publication/dynamic-prompt-middleware-contextual-prompt-refinement-controls-for-comprehension-tasks/)
.” This project examined how knowledge workers use generative AI when their goal is to
*understand*
rather than
*create*
. While much public discussion centers on AI producing text or images, understanding involves asking AI to explain, clarify, or teach—a task that can quickly become complex. Consider a spreadsheet formula: one user may want a simple syntax breakdown, another a debugging guide, and another an explanation suitable for teaching colleagues. The same formula can require entirely different explanations depending on the user’s role, expertise, and goals.

A great deal of complexity sits beneath these seemingly simple requests. Users often find that the way they phrase a question doesn’t match the
[level of detail the AI needs](https://www.microsoft.com/en-us/research/publication/what-is-it-like-to-program-with-artificial-intelligence/)
. Clarifying what they really want can require long, carefully worded prompts that are tiring to produce. And because the connection between natural language and system behavior isn’t always transparent, it can be difficult to predict how the AI will interpret a given request. In the end, users spend more time
[managing the interaction itself](https://www.microsoft.com/en-us/research/publication/the-metacognitive-demands-and-opportunities-of-generative-ai/)
than understanding the material they hoped to learn.

## Identifying how users want to guide AI outputs

To explore why these challenges persist and how people can better steer AI toward customized results, we conducted two studies with knowledge workers across technical and nontechnical roles. Their experiences highlighted important gaps that guided Promptions’ design.

Our first study involved 38 professionals across engineering, research, marketing, and program management. Participants reviewed design mock-ups that provided static prompt-refinement options—such as
*length*
,
*tone*
, or
*start with*
—for shaping AI responses.

Although these static options were helpful, they couldn’t adapt to the specific formula, code snippets, or text the participant was trying to understand. Participants also wanted direct ways to customize the tone, detail, or format of the response without having to type instructions.

### Why dynamic refinement matters

The second study tested prototypes in a controlled experiment. We compared the static design from the first study, called the “Static Prompt Refinement Control” (Static PRC), against a “Dynamic Prompt Refinement Control” (Dynamic PRC) with features that responded to participants’ feedback. Sixteen technical professionals familiar with generative AI completed six tasks, spanning code explanation, understanding a complex topic, and learning a new skill. Each participant tested both systems, with task assignments balanced to ensure fair comparison.

Comparing Dynamic PRC to Static PRC revealed key insights into how dynamic prompt-refinement options change users’ sense of control and exploration and how those options help them reflect on their understanding.

### Static prompt refinement

Static PRC offered a set of pre‑selected controls (Figure 1) identified in the initial study. We expected these options to be useful across many types of explanation-seeking prompts.

![Alt text: The Static PRC interface in the user study. It includes dropdowns and radio buttons for selecting expertise level (Beginner to Advanced), explanation length (Short to Long), role of AI (Coach, Teach, Explain), explanation type (End result, Modular, Step-by-step), starting point (High-level or Detailed), and tone (Formal, Informal, Encouraging, Neutral).](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/blog-fig02-staticprc-1.png)


Figure 1: The static PRC interface

### Dynamic prompt refinement

We built the Dynamic PRC system to automatically produce prompt options and refinements based on the user’s input, presenting them in real time so that users could adjust these controls and guide the AI’s responses more precisely (Figure 2).

![Alt text: How users interacted with the Dynamic PRC system. (1) shows a user input prompt of “Explain the formula” [with a long Excel formula] (2) Three rows of options relating to this prompt, Explanation Detail Level, Focus Areas, and Learning Objectives, with several options for each, preselected (3) User has modified the preselected options by clicking Troubleshooting under Learning Objectives (4) AI response of an explanation for the formula based on the selected options (5) Session chat control panel with text box that the user adds ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/blog-fig03-dynamicprc-1.png)


Figure 2. Interaction flow in the Dynamic PRC system. (1) The user asks the system to explain a long Excel formula. (2) Dynamic PRC generates refinement options: Explanation Detail Level, Focus Areas, and Learning Objectives. (3) The user modifies these options. (4) The AI returns an explanation based on the selected options. (5) In the session chat panel, the user adds a request to control the structure or format of the response. (6) Dynamic PRC generates new option sets based on this input. (7) The AI produces an updated explanation reflecting the newly applied options.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

## Findings

Participants consistently reported that dynamic controls made it easier to express the nuances of their tasks without repeatedly rephrasing their prompts. This reduced the effort of prompt engineering and allowed users to focus more on understanding content than managing the mechanics of phrasing.

![Alt text: Box plot chart titled “Dynamic vs Static PRC: Which tool…”, comparing user responses to six questions about preference, mental demand, feeling rushed, success, effort, and annoyance. Y-axis ranges from 1 (Dynamic) to 7 (Static), with 4 marked as Equal. Each question is represented by a box plot showing response distribution, median, and variability, illustrating perceived differences between dynamic and static PRC tools.](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/blog-fig04-plotpreferences-1.png)


Figure 3. Comparison of user preferences for Static PRC versus Dynamic PRC across key evaluation criteria.

Contextual options prompted users to try refinements they might not have considered on their own. This behavior suggests that Dynamic PRC can broaden how users engage with AI explanations, helping them uncover new ways to approach tasks beyond their initial intent. Beyond exploration, the dynamic controls prompted participants to think more deliberately about their goals. Options like “Learning Objective” and “Response Format” helped them clarify what they needed, whether guidance on applying a concept or step-by-step troubleshooting help.

![Alt text: Box plot chart titled “Dynamic vs Static PRC: Control Effectiveness,” comparing user agreement with four statements about AI control tools. Each statement has two box plots—blue for Dynamic and orange for Static—showing response distributions on a 1 (Strongly Disagree) to 7 (Strongly Agree) Likert scale. Statements assess perceived control over AI output, usefulness for understanding, desire for more control, and clarity of control functions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/blog-fig05-ploteffectiveness-1.png)


Figure 4. Participant ratings comparing the effectiveness of Static PRC and Dynamic PRC

While participants valued Dynamic PRC’s adaptability, they also found it more difficult to interpret. Some struggled to anticipate how a selected option would influence the response, noting that the controls seemed opaque because the effect became clear only after the output appeared.

However, the overall positive response to Dynamic PRC showed us that Promptions could be broadly useful, leading us to share it with the developer community.

### Technical design

Promptions works as a lightweight middleware layer that sits between the user and the underlying language model (Figure 5). It has two main components:

**Option Module**
. This module reviews the user’s prompt and conversation history, then generates a set of refinement options. These are presented as interactive UI elements (radio buttons, checkboxes, text fields) that directly shape how the AI interprets the prompt.

**Chat Module.**
This module produces the AI’s response based on the refined prompt. When a user changes an option, the response immediately updates, making the interaction feel more like an evolving conversation than a cycle of repeated prompts.

![Alt text: The Promptions system model. (1) The Option Module ingests the user’s prompt input along with the conversation history. (2) It then outputs a set of prompt options, each initialized based on the content of the prompt. (3) These options are rendered inline via a dedicated rendering engine. (4) The Chat Module incorporates the refined options as grounding, alongside the original prompt and conversation history, to generate a chat response. (5) The user can modify the GUI controls, which updates the refinements and triggers the Chat Module to regenerate the current response accordingly.](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/blog-fig07-systemflow-1.png)


Figure 5. Promptions middleware workflow. (1) The Option Module reads the user’s prompt and conversation history and (2) generates prompt options. (3) These options are rendered inline by a dedicated component. (4) The Chat Module incorporates these refined options alongside the original prompt and history to produce a response. (5) When the user adjusts the controls, the refinements update and the Chat Module regenerates the response accordingly.

### Adding Promptions to an application

Promptions easily integrates into any conversational chat interface. Developers only need to add a component to display the options and connect it to the AI system. There’s no need to store date between sessions, which keeps implementation simple. The
[Microsoft Foundry Labs
(opens in new tab)](https://labs.ai.azure.com/projects/promptions/)
repository includes two sample applications, a generic chatbot and an image generator, that demonstrate this design in practice.

Promptions is well-suited for interfaces where users need to provide context but don’t want to write it all out. Instead of typing lengthy explanations, they can adjust the controls that guide the AI’s response to match their preferences.

## Questions for further exploration

Promptions raises important questions for future research. Key usability challenges include clarifying how dynamic options affect AI output and managing the complexity of multiple controls. Other questions involve balancing immediate adjustments with persistent settings and enabling users to share options collaboratively.

On the technical side, questions focus on generating more effective options, validating and customizing dynamic interfaces, gathering relevant context automatically, and supporting the ability to save and share option sets across sessions.

These questions, along with broader considerations of collaboration, ethics, security, and scalability, are guiding our ongoing work on Promptions and related systems.

By making Promptions open source, we hope to help developers create smarter, more responsive AI experiences.

[Explore Promptions on Microsoft Foundry Labs
(opens in new tab)](https://labs.ai.azure.com/projects/promptions/)

Opens in a new tab