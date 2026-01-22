---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-22T16:15:27.488325+00:00'
exported_at: '2026-01-22T16:15:30.715010+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/rtx-ai-garage-comfyui-tutorial
structured_data:
  about: []
  author: ''
  description: Learn how to run advanced image and video generation locally with ComfyUI
    and LTX-2 on RTX PCs.
  headline: How to Get Started With Visual Generative AI on NVIDIA RTX PCs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/rtx-ai-garage-comfyui-tutorial
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How to Get Started With Visual Generative AI on NVIDIA RTX PCs
updated_at: '2026-01-22T16:15:27.488325+00:00'
url_hash: 9feb5ee29792e9910f3e37df530061616214025e
---

AI-powered content generation is now embedded in everyday tools like Adobe and Canva, with a slew of agencies and studios incorporating the technology into their workflows. Image models now deliver photorealistic results consistently, video models can generate long and coherent clips, and both can follow creative directions.

Creators are increasingly running these workflows locally on PCs to keep assets under direct control, remove cloud service costs and eliminate the friction of iteration — making it easier to refine outputs at the pace real creative projects demand.

VIDEO

Since their inception, NVIDIA RTX PCs have been the system of choice for running creative AI due to their high performance — reducing iteration time — and the fact that users can run models on them for free, removing token anxiety.

With recent RTX optimizations and new open-weight models introduced at CES earlier this month, creatives can work faster, more efficiently and with far greater creative control.

## **How to Get Started**

Getting started with visual generative AI can feel complex and limiting. Online AI generators are easy to use but offer limited control.

Open source community tools like ComfyUI simplify setting up advanced creative workflows and are easy to install. They also provide an easy way to download the latest and greatest models, such as FLUX.2 and LTX-2, as well as top community workflows.

Here’s how to get started with visual generative AI locally on RTX PCs using ComfyUI and popular models:

1. Visit
   [comfy.org](https://comfy.org)
   to download and install ComfyUI for Windows.
2. Launch ComfyUI.
3. Create an initial image using the starter template:

![](https://blogs.nvidia.com/wp-content/uploads/2026/01/comfyui-template-image-960x777.png)

* + Click on the “Templates” button, then on “Getting Started” and choose “1.1 Starter – Text to Image.”
  + Connect the model “Node” to the “Save Image Node.” The nodes work in a pipeline to generate content using AI.
  + Press the blue “Run” button and watch the green “Node” highlight as the RTX-powered PC generates its first image.

Change the prompt and run it again to enter more deeply into the creative world of visual generative AI.

Read more below on how to dive into additional ComfyUI templates that use more advanced image and video models.

## **Model Sizes and GPUs**

As users get more familiar with ComfyUI and the models that support it, they’ll need to consider GPU VRAM capacity and whether a model will fit within it. Here are some examples for getting started, depending on GPU VRAM:

![](https://blogs.nvidia.com/wp-content/uploads/2026/01/gpu-vram-image-gen-video-3d-chart-comparison-960x189.png)


\*Use FP4 models with NVIDIA GeForce RTX 50 Series GPUs, and FP8 models with RTX 40 Series GPUs for best results. This lets models use less VRAM while providing more performance.

## **Generating Images**

![](https://blogs.nvidia.com/wp-content/uploads/2026/01/2026-01-21-image-gen-tiger-960x768.png)

To explore how to improve image generation quality using FLUX.2-Dev:

From the ComfyUI “Templates” section, click on “All Templates” and search for “FLUX.2 Dev Text to Image.” Select it, and ComfyUI will load the collection of connected nodes, or “Workflow.”

FLUX.2-Dev has model weights that will need to be downloaded.

Model weights are the “knowledge” inside an AI model — think of them like the synapses in a brain. When an image generation model like FLUX.2 was trained, it learned patterns from millions of images. Those patterns are stored as billions of numerical values called “weights.”

ComfyUI doesn’t come with these weights built in. Instead, it downloads them on demand from repositories like Hugging Face. These files are large (FLUX.2 can be >30GB depending on the version), which is why systems need enough storage and download time to grab them.

A dialog will appear to guide users through downloading the model weights. The weight files (filename.safetensors) are automatically saved to the correct ComfyUI folder on a user’s PC.

![](https://blogs.nvidia.com/wp-content/uploads/2026/01/2026-01-21-missing-models-screenshot-960x777.png)

**Saving Workflows:**

Now that the model weights are downloaded, the next step is to save this newly downloaded template as a “Workflow.”

Users can click on the top-left hamburger menu (three lines) and choose “Save.” The workflow is now saved in the user’s list of “Workflows” (press W to show or hide the window). Close the tab to exit the workflow without losing any work.

If the download dialog was accidentally closed before the model weights finished downloading:

* Press W to quickly open the “Workflows” window.
* Select the Workflow and ComfyUI will load it. This will also prompt for any missing model weights to download.
* ComfyUI is now ready to generate an image using FLUX.2-Dev.

**Prompt Tips for FLUX.2-Dev:**

* Start with clear, concrete descriptions of the subject, setting, style and mood — for example: “Cinematic closeup of a vintage race car in the rain, neon reflections on wet asphalt, high contrast, 35mm photography.” Short‑to‑medium length prompts  — a single, focused sentence or two — are usually easier to control than long, storylike prompts, especially when getting started.
* Add constraints to guide consistency and quality. Specify things like:
  + Framing (“wide shot” or “portrait”)
  + Detail level (“high detail, sharp focus”)
  + Realism (“photorealistic” or “stylized illustration”)
* If results are too busy, remove adjectives instead of adding more.
* Avoid negative prompting — stick to prompting what’s desired.

Learn more about FLUX.2 prompting in
[this guide](https://docs.bfl.ai/guides/prompting_guide_flux2)
from Black Forest Labs.

**Save Locations on Disk:**

Once done refining the image, right click on “Save Image Node” to open the image in a browser, or save it in a new location.

ComfyUI’s default output folders are typically the following, based on the application type and OS:

* Windows (Standalone/Portable Version): The folder is usually found in C:\ComfyUI\output or a similar path within where the program was unzipped.
* Windows (Desktop Application): The path is usually located within the AppData directory, like: C:\Users\%username%\AppData\Local\Programs\@comfyorgcomfyui-electron\resources\ComfyUI\output
* Linux: The installation location defaults to ~/.config/ComfyUI.

## **Prompting Videos**

Explore how to improve video generation quality, using the new LTX-2 model as an example:

VIDEO

Lightrick’s LTX‑2 is an advanced audio-video model designed for controllable, storyboard-style video generation in ComfyUI. Once the LTX‑2 Image to Video Template and model weights are downloaded, start by treating the prompt like a short shot description, rather than a full movie script.

Unlike the first two Templates, LTX‑2 Image to Video combines an image and a text prompt to generate video.

Users can take one of the images generated in FLUX.2-Dev and add a text prompt to give it life.

**Prompt Tips for LTX‑2:**

For best results in ComfyUI, write a single flowing paragraph in the present tense or use a simple, script‑style format with scene headings (sluglines), action, character names and dialogue. Aim for four to six descriptive sentences that cover all the key aspects:

* Establish the shot and scene (wide/medium/closeup, lighting, color, textures, atmosphere).
* Describe the action as a clear sequence, define characters with visible traits and body language, and specify camera moves.
* Lastly, add audio, such as ambient sound, music and dialogue, using quotation marks.
* Match the level of detail to the shot scale. For example, closeups need more precise character and texture detail than wide shots. Be clear on how the camera relates to the subject, not just where it moves.

Additional details to consider adding to prompts:

* **Camera movement language:**
  Specify directions like “slow dolly in,” “handheld tracking,” “over‑the‑shoulder shot,” “pans across,” “tilts upward,” “pushes in,” “pulls back” or “static frame.”
* **Shot types:**
  Specify wide, medium or close‑ups with thoughtful lighting, shallow depth of field and natural motion.
* **Pacing:**
  Direct for slow motion, time‑lapses, lingering shots, continuous shots, freeze frames or seamless transitions that shape rhythm and tone.
* **Atmosphere:**
  Add details like fog, mist, rain, golden hour light, reflections and rich surface textures that ground the scene.
* **Style:**
  Early in the prompt, specify styles like painterly, film noir, analog film, stop‑motion, pixelated edges, fashion editorial or surreal.
* **Lighting**
  : Direct backlighting, specific color palettes, soft rim light, lens flares or other lighting details using specific language.
* **Emotions**
  : Focus on prompting for single‑subject performances with clear facial expressions and small gestures.
* **Voice and audio**
  : Prompt characters to speak or sing in different languages, supported by clear ambient sound descriptions.

**Optimizing VRAM Usage and Image Quality**

As a frontier model, LTX-2 uses significant amounts of video memory (VRAM) to deliver quality results. Memory use goes up as resolution, frame rates, length or steps increase.

ComfyUI and NVIDIA have collaborated to optimize a weight streaming feature that allows users to offload parts of the workflow to system memory if their GPU runs out of VRAM — but this comes at a cost in performance.

Depending on the GPU and use case, users may want to constrain these factors to ensure reasonable generation times.

LTX-2 is an incredibly advanced model — but as with any model, tweaking the settings has a big impact on quality.

Learn more about optimizing LTX-2 usage with RTX GPUs in the
[Quick Start Guide for LTX-2 In ComfyUI](https://www.nvidia.com/en-us/geforce/news/rtx-ai-video-generation-guide/)
.

## **Building a Custom Workflow With FLUX.2-Dev and LTX-2**

Users can simplify the process of hopping between ComfyUI Workflows with FLUX.2-Dev to generate an image, finding it on disk and adding it as an image prompt to the LTX-2 Image to Video Workflow by combining the models into a new workflow:

* Open the saved FLUX.2-Dev Text to Image Workflow.
* Ctrl+left mouse click the FLUX.2-Dev Text to Image node.
* In the LTX-2 Image to Video Workflow, paste the node using Ctrl+V.
* Simply hover over the FLUX.2-Dev Text to Image node IMAGE dot, left click and drag to the Resize Image/Mask Input dot. A blue connector will appear.

Save with a new name, and text prompt for image and video in one workflow.

## **Advanced 3D Generation**

Beyond generating images with FLUX.2 and videos with LTX‑2, the next step is adding 3D guidance. The
[NVIDIA Blueprint for 3D-guided generative AI](https://github.com/NVIDIA-AI-Blueprints/3d-guided-genai-rtx)
shows how to use 3D scenes and assets to drive more controllable, production-style image and video pipelines on RTX PCs — with ready-made workflows users can inspect, tweak and extend.

Creators can show off their work, connect with other users and find help on the
[Stable Diffusion subreddit](https://www.reddit.com/r/StableDiffusion/)
and
[ComfyUI Discord](https://discord.com/invite/comfyorg)
.

## **#ICYMI — The Latest Advancements in NVIDIA RTX AI PCs**

💻
**NVIDIA @ CES 2026**

[CES announcements](https://blogs.nvidia.com/blog/rtx-ai-garage-ces-2026-open-models-video-generation/)
included 4K AI video generation acceleration on PCs with LTX-2 and ComfyUI upgrades. Plus, major RTX accelerations across ComfyUI, LTX-2, Llama.cpp, Ollama, Hyperlink and more unlock video, image and text generation use cases on AI PCs.

**📝 Black Forest Labs FLUX 2 Variants**

FLUX.2 [klein] is a set of compact, ultrafast models that support both image generation and editing, delivering state-of-the-art image quality. The models are accelerated by NVFP4 and NVFP8, boosting speed by up to 2.5x and enabling them to run performantly across a wide range of RTX GPUs.

**✨Project**
**G-Assist Update**

With a new “Reasoning Mode” enabled by default, Project G-Assist gains an accuracy and intelligence boost, as well as the ability to action multiple commands at once. G-Assist can now control settings on G-SYNC monitors, CORSAIR peripherals and CORSAIR PC components through iCUE — covering lighting, profiles, performance and cooling.

Support is also coming soon to Elgato Stream Decks, bringing G-Assist closer to a unified AI interface for tuning and controlling nearly any system. For G-Assist plug-in devs, a new Cursor-based plug-in builder accelerates development using Cursor’s agentic coding environment.

*Plug in to NVIDIA AI PC on*
[*Facebook*](https://www.facebook.com/NVIDIA.AI.PC/)
*,*
[*Instagram*](https://www.instagram.com/nvidia.ai.pc/)
*,*
[*TikTok*](https://www.tiktok.com/@nvidia_ai_pc)
*and*
[*X*](https://x.com/NVIDIA_AI_PC)
*— and stay informed by subscribing to the*
[*RTX AI PC newsletter*](https://www.nvidia.com/en-us/ai-on-rtx/?modal=subscribe-ai)
*.*

*Follow NVIDIA Workstation on*
[*LinkedIn*](https://www.linkedin.com/showcase/3761136/)
*and*
[*X*](https://x.com/NVIDIAworkstatn)
*.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*