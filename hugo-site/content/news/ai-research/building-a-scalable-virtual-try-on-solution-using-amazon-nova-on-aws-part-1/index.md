---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-04T00:15:33.374647+00:00'
exported_at: '2026-03-04T00:15:36.755718+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/building-a-scalable-virtual-try-on-solution-using-amazon-nova-on-aws-part-1
structured_data:
  about: []
  author: ''
  description: In this post, we explore the virtual try-on capability now available
    in Amazon Nova Canvas, including sample code to get started quickly and tips to
    help get the best outputs.
  headline: 'Building a scalable virtual try-on solution using Amazon Nova on AWS:
    part 1'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/building-a-scalable-virtual-try-on-solution-using-amazon-nova-on-aws-part-1
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Building a scalable virtual try-on solution using Amazon Nova on AWS: part
  1'
updated_at: '2026-03-04T00:15:33.374647+00:00'
url_hash: ab1de0ef5fe150bcb7e6168aa4a8a672e874888b
---

In this first post in a two-part series, we examine how retailers can implement a virtual try-on to improve customer experience. In part 2, we will further explore real-world applications and benefits of this innovative technology.

Every fourth piece of clothing bought online is returned to the retailer, feeding into America’s
[$890 billion returns](https://nrf.com/research/2024-consumer-returns-retail-industry)
problem in 2024. Behind these numbers lies a simple truth: shoppers can’t judge fit and style through their screens. Among the top reasons for
[returned fashion items](https://www.dealnews.com/features/retail-returns-2023.html)
are poor fit, wrong size, or style mismatch.

Retailers face a critical challenge in that their most valuable customers often return the most items, forcing them to maintain generous return policies despite steep processing costs and environmental impact. Each return produces 30% more carbon emissions than the initial delivery and represents a missed sales opportunity until items are processed back into inventory. As digital shopping accelerates, virtual try-on technology has emerged as a solution to reduce returns while maintaining customer convenience, but early implementations struggled with accuracy, scalability, and preserving crucial details such as garment draping, patterns, and logos.

[Amazon Nova Canvas](https://docs.aws.amazon.com/ai/responsible-ai/nova-canvas/overview.html)
addresses these challenges through its virtual try-on capability, which uses two two-dimensional image inputs: a source image showing a person or living space and a reference image of the product. The system offers both automatic product placement through auto-masking functionality and manual controls for precise adjustments. Throughout the process, it carefully preserves important details such as logos and textures while providing comprehensive styling controls for customization.

Virtual try-on can be deployed across multiple customer engagement channels, from ecommerce websites and mobile shopping apps to in-store kiosks, social media shopping platforms, and virtual showrooms. Imagine visiting an ecommerce website, uploading your personal image, and seeing it applied across the clothing and accessory products on that website.

The following image shows a source image, a reference image, a mask image, and the resulting try-on image.

![Fashion styling diagram showing image composition technique with source image of woman in black blazer and white top, reference image with pink pleated skirt, mask visualization in purple, and final result combining elements through digital blending](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/13/ML-193001.png)

In this post, we explore the virtual try-on capability now available in Amazon Nova Canvas, including sample code to get started quickly and tips to help get the best outputs.

## Solution overview

With virtual try-on capability, retailers and ecommerce companies can integrate garment and product visualization directly into their existing or new customer touch points. Using only a photo upload and product selection, customers can see how items would look on themselves, a model, or other placement. You can experiment with virtual try-on in Amazon Nova Canvas within the
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
playground. And, we’ll guide you through implementing a complete solution around this feature in your own
[Amazon Web Services](https://aws.amazon.com/)
(AWS) environment. The following section provides detailed instructions and best practices for deployment.

At its core, the solution uses the new virtual try-on in Amazon Nova Canvas in Amazon Bedrock. This model offers fast inference speeds, making it suitable for real-time applications such as ecommerce. At the same time, it preserves high-fidelity details of reference items, including patterns, textures, and logos. The model maintains accurate semantic manipulations within scenes.

Our solution combines AWS serverless services with AI processing capabilities in an event-driven architecture.
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
[Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html)
triggers an
[AWS Step Functions](https://aws.amazon.com/step-functions/)
workflow and
[Amazon Simple Storage Service](https://aws.amazon.com/s3/)
(Amazon S3) events to manage result delivery. Amazon Nova Canvas in Amazon Bedrock manages both the mask generation and pose detection. The solution follows an asynchronous processing pipeline with real-time status updates in which WebSocket connections maintain real-time communication with clients, enabling continuous user engagement throughout the process. For detailed implementation guidance and best practices, refer to our
[guidance](https://aws.amazon.com/solutions/guidance/virtual-try-on-on-aws/)
.

## Detailed explanation of the architecture

The request initiation follows this flow:

1. Amazon S3 stores the uploaded customer model photos and product images.
2. Each upload generates a message sent to an
   [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
   (Amazon SQS) queue. The
   [AWS Lambda](https://aws.amazon.com/lambda/)
   function creates the corresponding metadata and S3 path and stores it in the DynamoDB product table for later retrieval.
3. [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
   manages the WebSocket connections for real-time status updates between the client and the virtual try-on.
4. Lambda processes initial requests by retrieving product information in the DynamoDB product table and creating job entries in DynamoDB.
5. Amazon DynamoDB: The products table (
   `vto-products`
   ) stores catalog items available for the virtual try-on, notably the Amazon S3 picture location.
6. The virtual try-on jobs DynamoDB table (
   `vto-jobs`
   ) tracks the state of each try-on request.

The virtual try-on generation follows this flow:

7. DynamoDB Streams asynchronously triggers AWS Step Functions workflows on job creation for processing try-on requests.
8. AWS Step Functions orchestrates the virtual try-on generation. It triggers a Lambda function that calls the Amazon Nova Canvas model through Amazon Bedrock. The DynamoDB job table is updated with the virtual try-on status.

The result delivery follows this flow:

9. Amazon S3 stores the generated try-on images with job ID metadata.
10. Amazon SQS handles S3 event notifications for completed try-on images.
11. AWS Lambda function sends the Amazon S3 URL of the result back to the user through WebSocket.

The following diagram illustrates the solution architecture.

![AWS Architecture using AWS Step Functions workflow architecture diagram showing serverless microservices integration with Lambda, DynamoDB, API Gateway, SQS, S3, and Bedrock services connected through numbered process flow steps](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/13/ML-193002.png)

## Solution process

This section explains the end-to-end process of the solution. The solution guidance provides further details and information on how you can replicate the
[solution](https://github.com/aws-solutions-library-samples/guidance-for-virtual-try-ons-on-aws)
.

When your customer initiates a try-on request, they first sign in on
[Amazon Cognito](https://aws.amazon.com/cognito/)
and then upload their photo(s) stored into Amazon S3. A workflow is available to auto populate the product table in DynamoDB through Amazon S3 events. The client establishes a WebSocket connection through API Gateway, creating a persistent channel for real-time updates. The client sends the ID of the product they want to virtually try as well as the S3 URL of the static model they want to use. A Lambda function processes this request by retrieving the product image URL from DynamoDB and creating a job entry with both image URLs, returning a unique job ID for tracking.

DynamoDB stream then triggers a step function to coordinate the different writes and updates in the DynamoDB table. The step function also invokes Amazon Nova Canvas virtual try-on feature. The model takes as input (1) the source image, which is the base image you would like to modify (for example, the image of the customer), (2) the reference image, which is an image containing the product(s) you want to insert into the base image. For garments, the reference image can contain garments on or off body and can even contain multiple products representing distinct outfit components (such as a shirt, pants, and shoes in a single image).

By default, a mask is computed automatically using auxiliary inputs (
`maskType: "GARMENT"`
or
`maskType: "PROMPT"`
). The mask image can either be provided directly by the developer (
`maskType: "IMAGE"`
).

When a mask type of
`“GARMENT”`
is specified, Amazon Nova Canvas will create a garment-aware mask based on a
`garmentClass`
input parameter value you specify. In most cases, you will use one of the following high-level garment classes:

* `"UPPER_BODY"`
  – Creates a mask that includes full arm length.
* `"LOWER_BODY"`
  – Creates a mask the includes full leg length with no gap between the legs.
* `"FOOTWEAR"`
  – Creates a mask that fits the shoe profile demonstrated in the source image.
* `"FULL_BODY"`
  – Creates a mask equivalent to the combination of
  `"UPPER_BODY"`
  and
  `"LOWER_BODY"`
  .

The following table shows example inputs with
`maskType: "GARMENT"`
.

|  |  |  |  |
| --- | --- | --- | --- |
| **Source** | **Reference** | **Garment class** | **Output** |
| Product photograph of white, gray, red, and black color-blocked athletic sneakers with white laces worn with gray pants against minimalist white background with geometric shadows | Pair of modern athletic running shoes displayed from multiple angles featuring white, gray, black, and red color scheme with visible air cushioning technology on white background |  | Close-up product photograph of polished black leather oxford dress shoes worn with gray business trousers in professional setting with natural lighting and minimal background |

The following table shows example inputs with
`maskType: "PROMPT"`
.

|  |  |  |  |
| --- | --- | --- | --- |
| **Source image** | **Mask prompt** | **Reference image** | **Output** |
| Modern living room interior design featuring dark gray sofa, warm beige walls, geometric circular wall art, brass pendant lights, and carefully arranged furniture with neutral color palette | Contemporary home office setup with laptop and enlarged display screen surrounded by decorative furniture, brass pendant lights, framed geometric artwork, and minimalist aesthetic in warm neutral tones | Modern two-seater sofa upholstered in burnt orange fabric with wooden tapered legs, featuring clean mid-century design lines and cushioned armrests on white background | 3D rendered modern living room interior design with vibrant orange sofa as focal point, moon phase wall art, brass pendant lights, mid-century furniture, and warm beige color scheme |

There are also more fine-grained subclasses that can be useful in certain edge cases. By using the
`“PROMPT”`
mask type, you can use natural language to describe the item in the source image that you want to replace. This is useful for images of items other than garments. This feature uses the same auto-masking functionality that exists in the Nova Canvas
`“INPAINTING”`
task using the
`maskPrompt`
parameter.

By using the mask and understanding which garment areas needs to be replaced, the product image is inserted on the user’s photo as input. The model then generates the try-on image, which is stored in Amazon S3 with the job ID as metadata. Throughout this process, the system sends progress updates through the WebSocket connection. An Amazon S3 event notification triggers a Lambda function through Amazon SQS. The function generates a presigned URL for the result image and delivers it to the client through the established WebSocket connection. This completes the process, typically taking 7–11 seconds.

## Implementation details

This section details the tables and schema used in our virtual try-on solution to help you further understand how the role each DynamoDB tables plays.

This solution uses four DynamoDB tables. The
`products_table`
stores the catalog of available items for virtual try-on. The
`virtual_try_on_jobs`
table maintains the state and tracking information for each try-on request. The
`vto-models`
table stores the catalog of customers images used for virtual try-on. The WebSocket connections table (
`vto-connections`
) tracks active WebSocket connections for real-time job status updates. The solution assumes the products table is prepopulated with the retailer’s inventory.

The products table (
`vto-products`
) stores the catalog of available items for virtual try-on. Products are automatically populated when images are uploaded to the /products/ S3 folder. The schema for the products table is as follows:

* **product\_id (string, partition key)**
  – Unique identifier for the product
* **product\_picture\_s3\_url (string)**
  – Amazon S3 URL of the original product image
* **name (string)**
  – Product display name
* **category (string)**
  – Product category for organization
* **description (string)**
  – Product details including style, color, and size options
* **auto\_imported (Boolean)**
  – Flag indicating if product was imported automatically through Amazon S3 upload
* **created\_at (string)**
  – ISO timestamp when product was added
* **updated\_at (string)**
  – ISO timestamp of last modification

The models table (
`vto-models`
) stores the catalog of customer images used for virtual try-on. Models are automatically populated when images are uploaded to the
`/models/ S3`
folder. The schema for the models table is as follows:

* **model\_id (string, partition key)**
  – Unique identifier for the model
* **model\_picture\_s3\_url (string)**
  – Amazon S3 URL of the model image
* **name (string)**
  – Model display name
* **category (string)**
  – Model category for organization
* **description (string)**
  – Model details and characteristics
* **auto\_imported (Boolean)**
  – Flag indicating if model was imported automatically using Amazon S3 upload
* **created\_at (string)**
  – ISO timestamp when model was added
* **updated\_at (string)**
  – ISO timestamp of last modification

The virtual try-on jobs table (
`vto-jobs`
) maintains state and tracking information for each try-on request throughout the processing workflow. The schema for the virtual try-on jobs table is as follows:

* **id (string, partition key)**
  – Unique identifier for each try-on job
* **model\_id (string)**
  – Reference to the model used
* **product\_id (string)**
  – Reference to the product being tried on
* **model\_picture\_s3\_url (string)**
  – Amazon S3 URL of the customer’s uploaded photo
* **product\_picture\_s3\_url (string)**
  – Amazon S3 URL of the product being tried on
* **result\_s3\_url (string)**
  – Amazon S3 URL of the generated virtual try-on result image
* **status (string)**
  – Current job status (created, processing, completed, or error)
* **parameters (map)**
  – Virtual try-on API parameters (such as
  `maskType`
  ,
  `mergeStyle`
  , or
  `garmentClass`
  )
* **connection\_id (string)**
  – WebSocket connection ID for real-time updates
* **error\_message (string)**
  – Error details if job fails
* **created\_at (string)**
  – ISO timestamp when job was created
* **updated\_at (string)**
  – ISO timestamp of last status update

The WebSocket connections table (
`vto-connections`
) tracks active WebSocket connections for real-time job status updates. Further information on how using WebSocket API can be found at the
[Create a WebSocket chat app with a WebSocket API, Lambda, and DynamoDB](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html)
tutorial. The schema is as follows:

* **connection\_id (string, partition key)**
  – WebSocket connection identifier
* **connected\_at (string)**
  – ISO timestamp when connection was established
* **ttl (number)**
  – Time-to-live for automatic cleanup of stale connections

## Conclusion

In this post, we covered how to implement virtual try-on at scale, covering the main building blocks. For a quick start, we provide a complete
[GitHub sample](https://github.com/aws-solutions-library-samples/guidance-for-virtual-try-ons-on-aws)
with prerequisites, deployment scripts, example code and a comprehensive solution guidance document with best practices and configuration details. Use this guide to get started right away in experimenting with the solution.

As ecommerce continues to grow, reducing return rates while maintaining customer satisfaction becomes increasingly critical for retailers’ profitability and sustainability. This Virtual try-on solution demonstrates how AWS serverless services can be combined with generative AI to address a significant challenge. By using Amazon Nova Canvas alongside a robust serverless architecture, retailers can provide customers with accurate product visualization and pose conservation while maintaining the seamless shopping experience their most loyal customers expect. Implementation considerations extend beyond the technical architecture. Successful deployment requires careful attention to service quotas, monitoring, and cost optimization. Our solution guidance provides further detailed recommendations for managing WebSocket connections, implementing retry strategies, and optimizing resource utilization. These operational aspects are crucial for maintaining reliable performance during peak shopping periods while managing costs effectively.

---

### About the authors

### Amandine Annoye

Amandine Annoye is a Solutions Architect at AWS, she works with Luxury & Fashion customers in France to help them drive business value. Amandine enjoys translating customers business needs into concrete and effective technical solutions. Outside of work, she enjoys travelling and painting.

### Kevin Polossat

Kevin Polossat is a Solutions Architect at AWS. He works with retail & CPG customers in France to help them create value through cloud adoption. Outside of work, he enjoys wine and cheese.

### Leopold Cheval

Leopold Cheval is a Solutions Architect at AWS based in Paris, working with Media & Entertainment and Retail customers on their cloud journey. He focuses on modern applications, AI/ML, and Generative AI technologies. Outside of work, Leopold enjoys traveling and camping.

### Rania Khemiri

Rania Khemiri is a Prototyping Architect at AWS. She focuses on agentic workflows and Generative AI applications, helping teams accelerate experimentation and adoption of AI technologies on AWS. Through hands-on prototyping, she empowers customers to transform ideas into functional proofs of concept and gain the skills to scale them into production.