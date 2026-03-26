---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-26T22:51:53.409860+00:00'
exported_at: '2026-03-26T22:51:56.063977+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/podcast/will-machines-ever-be-intelligent
structured_data:
  about: []
  author: ''
  description: In Episode 1 of “The Shape of Things to Come,” technologists Subutai
    Ahmad & Nicolò Fusi join Microsoft’s Doug Burger to compare how large language
    models work with how the human brain learns & what it means for AI’s future.
  headline: Will machines ever be intelligent?
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/podcast/will-machines-ever-be-intelligent
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Will machines ever be intelligent?
updated_at: '2026-03-26T22:51:53.409860+00:00'
url_hash: 75f244ad5edb24a42a2d34b221d6a693203c063c
---

[MUSIC FADES]

I’d like to ask each of my guests to introduce themselves. Tell me a little bit about your background and what you’re currently working on—to the extent you can talk about it—in AI. So, Nicolò, would you please start?

**NICOLÒ FUSI:**
Yeah, thank you, Doug, for having us and having me here. It’s so much fun. So I’m Nicolò Fusi. I’m a researcher at MSR [Microsoft Research]. So Doug is my boss, so I will be very, very, very good to Doug in this podcast.

No, but jokes aside, my own background is in Bayesian nonparametric. That’s what I started studying. So Gaussian processes and things like that. And then equally, I would say, in computational biology, because I found it, like, one of the most interesting use cases for AI techniques. And that, kind of, has been true throughout my career. And pretty much like everybody else, eventually, I moved away from the kernel methods and the Bayesian nonparametrics and I started working more on language models, transformer models, with a particular eye towards information theory and the connection between information theory and generative modeling. And that’s, kind of, one of the main things I do today other than, kind of, managing the research of people who do much more interesting work than I do. [LAUGHS]

**BURGER:**
I have to interject there, Nicolò, because you dragged a piece of bait across my path.

**FUSI:**
I figured.

**BURGER:**
You know, at Microsoft Research, I have a management rule that I can’t tell anyone what to do because we hire some of the best people in the world. You have to trust them. And everyone is always completely free to call BS on me. And so Nicolò was joking there; [LAUGHTER] he does not have to toe the party line. In fact, I encourage him not to. So, so …

**FUSI:**
I just have to be well-behaved. That’s the only thing I will say. [LAUGHS]

**BURGER:**
Yeah. Thank you, thank you for baiting me. [LAUGHS] Because he knew exactly what he was doing. And I love him for it.

Subutai, can you tell us a little bit about yourself?

**SUBUTAI AHMAD:**
Sure. Thank you so much, Doug, for having me. I’m really looking forward to the conversation between us all.

So I see myself fundamentally as a computer scientist. You know, I’ve been studying computer science for longer than I care to admit. But something changed for me during my undergrad years. I decided to minor in cognitive psychology, and I started to get really interested in how the brain works.

And to me, understanding intelligence and implementing intelligence was the hardest problem a computer scientists could ever solve. So I got very, very interested in that. You know, I couldn’t see how to really commercialize that. I was very interested in making products and stuff. So I stopped, you know, working on that for a while. I did a number of startups doing computer vision, you know, video processing, a lot of that stuff.

And then when Jeff Hawkins started Numenta back in 2005 with the idea of really deeply understanding how the brain works and figuring out how to apply that to AI, for me, it was like all my worlds coming together. This, like, this is what I had to do. None of us thought [LAUGHS] it would take as long as it did. We spent the last couple of decades really deeply trying to understand neuroscience from a computer scientist—from a programmer’s—standpoint, the underlying algorithms. And that’s really what I’m passionate about, just trying to translate what we understand about the neuroscience to today’s AI.

And in terms of what we’re working on today, it’s, you know, the human—maybe we’ll get into some of this—the brain is super efficient in how it works—power efficient, energy efficient—and we’re trying to embody those ideas and trying to make AI a lot more efficient than it is today.

**BURGER:**
Great. I think we’ll get into efficiency a little bit later in the podcast because that’s a subject that’s near and dear to my heart, you know, being a computer architect originally by training.

I want to go back to, you know, one of the reasons I got involved with Numenta is, you know, Subutai and I have been exchanging emails, like, discussing collaborations, you know, visiting each other through the years, and the thing that really stuck with me was when I read one of the
[earlier books from Jeff
*On Intelligence*

(opens in new tab)](https://us.macmillan.com/books/9780805078534/onintelligence/)
. And there was an example in the book that talked about how, you know, the human brain learns continuously. I think biological organisms in general learn continuously.

And the anecdote that I remember was this anecdote if you’re walking down your basement steps, you know, you’re walking down the stairs to your basement and there’s one step that’s always been a few inches off and you decide to fix it, and so you raise it so it’s even with the others, and then the next time you go down the stairs, you don’t remember and you’re wildly off and, you know, you hit that step, you hit it earlier or later than you anticipated, you go out of balance. You’re flailing around. You know, you get all this adrenaline. You think you’re going to pitch headfirst down the stairs. Hopefully you don’t. And then the second time you do it, you’re a little off balance, but it’s not crazy. And the third time you maybe notice a little bit, and the fourth time, it’s, like, it’s your basement stairs.

And so somewhere between that first time down and the third and fourth times down, there are molecular changes in your brain that have learned the new timing of your basement steps. And I remember just that example vividly from the book. And that got me thinking, wow, this is
*so*
different from the way our digital AI works. I’ll turn it over to you to comment for that and then I think we’ll go into the digital.

**AHMAD:**
Yeah, no, that’s a great example. I think it’s remarkable how our brain is constantly modeling our entire world at such a granular level, and we’re not even aware of it perceptually. Like, you know, that example of the steps is probably not … you wouldn’t consciously be aware of it, yet if something is different about anything in your world that you’re very familiar with, you’ll instantly notice it. And then you’ll, you know, you’ll update your world model, you’ll adjust, and you’ll continue on. It’s really remarkable how the brain’s able to do that so seamlessly.

**BURGER:**
And a lot of that is based on neurotransmitters, right? Because there’s just a … you know, when you have that physical reaction to “I’m about to pitch down the stairs,” you get a flood of transmitters that actually changes the way your brain’s learning or at least the rate.

**AHMAD:**
Yeah, there’s a flood of neurotransmitters and neuromodulators, as well, that invoke change, sometimes very rapidly. Another example, you know, if you touch a hot stove—that’s the canonical example—you will learn that very, very quickly. So there’s a lot of chemical changes that happen. But it’s also really interesting that we can update things and update our world knowledge without impacting everything else that we know. This is something that’s very, very different, again, from today’s AI models. We’re able to make these changes in a very contextual and very, sort of, fine-grained way.

**BURGER:**
So, Nicolò, I want to go and talk a little bit now to transformers. So I think, you know, you and I and Subutai were all working in the AI field, you know, many years before 2017, when the transformer hit. You know, I was building, you know, with my team hardware to accelerate RNNs [recurrent neural networks], LSTMs [long short-term memory], you know, which had this awful loop-carried dependence, you know, the bottlenecked computation, and then the transformer was just much more parallelizable.

So what do you think’s really going on in these things? And maybe we could start—I know you and I have talked a lot about this—maybe just start with the major blocks. You know, you’ve got the attention layer. You’ve got the feedforward layer. You’ve got, you know, the encoder stack and the decoder stack and the latent space in between. Can you just, kind of, walk us through those pieces at a high level and tell us what you think is going on?

**FUSI:**
Yeah.
Yeah, I mean, I have a very opinionated view of why transformers are so great.

**BURGER:**
That’s why you’re here. [LAUGHS]

**FUSI:**
Maybe, like, yeah, maybe I’ll inject it. I don’t know. I don’t think it’s a super novel creative opinion, but it is an opinion. So I guess the two principal … the two main components you already described: the, you know, the transformer [read: attention] layers and the feedforward layers. One way to think about them is, how does information in your context relate to each other and what is every token referring to, for instance, in the case of transformers in language models?

So by context, we mean, like, the information you feed through the model, that the model keeps continuously generating and appending to.

**BURGER:**
So like your chat history.

**FUSI:**
Your prompt. Your what? Your chat history or your particular prompt in a chat session.

**BURGER:**
OK.

**FUSI:**
That prompt, which is a sequence of words, gets discretized in a series of tokens. Tokens can be individual words, can be multiple words, kind of, connected together. The way we go from words to tokens typically is through an algorithm that tries to basically collapse as much as possible. Multiple words, like “the dog,” may be just one token as a first, kind of, level of compression to feed into the model. So it just tries to bring things together as efficiently as possible.

Then there is, you know, within these models, there is a transformer layer. This transformer layer or this attention layer, sorry, tries to basically figure out what the “the” refers to—the term “
*the*
” in “the dog,” or “the dog
*jumps*
on the table,” “jumps” refers to the dog. So there is this kind of, like, mapping that happens.

And then there is, like, feedforward layers, which in modern large language models, they store a lot of information. Like, that’s kind of, like, where the knowledge typically kind of sits in, the things that the model just
*knows*
. You know, that, I don’t know, if you slam your arm against [the] cup of water on your table, that cup of water falls off the table. That’s something that the model, kind of, has baked in through reading a lot about cups falling off of tables when they’re hit.

So that’s, kind of, those are, for me, the two fundamental components, and the reason why I have an opinionated view is that, you know, honestly, I do believe that RNNs and, you know, even state-space—
*modern*
incarnations of state-space models—are good enough to learn over these, you know, language data or whatever or vision data or audio data.

The good thing about transformers is that they do two things very well. One is they get out of the way. They don’t have this notion of “everything has to be encoded through a state” like recurrent networks. And two, they do that very computationally efficiently as you were saying. There isn’t a computational bottleneck. And so they created this nice overhang where they happen to be the right architecture at the right time to unlock enough flow of information through the model …

**BURGER:**
Yeah.

**FUSI:**
… that we could get through these amazing things.

**BURGER:**
Let me press you on one thing. Like, you know, in the attention blocks, you can figure out which words or which tokens relate to which tokens. So I put in the prompt and it’s finding all the relations and then feeding those relations up to, you know, the feedforward layer—well, the feedforward unit within a layer. And you said that knowledge is encoded there, but then what does it really mean for those maps to then access knowledge, but then you project it back into, you know, the output and then feed it up to the attention block in the next layer?

**FUSI:**
Again, yeah.

**BURGER:**
So it seems kind of weird that I’d be, like, accessing knowledge and then taking that knowledge, merging it, and going back to another attention map.

**FUSI:**
Well, you can see it as a mixing operation that happens in the feedforward part of the layer. You know, like, you’re attending, then you’re mixing, and, kind of, like, reprojecting to some space with higher-information content or, like, a different level of information extraction. And then you’re putting it back into, “OK, so let me do another round of processing” and, kind of, attending and then a mix again. And then I do it again and then I do it again.

So I think that the information that is present in the prompt and in the, you know, that has been baked into the weights gather further and further refined. Whether that refinement is extraction of structure or aggregation into higher-level concepts, I’m not sure. I think it’s just structure gets extracted and things that are irrelevant get kind of pushed away. But that doesn’t necessarily mean that it gets aggregated through the architecture.

**BURGER:**
So now I’m going to try to, like, restate what I think I hear you saying. So, you know, we’re adding information and we’re kind of adding information at a higher level but not necessarily throwing away the low-level information, at least that’s not relevant, right?

**FUSI:**
Yeah.

**BURGER:**
Because, you know, if the higher-level stuff depends on the low-level stuff, I have to have that first. And so then you get to the top of the encoder block and you’re in the latent space with all of that information kind of maximized. Is that a way to think about it? And if you agree, can you talk about what the encoder block really is and what the latent space is?

**FUSI:**
I tend to agree, yes. I mean, there is … you’re describing … I think you’re describing what I think is happening, which is there is given the context in your prompt and given the task that the model perceives or, like, figures out that you’re doing, it has to highlight and pull out the relevant information. And it does that not by summarizing layer by layer, but it does it by, you know, increasing the prominence of that information and suppressing other things. So I think that’s ultimately what happens up to the point where you reach this beautiful point in concept space, which identifies both your intent and the things in the prompt and in the knowledge of the model that are necessary to solve it.

**BURGER:**
And so one last question, and then I want to go to Subutai for a second.

So now when we go through the decoder stack, are we just going the other way and stripping out the high-level concepts early and then getting down to the granular tokens? Or, you know … because you go up through the encoder stack, those attention blocks and feedforward layers, to get to that magical latent space. And now we’re going to go the other direction. How do you think about that other direction through the decoder stack, which is the same primitives as the encoder stack?

**FUSI:**
Same primitives. You can think of it as kind of the reverse operation. Like you, you never lost information throughout. You just kind of suppress or privileged different kinds of information. And now you’re basically just projecting it back out to a space that is, you know, intelligible. And it’s, kind of, where the model gets it’s … I hesitate to use the term
*reward*
because it has a particular implication, but that’s, kind of, where the loss gets computed and then gets pushed back through the model.

**BURGER:**
Right, as you’re trying to evolve and train
*all*
those parameters—the relationship between words, the information in the feedforward layers, the design of that latent space, and the extraction of the knowledge from it.

**FUSI:**
That’s right. And so in encoder-decoder model, you push through the whole thing, you decode back to a particular token, which for people who don’t know, it’s, like, literally a number out of a vocabulary, like word No. 487. And if it was word No. 1,500, you get, you know, like, …

**BURGER:**
Something else.

**FUSI:**
… a bad reward. Yeah. Yeah. And then … and if you got it right, you get a positive signal that then just flows back through the model.

**BURGER:**
I’d like to go over to Subutai now. So after hearing this, you’ve studied, you know, neuroscience and the neocortex and cortical columns and all of this for a long time, and you and I have had lots of debates. Is the human brain doing something different than that? You know, are we just building latent spaces, then extracting? The architecture is very different, but what’s going on under the hood?

**AHMAD:**
Yeah, the architecture is very different. You know, as Nicolò
was describing what happens throughout a transformer stack, I was trying to relay and relate, you know, what we know in the brain, as well.

In a typical, you know, transformer model, there is, at the end of the day, there is a single latent space from which the next token is output. That does not happen in the brain. There are thousands and thousands of latent spaces that are, sort of, collaborating together, if you will.

You know, a lot of what we publish is under the moniker the Thousand Brains Theory of Intelligence. And Jeff
[has published a book a few years ago on that
(opens in new tab)](https://www.numenta.com/resources/books/a-thousand-brains-by-jeff-hawkins/)
. And that, kind of, dates back to
[discoveries in neuroscience from the ’60s and ’70s by the neuroscientist Vernon Mountcastle
(opens in new tab)](https://scispace.com/pdf/the-columnar-organization-of-the-neocortex-fyv7837bo3.pdf)
, who was a professor at Johns Hopkins.

**BURGER:**
Yup.

**AHMAD:**
And what he discovered … he made this remarkable discovery that, you know, our neocortex, which is the biggest part of our brain—that’s where all intelligent function happens—is actually
[composed of roughly 100,000 what he called cortical columns
(opens in new tab)](https://www.hachettebookgroup.com/titles/jeff-hawkins/a-thousand-brains/9781541675797/?lens=basic-books)
.

**BURGER:**
Right.

**AHMAD:**
And each cortical column is maybe 50,000 neurons. And there’s a very complex microcircuit and microarchitecture between the neurons in a cortical column.

But then there’s 100,000 of them, and every part of your brain—whether it’s doing visual processing, auditory processing, language, thought, motor actions—they’re all composed of this, essentially, this same microarchitecture. And this was a remarkable discovery. It says that there’s a universal architecture. It’s not a simple one. It’s complex. But it’s repeated throughout the brain.

And that’s where this, you know, the idea of the Thousand Brains … each of these cortical columns is actually a complete sensory-motor processing system. It has inputs; it has outputs. It’s getting sensory input. It’s sending outputs to motor systems. And it’s building, in our theory, complete world models. So there isn’t a single latent space. There’s thousands of these latent spaces.

And each little cortical column is trying to understand its little bit of the world. You know, one cortical column might be getting, at the lowest level, maybe one degree of visual information from the top right-hand corner of your retina. Another one might be focusing on specific frequencies in the auditory range. You know, each one has its own little view of the world, and it’s building its own little world model.

And then they all collaborate together. There’s no top or bottom here. There’s no homunculus in the brain. Everything is sort of equal. And they’re all simultaneously collaborating and voting and coming up to, you know, what is the, you know, consistent interpretation of all of these sensory inputs that we’re getting? What is the single consistent, you know, concept, if you will, and, based on that, make the motor actions that are most relevant to that.

So it’s a sensory-motor loop. It’s a, you know, it’s a constantly recurring system; we’re constantly making predictions. As we discussed earlier, you know, we are constantly learning. Every cortical column is constantly updating its connections, constantly updating its weights. It’s building and incrementally improving its world model constantly. So it’s a massively distributed, you know, set of processing elements that we call cortical columns that are, they’re all equal, operating in parallel.

So I think there are similarities, for sure, between them. But at least the way I described it, I think it’s very different in its operation than what I understand today’s LLMs to be. I don’t know if you agree with that or not.

**FUSI:**
Yeah, I …
To better understand, I had a question, which is, are these cortical columns relying on the fact that these are essentially multiple views of the same process and those multiple views, like, the, you know, the part of the sensory input that gets allocated or subdivided, is it happening at the same time point? So in other words, if you could artificially delay by some time
*t*
some cortical columns with respect to the rest, would the learning suffer?

**AHMAD:**
Yes, absolutely. Yeah.

**FUSI:**
And so in other words, how important is it that it’s, kind of, on the same schedule?

**AHMAD:**
[LAUGHS] Yeah, I mean, that’s another … I mean, LLMs today, you know, you get your input, one layer processes it, then the next, then the next, and the other layers are not operating. In the brain, it’s not like that. Everything is operating in parallel asynchronously. And this is important. They’re constantly trying to make predictions and so on. So if you were to artificially slow down some of your cortical columns, you would absolutely suffer. Your thinking would absolutely suffer.

**BURGER:**
I wanted to interject here just because this is where … this discussion is where, you know, I got
*super*
interested in the difference and then spent a bunch of time with Subutai to learn from him. So if I think about my skin, you know, which is an organ, you know, as I understand it, there’s a cortical column attached to each patch of my skin and the size of that patch, kind of, corresponds to the nerve density there.

**AHMAD:**
That’s right. Yeah.

**BURGER:**
So in my brain, there is a set of cortical columns that are skin sensors, and I could actually … if I numbered all the cortical columns in the brain, I could draw a map on my skin and say, “This is No. 72 in this patch. This is No. 73 in this patch.” Now are human cortical columns, like, better than, say, what we see in a mouse? And, of course, this is a leading question because I know the answer.

**AHMAD:**
[LAUGHS] Yeah. So, yes, it, you know, cortical columns in your sensory areas, primary sensory areas, each, you know, pay attention to or get input from a, you know, some patch of your skin somewhere on your body. And there’s many more cortical columns associated with your fingertips than, you know, a square centimeter of your back, for example. So there’s definitely, you know, areas of sensory information that we pay a lot more attention to and devote a lot more physical resources to.

In terms of a mouse and humans, it’s pretty remarkable that the cortical columns … so all mammals have cortical columns; all mammals have a neocortex. All mammals have cortical columns from a mouse all the way up to humans. And mice have cortical columns that are very, very similar to what a human has. It’s not identical. There
*are*
differences. But by and large, the architecture of a cortical column in a mouse is, you know, very, very similar to cortical columns in humans. Human cortical columns are bigger. There are more neurons, and there’s more detail there, but essentially, it’s the same. And …

**BURGER:**
Maybe just scaled up a little bit.

**AHMAD:**
Yeah. So evolution basically discovered this structure—that it’s really excellent for processing information and dealing with it—and then through, you know, very fast in evolutionary time, basically figured out that if you could scale up the number of cortical columns, you get more intelligent animals. And that’s what happened very, very fast evolutionarily.

**FUSI:**
I didn’t know about the unevenness of cortical columns present. Like, this is not … I’m not a neuroscientist, and so this is interesting because one of the biggest frustrations with many modern architectures of models is that they deploy a constant amount of computation no matter what the input is.

So I go through the same number of layers whether I’m trying to predict the word “dog” after “the” or whether I’m trying to solve, like, give the final answer to a very complicated math question or, you know, whether a theorem was proven or not in the prompt. And so that’s interesting because, like, some current instantiations of modern architecture actually deploy … try to cluster things together such that you have a constant amount of information that you then push together through the model. [LAUGHTER] And so maybe like on my fingertips, I need more processing than I need on my elbow because, like, you know … and so this, kind of, makes sense.

**BURGER:**
Nicolò is being humble. He was working on this problem two years ago and told me about it. It was one of the things I learned from you that made me think differently. So …

**FUSI:**
I just like to refer to
*people*
are working on this … [LAUGHS]

**BURGER:**
Random average people who are not all necessarily brilliant AI scientists.

So the prediction part of this, though, is really what’s fascinating to me, because, again, something else Subutai and I discussed many years ago, you know, if I’m, like, moving my finger towards the table and…my brain is making predictions because I have a world model. It knows a table is there. And the cortical columns representing that patch of skin, as it’s getting closer, they’re starting to predict that I’m going to feel something that feels
*like*
the table. And, yup, there; I hit it. Prediction met.

But if I touched it and it felt really icy cold or super hot or fluffy or not there—I pass through it—I’d get a flurry of activity because the prediction wouldn’t match the world model, and that’s where learning would happen.

Subutai, does that sound like the right model and intuition?

**AHMAD:**
Yeah, that’s definitely a very important component of it. We’re constantly making predictions. And as you said, you know, you’re moving your right fingertip down; you know, perhaps you’ve never sat in this room before or, you know, seen this table before, you would still have a prediction, a very good prediction of it.

**BURGER:**
Yeah.
Because you know what a table is.

**AHMAD:**
You know what a table is. And if it was different, you would, you know, you would notice it right away. But if your left hand, which you weren’t paying attention to, also felt icy cold, then you would notice that, as well. So you’re actually making not just one prediction; you’re making thousands and thousands of predictions constantly about …

**BURGER:**
Every cortical column.

**AHMAD:**
Every cortical column is making predictions. And if something were anomalous, highly anomalous, you would notice it. So this is something, you know, we don’t often realize; we’re making very, very granular predictions
*constantly*
. And when things are wrong, we do learn from it.

And the other interesting thing—and this is, again, possibly different from how LLMs work— you know, if I were to tell you to touch the, you know, the bottom surface of the table, you could without, again, without looking at the table or opening your eyes, you would be able to move your finger in and touch the bottom of your table because you have a, you know, set of reference frames that relate to …

**BURGER:**
Yup …

**AHMAD:**
There you go. Yep. You’re able to do it.

**BURGER:**
I did it! Yeah. Amazing.

**AHMAD:**
Even though you maybe never have been in this room; maybe you’ve never seen this table before. It doesn’t matter.

**BURGER:**
I’ve been in this room because we had to prep for the podcast series. But I didn’t touch the underside of the table, that’s for sure. [LAUGHS]

**AHMAD:**
Yeah, exactly. [LAUGHS] So, you know, we know where things are in relation to each other, where our body is in relation to everything, and we can very, very rapidly learn. And again, if the bottom part of the table was anomalous, you would notice it and potentially remember that.

**FUSI:**
I’m not going to lie. I was expecting you to find something under that table, [LAUGHTER] like a talk show.

**AHMAD:**
Or chewing gum or something.

**FUSI:**
*And if you reach under the table, you’re going to find a copy of my paper.*
[LAUGHS]

**BURGER:**
[LAUGHS] You know, if I was smarter and better prepared, that’s exactly what would have happened. But, sorry, guys.

I think you told me something, Subutai, you know, that … and I’ll give a little bit of preamble.

So, you know, the brain has these dendritic networks in each neuron, and they form synapses. And so a neuron fires, and that, you know, the axon of the neuron that’s firing will propagate a signal through the synapses, which might do a little signal processing to the dendrites of the downstream neurons, and those downstream—the dendrites can then prime the neuron to fire. That’s one of the fundamental mechanisms. And it’s the formation of those synapses, you know, between the upstream and downstream neurons, the dendrites, that seem to be the basis of learning, and to me, that feels a little bit like an attention map.

**AHMAD:**
Yes.

**BURGER:**
So maybe the dendritic network is doing something akin to self-attention, and we have some work going on in that direction at MSR. But the thing you told me was that your brain is actually forming an incredibly large number of synapses speculatively. In some sense, sampling the world when something happens in case it will recur. You know, it’s a more … maybe it’s a version of Hebbian learning, right? You know, things that fire together, wire together.

**AHMAD:**
Exactly.

**BURGER:**
But then if that pattern doesn’t recur, then they get pruned. And I’m just going to, you know, what is the fraction of your synapses to get turned over every three or four days, you know, ballpark?

**AHMAD:**
OK. Yeah, I remember this. This was an absolute mind-blowing
[study in [The Journal of] Neuroscience
(opens in new tab)](https://www.jneurosci.org/content/35/36/12535)
. So, you know, the way a lot of learning happens in the brain is by adding and dropping connections.

In AI models, it’s usually strengthening, you know, high-precision floating-point number, making it higher or lower. But you’re not adding and dropping connections. The connections are always—in fact, everything is fully connected, right, between layers. And so in the brain, you’re always adding and dropping connections. That’s a fundamental mechanism by which we learn,
*one*
of the fundamental mechanisms.

What I read in this study is that they looked at adult mice and adult animals, and what they found is that they would look at the number of synapses that were connected over the course of a couple of months—and they were able to trace individual synapses in this particular part of the brain—and what they found is that every four days, 30% of the synapses that were there were no longer there four days from now. And there was a new 30%. And there’s a huge number of connections that are constantly being added and constantly being pruned. And my theory of what’s going on there is that we’re always speculatively trying to learn things.

So, you know, there’s all sorts of random coincidences and things that we are exposed to on a day-to-day basis. We’re constantly forming connections there because we don’t know what’s actually going to be required and what’s real and what’s random. Most of it’s random; most of it’s not necessary. And the stuff that actually is necessary will stay on. But we’re constantly trying to learn.

This is a part of continuous learning that’s often not appreciated, I think, is that we’re constantly forming new connections, and then we prune the stuff that we don’t need. In an AI model, if you were to do that, it would just go, I don’t know, it would go bananas. [LAUGHTER]

**BURGER:**
Well, so let’s double-click on that. So when you told me that, the way I …

**AHMAD:**
This is mind-blowing, this 30%.

**BURGER:**
It’s crazy.

**AHMAD:**
Your brain is going to be totally different a few days from now.

**BURGER:**
It’s so mind-blowing. When you told me that, I spent some time processing it, so a whole bunch of synapses were created and destroyed during that time.

But it just made me think that we have, you know, we have all of these columns getting all of this input continuously. You know, eyes, hearing, smell, taste, skin, heat, and then, you know, interactions with people, and then planning and experiences, just at every level.
And they’re constantly sampling all this noise coming in and basically filtering out the noise. It’s like, kind of, like a low-pass filter. But when something statistically significant recurs, it’s going to lock and then become persistent.

**AHMAD:**
Yeah, yeah, I think so. There’s so much that’s happening, and you’re constantly learning, and, you know, when you touch a hot stove or something, there’s a flood of dopamine specific to those areas that caused these synapses to strengthen very, very quickly. You know, most of these synapses that are learned are very, very weak synapses.

**BURGER:**
Yup.

**AHMAD:**
And so, yeah, you know, when you look … in this study, they also quantified the turnover in, kind of, strong synapses versus weak synapses. And it’s comforting to know that the strong synapses stay there. It’s really these weak synapses that are constantly added and dropped. And then some of them will become strong.

**BURGER:**
Now I want to go back … return to Nicolò, but with an observation.

So when I’m training a transformer, it’s also a prediction-based system. You know, I’m running … I have my input in the training set; I have my masked token or the next token I’m trying to predict. I run it through. I look at how successfully did it make that prediction, and the worse it was, the, sort of, the steeper the error, you know, I drive back through the network. So, you know, if it’s spot-on, I don’t learn very much. But if the prediction is way off, I’ve got to change a bunch of stuff. That sounds analogous to what Subutai was just describing with the cortical columns.

**FUSI:**
No, that’s right. I mean, with, I don’t know, with one big pet peeve of mine in pretraining, in particular around pretraining these language models.

**BURGER:**
OK.

**FUSI:**
So again, for context, like, language models in particular, but, you know, many other
instantiations of large models, are trained in a few phases usually. One of them is pretraining, where you have some ground truth text and you remove, let’s say, just the last word, and then you ask the model to predict the last word. And that’s when you get that loss. Do you get the word right? Do you get the word wrong?

One of the big problems that I have is that, you know, in human experience, we do not get feedback every single thought.

The problem with language models, the way we are training them, at least in pretraining, is that they do a thing called teacher forcing. So they guess the word, then they get immediately the signal, and then the right word gets filled in, and then they predict the next one.

So when you go through, like, a passage of text, you constantly get this reward. And it’s such a bizarre way to train a model. It’s necessary because you want a lot of flow of supervision. Like, you want, like, a lot of supervision to essentially use all the computation available. But at the same time, it actually makes the models arguably a little bit worse than what they would be if you had enough compute to train them without this.

I went on a tangent just because it’s a pet peeve. [LAUGHS]

**BURGER:**
It’s a really important point, though, because your goal when you’re training a model is to get to your loss target with the minimal cost and time. Or, of course, like, fixed budget and, like, lowest loss target.

But, you know, biological systems, also, their goal is survival with energy minimization. And so, like, once you’ve built a world model that works, right, like touching the table, touching the underside of the table—nope, still nothing exciting there—like, it takes very little energy to do that. And I think a tragedy is that we all have these supercomputers in our heads. You know, the neocortex is what, about 10 watts? And it’s this amazing thing, right, that can compose symphonies. But once we have a world model, a lot of us just stop learning because it’s comfortable, right. You don’t have to perturb the state. You can go through … and, you know, I mean, how many of us go through every day and all of our predictions succeed [LAUGHTER], and there’s no surprises, you know?

So all the new synapses get swept away, right. That’s not a goal of pretraining because then you’re just wasting energy. But we’re trying to minimize energy consumption. So it does feel, kind of, aligned to me in some sense.

So I’ve got a straw man I want to hit you with, but before we do, Nicolò, I want you to talk about your view on compression, like LLMs as compressors, because I know this is something you’re very passionate about and opinionated about. And I’ve learned a lot from you on this, too.

And then, Subutai, after this, I’d like to hear your biological response. I mean, your response from a biological perspective. [LAUGHTER] And …

**AHMAD:**
You’ll get both.

**BURGER:**
That’s right, of course. And then I want to try … I want to throw out this hybrid straw man. So, Nicolò, tell us about compression.

**FUSI:**
The view is that basically the generative models are compressors in an information theoretic sense, and so trying to come up with a better generative model is equivalent to trying to find the best compressor for some data. And …

**BURGER:**
Now when you say compressor, do you mean lossless or lossy?

**FUSI:**
I mean lossless.

**BURGER:**
OK.

**FUSI:**
You can basically look at literally my much-maligned objective function that you use for pretraining, which is, you know, next-token prediction, and you can basically draw a complete parallel to what you would do if you were trying to come up with the, you know, try to do compression, which is coming up with the shortest possible code for something that you’re trying to compress.

And so the two things are the same, and it, kind of, fits into a broader picture that, you know, like, goes back to Occam’s razor and Kolmogorov complexity and Solomonoff’s principle of induction, which is, you want short descriptions for likely things that happen in the world and you want your algorithm that produces those short descriptions to be also short. That’s the minimum description length principle.

And I do feel like it fits in, kind of, also what you were saying about the concept of you have a good world model, why look for surprise? Because it simultaneously affects both terms, both the algorithm, like your own world model, but also the loss that you incur when something unexpected happens.

And so if I’m an agent in the world trying to minimize the minimum description length of the world, I’d like to go and seek some in-distribution data such that I don’t bump up my surprise term too much.

**BURGER:**
Right. And I think you said at some point that, you know, when I’m training a model, even though you took the same loss point, you know, between Model A and Model B, if I have a steeper loss curve in Model A than Model B, you know, it’s getting to a better, sort of, compressed-based vocabulary faster, which makes it more general. The shape of that curve matters from a compression perspective.

**FUSI:**
Yeah. I mean, I think it would help here to expand on what I was talking about in terms of, …

**BURGER:**
Yes. Please.

**FUSI:**
… like, minimum description length principle. The minimum description length principle is basically the loss of the model you’re training; that’s one component. And so it’s a sum over the mistakes you make at predicting or, you know, the mistakes you make at predicting each word. And that’s one term. And the other term is how long it takes you in code to describe the model and the training procedure, …

**BURGER:**
Right.

**FUSI:**
… to get to that training curve, to produce that training curve.

**BURGER:**
Right.

**FUSI:**
So, yes, if you look at collectively, one term is, kind of, fixed. It’s an amount of code it would take you to write out a language model, for instance, in code. Like, literally implement it,
*not the weights*
, just implement the initialization of it and then the training loop. And then on the other side, you have this training loss that gets generated as you start observing data. And, of course, because it’s a sum, you want to minimize really the area, like, you want to minimize the sum. And so, like, a flatter curve is much better than, like, the steeper curve, you know, even if it ends up at the end to be slightly better.

**BURGER:**
Yeah. Concave is better than convex.

**FUSI:**
Among other things, yes. [LAUGHTER]

**BURGER:**
Sorry. So, you know, I think that we could do a whole episode on this compression view because it’s really fascinating. And the lossless part of it is what blew my mind. And I think, you know, I’m guessing there are multiple camps here, and you’re squarely in one camp, so I’m guessing we’ll get a bunch of feedback from the other camps.

So, Subutai, you know, can I think of cortical columns as compressors?

**AHMAD:**
Yeah, it’s a good question. You know, I, you know, there’s so much in the compression literature that you can draw insight from. You know, if you look at the representations in cortical columns and that populations that neurons have, you know, some of the things you have to deal with are that the brain doesn’t have a huge nuclear power plant attached to it.

You know, we only have 12 watts or so to process everything we want to do, and the representations that evolution has discovered are incredibly sparse. And what that means is that you may have thousands and thousands of neurons in a layer, but only about 1% of them will actually be active at a time. And so it’s a very small subset of neurons that are actually active.

I don’t know about this minimum description length, whether that applies. I can say a couple of things about that. There’s, you know, by and large, the representations are very sparse when you’re predicting well. When you see a surprise, there’s a burst of activity.

**BURGER:**
Yup.

**AHMAD:**
When there’s something that’s unusual, there’s a lot more neurons that fire, and …

**BURGER:**
That’s why learning is
*tiring*
!

**AHMAD:**
That’s why learning [LAUGHTER] … exactly. No, no, that’s right, that’s right.

And so what we think is happening is that, you know, the actual representation of something is a very small number of neurons. When you’re surprised, there may be many things that are consistent with that surprise, and so your brain represents a union of all of those things at once.

And when you have a very sparse representation, you can actually have a union of many, many different things without getting confused. So that’s what we think is going on there. So it is a very compressed, very efficient representation. And because it’s such a small percentage of neurons that are firing, we are very, very parsimonious in how we represent things and extremely energy efficient metabolically.

**BURGER:**
I wanted to get to the efficiency point, but before I do, you know, you talk about this 1, you know, 1 to 2% of the neurons firing. But it’s, actually, the brain is actually much sparser than that at a fine grain, right?

**AHMAD:**
Yes, yes.

**BURGER:**
Because, you know, you have 1% of the neurons firing, but they aren’t connected to all the other neurons in the region.

**AHMAD:**
That’s right. Yeah.

**BURGER:**
So really the sparsity should be the product of the connectivity fraction times the activity factor.

**AHMAD:**
Yeah. Yeah.

**BURGER:**
Right. That’s about one out of 10,000. Something like that.

**AHMAD:**
Exactly. Yeah. So something like maybe 1% of the neurons are firing at any point in time, and maybe 1% of the connections that are possible are actually there at any point in time. So it’s a very, very small, you know, subnetwork through this massive network that’s actually being activated, a tiny percentage of neurons going through a very, very tiny piece of the full network.

You know, it’s common to, you know, some people say, “Oh, we’re only using 1% of our brain.” That’s not true. It just means at any point in time, you’re only using 1%, but at other points in time, a different 1% is being used. So, you know, the activity does move around quite a bit. But, any point in time, it’s extremely small.

**BURGER:**
So, OK, the sparsity, I think, you know, the representation—how the brain is doing this compression biologically—is super fascinating. And I want to go on a little bit of a detour now to efficiency. So I remember in 2017 when in MSR we were building, you know, hardware acceleration for RNNs.

And then the transformer hit, and they were optimized, you know, to be highly parallelizable across this quadratic attention map for GPUs. The way I would describe it is that that transition to semi-supervised training moved us from an era when we were really data limited, like you had to have good high-quality labeled data, to you were compute limited.

And when that transition happened, we hockey-sticked from, “I’m building faster machines but I’m limited by data” to the bigger machine I can build, as long as I have enough, you know, unlabeled data of high quality, the better I can do with the model. And so we went on the supercomputing arms race, and now we’re building these, like, just gargantuan machines.

And really, we’ve kind of been brute-forcing it. I mean, we’ve done a lot of things to optimize, like quantization, you know, and other and, you know, a better process node, you know, a better, more efficient tensor unit design. But to first order, we’ve been training bigger models by building bigger systems.

And I just wonder, do you think that the brain at this 10 to 12 watts in the neocortex just has a fundamentally more efficient learning mechanism? Or do we think that, you know, what we’re doing in transformers in the most advanced silicon is as efficient, we’re just building much larger, more capable models?

**AHMAD:**
Oh, I think without a doubt, transformers are extremely inefficient and very, very brute force. We touched on this a little bit earlier in the attention mechanism, where we’re, you know, transformers are essentially comparing every token to every other token. I mean, there are architectures which reduce that, for sure, but it’s essentially an
*n*
-squared operation. And we’re doing this at every layer.

I mean, there’s nothing like that in the brain. Our processing, you know, in some sense, the context for the very next word I’m about to say is my entire life, right? And the amount of time I take to take the next word doesn’t depend on the length of the context at all. It’s a constant time dependence on context.

So it’s a significant, you know, reduction in the compute that’s required. You can kind of think about, like the brain—I think has somewhere around maybe 70 trillion synapses. When I say the brain, I mean the neocortex, has about 70 trillion synapses. And it’s using only 12 watts. And a synapse is roughly equivalent to a parameter.

And if you were to take the most efficient GPUs today and try to run a 70 trillion parameter model, it would be something like a megawatt of power. It’s tens of thous … it’s orders of magnitude more inefficient than what our brain is doing. So I absolutely believe that.

**BURGER:**
The metric I use, to go back to your point, you know, is, this is something, I think we talked about this back in the day, right? When, you know, after this kicked off for a few years, we were trying to project, like, how far would this go under the current model to inform the research and the directions you took. Which is why I got so interested in sparsity and working with you.

And we would look at a training run and just say, how many joules did it take to train the whole model? How many parameters do we have? And sort of what’s our parameters per joule? And, if by that metric, you know, we were off by many orders of magnitude where the brain is, but I don’t know that that’s the right metric. So any thoughts on that?

**AHMAD:**
Yeah. I mean, in some ways, you know, transformers, you know, embody more knowledge in them than any human has.

**BURGER:**
Right.

**AHMAD:**
It has memorized, you know, the entire internet’s worth of knowledge, essentially.

**BURGER:**
All scientific papers …

**AHMAD:**
All scientific papers. You know, good and bad, whatever, you know, it has memorized everything. So that’s something that, you know, humans just cannot do. So there’s definitely stuff that’s better in transformers than humans.

But fundamentally, I think, you know, we’re extremely efficient in how we process the next token or the next bit of information that’s coming in. And I think there’s a lot we can learn from the brain and apply to LLMs and future AI models there.

**FUSI:**
I was going to ask a question related to that because … forget memorizing the internet. But let me give you another example that transformers do really well. And I’m wondering, like, you know, the human aspect of this or the brain aspect of this because transformers, because of the
*n-*
square computation, they’re really good at stuff, like a needle in the haystack.

So I can tell you right now, I can speak, I can talk to you, and I can tell you the password is something silly like “podcast microphone blue,” whatever. That’s the password. And then I can proceed and read the entire
*Odyssey*
or a bunch of other books to you out loud for the next 5 or 6 hours. And then I can ask the transformer, what was the password? And transformer will do this nice
*n*
-square computation many times, and it will spit out the password.

A human, you know, there will be a decay of that password. And then at some point, it won’t remember, and depending on the human, it may be in the first chapter of the
*Odyssey*
or like at the end, but … so fundamentally the type of computation that is done is very different. So it always makes me wonder about the efficiency because it’s just, like, it’s a different type of computation. So the efficiency of … like, efficiency is kind of like, what are you doing divided by how good are you at doing it. And so when the things we’re doing are so incomparable in many ways, that always makes me … always troubles me a little bit. I don’t know… I don’t know if there’s any question in there. [LAUGHTER]

**AHMAD:**
Yeah. I mean, transformers can do the stuff that humans find very, very difficult to do. Absolutely. You know, maybe there’s a way to get the best of both. I don’t know. You know, I don’t know that it’s fundamentally necessary to have such brute-force computation to get all of these features.

**FUSI:**
That’s right.

**BURGER:**
Yeah. Yeah, it is a weird thing because, you know, this is why memory palaces work so well. Like, there is a way, though, for a human to remember that my microphone is gray. It’s not actually blue, Nicolò.

**FUSI:**
Mine is blue. You don’t see it. It’s off camera. You see, your world model …

**BURGER:**
It’s off camera. Yeah, I know. I was just teasing you.

But there’s a way, like, if I can just connect it to enough things, get that connectivity graph, then I’ll remember it because it’s captured the signal out of the noise and connected to enough things I can retrieve it. And retrieval would be a whole other topic we don’t have time to get into today.

But I do … now, I want to go to the straw man. So let’s take continual learning off the table. Let’s imagine that, as I go through my day, I’m just saving all of the sensory data to put in my training set. And now imagine that I take 100,000 little transformer blocks, and I’m training them each with what they’re seeing.

OK, I replay the day so I don’t have to, again, I don’t have to worry about continuous learning and whatever cross-cortical column, you know, routing feature of the outputs, the inputs, and there’s—Subutai, we’ve talked about this—there’s a complex set of wiring there to bring features from here to there that gets learned. If I replicated that, could a transformer block kind of do what the cortical columns are doing?

Could I just instrument all my sensory patches with little transformer blocks and then wire them up in the right way and have it work?

**AHMAD:**
I think there’ll be … there’s still a couple of things we need. One is that cortical columns are fundamentally sensory motor. And so they’re actually, each one, each cortical column is initiating actions, as well. So you cannot have a static dataset fundamentally ahead of time. It’s always a dynamic because we’re constantly making movements to get the next bit of data. And so …

**BURGER:**
Couldn’t I tokenize that, though?

**AHMAD:**
I mean, you could tokenize the input and you can tokenize the output, but, you know, if you were to play the same set of inputs back again to a network that … a cortical column that’s randomly wired differently, it may make a different set of actions. And so as soon as it makes the first action that’s different, that dataset is no longer valid, right? It’s, you know, there is … you can’t fundamentally … you have to have a simulation of an environment rather than a static one-way dataset, if that makes sense.

So I think that’s one piece that I think’s missing in transformers today, is this, sort of, sensory-motor loop. And then the other piece we talked about is continuous learning.

**BURGER:**
Yeah.

**AHMAD:**
I guess you said take it off the table, but …

**BURGER:**
It’s fundamental.

**AHMAD:**
Fundamental … different. Yeah, yeah. And maybe one other difference. We talked, you know, much earlier about a single latent space and the prediction that’s being made at the top of the transformer that you compute the loss function, and that’s back-propagated through the transformer. That’s not how neurons learn. Neurons are making … every neuron is actually making predictions, and every neuron is getting its input.

And it’s learning independent of anything that happens at the top. And so it’s a much more granular learning signal. And information does flow from the top to bottom. But there’s also many, many other sources of information that it’s learning from. So it’s different in that sense, as well, mechanistically.

**BURGER:**
The reason I ask, and now I’d like to get into, you know, some of the … the fun speculation because I’ve just … it’s been a phenomenal discussion with the two. I think we’ve kind of elucidated the differences. Something I’ve wondered after I’ve talked to both of you … and, you know, Nicolò, kind of learning about this compression view of the world, lossless compression, and, Subutai, just, you know, the Thousand Brains Theory and these cortical columns and the sampling of, you know, the world to capture the signal that you can learn from.

So let’s say that I was able to design a really small, efficient digital cortical column. Maybe it’s transformer-based with some, you know, a sparse representation and some sensory-motor mechanism built in. Maybe it’s more dendritic-based, you know, mapped into digital hardware. And I put a cortical column on every sensor I have in the world, associated with every person, and wire them up together with some of this and then have a, you know, billions of them that can form higher-level abstractions. Like, what do you think would happen? What could we do?

**AHMAD:**
That’s a fantastic thought exercise, I think [LAUGHS]. You know, again, assuming the cortical column is faithful and can generate, you know, or suggest motor actions, as well. I mean, in some sense, you could potentially have a super intelligent system, right, that’s far more intelligent than anything else on the planet.

Now we’re scaling the number of cortical columns, you know, not from a mouse, you know, to a hundred thousand columns that a human might have, but potentially billions of cortical columns and way more. And there’s no reason to think there’s any fundamental limit there. So this sort of a system is, I think, the way that superintelligent systems will eventually be built.

**BURGER:**
But this is a very different direction …

**AHMAD:**
It’s a very different …

**BURGER:**
… than the one we’re currently headed down with, like, these monolithic models where we’re doing tons of RL, you know, to capture, you know, to get high-value human collaboration in distribution.

**AHMAD:**
Yes. It’s completely different than the direction we’re proceeding.

So I think they, you know, to go down that path, there needs to be a fundamental rethinking of some of our assumptions, potentially even down to the hardware architectures that are necessary to implement it. The, you know, fundamental learning algorithms, the fundamental training paradigm. We talked about, you know, you can’t have a static dataset. You’re constantly moving around in the world and doing things. So it’s a very, very different way of going about AI than what we’re doing today.

**BURGER:**
Sounds like a great time to be an AI researcher.

**AHMAD:**
Absolutely. [LAUGHTER]

**BURGER:**
Nicolò, what was your reaction to that hypothesis?

**FUSI:**
It sounds super interesting. I mean, my brain was churning. You know, my background is very different. And so, like, I’m in a much worse position to answer this question. But I was starting to think, OK, so let’s say I do this. What would be my loss function? What, you know, how would information flow through the system? Like, sounds like cortical columns would each have their own loss that then I would aggregate—and then I would add a contribution that is, like, higher level.

And then back to my question. You know, how is the temporal information coordinated? Because one way to see this is that, you know, the way I’m coming to understand this is that it’s kind of like a multi-view framework.

You have the same phenomena represented to multiple independent, but at the same time, views. And so part of me is like it feels like that you need to tie together these cortical columns in such a way that they all get that gradient feedback if you’re training with gradient-based methods, for instance. And so that’s, kind of, it feels super, super interesting.

It is related to a lot of, you know, very superficially, to a lot of ideas in machine learning around, hey, is it better to have one giant super deep network? Is it better to have a bunch of shallow networks? But the difference is also in the way you train them, right? We typically train this bunch of shallow networks on kind of the same objective and the same data and not typically into an experiential cycle. Whereas this sounds like this is a different way to do it.

**BURGER:**
Right, right.
I think … I want to pull this back around to the title of the podcast. And so I’ll share an observation. You know, so I’ve been using some of the latest models to code. You know, they’re getting better really fast. I’ve been using them to kind of relearn some of the physics that I never really understood deeply.

You know, especially in general relativity, like E=MC
2
. Like, why is C in there at all, right? Just stuff like that. Because now it can actually explain it to me, and I can keep beating at it until I understand it, and then, of course, work.

And at some point, I asked the model, “Can you describe how I think?” And I was just curious. And it, you know, it gave me a page description that my jaw dropped because I said this, this thing knows me better than I know myself. I don’t think any human being, including me, could have captured kind of the way my approach to learning and my brain works, and I just read it as, like, like, yep, that’s right. And I learned something about myself.

So I wouldn’t say that it passed the Turing test because this is way beyond Turing test. This was like, this thing knows me way better, you know, than I thought any machine ever could. I mean, I’m having a conversation with it. It could be human, but it’s superhuman. So in some sense, it’s like intelligent beyond human capabilities with its ability to discern patterns in how someone’s interacting.  And yet it’s a tool. You know, it’s not conscious. It doesn’t have agency, embodiment, emotion. It understands a lot of that stuff from the training data. But at the end of the day, it’s a stochastic parrot, right? It’s got, you know, it’s got the weights, and I give it a token, and it outputs a token. So, like, are these machines intelligent or not?

**FUSI:**
I’ll let Subutai answer first. [LAUGHS]

**AHMAD:**
OK. You know, you know, it’s definitely a savant, right? It knows a huge amount about the world. It’s absorbed a lot of stuff, and it can articulate that in ways that are just amazing. And, you know, it’s taken your chat history with, you know, presumably thousands of chats and able to summarize that in a way that’s remarkable.

At the same time, I think, you know, transformers are not intelligent in the way that a three-year-old is, right? A three-year-old human is very curious, is constantly learning. It can learn almost anything. And, you know, a three-year-old Einstein was able to learn and eventually come up with theories that shook the world. That, you know, E=MC
2
.

And so, you know, could a transformer do that? I don’t think so. And so I think there’s still a difference. There’s things it can do that are amazing. But there are still basic things that a child can do that transformers cannot do. So I think there’s still a gap there. Exactly how to articulate it, and how to bridge that gap, is, of course, the trillion-dollar question. But it is bridgeable. And there is a gap today.

**BURGER:**
Right. Nicolò?

**FUSI:**
You know, I think, from my perspective, they are intelligent. And from my perspective, I go back to the definition of intelligent, which is like, can you achieve your objectives in a variety of environments? It’s a very basic fundamental, but it’s kind of, you know, it can be embodied, a form of embodied intelligence, an agentic intelligence. If I plop you in an environment, and I give you an objective, can you achieve it? And the wilder the environment, the harder the task is.

And I do think … I agree with Subutai. Like, there is a jaggedness of intelligence we keep describing.

**BURGER:**
Yup.

**FUSI:**
Like these things cannot be simultaneously super good, you know, Olympiad-level mathematicians and still give you stupid answers when you’re trying to, I don’t know, you know, figure out which cable goes where in your … in your car’s battery, you know, like, whatever.

**BURGER:**
[LAUGHS] Well, then it’s better than me. I’m not an Olympiad-level mathematician, and I do stupid stuff all the time.

**FUSI:**
I know exactly. Well, you know, whatever that was, that was a bad example. But you get it. But part of it goes back to the compression view. Like, I do believe that intelligence is compression. So the ability to come up with succinct explanations for complex phenomena and even succinct explanations for complex worlds, and then it implies or leads to your ability to operate within them, and the fact that we have these things that they can prove crazy theorems but at the same time fail at fairly rudimentary tasks is a sign that the, yes, transformers are great in terms of inductive biases they put on the world and computation that are great, but we’re ultimately all subject to the
[No Free Lunch Theorem
(opens in new tab)](https://ieeexplore.ieee.org/document/585893)
.

You know, across the world, the set of tasks that you could be pursuing. You know, you have certain inductive biases that kind of privilege certain tasks at the expense of others. And there isn’t, like, a thing yet that has expanded our set of tasks that are addressable. And so I do think that it’s a matter of rethinking our approach to a few things, whether I think likely both on the architecture front and on the losses and the way we train these systems front. I think there is an opportunity to expand the intelligent frontier of these models. But yeah, from my perspective, they are intelligent already just in a jagged way.

**BURGER:**
It’s such an interesting question, and I know a lot of people write a lot about this, so I don’t think treading any new ground here. But, you know, there’s the diversity of the tasks you can excel at. You know, are you able to handle nuance and understand things deeply? Are you able to learn continuously? Right now, the systems can’t, right. Are you embodied? I don’t know if that matters. Do you have an objective? Well, we could give them one. Are you conscious? Is that … I mean, that’s a whole other thing.

So it just feels like there’s a bunch of check boxes, and we’ve checked a bunch of them, and a bunch of them are unchecked.
And maybe there’s no consensus on, like, where that threshold is because there are many dimensions of intelligence, and some of which humans don’t even have.

**FUSI:**
And that’s why we have the term AGI and ASI, and people are debating the
*G*
and the
*S*
—what is general, what is specialized. So there is, like, it’s a huge discourse, like, for sure. But that’s why we had to start characterizing. But if you go back in the definition, going back to my schooling, go back to the definition of intelligence from Plato and Aristotle and Descartes, like, in some sense, you see the goalpost moving through the centuries around what we define as intelligent.

**BURGER:**
Right.

**FUSI:**
And I feel like we are still doing it.

**BURGER:**
Yeah. We’ll be doing it for a long time, you know, which in AI velocity is probably another like four or five years.

Hey, I just want to thank you both for the dialogue. You know, I treasure both of you as, you know, intellects and scholars and friends. It was just a joy to nerd out with you all. So thank you both for taking the time.

**AHMAD:**
Thank you so much, Doug, for having me.

**FUSI:**
Thank you for having us. This was great.

[MUSIC]

**STANDARD OUTRO:**
You’ve been listening to
*The Shape of Things to Come*
, a Microsoft Research Podcast. Check out more episodes of the podcast at aka.ms/researchpodcast or on YouTube and major podcast platforms.

[MUSIC FADES]