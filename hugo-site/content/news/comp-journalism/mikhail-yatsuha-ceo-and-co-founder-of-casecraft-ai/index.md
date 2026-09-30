---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-30T02:44:09.116292+00:00'
exported_at: '2026-09-30T02:44:11.110596+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/mikhail-yatsuha-ceo-and-co-founder-of-casecraft-ai
structured_data:
  about: []
  author: ''
  description: Mikhail Yatsuha, CEO and Co-Founder of CaseCraft.AI, is a UK solicitor
    and legal technology entrepreneur with more than a decade of experience in legal
    services. He progressed from an intern and trainee solicitor to Part...
  headline: Mikhail Yatsuha, CEO and Co-Founder of CaseCraft.AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/mikhail-yatsuha-ceo-and-co-founder-of-casecraft-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mikhail Yatsuha, CEO and Co-Founder of CaseCraft.AI
updated_at: '2026-09-30T02:44:09.116292+00:00'
url_hash: ea5f8fb6dfb0a55990c864e02bcfe90039a95ad9
---

[Mikhail Yatsuha](https://www.linkedin.com/in/michael-iatsukha/)
, CEO and Co-Founder of CaseCraft.AI, is a UK solicitor and legal technology entrepreneur with more than a decade of experience in legal services. He progressed from an intern and trainee solicitor to Partner at Sterling Law, where he led the commercial department and repeatedly encountered viable lower-value disputes that became uneconomic once traditional legal costs were factored in. At the end of 2023, he co-founded CaseCraft.AI to rethink how civil claims are assessed, prepared and progressed using AI-enabled workflows rather than simply applying AI to legal drafting.

[CaseCraft.AI](http://casecraft.ai)

is a UK legal technology company building an AI-native platform for civil litigation. The platform brings case assessment, evidence processing, pre-action correspondence, document generation, procedural tracking and human legal review into a single workflow, serving individual claimants on a no-win-no-fee basis and businesses through subscription-based bulk-claim and case-management tools. The company raised circ. £1.8m across three funding rounds and, as of August 2026, had recorded 4,562 matters created with cumulative value of £14.9M, 51% had settled or been won on default judgment, and 373 matters in active legal work; it is also piloting its first enterprise deployment and testing an Employment Law MVP.

**You spent years progressing from an intern and trainee solicitor to Partner at Sterling Law before co-founding CaseCraft.AI in 2023. What did you repeatedly see in legal practice that convinced you the small-claims process could be fundamentally redesigned with AI rather than simply made more efficient with better legal software?**

What convinced me was not that lawyers needed a better drafting tool. It was that, for many lower-value disputes, the economics fail before a lawyer can help. The cost of representation can approach or exceed the value at stake, and most legal costs are generally not recoverable in small claims. I saw viable claims abandoned for that reason at Sterling Law, and later saw the same arithmetic with businesses writing off unpaid invoices. That is a delivery-model problem, not a drafting problem. AI made it possible to redesign more of the journey around the person bringing the claim rather than simply make the lawyer working on it a little faster.

**CaseCraft.AI has now been used to create thousands of legal matters, with hundreds progressing into active legal work. What have you learned from operating AI across real cases that you could never have discovered from prototypes, simulations, or benchmark testing alone?**

Two things stand out. First, generating a document is the easy part; running a matter is hard. A live case means evidence, payments, deadlines, responses and next steps have to stay consistent over months. As of August 2026, 4,500+ matters had been created through CaseCraft, 400+ had progressed into active legal work, and 130 claims had been issued at court.

Second, people behave differently with AI. They can be more candid, which helps surface important facts earlier, but the system also has to provide boundaries and know when a human should step in. We learned that directly when introducing a human call at a trust-sensitive stage improved conversion by at least 15%.

**Much of the first wave of generative AI focused on producing text. CaseCraft.AI instead has to gather evidence, determine eligibility, follow procedural rules, trigger actions, and track a matter over time. How does building this type of agentic workflow differ technically from building an AI assistant or chatbot?**

A chatbot answers a question; an agentic workflow has to maintain the state of a real matter over time – what has happened, what evidence exists, what is missing and what can happen next. We therefore think about the system as specialised components rather than one model doing everything: some collect and validate information, others ground legal reasoning or process incoming documents. The objective is not the best paragraph. It is a reliable sequence of decisions and actions that moves the matter towards the best available outcome.

**In a legal workflow, a model can produce something that sounds completely convincing while still being procedurally or factually wrong. How have you designed CaseCraft.AI to distinguish between plausible AI output and information that is actually reliable enough to use in a legal matter?**

The governing principle is that the model does not get to invent the legal universe it is operating in. We constrain the system to the evidence in the matter and to authoritative legal sources, rather than ask a general-purpose model to answer from memory. CaseCraft.AI has access to the latest changes in legislation, relevant precedents and established best practices through government APIs and other authoritative sources, so the legal context is kept current.

We also separate generation from validation and keep professional review inside the regulated legal-service framework. The test is not whether an output sounds like a lawyer wrote it, but whether the source, evidence and procedural step can be verified.

**You have spoken about the importance of “measurable human oversight.” What does that mean in practice, and how do you determine which decisions an AI system can make autonomously versus where a human must remain accountable?**

Measurable human oversight means human involvement is tied to identifiable risk, and we can see where intervention happens and why. ‘Human in the loop’ should not just be a reassuring phrase; we should be able to point to the trigger, the review and the decision that followed.

We are still building the evidence base for where those boundaries should sit. One measure we can already point to is review time: since launch, the time required for human review has decreased fourfold as the system has improved. Over time, the aim is to make review more risk-based, while keeping accountable professional judgement where it is legally required.

**Evidence is central to small claims, but evidence can arrive as contracts, invoices, emails, messages, photographs, and other unstructured information. How do you approach turning that material into structured inputs an AI system can reason over while preserving provenance and avoiding unsupported conclusions?**

The key principle is to keep extraction separate from inference. If a user uploads a WhatsApp thread with a builder, the dates, price quoted, and words used are extracted facts; a conclusion about the legal significance of that exchange is inference. The two should never be presented as the same thing. We structure documents so the workflow can use them while preserving the link back to the original evidence. If that link disappears, you can create a case file that reads well but falls apart when challenged.

**One of the hardest problems for autonomous systems is knowing when not to act. What signals tell CaseCraft.AI that a claim has become too ambiguous, complex, or risky for automation and should instead be escalated to a legal professional?**

One of our safeguards is counterintuitive: we pay attention not only to cases the AI wants to progress, but also to cases it is inclined to reject. Human oversight is not just about stopping an AI from being too aggressive; it can also stop the system from being too conservative and discarding a legitimate argument.

One of the clearest escalation signals today is a lack of evidence. People may not upload the relevant documents, may have lost them over time, or may not realise which evidence is important to the claim. Where the matter is not sufficiently clear or complete, the next step can be human review rather than automatic progression. Lawyers still handle context and grey areas more consistently than current systems do.

**As AI systems take on more steps traditionally performed by lawyers, how do you think the boundary between software automation and regulated legal services will evolve?**

The boundary will move, but more slowly than many people in technology expect. High-stakes systems cannot rely on the promise that the next model will be better; reliability has to be demonstrated through authoritative sources, validation, controls, and accountable human review. Over time, I expect AI to become something professionals can rely on within clearly defined limits, but autonomy has to be earned through observed performance and real outcomes. The useful question is not ‘software or lawyer?’ but which activity is being performed, what evidence supports it, and who remains accountable.

**General-purpose AI models are becoming more capable very quickly. What creates a sustainable advantage for a vertical AI company like CaseCraft.AI when the underlying foundation models available to everyone continue to improve?**

Our advantage was never going to be owning a foundation model. Better general-purpose models are good news for us. The difficult part is everything around them: retrieval, the matter database, legal knowledge, workflow infrastructure, integrations, controls and the operational understanding of how a claim moves from beginning to end. That work does not disappear when a new model ships.

For the user, it should feel like one place where the case happens, while the orchestration stays underneath. The same infrastructure is now beginning to support both individual claimants and businesses using batch-claim of up to 150 claims with one click and case-management workflows. I think that orchestration and domain execution are the durable moat for vertical AI.

**Looking beyond small claims, what have you learned from CaseCraft.AI about the broader future of agentic AI? Which other high-stakes industries do you believe are especially well suited to systems that can manage complex workflows while keeping humans accountable for critical decisions?**

I am optimistic about agentic AI, but the difficult work sits around the model: redesigning processes, structuring information, defining what the system may do, and building validation and escalation. That is why regulated industries often move more slowly – the people who understand the workflow well enough to automate it are usually the busiest experts in the organisation.

The strongest opportunities are workflows with lots of repeatable information gathering and document processing, but a smaller number of exceptions that still require accountable judgement. For CaseCraft, Employment Law is the nearest expansion, with an MVP in active testing, and we are exploring Personal Injury with a specialist litigation firm. Beyond law, insurance, financial services and compliance have a similar shape. The systems that win will know not only how to automate the conversation, but exactly when the machine should stop and a human should take over.

*Thank you for the great interview, readers who wish to learn more should visit
[CaseCraft.AI](http://casecraft.ai)
.*