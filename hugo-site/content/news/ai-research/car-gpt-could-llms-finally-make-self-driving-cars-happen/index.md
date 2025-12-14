---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-14T12:03:32.963196+00:00'
exported_at: '2025-12-14T12:03:35.569373+00:00'
feed: https://thegradient.pub/rss/
language: en
source_url: https://thegradient.pub/car-gpt
structured_data:
  about: []
  author: ''
  description: 'Exploring the utility of large language models in autonomous driving:
    Can they be trusted for self-driving cars, and what are the key challenges?'
  headline: 'Car-GPT: Could LLMs finally make self-driving cars happen?'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thegradient.pub/car-gpt
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Car-GPT: Could LLMs finally make self-driving cars happen?'
updated_at: '2025-12-14T12:03:32.963196+00:00'
url_hash: 0754271707cf5836a2e0ce170c91b7f6cb388491
---

In 1928, London was in the middle of a terrible health crisis, devastated by bacterial diseases like pneumonia, tuberculosis, and meningitis. Confined in sterile laboratories, scientists and doctors were stuck in a relentless cycle of trial and error, using traditional medical approaches to solve complex problems.

This is when, in September 1928, an accidental event changed the course of the world.
A Scottish doctor named Alexander Fleming forgot to close a petri dish (the transparent circular box you used in science class), which got contaminated by mold. This is when Fleming noticed something peculiar: all bacteria close to the moisture were dead, while the others survived.

"What was that moisture made of?" wondered M. Flemming.
This was when he discovered that Penicillin, the main component of the mold, was a powerful bacterial killer. This led to the groundbreaking discovery of penicillin, leading to the antibiotics we use today. In a world where doctors were relying on existing well-studied approaches, Penicillin was the unexpected answer.

**Self-driving cars may be following a similar event.**
Back in the 2010s, most of them were built using what we call a « modular » approach. The software « autonomous » part is split into several modules, such as Perception (the task of seeing the world), or Localization (the task of accurately localize yourself in the world), or Planning (the task of creating a trajectory for the car to follow, and implementing the « brain » of the car). Finally, all these go to the last module: Control, that generates commands such as « steer 20° right », etc… So this was the well-known approach.

But a decade later, companies started to take another discipline very seriously:
**End-To-End learning**
. The core idea is to replace every module with a single neural network predicting steering and acceleration, but as you can imagine, this introduces a black box problem.

![](https://lh7-us.googleusercontent.com/EpMJPDK-TBu9ZhN25UrxVbAk-9rJjEvtitzjvPpzjhTBPdkk-judKQtfWQNf7vtNrG1sfsvkUhpbtMGplWN5bbnx5ULbfNj6vpRf8RVlt5eDn8MN99FObGbPsmokdNlCGZ1NWq-uw32QVitv4NZC3zI)


The 4 Pillars of Self-Driving Cars are Perception, Localization, Planning, and Control. Could a Large Language Model replicate them? (
[source](https://www.thinkautonomous.ai/blog/autonomous-vehicle-architecture/)
)

These approaches are known, but don’t solve the self-driving problem yet. So, we could be wondering:
**"What if LLMs (Large Language Models), currently revolutionizing the world, were the unexpected answer to autonomous driving?"**

This is what we're going to see in this article, beginning with a simple explanation of what LLMs are and then diving into how they could benefit autonomous driving.

## **Preamble: LLMs-what?**

Before you read this article, you must know something: I'm not an LLM pro, at all. This means, I know too well the struggle to learn it. I understand what it's like to google "learn LLM"; then see 3 sponsored posts asking you to download e-books (in which nothing concrete appears)... then see 20 ultimate roadmaps and GitHub repos, where step 1/54 is to view a 2-hour long video (and no one knows what step 54 is because it's so looooooooong).

So, instead of putting you through this pain myself, let's just break down what LLMs are in 3 key ideas:

1. Tokenization
2. Transformers
3. Processing Language

### **Tokenization**

In ChatGPT, you input a piece of text, and it returns text, right? Well, what's actually happening is that your text is first converted into tokens.

![](https://lh7-us.googleusercontent.com/_rT6_ShRUbi-bZpaKL7JF-BhE_rfDg_V8De5nYj0O5tGgAtLTyYhnGleIy7nBJ3vyrUsfge6cdReCctzsfCyW_XP6WUm21pU350RpOoxWzb2SYRvMcKMIZAOE6wdFou7t_ERJ2_Jht6uUhfg_sBgcbI)


Example of tokenization of a sentence, each word becomes a "token"

But what's a token? You might ask. Well, a token can correspond to a word, a character, or anything we want. Think about it -- if you are to send a sentence to a neural network, you didn't plan on sending actual words, did you?

The input of a neural network is always a number, so you need to convert your text into numbers; this is tokenization.

![](https://lh7-us.googleusercontent.com/pZ3qf5HQNrqXqb5bbGkLgWQPvu04-2b_ejpv4m3i5C9VfcPg3yZm7cmaD6lq4xgrA4DhUBJpCa-HB4i7iAPo8-Hyrde9sLiBYBiY2d7c9O17ePJtCqAb15dvcDEGxofEwneP6Nx2_oSiT26m4cLvcMc)


What tokenization actually is: A conversion from words to numbers

Depending on the model (ChatGPT, LLAMA, etc...), a token can mean different things: a word, a subword, or even a character. We could take the English vocabulary and define these as words or take parts of words (subwords) and handle even more complex inputs. For example, the word « a » could be token 1, and the word « abracadabra » would be token 121.

### **Transformers**

Now that we understand how to convert a sentence into a series of numbers, we can send that series into our neural network! At a high level, we have the following structure:

![](https://lh7-us.googleusercontent.com/J1CkM3ItKevopmi-0gbSHWJnMStL4dZWksllG15OlaDI4PFgk-FtFeQ7O0CnP1dKx9ZHV7PUAlmBK9lFwJQrHnJj1JAXAMHdbZH13hd07dYL55ZCsxQChf06dYj_JoXEvNeAqdfmj2IcdwD8sP5OZtI)


A Transformer is an Encoder-Decoder Architecture that takes a sequence of tokens as input and outputs a another series of tokens

If you start looking around, you will see that some models are based on an encoder-decoder architecture, some others are purely encoder-based, and others, like GPT, are purely decoder-based.

Whatever the case, they all share the core Transformer blocks: multi-head attention, layer normalization, addition and concatenation, blocks, cross-attention, etc...

**This is just a series of attention blocks getting you to the output**
. So how does this word prediction work?

### **The output/ Next-Word Prediction**

The Encoder learns features and understands context... But what does the decoder do? In the case of object detection, the decoder is predicting bounding boxes. In the case of segmentation, the decoder is predicting segmentation masks. What about here?

In our case, the decoder is trying to generate a series of words; we call this task "next-word prediction".

Of course, it does it similarly by predicting numbers or tokens. This characterizes our full model as shown below,

![](https://lh7-us.googleusercontent.com/YS9WFjjuYTq7QkzPnx4xgTQnU0Pmr22i4fEzXXWuBf6wD--eYL8FvdoEpkqlCMKraBaSDuo7j0sWR7ltUaWI31_Bvq9PtJoPpoWRFQnjKOth1P7mnxfzmGT8ppUslOPMhbOzJY49F4IHBMZfyzax18E)


I would say the loss function for this particular output produces a near-0 value.

Now, there are many "concepts" that you should learn on top of this intro: everything Transformer and Attention related, but also few-shot learning, pretraining, finetuning, and more...

Ok... but what does it have to do with self-driving cars? I think it's time to move to stage 2.

## **Chat-GPT for Self-Driving Cars**

The thing is, you've already been through the tough part. The rest simply is: "How do I adapt this to autonomous driving?". Think about it; we have a few modifications to make:

* **Our input now becomes either images, sensor data**
  (LiDAR point clouds, RADAR point clouds, etc...), or even algorithm data (lane lines, objects, etc...). All of it is "tokenizable", as Vision Transformers or Video Vision Transformers do.
* **Our Transformer model pretty much remains the same**
  since it only operates on tokens and is independent of the kind of input.
* **The output is based on the set of tasks we want to do.**
  It could be explaining what's happening in the image or could  also be a direct driving task like switching lanes.

So, let's begin with the end:

### **What self-driving car tasks could LLM solve?**

There are many tasks involved in autonomous driving, but not all of them are GPT-isable. The most active research areas in 2023 have been:

* **Perception**
  : Based on an input image, describe the environment, number of objects, etc...
* **Planning**
  : Based on an image, or a bird-eye view, or the output of perception, describe what we should do (keep driving, yield, etc...)
* **Generation**
  : Generate training data, alternate scenarios, and more... using "diffusion"
* **Question & Answers**
  : Create a chat interface and ask the LLM to answer questions based on the scenario.

### **LLMs in Perception**

In Perception, the input is a series of images, and the output is usually a set of objects, lanes, etc... In the case of LLMs, we have 3 core tasks:
**Detection**
,
**Prediction**
, and
**Tracking**
. An example with Chat-GPT, when you send it an image and ask to describe what's going on is shown below:

![](https://lh7-us.googleusercontent.com/unUisu66NolUzzipNfKObr8kE6n8PRcTMy86cYYIG1aIPLkYKZd34zmzGrkM4yS6lKNoXpvORHwnfORfOsy8aRNUx9AwEDN_qQN4tiuutBRh8l3h_vVpfVzOJ7UdQ-CuWKI5EJsze9le6qRA7VQ1QoY)


A GPT-4 Vision model can return the objects in the image, just like object detectors do (
[source](https://arxiv.org/pdf/2311.05332.pdf)
)

Other models such as
[HiLM-D](https://arxiv.org/pdf/2309.05186v1.pdf)
and
[MTD-GPT](https://arxiv.org/pdf/2312.00812.pdf)
can also do this, some work also for videos. Models like
[PromptTrack](https://arxiv.org/pdf/2309.04379.pdf)
, also have the ability to assign unique IDs (this car in front of me is ID #3), similar to a 4D Perception model.

![](https://lh7-us.googleusercontent.com/WcjhR7diFbZrVeKdiVyQbC_HtYJVGUQsOBka0zikaD2JZpfmNxcyEJlpzxZfvobWrMu6srxUEGPcxpdVSywVKW-0gIuOISCqLCVfjaA6Q7KaNb1etKfNybXkya4yFyx7AY0Y2_ZZw_cY_gWSccO0B2Q)


PromptTrack combines the DETR object detector with Large Language Models

In this model, multi-view images are sent to an Encoder-Decoder network that is trained to predict annotations of objects such as bounding boxes, and attention maps). These maps are then combined with a prompt like 'find the vehicles that are turning right'.The next block then finds the 3D Bounding Box localization and assigns IDs using a bipartite graph matching algorithm like the
[Hungarian Algorithm](https://www.thinkautonomous.ai/blog/hungarian-algorithm)
.

This is cool, but this isn't the "best" application of LLMs so far:

### **LLMs in Decision Making, Navigation, and Planning**

If Chat-GPT can find objects in an image, it should be able to tell you what to do with these objects, shouldn't it? Well, this is the task of Planning i.e. defining a path from A to B, based on the current perception. While there are numerous models developed for this task, the one that stood out to me was
[Talk2BEV](https://arxiv.org/pdf/2310.02251.pdf)
:

![](https://lh7-us.googleusercontent.com/N3ZvMnLMjQ6jwL4FNvvTyM4U6KFrri0jV-0yOYVH9lAAtRH7MD8aMX_LHhjeBFKxGwTdrATJoNUQe-sUqEB3utLnpreCT4e4TIO3qX3LTrzBKwZ7kPAfzxAu6osJ35tYpapCiTTWDtx0tUOHXcNqu04)


Talk2BEV takes perception one step further and also tells you what to do

The main difference between models for planning and Perception-only models is that here, we're going to train the model on human behavior to suggest ideal driving decisions. We're also going to change the input from multi-view to
[Bird Eye View](https://courses.thinkautonomous.ai/bird-eye-view)
since it is much easier to understand.

This model works both with LLaVA and ChatGPT4, and here is a demo of the architecture:

![](https://lh7-us.googleusercontent.com/-bl_IDT2SqF75q3d20EORJcH22oXWMjFmkLFn0ZKbVV5oshlr5BkZEnscfUSg_-pkzMDJ3Jo38mdu6whUmIDWq7pXfxXxdwgc3Kj-WUwv5LNWUHIvH3r6mfpKP9s5PD7NoA7e0R3pBoic6ijwfD57aU)


Talk2BEV (
[source](https://github.com/llmbev/talk2bev)
)

As you can see, this isn't purely "prompt" based, because the core object detection model stays Bird Eye View Perception, but the LLM is used to "enhance" that output by suggesting to crop some regions, look at specific places, and predict a path. We're talking about "language enhanced BEV Maps".

Other models like
[DriveGPT](https://arxiv.org/pdf/2310.01415.pdf)
are trained to send the output of Perception to Chat-GPT and finetune it to output the driving trajectory directly.

![](https://lh7-us.googleusercontent.com/QbuhKKLWr0jA1DWdSWBIk6UtHnecHTITRBPidM1fjYn9VSC-56VcaxStqJbn5iTLslLN6ppQgnmfKZO-43TNCZADfuwdV-RChnMrzryLIKx7UvtySKEs0unIEum4c2ous07M3-WlUoTVeGT1s0nPz0U)


The DriveGPT model is pure madness... when trained correctly! (modified from
[source](https://arxiv.org/pdf/2310.01415.pdf)
)

I could go on and on, but I think you get the point. If we summarize, I would say that:

* Inputs are either tokenized images or outputs of Perception algorithm (BEV maps, ...)
* We fuse existing models (BEV Perception, Bipartite Matching, ...) with language prompts (find the moving cars)
* Changing the task is mainly about changing the data, loss function, and careful finetuning.

The Q&A applications are very similar, so let's see the last application of LLMs:

### **LLMs for Image Generation**

Ever tried Midjourney and DALL-E? Isn’t it super cool? Yes, and there is MUCH COOLER than this when it comes to autonomous driving. In fact, have you heard of Wayve's GAIA-1 model? The model takes text and images as input and directly produces videos, like this:

![](https://lh7-us.googleusercontent.com/R9xqQVFRcUlZrjXqqeY6qon7hxAezFKY3mI_ZdPh2R0eJGPQb2CjV0TFxjwblDEWxJz7va0N6KerXMRO_ltSFJkxiQRxmW7I_I_b13bD-PidrUD8sQ0REInSAUJuKGqazFFDCpwOQAVun5LREW41Q_w)


These videos are generated by Wayve's GAIA-1 model

The architecture takes images, actions, and text prompts as input, and then uses a World Model (an understanding of the world and its interactions) to produce a video.

![](https://lh7-us.googleusercontent.com/ougFIHYengzs40lyruVerlDFFa18VXH0K093yjHA93q8nTjTmLQAdfKCPl7sBAbZfpoxqY3tDdzufOqJoxmLUdL6W862_aPebPxABsPwjyaFZGWOCP2VTpaqcob0gkSJDRv9IqSm7-aHoXtG-FXWJBo)


Architecture of GAIA-1 (
[source](https://wayve.ai/thinking/scaling-gaia-1/)
)

You can find more examples on Wayve's YouTube channel and
[this dedicated post](https://wayve.ai/thinking/scaling-gaia-1/)
.

Similarly, you can see
[MagicDrive](https://github.com/cure-lab/MagicDrive)
, which takes the output of Perception as input and uses that to generate scenes:

![](https://lh7-us.googleusercontent.com/vVKUXuJno-UQWj2ZTWEA1JBMzZ6xnajJOrzMPtMW4qFjhvKqT7F2XiOoe9M1PCtM44S4CfrXqTVyVfKOisaB3iy-wa5vuCS7SFYaQdv6dzNfbzVcG2XXQzAAUqZXUeGxALkJ9fHuE8XFA4KvkKmZLN4)


(
[source](https://github.com/cure-lab/MagicDrive)
)

Other models, like
[Driving Into the Future](https://arxiv.org/pdf/2311.17918.pdf)
and
[Driving Diffusion](https://drivingdiffusion.github.io/)
can directly generate future scenarios based on the current ones. You get the point; we can generate scenes in an infinite way, get more data for our models, and have this endless positive loop.

We've just seen 3 prominent families of LLM usage in self-driving cars: Perception, Planning, and Generation. The real question is...

## **Could we trust LLMs in self-driving cars?**

**And by this, I mean... What if your model has hallucinations?**
What if its replies are completely absurd, like ChatGPT sometimes does? I remember, back in my first days in autonomous driving, big groups were already skeptical about Deep Learning, because it wasn't "deterministic" (as they call it).

We don't like Black Boxes, which is one of the main reasons End-To-End will struggle to get adopted. Is ChatGPT any better? I don't think so, and I would even say it's worse in many ways. However, LLMs are becoming more and more transparent, and the black box problem could eventually be solved.

To answer the question "Can we trust them?"... it's very early in the research, and I'm not sure someone has really used them "online" — meaning « live », in a car, on the streets, rather than in a headquarter just for training or image generation purpose.  I would definitely picture a Grok model on a Tesla someday just for Q&A purposes. So for now, I will give you my coward and safe answer...

**It's too early to tell!**

Because it really is. The first wave of papers mentioning LLMs in Self-Driving Cars is from mid-2023, so let's give it some time. In the meantime, you could start with
[this survey](https://arxiv.org/pdf/2311.01043.pdf)
that shows all the evolutions to date.

Alright, time for the best part of the article...

## **The LLMs 4 AD Summary**

* **A Large Language Model (LLM) works in 3 key steps: inputs, transformer, output.**
  The input is a set of tokenized words, the transformer is a classical transformer, and the output task is "next word prediction".
* **In a self-driving car, there are 3 key tasks we can solve with LLMs:**
  **Perception**
  (detection, tracking, prediction),
  **Planning**
  (decision making, trajectory generation), and
  **Generation**
  (scene, videos, training data, ...).
* **In Perception, the main goal is to describe the scene we're looking at.**
  The input is a set of raw multi-view images, and the Transformer aims to predict 3D bounding boxes. LLMs can also be used to ask for a specific query ("where are the taxis?").
* **In Planning, the main goal is to generate a trajectory for the car to take**
  . The input is a set of objects (output of Perception, BEV Maps, ...), and the Transformer uses LLMs to understand context and reason about what to do.
* **In Generation, the main goal is to generate a video that corresponds to the prompt used**
  . Models like GAIA-1 have a chat interface, and take as input videos to generate either alternate scenes (rainy, ...), or future scenes.
* **For now, it's very early to tell whether this can be used in the long run**
  , but research there is some of the most active in the self-driving car space. It all comes back to the question: "Can we really trust LLMs in general?"

## **Next Steps**

If you want to get started on LLMs for self-driving cars, there are several things you can do:

* **⚠️ Before this, the most important**
  : If you want to keep learning about self-driving cars. I'm talking about self-driving car every day through my private emails. I'm sending many tips and direct content.
  [You should join here](https://www.thinkautonomous.ai/private-emails/)
  .
* **✅ To begin, build an understanding of LLMs for self-driving cars**
  . This is partly done, you can continue to explore the resources I provided in the article.
* **➡️ Second, build skills related to Auto-Encoders and Transformer Networks**
  .
  [My image segmentation series](https://courses.thinkautonomous.ai/image-segmentation)
  is perfect for this, and will help you understand Transformer Networks with no NLP example, which means it's for Computer Vision Engineer's brains.
* **️ ➡️ Then, understand how Bird Eye View Networks works.**
  It might not be mentioned in general LLM courses, but in self-driving cars, Bird Eye View is the central format where we can fuse all the data (LiDARs, cameras, multi-views, ...), build maps, and directly create paths to drive. You can do so in my
  [Bird Eye View course](https://courses.thinkautonomous.ai/bird-eye-view)
  (if closed,
  [join my email list](https://www.thinkautonomous.ai/private-emails/)
  to be notified).
* **Finally, practice training, finetuning, and running LLMs in self-driving car scenarios**
  . Run repos like Talk2BEV and the others I mentioned in the article. Most of them are open source, but the data can be hard to find. This is noted last, but there isn't really an order in all of this.

---

## **Author Bio**

Jérémy Cohen is a self-driving car engineer and founder of
[Think Autonomous](https://www.thinkautonomous.ai/)
, a platform to help engineers learn about cutting-edge technologies such as self-driving cars and advanced Computer Vision. In 2022, Think Autonomous won the price for Top Global Business of the Year in the Educational Technology Category​ and Jeremy Cohen was named 2023 40 Under 40 Innovators in Analytics Insight magazine, the largest printed magazine on Artificial Intelligence.
*You can join 10,000 engineers reading his private daily emails on self-driving cars*
[*here*](https://www.thinkautonomous.ai/private-emails)
*.*

## Citation

For attribution in academic contexts or books, please cite this work as

```
Jérémy Cohen, "Car-GPT: Could LLMs finally make self-driving cars happen?", The Gradient, 2024.
```

BibTeX citation:

```
@article{cohen2024cargpt,
    author = {Jérémy Cohen},
    title = {Car-GPT: Could LLMs finally make self-driving cars happen?},
    journal = {The Gradient},
    year = {2024},
    howpublished = {\url{https://thegradient.pub/car-gpt},
}
```