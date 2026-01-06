---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-21T00:01:19.433085+00:00'
exported_at: '2025-11-21T00:01:22.240519+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/bioclip2-foundation-ai-model
structured_data:
  about: []
  author: ''
  description: BioCLIP 2 is an NVIDIA-accelerated, biology-based foundation model
    trained on the biggest, most diverse dataset of organisms to date.
  headline: 'The Largest Digital Zoo: Biology Model Trained on NVIDIA GPUs Identifies
    Over a Million Species'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/bioclip2-foundation-ai-model
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'The Largest Digital Zoo: Biology Model Trained on NVIDIA GPUs Identifies Over
  a Million Species'
updated_at: '2025-11-21T00:01:19.433085+00:00'
url_hash: 4f771f20fdb3cbbb7746dc583bc177db719a3e66
---

Tanya Berger-Wolf’s first computational biology project started as a bet with a colleague: that she could build an AI model capable of identifying individual zebras faster than a zoologist.

She won.

Now, the director of the
[Translational Data Analytics Institute](https://tdai.osu.edu/)
and a professor at The Ohio State University, Berger-Wolf is taking on the whole animal kingdom with
[BioCLIP 2](https://arxiv.org/pdf/2505.23883)
, a biology-based
[foundation model](https://blogs.nvidia.com/blog/what-are-foundation-models/)
trained on the biggest, most diverse dataset of organisms to date. The model will be showcased at this year’s
[NeurIPS](https://neurips.cc/)
AI research conference.

BioCLIP 2 goes beyond extracting information from images. It can distinguish species’ traits and determine inter-and intraspecies relationships. For example, the model arranged Darwin’s finches by beak size, without teaching the concept of size, shown in the image below.

![](https://blogs.nvidia.com/wp-content/uploads/2025/11/nvidia-beak-size-1680x1215.jpg)


Scatter plot shows how BioCLIP 2 arranges Darwin’s finches by beak size from left to right.

These capabilities will allow researchers to use the model as both a biological encyclopedia, a powerful scientific platform and an interactive research tool with inference capabilities to help address an ongoing issue in conservation biology: data deficiency for certain species.

“For iconic species like killer whales, we lack enough data to determine population size and for polar bears, the population is unknown,” said Berger-Wolf. “If we don’t have data for those species, what hope do the beetles and fungi have?”

AI models can enhance existing conservation efforts for threatened species and their habitats by filling this data-deficiency gap.

BioCLIP 2 is
[available under an open-source license on Hugging Face](https://huggingface.co/spaces/imageomics/bioclip-2-demo)
, where it was downloaded over 45,000 times last month. This paper builds on the first BioCLIP model, released over a year ago, which was also trained on NVIDIA GPUs and received the Best Student Paper award at the
[Computer Vision and Pattern Recognition](https://www.nvidia.com/en-us/events/cvpr/)
(CVPR) conference.

The BioCLIP 2 paper will be presented at NeurIPS, taking place Nov. 30-Dec. 5 in Mexico City, and Dec. 2-7 in San Diego.

## **Building the World’s Biggest Biological Flash Card Deck**

The project began with the compilation of a massive dataset,
[TREEOFLIFE-200M](https://huggingface.co/datasets/imageomics/TreeOfLife-200M)
, which comprises 214 million images of organisms that span over 925,000 taxonomic classes — from monkeys to mealworms and magnolias.

![](https://blogs.nvidia.com/wp-content/uploads/2025/11/funky-monkey-1680x945.png)

To curate this vast amount of data, Berger-Wolf’s team at the
[Imageomics Institute](https://imageomics.osu.edu/)
collaborated with the
[Smithsonian Institution](https://www.si.edu/)
, experts from various universities and other field-related organizations.

These researchers set out to discover what would happen if they trained a biology model on more data than ever.

The team wanted to see if it was possible to move “beyond the science of individual organisms to the science of ecosystems,” said Berger-Wolf.

After 10 days of training on 32 NVIDIA H100 GPUs, BioCLIP 2 displayed novel abilities, such as distinguishing between adult and juvenile as well as male and female animals within species — without being explicitly taught these concepts.

It also made associations between related species — like understanding how zebras relate to other equids.

“This model learns that at every level of taxonomy, all of these images of zebras have a particular genus label, and of these images of equids — including zebras, horses and donkeys — they have a particular family trait and so on,” she said. “It learns the hierarchy without ever being told it, just through these associations.”

The model can even determine the health of an organism based on training data. For example, it separated healthy apple or blueberry leaves from diseased leaves, as well as could recognize differing types of diseases, when generating the scatter plot below.

![](https://blogs.nvidia.com/wp-content/uploads/2025/11/nvidia-plant-doc-1680x447.jpg)


The scatter plots show plant species better separated as the model is trained. The intra-species variations also form clusters, making them easier to separate.

Berger-Wolf’s team used a cluster of 64
[NVIDIA Tensor Core GPUs](https://www.nvidia.com/en-us/data-center/tensor-cores/)
to accelerate model training, plus individual Tensor Core GPUs for
[inference](https://www.nvidia.com/en-us/glossary/ai-inference/)
.

“Foundation models like BioCLIP would not be possible without NVIDIA accelerated computing,” said Berger-Wolf.

## **Wildlife Digital Twins: The Future of Studying Ecosystem Relationships**

The researchers’ next endeavor is to develop a wildlife-based interactive digital twin that can be used to visualize and simulate ecological interactions between species as well as their ways of engaging with the environment.

The goal is to provide a safe, easy way to study organismal relationships that naturally occur in the wild, while minimizing impact and disturbance on ecosystems.

“The digital twin allows us to visualize species interactions and put them in context, as well as to play the what-if scenarios and test our models without destroying the actual environment — creating as light a footprint as possible,” said Berger-Wolf.

The digital twin will give scientists the opportunity to explore the points of view of the species they’re studying within the simulated environment, opening endless possibilities for more complex and accurate ecological research.

Eventually, versions of this technology could even be deployed for public use — such as through interactive platforms at zoos. People could explore, visualize and learn about the natural environment and its many species from entirely new vantage points.

“I’m getting goosebumps just imagining that scenario of a kid coming into the zoo and being like, wow — this is what you would see if you were another zebra part of that herd, or if you were the little spider sitting on that scratching post,” Berger-Wolf said.

*Learn more about*
[*BioCLIP 2*](https://arxiv.org/abs/2505.23883)
.