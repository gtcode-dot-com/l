---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-12T22:51:26.361771+00:00'
exported_at: '2025-11-12T22:54:41.520375+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/fine-tune-vlms-for-multipage-document-to-json-with-sagemaker-ai-and-swift
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate that fine-tuning VLMs provides a powerful
    and flexible approach to automate and significantly enhance document understanding
    capabilities. We also demonstrate that using focused fine-tuning allows smaller,
    multi-modal models to compete effectively with much larger counterparts (98% accuracy
    with Qwen2.5 VL 3B).
  headline: Fine-tune VLMs for multipage document-to-JSON with SageMaker AI and SWIFT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/fine-tune-vlms-for-multipage-document-to-json-with-sagemaker-ai-and-swift
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fine-tune VLMs for multipage document-to-JSON with SageMaker AI and SWIFT
updated_at: '2025-11-12T22:51:26.361771+00:00'
url_hash: ca8a2fc0859149bc725be1d682e89028c71035dc
---

Extracting structured data from documents like invoices, receipts, and forms is a persistent business challenge. Variations in format, layout, language, and vendor make standardization difficult, and manual data entry is slow, error-prone, and unscalable. Traditional optical character recognition (OCR) and rule-based systems often fall short in handling this complexity. For instance, a regional bank might need to process thousands of disparate documents—loan applications, tax returns, pay stubs, and IDs—where manual methods create bottlenecks and increase the risk of error. Intelligent document processing (IDP) aims to solve these challenges by using AI to classify documents, extract or derive relevant information, and validate the extracted data to use it in business processes. One of its core goals is to convert unstructured or semi-structured documents into usable, structured formats such as JSON, which then contain specific fields, tables, or other structured target information. The target structure needs to be consistent, so that it can be used as part of workflows or other downstream business systems or for reporting and insights generation. The following figure shows the workflow, which involves ingesting unstructured documents (for example, invoices from multiple vendors with varying layouts) and extracting relevant information. Despite differences in keywords, column names, or formats across documents, the system normalizes and outputs the extracted data into a consistent, structured JSON format.

![Intelligent Document Processing - High-level Flow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/22/image-1-17.png)

Vision language models (VLMs) mark a revolutionary advancement in IDP. VLMs integrate large language models (LLMs) with specialized image encoders, creating truly multi-modal AI capabilities of both textual reasoning and visual interpretation. Unlike traditional document processing tools, VLMs process documents more holistically—simultaneously analyzing text content, document layout, spatial relationships, and visual elements in a manner that more closely resembles human comprehension. This approach enables VLMs to extract meaning from documents with unprecedented accuracy and contextual understanding. For readers interested in exploring the foundations of this technology, Sebastian Raschka’s post—
[Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
—offers an excellent primer on multimodal LLMs and their capabilities.

This post has four main sections that reflect the primary contributions of our work and include:

1. An overview of the various IDP approaches available, including the option (our recommended solution) for fine-tuning as a scalable approach.
2. Sample code for fine-tuning VLMs for document-to-JSON conversion using
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/?trk=8987dd52-6f33-407a-b89b-a7ba025c913c&sc_channel=ps&ef_id=Cj0KCQjwuvrBBhDcARIsAKRrkjevNzXg2uCJ93x5136rcpMugrGTOuKkRQ-bmeIEFWY1YSIK443MBoMaAq3bEALw_wcB:G:s&s_kwcid=AL!4422!3!724218586004!e!!g!!amazon%20sagemaker%20ai!11206038603!174643422154&gad_campaignid=11206038603&gclid=Cj0KCQjwuvrBBhDcARIsAKRrkjevNzXg2uCJ93x5136rcpMugrGTOuKkRQ-bmeIEFWY1YSIK443MBoMaAq3bEALw_wcB)
   and the
   [SWIFT](https://github.com/modelscope/ms-swift)
   framework, a lightweight toolkit for fine-tuning various large models.
3. Developing an evaluation framework to assess performance processing structured data.
4. A discussion of the possible deployment options, including an explicit example for deploying the fine-tuned adapter.

SageMaker AI is a fully managed service to build, train and deploy models at scale. In this post, we use SageMaker AI to fine-tune the VLMs and deploy them for both batch and real-time inference.

## Prerequisites

Before you begin, make sure you have the following set up so that you can successfully follow the steps outlined in this post and the accompanying GitHub repository:

1. **AWS account:**
   You need an active AWS account with permissions to create and manage resources in SageMaker AI,
   [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
   , and
   [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/)
   .
2. **IAM permissions:**
   Your IAM user or role must have sufficient permissions. For production setups, follow the principle of least privilege as described in
   [security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
   . For a sandbox setup we suggest the following roles:
   * Full access to Amazon SageMaker AI (for example,
     `AmazonSageMakerFullAccess`
     ).
   * Read/write access to S3 buckets for storing datasets and model artifacts.
   * Permissions to push and pull Docker images from Amazon ECR (for example,
     `AmazonEC2ContainerRegistryPowerUser`
     ).
   * If using specific SageMaker instance types, make sure your service quotas are sufficient.
3. **GitHub repository:**
   Clone or download the project code from our
   [GitHub repository](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/tree/main?tab=readme-ov-file)
   . This repository contains the notebooks, scripts, and Docker artifacts referenced in this post.
   * ```
     git clone https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai.git
     ```
4. **Local environment set up:**
   * **Python:**
     Python 3.10 or higher is recommended.
   * **AWS CLI:**
     Make sure the
     [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli)
     is installed and configured with credentials that have the necessary permissions.
   * **Docker:**
     Docker must be installed and running on your local machine if you plan to build the custom Docker container for deployment.
   * **Jupyter Notebook and Lab:**
     To run the provided notebooks.
   * Install the required Python packages by running
     `pip install -r requirements.txt`
     from the cloned repository’s root directory.
5. **Familiarity (recommended):**
   * Basic understanding of Python programming.
   * Familiarity with AWS services, particularly SageMaker AI.
   * Conceptual knowledge of LLMs, VLMs, and the container technology will be beneficial.

## Overview of document processing and generative AI approaches

There are varying degrees of autonomy in intelligent document processing. On one end of the spectrum are fully manual processes: Humans manually reading documents and entering the information into a form using a computer system. Most systems today are semi-autonomous document processing solutions. For example, a human taking a picture of a receipt and uploading it to a computer system that automatically extracts part of the information. The goal is to get to fully autonomous intelligent document processing systems. This means reducing the error rate and assessing the use case specific risk of errors. AI is significantly transforming document processing by enabling greater levels of automation. A variety of approaches exist, ranging in complexity and accuracy—from specialized models for OCR, to generative AI.

Specialized OCR models that don’t rely on generative AI are designed as pre-trained, task-specific ML models that excel at extracting structured information such as tables, forms, and key-value pairs from common document types like invoices, receipts, and IDs.
[Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)
is one example of this type of service. This service offers high accuracy out of the box and requires minimal setup, making it well-suited for workloads where basic text extraction is required, and documents don’t vary significantly in structure or contain images.

However, as you increase the complexity and variability of documents, in addition to adding multimodality, using generative AI can help improve document processing pipelines.

While powerful, applying general-purpose VLMs or LLMs to document processing isn’t straightforward. Effective
*prompt engineering*
is important to guide the model. Processing large volumes of documents (scaling) requires efficient batching and infrastructure. Because LLMs are stateless, providing historical context or specific schema requirements for every document can be cumbersome.

Approaches to intelligent document processing that use LLMs or VLMs fall into four categories:

* **Zero-shot prompting**
  : the foundation model (FM) receives the result of previous OCR or a PDF and the instructions to perform the document processing task.
* **Few-shot prompting**
  : the FM receives the result of previous OCR or a PDF, the instructions to perform the document processing task, and some examples.
* **Retrieval-augmented few-shot prompting**
  : similar to the preceding strategy, but the examples sent to the model are selected dynamically using Retrieval Augmented Generation (RAG).
* **Fine-tuning VLMs**

In the following, you can see the relationship between increasing effort and complexity and task accuracy, demonstrating how different techniques—from basic prompt engineering to advanced fine-tuning—impact the performance of large and small base models compared to a specialized solution (inspired by the blog post
[Comparing LLM fine-tuning](https://www.signalfire.com/blog/comparing-llm-fine-tuning-methods)
methods)

![Fine-tuning methods by complexity](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/22/image-2-14.png)

As you move across the horizontal axis, the strategies grow in complexity, and as you move up the vertical axis, you improve overall accuracy. In general, large base models provide better performance than small base models in the strategies that require prompt engineering, however as we explain in the results of this post, fine-tuning small base models can deliver similar results as fine-tuning large base models for a specific task.

### Zero-shot prompting

Zero-shot prompting is a technique to use language models where the model is given a task without prior examples or fine-tuning. Instead, it relies solely on the prompt’s wording and its pre-trained knowledge to generate a response. In document processing, this approach involves giving the model either an image of a PDF document, the OCR-extracted text from the PDF, or a structured markdown representation of the document and providing instructions to perform the document processing task, in addition to the desired output format.

[Amazon Bedrock Data Automation](https://aws.amazon.com/blogs/machine-learning/simplify-multimodal-generative-ai-with-amazon-bedrock-data-automation/)
uses zero-shot prompting with generative AI to perform IDP. You can use Bedrock Data Automation to automate the transformation of multi-modal data—including documents containing text and complex structures, such as tables, charts and images—into structured formats. You can benefit from customization capabilities through the creation of blueprints that specify output requirements using natural language or a schema editor. Bedrock Data Automation can also extract bounding boxes for the identified entities and route documents appropriately to the correct blueprint. These features can be configured and used through a single API, making it significantly more powerful than a basic zero-shot prompting approach.

While out-of-the-box VLMs can handle general OCR tasks effectively, they often struggle with the unique structure and nuances of custom documents—such as invoices from diverse vendors. Although crafting a prompt for a single document might be straightforward, the variability across hundreds of vendor formats makes prompt iteration a labor-intensive and time-consuming process.

### Few-shot prompting

Moving to a more complex approach, you have few-shot prompting, a technique used with LLMs where a small number of examples are provided within the prompt to guide the model in completing a specific task. Unlike zero-shot prompting, which relies solely on natural language instructions, few-shot prompting improves accuracy and consistency by demonstrating the desired input-output behavior through examples.

One alternative is to use the
[Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html)
to perform few shot prompting. Converse API provides a consistent way to access LLMs using Amazon Bedrock. It supports turn-based messages between the user and the generative AI model, and allows including
[documents](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html)
as part of the content. Another option is using
[Amazon SageMaker Jumpstart](https://aws.amazon.com/sagemaker/ai/jumpstart/)
, which you can use to deploy models from providers like
[HuggingFace](https://huggingface.co/)
.

However, most likely your business needs to process different types of documents (for example, invoices, contracts and hand written notes) and even within one document type there are many variations, for example, there is not one standardized invoice layout and instead each vendor has their own layout that you cannot control. Finding a single or a few examples that cover all the different documents you want to process is challenging.

### Retrieval-augmented few-shot prompting

One way to address the challenge of finding the right examples is to dynamically retrieve previously processed documents as examples and add them to the prompt at runtime (RAG).

You can store a few annotated samples in a vector store and retrieve them based on the document that needs to be processed.
[Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
helps you implement the entire RAG workflow from ingestion to retrieval and prompt augmentation without having to build custom integrations to data sources and manage data flows.

This turns the intelligent document processing problem into a search problem, which comes with its own challenges on how to improve the accuracy of the search. In addition to how to scale for multiple types of documents, the few-shot approach is costly because every document processed requires a longer prompt with examples. This results in an increased number of input tokens.

![Intelligent Document Procesing Strategies](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/22/image-3-10.png)

As shown in the preceding figure, the prompt context will vary based on the strategy selected (zero-shot, few-shot or few-shot with RAG), which will overall change the results obtained.

### Fine-tuning VLMs

At the end of the spectrum, you have the option to fine-tune a custom model to perform document processing. This is our recommended approach and what we focus on in this post. Fine-tuning is a method where a pre-trained LLM is further trained on a specific dataset to specialize it for a particular task or domain. In the context of document processing, fine-tuning involves using labeled examples—such as annotated invoices, contracts, or insurance forms—to teach the model exactly how to extract or interpret relevant information. Usually, the labor-intensive part of fine-tuning is acquiring a suitable, high-quality dataset. In the case of document processing, your company probably already has a historic dataset in its existing document processing system. You can export this data from your document processing system (for example from your enterprise resource planning (ERP) system) and use it as the dataset for fine-tuning. This fine-tuning approach is what we focus on in this post as a scalable, high accuracy, and cost-effective approach for intelligent document processing.

The preceding approaches represent a spectrum of strategies to improve LLM performance along two axes:
**LLM optimization**
(shaping model behavior through prompt engineering or fine-tuning) and
**context optimization**
(enhancing what the model knows at inference through techniques such as few-shot learning or RAG). These methods can be combined—for example, using RAG with few-shot prompts or incorporating retrieved data into fine-tuning—to maximize accuracy.

## Fine-tuning VLMs for document-to-JSON conversion

Our approach—the recommended solution for cost-effective document-to-JSON conversion—uses a VLM and fine-tunes it using a dataset of historical documents paired with their corresponding ground-truth JSON that we consider as annotations. This allows the model to learn the specific patterns, fields, and output structure relevant to your historic data, effectively teaching it to
*read*
your documents and extract information according to your desired schema.

The following figure shows a high-level architecture of the document-to-JSON conversion process for fine-tuning VLMs by using historic data. This allows the VLM to learn from high data variations and helps ensure that the structured output matches the target system structure and format
***.***

![Document-to-JSON conversion process](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/22/image-4-7.png)

Fine-tuning offers several advantages over relying solely on OCR or general VLMs:

* **Schema adherence:**
  The model learns to output JSON matching a specific target structure, which is vital for integration with downstream systems like ERPs.
* **Implicit field location:**
  Fine-tuned VLMs often learn to locate and extract fields without explicit bounding box annotations in the training data, simplifying data preparation significantly.
* **Improved text extraction quality:**
  The model becomes more accurate at extracting text even from visually complex or noisy document layouts.
* **Contextual understanding:**
  The model can better understand the relationships between different pieces of information on the document.
* **Reduced prompt engineering:**
  Post fine-tuning, the model requires less complex or shorter prompts because the desired extraction behavior is built into its weights.

For our fine-tuning process, we selected the
[Swift framework](https://swift.readthedocs.io/en/latest/index.html)
. Swift provides a comprehensive, lightweight toolkit for fine-tuning various large language models, including VLMs like Qwen-VL and Llama-Vision.

## Data preparation

To fine-tune the VLMs, you will use the
[Fatura](https://doi.org/10.5281/zenodo.10371464)
2 dataset, a multi-layout invoice image dataset comprising 10,000 invoices with 50 distinct layouts.

The Swift framework expects training data in a specific JSONL (JSON Lines) format. Each line in the file is a JSON object representing a single training example. For multimodal tasks, this JSON object typically includes:

* `messages`
  : A list of conversational turns (for example,
  *system*
  ,
  *user*
  ,
  *assistant*
  ). The user turn contains placeholders for images (for example, <image>) and the text prompt that guides the model. The assistant turn contains the target output, which in this case is the ground-truth JSON string.
* `images`
  : A list of relative paths—within the dataset directory structure—to the document page images (JPG files) relevant to this training example.

As with standard ML practice, the dataset is split into training, development (validation), and test sets to effectively train the model, tune hyperparameters, and evaluate its final performance on unseen data. Each document (which could be single-page or multi-page) paired with its corresponding ground-truth JSON annotation constitutes a single row or example in our dataset. In our use case, one training sample is the invoice image (or multiple images of document pages) and the corresponding detailed JSON extraction. This one-to-one mapping is essential for supervised fine-tuning.

The conversion process, detailed in the
[dataset creation notebook](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/main/02_create_custom_dataset_swift.ipynb)
from the
[associated GitHub repo](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/tree/main)
, involves several key steps
**:**

1. **Image handling:**
   If the source document is a PDF, each page is rendered into a high-quality PNG image.
2. **Annotation processing (fill missing values):**
   We apply light pre-processing to the raw JSON annotation. Fine-tuning multiple models on an open source dataset, we observed that the performance increases when all keys are present in every JSON sample. To maintain this consistency, the target JSONs in the dataset are made to include the same set of top-level keys (derived from the entire dataset). If a key is missing for a particular document, it’s added with a null value.
3. **Key ordering:**
   The keys within the processed JSON annotation are sorted alphabetically. This consistent ordering helps the model learn a stable output structure.
4. **Prompt construction:**
   A user prompt is constructed. This prompt includes <image> tags (one for each page of the document) and explicitly lists the JSON keys the model is expected to extract. Including the JSON keys in the prompts improves the fine-tuned model’s performance.
5. **Swift formatting:**
   These components (prompt, image paths, target JSON) are assembled into the Swift JSONL format. Swift datasets support multimodal inputs, including images, videos and audios.

The following is an example structure of a single training instance in Swift’s JSONL format, demonstrating how multimodal inputs are organized. This includes conversational messages, paths to images, and objects containing bounding box (bbox) coordinates for visual references within the text. For more information about how to create a custom dataset for Swift, see the
[Swift documentation](https://swift.readthedocs.io/en/latest/Customization/Custom-dataset.html#multimodal)
.

```
 {
  "messages": [
    {"role": "system", "content": "Task definition"},
    {"role": "user", "content": "<image><image>... + optional text prompt"},
    {"role": "assistant", "content": "JSON or text output with extracted data with <bbox> references."}
  ],
  "images": ["path/to/image1.png", "path/to/image2.png"]
  "objects": {"ref": [], "bbox": [[90.9, 160.8, 135, 212.8], [360.9, 480.8, 495,   532.8]]} #Optional
 }
```

## Fine-tuning frameworks and resources

In our evaluation of fine-tuning frameworks for use with SageMaker AI, we considered several prominent options highlighted in the community and relevant to our needs. These included Hugging Face Transformers, Hugging Face Autotrain, Llama Factory, Unsloth, Torchtune, and ModelScope SWIFT (referred to simply as SWIFT in this post, aligning with the
[SWIFT 2024 paper by Zhao and](https://arxiv.org/html/2408.05517v3)
others.).

After experimenting with these, we decided to use SWIFT because of its lightweight nature, comprehensive support for various Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA and DoRA, and its design tailored for efficient training of a wide array of models, including the VLMS used in this post (for example,
[Qwen-VL 2.5](https://huggingface.co/Qwen/Qwen2.5-3B)
). Its scripting approach integrates seamlessly with SageMaker AI training jobs, allowing for scalable and reproducible fine-tuning runs in the cloud.

There are several strategies for adapting pre-trained models: full fine-tuning, where all model parameters are updated, PEFT, which offers a more efficient alternative by updating only a small new number of parameters (adapters), and quantization, a technique that reduces model size and speeds up inference using lower-precision formats (see Sebastian Rashka’s
[post on fine-tuning](https://magazine.sebastianraschka.com/p/finetuning-large-language-models)
to learn more about each technique).

Our project uses LoRA and DoRA, as configured in the
[fine-tuning notebook](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/main/03_finetune_swift.ipynb)
.

The following is an example of configuring and running a fine-tuning job (LoRA) as a SageMaker AI training job using SWIFT and remote function. When executing this function, the fine-tuning will be executed remotely as a SageMaker AI training job
***.***

```
from sagemaker.remote_function import remote
import json
import os
@remote (instance_type="ml.g6e.12xlarge", volume_size=200, use_spot_instances=True)
def fine_tune_document (training_data_s3, train_data_path="train.jsonl" , validation_data_path="validation.jsonl"):
    from swift.llm.sft import lim_sft, get_sft_main
    from swift.llm import sft_main

    ## copy the training data from input source to local directory
        ...
    train_data_local_path = ...
    validation_data_local_path = ...
    # set and run the fine-tuning using ms-swift framework
    os.environ["SIZE_FACTOR"] = json.dumps(8)# can be increase but requires more GPU memory
    os.environ["MAX_PIXELS"]= json.dumps (602112) # can be increase but requires more GPU memory os. environ ["CUDA_VISIBLE_DEVICES"]="0,1,2,3" # GPU devices to be used os. environ ["NPROC_PER_NODE"]="4" # we have 4 GPUs on on instance
    os.environ["USE_H_TRANSFER"] = json.dumps (1)
    argv = ['—model_type', 'qwen2_5_vl',
    '-model_id_or_path', 'Qwen/Qwen2.5-VL-3B-Instruct'
    '--train_type', 'lora'
    '--use_dora', 'true'
    '-output_dir', checkpoint_dir,
    '—max_length', '4096'
    '-dataset', train_data_local_path,
    '--val_dataset', validation_data_local_path,
	...
    ]

    sft_main (argv)
## potentially evaluate inference on test dataset return "done"
```

Fine-tuning VLMs typically requires GPU instances because of their computational demands. For models like Qwen2.5-VL 3B, an instance such as an Amazon SageMaker AI ml.g5.2xlarge or ml.g6.8xlarge can be suitable. Training time is a function of dataset size, model size, batch size, number of epochs, and other hyperparameters. For instance, as noted in our project
[readme.md](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/main/README.md)
, fine-tuning Qwen2.5 VL 3B on 300
[Fatura2](https://zenodo.org/records/10371464)
samples took approximately 2,829 seconds (roughly 47 minutes) on an ml.g6.8xlarge instance using Spot pricing. This demonstrates how smaller models, when fine-tuned effectively, can deliver exceptional performance cost-efficiently. Larger models like Llama-3.2-11B-Vision would generally require more substantial GPU resources (for example, ml.g5.12xlarge or larger) and longer training times.

## Evaluation and visualization of structured outputs (JSON)

A key aspect of any automation or machine learning project is evaluation. Without evaluating your solution, you don’t know how well it performs at solving your business problem. We wrote an
[evaluation notebook](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/main/05_evaluate_model.ipynb)
that you can use as a framework. Evaluating the performance of document-to-JSON models involves comparing the model-generated JSON outputs for unseen input documents (test dataset) against the ground-truth JSON annotations.

Key metrics employed in our project include:

1. **Exact match (EM) – accuracy:**
   This metric measures whether the extracted value for a specific field is an exact character-by-character match to the ground-truth value. It’s a strict metric, often reported as a percentage.
2. **Character error rate (CER) – edit distance:**
   calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change the model’s predicted string into the ground-truth string, typically normalized by the length of the ground-truth string. A lower CER indicates better performance.
3. **Recall-Oriented Understudy for Gisting Evaluation (ROGUE)**
   : This is a suite of metrics that compare n-grams (sequences of words) and the longest common subsequence between the predicted output and the reference. While traditionally used for text summarization, ROUGE scores can also provide insights into the overall textual similarity of the generated JSON string compared to the ground truth.

Visualizations are helpful for understanding model performance nuances. The following edit distance heatmap image provides a granular view, showing how closely the predictions match the ground truth (green means the model’s output exactly matches the ground truth, and shades of yellow, orange, and red depict increasing deviations). Each model has its own bar chart, allowing quick comparison across models. The X-axis is the number of sample documents. In this case, we ran inference on 250 unseen samples from the Fatura2 dataset. The Y-axis shows the JSON keys that we asked the model to extract; which will be different for you depending on what structure your downstream system requires.

In the image, you can see the performance of three different models on the Fatura2 dataset. From left to right: Qwen2.5 VL 3B fine-tuned on 300 samples from the Fatura2 dataset, in the middle Qwen2.5 VL 3B without fine-tuning (labeled
*vanilla*
), and Llama 3.2 11B vision fine-tuned on 1,000 samples.

The grey color shows the samples for which the Fatura2 dataset doesn’t contain any ground truth, which is why those are the same across the three models.

For a detailed, step-by-step walk-through of how the evaluation metrics are calculated, the specific Python code used, and how the visualizations are generated, see the comprehensive
[evaluation notebook in our project](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/main/05_evaluate_model.ipynb)
.

![Evaluation Comparison Plots](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/22/image-5-4.jpeg)

The image shows that Qwen2.5 vanilla is only decent at extracting the Title and Seller Name from the document. For the other keys it makes more than six character edit mistakes. However, out of the box Qwen2.5 is good at adhering to the JSON schema with only a few predictions where the key is missing (dark blue color) and no predictions of JSON that couldn’t be parsed (for example, missing quotation marks, missing parentheses, or a missing comma). Examining the two fine-tuned models, you can see improvement in performance with most samples, exactly matching the ground truth on all keys. There are only slight differences between fine-tuned Qwen2.5 and fine-tuned Llama 3.2, for example fine-tuned Qwen2.5 slightly outperforms fine-tuned Llama 3.2 on Total, Title, Conditions, and Buyer; whereas fine-tuned Llama 3.2 slightly outperforms fine-tuned Qwen2.5 on Seller Address, Discount, Tax, and Discount.

The goal is to input a document into your fine-tuned model and receive a clean, structured JSON object that accurately maps the extracted information to predefined fields.
**JSON-constrained decoding**
enforces adherence to a specified JSON schema during inference and is useful to make sure the output is valid JSON. For the Fatura2 dataset, this approach was not necessary—our fine-tuned Qwen 2.5 model consistently produced valid JSON outputs without additional constraints. However, incorporating constrained decoding remains a valuable safeguard, particularly for production environments where output reliability is critical.

[Notebook 07](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/b1cdcc140f9f5eb29d726c26b186fc0a4e327f41/07_consume_model.ipynb)
visualizes the input document and the extracted JSON data side-by-side.

## Deploying the fine-tuned model

After you fine-tune a model and evaluate it on your dataset, you will want to deploy it to run inference to process your documents. Depending on your use case, a different deployment option might be more suitable.

### Option a: vLLM container extended for SageMaker

To deploy our fine-tuned model for real-time inference, we use SageMaker endpoints. SageMaker endpoints provide fully managed hosting for real-time inference for FMs, deep learning, and other ML models and allows managed autoscaling and cost optimal deployment techniques. The process, detailed in our
[deploy model notebook](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/blob/main/06_deploy_model_endpoint.ipynb)
, involves building a custom Docker container. This container packages the
[vLLM serving engine](https://docs.vllm.ai/en/latest/)
, highly optimized for LLM and VLM inference, along with the Swift framework components needed to load our specific model and adapter. vLLM provides an OpenAI-compatible API server by default, suitable for handling document and image inputs with VLMs. Our custom docker-artifacts and Dockerfile adapts this vLLM base for SageMaker deployment. Key steps include:

1. Setting up the necessary environment and dependencies.
2. Configuring an entry point that initializes the vLLM server.
3. Making sure the server can load the base VLM and dynamically apply our fine-tuned LoRA adapter. The Amazon S3 path to the adapter (
   `model.tar.gz`
   ) is passed using the
   `ADAPTER_URI`
   environment variable when creating the SageMaker model.
4. The container, after being built and pushed to Amazon ECR, is then deployed to a SageMaker endpoint, which listens for invocation requests and routes them to the vLLM engine inside the container.

The following image shows a SageMaker vLLM deployment architecture, where a custom Docker container from Amazon ECR is deployed to a SageMaker endpoint. The container uses vLLM’s OpenAI-compatible API and Swift to serve a base VLM with a fine-tuned LoRA adapter dynamically loaded from Amazon S3.

![SageMaker vLLM deployment architecture](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/22/image-6-5.png)

### Option b (optional): Inference components on SageMaker

For more complex inference workflows that might involve sophisticated pre-processing of input documents, post-processing of the extracted JSON, or even chaining multiple models (for example, a classification model followed by an extraction model), Amazon SageMaker
[inference components](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceComponent.html)
offer enhanced flexibility. You can use them to build a pipeline of multiple containers or models within a single endpoint, each handling a specific part of the inference logic.

### Option c: Custom model inference in Amazon Bedrock

You can now import your custom models in Amazon Bedrock and then use Amazon Bedrock features to make inference calls to the model. Qwen 2.5 architecture is supported (see
[Supported Architectures](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html#model-customization-import-model-architecture)
). For more information, see
[Amazon Bedrock Custom Model Import now generally available](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-custom-model-import-now-generally-available/)
.

## Clean up

To avoid ongoing charges, it’s important to remove the AWS resources created for this project when you’re finished.

1. **SageMaker endpoints and models:**
   * In the AWS Management Console for SageMaker AI, go to
     **Inference**
     and then
     **Endpoints**
     . Select and delete endpoints created for this project.
   * Then, go to
     **Inference**
     and then
     **Models**
     and delete the associated models.
2. **Amazon S3 data:**
   * Navigate to the Amazon S3 console.
   * Delete the S3 buckets or specific folders or prefixes used for datasets, model artifacts (for example, model.tar.gz from training jobs), and inference results.
     **Note:**
     Make sure you don’t delete data needed by other projects.
3. **Amazon ECR images and repositories:**
   * In the Amazon ECR console, delete Docker images and the repository created for the custom vLLM container if you deployed one.
4. **CloudWatch logs (optional):**
   * Logs from SageMaker activities are stored in
     [Amazon CloudWatch](https://aws.amazon.com/cloudwatch)
     . You can delete relevant log groups (for example,
     `/aws/sagemaker/TrainingJobs`
     and
     `/aws/sagemaker/Endpoints`
     ) if desired, though many have automatic retention policies.

**Important:**
Always verify resources before deletion. If you experimented with Amazon Bedrock custom model imports, make sure those are also cleaned up. Use
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
to monitor for unexpected charges.

## Conclusion and future outlook

In this post, we demonstrated that fine-tuning VLMs provides a powerful and flexible approach to automate and significantly enhance document understanding capabilities. We have also demonstrated that using focused fine-tuning allows smaller, multi-modal models to compete effectively with much larger counterparts (98% accuracy with Qwen2.5 VL 3B). The project also highlights that fine-tuning VLMs for document-to-JSON processing can be done cost-effectively by using Spot instances and PEFT methods (approximately $1 USD to fine-tune a 3 billion parameter model on around 200 documents).

The fine-tuning task was conducted using
[Amazon SageMaker training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)
and the Swift framework, which proved to be a versatile and effective toolkit for orchestrating this fine-tuning process.

The potential for enhancing and expanding this work is vast. Some exciting future directions include deploying structured document models on CPU-based, serverless compute like
[AWS Lambda](https://aws.amazon.com/lambda)
or
[Amazon SageMaker Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
using tools like llama.cpp or vLLM. Using quantized models can enable low-latency, cost-efficient inference for sporadic workloads. Another future direction includes improving evaluation of structured outputs by going beyond field-level metrics. This includes validating complex nested structures and tables using methods like tree edit distance for tables (TEDS).

The complete code repository, including the notebooks, utility scripts, and Docker artifacts, is
[available on GitHub](https://github.com/aws-samples/sample-for-multi-modal-document-to-json-with-sagemaker-ai/tree/main)
to help you get started unlocking insights from your documents. For a similar approach, using
[Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/?trk=978e13b6-fa37-4872-9001-1825f3ca3367&sc_channel=ps&ef_id=CjwKCAjwu9fHBhAWEiwAzGRC_9iqhgtEeqOv5RsmmzW9xJI3RqV0llbP80kcyS833jM30xD2wavfhhoC9CMQAvD_BwE:G:s&s_kwcid=AL!4422!3!692006004844!e!!g!!amazon%20nova!21048268689!159639953895&gad_campaignid=21048268689&gbraid=0AAAAADjHtp-nx84Cu8s-AWHGpzg1jNtgL&gclid=CjwKCAjwu9fHBhAWEiwAzGRC_9iqhgtEeqOv5RsmmzW9xJI3RqV0llbP80kcyS833jM30xD2wavfhhoC9CMQAvD_BwE)
, please refer to this AWS blog for
[optimizing document AI and structured outputs by fine-tuning Amazon Nova Models and on-demand inference](https://aws.amazon.com/de/blogs/machine-learning/optimizing-document-ai-and-structured-outputs-by-fine-tuning-amazon-nova-models-and-on-demand-inference/)
.

---

### About the Authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/30/arlind.png)
Arlind Nocaj**
is a GTM Specialist Solutions Architect for AI/ML and Generative AI for Europe central based in AWS Zurich Office, who guides enterprise customers through their digital transformation journeys. With a PhD in network analytics and visualization (Graph Drawing) and over a decade of experience as a research scientist and software engineer, he brings a unique blend of academic rigor and practical expertise to his role. His primary focus lies in using the full potential of data, algorithms, and cloud technologies to drive innovation and efficiency. His areas of expertise include Machine Learning, Generative AI and in particular Agentic systems with Multi-modal LLMs for document processing and structured insights.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/03/malte.jpg)
Malte Reimann**
is a Solutions Architect based in Zurich, working with customers across Switzerland and Austria on their cloud initiatives. His focus lies in practical machine learning applications—from prompt optimization to fine-tuning vision language models for document processing. The most recent example, working in a small team to provide deployment options for Apertus on AWS. An active member of the ML community, Malte balances his technical work with a disciplined approach to fitness, preferring early morning gym sessions when it’s empty. During summer weekends, he explores the Swiss Alps on foot and enjoying time in nature. His approach to both technology and life is straightforward: consistent improvement through deliberate practice, whether that’s optimizing a customer’s cloud deployment or preparing for the next hike in the clouds.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/30/Nick.jpeg)
Nick McCarthy**
is a Senior Generative AI Specialist Solutions Architect on the Amazon Bedrock team, focused on model customization. He has worked with AWS clients across a wide range of industries — including healthcare, finance, sports, telecommunications, and energy — helping them accelerate business outcomes through the use of AI and machine learning. Outside of work, Nick loves traveling, exploring new cuisines, and reading about science and technology. He holds a Bachelor’s degree in Physics and a Master’s degree in Machine Learning.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/30/irene.jpeg)
**Irene Marban Alvarez**
is a Generative AI Specialist Solutions Architect at Amazon Web Services (AWS), working with customers in the United Kingdom and Ireland. With a background in Biomedical Engineering and Masters in Artificial Intelligence, her work focuses on helping organizations leverage the latest AI technologies to accelerate their business. In her spare time, she loves reading and cooking for her friends.