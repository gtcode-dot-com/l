---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-20T00:03:27.674829+00:00'
exported_at: '2025-12-20T00:03:30.014248+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-soci-indexing-for-amazon-sagemaker-studio-faster-container-startup-times-for-ai-ml-workloads
structured_data:
  about: []
  author: ''
  description: 'Today, we are excited to introduce a new feature for SageMaker Studio:
    SOCI (Seekable Open Container Initiative) indexing. SOCI supports lazy loading
    of container images, where only the necessary parts of an image are downloaded
    initially rather than the entire container.'
  headline: 'Introducing SOCI indexing for Amazon SageMaker Studio: Faster container
    startup times for AI/ML workloads'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/introducing-soci-indexing-for-amazon-sagemaker-studio-faster-container-startup-times-for-ai-ml-workloads
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Introducing SOCI indexing for Amazon SageMaker Studio: Faster container startup
  times for AI/ML workloads'
updated_at: '2025-12-20T00:03:27.674829+00:00'
url_hash: 5a80f7007ed62a9a6ee418f17f1d6c70f222d77a
---

Today, we are excited to introduce a new feature for
[SageMaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
:
[SOCI (Seekable Open Container Initiative)](https://aws.amazon.com/about-aws/whats-new/2022/09/introducing-seekable-oci-lazy-loading-container-images/)
indexing. SOCI supports lazy loading of container images, where only the necessary parts of an image are downloaded initially rather than the entire container.

[SageMaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
serves as a web Integrated Development Environment (IDE) for end-to-end machine learning (ML) development, so users can build, train, deploy, and manage both traditional ML models and foundation models (FM) for the complete ML workflow.

Each SageMaker Studio application runs inside a container that packages the required libraries, frameworks, and dependencies for consistent execution across workloads and user sessions. This containerized architecture allows SageMaker Studio to support a wide range of ML frameworks such as TensorFlow, PyTorch, scikit-learn, and more while maintaining strong environment isolation. Although SageMaker Studio provides containers for the most common ML environments, data scientists may need to tailor these environments for specific use cases by adding or removing packages, configuring custom environment variables, or installing specialized dependencies. SageMaker Studio supports this customization through
[Lifecycle Configurations (LCCs)](https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc.html)
, which allow users to run bash scripts at the startup of a Studio IDE space. However, repeatedly customizing environments using LCCs can become time-consuming and difficult to maintain at scale. To address this, SageMaker Studio supports building and registering
[custom container images](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-prepare-image.html)
with preconfigured libraries and frameworks. These reusable custom images reduce setup friction and improve reproducibility for consistency across projects, so data scientists can focus on model development rather than environment management.

As ML workloads become increasingly complex, the container images that power these environments have grown in size, leading to longer startup times that can delay productivity and interrupt development workflows. Data scientists, ML engineers, and developers may have longer wait times for their environments to initialize, particularly when switching between different frameworks or when using images with extensive pre-installed libraries and dependencies. This startup latency becomes a significant bottleneck in iterative ML development where quick experimentation and rapid prototyping are essential. Instead of downloading the entire container image upfront, SOCI creates an index that allows the system to fetch only the specific files and layers needed to start the application, with additional components loaded on-demand as required. This significantly reduces container startup times from minutes to seconds, allowing your SageMaker Studio environments to launch faster and get you working on your ML projects sooner, ultimately improving developer productivity and reducing time-to-insight for ML experiments.

### Prerequisites

To use SOCI indexing with SageMaker Studio, you need:

## SageMaker Studio SOCI Indexing – Feature overview

The
[SOCI (Seekable Open Container Initiative
)](https://aws.amazon.com/about-aws/whats-new/2022/09/introducing-seekable-oci-lazy-loading-container-images/)
, originally open sourced by AWS, addresses container startup delays in SageMaker Studio through selective image loading. This technology creates a specialized index that maps the internal structure of container images for granular access to individual files without downloading the entire container archive first. Traditional container images are stored as ordered lists of layers in gzipped tar files, which typically require complete download before accessing any content. SOCI overcomes this limitation by generating a separate index stored as an OCI Artifact that links to the original container image through OCI Reference Types. This design preserves all original container images, maintains consistent image digests, and ensures signature validity—critical factors for AI/ML environments with strict security requirements.

For SageMaker Studio users, you can implement SOCI indexing through the integration with
[Finch container runtime](https://github.com/runfinch/finch)
, this translates to 35-70% reduction in container startup times across all instance types using Bring Your Own Image (BYOI). This implementation extends beyond current optimization strategies that are limited to specific first-party image and instance type combinations, providing faster app launch times in SageMaker AI Studio and SageMaker Unified Studio environments.

## Creating a SOCI index

To create and manage SOCI indices, you can use several container management tools, each offering different advantages depending on your development environment and preferences:

* [Finch CLI](https://aws.amazon.com/blogs/opensource/introducing-finch-an-open-source-client-for-container-development/)
  is a Docker-compatible command-line tool developed by AWS that provides native support for building and pushing SOCI indices. It offers a familiar Docker-like interface while including built-in SOCI functionality, making it straightforward to create indexed images without additional tooling.
* [nerdctl](https://github.com/containerd/nerdctl)
  serves as an alternative container CLI for containerd, the industry-standard container runtime. It provides Docker-compatible commands while offering direct integration with containerd features, including SOCI support for lazy loading capabilities.
* Docker + SOCI CLI combines the widely used Docker toolchain with the dedicated SOCI command-line interface. This approach allows you to leverage existing Docker workflows while adding SOCI indexing capabilities through a separate CLI tool, providing flexibility for teams already invested in Docker-based development processes.

In the standard SageMaker Studio workflow, launching a machine learning environment requires downloading the complete container image before any application can start. When user initiates a new SageMaker Studio session, the system must pull the entire image containing frameworks like TensorFlow, PyTorch, scikit-learn, Jupyter, and associated dependencies from the container registry. This process is sequential and time consuming—the container runtime downloads each compressed layer, extracts the complete filesystem to local storage, and only then can the application begin initialization. For typical ML images ranging from 2-5 GB, this results in startup times of 3-5 minutes, creating significant friction in iterative development workflows where data scientists frequently switch between different environments or restart sessions.The SOCI-enhanced workflow transforms container startup by enabling intelligent, on-demand file retrieval. Instead of downloading entire images, SOCI creates a searchable index that maps the precise location of every file within the compressed container layers. When launching a SageMaker Studio application, the system downloads only the SOCI index (typically 10-20 MB) and the minimal set of files required for application startup—usually 5-10% of the total image size. The container begins running immediately while a background process continues downloading remaining files as the application requests them. This lazy loading approach reduces initial startup times from few minutes to seconds, allowing users to begin productive work almost immediately while the environment completes initialization transparently in the background.

## Converting the image to SOCI

You can convert your existing image into a SOCI image and push it to your private ECR using the following commands:

```
#/bin/bash
# Download and install soci-snapshotter, containerd, and nerdctl
sudo yum install soci-snapshotter
sudo yum install containerd jq
sudo systemctl start soci-snapshotter
sudo systemctl restart containerd
sudo yum install nerdctl

# Set your registry variables
REGISTRY="123456789012.dkr.ecr.us-west-2.amazonaws.com"
REPOSITORY_NAME="my-sagemaker-image"

# Authenticate for image pull and push
AWS_REGION=us-west-2
REGISTRY_USER=AWS
REGISTRY_PASSWORD=$(/usr/local/bin/aws ecr get-login-password --region $AWS_REGION)
echo $REGISTRY_PASSWORD | sudo nerdctl login -u $REGISTRY_USER --password-stdin $REGISTRY

# Pull the original image
sudo nerdctl pull $REGISTRY/$REPOSITORY_NAME\:original-image

# Create SOCI index using the convert subcommand
sudo nerdctl image convert --soci $REGISTRY/$REPOSITORY_NAME\:original-image $REGISTRY/$REPOSITORY_NAME\:soci-image

# Push the SOCI v2 indexed image
sudo nerdctl push --platform linux/amd64 $REGISTRY/$REPOSITORY_NAME\:soci-image
```

This process creates two artifacts for the original container image in your ECR repository:

* **SOCI index**
  – Metadata enabling lazy loading.
* **Image index manifest**
  – OCI-compliant manifest linking them together.

To use SOCI-indexed images in SageMaker Studio, you must reference the image index URI rather than the original container image URI when creating SageMaker Image and SageMaker Image Version resources. The image index URI corresponds to the tag you specified during the SOCI conversion process (for example, soci-image in the previous example).

```
#/bin/bash
# Use the SOCI v2 image index URI
IMAGE_INDEX_URI="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-sagemaker-image:soci-image"

# Create SageMaker Image
aws sagemaker create-image \
--image-name "my-sagemaker-image" \
--role-arn "arn:aws:iam::123456789012:role/SageMakerExecutionRole"

# Create SageMaker Image Version with SOCI index
aws sagemaker create-image-version \
--image-name "my-sagemaker-image" \
--base-image "$IMAGE_INDEX_URI"

# Create App Image Config for JupyterLab
aws sagemaker create-app-image-config \
--app-image-config-name "my-sagemaker-image-config" \
--jupyter-lab-app-image-config '{ "FileSystemConfig": { "MountPath": "/home/sagemaker-user", "DefaultUid": 1000, "DefaultGid": 100 } }'

#Update domain to include the custom image (required step)
aws sagemaker update-domain \
 --domain-id "d-xxxxxxxxxxxx" \
 --default-user-settings '{
        "JupyterLabAppSettings": {
        "CustomImages": [{
        "ImageName": "my-sagemaker-image",
        "AppImageConfigName": "my-sagemaker-image-config"
        }]
      }
 }'
```

The image index URI contains references to both the container image and its associated SOCI index through the OCI Image Index manifest. When SageMaker Studio launches applications using this URI, it automatically detects the SOCI index and enables lazy loading capabilities.

SOCI indexing is supported for all ML environments (JupyterLab, CodeEditor, etc.) for both SageMaker Unified Studio and SageMaker AI. For additional information on setting up your customer image, please reference
[SageMaker Bring Your Own Image documentation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/byoi.html)
.

## Benchmarking SOCI impact on SageMaker Studio JupyterLab startup

The primary objective of this new feature in SageMaker Studio is to streamline the end user experience by reducing the startup durations for SageMaker Studio applications launched with custom images. To measure the effectiveness of lazy loading custom container images in SageMaker Studio using SOCI, we will empirically quantify and contrast start-up durations for a given custom image both with and without SOCI. Further, we’ll conduct this test for a variety of custom images representing a diverse sets of dependencies, files, and data, to evaluate how effectiveness may vary for end users with different custom image needs.

To empirically quantify the startup durations for custom image app launches, we will programmatically launch JupyterLab and CodeEditor Apps with the SageMaker
`CreateApp`
API—specifying the candidate
`sageMakerImageArn`
and
`sageMakerImageVersionAlias`
event time with an appropriate
`instanceType`
—recording the
`eventTime`
for analysis. We will then poll the SageMaker
`ListApps`
API every second to monitor the app startup, recording the
`eventTime`
of the first response that where
`Status`
is reported as
`InService`
. The delta between these two times for a particular app is the startup duration.

For this analysis, we have created two sets of private ECR repositories, each with the same SageMaker custom container images but with only one set implementing SOCI indices. When comparing the equivalent images in ECR, we can see the SOCI artifacts present in only one repo. We will be deploying the apps into a single SageMaker AI domain. All custom images are attached to that domain so that its SageMaker Studio users can choose those custom images when invoking startup of a JupyterLab space.

To run the tests, for each custom image, we invoke a series of ten
`CreateApp`
API calls:

```
"requestParameters": {
    "domainId": "<>",
    "spaceName": "<>",
    "appType": "JupyterLab",
    "appName": "default",
    "tags": [],
    "resourceSpec": {
        "sageMakerImageArn": "<>",
        "sageMakerImageVersionAlias": "<>",
        "instanceType": "<>"
    },
    "recoveryMode": false
}
```

The following table captures the startup acceleration with SOCI index enabled for Amazon SageMaker distribution images:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **App type** | **Instance type** | **Image** | **App startup duration (sec)** | | **% Reduction in app startup duration** |
|  |  |  | **Regular image** | **SOCI image** |  |
| **SMAI JupyterLab** | t3.medium | SMD 3.4.2 | 231 | 150 | 35.06% |
|  | t3.medium | SMD 3.4.2 | 350 | 191 | 45.43% |
|  | c7i.large | SMD 3.4.2 | 331 | 141 | 57.40% |
| **SMAI CodeEditor** | t3.medium | SMD 3.4.2 | 202 | 110 | 45.54% |
|  | t3.medium | SMD 3.4.2 | 213 | 78 | 63.38% |
|  | c7i.large | SMD 3.4.2 | 279 | 91 | 67.38% |

*Note: Each app startup latency and their improvement may vary depending on the availability of SageMaker ML instances.*

Based on these findings, we see that running SageMaker Studio custom images with SOCI indexes allows SageMaker Studio users to launch their apps faster compared to without SOCI indexes. Specifically, we see ~35-70% faster container start-up time.

## Conclusion

In this post, we showed you how the introduction of SOCI indexing to SageMaker Studio improves the developer experience for machine learning practitioners. By optimizing container startup times through lazy loading—reducing wait times from several minutes to under a minute—AWS helps data scientists, ML engineers, and developers spend less time waiting and more time innovating. This improvement addresses one of the most common friction points in iterative ML development, where frequent environment switches and restarts impact productivity. With SOCI, teams can maintain their development velocity, experiment with different frameworks and configurations, and accelerate their path from experimentation to production deployment.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/10/PranavMurthy-ProfilePhoto.jpg)
Pranav Murthy**
is a Senior Generative AI Data Scientist at AWS, specializing in helping organizations innovate with Generative AI, Deep Learning, and Machine Learning on Amazon SageMaker AI. Over the past 10+ years, he has developed and scaled advanced computer vision (CV) and natural language processing (NLP) models to tackle high-impact problems—from optimizing global supply chains to enabling real-time video analytics and multilingual search. When he’s not building AI solutions, Pranav enjoys playing strategic games like chess, traveling to discover new cultures, and mentoring aspiring AI practitioners. You can find Pranav on
[LinkedIn](https://www.linkedin.com/in/pranav-murthy-6bbb5773/)
**.**

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/18/niki-2.jpg)
Raj Bagwe**
is a Senior Solutions Architect at Amazon Web Services, based in San Francisco, California. With over 6 years at AWS, he helps customers navigate complex technological challenges and specializes in Cloud Architecture, Security and Migrations. In his spare time, he coaches a robotics team and plays volleyball. You can find Raj on
[LinkedIn](https://www.linkedin.com/in/rajesh-bagwe-1995762/)
.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/18/niki-1-1.jpg)
**Nikita Arbuzov**
is a Software Development Engineer at Amazon Web Services, working and maintaining SageMaker Studio platform and its applications, based in New York, NY. With over 3 years of experience in backend platform latency optimization, he works on improving customer experience and usability of SageMaker AI and SageMaker Unified Studio. In his spare time, Nikita performs different outdoor activities, like mountain biking, kayaking, and snowboarding, loves traveling around the US and enjoys making new friends. You can find Nikita on
[LinkedIn](https://www.linkedin.com/in/nikita-arbuzov-psu/)
.