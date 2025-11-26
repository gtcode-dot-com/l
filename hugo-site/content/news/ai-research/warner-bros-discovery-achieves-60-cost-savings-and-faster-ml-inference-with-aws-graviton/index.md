---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T00:00:19.371324+00:00'
exported_at: '2025-11-26T00:00:22.024323+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/warner-bros-discovery-achieves-60-cost-savings-and-faster-ml-inference-with-aws-graviton
structured_data:
  about: []
  author: ''
  description: Warner Bros. Discovery (WBD) is a leading global media and entertainment
    company that creates and distributes the world’s most differentiated and complete
    portfolio of content and brands across television, film and streaming. In this
    post, we describe the scale of our offerings, artificial intelligence (AI)/machine
    learning (ML) inference infrastructure requirements for our real time recommender
    systems, and how we used AWS Graviton-based Amazon SageMaker AI instances for
    our ML inference workloads and achieved 60% cost savings and 7% to 60% latency
    improvements across different models.
  headline: Warner Bros. Discovery achieves 60% cost savings and faster ML inference
    with AWS Graviton
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/warner-bros-discovery-achieves-60-cost-savings-and-faster-ml-inference-with-aws-graviton
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Warner Bros. Discovery achieves 60% cost savings and faster ML inference with
  AWS Graviton
updated_at: '2025-11-26T00:00:19.371324+00:00'
url_hash: 0ed65247eb12a213bed0c6409b8a4ef35e581222
---

*This post is written by Nukul Sharma, Machine Learning Engineering Manager, and Karthik Dasani, Staff Machine Learning Engineer, at Warner Bros. Discovery.*

Warner Bros. Discovery (
[WBD](https://www.wbd.com/)
) is a leading global media and entertainment company that creates and distributes the world’s most differentiated and complete portfolio of content and brands across television, film and streaming. With iconic brands including HBO, Discovery Channel, Warner Bros., CNN, DC Entertainment, and many others, WBD delivers premium storytelling to audiences worldwide through diverse systems and experiences. Our streaming services, including HBO Max and discovery+, represent a cornerstone of our direct-to-consumer strategy, offering viewers unprecedented access to our 200,000+ hours of programming.

In this post, we describe the scale of our offerings, artificial intelligence (AI)/machine learning (ML) inference infrastructure requirements for our real time recommender systems, and how we used
[AWS Graviton](https://aws.amazon.com/ec2/graviton/)
-based
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
instances for our ML inference workloads and achieved 60% cost savings and 7% to 60% latency improvements across different models.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/WBD_logo.png)

Warner Bros. Discovery (WBD) brands

In the rapidly evolving world of digital entertainment, exceptional content alone isn’t enough—viewers need to discover programs that match their unique interests. Delivering highly personalized content has become essential for engaging audiences, driving viewing sessions, and building lasting relationships with users. To effectively serve our diverse base of over 125M+ users across 100+ countries (as of 2025), we employ data science, user behavior analysis, and human curation to predict what viewers will love. Our work focuses on crafting dynamic recommendation algorithms and tailoring suggestions to individual preferences, while continuously testing and refining strategies to improve content relevance accuracy.

## The challenge: Scaling personalization globally while managing costs

HBO Max’s Search and Personalization infrastructure spans 9
[AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
spread across USA, EMEA and APAC to deliver localized recommendations tailored to regional preferences. This extensive infrastructure enables us to maintain consistent sub-100ms latency requirements while serving personalized content recommendations across diverse geographic regions.

With a vast portfolio of our beloved brands combined with a diverse user base, we faced the challenge of personalizing content recommendations without compromising on budget. Recommendation systems are latency critical; they need to be run in real-time which means stringent requirements for the ML infrastructure needed to deploy our services. This content discovery challenge requires sophisticated recommender systems that can perform reliably at massive scale, even during major premieres when traffic surges up to 500% within minutes. We were looking for real-time performance and a cost-effective infrastructure solution for our AI/ML workloads.

## Our solution: Using AWS Graviton for cost-effective ML inference at scale

Our solution combined two key AWS technologies:
[AWS Graviton](https://aws.amazon.com/ec2/graviton/)
processors and
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai)
. This integrated approach allowed us to comprehensively address both our performance and cost challenges.

AWS Graviton is a family of processors designed to deliver the best price performance for cloud workloads running in
[Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/)
and fully managed services. They are also optimized for ML workloads, including
[Neon](https://developer.arm.com/Architectures/Neon)
vector processing engines, support for
[bfloat16](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
, Scalable Vector Extension (
[SVE](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions)
), and Matrix Multiplication (
[MMLA](https://developer.arm.com/documentation/ddi0596/2020-12/SVE-Instructions/BFMMLA--BFloat16-floating-point-matrix-multiply-accumulate-)
) instructions, making them an ideal choice for our latency critical recommender systems.

We decided to try them for our XGBoost and TensorFlow-based ML models for which we followed a two-step process. First, we started with a sandbox environment, fine-tuned workers and threads to maximize the throughput on a single instance and observed substantially better performance compared to x86-based instances in our fleet. Second, we moved on to the production traffic, where we performed shadow testing to confirm the cost and the performance benefits we observed in the standalone environment. We noticed that Graviton instances were able to scale almost linearly even at higher CPU loading. We reconfigured our auto-scale configs to increase the instance utilization and because Graviton instances were able to handle burst traffic more effectively, we also reduced the minimum number of instances. Additionally, we balanced the cost vs performance not to impact one in over-optimizing for the other.

The
[SageMaker Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
played a crucial role in streamlining our testing workflow. By automating the benchmarking process across different instance types and configurations, this tool significantly reduced the time needed to identify optimal setups for our models. The automated performance analysis helped us make data-driven decisions about instance selection and accelerated our model deployment pipeline.

To validate the performance and reliability of our new infrastructure, we utilized the
[shadow testing](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)
capabilities of Amazon SageMaker. This testing framework enabled our team to evaluate new deployments alongside existing production systems, providing real-world performance comparisons without risking impact to our users’ experience. This approach proved particularly valuable for our Machine Learning Platform (MLP) team users as they assessed various infrastructure modifications. By running parallel tests of different hardware setups and fine-tuning inference parameters, we could thoroughly evaluate system performance before committing to changes. This strategic testing method helped us anticipate potential issues and optimize configurations early in our deployment process.

The following diagram highlights the end-to-end deployment of our ML inference workload on AWS. As shown here, we’ve already been using multiple fully managed AWS services like
[Amazon SageMaker](https://aws.amazon.com/sagemaker/ai/)
,
[Amazon Simple Storage Service (Amazon S3](https://aws.amazon.com/s3/)
), and
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
to achieve our recommender systems’ objectives. This time, we took one step forward to migrate to AWS Graviton-based instances that resulted in cost savings and improved performance.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/architecture_latest-1.png)

## Results

The migration to AWS Graviton-based instances from x86-base instances delivered remarkable results across our recommendation system portfolio.

### Achieved 60% cost savings

Our comprehensive analysis revealed substantial cost reductions across our personalization models, achieving an average cost savings of 60%. The improvements were particularly notable in our catalog ranking models, where we observed cost reductions of up to 88%.

### Improved average and p99 latencies, ranging from 7% to 60% across different models

Apart from cost savings, we also achieved significant performance enhancements. The P99 latency improvements were impressive across our model suite with our XGBoost model showing a dramatic 60% reduction in latency. Other models in our portfolio demonstrated consistent latency improvements up to 21%. The following dashboard from our A/B testing highlights how migrating to AWS Graviton-based ML instances improved the average and p99 latencies and cut down the instance count substantially.
GREEN
lines are from x86 based servers in our fleet and the
YELLOW
lines are from AWS Graviton based servers.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/metrics.png)

### Improved user experience

By reducing latency, we significantly improved the performance of our services and the user experience for our customers; viewers experienced more responsive recommendations that better match their interests.

### Experienced seamless migration

We had a great collaboration with AWS account and service teams throughout the project. The migration was seamless. From the initial benchmarking to the final migration it took around one month; proof of concept on a catalog ranking model that gave 60% cost saving was done in a week’s time, which was much faster than the time we had originally estimated.

### Motivated to achieve 100% of recommender system to run on Graviton-based instance

Looking at the substantial cost savings we’ve achieved with Graviton adoption, we are currently working on migrating our remaining models to Graviton with a target of achieving 100% of recommender system to run on Graviton-based instances.

## Conclusion

By migrating our ML inference workloads to AWS Graviton-based instances, we’ve transformed how we deliver personalized content recommendations to our 125M+ users across 100+ countries. The migration yielded impressive results with cost reductions averaging 60% across our recommender systems and latency improvements ranging from 7% to 60% across different models. These performance gains translate into tangible business outcomes: viewers experience more responsive recommendations that better match their interests, resulting in deeper engagement, extended viewing sessions, and ultimately stronger retention on our systems—all while allowing us to scale our operations efficiently.

Overall, the adoption of AWS Graviton processors exemplifies how innovative cloud solutions can drive both operational efficiency and business value. Our experience demonstrates that organizations can successfully balance the competing demands of performance, cost, and scale in the rapidly evolving business landscape. As we continue to optimize our ML infrastructure, these improvements will help us stay competitive while delivering increasingly personalized experiences to our global audience.

For further reading, refer to the following:

The WBD team would like to thank Sunita Nadampalli, Utsav Joshi, Karthik Rengasamy, Tito Panicker, Sapna Patel, and Gautham Panth from AWS for their contributions to this solution.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/nukul.jpg)
Nukul Sharma**
is a Machine Learning Engineering Manager with 18+ years of experience leading top-performing engineering and MLOps teams at Warner Bros. Discovery. Skilled in developing scalable solutions, end-to-end ML pipelines, cloud systems, and CI/CD. Proven track record in delivering impactful personalization and MLOps solutions that drive efficiency and growth.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/karthikD.jpg)
Karthik Dasani**
is a Staff Machine Learning Engineer with expertise in large-scale recommendation systems and ML Ops at Warner Bros. Discovery. He has extensive experience in productionizing AI solutions with a strong focus on performance and cost optimization. His work bridges applied research and scalable, real-world machine learning systems.

---

### About the AWS Team

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/sunita-100x108.jpg)
Sunita Nadampalli**
is a Principal Engineer and AI/ML expert at AWS. She leads AWS Graviton software performance optimizations for AI/ML and HPC workloads. She is passionate about open-source software development and delivering high-performance and sustainable software solutions for SoCs based on the Arm ISA.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/utsav-100x99.jpg)
Utsav Joshi**
is a Principal Technical Account Manager at AWS. He lives in New Jersey and enjoys working with AWS customers in solving architectural, operational, and cost optimization challenges. In his spare time, he enjoys traveling, road trips, and playing with his kids.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/karthikR-100x129.jpg)
Karthik Rengasamy**
is a Senior Solutions Architect at AWS, specializing in helping media and entertainment customers design and scale their cloud architectures. He focuses on media supply chain, archive, and video streaming solutions, working closely with customers to drive innovation and optimize media workloads on AWS. His passion lies in building secure, scalable, and cost-effective solutions that transform how media is managed and delivered to global audiences.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/tito-100x150.jpg)
Tito Panicker**
is a Sr. Global Solutions Architect who helps the largest enterprise customers architect secure, scalable, and resilient solutions in the cloud. His primary area of focus is the Media and Entertainment vertical, where he specializes in Direct-to-Consumer (D2C) streaming, data/analytics, AI/ML, and generative AI.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/sapna-100x133.png)
Sapna Patel**
is a Principal Customer Solutions Manager at AWS who helps media and entertainment customers optimize their cloud journey through strategic guidance and relationship management. She focuses on driving customer success by aligning AWS solutions with business objectives, making sure customers maximize value from their cloud investments while achieving their technical and operational goals.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/gautham-100x133.png)
Gautham Panth**
is a Principal Product Manager at AWS focused on building pioneering cloud infrastructure solutions. With over 20 years of cross-disciplinary expertise spanning cloud computing, enterprise infrastructure, and software, Gautham leverages his comprehensive understanding of customer challenges, to drive future direction and capabilities of AWS offerings.