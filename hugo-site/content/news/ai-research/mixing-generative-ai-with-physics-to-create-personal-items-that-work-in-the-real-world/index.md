---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-26T06:08:08.814776+00:00'
exported_at: '2026-02-26T06:08:11.312140+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/mixing-ai-with-physics-to-create-personal-items-0225
structured_data:
  about: []
  author: ''
  description: A system known as PhysiOpt complements generative AI models with physics
    simulations to create 3D models of personal items. Users can prompt the system
    using text or images, and get a blueprint that works in the real world when fabricated.
  headline: Mixing generative AI with physics to create personal items that work in
    the real world
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/mixing-ai-with-physics-to-create-personal-items-0225
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Mixing generative AI with physics to create personal items that work in the
  real world
updated_at: '2026-02-26T06:08:08.814776+00:00'
url_hash: e316f174133c9ad4fdc4541efe4705cc53337473
---

Have you ever had an idea for something that looked cool, but wouldn’t work well in practice? When it comes to designing things like decor and personal accessories, generative artificial intelligence (genAI) models can relate. They can produce creative and elaborate 3D designs, but when you try to fabricate such blueprints into real-world objects, they usually don’t sustain everyday use.


The underlying problem is that genAI models often lack an understanding of physics. While tools like Microsoft’s
[TRELLIS](https://microsoft.github.io/TRELLIS.2/)
system can create a 3D model from a text prompt or image, its design for a chair, for example, may be unstable, or have disconnected parts. The model doesn’t fully understand what your intended object is designed to do, so even if your seat can be 3D printed, it would likely fall apart under the force of someone sitting down.

In an attempt to make these designs work in the real world, researchers at MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) are giving generative AI models a reality check. Their “PhysiOpt” system augments these tools with physics simulations, making blueprints for personal items such as cups, keyholders, and bookends work as intended when they’re 3D printed. It rapidly tests if the structure of your 3D model is viable, gently modifying smaller shapes while ensuring the overall appearance and function of the design is preserved.

You can simply type what you want to create and what it’ll be used for into PhysiOpt, or upload an image to the system’s user interface, and in roughly half a minute, you’ll get a realistic 3D object to fabricate. For example, CSAIL researchers prompted it to generate a “flamingo-shaped glass for drinking,” which they 3D printed into a drinking glass with a handle and base resembling the tropical bird’s leg. As the design was generated, PhysiOpt made tiny refinements to ensure the design was structurally sound.


“PhysiOpt combines GenAI and physically-based shape optimization, helping virtually anyone generate the designs they want for unique accessories and decorations,” says MIT electrical engineering and computer science (EECS) PhD student and CSAIL researcher Xiao Sean Zhan SM ’25, who is a co-lead author on a
[paper](https://physiopt.github.io/)
presenting the work. “It’s an automatic system that allows you to make the shape physically manufacturable, given some constraints. PhysiOpt can iterate on its creations as often as you’d like, without any extra training.”

This approach enables you to create a “smart design,” where the AI generator crafts your item based on users’ specifications, while considering functionality. You can plug in your favorite 3D generative AI model, and after typing out what you want to generate, you specify how much force or weight the object should handle. It’s a neat way to simulate real-world use, such as predicting whether a hook will be strong enough to hold up your coat. Users also specify what materials they’ll fabricate the item with (such as plastics or wood), and how it’s supported — for instance, a cup stands on the ground, whereas a bookend leans against a collection of books.

Given the specifics, PhysiOpt begins to iteratively optimize the object. Under the hood, it runs a physics simulation called a “finite element analysis” to stress test the design. This comprehensive scan provides a heat map over your 3D model, which indicates where your blueprint isn’t well-supported. If you were generating, say, a birdhouse, you may find that the support beams under the house were colored bright red, meaning the house will crumble if it’s not reinforced.

PhysiOpt can create even bolder pieces. Researchers saw this versatility firsthand when they fabricated a steampunk (a style that blends Victorian and futuristic aesthetics) keyholder featuring intricate, robotic-looking hooks, and a “giraffe table” with a flat back that you can place items on. But how did it know what “steampunk” is, or even how such a unique piece of furniture should look?


Remarkably, the answer isn’t extensive training — at least, not from the researchers. Instead, PhysiOpt uses a pre-trained model that’s already seen thousands of shapes and objects. “Existing systems often need lots of additional training to have a semantic understanding of what you want to see,” adds co-lead author Clément Jambon, who is also an MIT EECS PhD student and CSAIL researcher. “But we use a model with that feel for what you want to create already baked in, so PhysiOpt is training-free.”

By working with a pre-trained model, PhysiOpt can use “shape priors,” or knowledge of how shapes should look based on earlier training, to generate what users want to see. It’s sort of like an artist recreating the style of a famous painter. Their expertise is rooted in closely studying a variety of artistic approaches, so they’ll likely be able to mirror that particular aesthetic. Likewise, a pre-trained model’s familiarity with shapes helps it generate 3D models.

CSAIL researchers observed that PhysiOpt’s visual know-how helped it create 3D models more efficiently than “
[DiffIPC](https://arxiv.org/abs/2205.13643)
,” a comparable method that simulates and optimizes shapes. When both approaches were tasked with generating 3D designs for items like chairs, CSAIL’s system was nearly 10 times faster per iteration, while creating more realistic objects.

PhysiOpt presents a potential bridge between ideas and real-world personal items. What you may think is a great idea for a coffee mug, for instance, could soon make the jump from your computer screen to your desk. And while PhysiOpt already does the stress-testing for designers, it may soon be able to predict constraints such as loads and boundaries, instead of users needing to provide those details. This more autonomous, common-sense approach could be made possible by incorporating vision language models, which combine an understanding of human language with computer vision.

What’s more, Zhan and Jambon intend to remove the artifacts, or random fragments that occasionally appear in PhysiOpt’s 3D models, by making the system even more physics-aware. The MIT scientists are also considering how they can model more complex constraints for various fabrication techniques, such as minimizing overhanging components for 3D printing.


Zhan and Jambon wrote their paper with MIT-IBM Watson AI Lab Principal Research Scientist Kenney Ng ’89, SM ’90, PhD ’00 and two CSAIL colleagues: undergraduate researcher Evan Thompson and Assistant Professor Mina Konaković Luković, who is a principal investigator at the lab.

The researchers’ work was supported, in part, by the MIT-IBM Watson AI Laboratory and the Wistron Corp. They presented it in December at the Association for Computing Machinery’s SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia.