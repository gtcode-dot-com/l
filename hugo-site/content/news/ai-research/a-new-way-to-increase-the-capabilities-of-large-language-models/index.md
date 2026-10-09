---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-18T00:03:46.930166+00:00'
exported_at: '2025-12-18T00:03:49.571336+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/new-way-to-increase-large-language-model-capabilities-1217
structured_data:
  about: []
  author: ''
  description: MIT-IBM Watson AI Lab researchers developed an AI expressive architecture
    called PaTH Attention, increasing the capabilities of large language models that
    can perform better state tracking and sequential reasoning over long text.
  headline: A new way to increase the capabilities of large language models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/new-way-to-increase-large-language-model-capabilities-1217
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: A new way to increase the capabilities of large language models
updated_at: '2025-12-18T00:03:46.930166+00:00'
url_hash: 19f38dfeb9b1f04f734b0d91dc84af5d435e6935
---

Most languages use word position and sentence structure to extract meaning. For example, “The cat sat on the box,” is not the same as “The box was on the cat.” Over a long text, like a financial document or a novel, the syntax of these words likely evolves.

Similarly, a person might be tracking variables in a piece of code or following instructions that have conditional actions. These are examples of state changes and sequential reasoning that we expect state-of-the-art artificial intelligence systems to excel at; however, the existing, cutting-edge attention mechanism within transformers — the primarily architecture used in large language models (LLMs) for determining the importance of words — has theoretical and empirical limitations when it comes to such capabilities.

An attention mechanism allows an LLM to look back at earlier parts of a query or document and, based on its training, determine which details and words matter most; however, this mechanism alone does not understand word order. It “sees” all of the input words, a.k.a. tokens, at the same time and handles them in the order that they’re presented, so researchers have developed techniques to encode position information. This is key for domains that are highly structured, like language. But the predominant position-encoding method, called rotary position encoding (RoPE), only takes into account the relative distance between tokens in a sequence and is independent of the input data. This means that, for example, words that are four positions apart, like “cat” and “box” in the example above, will all receive the same fixed mathematical rotation specific to that relative distance.

Now research led by MIT and the MIT-IBM Watson AI Lab has produced an encoding technique known as “PaTH Attention” that makes positional information adaptive and context-aware rather than static, as with RoPE.

“Transformers enable accurate and scalable modeling of many domains, but they have these limitations vis-a-vis state tracking, a class of phenomena that is thought to underlie important capabilities that we want in our AI systems. So, the important question is: How can we maintain the scalability and efficiency of transformers, while enabling state tracking?” says the paper’s senior author Yoon Kim, an associate professor in the Department of Electrical Engineering and Computer Science (EECS), a member of the Computer Science and Artificial Intelligence Laboratory (CSAIL), and a researcher with the MIT-IBM Watson AI Lab.

A new paper on this work was presented earlier this month at the Conference on Neural Information Processing Systems (NeurIPS). Kim’s co-authors include lead author Songlin Yang, an EECS graduate student and former MIT-IBM Watson AI Lab Summer Program intern; Kaiyue Wen of Stanford University; Liliang Ren of Microsoft; and Yikang Shen, Shawn Tan, Mayank Mishra, and Rameswar Panda of IBM Research and the MIT-IBM Watson AI Lab.

**Path to understanding**

Instead of assigning every word a fixed rotation based on relative distance between tokens, as RoPE does, PaTH Attention is flexible, treating the in-between words as a path made up of small, data-dependent transformations. Each transformation, based on a mathematical operation called a Householder reflection, acts like a tiny mirror that adjusts depending on the content of each token it passes. Each step in a sequence can influence how the model interprets information later on. The cumulative effect lets the system model how the meaning changes along the path between words, not just how far apart they are. This approach allows transformers to keep track of how entities and relationships change over time, giving it a sense of “positional memory.” Think of this as walking a path while experiencing your environment and how it affects you. Further, the team also developed a hardware-efficient algorithm to more efficiently compute attention scores between every pair of tokens so that the cumulative mathematical transformation from PaTH Attention is compressed and broken down into smaller computations so that it’s compatible with fast processing on GPUs.

The MIT-IBM researchers then explored PaTH Attention’s performance on synthetic and real-world tasks, including reasoning, long-context benchmarks, and full LLM training to see whether it improved a model’s ability to track information over time. The team tested its ability to follow the most recent “write” command despite many distracting steps and multi-step recall tests, tasks that are difficult for standard positional encoding methods like RoPE. The researchers also trained mid-size LLMs and compared them against other methods. PaTH Attention improved perplexity and outcompeted other methods on reasoning benchmarks it wasn’t trained on. They also evaluated retrieval, reasoning, and stability with inputs of tens of thousands of tokens. PaTH Attention consistently proved capable of content-awareness.

“We found that both on diagnostic tasks that are designed to test the limitations of transformers and on real-world language modeling tasks, our new approach was able to outperform existing attention mechanisms, while maintaining their efficiency,” says Kim. Further, “I’d be excited to see whether these types of data-dependent position encodings, like PATH, improve the performance of transformers on structured domains like biology, in [analyzing] proteins or DNA.”

**Thinking bigger and more efficiently**

The researchers then investigated how the PaTH Attention mechanism would perform if it more similarly mimicked human cognition, where we ignore old or less-relevant information when making decisions. To do this, they combined PaTH Attention with another position encoding scheme known as the Forgetting Transformer (FoX), which allows models to selectively “forget.” The resulting PaTH-FoX system adds a way to down-weight information in a data-dependent way, achieving strong results across reasoning, long-context understanding, and language modeling benchmarks. In this way, PaTH Attention extends the expressive power of transformer architectures.

Kim says research like this is part of a broader effort to develop the “next big thing” in AI. He explains that a major driver of both the deep learning and generative AI revolutions has been the creation of “general-purpose building blocks that can be applied to wide domains,” such as “convolution layers, RNN [recurrent neural network] layers,” and, most recently, transformers. Looking ahead, Kim notes that considerations like accuracy, expressivity, flexibility, and hardware scalability have been and will be essential. As he puts it, “the core enterprise of modern architecture research is trying to come up with these new primitives that maintain or improve the expressivity, while also being scalable.”

This work was supported, in part, by the MIT-IBM Watson AI Lab and the AI2050 program at Schmidt Sciences.