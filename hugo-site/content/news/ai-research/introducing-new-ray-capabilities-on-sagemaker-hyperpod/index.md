---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-22T04:26:29.378266+00:00'
exported_at: '2026-09-22T04:26:33.427124+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-new-ray-capabilities-on-sagemaker-hyperpod
structured_data:
  about: []
  author: ''
  description: Amazon SageMaker HyperPod now offers managed Ray support on Amazon
    EKS. Create and monitor Ray clusters, connect JupyterLab and Code Editor notebooks
    to live clusters, get out-of-the-box observability, and run resilient distributed
    training and accelerated inference from SageMaker Studio, all with open-source
    KubeRa...
  headline: Introducing new Ray capabilities on SageMaker HyperPod
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/introducing-new-ray-capabilities-on-sagemaker-hyperpod
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing new Ray capabilities on SageMaker HyperPod
updated_at: '2026-09-22T04:26:29.378266+00:00'
url_hash: ce8bd1cd1375721dca43fbe2d5248feace82b725
---

Today, we are announcing new Ray capabilities on
[Amazon SageMaker HyperPod](/sagemaker/hyperpod/)
that integrate Ray with the HyperPod purpose-built infrastructure for foundation model training and serving.

[Ray](https://docs.ray.io/)
is an open-source framework that data scientists use to scale distributed Python workloads across clusters of GPUs, from distributed training with Ray Train to model serving with Ray Serve. On Kubernetes, Ray clusters are managed by
[KubeRay](https://github.com/ray-project/kuberay)
, an open-source operator that handles cluster lifecycle through custom resources (RayCluster, RayJob, RayService). SageMaker HyperPod provides purpose-built infrastructure for large-scale machine learning (ML) on
[Amazon Elastic Kubernetes Service](/eks/)
(Amazon EKS) with built-in node health monitoring and automatic recovery. Until now, running Ray on Kubernetes required data scientists to write YAML manifests, manage Docker image rebuilds for every dependency change, set up kubectl port-forward to access their Ray Dashboard, and configure Prometheus and Grafana manually for observability.

With this launch, data scientists can create Ray clusters, open the Ray Dashboard and
[Amazon Managed Grafana](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/amg-dashboarding-visualization.html)
observability dashboards, connect a JupyterLab or Code Editor workspace to their cluster, submit distributed jobs, and configure hung job detection, all from
[SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html)
. At the application level, Ray training jobs gain automatic fault tolerance through HyperPod node health monitoring and recovery, plus tiered checkpointing for faster resume through HyperPod distributed tiered storage.
[SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
integration loads model weights directly into Ray Serve endpoints, with KV cache offloading to tiered storage for serving long-context requests. These capabilities work with open-source
[KubeRay](https://github.com/ray-project/kuberay)
and standard Ray APIs, so existing scripts and workflows run without modification.

In this post, we walk through how to get started with each of these capabilities.

## Prerequisites

To follow along with this post, you need an
[Amazon SageMaker HyperPod cluster with Amazon EKS orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html)
and the following components installed on your cluster:

* **SageMaker Spaces EKS add-on**
  , which enables JupyterLab and Code Editor workspaces in Amazon SageMaker HyperPod that attach to Ray clusters for interactive development.
* **HyperPod Observability EKS add-on**
  , which collects metrics from Ray workloads and provisions Grafana dashboards in Amazon Managed Grafana.
* **KubeRay operator**
  , which manages RayCluster, RayJob, and RayService as native Kubernetes resources.
* **HyperPod Ray Endpoint Operator**
  (Helm chart), which generates authenticated public endpoints for dashboard access and remote job submission.

You also need a SageMaker Studio domain, which provides the console interface for creating Ray clusters, viewing workloads, opening dashboards, and managing HyperPod Spaces. For full setup instructions, see the
[Ray on HyperPod getting started guide.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-getting-started.html)

## Purpose-built data scientist experience

SageMaker Studio now provides a complete Ray development environment. Data scientists can create, manage, and monitor Ray clusters directly from the console without writing Kubernetes manifests or running kubectl commands. You can check out the full experience
[in this interactive demo.](https://d1dpyy0tl92esj.cloudfront.net/overview)

To get started, navigate to SageMaker Studio and choose
**HyperPod**
. Select your HyperPod cluster, then go to the
**Tasks**
tab. From the task type list, choose
**RayCluster**
. The console displays your Ray clusters with their status, instance types, and available actions. To create a new cluster, choose
**Create Ray Cluster**
.

![SageMaker Studio HyperPod Tasks tab listing Ray clusters with a Create Ray Cluster button](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-2.-create-cluster.png)

The creation form prompts you for a cluster name, head and worker instance types, worker count, and container image. By default, clusters use the
[SageMaker Distribution](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-images.html)
image, which comes with Ray pre-installed and is managed by AWS with regular vulnerability patching and software upgrades. You can also specify a custom container image if your workload requires additional dependencies.

For customers who prefer kubectl or need advanced customization, an inline YAML editor in Studio exposes the full Kubernetes manifest. The KubeRay operator also integrates with
[HyperPod task governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html)
, so administrators can set compute quotas and scheduling priorities for Ray workloads alongside other training jobs.

During creation, enable remote endpoints so that you can access the Ray Dashboard, submit jobs, and retrieve logs from anywhere with internet access, securely and without local kubectl port-forwarding. To learn more, see
[Ray Dashboard access.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-dashboard.html)

![Ray cluster creation form with remote endpoints enabled](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-3.-enable-endpoints.png)

After the create cluster form is submitted, go back to the tasks tab and it will show the cluster like in the screenshot below. From the
**Actions**
menu, you can open the Ray Dashboard, view Grafana metrics, edit the cluster configuration, or delete the cluster.

![Tasks tab showing a running Ray cluster with the Actions menu open](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-4.-List-clusters.png)

After the cluster reaches Running status, choose
**Open Ray Dashboard**
from the Actions menu. The system generates a short-lived, IAM-authenticated URL scoped to the cluster creator. The Ray Dashboard opens in a new tab, showing cluster health, running jobs, and node status.

![Ray Dashboard showing cluster health, running jobs, and node status](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-5-ray-dashboard.png)



### Remote job submission

For production workloads, you can submit jobs remotely to Ray clusters from Studio, your laptop, or continuous integration and continuous delivery (CI/CD) pipelines using the
`toolkit-for-ray-on-sagemaker-ai`
[Python package](https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/)
. The package handles endpoint resolution and EKS API credential generation through IAM authentication, so you use standard Ray job submission APIs with a SageMaker-aware address resolver:

```
$ aws eks update-kubeconfig --name &lt;eks-cluster-name&gt; --region &lt;region&gt;
$ pip install toolkit-for-ray-on-sagemaker-ai
$ ray job submit --address sagemaker_ray://&lt;ray-cluster-name&gt;/&lt;namespace&gt; \
     --working-dir &lt;your-code-directory&gt; \
     --python your-code.py
# To list ray jobs
$ ray job list --address sagemaker_ray://&lt;ray-cluster-name&gt;/&lt;namespace&gt;
```

### Interactive development with SageMaker Spaces

Data scientists can attach a Ray cluster to a
[HyperPod JupyterLab or Code Editor space](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-ide.html)
from Studio. The space joins the cluster as a zero-compute worker node, giving the notebook full native Ray driver access. You select your cluster from a list during space creation and begin working immediately.

After creating a HyperPod JupyterLab or Code Editor space, a Ray cluster integration option appears in the configuration panel.

![HyperPod space configuration panel showing the Ray cluster integration option](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-6.-Select-RayCluster-in-spaces.png)

Select the Ray cluster you want your workspace to connect to.

![Selecting the Ray cluster to attach to the workspace during space creation](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-7.-attach-ray-cluster.png)

Attaching a Ray cluster restarts the space. Once it restarts, open JupyterLab or Code Editor in your browser and call
`ray.init(address="auto")`
. You are connected to your Ray cluster and can run distributed workloads as if you were on the head node. Ray’s
`runtime_env`
parameter lets you inject Python dependencies at runtime without rebuilding container images, and you can scale workers up or down without recreating the cluster. For example, a data scientist training a model can start prototyping in a notebook with a single worker, then scale to four GPU workers by changing one line in
[ScalingConfig](https://docs.ray.io/en/latest/train/api/doc/ray.train.ScalingConfig.html)
. The training runs distributed across the attached Ray cluster while the notebook remains interactive for monitoring progress, adjusting hyperparameters, or inspecting intermediate results. The entire workflow stays within the notebook.

![JupyterLab notebook connected to a Ray cluster running a distributed training job](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-8-Screenshot-2026-08-17-at-2.54.45%E2%80%AFPM.png)



To learn more, see
[IDEs and Notebooks with Ray.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-ide-notebooks.html)

## Out-of-the-box observability

Setting up Ray observability on Kubernetes with
[Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
and
[Amazon Managed Grafana](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/amg-dashboarding-visualization.html)
is a multi-step process that involves installing Helm charts, creating PodMonitors and ServiceMonitors, configuring IAM roles for SigV4 signing, and manually importing dashboard JSON files.

The HyperPod Observability EKS add-on now handles all of this. It automatically discovers Ray head and worker pods, scrapes their metrics endpoints, and provisions four pre-built Grafana dashboards in Amazon Managed Grafana: Ray Core, Ray Data, Ray Train, and Ray Serve. You do not need to create PodMonitors, configure scrape targets, or import dashboard JSON files.

All four dashboards are organized under a
**Ray**
folder in Amazon Managed Grafana and support filtering metrics by specific Ray cluster. The
**Open Grafana**
action from the cluster list (shown in the first screenshot) takes you directly to the metrics for your specific cluster in one click. The dashboards appear alongside existing HyperPod infrastructure dashboards (GPU, EFA, task governance), so operations teams see Ray workload metrics and cluster health in one place.

![Amazon Managed Grafana Ray dashboard showing Ray workload metrics](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/24/ml-21715-9-grafana.png)

## Resilient training

SageMaker HyperPod provides three layers of resilience for Ray training workloads: automatic node recovery when hardware fails, hung job detection when training stalls, and tiered checkpointing for fast recovery after either event.

### Automatic node recovery

SageMaker HyperPod continuously monitors node health and can
[automatically replace faulty nodes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-node-recovery.html)
so your Ray training jobs can run for as long as needed without manual restarts. When a node is replaced, Ray reschedules worker pods onto the new healthy node. If your training code saves checkpoints periodically and includes logic to resume from the latest checkpoint, the job picks up where it left off. This requires no changes to your existing Ray training code. You only need to configure a sufficient number of retries in your
[RayJob’s FailureConfig](https://docs.ray.io/en/latest/train/api/doc/ray.train.FailureConfig.html)
so that jobs recover automatically rather than failing permanently on the first interruption. To learn more, see
[Automatic node recovery with Ray.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-node-recovery.html)

### Hung job detection

Distributed training jobs can hang without producing errors. A single pod fails (because of a network partition, storage mount issue, or hardware fault), and every other pod blocks at the next collective operation, waiting indefinitely. GPUs stay allocated with memory loaded but produce no useful compute. Because there is no error message or crash, data scientists often discover the problem hours later when they check job progress manually. At scale, a few hours of undetected hang time across dozens of GPUs represents significant wasted cost.

SageMaker HyperPod EKS now includes a per-node Job Monitoring Agent that detects these conditions for Ray Train workloads automatically, with no changes to your code. The agent monitors multiple node-level and job-level signals to determine when a training job has stalled, and notifies the user through the cluster’s Amazon CloudWatch log group and the Ray Train Grafana dashboard provisioned by the HyperPod Observability add-on.

For custom detection rules, data scientists can use the
`toolkit-for-ray-on-sagemaker-ai`
library to define log patterns and timeout thresholds. When the configured action is
`cancel`
, HyperPod terminates the hung worker process and Ray Train’s built-in FailureConfig restarts workers from the last checkpoint. To learn more, see
[HyperPod Hung Job Detection on Ray.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-hung-job-detection.html)

### Tiered checkpointing

Fast checkpoint recovery is critical for both node replacement and hung job restart scenarios. The
`amzn-sagemaker-checkpointing`
library integrates with
[HyperPod managed tiered checkpointing](https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing.html)
, which writes checkpoints to local disk and asynchronously uploads them to Amazon Simple Storage Service (Amazon S3). When a job restarts, the library checks HyperPod Tiered Storage first. If the checkpoint is still available there, recovery is faster than restoring from Amazon S3. For large models, this can reduce recovery time compared to restoring directly from Amazon S3. To learn more, see
[HyperPod Tiered Storage on Ray.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-tiered-storage.html)

## Accelerated inference

[Ray Serve](https://docs.ray.io/en/latest/serve/index.html)
is Ray’s framework for deploying ML models as scalable, production-ready endpoints. It supports multi-model composition, autoscaling, and works with serving engines like vLLM. SageMaker HyperPod supports Ray Serve workloads on EKS, so you can deploy and scale inference endpoints on your HyperPod cluster.

[SageMaker JumpStart](/sagemaker/jumpstart/)
provides a catalog of pre-trained models. With this launch, the
`toolkit-for-ray-on-sagemaker-ai`
library now includes a JumpStart model loader that downloads model weights from the JumpStart catalog and deploys them directly into Ray Serve on HyperPod without manual weight download, model configuration, or container setup.

One common challenge with large language model (LLM) serving is that inference latency grows with context length. Each new token requires recalculating attention over all previous tokens, making long documents and multi-turn conversations slow and expensive. SageMaker HyperPod addresses this with
[Managed Tiered KV Cache](/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/)
. The tiered cache stores attention key-value vectors in CPU memory on each node (L1) and on HyperPod Tiered Storage for cross-instance sharing (L2). Your Ray Serve deployments can take advantage of the Tiered Storage KV caching capabilities in SageMaker HyperPod with minimal code changes, reducing time-to-first-token for multi-turn conversations and long-document workloads. To learn more, see
[Accelerated Ray Inference on SageMaker HyperPod.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-accelerated-inference.html)

## Clean up

To free up compute capacity on your cluster, delete any Ray clusters you created during this walkthrough. From the SageMaker Studio Tasks tab, select your Ray cluster and choose
**Delete**
from the Actions menu. If you created a HyperPod cluster, you can
[delete the cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-delete-cluster.html)
from the Amazon SageMaker AI console to stop incurring charges for the underlying compute instances. If you installed any prerequisite add-ons for testing,
[uninstall them from EKS console](https://docs.aws.amazon.com/eks/latest/userguide/removing-an-add-on.html)
to free up compute capacity.

## Conclusion

In this post, we walked through how Amazon SageMaker HyperPod now provides a complete Ray experience on EKS, from cluster creation and interactive notebooks to resilient training and accelerated inference. All of this works with open-source KubeRay and standard Ray APIs, so existing scripts run without modification. We’d like to thank Dhawal Parkar, Pradeep Cruz, Mark Vinciguerra, and Giuseppe Angelo Porcelli for their contributions to this post.

This integration is available today in all AWS Regions where SageMaker HyperPod EKS is supported. To get started, see the
[Amazon SageMaker HyperPod documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
and the
[Ray on HyperPod getting started guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray.html)
. You can also explore the full workflow in this
[interactive demo](https://d1dpyy0tl92esj.cloudfront.net/overview)
. If you’d like to discuss how Ray on HyperPod can support your workloads,
[contact an AWS representative](/contact-us/)
.

---

## About the authors

### Nilesh PS

Nilesh is a Senior Software Development Engineer at AWS working on Amazon SageMaker HyperPod. He focuses on Ray cluster management, training resiliency, and observability for large-scale distributed ML workloads on Kubernetes.

### Vishal Shahane

Vishal is a Principal Engineer at AWS working on Amazon SageMaker HyperPod, where he focuses on building reliable, scalable infrastructure for large-scale AI/ML workloads.

### Shreyas Adiyodi

Shreyas is a Product Manager at AWS based out of Seattle. He is focused on enabling Gen AI model development on SageMaker HyperPod, partnering with customers to simplify cluster provisioning, enhance OSS AI/ML framework support, and strengthen security and compliance.