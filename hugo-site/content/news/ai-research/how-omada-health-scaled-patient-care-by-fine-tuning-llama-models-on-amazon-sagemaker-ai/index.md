---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-12T18:15:27.015461+00:00'
exported_at: '2026-01-12T18:15:29.386245+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-omada-health-scaled-patient-care-by-fine-tuning-llama-models-on-amazon-sagemaker-ai
structured_data:
  about: []
  author: ''
  description: This post is co-written with Sunaina Kavi, AI/ML Product Manager at
    Omada Health. Omada Health, a longtime innovator in virtual healthcare delivery,
    launched a new nutrition experience in 2025, featuring OmadaSpark, an AI agent
    trained with robust clinical input that delivers real-time motivational interviewing
    and nutrition education. It was built on AWS. OmadaSpark was designed […]
  headline: How Omada Health scaled patient care by fine-tuning Llama models on Amazon
    SageMaker AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-omada-health-scaled-patient-care-by-fine-tuning-llama-models-on-amazon-sagemaker-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How Omada Health scaled patient care by fine-tuning Llama models on Amazon
  SageMaker AI
updated_at: '2026-01-12T18:15:27.015461+00:00'
url_hash: cb19e7a0523443132279e02a0adafc8f758ac944
---

*This post is co-written with Sunaina Kavi, AI/ML Product Manager at Omada Health.*

[Omada Health](https://www.omadahealth.com/product-innovation)
, a longtime innovator in virtual healthcare delivery, launched a new nutrition experience in 2025, featuring
[OmadaSpark](https://www.omadahealth.com/resource-center/omada-introduces-nutritional-intelligence-to-transform-food-relationships-with-ai-driven-tools-and-human-care)
, an AI agent trained with robust clinical input that delivers real-time motivational interviewing and nutrition education. It was built on AWS. OmadaSpark was designed to help members identify their own motivational challenges like emotional eating, improve food decisions, set goals, and sustain lasting behavior change. The following screenshot shows an example of OmadaSpark’s Nutritional Education feature, demonstrating how members receive personalized nutrition education in real time.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/09/image001.gif)

In this post, we examine how Omada partnered with AWS and Meta to develop this healthcare-aligned AI solution using Llama models on
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/?trk=b6c2fafb-22b1-4a97-a2f7-7e4ab2c7aa28&sc_channel=ps&ef_id=CjwKCAjw3f_BBhAPEiwAaA3K5BEEs8CWsy3c2xQelhxVhLlyQ2WCZOsGLxOdRLT-9ofpmVF6YVukVBoCpfkQAvD_BwE:G:s&s_kwcid=AL!4422!3!651751060692!e!!g!!amazon%20sagemaker!19852662230!145019225977&gad_campaignid=19852662230&gbraid=0AAAAADjHtp-RNjX9lRRxTXDmKmqbpRgmE&gclid=CjwKCAjw3f_BBhAPEiwAaA3K5BEEs8CWsy3c2xQelhxVhLlyQ2WCZOsGLxOdRLT-9ofpmVF6YVukVBoCpfkQAvD_BwE)
. We explore the technical implementation, architecture, and evaluation process that helped Omada scale personalized nutrition guidance while maintaining their commitment to evidence-based care.

## The opportunity for AI-powered nutrition guidance

Nutrition education serves as a cornerstone of Omada’s chronic condition management programs. Although health coaches excel at providing personalized care, the growing demand for quick, convenient nutritional information presented an opportunity to enhance our coaches’ impact through technology. Omada sought an innovative solution that would complement their coaches’ expertise by handling routine analytical tasks, so they could focus more deeply on meaningful member interactions. The goal was to provide immediate, high-quality nutrition education while maintaining strict healthcare compliance with Omada’s care protocols and the personal touches that makes their program effective.

Omada Health’s OmadaSpark aims to help members identify real-world emotional and practical barriers to healthy eating in today’s environment, where ultra-processed foods are prevalent and diets can fail to deliver long-term results. OmadaSpark features motivational interviewing,using questions to help members identify their own goals, reinforce autonomy, and find motivation to change habits. OmadaSpark’s Nutritional Education feature can reduce the mental load of real-time food decisions and encourage members to gradually incorporate healthier food alternatives. Omada’s nutrition experience offers updated tracking capabilities, like water tracking, barcode scanning, and photo-recognition technology that offer flexible and non-restrictive support designed to promote a healthy relationship to food.

“We see AI as a force multiplier for our health coaches, not a replacement,” explains Terry Miller, Omada’s Vice President, Machine Learning, AI and Data Strategy. “Our collaboration with AWS and Meta allowed us to implement an AI solution that aligns with our values of evidence-based, personalized care.”

## Solution overview

Omada Health developed the Nutritional Education feature using a fine-tuned Llama 3.1 model on SageMaker AI. The implementation included the Llama 3.1 8B model fine-tuned using
[Quantized Low Rank Adaptation (QLoRA)](https://arxiv.org/abs/2305.14314)
techniques, a fine-tuning method that allows language models to efficiently learn on smaller datasets. Initial training used 1,000 question-answer pairs created from Omada’s internal care protocols and peer reviewed literature and specialty society guidelines to provide evidence-based nutritional education.

The following diagram illustrates the high-level architecture of Omada Health’s Llama implementation on AWS.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/18/omada-health-architecture.drawio.final_.drawio.png)

The solution workflow consists of the following high-level steps:

1. The Q&A pairs for nutritional education datasets are uploaded to
   [Amazon Simple Storage Service](https://aws.amazon.com/s3/)
   (Amazon S3) for model training.
2. [Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
   is used to launch a training job using Hugging Face estimators for fine-tuning Llama 3.1 8B model. QLoRA techniques are used to train the model and model artifacts saved to Amazon S3.
3. The inference workflow is invoked through a user question through a mobile client for OmadaSpark’s nutritional education feature. A request is invoked to fetch member personal data based on the user profile as well as conversation history, so that responsive information is personalized. For example, a roast beef recipe won’t be delivered to a vegetarian. At the same time, this feature does not provide medical information that is related to a particular person’s medical situation, such as their latest blood glucose test. The SageMaker AI endpoint is invoked for nutrition generation based on the member’s query and historical conversations as context.
4. The model generates personalized nutrition education, which are fed back to the mobile client, providing evidence-based education for people in Omada’s cardiometabolic programs..
5. For evaluation of the model performance,
   [LangSmith](https://www.langchain.com/langsmith/observability)
   , an observability and evaluation service where teams can monitor AI application performance, is used to capture inference quality and conversation analytics for continuous model improvement.
6. Registered Dietitians conduct human review processes, verifying clinical accuracy and safety of the nutrition education provided to users. Upvoted and downvoted responses are viewed in LangSmith annotation queues to determine future fine-tuning and system prompt updates.

The following diagram illustrates the workflow sequence in more detail.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/09/Picture1-10.png)

### Collaboration and data fine-tuning

A critical aspect of Omada Health’s success with AI implementation was the close collaboration between their clinical team and the AI development team. Omada AI/ML Product Manager Sunaina Kavi, a key figure in this collaboration, highlights the importance of this synergy:

“Our work with the clinical team was pivotal in building trust and making sure the model was optimized to meet real-world healthcare needs,” says Kavi. “By closely working on data selection and evaluation, we made sure that OmadaSpark Nutritional Education not only delivered accurate and personalized nutrition e but also upheld high standards of patient care.

“The AWS and Meta partnership gave us access to state-of-the-art foundation models while maintaining the self-hosted control we need in healthcare, for privacy, security, and quality purposes. The fine-tuning capabilities of SageMaker AI allowed us to adapt Llama to our specific nutrition use case while preserving our data sovereignty.”

Patient data protection remained paramount throughout development. Model training and inference occurred within HIPAA-compliant AWS environments (AWS is Omada’s HIPAA Business Associate), with fine-tuned model weights remaining under Omada’s control through model sovereignty capabilities in SageMaker AI. The AWS security infrastructure provided the foundation for implementation, helping maintain patient data protection throughout the AI development lifecycle. Llama models offered the flexibility needed for healthcare-specific customization without compromising performance. Omada centered their technical implementation around SageMaker AI for model training, fine-tuning, and deployment.

Finally, Omada implemented rigorous testing protocols, including regular human review of model outputs by qualified. Omada launched the entire workflow with the model in 4.5 months. Throughout this process, they continuously monitored response accuracy and member satisfaction, with iterative fine-tuning based on real-world feedback.

## Business impact

The introduction of OmadaSpark significantly boosted member engagement of those that used the tool. Members who interacted with the nutrition assistant were three times more likely to return to the Omada app in general compared to those who did not interact with the tool. By providing round-the-clock access to personalized nutritional education, Omada dramatically reduced the time it took to address member nutrition questions from days to seconds.

Following their successful launch, Omada is deepening their partnership with AWS and Meta to expand AI capabilities including fine-tuning models, context window optimization, and adding memory. They are developing a continuous training pipeline incorporating real member questions and enhancing AI features with additional health domains beyond nutrition.

“Our collaboration with AWS and Meta has shown the value of strategic partnerships in healthcare innovation,” shares Miller. “As we look to the future, we’re excited to build on this foundation to develop even more innovative ways to support our members.”

## Conclusion

Omada Health’s implementation demonstrates how healthcare organizations can effectively adopt AI while addressing industry-specific requirements and member needs. By using Llama models on SageMaker AI, Omada amplifies the humanity of health coaches and further enriches the member experience. The Omada, AWS, and Meta collaboration showcases how organizations in highly regulated industries can rapidly build AI applications by using innovative foundation models on AWS, the trusted healthcare cloud provider. By combining clinical expertise with advanced AI models and secure infrastructure, they’ve created a solution that can transform care delivery at scale while maintaining the personalized, human-led approach that makes Omada effective.

“This project proves that responsible AI adoption in healthcare is not just possible—it’s essential for reaching more patients with high-quality care,” concludes Miller.

Omada remains committed to growing its human care teams with the efficiency of AI-enabled technology. Looking ahead, the team is dedicated to creating new innovations that foster a sense of real-time support, confidence, and autonomy among members.

For more information, see the following resources:

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/04/sunaina-100x100.jpeg)
**Sunaina Kavi**
is an AI/ML product manager at Omada, dedicated to leveraging artificial intelligence for behavior change to improve outcomes in diabetes, hypertension, and weight management. She earned a Bachelor of Science in Biomedical Engineering and an MBA from the University of Michigan’s Ross School of Business, specializing in Entrepreneurship and Finance. Prior to transitioning to Omada, she gained experience as an investment banker in Technology, Media, and Telecom in San Francisco. She later joined Rivian, focusing on charging solutions within their infotainment group, and founded her own startup aimed at using AI to manage autoimmune flares. Sunaina is also actively involved in the Generative AI group in San Francisco, working to enhance safety, security, and systematic evaluations within the healthcare community.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/04/image-3-4-100x100.png)
Breanne Warner**
is an Enterprise Solutions Architect at Amazon Web Services supporting healthcare and life science (HCLS) customers. She is passionate about supporting customers to use generative AI on AWS and evangelizing model adoption for first-party and third-party models. Breanne is also Vice President of the Women at Amazon with the goal of fostering inclusive and diverse culture at Amazon. Breanne holds a Bachelor of Science in Computer Engineering from the University of Illinois Urbana-Champaign.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/04/pfp_cropped-100x111.jpg)
Baladithya Balamurugan**
is a Solutions Architect at AWS focused on ML deployments for inference and using AWS Neuron to accelerate training and inference. He works with customers to enable and accelerate their ML deployments on services such as Amazon SageMaker and Amazon EC2. Based out of San Francisco, Baladithya enjoys tinkering, developing applications and his homelab in his free time.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/04/Image-from-iOS-2-100x115.jpg)
Amin Dashti, PhD**
, is a Senior Data Scientist at AWS, specializing in model customization and training using Amazon SageMaker. With a PhD in Physics, he brings a deep scientific rigor to his work in machine learning and applied AI. His multidisciplinary background—spanning academia, finance, and tech—enables him to tackle complex challenges from both theoretical and practical perspectives. Based in the San Francisco Bay Area, Amin enjoys spending his free time with his family exploring parks, beaches, and local trails.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/04/Marco-Punio.jpg)
Marco Punio**
is a Sr. Specialist Solutions Architect focused on GPU-accelerated AI workloads, large-scale model training, and applied AI solutions on AWS. As a member of the Gen AI Applied Sciences SA team at AWS, he specializes in high-performance computing for AI, optimizing GPU clusters for foundation model training and inference, and serves as a global lead for the Meta–AWS Partnership and technical strategy. Based in Seattle, Washington, Marco enjoys writing, reading, exercising, and building GPU-optimized AI applications in his free time.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/09/04/Evan-100x100.jpeg)
Evan Grenda**
Sr. GenAI Specialist at AWS, where he works with top-tier third-party foundation model and agentic frameworks providers to develop and execute joint go-to-market strategies, enabling customers to effectively deploy and scale solutions to solve enterprise agentic AI challenges. Evan holds a BA in Business Administration from the University of South Carolina, a MBA from Auburn University, and an MS in Data Science from St. Joseph’s University.