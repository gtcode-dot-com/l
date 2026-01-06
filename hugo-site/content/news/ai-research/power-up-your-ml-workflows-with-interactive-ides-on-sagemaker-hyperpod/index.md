---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-25T00:00:20.086999+00:00'
exported_at: '2025-11-25T00:00:23.713680+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/power-up-your-ml-workflows-with-interactive-ides-on-sagemaker-hyperpod
structured_data:
  about: []
  author: ''
  description: Amazon SageMaker HyperPod clusters with Amazon Elastic Kubernetes Service
    (EKS) orchestration now support creating and managing interactive development
    environments such as JupyterLab and open source Visual Studio Code, streamlining
    the ML development lifecycle by providing managed environments for familiar tools
    to data scientists. This post shows how HyperPod administrators can configure
    Spaces for their clusters, and how data scientists can create and connect to these
    Spaces.
  headline: Power up your ML workflows with interactive IDEs on SageMaker HyperPod
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/power-up-your-ml-workflows-with-interactive-ides-on-sagemaker-hyperpod
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Power up your ML workflows with interactive IDEs on SageMaker HyperPod
updated_at: '2025-11-25T00:00:20.086999+00:00'
url_hash: 50457573a0ef2b3226c4191aedca266ce638c69d
---

[Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/)
clusters with
[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
orchestration now support creating and managing interactive development environments such as JupyterLab and open source Visual Studio Code, streamlining the ML development lifecycle by providing managed environments for familiar tools to data scientists. This feature introduces a new add-on called Amazon SageMaker Spaces for AI developers to create and manage self-contained environments for running notebooks. Organizations can now maximize their GPU investments by running both interactive workloads and their training jobs on the same infrastructure, with support for fractional GPU allocations to improve cost efficiency. This feature reduces the complexity of managing multiple development environments and focus on building and deploying their AI and ML models.

This post shows how HyperPod administrators can configure Spaces for their clusters, and how data scientists can create and connect to these Spaces. You’ll also learn how to connect directly from your local VS Code environment to Spaces created in HyperPod.

## Solution overview

The following diagram showcases the different components involved in creating and managing Spaces on HyperPod clusters.

![Solution architecture showing how Spaces on HyperPod works](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/spaces-architecture.png)

Here’s how the feature works:

1. Cluster administrator installs the Spaces add-on from the SageMaker AI console. The administrator can either use a
   **Quick install**
   or a
   **Custom install**
   option to install the add-on.
2. Once the cluster is set up, data scientists and AI developers can create Spaces using
   [HyperPod Command Line Interface](https://github.com/aws/sagemaker-hyperpod-cli)
   , or
   [kubectl](https://kubernetes.io/docs/reference/kubectl/)
   .
3. Once the Space is created, the user can connect to a running Space through one of the following two options:
   1. **Access Space Web UI**
      : This requires setting up an
      [AWS Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
      (ALB) and setting up or registering your own custom Domain Name System (DNS) in
      [Amazon Route 53](https://aws.amazon.com/route53/)
      . Once the custom domain is set up, the user will be able to connect to the JupyterLab or Code Editor space securely using a presigned URL through their web browser.
   2. **Remote IDE connection**
      (connect to the Space remotely from local Visual Studio Code): SSH-over-SSM tunneling is used under the hood to securely connect remote IDEs to SageMaker Spaces pods without requiring customers to manage SSH keys or exposing port 22.

### Prerequisites

To follow along, you need the following prerequisites:

1. An AWS account with permissions to create IAM roles, SageMaker resources such as HyperPod, and access to EKS cluster resources. If you are creating a new SageMaker HyperPod cluster, you will also need permissions to create networking and storage resources, see
   [IAM permissions for cluster creation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.html#sagemaker-hyperpod-prerequisites-iam-cluster-creation)
   .
2. A SageMaker HyperPod cluster orchestrated using EKS, running Kubernetes version 1.30 or later. If you do not have one, you can create by following instructions in
   [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-create-cluster.html)
   . This workflow will create a HyperPod cluster, an EKS cluster and the associated resources such as an
   [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)
   (VPC) and
   [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/)
   volume for storage.
3. [HyperPod CLI](https://github.com/aws/sagemaker-hyperpod-cli)
   installed (or
   [kubectl](https://kubernetes.io/docs/reference/kubectl/)
   ).
4. A local IDE such as VS Code, with the
   [AWS Toolkit for VS Code](https://aws.amazon.com/visualstudiocode/)
   installed, to connect to the Spaces.

#### Step 1: Install the Spaces add-on

To get started, first install the Spaces add-on to your SageMaker cluster. This add-on allows users to run JupyterLab and Code Editor applications directly on cluster compute. The
**Quick install**
option is the fastest way to get started. With a single click, SageMaker AI automatically creates and configures the required AWS resources with optimized defaults. Here’s how to install it:

1. In the SageMaker AI console, choose
   **Clusters**
   on the left pane and navigate to your HyperPod cluster
2. Choose the
   **IDE and Notebooks**
   tab
3. Choose
   **Quick install**

![Screenshot of the SageMaker console with IDE and Notebooks selected](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/ides-and-notebooks.png)

4. Review the dependencies that will be automatically installed and choose
   **Install**
   .

The Quick install will create the associated dependencies for your Spaces add-on with default settings. They are listed below:

5. IAM roles for SageMaker Spaces:
   1. Controller pod role for AWS API calls and
      [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
      Session Manager (SSM) operations.
   2. In-cluster router role for
      [AWS Key Management Service](https://aws.amazon.com/kms/)
      (KMS) operations and JWT signing.
   3. SSM managed instance role for remote access to Spaces.

      A list of the IAM roles and the required permissions are available in
      [Set up permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/permission-setup.html)
      .
6. Remote access components:
   1. Enables SSH connectivity to Spaces including SSM activation and session documents. This activates Systems Manager Advanced tier which includes additional per-instance charges.
7. Dependent EKS add-ons:
   1. [Cert-manager](https://docs.aws.amazon.com/eks/latest/userguide/community-addons.html#addon-cert-manager)
      for certificate management.
   2. [Amazon Elastic Block Store](https://aws.amazon.com/ebs/)
      (EBS) CSI driver for persistent storage volumes.
   3. [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)
      to manage AWS Elastic Load Balancers.
8. SageMaker Spaces add-on
   1. Deploys the Spaces controller and in-cluster router for managing Space lifecycle operations.

The Quick install option does not install web UI configurations such as Route 53 DNS records and SSL certificates for accessing Spaces through the web browser. Administrators can either use the
**Custom install**
option or configure these properties after installation of the add-on. For instructions on configuring web browser access, see
[Operator installing – helm/Console](https://docs.aws.amazon.com/sagemaker/latest/dg/operator-install.html#installation)
.

The installation typically takes 2-5 minutes depending on availability of pre-existing dependencies or if the Spaces add-on will need to provision completely new resources.  After installation completes, administrators can perform the following actions as shown below:

* **View the Spaces**
  created by data scientists in the Spaces table
* **Configure namespaces**
  to organize Spaces by team or project
* **Create Space templates**
  with pre-configured settings for common use cases
* **Edit configuration**
  at as needed to enable or disable Spaces features or change your configuration settings

![Screenshot of IDE and Notebooks after installing the add-on](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/ides-and-notebooks-after-install.png)

For production use cases, we recommend using the
**Custom install**
option, where admins can set up fine-grained IAM policies that apply principle of least-privilege. For the full set of configurations that can be set up using the
**Custom install**
option, including namespaces and default templates, see
[Installation](https://docs.aws.amazon.com/sagemaker/latest/dg/operator-install.html#installation)
.

#### Step 2: Create or update EKS access entries

To give your users access to create and manage Spaces, grant them access through
[EKS access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html)
. The following two access entry policies are required:

* `AmazonSagemakerHyperpodSpacePolicy`
* `AmazonSagemakerHyperpodSpaceTemplatePolicy`

For instructions on creating and editing access entries, see
[Create access entries](https://docs.aws.amazon.com/eks/latest/userguide/creating-access-entries.html)
and
[Update access entries](https://docs.aws.amazon.com/eks/latest/userguide/updating-access-entries.html)
.

#### Step 3: Create and manage Spaces

Data scientists can create JupyterLab and Code Editor Spaces on the cluster using
`kubectl`
or the HyperPod CLI. For detailed instructions on creating and managing Spaces, see
[Hyperpod CLI](https://github.com/aws/sagemaker-hyperpod-cli/tree/main?tab=readme-ov-file#space)
.

To create a Space, run the following commands:

```
# set cluster context using hyp CLI
hyp set-cluster-context --cluster-name <your-hyperpod-cluster-name>

# create a space
hyp create hyp-space \
     --name "data-science-space" \
     --display-name "Data Science Workspace" \
     --namespace "default"
```

The
`hyp create hyp-space`

command will create a Space with the default settings. To create a Code Editor space, use the command below:

```
hyp create hyp-space \
    --name code-editor-demo \
    --display-name "code-editor space" \
    --memory 8Gi \
    --template-ref name=sagemaker-code-editor-template,namespace=jupyter-k8s-system
```

You can modify the settings when creating the Space as well, see example below:

```
hyp create hyp-space \
    --name test-space \
    --display-name "test space" \
    --memory 8Gi \
    --volume name=vol,mountPath=/home/,persistentVolumeClaimName=pvcname
```

Once the Space is created, you can access the Space from either the web UI, or from your local VS Code. To open the Space in VS Code, run:

```
hyp create hyp-space-access \
    --name data-science-space \
    --connection-type vscode-remote
```

If you have set up the custom domain following our documentation, you can get the Space access URL as shown below. This will open your space on your browser.

```
hyp create hyp-space-access \
    --name data-science-space \
    --connection-type web-ui
```

Alternatively, you can connect to the Space from your local VS Code using the AWS toolkit. From your VS Code IDE, open the AWS toolkit panel. From the toolkit, under SageMaker AI, choose
**HyperPod**
. Here, you can list, start, stop, and connect to Spaces.

![Screenshot showing AWS Toolkit for VS Code and HyperPod Spaces](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/toolkit-for-vscode.png)

The Spaces need to be created using the HyperPod CLI or
`kubectl`
.

HyperPod CLI supports additional CRUD operations to Spaces such as updating, describing and deleting Spaces. For a list of the operations, see
[HyperPod CLI on Github](https://github.com/aws/sagemaker-hyperpod-cli)
.

For practitioners familiar with
`kubectl`
, they can also create, update and delete Spaces using
`kubectl`
. For example, you can create a Space using
`kubectl`
as shown below:

```
kubectl apply -f - <<EOF
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: training-workspace-1
  namespace: hyperpod-training-team
  labels:
    kueue.x-k8s.io/queue-name: hyperpod-ns-training-team-localqueue
    kueue.x-k8s.io/priority-class: ide-priority
spec:
  displayName: "Training Team Workspace 1"
  image: jupyter/minimal-notebook:latest
  desiredStatus: Running
  resources:
    requests:
      cpu: 3
      memory: 12Gi
    limits:
      cpu: 3
      memory: 12Gi
EOF
```

## Best practices

We recommend the following best practices when using SageMaker Spaces.

### User management, RBAC, and collaboration

SageMaker Spaces identifies users through Amazon EKS Access Entries, which are derived from your IAM identity when you interact with a Space using either the HyperPod CLI or kubectl. Your EKS captured identity may appear as an IAM user or as an assumed-role session ARN. For assumed roles, the session name can represent the actual user when admin applies
[IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_rolesessionname)
to enforce assumed role session names that reflect individual identities. If session names are not enforced or do not uniquely map to users, SageMaker Spaces access control falls back to role-based access control, causing all users sharing the same role to be treated as the same identity. For more details see
[Add users and set up service accounts](https://docs.aws.amazon.com/sagemaker/latest/dg/add-user.html)
.

Spaces can either be private, accessible only by the user who created the Spaces, or public, accessible by any user who has access to the hosting Kubernetes namespace. Spaces are public by default. The creator and the administrator group still retain full control, including the ability to update or delete the Space. A Space becomes private only when access is restricted to the creator and the admin group. This model gives teams a flexible foundation: public Spaces support open collaboration within a shared environment, while private Spaces provide isolation.

Multiple users can collaborate on the same Space if it is configured to be shared. When enabled with
[SageMaker Distribution](https://github.com/aws/sagemaker-distribution)
images for JupyterLab environments, we also support real time collaboration (RTC) which enables multiple users to collaborate on the interactive ML experiments and workloads.

### Admin defaults and controls

Templates set up by admins help data scientists quickly use pre-configured Space settings for their use case. SageMaker provides two pre-created system templates, one for JupyterLab and one for Code Editor, so that data scientists to get started without additional configurations needed. Admins can also set up custom templates for data scientists with custom configurations such as image, storage and compute.Templates can be used by data scientists in the cluster and are flexible depending on the needs of admins. Admins can create multiple templates based on specific use cases, projects, or dependency requirements.

### Customizing Spaces

Administrators and developers can customize their Spaces using custom images and lifecycle scripts. Use lifecycle scripts for minimal customization such as installing additional packages, setting up default variables, or running clean up tasks, while still using the SageMaker Distribution image capabilities. For organizations that have a standardized image for development and training, SageMaker Spaces also supports custom images and entry points for users. For custom image specifications, see
[Customization](https://docs.aws.amazon.com/sagemaker/latest/dg/customization.html)
.

### Shutdown idle compute

Spaces by default support automatic shutdown of idle workspaces to optimize resource usage. When idle shutdown is enabled, the system periodically checks the Space for activity and if the workspace is idle for the specified timeout duration, the workspace automatically stops, freeing up the compute resources for other tasks. Administrators can set default timeouts and optionally avoid overrides to defaults to enforce the idle shutdown.

### Integration with other HyperPod add-ons

For guardrails against excess resource usage, set up
[HyperPod task governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html)
, which provides comprehensive resource management controls. To help prevent workspaces from being evicted due to changes in unrelated workloads, configure task governance to set interactive ML workloads as the highest priority or schedule them in task governance namespaces with eviction turned off.

Set up the
[HyperPod Observability](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability.html)
plug in to monitor the resource usage of Spaces running within the cluster. With one click install, the observability plugin provides insight into how many resources Spaces are using over time, allowing admins to observe and tune their compute allocations.

### Fractional GPU support

SageMaker Spaces support fractional GPU configurations, specifically the
[MIG technology](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)
provided by NVIDIA GPUs. Fractional GPU support with MIG means that users can share GPU instances, optimizing compute usage, while still providing isolation between workloads. This means that experiments running on a fractional GPU profile are unlikely to interfere with other workloads running on the same GPU.

To check if an instance in your cluster supports fractional GPU, run the command:

```
hyp list-accelerator-partition-type --instance-type <instance type>
```

If your cluster contains instance groups that support fractional GPU, you can create a space with fractional GPU as shown below:

```
hyp create hyp-space \
    --name test-space \
    --display-name "mig-testing" \
    --accelerator-partition-type mig-3g.20gb \
    --accelerator-partition-count 1 \
    --memory 8Gi \
    --template-ref sagemaker-code-editor-template
```

## Clean up

To avoid incurring unnecessary charges, clean up the resources you created in this walkthrough.

1. Delete all spaces you created. Run this command for each space you created:

   ```
   hyp delete hyp-space \
   --name <space-name>
   ```
2. Remove the SageMaker HyperPod Spaces add-on: From the cluster details page, navigate to the
   **IDE and Notebooks**
   tab, and choose
   **Remove.**
3. If you created a HyperPod cluster for the purposes of this blog, delete the cluster to avoid being charged for unused compute. To delete the cluster, follow the instructions in
   [Deleting a SageMaker HyperPod cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-delete-cluster.html)
   . Additionally, if you used the console to create the cluster, go to the
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
   console and delete the parent stack to remove the additional resources such as storage and networking resources created for the cluster. The parent stack will be in the format
   `sagemaker-<your-hyperpod-cluster-name>-<unique-id>`

## Conclusion

Spaces in SageMaker HyperPod boosts data scientist and AI developer productivity by providing more secure, managed development environments on purpose-build compute. We walked through the setup steps for administrators and data scientists, showing how teams can quickly create and connect to Spaces. With this feature, teams can now reduce time spent on environment setup and focus on model development, while also maintaining consistent development environments. By integrating with HyperPod task governance features, administrators can optimize for cost and equitable compute allocations.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/surydurg-1.png)
**Durga Sury**
is a Senior Solutions Architect at Amazon SageMaker, helping enterprise customers build secure and scalable AI/ML systems. When she’s not architecting solutions, you can find her enjoying sunny walks with her dog, immersing herself in murder mystery books, or catching up on her favorite Netflix shows.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/sunp.png)
**Edward Sun**
is a Senior SDE working for SageMaker Studio at Amazon Web Services. He is focused on building interactive ML solutions and simplifying the customer experience to integrate SageMaker Studio with popular technologies in data engineering and ML landscape. In his spare time, Edward is big fan of camping, hiking, and fishing, and enjoys spending time with his family.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/joshua-dunne.png)
**Josh Dunne**
is a Senior UX Designer at SageMaker AI at Amazon Web Services. He has 7+ years of experience across UX and product management, with a focus on ML/AI and cloud computing creating practical, straightforward to use workflows for machine learning builders across SageMaker AI, including HyperPod, SageMaker Studio, SageMaker Unified Studio, and interactive IDEs.  Outside of work, he enjoys exploring the Pacific Northwest and traveling with his wife and their dog and trying new restaurants.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/joshua-towner.png)
**Joshua Towner**
is a Senior SDE working for SageMaker AI at Amazon Web Services, where he is currently working on building and improving interactive ML solutions for SageMaker Studio and HyperPod. Outside of work, he enjoys traveling, skiing, and watching movies.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/khushbsr.png)
**Khushboo Srivastava**
is a Product Manager for Amazon SageMaker, AWS. She enjoys building products that simplify machine learning workflows for users. With over 7+ years in software engineering and data science, and 7+ years in product management, Khushboo has launched several products and services that have helped accelerate speed of AI/ML development for customers. With her background in generative AI and distributed computing, and her passion for democratizing AI, she is committed to sharing insights and empowering others in their AI and open source journey.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/prayag.png)
**Prayag Singh**
is a Senior SDE working for SageMaker AI at Amazon Web Services. With 10+ years of software development experience, he focuses on integrating customers’ preferred ML tools and IDEs on SageMaker Studio and HyperPod. Outside of work, Prayag enjoys traveling and all things comedy, from stand-up specials to sitcoms. You can find him on
[LinkedIn](https://www.linkedin.com/in/prayag21/)
.