---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-21T18:15:42.408517+00:00'
exported_at: '2026-04-21T18:15:44.913465+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/end-to-end-lineage-with-dvc-and-amazon-sagemaker-ai-mlflow-apps
structured_data:
  about: []
  author: ''
  description: In this post, we show how to combine DVC (Data Version Control), Amazon
    SageMaker AI, and Amazon SageMaker AI MLflow Apps to build end-to-end ML model
    lineage. We walk through two deployable patterns — dataset-level lineage and record-level
    lineage — that you can run in your own AWS account using the companion noteb...
  headline: End-to-end lineage with DVC and Amazon SageMaker AI MLflow apps
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/end-to-end-lineage-with-dvc-and-amazon-sagemaker-ai-mlflow-apps
  publisher:
    logo: /favicon.ico
    name: GTCode
title: End-to-end lineage with DVC and Amazon SageMaker AI MLflow apps
updated_at: '2026-04-21T18:15:42.408517+00:00'
url_hash: d63458a24b22f5459a3822753efe5e2e0b7a19db
---

Production machine learning (ML) teams struggle to trace the full lineage of a model through the data and the code that trained it, the exact dataset version it consumed, and the experiment metrics that justified its deployment. Without this traceability, questions like “which data trained the model currently in production?” or “can we reproduce the model we deployed six months ago?” become multi-day investigations through scattered logs, notebooks, and Amazon Simple Storage Service (Amazon S3) buckets. This gap is especially acute in regulated industries. For example, healthcare, financial services, autonomous vehicles, where audit requirements demand that you link deployed models to their precise training data, and where individual records might need to be excluded from future training on request.

In this post, we show how to combine three tools to close this gap:

We walk through two deployable patterns, dataset-level lineage and record-level lineage, that you can run end-to-end in your own AWS account using the
[companion notebooks](https://github.com/aws-samples/sample-amazon-sagemaker-mlflow-dvc-lineage/)
.

## Solution overview

The architecture integrates DVC, SageMaker AI, and SageMaker AI MLflow App into a single workflow where every model is traceable back to its exact training data.

![This diagram illustrates an end-to-end machine learning workflow on AWS that enables ML traceability by integrating Data Version Control (DVC) and MLflow with Amazon SageMaker, showing how data flows from preprocessing through model training to deployment across nine sequential steps. The architecture demonstrates how versioned datasets are managed through S3 and CodeCommit, training experiments are tracked via MLflow, and models are ultimately deployed to SageMaker endpoints for production serving.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/13/ML-20309-image1.jpg)

Each tool plays a distinct role:

|  |  |  |
| --- | --- | --- |
| **Tool** | **Role** | **What it stores** |
| DVC | Data and artifact versioning | Lightweight `.dvc` metafiles in Git; actual data in Amazon S3 |
| Amazon SageMaker AI | Scalable compute for processing, training, and hosting | Processing/Training job orchestration and model Hosting |
| Amazon SageMaker AI MLflow App | Experiment tracking, model registry, lineage | Parameters, metrics, artifacts, registered models |

The data flows through four stages:

1. A SageMaker AI Processing job preprocesses raw data and versions the processed dataset with DVC, pushing the data to S3 and metadata to a Git repository.
2. A SageMaker AI Training job clones the DVC repository at a specific Git tag, runs
   `dvc pull`
   to retrieve the exact versioned dataset, trains the model, and logs everything to MLflow.
3. Every MLflow training run records the
   `data_git_commit_id`
   , which is the DVC commit hash that points to the exact dataset in Amazon S3.
4. The trained model is registered in the MLflow Model Registry and can be deployed to a SageMaker AI endpoint.

This creates a complete traceability chain: Production Model → MLflow Run → DVC commit → exact dataset in Amazon S3.

## Prerequisites

You must have the following prerequisites to follow along with this post:

* An AWS account with permissions for Amazon SageMaker (Processing, Training, MLflow Apps, Endpoints), Amazon S3, AWS CodeCommit, and AWS Identity Access Management (IAM).
* Python 3.11 or Python 3.12.
* The
  [SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk)
  v3.4.0 or later.

The
[companion repository](https://github.com/aws-samples/sample-amazon-sagemaker-mlflow-dvc-lineage/)
includes a
`requirements.txt`
with all dependencies. If running outside SageMaker Studio, your IAM role must have a trust relationship allowing
`sagemaker.amazonaws.com`
to assume it.

> ***Note on Git providers:**
> The notebooks use AWS CodeCommit as the Git backend for DVC metadata. However, DVC works with other Git providers (GitHub, GitLab, Bitbucket). All you need to do is replace the
> `git remote add origin`
> URL and configure appropriate credentials. For example, by storing tokens in
> [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
> and fetching them at runtime or by using
> [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html)
> . The key requirement is that your SageMaker AI execution role can access the Git repository or has permissions to use AWS CodeConnections.*

## How DVC and SageMaker AI MLflow work together

The key insight behind this architecture is that DVC and MLflow each solve half of the lineage problem, and together they close the loop.

[**DVC (Data Version Control)**](https://dvc.org/)
is a no cost, open source tool that extends Git to handle large datasets and ML artifacts. Git alone can’t manage large binary files because repositories become bloated and slow, and systems like GitHub block files over 100 MB. DVC addresses this through codification: it tracks lightweight
`.dvc`
metafiles in Git (content-addressable pointers) while the actual data lives in remote storage such as Amazon S3. This gives you Git-like versioning semantics (branching, tagging, diffing) for datasets that can be gigabytes or terabytes in size, without bloating your repository.

> **Storage efficiency:**
>
> *DVC uses
> [content-addressable storage](https://dvc.org/doc/user-guide/project-structure/internal-files#files)
> (MD5 hashes), so it stores only new or modified files rather than duplicating entire datasets. Files with identical contents are stored only once in the DVC cache, even if they appear under different names or across different dataset versions. For example, adding 1,000 new images to an existing dataset only uploads those new files to S3. The unchanged files aren’t re-uploaded. However, if a preprocessing step modifies existing files, the affected files get new hashes and are stored as new objects.*

Beyond data versioning, DVC also supports reproducible
[data pipelines](https://dvc.org/doc/start/data-pipelines)
,
[experiment management](https://dvc.org/doc/user-guide/experiment-management)
, and can serve as a
[data registry](https://dvc.org/doc/use-cases/data-registry)
for sharing datasets across teams. In this architecture, we use DVC specifically for its data versioning capability. Every time you version a dataset with
`dvc add`
and commit the resulting
`.dvc`
file, you create a Git commit that maps to a specific dataset state. Tagging that commit gives you a stable reference you can return to with
`git checkout <tag> && dvc pull`
. For a deeper dive into DVC’s versioning capabilities, see the
[Versioning Data and Models](https://dvc.org/doc/use-cases/versioning-data-and-models)
guide.

[SageMaker AI MLflow App](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
is a fully managed AWS service offered within SageMaker AI Studio, for managing the end-to-end ML and generative AI lifecycle. Its core capabilities include experiment tracking (logging parameters, metrics, and artifacts for every training run), a model registry with versioning and lifecycle stage management, model evaluation, and deployment integrations. In this post’s architecture, we use MLflow for full experiment tracking including DVC results and the model registry. By logging the DVC commit hash as a parameter (
`data_git_commit_id`
) on every training run, we create the bridge: models in the MLflow registry can be traced back to the exact Git tag, which maps to the exact dataset in S3.

While DVC can handle both data versioning and experiment tracking on its own, MLflow brings a more mature model registry with model versioning, aliases for lifecycle management, and deployment integrations. By using DVC for data versioning and MLflow for model lifecycle management, we get a clean separation of concerns: DVC owns the data-to-training lineage, MLflow owns the training-to-deployment lineage, and the Git commit hash ties them together.

## Pattern one: Dataset-level lineage (foundational)

Before building the integration, it’s essential to understand how DVC’s dataset versioning and MLflow’s run tracking complement each other in forming a full lineage. The foundational notebook demonstrates the core pattern by simulating a common scenario: starting with limited labeled data and expanding over time.

### The workflow

The notebook runs two experiments using the CIFAR-10 image classification dataset:

* **v1.0**
  : Process and train with 5% of the data (~2,250 training images)
* **v2.0**
  : Process and train with 10% of the data (~4,500 training images)

For each version, the same two-step pipeline executes:

**Step 1 — Processing job**
: A SageMaker Processing job downloads CIFAR-10, samples the configured fraction, splits into train/validation/test sets, saves images in ImageFolder format, and versions the result with DVC. The processed dataset is pushed to S3 via
`dvc push`
, and the Git metadata (including a unique tag like
`v1.0-02-24-26_1430`
) is pushed to CodeCommit.

The processing job receives the DVC repository URL and MLflow tracking URI as environment variables:

```
processor_v1 = FrameworkProcessor(
    image_uri=processing_image,
    role=role,
    instance_type="ml.m5.xlarge",
    instance_count=1,
    env={
        "DVC_REPO_URL": dvc_repo_url,
        "DVC_REPO_NAME": dvc_repo_name,
        "MLFLOW_TRACKING_URI": mlflow_app_arn,
        "MLFLOW_EXPERIMENT_NAME": experiment_name,
        "PIPELINE_RUN_ID": pipeline_run_id_v1,
    }
)

processor_v1.run(
    code="preprocessing_foundational.py",
    source_dir="../source_dir",
    arguments=[
        "--data-fraction", str(data_fraction_v1),
        "--data-version", data_version_v1,
        "--val-split", "0.1"
    ],
    wait=True
)
```

Inside the processing script, after preprocessing, the dataset is versioned with DVC and the commit hash is logged to MLflow:

```
def version_with_dvc(repo_path, version_tag, pipeline_run_id):
    """Add data to DVC and push to remote."""
    subprocess.check_call(["dvc", "add", "dataset"], cwd=repo_path)
    subprocess.check_call(["git", "add", "dataset.dvc", ".gitignore"], cwd=repo_path)
    subprocess.check_call(
        ["git", "commit", "-m", f"Add dataset version {version_tag}"],
        cwd=repo_path
    )
    subprocess.check_call(["git", "tag", pipeline_run_id], cwd=repo_path)

    subprocess.check_call(["dvc", "push"], cwd=repo_path)
    subprocess.check_call(["git", "push", "origin", "main"], cwd=repo_path)
    subprocess.check_call(["git", "push", "origin", pipeline_run_id], cwd=repo_path)

    commit_id = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repo_path
    ).decode().strip()
    return commit_id
```

**Step 2 — Training job**
: A SageMaker AI Training job clones the DVC repository at the exact tag from Step 1, runs
`dvc pull`
to download the versioned dataset, and fine-tunes a pretrained MobileNetV3-Small model. The training script logs the parameters (including the DVC commit hash), per-epoch metrics, and the trained model to MLflow. The model is automatically registered in the MLflow Model Registry.

The critical lineage bridge (logging the DVC commit hash to MLflow), happens in the training script:

```
# Fetch data: clone DVC repo at the exact tag, then dvc pull
data_git_commit_id = fetch_data_from_dvc()

with mlflow.start_run(run_name=run_name) as run:
    mlflow.log_params({
        "data_version": data_version,
        "data_git_commit_id": data_git_commit_id,  # <-- the lineage bridge
        "dvc_repo_url": dvc_repo_url,
        "model_architecture": "mobilenet_v3_small",
        "epochs": args.epochs,
        "learning_rate": args.learning_rate,
        # ...
    })
```

### What you see in MLflow

After both experiments complete, the MLflow UI shows both runs side-by-side, as shown in the following screenshot. In the MLflow experiment, you can compare:

* Training and validation accuracy curves across data versions
* The exact hyperparameters and data version for each run
* The
  `data_git_commit_id`
  that links each model to its DVC dataset

![This MLflow experiment tracking dashboard displays model performance metrics for a CIFAR-10 machine learning experiment, comparing two model versions (v1.0 and v2.0) across six visualization charts including final training accuracy, validation accuracy, training accuracy over steps, and loss metrics. The interface shows grouped experiment runs with filtering capabilities and real-time metric comparisons, demonstrating how MLflow enables comprehensive experiment tracking and model performance analysis for machine learning workflows.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/13/ML-20309-image2.jpg)

Selecting into a run shows the full detail, loss curves, parameters, and the DVC commit linking to the exact dataset in S3, as shown in the following screenshot.

![This MLflow run details page shows comprehensive tracking information for a CIFAR-10 training experiment (train-v2.0-01-28-26_1445), including six model metrics such as validation accuracy (0.77) and training loss, along with twelve parameters like data version (v2.0) and model architecture (mobilenet_v3_small). The interface displays complete experiment metadata including run duration (2.3min), registered model (CIFAR10-MobileNetV3 v4), and Git commit information, demonstrating MLflow's capability for full ML experiment reproducibility and traceability.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/13/ML-20309-image3.jpg)

Finally, trained artificial intelligence and machine learning (AI/ML) Models are automatically registered in the MLflow Model Registry with version history and links to the training run that produced them, as shown in the following screenshot. Furthermore, with SageMaker AI MLflow App integrated with SageMaker AI Model Registry, the MLflow automatically logs the registered model into SageMaker AI Model Registry.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/13/ML-20309-image4.jpg)

### Deploying the model

The notebook deploys the recommended model (v2.0, trained on more data) from the MLflow Model Registry to a SageMaker AI real-time endpoint using
`ModelBuilder`
. After deployed, you can invoke the endpoint with raw image bytes and get back class predictions. The full deployment and inference code is in the notebook.

### What this pattern answers

With dataset-level lineage, you can answer:

* *“Which dataset version trained this model?”*
  — Look up the
  `data_git_commit_id`
  in the MLflow run
* *“Can I reproduce this model’s training data?”*
  — Run
  `git checkout <tag> && dvc pull`
  to restore the exact dataset
* *“Why did model performance change?”*
  — Compare runs in MLflow and trace each to its data version

What it
*doesn’t*
answer without extra work:
*“Was record X in this model’s training data?”*
You’d need to pull the full dataset and search through it. That’s where Pattern two comes in.

## Pattern two: Record-level lineage (healthcare compliance)

Pattern 2 builds directly on the dataset-level approach, adding record/patient-level traceability through manifests and consent registries. The example healthcare compliance notebook extends the foundational pattern for regulated environments where you need to trace individual records, not only datasets, through the ML lifecycle.

### The key addition: a manifest

The difference is a manifest. A manifest is a structured CSV listing every individual record in each dataset version:

```
patient_id,scan_id,file_path,split,label
PAT-00001,PAT-00001-SCAN-0001,train/normal/00042.png,train,normal
PAT-00023,PAT-00023-SCAN-0015,train/tubercolosis/00015.png,train,tubercolosis
...
```

This manifest is saved inside the DVC-versioned dataset directory
*and*
logged as an MLflow artifact on every training run. This makes individual records queryable directly from MLflow without pulling the full dataset from DVC.

### The consent registry

The workflow is driven by a
**consent registry**
, which is a CSV file listing each patient and their consent status. In production, this would be a database with transactional commitments, its own audit trail, and potentially event-driven triggers to initiate re-training. The CSV approach here is streamlined for demonstration purposes, but the integration pattern is the same: the processing job reads the registry and only includes records with active consent.

The processing code is idempotent. It doesn’t know or care about opt-outs, it filters for
`consent_status == "active"`
and processes whatever remains. An opt-out is an input change that produces a new, clean dataset when the same pipeline runs again.

### The opt-out workflow

The notebook demonstrates a complete opt-out cycle:

1. **v1.0 — Baseline**
   – Process and train with all consented patients. The manifest lists the patience scans. The model is registered in MLflow with the manifest as an artifact.
2. **Opt-out event**
   – Patient
   `PAT-00023`
   requests to opt out. Their consent status is updated to
   `revoked`
   in the registry, and the updated registry is uploaded to S3.
3. **v2.0 — Clean dataset**
   – The
   *same*
   processing job runs with the updated registry.
   `PAT-00023`
   ‘s images are automatically excluded. DVC versions the new dataset (137 patients). The model is retrained and registered as a new version in MLflow.
4. **Audit verification**
   – Query MLflow to confirm
   `PAT-00023`
   appears only in the v1.0 model and is absent from models trained after the opt-out date.

### Audit queries

The companion
`utils/audit_queries.py`
module provides three query functions that work by downloading manifest artifacts from MLflow:

* `find_models_with_patient("PAT-00023")`
  — Searches the training runs for a patient ID. Returns only the v1.0 run.
* `verify_patient_excluded_after_date("PAT-00023", "2025-06-01")`
  — Checks the models trained after a date and confirms that the patient is absent. Returns PASSED or FAILED with details.
* `get_patients_in_model(run_id)`
  — Lists the patient IDs in a specific model’s training data.

```
from utils.audit_queries import find_models_with_patient

# "Which models were trained on this patient's data?"
find_models_with_patient("PAT-00023", experiment_name="demo-cxr-mlflow-dvc")
```

These queries don’t require a DVC checkout — they operate entirely on MLflow artifacts, making them fast enough for interactive audit responses.

**Production note:**
The previous queries download the
`manifest.csv`
artifact from every training run and scan it. This works for a handful of runs but doesn’t scale. In production, consider writing (
`record_id`
,
`run_id`
,
`data_version`
) tuples to Amazon DynamoDB at training time, pointing Amazon Athena at the MLflow artifact prefix in S3, or using a post-training AWS Lambda to populate an index.

### What this pattern answers

Beyond everything the foundational pattern provides, record-level lineage answers:

* *“Which models were trained using patient X’s scans?”*
  — Instant query across MLflow runs
* *“Verify that patient X was excluded from all models after their opt-out date”*
  — Automated pass/fail audit
* *“List every record in model Y’s training data”*
  — Download the manifest artifact

While this demo uses healthcare terminology, the pattern applies to other domains requiring record-level traceability: financial services, content moderation (user-submitted content), or other ML systems subject to data deletion requests.

## Best practices and governance

### The three-layer traceability chain

The integrated workflow creates traceability at three levels:

1. **Git + DVC layer**
   – Every dataset version is a Git tag pointing to a DVC commit. Running
   `git checkout <tag> && dvc pull`
   restores the exact processed data.
2. **MLflow layer**
   – Every training run records the
   `data_git_commit_id`
   , linking the model to its DVC data version. The record-level manifest (when used) makes individual records queryable.
3. **Model Registry layer**
   – Every registered model version links to its training run, which links to its data version.

### Security considerations for regulated environments

DVC and MLflow provide traceability and experiment tracking but aren’t tamper-evident on their own. For regulated deployments (HIPAA, FDA 21 CFR Part 11, GDPR), layer on infrastructure-level controls:

* **S3 Object Lock**
  (compliance mode) on DVC remotes and MLflow artifact stores to avoid modification or deletion of versioned data and model artifacts
* **AWS CloudTrail**
  for independent, append-only logging of access to storage and training infrastructure
* **IAM policies**
  enforcing least-privilege access to production buckets, MLflow tracking servers, and Git repositories
* **Encryption at rest**
  using AWS Key Management Service (AWS KMS) for S3 buckets storing DVC data and MLflow artifacts

### Speeding up iteration

When running repeated experiments (like the v1.0 → v2.0 flow), two SageMaker AI features help streamline the process:

* [**SageMaker Managed Warm Pools**](https://docs.aws.amazon.com/sagemaker/latest/dg/train-warm-pools.html)
  — Keep training instances warm between jobs so back-to-back training runs reuse already-provisioned infrastructure. Add
  `keep_alive_period_in_seconds`
  to your
  `Compute`
  config to enable it. Note that warm pools apply to training jobs only, not processing jobs.
* [**SageMaker AI Pipelines**](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-overview.html)
  — Orchestrate the processing → training → registration workflow as a single, repeatable pipeline. Pipelines handle step dependencies, pass artifacts between steps automatically, and can be triggered programmatically (for example, when a patient opts out and the manifest is updated).

## Cleanup

To avoid ongoing charges, delete the resources created during the walkthrough: the SageMaker AI endpoint, the MLflow App (optional), the AWS CodeCommit repository, and the S3 data. The notebooks include cleanup cells with the exact commands. The primary cost driver is the SageMaker AI real-time endpoint. Make sure to delete it promptly after testing.

## Conclusion

In this post, we demonstrated how to build an end-to-end MLOps workflow that combines DVC for data versioning, Amazon SageMaker AI for scalable training and orchestration, and SageMaker AI MLflow Apps for experiment tracking and model registry.The key outcomes:

* **Full reproducibility**
  – Models can be traced back to its exact training data via DVC commit hashes stored in MLflow.
* **Record-level lineage**
  – The manifest pattern enables querying which individual records trained a given model. This is critical for opt-out compliance and audit responses.
* **Stateless compliance alignment**
  – The consent registry pattern handles record exclusion without changing processing code. An opt-out is an input change that flows through the same pipeline.
* **Experiment comparison**
  – MLflow provides side-by-side comparison of models trained on different data versions, with full parameter and metric tracking.

The two notebooks in the
[companion GitHub repository](https://github.com/aws-samples/sample-amazon-sagemaker-mlflow-dvc-lineage/)
are deployable as-is. The foundational pattern suits teams that need dataset-level traceability. The healthcare compliance pattern extends it for regulated environments requiring record-level audit trails. Both share the same SageMaker AI training code and architecture.

While the notebooks demonstrate an interactive workflow, the same pattern integrates directly into automated pipelines. SageMaker AI Pipelines can orchestrate the processing and training steps, with DVC tagging and MLflow logging happening identically inside each job. The lineage chain remains the same whether triggered from a notebook or a SageMaker AI Pipeline.

---

## About the authors

### Manuwai Korber

Manuwai Korber is an AI/ML Specialist Solutions Architect at AWS with a background in ML engineering. He helps customers architect production-grade AI/ML systems across the full model lifecycle — from experimentation, training and fine-tuning through to serving and production deployment. In addition, building GenAI-powered applications and agentic AI systems.

### Paolo Di Francesco

Paolo Di Francesco is a Senior Solutions Architect at Amazon Web Services (AWS). He holds a PhD in Telecommunications Engineering and has experience in software engineering. He is passionate about machine learning and is currently focusing on using his experience to help customers reach their goals on AWS, in discussions around MLOps. Outside of work, he enjoys playing football and reading.

### Sandeep Raveesh

Sandeep Raveesh is a GenAI Specialist Solutions Architect at AWS. He works with customer through their AIOps journey across model training, Retrieval-Augmented-Generation(RAG), GenAI Agents, and scaling GenAI use-cases. He also focuses on Go-To-Market strategies helping AWS build and align products to solve industry challenges in the Generative AI space. You can find Sandeep on
[LinkedIn](https://www.linkedin.com/in/sandeep-raveesh-750aa630/)
.

### Nick McCarthy

Nick McCarthy is a Senior Generative AI Specialist Solutions Architect on the Amazon Bedrock team, focused on model customization. He has worked with AWS clients across a wide range of industries — including healthcare, finance, sports, telecommunications, and energy — helping them accelerate business outcomes through the use of AI and machine learning. Outside of work, Nick loves traveling, exploring new cuisines, and reading about science and technology. He holds a Bachelor’s degree in Physics and a Master’s degree in Machine Learning.