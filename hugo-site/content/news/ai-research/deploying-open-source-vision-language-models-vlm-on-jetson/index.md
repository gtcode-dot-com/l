---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T03:25:15.609145+00:00'
exported_at: '2026-03-03T03:25:19.382646+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/cosmos-on-jetson
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: Deploying Open Source Vision Language Models (VLM) on Jetson
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/cosmos-on-jetson
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Deploying Open Source Vision Language Models (VLM) on Jetson
updated_at: '2026-03-03T03:25:15.609145+00:00'
url_hash: 328ac70aed76788dbf6102d13722ea7596d612ab
---

# Deploying Open Source Vision Language Models (VLM) on Jetson

Vision-Language Models (VLMs) mark a significant leap in AI by blending visual perception with semantic reasoning. Moving beyond traditional models constrained by fixed labels, VLMs utilize a joint embedding space to interpret and discuss complex, open-ended environments using natural language.

The rapid evolution of reasoning accuracy and efficiency has made these models ideal for edge devices. The
[NVIDIA Jetson family](https://marketplace.nvidia.com/en-us/enterprise/robotics-edge/?limit=15)
, ranging from the high-performance AGX Thor and AGX Orin to the compact Orin Nano Super is purpose-built to drive accelerated applications for physical AI and robotics, providing the optimized runtime necessary for leading
[open source models](https://www.jetson-ai-lab.com/models/)
.

In this tutorial, we will demonstrate how to deploy the
[NVIDIA Cosmos Reason 2B](https://build.nvidia.com/nvidia/cosmos-reason2-2b)
model across the Jetson lineup using the
[vLLM](https://vllm.ai/)
framework. We will also guide you through connecting this model to the
[Live VLM WebUI](https://github.com/NVIDIA-AI-IOT/live-vlm-webui)
, enabling a real-time, webcam-based interface for interactive physical AI.

[![robot_pick_place](https://cdn-uploads.huggingface.co/production/uploads/658e083904cd2b7fd5f530d6/lrsP6RhYbwj0hBeuLjV_k.png)](https://cdn-uploads.huggingface.co/production/uploads/658e083904cd2b7fd5f530d6/lrsP6RhYbwj0hBeuLjV_k.png)

## Prerequisites

**Supported Devices:**

* Jetson AGX Thor Developer Kit
* Jetson AGX Orin (64GB / 32GB)
* Jetson Orin Super Nano

**JetPack Version:**

* JetPack 6 (L4T r36.x) — for Orin devices
* JetPack 7 (L4T r38.x) — for Thor

**Storage:**
NVMe SSD
**required**

* ~5 GB for the FP8 model weights
* ~8 GB for the vLLM container image

**Accounts:**

* Create
  [NVIDIA NGC](https://ngc.nvidia.com/)
  account(free) to download both the model and vLLM contanier

---

## Overview

|  | Jetson AGX Thor | Jetson AGX Orin | Orin Super Nano |
| --- | --- | --- | --- |
| **vLLM Container** | `nvcr.io/nvidia/vllm:26.01-py3` | `ghcr.io/nvidia-ai-iot/vllm:r36.4-tegra-aarch64-cu126-22.04` | `ghcr.io/nvidia-ai-iot/vllm:r36.4-tegra-aarch64-cu126-22.04` |
| **Model** | FP8 via NGC (volume mount) | FP8 via NGC (volume mount) | FP8 via NGC (volume mount) |
| **Max Model Length** | 8192 tokens | 8192 tokens | 256 tokens (memory-constrained) |
| **GPU Memory Util** | 0.8 | 0.8 | 0.65 |

The workflow is the same for both devices:

1. **Download**
   the FP8 model checkpoint via NGC CLI
2. **Pull**
   the vLLM Docker image for your device
3. **Launch**
   the container with the model mounted as a volume
4. **Connect**
   Live VLM WebUI to the vLLM endpoint

---

## Step 1: Install the NGC CLI

The NGC CLI lets you download model checkpoints from the
[NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/?tab=model)
.

### Download and install

```
mkdir -p ~/Projects/CosmosReason
cd ~/Projects/CosmosReason

# Download the NGC CLI for ARM64
# Get the latest installer URL from: https://org.ngc.nvidia.com/setup/installers/cli
wget -O ngccli_arm64.zip https://api.ngc.nvidia.com/v2/resources/nvidia/ngc-apps/ngc_cli/versions/4.13.0/files/ngccli_arm64.zip
unzip ngccli_arm64.zip
chmod u+x ngc-cli/ngc

# Add to PATH
export PATH="$PATH:$(pwd)/ngc-cli"
```

### Configure the CLI

```
ngc config set
```

You will be prompted for:

* **API Key**
  — generate one at
  [NGC API Key setup](https://org.ngc.nvidia.com/setup/api-key)
* **CLI output format**
  — choose
  `json`
  or
  `ascii`
* **org**
  — press Enter to accept the default

---

## Step 2: Download the Model

Download the
**FP8 quantized**
checkpoint. This is used on all Jetson devices:

```
cd ~/Projects/CosmosReason
ngc registry model download-version "nim/nvidia/cosmos-reason2-2b:1208-fp8-static-kv8"
```

This creates a directory called
`cosmos-reason2-2b_v1208-fp8-static-kv8/`
containing the model weights. Note the full path — you will mount it into the Docker container as a volume.

---

## Step 3: Pull the vLLM Docker Image

### For Jetson AGX Thor

```
docker pull nvcr.io/nvidia/vllm:26.01-py3
```

### For Jetson AGX Orin / Orin Super Nano

```
docker pull ghcr.io/nvidia-ai-iot/vllm:r36.4-tegra-aarch64-cu126-22.04
```

---

[
](https://cdn-uploads.huggingface.co/production/uploads/658e083904cd2b7fd5f530d6/dR3UVpD22I0vP1kzhdXQ1.mp4)

## Step 4: Serve Cosmos Reason 2B with vLLM

### Option A: Jetson AGX Thor

Thor has ample GPU memory and can run the model with a generous context length.

Set the path to your downloaded model and free cached memory on the host:

```
MODEL_PATH="$HOME/Projects/CosmosReason/cosmos-reason2-2b_v1208-fp8-static-kv8"
sudo sysctl -w vm.drop_caches=3
```

**Launch the container with the model mounted:**

```
docker run --rm -it \
  --runtime nvidia \
  --network host \
  --ipc host \
  -v "$MODEL_PATH:/models/cosmos-reason2-2b:ro" \
  -e NVIDIA_VISIBLE_DEVICES=all \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
  nvcr.io/nvidia/vllm:26.01-py3 \
  bash
```

**Inside the container, activate the environment and serve the model:**

```
vllm serve /models/cosmos-reason2-2b \
  --max-model-len 8192 \
  --media-io-kwargs '{"video": {"num_frames": -1}}' \
  --reasoning-parser qwen3 \
  --gpu-memory-utilization 0.8
```

**Note:**
The
`--reasoning-parser qwen3`
flag enables chain-of-thought reasoning extraction. The
`--media-io-kwargs`
flag configures video frame handling.

Wait until you see:

```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Option B: Jetson AGX Orin

AGX Orin has enough memory to run the model with the same generous parameters as Thor.

Set the path to your downloaded model and free cached memory on the host:

```
MODEL_PATH="$HOME/Projects/CosmosReason/cosmos-reason2-2b_v1208-fp8-static-kv8"
sudo sysctl -w vm.drop_caches=3
```

**1. Launch the container:**

```
docker run --rm -it \
  --runtime nvidia \
  --network host \
  -v "$MODEL_PATH:/models/cosmos-reason2-2b:ro" \
  -e NVIDIA_VISIBLE_DEVICES=all \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
  ghcr.io/nvidia-ai-iot/vllm:r36.4-tegra-aarch64-cu126-22.04 \
  bash
```

**2. Inside the container, activate the environment and serve:**

```
cd /opt/
source venv/bin/activate

vllm serve /models/cosmos-reason2-2b \
  --max-model-len 8192 \
  --media-io-kwargs '{"video": {"num_frames": -1}}' \
  --reasoning-parser qwen3 \
  --gpu-memory-utilization 0.8
```

Wait until you see:

```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Option C: Jetson Orin Super Nano (memory-constrained)

The Orin Super Nano has significantly less RAM, so we need aggressive memory optimization flags.

Set the path to your downloaded model and free cached memory on the host:

```
MODEL_PATH="$HOME/Projects/CosmosReason/cosmos-reason2-2b_v1208-fp8-static-kv8"
sudo sysctl -w vm.drop_caches=3
```

**1. Launch the container:**

```
docker run --rm -it \
  --runtime nvidia \
  --network host \
  -v "$MODEL_PATH:/models/cosmos-reason2-2b:ro" \
  -e NVIDIA_VISIBLE_DEVICES=all \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
  ghcr.io/nvidia-ai-iot/vllm:r36.4-tegra-aarch64-cu126-22.04 \
  bash
```

**2. Inside the container, activate the environment and serve:**

```
cd /opt/
source venv/bin/activate

vllm serve /models/cosmos-reason2-2b \
  --host 0.0.0.0 \
  --port 8000 \
  --trust-remote-code \
  --enforce-eager \
  --max-model-len 256 \
  --max-num-batched-tokens 256 \
  --gpu-memory-utilization 0.65 \
  --max-num-seqs 1 \
  --enable-chunked-prefill \
  --limit-mm-per-prompt '{"image":1,"video":1}' \
  --mm-processor-kwargs '{"num_frames":2,"max_pixels":150528}'
```

**Key flags explained (Orin Super Nano only):**

| Flag | Purpose |
| --- | --- |
| `--enforce-eager` | Disables CUDA graphs to save memory |
| `--max-model-len 256` | Limits context to fit in available memory |
| `--max-num-batched-tokens 256` | Matches the model length limit |
| `--gpu-memory-utilization 0.65` | Reserves headroom for system processes |
| `--max-num-seqs 1` | Single request at a time to minimize memory |
| `--enable-chunked-prefill` | Processes prefill in chunks for memory efficiency |
| `--limit-mm-per-prompt` | Limits to 1 image and 1 video per prompt |
| `--mm-processor-kwargs` | Reduces video frames and image resolution |
| `--VLLM_SKIP_WARMUP=true` | Skips warmup to save time and memory |

Wait until you see the server is ready:

```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Verify the server is running

From another terminal on the Jetson:

```
curl http://localhost:8000/v1/models
```

You should see the model listed in the response.

---

## Step 5: Test with a Quick API Call

Before connecting the WebUI, verify the model responds correctly:

```
curl -s http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "/models/cosmos-reason2-2b",
    "messages": [
      {
        "role": "user",
        "content": "What capabilities do you have?"
      }
    ],
    "max_tokens": 128
  }' | python3 -m json.tool
```

> **Tip:**
> The model name used in the API request must match what vLLM reports. Verify with
> `curl http://localhost:8000/v1/models`
> .

---

## Step 6: Connect to Live VLM WebUI

[Live VLM WebUI](https://github.com/NVIDIA-AI-IOT/live-vlm-webui)
provides a real-time webcam-to-VLM interface. With vLLM serving Cosmos Reason 2B, you can stream your webcam and get live AI analysis with reasoning.

### Install Live VLM WebUI

The easiest method is pip (Open another terminal):

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
cd ~/Projects/CosmosReason
uv venv .live-vlm --python 3.12
source .live-vlm/bin/activate
uv pip install live-vlm-webui
live-vlm-webui
```

Or use Docker:

```
git clone https://github.com/nvidia-ai-iot/live-vlm-webui.git
cd live-vlm-webui
./scripts/start_container.sh
```

### Configure the WebUI

1. Open
   **`https://localhost:8090`**
   in your browser
2. Accept the self-signed certificate (click
   **Advanced**
   →
   **Proceed**
   )
3. In the
   **VLM API Configuration**
   section on the left sidebar:
   * Set
     **API Base URL**
     to
     `http://localhost:8000/v1`
   * Click the
     **Refresh**
     button to detect the model
   * Select the Cosmos Reason 2B model from the dropdown
4. Select your camera and click
   **Start**

The WebUI will now stream your webcam frames to Cosmos Reason 2B and display the model’s analysis in real-time.

### Recommended WebUI settings for Orin

Since Orin runs with a shorter context length, adjust these settings in the WebUI:

* **Max Tokens**
  : Set to
  **100–150**
  (shorter responses complete faster)
* **Frame Processing Interval**
  : Set to
  **60+**
  (gives the model time between frames)

---

## Troubleshooting

### Out of memory on Orin

**Problem:**
vLLM crashes with CUDA out-of-memory errors.

**Solution:**

1. Free system memory before starting:

   ```
   sudo sysctl -w vm.drop_caches=3
   ```
2. Lower
   `--gpu-memory-utilization`
   (try
   `0.55`
   or
   `0.50`
   )
3. Reduce
   `--max-model-len`
   further (try
   `128`
   )
4. Make sure no other GPU-intensive processes are running

### Model not found in WebUI

**Problem:**
The model doesn’t appear in the Live VLM WebUI dropdown.

**Solution:**

1. Verify vLLM is running:
   `curl http://localhost:8000/v1/models`
2. Make sure the WebUI API Base URL is set to
   `http://localhost:8000/v1`
   (not
   `https`
   )
3. If vLLM and WebUI are in separate containers, use
   `http://<jetson-ip>:8000/v1`
   instead of
   `localhost`

### Slow inference on Orin

**Problem:**
Each response takes a very long time.

**Solution:**

* This is expected with the memory-constrained configuration. Cosmos Reason 2B FP8 on Orin prioritizes fitting in memory over speed
* Reduce
  `max_tokens`
  in the WebUI to get shorter, faster responses
* Increase the frame interval so the model isn’t constantly processing new frames

### vLLM fails to load model

**Problem:**
vLLM reports that the model path doesn’t exist or can’t be loaded.

**Solution:**

* Verify the NGC download completed successfully:
  `ls ~/Projects/CosmosReason/cosmos-reason2-2b_v1208-fp8-static-kv8/`
* Make sure the volume mount path is correct in your
  `docker run`
  command
* Check that the model directory is mounted as read-only (
  `:ro`
  ) and the path inside the container matches what you pass to
  `vllm serve`

---

## Summary

In this tutorial, we showcased how to deploy
**NVIDIA Cosmos Reason 2B**
model on Jetson family of devices using vLLM.

The combination of Cosmos Reason 2B’s chain-of-thought capabilities with Live VLM WebUI’s real-time streaming makes it ideal to prototype and evaluate vision AI applications at the edge.

---

[![Alt text](https://github.com/NVIDIA-AI-IOT/live-vlm-webui/raw/main/docs/images/chrome_app-running_light-theme.jpg)](https://github.com/NVIDIA-AI-IOT/live-vlm-webui/raw/main/docs/images/chrome_app-running_light-theme.jpg)

## Additional Resources