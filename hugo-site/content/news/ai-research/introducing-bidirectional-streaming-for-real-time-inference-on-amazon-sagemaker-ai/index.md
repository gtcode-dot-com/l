---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T00:00:19.017852+00:00'
exported_at: '2025-11-26T00:00:22.026739+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-bidirectional-streaming-for-real-time-inference-on-amazon-sagemaker-ai
structured_data:
  about: []
  author: ''
  description: We're introducing bidirectional streaming for Amazon SageMaker AI Inference,
    which transforms inference from a transactional exchange into a continuous conversation.
    This post shows you how to build and deploy a container with bidirectional streaming
    capability to a SageMaker AI endpoint. We also demonstrate how you can bring your
    own container or use our partner Deepgram's pre-built models and containers on
    SageMaker AI to enable bi-directional streaming feature for real-time inference.
  headline: Introducing bidirectional streaming for real-time inference on Amazon
    SageMaker AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/introducing-bidirectional-streaming-for-real-time-inference-on-amazon-sagemaker-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Introducing bidirectional streaming for real-time inference on Amazon SageMaker
  AI
updated_at: '2025-11-26T00:00:19.017852+00:00'
url_hash: 2457eab13e02cfe8094537d085fdbe67e3d7af6f
---

In 2025, generative AI has evolved from text generation to multi-modal use cases ranging from audio transcription and translation to voice agents that require real-time data streaming. Today’s applications demand something more: continuous, real-time dialogue between users and models—the ability for data to flow both ways, simultaneously, over a single persistent connection. Imagine a speech to text use-case, where you will need to stream the audio stream as input and receive the transcripted text as a continuous stream. Such use-cases will require bi-directional streaming capability.

We’re introducing bidirectional streaming for
[Amazon SageMaker AI Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
, which transforms inference from a transactional exchange into a continuous conversation. Speech works best with real-time AI when conversations flow naturally without interruptions. With bidirectional streaming, speech to text becomes immediate. The model listens and transcribes at the same time, so words appear the moment they are spoken. Picture a caller describing an issue to a support line. As they speak, the live transcript appears in front of the call center agent, giving the agent instant context and letting them respond without waiting for the caller to finish. This kind of continuous exchange makes voice experiences feel fluid, responsive and human.

This post shows you how to build and deploy a container with bidirectional streaming capability to a SageMaker AI endpoint. We also demonstrate how you can bring your own container or use our partner Deepgram’s pre-built models and containers on SageMaker AI to enable bi-directional streaming feature for real-time inference.

## Bidirectional streaming: Deep dive

With bidirectional streaming, data flows both ways at once through a single, persistent connection.

In the traditional approach to inference requests, the client sends a complete question and waits, while the model processes the request and returns a complete answer before the client can send the next question.

```
Client: [sends complete question] → waits...
Model: ...processes... [returns complete answer]
Client: [sends next question] → waits...
Model: ...processes... [returns complete answer]
```

In bidirectional streaming, the client’s speech starts flowing while the model simultaneously begins processing and transcribing the answer immediately.

```
Client: [question starts flowing with enough context] →
Model: ← [answer starts flowing immediately]
Client: → [continues/adjusts question]
                                    ↓
Model: ← [adapts answer in real-time]
```

Users see results as soon as the model starts generating them. Maintaining one persistent connection replaces hundreds of short-lived connections. This reduces overhead on networking infrastructure, TLS handshakes, and connection management. Models can maintain context across a continuous stream, enabling multi-turn interactions without resending conversation history each time.

## SageMaker AI Inference bidirectional streaming capability

SageMaker AI Inference combines HTTP/2 and WebSocket protocols for real-time, two-way communication between clients and models. When you invoke a SageMaker AI Inference endpoint with bidirectional streaming, your request travels through the three-layer infrastructure in SageMaker AI:

* **Client to SageMaker AI router**
  : Your application connects to the Amazon SageMaker AI runtime endpoint using HTTP/2, establishing an efficient, multiplexed connection that supports bidirectional streaming.
* **SageMaker AI router to model container**
  : The router forwards your request to a Sidecar (a lightweight proxy running alongside your model container), which then establishes a WebSocket connection to your model container at
  `ws://localhost:8080/invocations-bidirectional-stream`
  .

Once the connection is established, data flows freely in both directions:

* **Request stream**
  : Your application sends input as a series of payload chunks over HTTP/2. The SageMaker AI infrastructure converts these into WebSocket data frames—either text (for UTF-8 data) or binary—and forwards them to your model container. The model receives these frames in real-time and can begin processing immediately, even before the complete input arrives such as for transcribing use cases.
* **Response stream**
  : Your model generates output and sends it back as WebSocket frames. SageMaker AI wraps each frame into a response payload and streams it directly to your application over HTTP/2. Users see results as soon as the model produces them—word by word for text, frame by frame for video, or sample by sample for audio.

The WebSocket connection between the Sidecar and model container remains open for the duration of your session, with built-in health monitoring. To maintain connection health, SageMaker AI sends WebSocket ping frames every 60 seconds to verify the connection is active, and your model container responds with pong frames to confirm it’s healthy. If 5 consecutive pings go unanswered, the connection is gracefully closed.

## Building your own container for implementing bidirectional streaming

If you would like to use open source or your own models, you can customize your container to support bidirectional streaming. Your container must implement the WebSocket protocol to handle incoming data frames and send response frames back to SageMaker AI.

To get started, let us build an example bi-directional streaming application with bring-your-own container use case. With this example we will:

* Build a docker container with bi-directional streaming capability – a simple echo container that streams the same bytes as received as an input to the container
* Deploy the container to a SageMaker AI endpoint
* Invoke the SageMaker AI endpoint with the new bidirectional streaming API

### Prerequisites

* AWS Account with SageMaker AI permissions
* Docker installed locally
* Python 3.12+
* Install
  [aws-sdk-python](https://pypi.org/project/aws-sdk-python/)
  for SageMaker AI Runtime
  `InvokeEndpointWithBidirectionalStream`

  API

### Build docker container with bi-directional streaming capability

First, clone our
[demo repository](https://github.com/aws-samples/sagemaker-genai-hosting-examples/tree/main/03-features/bidirectional-streaming-byoc)
and set up your environment as defined in the README.md. The steps below will create a simple demo docker image and push it Amazon ECR repository in your account.

```
# The application uses environment variables for AWS authentication. Set these before running the application:
# export AWS_ACCESS_KEY_ID="your-access-key"
# export AWS_SECRET_ACCESS_KEY="your-secret-key"
# export AWS_DEFAULT_REGION="us-west-2"

container_name="sagemaker-bidirectional-streaming"
container_tag="latest"

cd container

account=$(aws sts get-caller-identity --query Account --output text)

# Get the region defined in the current configuration (default to us-west-2 if none defined)
region=$(aws configure get region)
region=${region:-us-west-2}

container_image_uri="${account}.dkr.ecr.${region}.amazonaws.com/${container_name}:${container_tag}"

# If the repository doesn't exist in ECR, create it.
aws ecr describe-repositories --repository-names "${container_name}" --region "${region}" > /dev/null 2>&1

if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "${container_name}" --region "${region}" > /dev/null
fi

# Get the login command from ECR and execute it directly
aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account}.dkr.ecr.${region}.amazonaws.com/${container_name}

# Build the docker image locally with the image name and then push it to ECR
# with the full name.
docker build --platform linux/amd64 --provenance=false -t ${container_name} .
docker tag ${container_name} ${container_image_uri}

docker push ${container_image_uri}
```

This creates a container with a Docker label indicating to SageMaker AI that bidirectional streaming capability is supported on this container.

```
com.amazonaws.sagemaker.capabilities.bidirectional-streaming=true
```

### Deploy the demo bi-directional streaming container to the SageMaker AI endpoint

The following example script creates the SageMaker AI endpoint with the created container:

```
import boto3
from datetime import datetime

sagemaker_client = boto3.client('sagemaker', region_name=REGION)

# Create model
sagemaker_client.create_model(
    ModelName=MODEL_NAME,
    PrimaryContainer={'Image': IMAGE_URI, 'Mode': 'SingleModel'},
    ExecutionRoleArn=ROLE
)

# Create config
sagemaker_client.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[{
        'VariantName': 'AllTraffic',
        'ModelName': MODEL_NAME,
        'InitialInstanceCount': 1,
        'InstanceType': INSTANCE_TYPE,
        'InitialVariantWeight': 1.0
    }]
)

# Create endpoint
sagemaker_client.create_endpoint(
    EndpointName=ENDPOINT_NAME,
    EndpointConfigName=ENDPOINT_CONFIG_NAME
)

print(f"Endpoint '{ENDPOINT_NAME}' creation initiated")
```

### Invoke the SageMaker AI endpoint with the new bidirectional streaming API

Once the SageMaker AI endpoint is InService, we can proceed to invoke the endpoint to test the bidirectional streaming functionality of the test container.

```
#!/usr/bin/env python3
"""
SageMaker AI Bidirectional Streaming Python SDK Script.
This script connects to a SageMaker AI endpoint for bidirectional streaming communication.
"""

import argparse
import asyncio
import sys
from aws_sdk_sagemaker_runtime_http2.client import SageMakerRuntimeHTTP2Client
from aws_sdk_sagemaker_runtime_http2.config import Config, HTTPAuthSchemeResolver
from aws_sdk_sagemaker_runtime_http2.models import InvokeEndpointWithBidirectionalStreamInput, RequestStreamEventPayloadPart, RequestPayloadPart
from smithy_aws_core.identity import EnvironmentCredentialsResolver
from smithy_aws_core.auth.sigv4 import SigV4AuthScheme
import logging


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Connect to SageMaker AI endpoint for bidirectional streaming"
    )
    parser.add_argument(
        "ENDPOINT_NAME",
        help="Name of the SageMaker AI endpoint to connect to"
    )
    return parser.parse_args()


# Configuration
AWS_REGION = "us-west-2"
BIDI_ENDPOINT = f"https://runtime.sagemaker.{AWS_REGION}.amazonaws.com:8443"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SimpleClient:
    def __init__(self, endpoint_name, region=AWS_REGION):
        self.endpoint_name = endpoint_name
        self.region = region
        self.client = None
        self.stream = None
        self.response = None
        self.is_active = False

    def _initialize_client(self):
        config = Config(
            endpoint_uri=BIDI_ENDPOINT,
            region=self.region,
            aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
            auth_scheme_resolver=HTTPAuthSchemeResolver(),
            auth_schemes={"aws.auth#sigv4": SigV4AuthScheme(service="sagemaker")}
        )
        self.client = SageMakerRuntimeHTTP2Client(config=config)

    async def start_session(self):
        if not self.client:
            self._initialize_client()

        logger.info(f"Starting session with endpoint: {self.endpoint_name}")
        self.stream = await self.client.invoke_endpoint_with_bidirectional_stream(
            InvokeEndpointWithBidirectionalStreamInput(endpoint_name=self.endpoint_name)
        )
        self.is_active = True

        self.response = asyncio.create_task(self._process_responses())

    async def send_words(self, words):
        for i, word in enumerate(words):
            logger.info(f"Sending payload: {word}")
            await self.send_event(word.encode('utf-8'))
            await asyncio.sleep(1)

    async def send_event(self, data_bytes):
        payload = RequestPayloadPart(bytes_=data_bytes)
        event = RequestStreamEventPayloadPart(value=payload)
        await self.stream.input_stream.send(event)

    async def end_session(self):
        if not self.is_active:
            return

        await self.stream.input_stream.close()
        logger.info("Stream closed")

    async def _process_responses(self):
        try:
            output = await self.stream.await_output()
            output_stream = output[1]

            while self.is_active:
                result = await output_stream.receive()

                if result is None:
                    logger.info("No more responses")
                    break

                if result.value and result.value.bytes_:
                    response_data = result.value.bytes_.decode('utf-8')
                    logger.info(f"Received: {response_data}")
        except Exception as e:
            logger.error(f"Error processing responses: {e}")


def main():
    """Main function to parse arguments and run the streaming client."""
    args = parse_arguments()

    print("=" * 60)
    print("SageMaker AI Bidirectional Streaming Client")
    print("=" * 60)
    print(f"Endpoint Name: {args.ENDPOINT_NAME}")
    print(f"AWS Region: {AWS_REGION}")
    print("=" * 60)

    async def run_client():
        sagemaker_client = SimpleClient(endpoint_name=args.ENDPOINT_NAME)

        try:
            await sagemaker_client.start_session()

            words = ["I need help with", "my account balance", "I can help with that", "and recent charges"]
            await sagemaker_client.send_words(words)

            await asyncio.sleep(2)

            await sagemaker_client.end_session()
            sagemaker_client.is_active = False

            if sagemaker_client.response and not sagemaker_client.response.done():
                sagemaker_client.response.cancel()

            logger.info("Session ended successfully")
            return 0

        except Exception as e:
            logger.error(f"Client error: {e}")
            return 1

    try:
        exit_code = asyncio.run(run_client())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

The following is sample output displaying the input and output streams generated by the previous script. The container echoes incoming data to the output stream, demonstrating bidirectional streaming capability.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/demo2output.gif)

## SageMaker AI integration with Deepgram models

SageMaker AI and Deepgram have collaborated to build bidirectional streaming support for SageMaker AI endpoints.
[Deepgram](https://deepgram.com/)
, an AWS Advanced Tier Partner, delivers enterprise-grade voice AI models with industry-leading accuracy and speed. Their models power real-time transcription, text-to-speech and voice agents for contact centers, media platforms, and conversational AI applications.

For customers with strict compliance requirements that require audio processing to never leave their AWS VPC, traditional self-hosted options have required significant operational overhead to setup and maintain. Amazon SageMaker bidirectional streaming transforms this experience so customers can deploy and scale real-time AI applications with just a few actions in the AWS Management Console.

Deepgram Nova-3 speech-to-text model is available today in the AWS Marketplace for deployment as a SageMaker AI endpoint with additional models coming soon. Capabilities of Deepgram Nova-3 include multi-lingual transcription, enterprise scale performance and domain specific recognition. Deepgram is offering a 14 day free trial on Amazon SageMaker AI for developers to prototype applications without incurring software license fees. Infrastructure charges of the chosen machine type will still be incurred during this time. For more details, see the
[Amazon SageMaker AI Pricing documentation](https://aws.amazon.com/sagemaker/ai/pricing/)
.

A high-level overview and sample code is provided in the following section. Refer to the detailed quick start guide on the
[Deepgram documentation page](https://developers.deepgram.com/docs/deploy-amazon-sagemaker)
for additional information and examples. Connect with the
[Deepgram Developer Community](https://developers.deepgram.com/support)
if you need additional help with set up.

## Set up a Deepgram SageMaker AI real-time inference endpoint

To set up a Deepgram SageMaker AI endpoint:

* Navigate to the
  [AWS Marketplace Model packages section](https://us-east-1.console.aws.amazon.com/sagemaker/home?region=us-east-1#/marketplace-search-model-packages!mpSearch/search?text=deepgram)
  within the Amazon SageMaker AI console and search for
  **Deepgram**
  .
* Subscribe to the product and proceed to the launch wizard on the product page.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/Screenshot-2025-11-17-at-2.54.16-PM.png)

* Continue by providing details in the Amazon SageMaker AI real-time endpoint creation wizard. Verify that you edit the production variant to include a valid instance type when creating your endpoint configuration. The edit button may be hidden until scrolling right in the production variant table.
  `ml.g6.2xlarge`
  is a preferred instance type for initial testing. Refer to the
  [Deepgram documentation](https://developers.deepgram.com/docs/self-hosted-deployment-environments#hardware-specifications)
  for specific hardware requirements and selection guidance.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/Screenshot-2025-11-18-at-12.45.08-AM.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/24/Screenshot-2025-11-20-at-10.34.41-AM.png)

* In the endpoint summary page, take note of the endpoint name you provided as this will be needed in the following section.

## Using the Deepgram SageMaker AI real-time inference endpoint

We’ll now walk through a sample typescript application that streams an audio file to the Deepgram model hosted on a SageMaker AI real-time inference endpoint and prints a transcription streamed back in real-time.

* **Create a simple function to stream the WAV file**
  + This function opens a local audio file and sends it to Amazon SageMaker AI Inference in small binary chunks.

```
import * as fs from "fs";
import * as path from "path";
import { RequestStreamEvent } from '@aws-sdk/client-sagemaker-runtime-http2';

function sleep(ms: number): Promise<void> {
 return new Promise(resolve => setTimeout(resolve, ms));
}

async function* streamWavFile(filePath: string): AsyncIterable<RequestStreamEvent> {
 const full = path.resolve(filePath);

 if (!fs.existsSync(full)) {
 throw new Error(`Audio file not found: ${full}`);
 }

 console.log(`Streaming audio: ${full}`);

 const readStream = fs.createReadStream(full, { highWaterMark: 512_000 }); // 512 KB

 for await (const chunk of readStream) {
 yield {
 PayloadPart: {
 Bytes: chunk,
 DataType: "BINARY"
 }
 };
 }

 // Keep the stream alive to receive transcription responses after whole audio file is sent
 console.log("Audio sent, waiting for transcription to finish...");
 await sleep(15000); // Wait 15 seconds for processing final audio chunk.
 //Long audio files may require sending keep alive packets while the transcript is being processed. see https://developers.deepgram.com/docs/audio-keep-alive for more information.

 // Tell the container we're done
 yield {
 PayloadPart: {
 Bytes: new TextEncoder().encode('{"type":"CloseStream"}'),
 DataType: "UTF8"
 }
 };
}
```

* **Configure the Amazon SageMaker AI runtime client**
  + This section configures the AWS Region, the SageMaker AI endpoint name, and the Deepgram model route inside the container. Update the following values as necessary:
    - `region`
      if not using us-east-1
    - `endpointName`
      noted from the endpoint setup above
    - `test.wav`
      if using a different name for the locally stored audio file

```
import {
    SageMakerRuntimeHTTP2Client,
    InvokeEndpointWithBidirectionalStreamCommand
} from '@aws-sdk/client-sagemaker-runtime-http2';

const region = "us-east-1";              // AWS Region
const endpointName = "REPLACEME";        // Your SageMaker Deepgram endpoint name
const audioFile = "test.wav";            // Local audio file

// Deepgram WebSocket path inside the model container
const modelInvocationPath = "v1/listen";
const modelQueryString = "model=nova-3";

const client = new SageMakerRuntimeHTTP2Client({
    region
});
```

* **Invoke the endpoint and print the streaming transcription**
  + This final snippet sends the audio stream to the SageMaker AI endpoint and prints Deepgram’s streaming JSON events as they arrive. The application will show live speech-to-text output being generated.

```
async function run() {
    console.log("Sending audio to Deepgram via SageMaker...");

    const command = new InvokeEndpointWithBidirectionalStreamCommand({
        EndpointName: endpointName,
        Body: streamWavFile(audioFile),
        ModelInvocationPath: modelInvocationPath,
        ModelQueryString: modelQueryString
    });

    const response = await client.send(command);

    if (!response.Body) {
        console.log("No streaming response received.");
        return;
    }

    const decoder = new TextDecoder();

    for await (const msg of response.Body) {
        if (msg.PayloadPart?.Bytes) {
            const text = decoder.decode(msg.PayloadPart.Bytes);

            try {
                const parsed = JSON.parse(text);

                // Extract and display the transcript
                if (parsed.channel?.alternatives?.[0]?.transcript) {
                    const transcript = parsed.channel.alternatives[0].transcript;
                    if (transcript.trim()) {
                        console.log("Transcript:", transcript);
                    }
                }

                console.debug("Deepgram (raw):", parsed);

            } catch {
                console.error("Deepgram (error):", text);
            }
        }
    }

    console.log("Streaming finished.");
}

run().catch(console.error);
```

## Conclusion

In this post, we provided an overview of building real time agents with generative AI, the challenges, and how SageMaker AI bidirectional streaming helps you address these challenges. We also provided details on how to build your own container to leverage bidirectional streaming feature. We then walked you through the steps to build a sample chatbot container and the real-time speech-to-text model offered by our partner Deepgram which is a core component in a real-time voice AI agent application.

Start building bidirectional streaming applications with LLMs and SageMaker AI today.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/09/10/llinx.png)
Lingran Xia**
is a software development engineer at AWS. He currently focuses on improving inference performance of machine learning models. In his free time, he enjoys traveling and skiing.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/12/03/vggangas-LR-1.jpg)
Vivek Gangasani**
is a Worldwide Lead GenAI Specialist Solutions Architect for SageMaker Inference. He drives Go-to-Market (GTM) and Outbound Product strategy for SageMaker Inference. He also helps enterprises and startups deploy, manage, and scale their GenAI models with SageMaker and GPUs. Currently, he is focused on developing strategies and solutions for optimizing inference performance and GPU efficiency for hosting Large Language Models. In his free time, Vivek enjoys hiking, watching movies, and trying different cuisines.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/05/23/ml16160-008.jpg)
**Victor Wang**
is a Sr. Solutions Architect at Amazon Web Services, based in San Francisco, CA, supporting GenAI Startups including Deepgram. Victor has spent 7 years at Amazon; previous roles include software developer for AWS Site-to-Site VPN, AWS ProServe Consultant for Public Sector Partners, and Technical Program Manager for Amazon Aurora MySQL. His passion is learning new technologies and traveling the world. Victor has flown over two million miles and plans to continue his eternal journey of exploration.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/11/22/Chinmay-Bapat.jpg)
Chinmay Bapat**
is an Engineering Manager in the Amazon SageMaker AI Inference team at AWS, where he leads engineering efforts focused on building scalable infrastructure for generative AI inference. His work enables customers to deploy and serve large language models and other AI models efficiently at scale. Outside of work, he enjoys playing board games and is learning to ski.

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2022/06/15/deepti-ragha.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2022/06/15/deepti-ragha.png)
Deepti Ragha**
is a Senior Software Development Engineer on the Amazon SageMaker AI team, specializing in ML inference infrastructure and model hosting optimization. She builds features that improve deployment performance, reduce inference costs, and make ML accessible to organizations of all sizes. Outside of work, she enjoys traveling, hiking, and gardening.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/07/10/image-7-4-100x147.jpeg)
**[Kareem Syed-Mohammed](https://www.linkedin.com/in/kareemuddin/)**
is a Product Manager at AWS. He is focuses on enabling Gen AI model development and governance on SageMaker HyperPod. Prior to this, at Amazon QuickSight, he led embedded analytics, and developer experience. In addition to QuickSight, he has been with AWS Marketplace and Amazon retail as a Product Manager. Kareem started his career as a developer for call center technologies, Local Expert and Ads for Expedia, and management consultant at McKinsey.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/01/29/xddeng-100.png)
Xu Deng**
is a Software Engineer Manager with the SageMaker team. He focuses on helping customers build and optimize their AI/ML inference experience on Amazon SageMaker. In his spare time, he loves traveling and snowboarding.