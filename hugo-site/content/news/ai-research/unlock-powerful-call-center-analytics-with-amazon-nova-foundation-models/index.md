---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-06T00:15:31.373355+00:00'
exported_at: '2026-03-06T00:15:34.738452+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/unlock-powerful-call-center-analytics-with-amazon-nova-foundation-models
structured_data:
  about: []
  author: ''
  description: In this post, we discuss how Amazon Nova demonstrates capabilities
    in conversational analytics, call classification, and other use cases often relevant
    to contact center solutions. We examine these capabilities for both single-call
    and multi-call analytics use cases.
  headline: Unlock powerful call center analytics with Amazon Nova foundation models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/unlock-powerful-call-center-analytics-with-amazon-nova-foundation-models
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Unlock powerful call center analytics with Amazon Nova foundation models
updated_at: '2026-03-06T00:15:31.373355+00:00'
url_hash: bcee7b29a9cf8f6f9c9cf14c4dde7b059ebbf12c
---

Call center analytics play a crucial role in improving customer experience and operational efficiency. With foundation models (FMs), you can improve the quality and efficiency of call center operations and analytics. Organizations can use generative AI to assist human customer support agents and managers of contact center teams, so they can gain insights that are more nuanced, helping redefine how and what questions can be asked from call center data.

Whereas some organizations look for turnkey solutions to introduce generative AI into their operations, such as
[Amazon Connect Contact Lens](https://aws.amazon.com/connect/contact-lens/)
, others build custom customer support systems using AWS services for their microservices backend. With this comes the opportunity to integrate FMs into the system to provide AI support to human customer support agents and their managers.

One of the major decisions these organizations face is which model to use to power the AI support and analytics in their platform. For this, the
[Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/)
developed a demo application that features a collection of use cases powered by Amazon’s latest family of FMs,
[Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/)
. In this post, we discuss how Amazon Nova demonstrates capabilities in conversational analytics, call classification, and other use cases often relevant to contact center solutions. We examine these capabilities for both single-call and multi-call analytics use cases.

## Amazon Nova FMs for scale

Amazon Nova FMs provide leading price-performance, making them suitable for generative AI at scale. These models are pre-trained on vast amounts of data, enabling them to perform a wide range of language tasks with remarkable accuracy and efficiency while effectively scaling to support large demand. In the context of call center analytics, Amazon Nova models can comprehend complex conversations, extract key information, and generate valuable insights that were previously difficult or impossible to obtain at scale. The demo application showcases the capabilities of Amazon Nova models for various analytical tasks, including:

* Sentiment analysis
* Topic identification
* Vulnerable customer assessment
* Protocol adherence checking
* Interactive question-answering

By using these advanced AI capabilities from Amazon Nova FMs, businesses can gain a deeper understanding of their customer interactions and make data-driven decisions to improve service quality and operational efficiency.

## Solution overview

The Call Center Analytics demo application is built on a simple architecture that seamlessly integrates
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
and Amazon Nova to enable end-to-end call center analytics for both single-call and multi-call analytics. The following diagram illustrates this architecture.

![call center diagram analytics machine learning aws ](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/10/call-center-diagram.png)

* [Amazon Bedrock](https://aws.amazon.com/bedrock/)
  – Provides access to the Amazon Nova FMs, enabling powerful natural language processing capabilities
* [Amazon Athena](https://aws.amazon.com/athena/)
  – Used for querying the call data stored in a structured format, allowing for efficient data retrieval and analysis
* [Amazon Transcribe](https://aws.amazon.com/transcribe/)
  – Fully managed, automatic speech recognition (ASR) service
* [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
  – Object storage service offering industry-leading scalability, data availability, security, and performance
* [Streamlit](https://streamlit.io/)
  – Powers the web-based UI, providing an intuitive and interactive experience for users

The application is divided into two main components: Single Call Analytics and Multi-Call Analytics. These scripts work together to provide a comprehensive solution that combines post-call analysis with historical data insights.

## Single Call Analytics

The Single Call Analytics functionality of the application provides a detailed analysis of individual customer service calls. This feature is implemented in the Single\_Call\_Analytics.py script. In this section, we explore some of the key capabilities.

### Sentiment analysis and vulnerable customer assessment

The solution uses Amazon Nova FMs to derive insights on both the customer and agent sentiment, as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/10/image2.png)

By using the chatbot feature, users can ask for an explanation on why the sentiment was classified as such and also get references from the transcription. This feature gives more understanding on the sentiment class by quickly finding supporting phrases from the transcription itself, which later can be used for other analyses.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/10/image3.png)

A vulnerable customer or potentially vulnerable customer is someone who, due to their personal circumstances, is particularly susceptible to financial harm or requires special consideration in financial services. The application assesses whether the customer calling in might be considered vulnerable or potentially vulnerable, by passing the call transcript of the selected call with the following prompt:

```
vc_prompt = f"""You are a AI Assistant for Banking Call Center.
Your goal is to determine if the customer in the <call_transcription> below
qualifies as Vulnerable Customer (VC) or Potentially Vulnerable Customer (PVC).

<call_transcription>
{speaker_texts}
</call_transcription>

If the customer qualifies as a VC or PVC, return Yes and explain why.
If the customer does not qualify as a VC or PVC, return No and explain why.
"""

isVC = invoke_llm(vc_prompt, vc_model)
```

In this prompt, the Amazon Nova FM uses a generic definition of a vulnerable or potentially vulnerable customer to make the assessment. However, if a business has its own definition of vulnerable or potentially vulnerable customers, they can engineer the prompt to have the FM make the classification using this custom definition. This feature helps call center managers identify potentially sensitive situations and make sure vulnerable customers receive appropriate care and attention along with an explanation on why the customer was identified as such.

### Protocol assistance and step completion

The application uses Amazon Nova models to identify the relevant protocol for each call and check if the agent followed the prescribed steps. Protocols are currently defined in a JSON file that are ingested locally at runtime. The following code shows an example of how this is implemented:

```
protocol_identification_formatted = protocol_identification_prompt.format(transcript=context, protocols=protocols)
llm_protocol_key = invoke_llm(protocol_identification_formatted, protocol_model)

step_completion_formatted = step_completion_prompt.format(protocol_steps=protocol_list, context=context)
step_check = invoke_llm(step_completion_formatted, protocol_model)
```

This code snippet shows how the application first identifies the relevant protocol using the call transcript and a list of available protocols. After the protocol has been identified, the call transcript and protocol steps for the determined protocol are passed together to check if each step of the protocol was completed by the agent. The results are displayed in a user-friendly format, helping managers quickly assess agent performance and adherence to guidelines.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/10/image4.png)

### Interactive transcription view and AI assistant

The Single Call Analytics page provides an interactive transcription view, so users can read through the conversation between the agent and customer. Additionally, it includes an AI assistant feature so users can ask specific questions about the call:

```
user_message = call_prompt.format(query=prompt, context=context, chat_history=st.session_state.messages)
ans = invoke_llm(user_message, cb_model)
```

This assistant functionality, powered by Amazon Nova models, helps users gain deeper insights into specific aspects of the call without having to manually search through the transcript.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/02/ml-18030-image-5.png)

## Multi-Call Analytics

The Multi-Call Analytics functionality, implemented in the Multi\_Call\_Analytics.py script, provides aggregate analysis across multiple calls and enables powerful business intelligence (BI) queries.

### Data visualization and flexible model selection

This feature helps users quickly visualize trends and patterns across multiple calls, making it straightforward to identify areas for improvement or success.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/10/image6.png)

The “Top 5 Call Topics” visual in the preceding screenshot is also powered by Amazon Nova models; users can classify the call’s topic from passing in the call transcript and then letting the model determine what the main topic of the call was. This feature can help users quickly classify calls and place them in the bucket of the determined topic to generate visuals. By seeing the top reasons customers are calling in, businesses can focus on devising strategies to reduce call volumes for these topic categories. Additionally, the application provides flexible model selection options, so users can choose between different Amazon Nova models (such as Nova Pro, Nova Lite, and Nova Micro) for various analytical tasks. This flexibility means users can select the most appropriate model for their specific needs and use cases.

### Analytical AI Assistant

One of the key features of the Multi-Call Analytics page is the Analytical AI Assistant, which can handle complex BI queries using SQL.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/10/image7.png)

The following code demonstrates how the application uses Amazon Nova models to generate SQL queries based on natural language questions:

```
user_prompt = """Given the following schema:
{schema}
and a user query, generate a SQL query which can be executed in AWS Athena.
The table name is {table_name}.

Give the SQL query as a JSON response.
"""

sql_query, chart = invoke_llm(final_prompt, cb_model, "sql")
```

The assistant can understand complex queries, translate them into SQL, and even suggest appropriate chart types for visualizing the results. The SQL queries are run on processed data from Amazon Transcribe and queried using Athena, which are then surfaced in the Analytical AI Assistant.

## Implementation

The Call Analytics demo application is implemented using the Streamlit UI for speed and simplicity of development. The application is a mix of specific use cases and AI tasks to provide a sample of what Amazon Nova models can do for call center operations and analytics use cases. For more information about how this demo application is implemented, refer to the following
[GitHub repo](https://github.com/aws-samples/sample-for-Unlocking-Powerful-Call-Center-Analytics-with-Amazon-Nova-Foundation-Models)
.

## Conclusion

In this post, we discussed how Amazon Nova FMs power the Call Center Analytics demo application, representing significant advancements in the field of call center analytics. By using the power of these advanced AI models, businesses can gain unique insights into their customer interactions, improve agent performance, and enhance overall operational efficiency. The application’s comprehensive features, including sentiment analysis, protocol adherence checking, vulnerable customer assessment, and powerful BI capabilities, provide call center managers the tools they need to make data-driven decisions and continuously improve their customer service operations.

As Amazon Nova FMs continue to evolve and improve, we can expect even more powerful and sophisticated analytics capabilities in the future. This demo serves as an excellent starting point for customers looking to explore the potential of AI-powered call center analytics and applying it in their own environment. We encourage readers to explore the Call Center Analytics demo to learn more details of how Amazon Nova models are integrated in the application.

---

### About the authors

### Francisco Calderon Rodriguez

Francisco Calderon Rodriguez is a Data Scientist at the Generative AI Innovation Center (GAIIC). As a member of the GAIIC, he helps discover the art of the possible with AWS customers using generative AI technologies. In his spare time, Francisco likes playing music and guitar, playing soccer with his daughters, and enjoying time with his family.

### Harpreet Cheema

Harpreet Cheema is a Deep Learning Architect at the AWS Generative AI Innovation Center. He is very passionate in the field of machine learning and in tackling different problems in the ML domain. In his role, he focuses on developing and delivering Generative AI focused solutions for real-world applications.

### Jamal Saboune

Jamal Saboune is an Applied Science Manager with AWS Generative AI Innovation Center. He is currently leading a team focused on supporting AWS customers build innovative and scalable Generative AI products across several industries. Jamal holds a PhD in AI and Computer Vision from the INRIA Lab in France, and has a long R&D experience designing and building AI solutions that add value to users.