---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-23T00:03:32.145828+00:00'
exported_at: '2025-12-23T00:03:35.479343+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-mistral-ais-voxtral-on-amazon-sagemaker-ai
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate hosting Voxtral models on Amazon SageMaker
    AI endpoints using vLLM and the Bring Your Own Container (BYOC) approach. vLLM
    is a high-performance library for serving large language models (LLMs) that features
    paged attention for improved memory management and tensor parallelism for distributing
    models across multiple GPUs.
  headline: Deploy Mistral AI’s Voxtral on Amazon SageMaker AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/deploy-mistral-ais-voxtral-on-amazon-sagemaker-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Deploy Mistral AI’s Voxtral on Amazon SageMaker AI
updated_at: '2025-12-23T00:03:32.145828+00:00'
url_hash: 443103ab6b2aa82f77215de5eaac5167473bae70
---

- Configure your model in code/serving.properties:
  1. To deploy Voxtral-Mini, use the following code:

     ```
     option.model_id=mistralai/Voxtral-Mini-3B-2507
     option.tensor_parallel_degree=1
     ```
  2. To deploy Voxtral-Small, use the following code:

     ```
     option.model_id=mistralai/Voxtral-Small-24B-2507
     option.tensor_parallel_degree=4
     ```
  4. Open and run Voxtral-vLLM-BYOC-SageMaker.ipynb to deploy your endpoint and test with text, audio, and function calling capabilities.

  ### Docker container configuration

  The
  [GitHub repo](https://github.com/aws-samples/mistral-on-aws/tree/main/Mistral%20Voxtral/Voxtral-vllm-byoc)
  contains the full Dockerfile. The following code snippet highlights the key parts:

  ```
  # Custom vLLM Container for Voxtral Model Deployment on SageMaker
  FROM --platform=linux/amd64 vllm/vllm-openai:latest
  # Set environment variables for SageMaker
  ENV MODEL_CACHE_DIR=/opt/ml/model
  ENV TRANSFORMERS_CACHE=/tmp/transformers_cache
  ENV HF_HOME=/tmp/hf_home
  ENV VLLM_WORKER_MULTIPROC_METHOD=spawn
  # Install audio processing dependencies
  RUN pip install --no-cache-dir \
  "mistral_common>=1.8.1" \
  librosa>=0.10.2 \
  soundfile>=0.12.1 \
  pydub>=0.25.1
  ```

  This Dockerfile creates a specialized container that extends the official vLLM server with Voxtral-specific capabilities by adding essential audio processing libraries (
  `mistral_common`
  for tokenization,
  `librosa/soundfile/pydub`
  for audio handling) while configuring the proper SageMaker environment variables for model loading and caching. The approach separates infrastructure from business logic by keeping the container generic and allowing SageMaker to dynamically inject model-specific code (
  `model.py`
  and
  `serving.properties`
  ) from Amazon S3 at runtime, enabling flexible deployment of different Voxtral variants without requiring container rebuilds.

  ### Model configurations

  The full model configurations are in the
  `serving.properties`
  file located in the code folder. The following code snippet highlights the key configurations:

  ```
  # Model configuration
  option.model_id=mistralai/Voxtral-Small-24B-2507
  option.tensor_parallel_degree=4
  option.dtype=bfloat16
  # Voxtral-specific settings (as per official documentation)
  option.tokenizer_mode=mistral
  option.config_format=mistral
  option.load_format=mistral
  option.trust_remote_code=true
  # Audio processing (Voxtral specifications)
  option.limit_mm_per_prompt=audio:8
  option.mm_processor_kwargs={"audio_sampling_rate": 16000, "audio_max_length": 1800.0}
  # Performance optimizations (vLLM v0.10.0+ features)
  option.enable_chunked_prefill=true
  option.enable_prefix_caching=true
  option.use_v2_block_manager=true
  ```

  This configuration file provides Voxtral-specific optimizations that follow Mistral’s official recommendations for vLLM server deployment, setting up proper tokenization modes, audio processing parameters (supporting up to eight audio files per prompt with 30-minute transcription capability), and using the latest vLLM v0.10.0+ performance features like chunked prefill and prefix caching. The modular design supports seamless switching between Voxtral-Mini and Voxtral-Small by simply changing the
  `model_id`
  and
  `tensor_parallel_degree`
  parameters, while maintaining optimal memory utilization and enabling advanced caching mechanisms for improved inference performance.

  ### Custom inference handler

  The full custom inference code is in the model.py file located in the code folder. The following code snippet highlights the key functions:

  ```
  # FastAPI app for SageMaker compatibility
  app = FastAPI(title="Voxtral vLLM Inference Server", version="1.1.0")
  model_engine = None
  # vLLM Server Initialization for Voxtral
  def start_vllm_server():
  	"""Start vLLM server with Voxtral-specific configuration"""
  	config = load_serving_properties()

  	cmd = [
  	"vllm", "serve", config.get("option.model_id"),
  	"--tokenizer-mode", "mistral",
  	"--config-format", "mistral",
  	"--tensor-parallel-size", config.get("option.tensor_parallel_degree"),
  	"--host", "127.0.0.1",
  	"--port", "8000"
  	]

  	vllm_server_process = subprocess.Popen(cmd, env=vllm_env)
  	server_ready = wait_for_server()
  	return server_ready
  @app.post("/invocations")
  async def invoke_model(request: Request):
  	"""Handle chat, transcription, and function calling"""
  	# Transcription requests
  	if "transcription" in request_data:
  		audio_source = request_data["transcription"]["audio"]
  	return transcribe_audio(audio_source)

  # Chat requests with multimodal support
  messages = format_messages_for_openai(request_data["messages"])
  tools = request_data.get("tools")

  # Generate via vLLM OpenAI client
  response = openai_client.chat.completions.create(
  	model=model_config["model_id"],
  	messages=messages,
  	tools=tools if supports_function_calling() else None
  	)
  	return response
  ```

  This custom inference handler creates a FastAPI-based server that directly integrates with the vLLM server for optimal Voxtral performance. The handler processes multimodal content including base64-encoded audio and audio URLs, dynamically loads model configurations from the
  `serving.properties`
  file, and supports advanced features like function calling for Voxtral-Small deployments.

  ### SageMaker deployment code

  The Voxtral-vLLM-BYOC-SageMaker.ipynb notebook included in the
  `Voxtral-vllm-byoc`
  folder orchestrates the entire deployment process for both Voxtral models:

  ```
  import boto3
  import sagemaker
  from sagemaker.model import Model
  # Initialize SageMaker session
  sagemaker_session = sagemaker.Session()
  role = sagemaker.get_execution_role()
  bucket = "your-s3-bucket"
  # Upload model artifacts to S3
  byoc_config_uri = sagemaker_session.upload_data(
  path="./code",
  bucket=bucket,
  key_prefix="voxtral-vllm-byoc/code"
  )
  # Configure custom container image
  account_id = boto3.client('sts').get_caller_identity()['Account']
  region = boto3.Session().region_name
  image_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/voxtral-vllm-byoc:latest"
  # Create SageMaker model
  voxtral_model = Model(
  	image_uri=image_uri,
  	model_data={
  		"S3DataSource": {
  		"S3Uri": f"{byoc_config_uri}/",
  		"S3DataType": "S3Prefix",
  		"CompressionType": "None"
  		}
  	},
  	role=role,
  	env={
  		'MODEL_CACHE_DIR': '/opt/ml/model',
  		'TRANSFORMERS_CACHE': '/tmp/transformers_cache',
  		'SAGEMAKER_BIND_TO_PORT': '8080'
  		}
  	)
  # Deploy to endpoint
  predictor = voxtral_model.deploy(
  	initial_instance_count=1,
  	instance_type="ml.g6.12xlarge", # For Voxtral-Small
  	container_startup_health_check_timeout=1200,
  	wait=True
  	)
  ```

  ## Model use cases

  The Voxtral models support various text and speech-to-text use cases, and the Voxtral-Small model supports tool use with voice input. Refer to the
  [GitHub repository](https://github.com/aws-samples/mistral-on-aws/tree/main/Mistral%20Voxtral/Voxtral-vllm-byoc)
  for the complete code. In this section, we provide code snippets for different use cases that the model supports.

  ### Text-only

  The following code shows a basic text-based conversation with the model. The user sends a text query and receives a structured response:

  ```
  payload = {
  	"messages": [
  	{
  		"role": "user",
  		"content": "Hello! Can you tell me about the advantages of using vLLM for model inference?"
  		}
  	],
  	"max_tokens": 200,
  	"temperature": 0.2,
  	"top_p": 0.95
  }
  response = predictor.predict(payload)
  ```

  ### Transcription-only

  The following example focuses on speech-to-text transcription by setting temperature to 0 for deterministic output. The model processes an audio file URL or audio file converted to base64 code, then returns the transcribed text without additional interpretation:

  ```
  payload = {
  	"transcription": {
  		"audio": "https://audiocdn.frenchtoday.com/file/ft-public-files/audiobook-samples/AMPFE/AMP%20FE%20Ch%2002%20Story%20Slower.mp3",
  		"language": "fr",
  		"temperature": 0.0
  		}
  	}
  response = predictor.predict(payload)
  ```

  ### Text and audio understanding

  The following code combines both text instructions and audio input for multimodal processing. The model can follow specific text commands while analyzing the provided audio file in one inference pass, enabling more complex interactions like guided transcription or audio analysis tasks:

  ```
  payload = {
  	"messages": [
  	{
  		"role": "user",
  		"content": [
  			{
  				"type": "text",
  				"text": "Can you summarise this audio file"
  			},
  			{
  				"type": "audio",
  				"path": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama.mp3"
  			}
  			]
  		}
  	],
  	"max_tokens": 300,
  	"temperature": 0.2,
  	"top_p": 0.95
  }
  response = predictor.predict(payload)
  ```

  ### Tool use

  The following code showcases function calling capabilities, where the model can interpret voice commands and execute predefined tools. The example demonstrates weather queries through voice input, with the model automatically calling the appropriate function and returning structured results:

  ```
  # Define weather tool configuration
  WEATHER_TOOL = {
      "type": "function",
  	"function": {
  		"name": "get_current_weather",
  		"description": "Get the current weather for a specific location",
  		"parameters": {
  			"type": "object",
              "properties": {
                  "location": {
                      "type": "string",
                      "description": "The city and state, e.g. San Francisco, CA"
                  },
                  "format": {
                      "type": "string",
                      "enum": ["celsius", "fahrenheit"],
                      "description": "The temperature unit to use."
                  }
              },
  		    "required": ["location", "format"]
          }
  	}
  }
  # Mock weather function
  def mock_weather(location, format="celsius"):
  	"""Always returns sunny weather at 25°C/77°F"""
  	temp = 77 if format.lower() == "fahrenheit" else 25
  	unit = "°F" if format.lower() == "fahrenheit" else "°C"
  	return f"It's sunny in {location} with {temp}{unit}"
  # Test payload with audio
  payload = {
  	"messages": [
  	{
  		"role": "user",
  		"content": [
  			{
  				"type": "audio",
  				"path": "https://huggingface.co/datasets/patrickvonplaten/audio_samples/resolve/main/fn_calling.wav"
              }
              ]
  		}
  	],
  	"temperature": 0.2,
  	"top_p": 0.95,
  	"tools": [WEATHER_TOOL]
  }
  response = predictor.predict(payload)
  ```

  ### Strands Agents integration

  The following example shows how to integrate Voxtral with the
  [Strands framework](https://strandsagents.com/latest/)
  to create intelligent agents capable of using multiple tools. The agent can automatically select and execute appropriate tools (such as calculator, file operations, or shell commands from Strands prebuilt tools) based on user queries, enabling complex multi-step workflows through natural language interaction:

  ```
  # SageMaker integration with Strands agents
  # from strands import Agent
  from strands import Agent
  from strands.models.sagemaker import SageMakerAIModel
  from strands_tools import calculator, current_time, file_read, shell
  model = SageMakerAIModel(
  	endpoint_config={
  		"endpoint_name": endpoint_name,
  		"region_name": "us-west-2",
  	},
  	payload_config={
  		"max_tokens": 1000,
  		"temperature": 0.7,
  		"stream": False,
  	}
  )
  agent = Agent(model=model, tools=[calculator, current_time, file_read, shell])
  response = agent("What is the square root of 12?")
  ```

  ## Clean up

  When you finish experimenting with this example, delete the SageMaker endpoints that you created in the notebook to avoid unnecessary costs:

  ```
  # Delete SageMaker endpoint
  print(f" Deleting endpoint: {endpoint_name}")
  predictor.delete_endpoint(delete_endpoint_config=True)
  print(" Endpoint deleted successfully")
  ```

  ## Conclusion

  In this post, we demonstrated how to successfully self-host Mistral’s open source Voxtral models on SageMaker using the BYOC approach. We’ve created a production-ready system that uses the latest vLLM framework and official Voxtral optimizations for both Mini and Small model variants. The solution supports the full spectrum of Voxtral capabilities, including text-only conversations, audio transcription, sophisticated multimodal understanding, and function calling directly from voice input. With this flexible architecture, you can switch between Voxtral-Mini and Voxtral-Small models through simple configuration updates without requiring container rebuilds.

  Take your multimodal AI applications to the next level by trying out the complete code from the
  [GitHub repository](https://github.com/aws-samples/mistral-on-aws/tree/main/Mistral%20Voxtral/Voxtral-vllm-byoc)
  to host the Voxtral model on SageMaker and start building your own voice-enabled applications. Explore Voxtral’s full potential by visiting
  [Mistral’s official website](https://mistral.ai/news/voxtral)
  to discover detailed capabilities, performance benchmarks, and technical specifications. Finally, explore the
  [Strands Agents](https://strandsagents.com/latest/)
  framework to seamlessly create agentic applications that can execute complex workflows.

  ---

  ### About the authors

  ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2023/11/29/ying_hou-1.jpg)
  **Ying Hou, PhD,**
  is a Sr. Specialist Solution Architect for GenAI at AWS, where she collaborates with model providers to onboard the latest and most intelligent AI models onto AWS platforms. With deep expertise in Gen AI, ASR, computer vision, NLP, and time-series forecasting models, she works closely with customers to design and build cutting-edge ML and GenAI applications.