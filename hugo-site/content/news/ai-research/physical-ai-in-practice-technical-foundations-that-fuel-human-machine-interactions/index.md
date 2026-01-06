---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T00:00:19.666881+00:00'
exported_at: '2025-11-26T00:00:22.019341+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/physical-ai-in-practice-technical-foundations-that-fuel-human-machine-interactions
structured_data:
  about: []
  author: ''
  description: In this post, we explore the complete development lifecycle of physical
    AI—from data collection and model training to edge deployment—and examine how
    these intelligent systems learn to understand, reason, and interact with the physical
    world through continuous feedback loops. We illustrate this workflow through Diligent
    Robotics' Moxi, a mobile manipulation robot that has completed over 1.2 million
    deliveries in hospitals, saving nearly 600,000 hours for clinical staff while
    transforming healthcare logistics and returning valuable time to patient care.
  headline: 'Physical AI in practice: Technical foundations that fuel human-machine
    interactions'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/physical-ai-in-practice-technical-foundations-that-fuel-human-machine-interactions
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Physical AI in practice: Technical foundations that fuel human-machine interactions'
updated_at: '2025-11-26T00:00:19.666881+00:00'
url_hash: 353446de0dd05f4c50ead9f6acddb6665ae5b8fa
---

In our previous post,
[Transforming the physical world with AI: the next frontier in intelligent automation](https://aws.amazon.com/blogs/machine-learning/transforming-the-physical-world-with-ai-the-next-frontier-in-intelligent-automation/)
, we explored how the field of physical AI is redefining a wide range of industries including construction, manufacturing, healthcare, and agriculture. Now, we turn our attention to the complete development lifecycle behind this technology – the process of creating intelligent systems that don’t just follow instructions, but truly partner with humans by collaborating, anticipating requirements, and actively driving toward common objectives.

To illustrate this workflow in action, we’ll explore how
[Diligent Robotics](https://www.diligentrobots.com/)
applies physical AI principles to develop mobile robots that assist clinical teams in hospital settings. We’ll also share key considerations for business leaders looking to implement physical AI solutions that can improve both their operations and customer experiences.

## Defining physical AI

The relationship between humans and machines is undergoing a profound transformation. What began as simple tools under direct human control has evolved into sophisticated partnerships where intelligent machines can understand context, interpret intentions, and make autonomous decisions.

The term
*physical AI*
describes a system that is interactive and iterative. Physical AI is a process where elements work together in various patterns to understand, reason, learn, and interact with the physical world. At each step of the autonomy flywheel, elements are continuously learning and improving to feed the next step in the journey.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/ML-20088-2-300x289.png)

The process begins with understanding. Here we integrate models and algorithms with sensors, real world and simulated data, and use these datasets to create reasoning. Next, a reasoning model predicts actions that will be realized in the physical world in real-time. But the process for these intelligent systems doesn’t stop there – they must continuously learn iteratively through feedback loops to improve overall performance of the system.

## End-to-end physical AI workflow for human-machine teamwork

What does this next leap in advanced autonomy entail? Developing and deploying physical AI solutions is an iterative process that includes data collection and preparation, model training and optimization, and edge operation. The development lifecycle is shown in the following diagram. Let’s explore each of these elements.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/ML-20088-4.jpg)

### Data collection and preparation

The first step in the workflow is to collect and prepare data for downstream tasks, including model training and evaluation. This may include proprietary data collected for specific applications as well as open-source and simulation data. These data sources are stored, cleaned, and filtered based on the downstream task.

### Model training and fine-tuning

Training physical AI systems to interact effectively with the real world presents unique challenges that go beyond traditional machine learning approaches. These systems must learn to navigate complex, dynamic environments, manipulate objects with varying properties, and adapt to unexpected situations. Specialized training methodologies have emerged for developing capable and robust physical AI systems that can operate reliably in diverse, real-world settings. These include:

* **Reinforcement learning:**
  Autonomous machines can learn skills through trial-and-error interactions with their environment. Unlike supervised learning, which requires labeled datasets, reinforcement learning allows physical AI systems to learn directly from experience by maximizing a reward function.
* **Physics-informed reinforcement learning:**
  Integrates physical knowledge into the learning process to improve sample efficiency and generalization. This approach helps bridge the gap between purely data-driven methods and traditional physics-based control.
* **Imitation learning**
  : Physical AI systems can learn from human demonstrations rather than through trial and error. This approach is particularly valuable for tasks that are difficult to specify through reward functions but can be straightforwardly demonstrated by humans. Techniques like behavioral cloning and inverse reinforcement learning allow robots to observe human actions and infer the underlying policies or reward functions.
* **Simulation-based training:**
  Provides virtual replicas of physical systems that support safe, cost-effective training before deployment in the real world. Digital twins serve as simulation systems for training specialized AI models so developers can test and refine robot behaviors before real-world deployment. Simulation-based training offers several advantages including safety, speed, scalability, reproducibility, and cost-effectiveness.

### Model optimization

Once the model has been trained, it can be optimized for specific hardware, latency requirements, computational cost, or performance. Techniques for model optimization include:

* **Quantization**
  : Reduces the numerical precision of weights and activations. Common quantization approaches include reducing
  `float32`
  to
  `float16`
  and
  `float32`
  to
  `int8`
  . Quantization serves to decrease memory storage requirements and improve inference speed.
* **Distillation:**
  Transfers knowledge from a larger model to a smaller one while preserving performance. Smaller models can be deployed on less powerful hardware and have lower computational costs.

The resulting edge-compatible model is then evaluated on real-world or simulation tasks. Model training and optimization are iteratively refined until the desired performance is achieved.

### Edge operation

Lastly, the optimized model is deployed in the field to validate functionality on actual hardware in the real world. The system continuously collects operational data and performance metrics, which are systematically transmitted back to cloud-based solutions for analysis. The cloud infrastructure can perform additional model training and optimization strategies. The modified models are then redeployed to the edge, where model inference (edge compute) occurs. Edge computing is when decisions and actions occur, for example, stopping a robotic arm or opening a gate. This workflow of sensing, thinking, and acting creates a continuous cycle of improvement. For mission-critical applications, the ability to predict actions in mere milliseconds matters.

## Technology in action: How Diligent Robotics is transforming healthcare

The technologies to support this proactive partnership, where intelligent systems anticipate needs and work alongside humans, isn’t theoretical. They are already being implemented, and delivering measurable impact, for example, in healthcare, where the stakes are high and the need for human connection is paramount.

Consider the daily reality for nurses. They typically spend a significant portion of their day on tasks that pull them away from patient care, for example, delivering medications, transporting lab samples, and fetching supplies.
[Diligent Robotics](https://www.diligentrobots.com/)
, an AWS
[Physical AI Fellow](https://www.massrobotics.org/physical-ai-fellowship-cohort/)
, addresses this challenge using the workflow described above with Moxi, a mobile manipulation robot designed to handle routine logistics and return valuable time to nurses and their patients.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/ML-20088-5.jpeg)

Moxi’s intelligence grows through continuous learning from hospital environments. The robot collects operational data that feeds into its underlying models. This iterative process makes Moxi increasingly reliable and capable of navigating the complex, dynamic settings of medical facilities. The models are then optimized for efficiency – requiring less computational power and enabling faster processing – so they can be deployed at the edge. Edge deployment allows Moxi to make real-time decisions autonomously, whether that means pressing an elevator button or opening a door, which is crucial in safety critical environments where relying on connectivity is not always possible.

The results have been remarkable, with Diligent Robotics reporting:

* **Over 1.2 million deliveries**
  completed across Moxi’s hospital fleet
* Nearly
  **600,000 hours saved**
  for hospital staff

Moxi has made an impact in health systems across the country. For example, at Rochester Regional Health in New York, Moxi robots have:

* Reshaped medication delivery workflows like Meds to Beds Programs where Moxi supports time-sensitive medication delivery to reduce discharge delays, improving patient experience and minimize readmissions
* Streamlined lab workflows to improve the predictability and timeliness of lab results for patients

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/ML-20088-6.png)

Moxi’s impact extends beyond the numbers. The Chief Pharmacy Officer at Rochester Regional Health noted, “We’re focused on designing healthcare for the next generation, and that means innovating wherever we can to get our teams back to patient care. Moxi has become an essential part of our operations.”

As Andrea Thomaz, Founder and CEO of Diligent Robotics observes: “Watching clinical teams interact with Moxi as if it’s a real member of the team – saying, ‘Good morning,’ giving it high-fives, and even naming it ‘Employee of the Week’ – has been one of the most rewarding human-robot experiences.”

## The way forward with physical AI

The path ahead for physical AI is already being charted by early adopters who are proving its value in real-world settings – from hospitals reducing burnout and improving patient care, to factories enhancing safety and consistency. Their results offer a clear signal: success doesn’t come from sweeping overhauls but from focused, high-impact applications that deliver measurable results.

Building solutions with best-in-class technology alone is not enough. As physical AI systems become more integrated into our world, thoughtful governance becomes essential for business leaders. Recent breakthroughs are creating new opportunities – and new challenges. Enterprise leaders will need to address:

* **Cybersecurity**
  for cloud-connected robot fleets
* **Interoperability**
  between systems and existing infrastructure
* **Safety mechanisms**
  including adaptive approaches and redundancy systems
* **Ethical frameworks**
  facilitating transparency, fairness, and privacy

Regulatory approaches vary across jurisdictions. For example, the EU has adopted a comprehensive framework addressing safety and ethics, while the U.S. takes a sector-specific approach driven by industry-led initiatives.

Business leaders must navigate these different standards while maintaining consistent global operations. A risk-based governance approach provides an effective strategy – classifying AI applications based on their potential impact and applying appropriate controls accordingly. This balanced approach satisfies diverse regulatory requirements while preserving the agility needed for continued innovation.

By starting small, learning fast, and scaling what works, organizations can build lasting capability, deliver clear ROI, and position themselves for broader implementation at the forefront of the physical AI revolution. The future belongs to organizations that successfully integrate digital intelligence with physical capability while addressing governance, safety, and ethical considerations proactively.

Initiatives like the
[Physical AI Fellowship](https://press.aboutamazon.com/aws/2025/9/massrobotics-aws-and-nvidia-launch-first-of-its-kind-physical-ai-fellowship)
– powered by AWS, MassRobotics, and NVIDIA – embody the collaborative spirit needed to accelerate this kind of progress.

## Getting started with physical AI

Ready to explore how physical AI can transform your operations? Learn more about the
[Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/)
and how we partner with organizations to accelerate their journey from concept to production-ready physical AI solutions.

Contact your AWS account manager to discuss our physical AI solutions and receive implementation support tailored to your needs.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/13/ML-19853-1.png)
Sri Elaprolu**
is Director of the AWS Generative AI Innovation Center, where he leads a global team implementing cutting-edge AI solutions for enterprise and government organizations. During his 13-year tenure at AWS, he has led ML science teams partnering with organizations like the NFL, Cerner, and NASA. Prior to AWS, he spent 14 years at Northrop Grumman in product development and software engineering leadership roles. Sri holds a Master’s in Engineering Science and an MBA.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/13/ML-19853-2.png)**
**Alla Simoneau**
is a technology and commercial leader with over 15 years of experience, currently serving as the Emerging Technology Physical AI Lead at Amazon Web Services (AWS), where she drives global innovation at the intersection of AI and real-world applications. With over a decade at Amazon, Alla is a recognized leader in strategy, team building, and operational excellence, specializing in turning cutting-edge technologies into real-world transformations for startups and enterprise customers.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/13/ML-19853-3.png)**
**Paul Amadeo**
is a seasoned technology leader with over 30 years of experience spanning artificial intelligence, machine learning, IoT systems, RF design, optics, semiconductor physics, and advanced engineering. As Technical Lead for Physical AI in the AWS Generative AI Innovation Center, Paul specializes in translating AI capabilities into tangible physical systems, guiding enterprise customers through complex implementations from concept to production. His diverse background includes architecting computer vision systems for edge environments, designing robotic smart card manufacturing technologies that have produced billions of devices globally, and leading cross-functional teams in both commercial and defense sectors. Paul holds an MS in Applied Physics from the University of California, San Diego, a BS in Applied Physics from Caltech, and holds six patents spanning optical systems, communication devices, and manufacturing technologies.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/laurakul-100x100.png)
Laura Kulowski**
is a Senior Applied Scientist at the AWS Generative AI Innovation Center, where she works with customers to build generative AI solutions. Before joining Amazon, Laura completed her PhD at Harvard’s Department of Earth and Planetary Sciences and investigated Jupiter’s deep zonal flows and magnetic field using Juno data.