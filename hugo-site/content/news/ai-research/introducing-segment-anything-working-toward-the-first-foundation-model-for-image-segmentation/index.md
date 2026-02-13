---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T06:48:29.772398+00:00'
exported_at: '2026-02-13T06:48:35.969687+00:00'
feed: https://research.facebook.com/feed
language: en
source_url: https://ai.facebook.com/blog/segment-anything-foundation-model-image-segmentation
structured_data:
  about: []
  author: ''
  description: By sharing our research and dataset, we hope to further accelerate
    research into segmentation and more general image and video understanding.
  headline: 'Introducing Segment Anything: Working toward the first foundation model
    for image segmentation'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://ai.facebook.com/blog/segment-anything-foundation-model-image-segmentation
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Introducing Segment Anything: Working toward the first foundation model for
  image segmentation'
updated_at: '2026-02-13T06:48:29.772398+00:00'
url_hash: dc65fff014e31e9c73ba97e9cc12243f47f41935
---

Something Went Wrong

We're having trouble playing this video.

Segmentation — identifying which image pixels belong to an object — is a core task in computer vision and is used in a broad array of applications, from analyzing scientific imagery to editing photos. But creating an accurate
[segmentation model](https://ai.facebook.com/blog/efficient-accurate-object-detection-for-hundreds-of-uncommon-object-classes/)
for specific tasks typically requires highly specialized work by technical experts with access to
[AI training infrastructure](https://ai.facebook.com/blog/ai-rsc/)
and large volumes of carefully annotated in-domain data.

Today, we aim to democratize segmentation by introducing the Segment Anything project: a new task, dataset, and model for image segmentation, as we explain in our
[research paper](https://arxiv.org/abs/2304.02643)
. We are releasing both our general
[Segment Anything Model (SAM)](https://github.com/facebookresearch/segment-anything)
and our
[Segment Anything 1-Billion mask dataset (SA-1B)](https://ai.facebook.com/datasets/segment-anything/)
, the largest ever segmentation dataset, to enable a broad set of applications and foster further research into foundation models for computer vision. We are making the SA-1B dataset available for research purposes and the Segment Anything Model is available under a permissive open license (Apache 2.0). Check out the
[demo to try SAM](https://segment-anything.com/)
with your own images.

Reducing the need for task-specific modeling expertise, training compute, and custom data annotation for image segmentation is at the core of the Segment Anything project. To realize this vision, our goal was to build a foundation model for image segmentation: a promptable model that is trained on diverse data and that can adapt to specific tasks, analogous to how prompting is used in natural language processing models. However, the segmentation data needed to train such a model is not readily available online or elsewhere, unlike images, videos, and text, which are abundant on the internet. Thus, with Segment Anything, we set out to simultaneously develop a general, promptable segmentation model and use it to create a segmentation dataset of unprecedented scale.

SAM has learned a general notion of what objects are, and it can generate masks for any object in any image or any video, even including objects and image types that it had not encountered during training. SAM is general enough to cover a broad set of use cases and can be used out of the box on new image “domains” — whether underwater photos or cell microscopy — without requiring additional training (a capability often referred to as zero-shot transfer).

In the future, SAM could be used to help power applications in numerous domains that require finding and segmenting any object in any image. For the AI research community and others, SAM could become a component in larger AI systems for more general multimodal understanding of the world, for example, understanding both the visual and text content of a webpage. In the AR/VR domain, SAM could enable selecting an object based on a user’s gaze and then “lifting” it into 3D. For content creators, SAM can improve creative applications such as extracting image regions for collages or video editing. SAM could also be used to aid scientific study of natural occurrences on Earth or even in space, for example, by localizing animals or objects to study and track in video. We believe the possibilities are broad, and we are excited by the many potential use cases we haven’t even imagined yet.

Something Went Wrong

We're having trouble playing this video.

Segment Anything’s promptable design enables flexible integration with other systems. SAM could receive input prompts, such as a user’s gaze from an AR/VR headset, like

[Project Aria](https://about.meta.com/realitylabs/projectaria/)

.

## SAM: A generalized approach to segmentation

Previously, to solve any kind of segmentation problem, there were two classes of approaches. The first, interactive segmentation, allowed for segmenting any class of object but required a person to guide the method by iteratively refining a mask. The second, automatic segmentation, allowed for segmentation of specific object categories defined ahead of time (e.g., cats or chairs) but required substantial amounts of manually annotated objects to train (e.g., thousands or even tens of thousands of examples of segmented cats), along with the compute resources and technical expertise to train the segmentation model. Neither approach provided a general, fully automatic approach to segmentation.

SAM is a generalization of these two classes of approaches. It is a single model that can easily perform both interactive segmentation and automatic segmentation. The model’s promptable interface (described shortly) allows it to be used in flexible ways that make a wide range of segmentation tasks possible simply by engineering the right prompt for the model (clicks, boxes, text, and so on). Moreover, SAM is trained on a diverse, high-quality dataset of over 1 billion masks (collected as part of this project), which enables it to generalize to new types of objects and images beyond what it observed during training. This ability to generalize means that, by and large, practitioners will no longer need to collect their own segmentation data and fine-tune a model for their use case.

Taken together, these capabilities enable SAM to generalize both to new tasks and to new domains. This flexibility is the first of its kind for image segmentation.

Here is a short video showcasing some of SAM’s capabilities:

Something Went Wrong

We're having trouble playing this video.

(1) SAM allows users to segment objects with just a click or by interactively clicking points to include and exclude from the object. The model can also be prompted with a bounding box.

(2) SAM can output multiple valid masks when faced with ambiguity about the object being segmented, an important and necessary capability for solving segmentation in the real world.

(3) SAM can automatically find and mask all objects in an image.

(4) SAM can generate a segmentation mask for any prompt in real time after precomputing the image embedding, allowing for real-time interaction with the model.

## How SAM works: Promptable segmentation

In natural language processing and, more recently, computer vision, one of the most exciting developments is that of foundation models that can perform zero-shot and few-shot learning for new datasets and tasks using “prompting” techniques. We took inspiration from this line of work.

We trained SAM to return a
*valid*
segmentation mask for
*any*
prompt, where a prompt can be foreground/background points, a rough box or mask, freeform text, or, in general, any information indicating what to segment in an image. The requirement of a
*valid*
mask simply means that even when a prompt is
*ambiguous*
and could refer to multiple objects (for example, a point on a shirt may indicate either the shirt or the person wearing it), the output should be a reasonable mask for
*one*
of those objects. This task is used to pretrain the model and to solve general downstream segmentation tasks via prompting.

We observed that the pretraining task and interactive data collection imposed specific constraints on the model design. In particular, the model needs to run in real time on a CPU in a web browser to allow our annotators to use SAM interactively in real time to annotate efficiently. While the runtime constraint implies a trade-off between quality and runtime, we find that a simple design yields good results in practice.

Under the hood, an image encoder produces a one-time embedding for the image, while a lightweight encoder converts any prompt into an embedding vector in real time. These two information sources are then combined in a lightweight decoder that predicts segmentation masks. After the image embedding is computed, SAM can produce a segment in just 50 milliseconds given any prompt in a web browser.

![](https://scontent.fhnl3-2.fna.fbcdn.net/v/t39.2365-6/338558258_1349701259095991_4358060436604292355_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=z7W-Xk6F1dkQ7kNvwHpCuPB&_nc_oc=AdkzPzXWU7kcMCTwQMlMep_zWwjJrPkzY6F-z5eYtHjsaWE90c8qMy2W1lbGysOfgwg&_nc_zt=14&_nc_ht=scontent.fhnl3-2.fna&_nc_gid=igYKb9UNvhaXv54Qh1ON8g&oh=00_AfswMAeZwxpaAq-kQP7-fe3Xo0BAEhMNnWkZcDxYqsEHtA&oe=69A904C9)

In a web browser, SAM efficiently maps the image features and a set of prompt embeddings to produce a segmentation mask.

## Segmenting 1 billion masks: How we built SA-1B

To train our model, we needed a massive and diverse source of data, which did not exist at the start of our work. The segmentation dataset we are releasing today is the largest to date (by far). The data was collected using SAM. In particular, annotators used SAM to interactively annotate images, and then the newly annotated data was used to update SAM in turn. We repeated this cycle many times to iteratively improve both the model and dataset.

With SAM, collecting new segmentation masks is faster than ever before. With our tool, it only takes about 14 seconds to interactively annotate a mask. Our per-mask annotation process is only 2x slower than annotating bounding boxes, which takes about 7 seconds using the fastest annotation interfaces. In comparison with previous large-scale segmentation data collection efforts, our model is 6.5x faster than COCO fully manual polygon-based mask annotation and 2x faster than the previous largest data annotation effort, which was also model-assisted.

However, relying on interactively annotating masks does not scale sufficiently to create our 1 billion mask dataset. Therefore, we built a data engine for creating our SA-1B dataset. This data engine has three “gears.” In the first gear, the model assists annotators, as described above. The second gear is a mix of fully automatic annotation combined with assisted annotation, helping increase the diversity of collected masks. The last gear of the data engine is fully automatic mask creation, allowing our dataset to scale.

Our final dataset includes more than 1.1 billion segmentation masks collected on about 11 million licensed and privacy-preserving images. SA-1B has 400x more masks than any existing segmentation dataset, and as verified by human evaluation studies, the masks are of high quality and diversity, and in some cases even comparable in quality to masks from the previous much smaller, fully manually annotated datasets.

![](https://scontent.fhnl3-2.fna.fbcdn.net/v/t39.2365-6/338490494_577019134187999_95483266747832988_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=LVSVBgk2VEIQ7kNvwHbV6kR&_nc_oc=AdmCGmGp8xz1WDGQFOLEv_fpbFMfoSsl9nR-TQOEAtQUKVvTHzBkOfv1zgJwR-5GjNo&_nc_zt=14&_nc_ht=scontent.fhnl3-2.fna&_nc_gid=igYKb9UNvhaXv54Qh1ON8g&oh=00_Aft5luL9-ojtc4P2JZFq1TCvJhVNPjNjgCHMCTybhc7veA&oe=69A918BC)
![](https://scontent.fhnl3-2.fna.fbcdn.net/v/t39.2365-6/338713754_989652268682274_1644116157216484057_n.png?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=--Pq8wb-4ZIQ7kNvwFNYOc4&_nc_oc=AdnrZMh3HiBf8eFAtKh6j9bjWzVvGQ65vusjVTo9uqNBragbmlbUdGT5v_K5WzCGkOQ&_nc_zt=14&_nc_ht=scontent.fhnl3-2.fna&_nc_gid=igYKb9UNvhaXv54Qh1ON8g&oh=00_Aft5fqzxJ7B2pxZPFQvB1YZJsNAonZ_vNETeCk8vBxHoHw&oe=69A9093F)

Segment Anything’s capabilities are the result of training on millions of images and masks collected using a data engine. The result is a dataset of more than 1 billion segmentation masks – 400x larger than any prior segmentation dataset.

Images for SA-1B were sourced via a photo provider from multiple countries that span a diverse set of geographic regions and income levels. While we recognize that certain geographic regions are still underrepresented, SA-1B has a larger number of images and overall better representation across all regions than previous segmentation datasets. Moreover, we analyzed potential biases of our model across the perceived gender presentation, perceived skin tone and perceived age range of people, and we found that SAM performs similarly across different groups. Together, we hope this will make our work more equitable for use in real-world use cases.

While SA-1B made our research possible, it can also enable other researchers to train foundation models for image segmentation. We further hope that this data can become a basis for new datasets with additional annotations, such as a text description associated with each mask.

## What lies ahead

In the future, SAM could be used to identify everyday items via AR glasses that could prompt users with reminders and instructions.

SAM has the potential to impact a wide range of domains — perhaps one day helping farmers in the agricultural sector or assisting biologists in their research.

By sharing our research and dataset, we hope to further accelerate research into segmentation and more general image and video understanding. Our promptable segmentation model can perform a segmentation task by acting as a component in a larger system. Composition is a powerful tool that allows a single model to be used in extensible ways, potentially to accomplish tasks unknown at the time of model design. We anticipate that composable system design, enabled by techniques such as prompt engineering, will enable a wider variety of applications than systems trained specifically for a fixed set of tasks, and that SAM can become a powerful component in domains such as AR/VR, content creation, scientific domains, and more general AI systems. And as we look ahead, we see tighter coupling between understanding images at the pixel level and higher-level semantic understanding of visual content, unlocking even more powerful AI systems.

[Try the Segment Anything demo](https://segment-anything.com/)
[Learn more about SA-1B](https://ai.facebook.com/datasets/segment-anything/)
[Download SAM](https://github.com/facebookresearch/segment-anything)
[Read the paper](https://arxiv.org/abs/2304.02643)