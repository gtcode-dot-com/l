---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-05T01:05:34.440508+00:00'
exported_at: '2026-03-05T01:05:36.045341+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-ricoh-built-a-scalable-intelligent-document-processing-solution-on-aws
structured_data:
  about: []
  author: ''
  description: This post explores how Ricoh built a standardized, multi-tenant solution
    for automated document classification and extraction using the AWS GenAI IDP Accelerator
    as a foundation, transforming their document processing from a custom-engineering
    bottleneck into a scalable, repeatable service.
  headline: How Ricoh built a scalable intelligent document processing solution on
    AWS
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-ricoh-built-a-scalable-intelligent-document-processing-solution-on-aws
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How Ricoh built a scalable intelligent document processing solution on AWS
updated_at: '2026-03-05T01:05:34.440508+00:00'
url_hash: 38f8fd984573d167956641de015a2cd7b6bd141e
---

*This post is cowritten by Jeremy Jacobson and Rado Fulek from Ricoh.*

This post demonstrates how enterprises can overcome document processing scaling limits by combining generative AI, serverless architecture, and standardized frameworks. Ricoh engineered a repeatable, reusable framework using the
[AWS GenAI Intelligent Document Processing (IDP) Accelerator](http://www.amazon.com/genai-idp-accelerator)
. This framework reduced customer onboarding time from weeks to days. It also increased processing capacity for new AI-intensive workflows that required complex document splitting. The capacity is projected to grow sevenfold to over 70,000 documents per month. Additionally, the solution decreased engineering hours per deployment by over 90%.

Ricoh USA, Inc. is a global technology leader serving a diverse client base in over 200 countries. Within its healthcare practice, Ricoh serves major health insurance payers, managed care organizations, and healthcare providers—processing hundreds of thousands of critical documents each month, including insurance claims, grievances, appeals, and clinical records for their clients. They faced a challenge common to enterprises modernizing document-heavy workflows: reliance on custom manual engineering. Each new healthcare customer implementation required unique development and tuning by specialized engineers. Additionally, deployment required custom prompt engineering, model fine-tuning, and integration testing that couldn’t be reused across customers. Although this provided an exceptional, bespoke experience for Ricoh customers, the time and effort involved created bottlenecks that limited expansion. With an anticipated sevenfold increase in volume, Ricoh seized the opportunity to innovate.

The challenge was not just to automate processes. It was to build a scalable solution that could deliver state-of-the-art AI for document extraction and agentic workflows. This solution needed to meet strict compliance standards, including HITRUST, HIPAA, and SOC II. These requirements often stand at odds with rapid AI innovation. Compliance frameworks typically restrict data sharing that limits model training capabilities. They also mandate rigorous security controls that can impede the agility needed for iterative AI development and deployment. Despite these challenges, Ricoh made it a priority to overcome this tension for their customers. Building upon foundation models (FMs) available through
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
and combining them with
[Amazon Textract](https://aws.amazon.com/textract/)
, Ricoh made it possible for customers to benefit from cutting-edge automation that aligns with the strictest compliance standards.

This post explores how Ricoh built a standardized, multi-tenant solution for automated document classification and extraction using the AWS GenAI IDP Accelerator as a foundation, transforming their document processing from a custom-engineering bottleneck into a scalable, repeatable service.

## Customer overview

Ricoh USA, Inc. is a global technology leader delivering digital workplace services, document management, and business process automation solutions to organizations in over 200 countries. Within its healthcare practice, Ricoh serves major health insurance payers, managed care organizations, and healthcare providers—processing thousands of critical documents each month, including insurance claims, grievances, appeals, and clinical records.

“Within the Ricoh Intelligent Business Platform, the workflows that required the highest levels of intelligence for key IDP tasks experienced explosive growth. We needed to move from bespoke builds to a platform,” says Jeremy Jacobson, AI Architect, Portfolio Solution Development at Ricoh. “For our customers, we integrate, operate, and evolve AI so they don’t have to. Aligning our proprietary IDP patterns and technologies with the AWS GenAI IDP accelerator amplified this advantage. So equipped, we delivered a HITRUST CSF-certified configurable IDP platform that ties our customers to the frontiers of AI.”

Healthcare documents often arrive unstructured and highly variable. A single packet might include multiple document types—fax covers, clinical notes, and appeal forms—each with different layouts and naming conventions. Documents ranged from 15–50 pages, with some containing cover letters while others did not. Different healthcare providers used varying document structures, field naming conventions, and placement of critical information across different healthcare providers. Template-based extraction approaches proved ineffective.

For Ricoh’s Intelligent Business Platform services, functional requirements included capturing data attributes from scans of unstructured or semi-structured documents and assigning to each data attribute a confidence level that reliably identifies when human review is needed. Every attribute with a confidence level below a predefined threshold is reviewed by a person to verify accuracy and compliance. Human reviewers verify extracted data, correct errors, and validate that critical healthcare information—such as member IDs, diagnosis codes, and claim amounts—meets the quality standards required for regulatory compliance alignment and claims processing. This human-in-the-loop approach achieves two key business outcomes: maintaining the high accuracy levels (typically 98–99%) required by healthcare payers while reducing manual review costs by 60–70% compared to fully manual processing.

The solution needed to extract key data such as member IDs, provider information, and claim details from various sections of documents, with the capability to search through clinical notes and other sections when information was not found in cover letters. Non-functional requirements addressed several critical operational needs:

* **Performance and scalability**
  – Handle traffic spikes to process up to 1,000 documents in minutes while avoiding wasted computational resources during low-traffic periods
* **Accuracy and quality**
  – Meet strict service level agreements (SLAs) for delivery deadlines and data accuracy
* **Cost optimization**
  – Enable configurable confidence thresholds that balance accuracy requirements with manual review costs—keeping wrongly captured attributes below the agreed SLA while minimizing expensive human review
* **Operational efficiency**
  – Enable quick customer onboarding through configuration changes rather than code changes

## Challenges with complex document processing workflows

For some time, the Ricoh team had combined traditional optical character recognition (OCR)—which detects and extracts text from scanned documents—with multimodal AI models that can understand both text and images simultaneously. This approach helped address complex challenges such as distinguishing between similar fields when extracting data from documents with multiple names and addresses.

After multimodal FMs became available on Amazon Bedrock, it soon became clear that a simple API call to Amazon Bedrock—that is, sending a scanned document along with a prompt—would not suffice for complex workflows. When documents are composed of multiple parts or sections, such as cover sheets, contracts, or authorization responses, extraction rules often depend upon first successfully classifying the section type.

The solution needed to handle complex document classification, distinguishing between claims, disputes, emails, and fax cover sheets without breaking down packets into granular document types. Additionally, large language models (LLMs) have context window limits and experience declining performance in following instructions as the context fills. Document page size limitations required the Ricoh team to use alternative approaches for larger documents.

The Ricoh team also required flexibility to integrate with their existing high-capacity document processing workflows—including document routing systems, case management services, and downstream business applications—while maintaining control over processing steps and model selection. This included unique requirements such as splitting documents based on healthcare provider or patient information.

To improve accuracy, the Ricoh team utilized more sophisticated means of dynamically inserting context into prompts—a technique where relevant document metadata, previously extracted fields, and document structure information are programmatically added to the AI model’s instructions based on the specific document being processed. This context-aware prompting improved extraction accuracy by 15–20% compared to static prompts, helping the model understand document relationships and field dependencies.

Although these gains were substantial, when trying to recreate this success, the Ricoh team ran into a persistent hurdle: these workflows demanded 40–60 hours of developer time per customer to set up, for instance to incorporate newly released features of the underlying models. Ricoh coordinated with the AWS Generative AI Innovation Center on the IDP Accelerator to address these scalability challenges.

## Solution overview

Ricoh partnered with AWS to implement the
[GenAI IDP Accelerator](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws)
, a reference framework designed to help you deploy production-grade document processing solutions. The accelerator provides multiple processing patterns optimized for different document types and workflows.

The team selected
[Processing Pattern 2](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws/blob/main/docs/pattern-2.md)
, which combines Amazon Textract for OCR—the technology that converts images of text into machine-readable text—with Amazon Bedrock FMs for intelligent classification and extraction. This pattern is specifically designed for complex, multi-part documents that require both text extraction and AI-powered understanding. The approach offered full control over model orchestration and was ideal for handling Ricoh’s multi-part healthcare documents because it supports sequential processing (classify first, then extract based on classification) and handles documents exceeding typical LLM context windows by processing them in sections.

The solution was architected to align with stringent healthcare compliance requirements. For HIPAA compliance, the Protected Health Information (PHI) is encrypted at rest using
[AWS Key Management Service](https://aws.amazon.com/kms/)
(AWS KMS) and in transit using TLS 1.2+. Access controls follow the principle of least privilege, with
[AWS Identity and Access Management](https://aws.amazon.com/iam/)
(IAM) policies restricting data access to authorized personnel only.

For HITRUST certification requirements, the architecture implements comprehensive audit logging through
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
and
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
, capturing data access and processing activities. SOC 2 Type II compliance alignment is supported through the use of AWS services that maintain their own SOC 2 certifications, combined with Ricoh’s documented operational controls for change management, event response, and continuous monitoring.

The pay-per-use pricing model removes idle infrastructure costs—Ricoh only pays for actual document processing, with no charges during periods of inactivity. This cost predictability was crucial for supporting multiple customers with varying document volumes, as each customer’s costs scale proportionally with their usage rather than requiring fixed infrastructure investments.

Documents enter using
[Amazon Simple Storage Service](https://aws.amazon.com/s3/)
(Amazon S3), triggering event-driven workflows.
[AWS Lambda](https://aws.amazon.com/lambda/)
functions invoke Amazon Bedrock models to determine document types such as claims, appeals, faxes, grievances, prior authorization requests, and clinical documentation. Amazon Textract parses text and layout, and the results are combined with Amazon Bedrock models for structured data extraction. Custom business rules—configurable logic specific to each customer’s requirements, such as field validation rules, document routing criteria, and data transformation specifications—work alongside confidence scoring to determine which fields require human review.

Confidence scores are calculated by comparing extraction results from multiple sources (Amazon Textract and Amazon Bedrock) and assigning a numerical value (0–100%) indicating the system’s certainty in each extracted field. Fields scoring below customer-defined thresholds (typically 70–85%) are flagged for human validation. Final outputs are stored in Amazon S3, with low-confidence cases routed for human validation through review queues where operators verify extracted data, correct errors, and provide feedback that improves future processing.

The core
[IDP-Common](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws/blob/main/lib/idp_common_pkg/README.md)
engine from the AWS GenAI IDP Accelerator served as the integration layer, helping Ricoh maintain its established workflows. The IDP Common Package is a Python library that provides shared functionality for the Accelerated Intelligent Document Processing solution on AWS. This solution helps businesses automatically extract and process information from documents using AI services, removing manual data entry and improving accuracy.

Each customer deployment is instantiated using a configurable
[AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/)
(AWS SAM) application deployed as an
[AWS CloudFormation](https://aws.amazon.com/cloudformation/)
stack, supporting rapid onboarding. This abstracts away infrastructure details—including
[Amazon Virtual Private Cloud](http://aws.amazon.com/vpc)
(Amazon VPC) configuration, security group rules, IAM role policies, and service quotas—so team members can focus only on the customer-dependent parameters such as Lambda reserved concurrency or database connection details. This focused approach is valuable when onboarding a new customer.

The modular design helped Ricoh integrate specific parameters and custom functionality such as customer-defined proprietary document classification, custom data extraction for industry-specific forms, or redaction rules for personally identifiable information (PII) compliance alignment into their existing high-capacity workflow without disrupting established processes. This approach helped the team maintain operational efficiency through automated deployment that reduced customer onboarding time from weeks to days, while adding advanced AI capabilities for document processing, including intelligent document classification, and automated data extraction from unstructured forms.

## Architecture details

The architecture was designed with three primary objectives: enable rapid customer onboarding through configuration rather than code changes, help align with healthcare regulations (HIPAA, HITRUST, SOC 2), and provide cost-effective scalability for variable document volumes. The serverless approach was chosen to remove infrastructure management overhead and align costs directly with usage, and the multi-tenant design with per-customer queues balances resource efficiency with workload isolation. The decision to use Processing Pattern 2 (Amazon Textract and Amazon Bedrock) rather than Amazon Bedrock alone was driven by the need to handle documents exceeding LLM context windows and the requirement for structured text extraction that could be selectively included in prompts based on document type.

The implementation used a serverless architecture in which Lambda functions are automatically invoked upon upload of scanned documents to Amazon S3. The Lambda functions handle calls to the AI services—Amazon Textract and Amazon Bedrock—and output the captured attributes along with their confidence scores to an
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
database.

The architecture incorporates AWS Well-Architected Framework principles across multiple pillars. For
**security**
, the data is encrypted at rest using AWS KMS with customer-managed keys and in transit using TLS 1.2+. IAM roles enforce least-privilege access, separated by function, with separate roles for document ingestion, processing, and retrieval. CloudTrail logs the API calls for audit trails, and CloudWatch Logs captures application-level events for security monitoring.

For
**reliability**
, the serverless design removes single points of failure, with automatic retries and dead-letter queues (DLQs) handling transient errors. For
**performance efficiency**
, Lambda concurrency limits and
[Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
(Amazon SQS) queue throttling helps prevent API quota exhaustion while maintaining high throughput. For
**cost optimization**
, the pay-per-use model removes idle resource costs, and Amazon S3 lifecycle policies automatically transition processed documents to lower-cost storage tiers.

For
**operational excellence**
, infrastructure as code using AWS SAM and CloudFormation enables consistent deployments, and CloudWatch dashboards and alarms provide real-time visibility into processing metrics and error rates.

A critical part of the architecture is an SQS queue that makes it possible for the team to control the rate at which they are making requests to Amazon Textract and Amazon Bedrock API endpoints by controlling message processing velocity through Lambda concurrency settings and Amazon SQS visibility timeouts. This design helps them stay within service quota limits (such as transactions per second for Amazon Textract and requests per minute for Amazon Bedrock). Furthermore, Amazon SQS seamlessly facilitates retries and sending of unprocessed messages to a DLQ.

Each customer has its own
[Amazon EventBridge](https://aws.amazon.com/eventbridge/)
rule and SQS queue, enabling multi-tenant isolation (helping prevent one customer’s high volume from impacting others) and independent scaling (allowing per-customer concurrency limits and throughput controls).

The architecture used Amazon S3 for document storage. Different buckets were created to manage documents from various sources, including fax, scan, and SFTP systems. DynamoDB tables stored document metadata and processing state, tracking document versions and helping prevent multiple attempts to update the same document simultaneously. CloudWatch provided comprehensive monitoring and logging of successful extraction rates and processing anomalies.

The actual interaction with AI services uses Amazon Textract to augment Amazon Bedrock prompts with structured data extracted from the scanned document. Here, the team took advantage of their previous Amazon Textract based solution and used it as another source of truth for the extracted values, which make it possible to compute reliable confidence scores by comparing results from both extraction methods. This dual-extraction approach was used during the initial deployment phase to validate accuracy, with the legacy system phased out after confidence in the new system was established.

For document processing, the solution used Amazon Textract to extract text from large healthcare documents, addressing the challenge of documents that exceeded the context window limitations of FMs when processed as images. For example, a 50-page clinical record would exceed most LLM context windows if sent as images, but Amazon Textract converts it to structured text that can be selectively included in prompts. Amazon Bedrock FMs handled the intelligent classification and extraction tasks, with tailored instructions for healthcare data designed to identify document types and extract healthcare-specific information such as member IDs, provider details, and claim information.

For document classification and splitting, the team used LLMs to intelligently identify document types and split multi-document packets based on provider or patient information.

Regarding fast onboarding for new customers, the team used a configurable AWS SAM application deployed as a CloudFormation nested stack for each customer. This abstracts away infrastructure details—such as VPC configuration, security group rules, IAM role policies, and service quotas—and so team members can focus only on the customer-dependent parameters when onboarding a new customer.

The modular architecture helped Ricoh deploy only the components they needed while maintaining the option to add additional features such as document summarization or knowledge base integration in the future.

## Results and outcomes

Ricoh has been able to lower prices for an important healthcare customer by measuring and achieving significant reductions in human labor required to index documents in production. Human indexers now concentrate their time on difficult documents and extractions, with AI serving as their partner in the process rather than performing routine data entry.

Ricoh’s Intelligent Business Platform achieved significant operational improvements and potential annual savings exceeding 1,900 person-hours through automation, dramatically reducing the manual effort required for document processing.

The automated classification system successfully distinguished between insurance policy holders’ grievances and appeals claims, a critical capability for healthcare compliance and workflow management. These document types have different regulatory timelines (grievances typically require 30-day resolution, appeals require 60 days) and must be routed to different processing teams. Misclassification can result in missed deadlines, regulatory penalties, and member dissatisfaction.

The solution demonstrated extraction accuracy levels that help minimize financial penalties from processing errors, a crucial outcome in the heavily regulated healthcare industry. The confidence scoring capabilities enabled effective human-in-the-loop review processes, helping verify that documents requiring expert validation were properly flagged while allowing high-confidence extractions to proceed automatically.

Ricoh successfully created a reusable framework that can be deployed across multiple healthcare customers, providing a scalable foundation for expanding their document processing services to future use cases. The solution now processes over 10,000 healthcare documents monthly with the infrastructure in place to scale to 70,000 documents as client needs grow.

The Intelligent Business Platform achieved significant operational improvements, as detailed in the following table.

| Key Performance Indicator | Before (Legacy) | After (AWS IDP Accelerator) | Impact |
| --- | --- | --- | --- |
| Onboarding Time | 4–6 weeks | 2–3 days | >90% reduction |
| Monthly Throughput | ~10,000 documents | >70,000 documents | 7-fold increase |
| Engineering Hours per Deployment | ~80 hours | <5 hours | >90% reduction |
| Processing Capacity | Limited | 1,000 documents in minutes | Handles traffic spikes |

## Best practices and lessons learned

The Ricoh implementation highlighted several best practices for deploying IDP solutions in production environments:

* **Choose the appropriate processing pattern –**
  Selecting Pattern 2 from the AWS IDP Accelerator provided the flexibility needed for complex healthcare document requirements while maintaining control over model selection and processing steps. This choice was essential for handling unique document splitting requirements and integration with existing workflows.
* **Use a hybrid approach combining OCR with FMs –**
  The team found that using Amazon Textract to augment Amazon Bedrock prompts with structured data provided both scalability and accuracy for documents of varying sizes and complexity. This hybrid approach of combining OCR with FMs addressed practical limitations around context window sizes when processing documents as images—Amazon Textract handles documents of different sizes, and Amazon Bedrock provides intelligent understanding of the extracted text, enabling both scalability (no document size limits) and accuracy (AI-powered field extraction and validation). Taking advantage of the previous Amazon Textract based solution as another source of truth during the validation phase helped the team compute reliable confidence scores without incurring significant additional costs, because Amazon Textract was already being used for text extraction in the new architecture.
* **Integrate confidence scoring from the beginning –**
  Integrating confidence scoring from the beginning enabled effective human-in-the-loop workflows, allowing the system to automatically flag uncertain extractions for expert review. This approach balanced automation benefits with the accuracy requirements of healthcare document processing. Configurable confidence thresholds proved essential for meeting customer requirements—helping teams keep wrongly captured attributes below agreed SLAs while minimizing the cost of manual review.
* **Implement rate limiting with SQS queues –**
  Implementing an SQS queue to limit the rate of API calls to Amazon Textract and Amazon Bedrock endpoints helped the team stay within quota limits while seamlessly facilitating retries and DLQ handling. This architectural decision helped prevent throttling issues and improved overall system reliability.
* **Standardize using configuration rather than code –**
  Standardizing using configuration rather than code changes was a key enabler of rapid customer onboarding. The configurable AWS SAM application deployed as a CloudFormation nested stack for each customer abstracted away infrastructure details, so team members could focus only on customer-dependent parameters. This approach reduced maintenance efforts and enabled quick onboarding for new customers.
* **Use a modular architecture for integration –**
  The modular architecture of the GenAI IDP Accelerator proved valuable for integration with existing systems. Rather than replacing established workflows, the core IDP-Common engine helped Ricoh enhance their current infrastructure with AI capabilities—including document classification, intelligent field extraction, confidence scoring, and natural language understanding.
* **Plan for scalability from the outset –**
  Planning for scalability from the outset enabled smooth growth from proof of concept to production volumes. The serverless architecture’s automatic scaling capabilities and pay-per-use pricing model aligned infrastructure costs with business growth, providing predictable economics as document volumes increased. The architecture handled spikes in traffic to seamlessly process up to 1,000 documents in a few minutes while not wasting computational resources during periods of low or no traffic.

## Getting started

Ready to build your own IDP solution? The AWS GenAI IDP Accelerator provides a proven foundation for deploying production-grade document automation:

* **Explore the accelerator**
  – Visit the
  [GenAI IDP Accelerator repository](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws)
  to review the architecture patterns, deployment guides, and sample code
* **Choose your pattern**
  – Review the multiple processing patterns available and select the one that best fits your document types and workflow requirements
* **Start small, scale fast**
  – Begin with a proof of concept using your most challenging document types, then use the modular architecture to expand across your organization
* **Leverage AWS expertise**
  – Connect with AWS Solutions Architects and the GenAI Innovation Center to discuss your specific use case and implementation strategy

For organizations processing high volumes of complex documents, the combination of serverless architecture, FMs, and standardized frameworks offers a path to rapid deployment and scalable growth.

## Conclusion

Ricoh’s implementation of the AWS GenAI IDP Accelerator demonstrates how enterprises can overcome scaling limits by combining generative AI, serverless architecture, and compliance frameworks. The result is faster onboarding, higher accuracy, and reduced operational overhead—all without compromising compliance standards (HIPAA, HITRUST, SOC 2) or operational control. By developing a reusable framework rather than single-use solutions, Ricoh transformed document processing into a scalable service.

The Intelligent Business Platform’s ability to handle complex healthcare document variations, provide confidence scoring for human-in-the-loop workflows, and scale from 10,000 to potentially 70,000 documents monthly showcases the practical benefits of IDP powered by generative AI on AWS. The reusable framework Ricoh created can now be deployed across multiple healthcare customers, providing a foundation for expanding their document processing services.

For organizations facing similar document processing challenges, the GenAI IDP Accelerator offers a proven path from proof of concept to production-ready solutions. The combination of serverless architecture, multiple processing patterns, and integration flexibility helps teams build document automation tailored to their specific needs while using the latest advances in generative AI and AWS services. Their story is proof that with the right foundation, AI doesn’t just automate work—it can accelerate growth.

To get started with the GenAI IDP Accelerator, visit the
[project repository](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws)
and explore the documentation and deployment guides.

### Acknowledgments

Special thank you to Bob Strahan for his leadership of the GenAI IDP Accelerator project. We would also like to thank Guillermo Tantachuco, Saeideh Shahrokh Esfahani, Mofijul Islam, Suresh Konappanava, and Yingwei Yu for their contributions and guidance throughout.

---

### About the authors

### Jeremy Jacobson

Jeremy Jacobson is a lead developer and solutions architect for AI within Ricoh USA’s Intelligent Business Platform (IBP) services. His background includes experience at Emory University and the Fields Institute, which informs his approach to building production AI systems.

### Rado Fulek

Rado Fulek is a software engineer at Ricoh where he builds secure, scalable and reliable document processing platforms. Previously, he conducted cutting-edge algorithmic research, publishing in top journals on algorithms, and discovering efficient algorithms, whose existence had been open for decades. Rado brings a problem solver mindset to AI, emphasizing practical, well-architected solutions that bridge the gap between cutting-edge research and real-world production systems.

### Earl Bovell

Earl Bovell is a Senior Solutions Architect at Amazon Web Services (AWS), where he serves as a technical advisor and strategist helping enterprise customers solve business problems by leveraging AWS technology.

### Vincil Bishop

Vincil Bishop is a Senior Deep Learning Architect in AWS’s Generative AI Innovation Center. He has over 25 years of experience in the IT industry and holds a PhD in Systems Engineering. Vincil specializes in designing and implementing AI solutions that help organizations solve their toughest business challenges.

### Jordan Ratner

Jordan Ratner is a Senior Generative AI Strategist in the AWS Generative AI Innovation Center, where he partners with C-suite leaders and engineering teams to design, prototype, and deploy generative AI solutions.