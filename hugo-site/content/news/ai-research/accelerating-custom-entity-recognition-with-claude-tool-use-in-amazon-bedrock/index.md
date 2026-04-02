---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:03:54.433235+00:00'
exported_at: '2026-04-02T04:03:57.340005+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-custom-entity-recognition-with-claude-tool-use-in-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: This post introduces Claude Tool use in Amazon Bedrock which uses the
    power of large language models (LLMs) to perform dynamic, adaptable entity recognition
    without extensive setup or training.
  headline: Accelerating custom entity recognition with Claude tool use in Amazon
    Bedrock
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/accelerating-custom-entity-recognition-with-claude-tool-use-in-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Accelerating custom entity recognition with Claude tool use in Amazon Bedrock
updated_at: '2026-04-02T04:03:54.433235+00:00'
url_hash: bef5820c3ebfda8f5e62e664f3a6ad44c0f82af6
---

Businesses across industries face a common challenge: how to efficiently extract valuable information from vast amounts of unstructured data. Traditional approaches often involve resource-intensive processes and inflexible models. This post introduces a game-changing solution:
[Claude Tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html)
in
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
which uses the power of large language models (LLMs) to perform dynamic, adaptable entity recognition without extensive setup or training.

In this post, we walk through:

* What Claude Tool use (function calling) is and how it works
* How to use Claude Tool use to extract structured data using natural language prompts
* Set up a serverless pipeline with Amazon Bedrock,
  [AWS Lambda](https://aws.amazon.com/lambda/)
  , and
  [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/)
* Implement dynamic entity extraction for various document types
* Deploy a production-ready solution following AWS best practices

## **What is Claude Tool use (function calling)?**

Claude Tool use, also known as function calling, is a powerful capability that allows us to augment Claude’s abilities by establishing and invoking external functions or tools. This feature enables us to provide Claude with a collection of pre-established tools that it can access and employ as needed, enhancing its functionality.

## **How Claude Tool use works with Amazon Bedrock**

Amazon Bedrock is a fully managed generative artificial intelligence (AI) service that offers a range of high-performing foundation models (FMs) from industry leaders like Anthropic. Amazon Bedrock makes implementing Claude’s Tool use remarkably straightforward:

1. Users define a set of tools, including their names, input schemas, and descriptions.
2. A user prompt is provided that may require the use of one or more tools.
3. Claude evaluates the prompt and determines if any tools could be helpful in addressing the user’s question or task.
4. If applicable, Claude selects which tools to utilize and with what input.

## **Solution overview**

In this post, we demonstrate how to extract custom fields from driver’s licenses using Claude Tool use in Amazon Bedrock. This serverless solution processes documents in real-time, extracting information like names, dates, and addresses without traditional model training.

## **Architecture**

Our custom entity recognition solution uses a serverless architecture to process documents efficiently and extract relevant information using Amazon Bedrock’s Claude model. This approach minimizes the need for complex infrastructure management while providing scalable, on-demand processing capabilities.

The solution architecture uses several AWS services to create a seamless pipeline. Here’s how the process works:

1. Users upload documents into Amazon S3 for processing
2. An S3 PUT event notification triggers an AWS Lambda function
3. Lambda processes the document and sends it to Amazon Bedrock
4. Amazon Bedrock invokes Anthropic Claude for entity extraction
5. Results are logged in Amazon CloudWatch for monitoring

The following diagram shows how these services work together:

![AWS architecture diagram showing a serverless driver's license information extraction system using Amazon S3, Lambda, Bedrock with Claude 4.5 Sonnet, and CloudWatch Logs, along with Lambda configuration screens and sample input/output data.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/14/ML-17616-1.png)

### **Architecture components**

* **Amazon S3:**
  Stores input documents
* **AWS Lambda**
  : Triggers on file upload, sends prompts and data to Claude, stores results
* **Amazon Bedrock (Claude):**
  Processes input and extracts entities
* **Amazon CloudWatch**
  : Monitors and logs workflow performance

### **Prerequisites**

### **Step-by-step implementation guide:**

This implementation guide demonstrates how to build a serverless document processing solution using Amazon Bedrock and related AWS services. By following these steps, you can create a system that automatically extracts information from documents like driver’s licenses, avoiding manual data entry and reducing processing time. Whether you’re handling a few documents or thousands, this solution can scale automatically to meet your needs while maintaining consistent accuracy in data extraction.

1. **Setting Up Your Environment (10 minutes)**
   1. [Create](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)
      source S3 bucket for the input (for example, driver-license-input).
   2. Configure IAM roles and permissions:

```
{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "bedrock:InvokeModel",
         "Resource": "arn:aws:bedrock:*::foundation-model/*", "arn:aws:bedrock:*:111122223333:inference-profile/*”
       },
       {
         "Effect": "Allow",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
       }
     ]
   }
```

2. ****Creating the Lambda function (30 minutes)****
   This Lambda function is triggered automatically when a new image is uploaded to your S3 bucket. It reads the image, encodes it in base64, and sends it to Claude 4.5 Sonnet via Amazon Bedrock using the Tool use API.The function defines a single tool called
   **extract\_license\_fields**
   for demonstration purposes. However, you can define tool names and schemas based on your use case — for example, extracting insurance card data, ID badges, or business forms. Claude dynamically selects whether to call your tool based on prompt relevance and input structure.

   We’re using
   **“tool\_choice”: “auto”**
   to let Claude decide when to invoke the function. In production use cases, you may want to hardcode
   **“tool\_choice”: { “type”: “tool”, “name”: “your\_tool\_name” }**
   for deterministic behavior.
   1. Go to
      [AWS Lambda console](https://us-east-1.console.aws.amazon.com/lambda/)
      * Choose
        **Create function.**
      * Select
        **Author from scratch.**
      * Set runtime to
        **Python 3.12.**
      * Choose
        **Create Function.

        ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/14/ML-17616-3.png)**
   2. Configure Lambda Timeout
      * In your Lambda function configuration, click
        **General Configuration**
        tab.
      * Under
        **General Configuration**
        , click
        **Edit**
      * For
        **Timeout**
        , increase from default 3 seconds to at least 30 seconds. We recommend setting it to 1-2 minutes for larger images.
      * Choose
        **Save**
        .

        ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/14/ML-17616-5.png)
        **Note:**
        This adjustment is crucial because processing images through Claude may take longer than Lambda’s default timeout, especially for high-resolution images or when processing multiple fields. Monitor your function’s execution time in CloudWatch Logs to fine-tune this setting for your specific use case.
   3. Paste this code in the
      **lambda\_function.py**
      code file:

      ```
      import boto3, json
      import base64

      def lambda_handler(event, context):
          bedrock = boto3.client("bedrock-runtime")
          s3 = boto3.client("s3")

          bucket = event["Records"][0]["s3"]["bucket"]["name"]
          key = event["Records"][0]["s3"]["object"]["key"]
          file = s3.get_object(Bucket=bucket, Key=key)

          # Convert image to base64
          image_data = file["Body"].read()
          base64_image = base64.b64encode(image_data).decode('utf-8')

          # Define tool schema
          tools = [{
              "name": "extract_license_fields",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "first_name": { "type": "string" },
                      "last_name": { "type": "string" },
                      "issue_date": { "type": "string" },
                      "license_number": { "type": "string" },
                      "address": {
                          "type": "object",
                          "properties": {
                              "street": { "type": "string" },
                              "city": { "type": "string" },
                              "state": { "type": "string" },
                              "zip": { "type": "string" }
                          }
                      }
                  },
                  "required": ["first_name", "last_name", "issue_date", "license_number", "address"]
              }
          }]

          payload = {
              "anthropic_version": "bedrock-2023-05-31",
              "max_tokens": 2048,
              "messages": [{
                  "role": "user",
                  "content": [
                      {
                          "type": "image",
                          "source": {
                              "type": "base64",
                              "media_type": "image/jpeg",
                              "data": base64_image
                          }
                      },
                      {
                          "type": "text",
                          "text": "Extract the driver's license fields from this image."
                      }
                  ]
              }],
              "tools": tools
          }

          try:
              response = bedrock.invoke_model(
                  modelId="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
                  body=json.dumps(payload)
              )

              result = json.loads(response["body"].read())

              # Print every step for debugging
              print("1. Raw Response:", json.dumps(result, indent=2))

              if "content" in result:
                  print("2. Content found in response")
                  for content in result["content"]:
                      print("3. Content item:", json.dumps(content, indent=2))

                      if isinstance(content, dict):
                          print("4. Content type:", content.get("type"))

                          if content.get("type") == "text":
                              print("5. Text content:", content.get("text"))

                          if content.get("type") == "tool_calls":
                              print("6. Tool calls found")
                              extracted = json.loads(content["tool_calls"][0]["function"]["arguments"])
                              print("7. Extracted data:", json.dumps(extracted, indent=2))

              return {
                  "statusCode": 200,
                  "body": json.dumps({
                      "message": "Process completed",
                      "raw_response": result
                  }, indent=2)
              }

          except Exception as e:
              print(f"Error occurred: {str(e)}")
              return {
                  "statusCode": 500,
                  "body": json.dumps({
                      "error": str(e),
                      "type": str(type(e))
                  })
              }
      ```
   4. Deploy the Lambda Function: After pasting the code, choose the
      **Deploy**
      button on the left side of the code editor and wait for the deployment confirmation message.

      **Important:**
      Always remember to deploy your code after making changes. This ensures that your latest code is saved and will be executed when the Lambda function is triggered.
3. **Working with Claude Tool use schemas**
   1. Amazon Bedrock with Claude 4.5 Sonnet supports function calling using Tool use — where you define callable tools with clear JSON schemas. A valid tool entry must include:
      * **name:**
        Identifier for your tool (e.g.
        `extract_license_fields`
        )
      * **input\_schema:**
        JSON schema that defines required fields, types, and structure
   2. Example Tool use definition:

      ```
      [{
        "name": "extract_license_fields",
        "input_schema": {
          "type": "object",
          "properties": {
            "first_name": { "type": "string" },
            "last_name": { "type": "string" },
            "issue_date": { "type": "string" },
            "license_number": { "type": "string" },
            "address": {
              "type": "object",
              "properties": {
                "street": { "type": "string" },
                "city": { "type": "string" },
                "state": { "type": "string" },
                "zip": { "type": "string" }
              }
            }
          },
          "required": ["first_name", "last_name", "issue_date", "license_number", "address"]
        }
      }]
      ```
   3. You can define multiple tools in the
      **tools array**
      . Claude selects one (or none) depending on the
      **tool\_choice**
      value and how well the prompt matches a given schema.
4. **Configure S3 Event Notification (5 minutes)**
   1. Open the Amazon S3 console.
      * Select your S3 bucket.
      * Click the
        **Properties**
        tab.
      * Scroll down to
        **Event notifications.**
      * Click
        **Create event notification.**
      * Enter a name for the notification (e.g., “LambdaTrigger”).
      * Under
        **Event types**
        , select
        **PUT.**
      * Under
        **Destination**
        , select
        **Lambda function.**
      * Choose your Lambda function from the dropdown.
      * Click
        **Save changes.**
5. **Testing and Validation (15 minutes)**
   1. **Supported Formats:**
      Claude 4.5 supports image inputs in JPEG, PNG, WebP, and single-frame GIF formats.
      **Note:**
      While this implementation currently supports only
      **.jpeg**
      images, you can extend support for other formats by modifying the
      **media\_type**
      field in the Lambda function to match the uploaded file’s MIME type.
   2. **Size and Resolution Limits:**
      * Max image size: 20 MB
      * Recommended resolution: 300 DPI or higher
      * Max dimensions: 4096 x 4096 pixels
      * Images larger than this may fail to process or produce inaccurate results.
6. **Preprocessing Tips for Better Accuracy:**
   1. Crop the image tightly to remove noise and irrelevant sections.
   2. Adjust contrast and brightness to ensure text is clearly legible.
   3. De-skew scans and ensure text is horizontally aligned.
   4. Avoid low-resolution screenshots or images with heavy compression artifacts.
   5. Prefer white backgrounds and dark text for maximum OCR clarity.
7. Upload Test Image:

   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/14/ML-17616-7.jpg)
   1. Open your S3 bucket
   2. Upload a driver’s license image (supported formats: .jpeg, .jpg).
   3. Note: Ensure image is clear and readable for best results.
8. Monitor CloudWatch Logs
   1. Go to the
      [Amazon CloudWatch console](https://us-east-1.console.aws.amazon.com/cloudwatch)
      .
   2. Click on
      **Log groups**
      in the left navigation.
   3. Search for your Lambda function name
      `invoke_drivers_license`
      .
   4. Click on the latest log stream (sorted by timestamp).
   5. View the execution results, which shows this sample output:

```
{
  "type": "tool_use",
  "id": "toolu_bdrk_01Ar6UG7BcARjqAKsiSPyNdf",
  "name": "extract_license_fields",
  "input": {
        "first_name": "JANE",
        "last_name": "DOE",
        "issue_date": "05/05/2025",
        "license_number": "111222333",
        "address": {
            "street": "123 ANYWHERE STREET",
            "city": "EXAMPLE CITY",
            "state": "VA",
            "zip": "00000"
               }
           }
 }
```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/14/ML-17616-9-1.png)

### **Performance optimization**

* Configure Lambda memory and timeout settings
* Implement batch processing for multiple documents
* Use S3 event notifications for automatic processing
* Add CloudWatch metrics for monitoring

### **Security best practices**

* Implement encryption at rest for S3 buckets
* Use
  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
  keys for sensitive data
* Apply least privilege IAM policies
* Enable virtual private cloud (VPC) endpoints for private network access

### **Error handling and monitoring**

1. Claude’s output is structured as a list of content blocks, which may include text responses,
   **tool\_calls**
   , or other data types. To debug:
   1. Always log the raw response from Claude.
   2. Check if
      `tool_calls`
      is present in the response.
   3. Use a try-except block around the function call to catch errors like malformed payloads or model timeouts.
2. Here’s a minimal error handling pattern:

```
try:
    result = json.loads(response["body"].read())
    if "tool_calls" in result.get("content", [{}])[0]:
        args = result["content"][0]["tool_calls"][0]["function"]["arguments"]
        print("Extracted Fields:", json.dumps(json.loads(args), indent=2))
except Exception as e:
    print("Error occurred:", str(e))
```

### **Clean Up**

1. Delete S3 bucket and contents.
2. Remove Lambda functions.
3. Delete IAM roles and policies.
4. Disable Bedrock access if no longer needed.

### **Conclusion**

Claude Tool use in Amazon Bedrock provides a powerful solution for custom entity extraction, minimizing the need for complex machine learning (ML) models. This serverless architecture enables scalable, cost-effective processing of documents with minimal setup and maintenance. By leveraging the power of large language models through Amazon Bedrock, organizations can unlock new levels of efficiency, insight, and innovation in handling unstructured data.

### **Next steps**

We encourage you to explore this solution further by implementing the sample code in your environment and customizing it for your specific use cases. Join the discussion about entity extraction solutions in the
[AWS re:Post](https://repost.aws/)
community, where you can share your experiences and learn from other developers.

For deeper technical insights, explore our comprehensive documentation on
[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/)
,
[AWS Lambda](https://docs.aws.amazon.com/lambda/)
, and
[Amazon S3](https://docs.aws.amazon.com/s3/)
. Consider enhancing your implementation by integrating with
[Amazon Textract](https://aws.amazon.com/textract/)
for additional document processing features or
[Amazon Comprehend](https://aws.amazon.com/comprehend/)
for advanced text analysis. To stay updated on similar solutions, subscribe to our
[AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/)
and explore more examples in the
[AWS Samples GitHub repository](https://github.com/aws-samples/)
. If you’re new to AWS machine learning services, check out our
[AWS Machine Learning University](https://aws.amazon.com/machine-learning/mlu/)
or explore our
[AWS Solutions Library.](https://aws.amazon.com/solutions)
For enterprise solutions and support, reach out through your
[AWS account team](https://aws.amazon.com/contact-us/)
.

---

## About the authors

Kimo is an AWS Solutions Architect with expertise spanning infrastructure, storage, security, GenAI, and data analytics, among other areas. He is passionate about working with customers across various industry verticals, helping them leverage AWS services to drive their digital transformation and meet their business needs.