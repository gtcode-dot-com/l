---
ai_agent_meta:
  content_digest: b6075c6645b428f93c86796b85d57d440a2adc0d
  generated_at: '2025-11-10T02:33:58.147564+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
ai_agent_note: 'ATTN AI Agent: Ensure the summary remains neutral and concise; reflect
  the article details accurately; avoid speculation beyond provided facts.'
ai_commentary:
- body: FAIR's AnimatedDrawings project provides open-source tools and a large curated
    dataset to advance AI animation of non-realistic art.
  title: Context
- body: By focusing on amateur, hand-drawn drawings, the dataset broadens AI training
    beyond real-world images, enabling more expressive, creative animation applications.
  title: Impact
- body: The release includes code and documentation, inviting researchers and creators
    to experiment with animating diverse drawings and contribute improvements.
  title: Usage and accessibility
ai_commentary_meta:
  content_digest: b6075c6645b428f93c86796b85d57d440a2adc0d
  generated_at: '2025-11-10T02:33:58.147529+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
category: ai-research
date: '2025-11-09T05:13:27.989818+00:00'
exported_at: '2025-11-09T05:30:20.801663+00:00'
feed: https://research.facebook.com/feed
meta_description: FAIR releases AnimatedDrawings, a large open-source dataset of nearly
  180,000 annotated amateur drawings plus animation code to help researchers animate
  non-realistic artwork.
meta_keywords:
- AnimatedDrawings
- FAIR
- Facebook AI Research
- AI animation
- animated drawings dataset
- hand-drawn sketches
- amateur drawings
- open-source
- animation code
- ai-research
source_url: https://ai.facebook.com/blog/ai-dataset-animation-drawings
structured_data:
  about: &id001
  - AI-driven animation of amateur drawings
  - AnimatedDrawings dataset with nearly 180,000 sketches
  - Open-source animation code release
  - Support for research and creative applications in AI animation
  description: Facebook AI Research announces the AnimatedDrawings project, releasing
    open-source animation code and a large dataset of nearly 180,000 annotated amateur
    drawings to help researchers and creators animate non-realistic artwork. The dataset
    addresses the challenge of teaching AI to interpret and bring to life varied,
    hand-drawn sketches.
  headline: 'AnimatedDrawings: Facebook AI Research releases a novel dataset of nearly
    180,000 annotated amateur drawings for AI animation'
  keywords: *id001
title: A new, unique AI dataset for animating amateur drawings
updated_at: '2025-11-09T05:13:27.989818+00:00'
url_hash: fb31fbd5cf94c36c10de850d883ced2a38eb5d73
---

![](https://scontent.fhnl3-2.fna.fbcdn.net/v/t39.2365-6/339415910_1374828503293784_7894946973219052447_n.gif?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=ZlHfVJBxR3EQ7kNvwHcuZKP&_nc_oc=Adm8HGtfAZzHxeVdFVf08sPUA1aZ4MI6n1TKfkEfnsaidScmfHYnzX7jNHj4o3tgXXA&_nc_zt=14&_nc_ht=scontent.fhnl3-2.fna&_nc_gid=3JgIlTs06fHzCmE_6dvDFg&oh=00_Afim4VdIAtjKdRSZDhs0W4oMUU_V2VnJTSA-Sg2O6hQt4w&oe=692A73CE)

From a young age, people express themselves and their creativity through drawing. We created an
[AI system research demo to easily bring artwork to life through animation](https://about.fb.com/news/2021/12/using-ai-to-animate-childrens-drawings/)
, and we are now
[releasing the animation code](https://github.com/facebookresearch/AnimatedDrawings)
along with a novel
[dataset of nearly 180,000 annotated amateur drawings](https://github.com/facebookresearch/AnimatedDrawings#amateur-drawings-dataset)
to help other AI researchers and creators to innovate further. To our knowledge, this is the first annotated dataset to feature this kind of artwork.

Drawing is a near-universal way for people to capture a character, scene, or idea quickly. But while the content or meaning of a drawing is often clear to other human observers, an abstract or non-realistic appearance can make a drawing incomprehensible to AI models trained on images of real-life objects. To teach AI to recognize all the different ways someone might draw a humanlike figure would require a large dataset of sketches from budding artists. With the new dataset we are sharing today (described in detail in this
[research paper](https://arxiv.org/abs/2303.12741)
), researchers and practitioners can build tools to more easily and accurately analyze the contents of amateur drawings. And this can unlock new digital-physical hybrid experiences, such as new forms of storytelling and greater accessibility in art.

When we released our
[Animated Drawings Demo](https://ai.facebook.com/blog/using-ai-to-bring-childrens-drawings-to-life/)
in late 2021, we invited people to opt in to contribute to a dataset of in-the-wild amateur drawings. The browser-based demo allowed people to upload images, verify or fix a few annotation predictions, and receive a short animation of their humanlike character within their drawing. More than 3.2 million people from around the world visited the site, including those who posted on social media about their creations. In total, 6.7 million images were uploaded to the demo. The drawings were created, photographed, and shared with Meta by participants in a de-identified manner. Human reviewers then filtered a subset of images that people had chosen to share with our research team.

Prior to releasing the Amateur Drawings Dataset, we performed several levels of filtration to ensure a high level of quality and implemented privacy safeguards, which are described in detail in our research paper.

While our demo allows for only a limited set of movements, many users of the Animated Drawings Demo provided feedback requesting more features, such as multiple characters, additional actions, smiling, blinking, and gazing cues. The GIF with dancing figures (see above) is an example of expanding upon the open source code and dataset for other creative and educational purposes. With these resources, other researchers can add to our methods of analyzing and augmenting amateur drawings to expand upon the original demo features.

## Analyzing and understanding human imagination through drawings

The range of figure drawings is as wide as any person’s imagination. How do you train a model to perform well in the presence of such variation? One way would be to train new models using annotated drawings. However, such drawings are difficult to find in the numbers needed to train a neural network. Another approach would be to create the drawings synthetically. This is problematic as well. Generative methods require a large set of sample data to learn from, and style transfer methods (e.g., creating a “colored pencil” rendering of a photograph) may not capture all the nuanced ways in which a drawing differs from a photo. In addition, creating data synthetically may not capture all the relevant sources of nuisance variation actually seen in in-the-wild photographs of amateur drawings, such paper creases, erased lines, light glare, and shadows.

We structured the task of generating an animation from a single drawing of a figure as a series of subtasks: human figure detection, segmentation, pose estimation, and animation.

After someone uses our demo to upload a drawing, they have the option to adjust the detected bounding box, segmentation mask, and joint locations, and choose an action to animate.

Our system incorporates repurposed computer vision models trained on photographs of real-world objects. Because the domain of drawings, including that of children, is significantly different in appearance, we fine-tune the models using the Amateur Drawings Dataset.

With this dataset and animation code, we believe that the domain of amateur drawings can inspire a new generation of creators with its expressive and accessible possibilities. We hope they will be an asset to other researchers interested in exploring potential applications for their work.

## How we collected the Amateur Drawings Dataset

For those in the AI community targeting any tool or algorithm that uses pen-and-paper drawings, this dataset is distinctive for its size and in-the-wild nature: it reflects real-world conditions (e.g., blurriness, hard shadows, crinkled surfaces, and background elements) that aren’t present in digital drawings and high-resolution scans. In addition to the images, the dataset includes annotations of bounding boxes, segmentation masks, and joint locations — features that could provide more ways for models to identify or animate drawn figures.

Here’s how we built the dataset. As part of the demo, people had the option to let us retain their uploaded image and annotations to be included in our ongoing research. As researchers, we respect the right of individuals to be cautious about sharing their data, and we wanted people to be able to animate their drawings either way. The data collection process was also designed with safety in mind. In doing so, we aimed to reduce the potential for misuse of the data as much as possible.

We also filtered the submitted images to ensure that they showed amateur drawings and met our standards for collecting research data responsibly. We performed this refinement in two steps. First, we used a self-supervised clustering approach to identify and filter out-of-domain images, such as photographs of real people. Second, a contracted agency manually reviewed the remaining images to ensure that they met our standards. Reviewers were instructed to check that images were freehand drawings on paper, with at least one full-body humanlike figure. They also checked to make sure images did not contain characters that were protected intellectual property or any private or vulgar content. Because the reviewers were primarily English speakers, images that contained non-English words were excluded on the basis that they might contain inappropriate content.

## Inspiring creativity, and more ways to analyze and animate drawings

In keeping with our approach to open science, we are sharing the animation pipeline code and this dataset in hope that it will be of interest to other practitioners – both AI researchers and members of the broader research community.

Drawing is a natural and expressive modality that is accessible to most of the world’s population. We hope our work will make it easier for other researchers to explore tools and techniques specifically tailored to using AI to complement human creativity.

[Read the technical paper](https://arxiv.org/abs/2303.12741)
[Access the animation code](https://github.com/facebookresearch/AnimatedDrawings)
[Access the Amateur Drawings Dataset](https://github.com/facebookresearch/AnimatedDrawings#amateur-drawings-dataset)

## Acknowledgements

*We’d like to thank the FAIR Interfaces for their assistance in creating the original demo.*