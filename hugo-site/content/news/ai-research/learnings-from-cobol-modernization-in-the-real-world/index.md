---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T03:25:18.054336+00:00'
exported_at: '2026-03-03T03:25:19.368002+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/learnings-from-cobol-modernization-in-the-real-world
structured_data:
  about: []
  author: ''
  description: Delivering successful COBOL modernization requires a solution that
    can reverse engineer deterministically, produce validated and traceable specs,
    and help those specs flow into any AI-powered coding assistant for the forward
    engineering. A successful modernization requires both reverse engineering and
    forward engine...
  headline: Learnings from COBOL modernization in the real world
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/learnings-from-cobol-modernization-in-the-real-world
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Learnings from COBOL modernization in the real world
updated_at: '2026-03-03T03:25:18.054336+00:00'
url_hash: 3e65c2de92bb5ee154f471596f9c4b6be67046b7
---

There’s a lot of excitement right now about AI enabling mainframe application modernization. Boards are paying attention. CIOs are getting asked for a plan. AI is a genuine accelerator for COBOL modernization but to get results, AI needs additional context that source code alone can’t provide.Here’s what we’ve learned working with 400+ enterprise customers: mainframe modernization has two very different halves. The first half is reverse engineering, understanding what your existing systems actually do. The second half is forward engineering, building the new applications.

The first half is where mainframe projects live or die. However, coding assistants are genuinely good at only the second half. Give them a clear, validated spec and they’ll build modern applications fast.

We have learned that delivering successful COBOL modernization requires a solution that can reverse engineer deterministically, produce validated and traceable specs, and help those specs flow into any AI-powered coding assistant for the forward engineering. A successful modernization requires
*both*
reverse engineering and forward engineering.

## What a successful mainframe modernization requires

### Bounded, complete context

Mainframe applications are big. Really big. A single program can run tens of thousands of lines, pulling in shared data definitions from across the system, calling other programs, orchestrated through JCL that spans the entire landscape. Today, AI can only process a limited amount of code at a time. Feed it one program and it can’t see the copybooks, the called subroutines, the shared files, or the JCL that ties everything together. It will produce output that looks reasonable for the code it can see but miss dependencies it was never shown. In working with customers, we solve this by extracting all implicit dependencies deterministically first, then feeding AI bounded, complete units with everything it needs already resolved. That way AI focuses on what it’s great at (understanding business logic, generating specifications) instead of guessing at connections it can’t see.

### Platform-aware context

Here’s something that surprises people: the same COBOL source code behaves differently depending on the compiler and runtime. How numbers get rounded, how data sits in memory, how programs talk to middleware. These aren’t in the source code. They’re determined by the specific compiler and runtime environment the code was built for. Decades of hardware-software integration can’t be replicated by simply moving code. We found that AI does its best work when platform-specific behavior has already been resolved. Feed AI clean, platform-aware input, and it delivers. Feed it raw source code, and it’ll generate output that looks right but behaves differently than the original. In financial systems, a rounding difference isn’t a cosmetic issue. It’s a material error.

### A traceable foundation

If you’re in banking, insurance, or government, your regulators will ask one question: can you prove you didn’t miss anything? AI on its own isn’t enough to extract business logic and generate documentation that regulators will accept. Regulatory compliance requires every output to have a formal, auditable connection back to the original system. We learned early that traceability doesn’t come from AI reading source code. It comes from structuring the code into precise, bounded units so we know exactly what goes into the AI and can trace every output back to its source. For customers in regulated industries, this is often the difference between a project that moves forward and one that stalls.

### How we set AI up for success in AWS Transform

We built AWS Transform to modernize mainframe applications at scale. The idea is straightforward: give AI the right foundation, and customers get traceable, correct, and complete results they can take to production. AWS Transform starts by building a complete, deterministic model of the application. Specialized agents extract code structure, runtime behavior, and data relationships across the entire system — not one program at a time, but the whole landscape. This produces a dependency graph aligned with the actual compiler semantics, capturing cross-program dependencies, middleware interactions, and platform-specific behavior before AI gets involved. From there, large programs get decomposed into bounded, processable, units. Platform-specific behavior is resolved deterministically. The units are sized for AI to process effectively. Then AI extracts business logic in natural language, and every output gets validated against the deterministic evidence we’ve already extracted. Specs map back to the original code. When a regulator asks “did you miss anything?”, there’s a verifiable answer. What sets this apart is that AI never operates in the dark. Every unit it processes has known inputs and expected outputs, so we can validate what comes back. No other approach on the market closes that loop. What comes out is a set of validated, traceable technical specifications that plug into any modern development environment. The hard part of modernization is understanding what exists today. Once you’ve captured that in precise specs, AI-powered IDEs can build the new application with confidence.

### An end-to-end platform for enterprise transformation

Nobody modernizes one app. Our customers are staring at portfolios of hundreds or thousands of interconnected applications, and they need way more than analysis help. AWS Transform automates across the full lifecycle: analysis, test planning, refactoring, reimagination. The whole thing. And within that, different apps need different paths. Some get re-imagined from scratch. Some just need a clean, deterministic conversion to Java. Some need to get out of the data center first and modernize later. Some will remain on the mainframe. We learned the hard way that treating them all the same is how projects blow up. The portfolio decision (which app, which path, what order) matters as much as the tech. In our experience, this is the only way enterprise modernization actually finishes. One-size-fits-all approaches are why these projects fail. One more thing that gets overlooked constantly: test data. You can’t prove the modernized app works without real production data and real scenarios. We’ve watched teams get all the way through code conversion and then stall because nobody planned for data capture. So, we built test planning and on-prem data capture into the platform from day one. Not a cleanup exercise at the end. That’s what this actually looks like when it works. End-to-end automation, the right path for each app, validation baked in.

### How to get this right

The question isn’t “should we use AI for COBOL modernization?” Of course you should. The question is how you set AI up to deliver: traceability for regulators, platform-specific behavior handled correctly, consistency across your application portfolio, and the ability to scale to hundreds of interconnected programs. That’s what we figured out building AWS Transform. Deterministic analysis as the foundation. AI as the accelerator. An AWS service that covers the full range of modernization patterns.

And it’s working.

BMW Group reduced testing time by 75% and increased test coverage by 60%, significantly lowering risk while accelerating modernization timelines.

Fiserv completed a mainframe modernization project that would have taken 29+ months in just 17 months.

Itau cut mainframe application discovery time and testing time by more than 90%, enabling teams to modernize applications 75% faster than with previous manual efforts.

---

## About the authors

### Dr. Asa Kalavade

[Asa](author%20LinkedIn)
leads AWS Transform, helping customers migrate and modernize their infrastructure, applications, and code. Previously, she led the AWS go-to-market tools transformation, incorporating generative AI capabilities. She also managed hybrid storage and data transfer services. Before joining AWS in 2016, Asa founded two venture-backed startups and remains active in mentoring Boston startups. She holds a PhD in electrical engineering and computer science from UC Berkeley and more than 40 patents.