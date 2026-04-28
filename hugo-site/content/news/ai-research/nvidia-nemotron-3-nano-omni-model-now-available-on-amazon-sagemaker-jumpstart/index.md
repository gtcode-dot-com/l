---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-28T18:15:34.649646+00:00'
exported_at: '2026-04-28T18:15:37.197745+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-nano-omni-model-now-available-on-amazon-sagemaker-jumpstart
structured_data:
  about: []
  author: ''
  description: Today, we are excited to announce the day zero availability of NVIDIA
    Nemotron 3 Nano Omni on Amazon SageMaker JumpStart. In this post, we walk through
    the model architecture and key capabilities of Nemotron 3 Nano Omni, explore the
    enterprise use cases it unlocks, and show you how to deploy and run inference
    using...
  headline: NVIDIA Nemotron 3 Nano Omni model now available on Amazon SageMaker JumpStart
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-nano-omni-model-now-available-on-amazon-sagemaker-jumpstart
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Nemotron 3 Nano Omni model now available on Amazon SageMaker JumpStart
updated_at: '2026-04-28T18:15:34.649646+00:00'
url_hash: fc16856ee8dd2f1f6e031303a1636c35471eea1e
---

Today, we are excited to announce the day zero availability of NVIDIA Nemotron 3 Nano Omni on Amazon SageMaker JumpStart. This multimodal model from NVIDIA combines video, audio, image, and text understanding into a single, efficient architecture, enabling enterprise customers to build intelligent applications that can see, hear, and reason across modalities in one inference pass.

In this post, we walk through the model architecture and key capabilities of Nemotron 3 Nano Omni, explore the enterprise use cases it unlocks, and show you how to deploy and run inference using Amazon SageMaker JumpStart.

## Overview of NVIDIA Nemotron 3 Nano Omni

NVIDIA Nemotron 3 Nano Omni is an open, multimodal large language model with 30 billion total parameters and 3 billion active parameters (30B A3B). It is built on a Mamba2 Transformer Hybrid Mixture of Experts (MoE) architecture, combining three core components:

1. **Nemotron 3 Nano LLM**
   as the language backbone
2. **CRADIO v4-H**
   as the vision encoder for image and video understanding
3. **Parakeet**
   as the speech encoder for audio transcription and comprehension

This unified architecture processes video, audio, images, and text as input and generates text as output. It supports a 131K token context length, chain of thought reasoning, tool calling, JSON output, and word level timestamps for transcription tasks. The model is available in FP8 precision on SageMaker JumpStart, delivering an optimal balance of accuracy and efficiency for enterprise workloads. It is licensed under the NVIDIA Open Model Agreement for commercial use.Enterprise agent workflows are inherently multimodal. Agents must interpret screens, documents, audio, video, and text, often within the same reasoning loop. Today, most agentic systems stitch together separate models for vision, speech, and language. This approach increases latency through repeated inference passes, complicates orchestration and error handling, fragments context across modalities, and amplifies cost and failure modes over time.

Nemotron 3 Nano Omni solves this by functioning as the multimodal perception and context sub-agent in a system of agents. It provides the agent system with eyes and ears: reading screens, interpreting documents, transcribing speech, and analyzing video, all while maintaining a converged multimodal context across reasoning loops.Nano Omni understands screens, documents, audio, and video in a single reasoning loop. This replaces fragmented model stacks and simplifies agent workflow design significantly. For anyone building agentic architectures, this collapses inference hops, orchestration logic, and cross-model synchronization overhead into a single model call.The model accepts the following input types:

|  |  |  |
| --- | --- | --- |
| **Input Type** | **Supported Formats** | **Constraints** |
| Video | mp4 | Up to 2 minutes, up to 256 frames |
| Audio | wav, mp3 | Up to 1 hour, 8kHz+ sampling rate |
| Image | JPEG, PNG (RGB) | Standard resolution |
| Text | String | Up to 131K context |

## Enterprise use cases

The multimodal capabilities of Nemotron 3 Nano Omni make it a powerful, flexible model choice for enterprise use cases.

### Computer use agents

Nemotron 3 Nano Omni powers the perception loop for agents navigating graphical user interfaces. It reads screens, understands UI state over time, and validates outcomes, while execution agents handle the actions. This collapses vision and reasoning into a single loop, eliminating the need for split perception pipelines. Practical applications include incident management dashboards, agentic search, browser automation, and email workflow agents.

### Document intelligence

The model interprets documents, charts, tables, screenshots, and mixed media inputs, enabling agents to reason across visual structure and text content coherently. This is critical for enterprise analysis and compliance workflows involving contracts, statements of work, financial documents, and scientific literature.

### Audio and video understanding agents

For customer service, research, and monitoring workflows, Nemotron 3 Nano Omni maintains continuous audio and video context. It ties together what was said, shown, and documented into a single reasoning stream instead of disconnected summaries. This enables applications such as meeting recording analysis, media and entertainment asset management, drive-thru order verification, and customer service video review (for example, verifying package delivery at a given address via OCR).

## Getting started with SageMaker JumpStart

You can deploy Nemotron 3 Nano Omni through Amazon SageMaker JumpStart in a few steps. SageMaker JumpStart provides one-click deployment of foundation models with optimized inference containers, removing the need to manage infrastructure, configure serving frameworks, or handle model artifact downloads.

### Prerequisites

Before you begin, make sure you have:

### Deploy using SageMaker Studio

1. Open Amazon SageMaker Studio
2. In the left navigation pane, choose
   **JumpStart**
3. Search for
   **Nemotron 3 Nano Omni**
4. Select the model card and choose
   **Deploy**
5. Configure your instance type and deployment settings
6. Choose
   **Deploy**
   to create the endpoint

### Deploy using the SageMaker Python SDK

You can also deploy programmatically using the SageMaker Python SDK:

```
from sagemaker.jumpstart.model import JumpStartModel

model = JumpStartModel(
  model_id="huggingface-vlm-nvidia-nemotron3-nano-omni-30ba3b-reasoning-fp8",
  role="<your_sagemaker_execution_role>",
)

predictor = model.deploy(
  accept_eula=True,
)
```

### Run inference: Image understanding

Once deployed, you can send multimodal requests to the endpoint. The following example shows how to send an image understanding request:

```
import base64

def encode_image(image_path):
  with open(image_path, "rb") as f:
    return base64.b64encode(f.read()).decode("utf-8")

image_b64 = encode_image("example.jpg")

payload = {
  "messages": [{
    "role": "user",
    "content": [
      {"type": "text", "text": "Describe this image in detail."},
      {"type": "image_url",
       "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
    ],
  }],
  "max_tokens": 1024,
  "temperature": 0.2,
}

response = predictor.predict(payload)
print(response["choices"][0]["message"]["content"])
```

### Run inference: Video understanding with reasoning

```
import base64

def encode_video(video_path):
  with open(video_path, "rb") as f:
    return base64.b64encode(f.read()).decode("utf-8")

video_b64 = encode_video("meeting_recording.mp4")

payload = {
  "messages": [{
    "role": "user",
    "content": [
      {"type": "video_url",
       "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}},
      {"type": "text",
       "text": "Summarize the key discussion points."},
    ],
  }],
  "max_tokens": 20480,
  "temperature": 0.6,
  "top_p": 0.95,
}

response = predictor.predict(payload)
print(response["choices"][0]["message"]["content"])
```

### Run inference: Audio transcription

```
import base64

def encode_audio(audio_path):
  with open(audio_path, "rb") as f:
    return base64.b64encode(f.read()).decode("utf-8")

audio_b64 = encode_audio("customer_call.wav")

payload = {
  "messages": [{
    "role": "user",
    "content": [
      {"type": "audio_url",
       "audio_url": {"url": f"data:audio/wav;base64,{audio_b64}"}},
      {"type": "text",
       "text": "Transcribe this audio and identify key action items."},
    ],
  }],
  "max_tokens": 1024,
  "temperature": 0.2,
}

response = predictor.predict(payload)
print(response["choices"][0]["message"]["content"])
```

### Recommended inference parameters

The following table contains the recommended hyperparameter values for Omni inference requests. The values change depending on the inference mode.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mode** | **Temperature** | **top\_p** | **max\_tokens** | **Use Case** |
| Thinking | 0.6 | 0.95 | 20480 | Complex reasoning |
| Instruct | 0.2 | N/A | 1024 | General tasks, ASR |

For tasks that involve reasoning and complex understanding, we recommend enabling thinking mode. For transcription and straightforward tasks, instruct mode (with thinking disabled) provides faster responses.

## Clean up

To avoid incurring unnecessary charges, delete the SageMaker endpoint when you are done:

```
predictor.delete_endpoint()
```

## Conclusion

NVIDIA Nemotron 3 Nano Omni brings a new level of multimodal intelligence to Amazon SageMaker JumpStart. By unifying video, audio, image, and text understanding into a single efficient model, it simplifies the development of enterprise agentic applications while delivering leading accuracy and up to 9x higher throughput compared to alternative open omni models.

Whether you are building computer use agents that navigate GUIs, document intelligence pipelines for compliance workflows, or audio and video analysis systems for customer service, Nemotron 3 Nano Omni provides the perception layer your agents need in a single model call.

Get started today by deploying Nemotron 3 Nano Omni from Amazon SageMaker JumpStart. For more information about the model, visit the
[NVIDIA Nemotron model page](https://huggingface.co/docs/transformers/en/model_doc/nemotron)
on Hugging Face.

---

## About the authors

Dan Ferguson is a Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.

**Malav Shastri**
is a Software Development Engineer at AWS, where he works on the Amazon SageMaker JumpStart and Amazon Bedrock teams. His role focuses on enabling customers to take advantage of state-of-the-art open source and proprietary foundation models and traditional machine learning algorithms. Malav holds a Master’s degree in Computer Science.

**Vivek Gangasani**
is a Worldwide Leader for Solutions Architecture, SageMaker Inference. He leads Solution Architecture, Technical Go-to-Market (GTM) and Outbound Product strategy for SageMaker Inference. He also helps enterprises and startups deploy and optimize a GenAI models and build AI workflows with SageMaker and GPUs. Currently, he is focused on developing strategies and content for optimizing inference performance and use-cases such as Agentic workflows, RAG etc. In his free time, Vivek enjoys hiking, watching movies, and trying different cuisines.