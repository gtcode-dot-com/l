---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T06:41:23.991647+00:00'
exported_at: '2026-02-13T06:41:31.736312+00:00'
feed: http://feeds.feedburner.com/blogspot/gJZg
language: en
source_url: http://blog.research.google/2024/03/melon-reconstructing-3d-objects-from.html
structured_data:
  about: []
  author: ''
  description: 'MELON: Reconstructing 3D objects from images with unknown poses'
  headline: 'MELON: Reconstructing 3D objects from images with unknown poses'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://blog.research.google/2024/03/melon-reconstructing-3d-objects-from.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'MELON: Reconstructing 3D objects from images with unknown poses'
updated_at: '2026-02-13T06:41:23.991647+00:00'
url_hash: 81999604ae898a68e0b3c3039b18a2b95f933ae3
---

We leverage two key techniques to aid convergence of this ill-posed problem. The first is a very lightweight, dynamically trained
[convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
(CNN) encoder that regresses camera poses from training images. We pass a downscaled training image to a four layer CNN that infers the camera pose. This CNN is initialized from noise and requires no pre-training. Its capacity is so small that it forces similar looking images to similar poses, providing an implicit regularization greatly aiding convergence.

The second technique is a
*modulo loss*
that simultaneously considers pseudo symmetries of an object. We render the object from a fixed set of viewpoints for each training image, backpropagating the loss only through the view that best fits the training image. This effectively considers the plausibility of multiple views for each image. In practice, we find
*N*
=2 views (viewing an object from the other side) is all that’s required in most cases, but sometimes get better results with
*N*
=4 for square objects.

These two techniques are integrated into standard NeRF training, except that instead of fixed camera poses, poses are inferred by the CNN and duplicated by the modulo loss. Photometric gradients back-propagate through the best-fitting cameras into the CNN. We observe that cameras generally converge quickly to globally optimal poses (see animation below). After training of the neural field, MELON can synthesize novel views using standard NeRF rendering methods.

We simplify the problem by using the
[NeRF-Synthetic](https://github.com/bmild/nerf)
dataset, a popular benchmark for NeRF research and common in the pose-inference literature. This synthetic dataset has cameras at precisely fixed distances and a consistent “up” orientation, requiring us to infer only the
[polar coordinates](https://en.wikipedia.org/wiki/Spherical_coordinate_system)
of the camera. This is the same as an object at the center of a globe with a camera always pointing at it, moving along the surface. We then only need the latitude and longitude (2 degrees of freedom) to specify the camera pose.