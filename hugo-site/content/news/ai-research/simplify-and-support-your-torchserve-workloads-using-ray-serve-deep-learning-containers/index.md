---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-30T02:43:31.071679+00:00'
exported_at: '2026-09-30T02:43:35.348256+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers
structured_data:
  about: []
  author: ''
  description: TorchServe is no longer maintained, leaving teams to own the entire
    GPU inference stack. The AWS Ray Serve Deep Learning Container is a supported,
    pre-tested container with the framework, GPU drivers, and serving layer already
    assembled. This post walks through deploying a vision-language model on Amazon
    EKS using t...
  headline: Simplify and support your TorchServe workloads using Ray Serve Deep Learning
    Containers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Simplify and support your TorchServe workloads using Ray Serve Deep Learning
  Containers
updated_at: '2026-09-30T02:43:31.071679+00:00'
url_hash: fd8c222d170bd9f70b1f928dc03e885b7ae4c867
---

[TorchServe](https://pytorch.org/serve/)
is no longer actively maintained. The official project notice states there are no planned updates, bug fixes, new features, or security patches, and that vulnerabilities might not be addressed. For teams that run model inference on TorchServe today, this means security patches stop and compatibility updates with newer versions of PyTorch and CUDA stop. Engineers are left owning the entire dependency chain themselves: choosing compatible versions across the GPU stack, patching vulnerabilities in every layer, and debugging subtle failures when any component drifts out of alignment. This is undifferentiated work that slows model delivery without adding value to the final product.

[AWS Deep Learning Containers](/ai/machine-learning/containers/)
(DLCs) have long addressed this kind of problem for training workloads. DLCs are pre-built, performance-optimized Docker images that bundle a framework, its dependencies, and the GPU stack into a tested, patched combination you can pull and use immediately. With the launch of the
[Ray Serve DLC](https://gallery.ecr.aws/deep-learning-containers/ray)
, that same approach now extends to inference. You get a container purpose-built for serving models behind an HTTP endpoint, maintained and tested by AWS, with the full inference stack already assembled.

This post introduces the Ray Serve DLC and walks through deploying a vision-language model on
[Amazon Elastic Kubernetes Service](/eks/)
(Amazon EKS) using this new image. We cover running a model with the Ray Serve DLC, running the serving application with
[Ray Serve](https://docs.ray.io/en/latest/serve/index.html)
, and deploying it on a single GPU node. The complete code is available in the
[accompanying repository](https://github.com/aws-samples/sample-aws-deep-learning-containers/tree/main/inference/ray-serve/ray-serve-single-node)
.

## Prerequisites

To follow along with this post, you need:

* An AWS account with billing enabled.
* Sufficient service quotas for
  `g5.xlarge`
  instances in your target Region.
* The AWS Command Line Interface (AWS CLI),
  `eksctl`
  , and
  `kubectl`
  installed and configured.

## Compose Ray Serve application

The Ray Serve DLC for CPU is built on the Amazon Linux 2023 base image. The GPU variant is built on the official NVIDIA Amazon Linux 2023 image, which includes both the OS layer and the CUDA runtime libraries. On top of this foundation, the DLC adds a deep learning framework (PyTorch), the Ray Serve serving layer with FastAPI and Uvicorn, and common utilities for vision, audio, and multimodal workloads. These utilities include FFmpeg compiled with NVIDIA hardware acceleration for video preprocessing. All components are validated and tested together before each release, so there’s no version drift between the CUDA runtime, the framework, and the serving layer. Security patches are applied at build time.

The Ray Serve DLC is published as separate images for Amazon EKS and Amazon Elastic Compute Cloud (Amazon EC2), and for Amazon SageMaker, each with a dedicated entrypoint suited to that environment’s serving contract. Both share the same underlying stack and dependencies. For the current list of available image tags, see the
[Ray DLC availale images page](https://aws.github.io/deep-learning-containers/reference/available_images/#ray-serve)
.

The DLC ships the common inference stack, so many models, including the Qwen3-VL model, run on it without a custom image. For models that need extra libraries, engineers can layer them on the same tested base.

In this post, we use the GPU version of the Ray Serve DLC to serve the
[Qwen3-VL-2B](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct)
vision-language model. The application is injected into the container through a ConfigMap, which keeps the deployment flexible so you can change the serving code without rebuilding the image. DLC already provides the GPU stack, PyTorch, Ray Serve, and Transformers.

## Write the serving application

With Ray Serve, a model endpoint is a Python class decorated with
[@serve.deployment](https://docs.ray.io/en/latest/serve/api/doc/ray.serve.deployment.html)
. You implement
`__call__`
to handle HTTP requests and call
`.bind()`
to register it. There’s no model archiver, no handler class hierarchy, and no properties configuration file. If you’re coming from TorchServe, this replaces the custom handler, the
`torch-model-archiver`
step, and the
`config.properties`
file.

The following example loads the
`Qwen3-VL-2B`
vision-language model onto the GPU and exposes it as an HTTP endpoint. When a request arrives with an image URL and a text prompt, the model generates a natural-language response describing or answering questions about the image:

```
from ray import serve
from transformers import AutoModelForImageTextToText, AutoProcessor
import torch

@serve.deployment(ray_actor_options={"num_gpus": 1})
class QwenVLService:
    def __init__(self):
        model_name = "Qwen/Qwen3-VL-2B-Instruct"
        self.processor = AutoProcessor.from_pretrained(model_name)
        self.model = AutoModelForImageTextToText.from_pretrained(
            model_name, torch_dtype=torch.float16
        ).to("cuda")

    async def __call__(self, request):
        try:
            body = await request.json()
            image_url = body.get("image_url")
            prompt = body.get("prompt")
            messages = [{"role": "user", "content": [
                {"type": "image", "image": image_url},
                {"type": "text", "text": prompt},
            ]}]
            inputs = self.processor.apply_chat_template(
                messages, tokenize=True, add_generation_prompt=True,
                return_dict=True, return_tensors="pt"
            ).to("cuda")
            generated_ids = self.model.generate(**inputs, max_new_tokens=200)
            trimmed = [o[len(i):] for i, o in zip(inputs.input_ids, generated_ids)]
            output = self.processor.batch_decode(trimmed, skip_special_tokens=True)[0]
            return {"response": output}
        Except Exception:
            logger.exception("Qwen inference request failed")
            return {"error": "Unable to generate a response. Please try again later."}

app = QwenVLService.bind()
```

The entire serving logic in
`qwen_serve.py`
is added to a
`qwen-serve-code`
ConfigMap. The
`@serve.deployment`
decorator with
`ray_actor_options={"num_gpus": 1}`
tells Ray to schedule this deployment on a worker with one available GPU. The model loads in
`float16`
to fit within the 24 GB of VRAM available on the A10G GPU used in the next section.

## Deploy on Amazon EKS

Deploy the Ray Serve DLC along with the
`qwen-serve-code`
ConfigMap created earlier. The following diagram shows the target architecture: an Amazon EKS cluster with a single GPU node running one pod that serves the model over HTTP on port 8000.

[![Architecture diagram of an Amazon EKS cluster with a single GPU node running one pod that serves the model over HTTP on port 8000](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/09/08/ML-21647-1.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/09/08/ML-21647-1.png)

Figure 1: Single-node inference architecture on Amazon EKS, with one GPU pod serving the model over HTTP on port 8000

This deployment uses a single
[g5.xlarge](/ec2/instance-types/g5/)
instance (one NVIDIA A10G GPU, 24 GB VRAM). It’s a single-node inference setup: one pod, one GPU, one machine. For multi-node distributed serving (model parallelism across machines or horizontal autoscaling with multiple replicas), you would build on top of this foundation using
[KubeRay](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
to orchestrate Ray workers across nodes.

The
[accompanying repository](https://github.com/aws-samples/sample-aws-deep-learning-containers/tree/main/inference/ray-serve/ray-serve-single-node)
includes scripts that automate the infrastructure setup:

1. `deploy_cluster.sh`
   provisions an EKS cluster using
   `eksctl`
   , with virtual private cloud (VPC) networking, an OIDC provider for AWS Identity and Access Management (IAM)-based pod authentication, and core cluster add-ons.
2. `deploy_node_group.sh`
   adds a managed GPU node group with a single
   `g5.xlarge`
   instance labeled
   `role=gpu-worker`
   .
3. `deploy_ray_cluster.sh`
   applies a ConfigMap with
   `qwen_serve.py`
   , deploys a Kubernetes Deployment manifest that schedules the pod on the GPU node, and starts Ray Serve on port 8000.
4. After running the three scripts, verify that the pod is running and the GPU is allocated:

   ```
   kubectl get pods -n inference
   kubectl describe pod -n inference -l app=ray-serve | grep "nvidia.com/gpu"
   ```

With the pod reporting ready, port-forward to it so we can test it.

```
kubectl port-forward -n inference deploy/ray-cluster 8000:8000
```

On a new terminal, send a request that asks the
`Qwen3-VL-2B`
vision-language model to describe an image:

```
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{
    "image_url": "https://s3.amazonaws.com/model-server/inputs/kitten.jpg",
    "prompt": "Describe this image briefly."
  }'
```

You should receive a JSON response with the model’s description of the image. To confirm that inference is running on the GPU:

```
kubectl exec -n inference deploy/ray-cluster -- nvidia-smi
```

**Note:**
The pod reports Ready a minute or two before Ray Serve starts answering, because the model is still loading. If the first request is refused, wait a minute and try the request again.

## Clean up

To avoid ongoing charges, tear down the resources in reverse order:

```
./delete_ray_cluster.sh   # Remove the Ray Serve deployment
./delete_node_group.sh    # Remove the GPU node group
./delete_cluster.sh       # Delete the EKS cluster
```

## Conclusion and next steps

At this point you have a working inference endpoint, and you got there without maintaining CUDA compatibility yourself, without writing TorchServe handler boilerplate, and without assembling a multi-stage Dockerfile that stitches the GPU stack together. That’s what the Ray Serve DLC is designed to do: provide a supported, pre-tested container so you can focus on model code rather than infrastructure maintenance.

For teams currently on TorchServe, this is a strong migration path. The DLC eliminates version drift, simplifies upgrades to a tag swap, and provides regular security patches managed by AWS. For workloads that need to scale beyond a single node,
[KubeRay](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
extends this same foundation to multi-node distributed serving.

To get started, try the accompanying
[code sample](https://github.com/aws-samples/sample-aws-deep-learning-containers/tree/main/inference/ray-serve/ray-serve-single-node)
for a complete end-to-end deployment. To browse all available DLC images, including CPU variants and other frameworks, visit the
[AWS Deep Learning Containers reference](https://aws.github.io/deep-learning-containers/reference/available_images/)
.

---

## About the authors

### Ananth Raghavendra

Ananth is a Senior AI Solutions Architect at AWS. He specializes in architecting distributed Gen AI applications running on NVIDIA GPUs, AWS Trainium and AWS Inferentia using platforms and orchestrators such as Amazon SageMaker HyperPod, Amazon EKS, Ray, SageMaker Serverless Inference, Amazon Nova Forge, and Slurm.

### Jinyan Li

Jinyan is a Software Development Engineer at Amazon Web Services. Her work focuses on building and improving containerized environments for machine learning workloads on AWS. She holds a Master’s degree in Computer Science from Northeastern University.

### Felipe Lopez

Felipe is a Principal AI/ML Specialist Solutions Architect at AWS. Prior to joining AWS, Felipe worked with GE Digital and SLB, where he focused on modeling and optimization products for industrial applications.