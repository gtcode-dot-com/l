---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T19:52:18.103471+00:00'
exported_at: '2026-03-03T19:52:22.252820+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-serverless-conversational-ai-agent-using-claude-with-langgraph-and-managed-mlflow-on-amazon-sagemaker-ai
structured_data:
  about: []
  author: ''
  description: This post explores how to build an intelligent conversational agent
    using Amazon Bedrock, LangGraph, and managed MLflow on Amazon SageMaker AI.
  headline: Build a serverless conversational AI agent using Claude with LangGraph
    and managed MLflow on Amazon SageMaker AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/build-a-serverless-conversational-ai-agent-using-claude-with-langgraph-and-managed-mlflow-on-amazon-sagemaker-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Build a serverless conversational AI agent using Claude with LangGraph and
  managed MLflow on Amazon SageMaker AI
updated_at: '2026-03-03T19:52:18.103471+00:00'
url_hash: 9780145a7275ae9e6579d9676d23b83788c76ae1
---

Customer service teams face a persistent challenge. Existing chat-based assistants frustrate users with rigid responses, while direct
[large language model](https://aws.amazon.com/what-is/large-language-model/)
(LLM) implementations lack the structure needed for reliable business operations. When customers need help with order inquiries, cancellations, or status updates, traditional approaches either fail to understand natural language or can’t maintain context across multistep conversations.

This post explores how to build an intelligent conversational agent using
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
,
[LangGraph](https://www.langchain.com/langgraph)
, and
[managed MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
on
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/)
.

## Solution overview

The conversational AI agent presented in this post demonstrates a practical implementation for handling customer order inquiries, a common but often challenging use case for existing customer service automation solutions. We implement an intelligent order management agent that addresses these challenges by helping customers find information about their orders and take actions such as cancellations through natural conversation. The system uses a graph-based conversation flow with three key stages:

1. **Entry intent**
   – Identifies what the customer wants and collects necessary information
2. **Order confirmation**
   –Presents found order details and verifies customer intentions
3. **Resolution**
   – Executes the customer’s request and provides closure

This agentic flow is illustrated in the following graphic.

![Customer service workflow diagram showing process flow from start through entry intent, order confirmation, and resolution to end, with multiple pathway options](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-18704-1.png)

## Problem statement

Most customer service automation solutions fall into two categories, each with significant limitations.

Rule-based chat assistant often fail at natural language understanding, leading to frustrating user experiences. They typically follow rigid decision trees that can’t handle the nuances of human conversation. When users deviate from expected inputs, these systems fail, forcing users to adapt to the assistant rather than the other way around. For example, a rule-based chat assistant might recognize “I want to cancel my order” but fail with “I need to return something I just bought” because it doesn’t match predefined patterns.

Meanwhile, modern LLMs excel at understanding natural language but present their own challenges when used directly. LLMs don’t inherently maintain state or follow multistep processes, making conversation management difficult. Connecting LLMs to backend systems requires careful orchestration, and monitoring their performance presents unique observability challenges. Most critically, LLMs may generate plausible but incorrect information when they lack access to domain knowledge.

To understand these limitations for a real-world example, consider a seemingly simple customer service scenario: a user needs to check on an order status or request a cancellation. This interaction requires understanding the user’s intent, extracting relevant information like order numbers and account details, verifying information against backend systems, confirming actions before execution, and maintaining context throughout the conversation. Without a structured approach, both rule-based systems and raw LLMs can’t handle these multistep processes that require memory, planning, and integration with external systems.

These fundamental limitations explain why existing approaches consistently fall short in real-world applications. Rule-based systems can’t effectively bridge natural conversation with structured business processes, while LLMs can’t maintain state across multiple interactions. Neither approach can seamlessly integrate with backend systems for data retrieval and updates, and both provide limited visibility into performance and user experience. Most critically, current solutions can’t balance the flexibility needed for natural conversation with the business rule enforcement required for reliable customer service.

This solution addresses these challenges through AI agents—systems that combine the natural language capabilities of LLMs with structured workflows, tool integration, and comprehensive observability.

## Solution architecture

This solution implements a serverless conversational AI system using a WebSocket-based architecture for real-time customer interactions. Customers access a React frontend hosted on
[Amazon Simple Storage Service](https://aws.amazon.com/s3/)
(Amazon S3) and delivered through
[Amazon CloudFront](https://aws.amazon.com/cloudfront/)
. When customers send messages, the system establishes a persistent WebSocket connection through
[Amazon API Gateway](https://aws.amazon.com/api-gateway/)
to
[AWS Lambda](https://aws.amazon.com/lambda/)
functions that orchestrate the conversation flow. The following diagram illustrates the solution architecture.

![Amazon Web Services cloud architecture diagram showing serverless application with Amazon CloudFront, Amazon API Gateway, Amazon Virtual Private Cloud with public and private subnets, AWS Lambda, Amazon Relational Database Service, and machine learning services including Amazon SageMaker and Amazon Bedrock](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-18704-2.png)

## Agent architecture

This solution uses AI agents, systems where LLMs dynamically direct their own processes and tool usage while maintaining control over how they accomplish tasks. Unlike simple LLM applications, these agents maintain state and context across multiple interactions, can use external tools to gather information or perform actions, reason about their next steps based on previous outcomes, and operate with some degree of autonomy. The agent workflow follows a structured pattern of initialization, understanding user intent, planning required actions, executing tool calls when needed, generating responses, and updating conversation state for future interactions.

To build effective conversational agents, we need four core capabilities:

1. Intelligence to understand and respond to users
2. Memory to maintain context across conversations
3. Ability to take actions in external systems
4. Orchestration to manage complex multistep workflows

Our implementation addresses these requirements through specific
[Amazon Web Services](https://aws.amazon.com/)
(AWS) services and frameworks.

[Amazon Bedrock](https://aws.amazon.com/bedrock/)
serves as the intelligence layer, providing access to state-of-the-art
[foundation models](https://aws.amazon.com/what-is/foundation-models/)
(FMs) through a consistent API. Amazon Bedrock is used to handle intent recognition to understand what users are trying to accomplish, entity extraction to identify key information such as order numbers and customer details, natural language generation to create contextually appropriate responses, decision-making to determine the next best action in conversation flows, and coordination of tool use to interact with external systems. This intelligence layer enables our agent to understand natural language while maintaining the structured decision-making needed for reliable customer service.

State management (agent memory) is handled through
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
, which provides persistent storage for conversation context even if there are interruptions or system restarts. The state includes session IDs as unique conversation identifiers, complete conversation history for context maintenance, formatted transcripts optimized for model context windows, extracted information such as order numbers and customer details, and process flags indicating confirmation status and information retrieval success. This persistent state allows our agent to maintain context across multiple interactions, addressing one of the key limitations of raw LLM implementations.

State management snippet code (for full implementation you can reference the code in
[backed/app.py](https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow/blob/main/backend/app.py)
):

```
# Save conversation state to DynamoDB
ttl_value = int(time.time()) + (3600 * 4)  # 4 hrs
item = {
    'conversationId': session_id,
    'state': json.dumps(state_dict),
    'chat_status': state_dict['session_end'],
    'update_ts_pst': str(datetime.now(pst)),
    'ttl': ttl_value,
    'timestamp': int(time.time())
}
ddb_table.put_item(Item=item)
```

The state includes a Time-To-Live (TTL) value that automatically expires conversations after a period of inactivity, helping to manage storage costs.

Function calling, also known as tool use, enables our agent to interact with external systems in a structured way. Instead of generating free-form text that attempts to describe an action, the model generates structured calls to predefined functions with specific parameters. You can think of this as giving the LLM a set of tools complete with instruction manuals, where the LLM decides when to use these tools and what information to provide. Our implementation defines specific tools that connect to an
[Amazon Relational Database (Amazon RDS) for PostgreSQL](https://aws.amazon.com/rds/postgresql/)
database:
`get_user`
for customer lookups,
`get_order_by_id`
for order details,
`get_customer_orders`
for listing customer orders,
`cancel_order`
for order cancellations, and
`update_order`
for order modifications.

The following code snippet allows proper handling of the message sequence between the assistant and user along with the right tool name and inputs or parameters required. (For implementation details, refer to
[backend/utils/utils.py](https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow/blob/main/backend/utils/utils.py)
):

```
def use_tool(messages):
    tool_use = messages[-1]["content"][-1].get("toolUse")
    if tool_use:
        tool_name = tool_use["name"]
        tool_input = tool_use["input"]

        # Process the tool call
        tool_result = _process_tool_call(tool_name, tool_input)

        # Format response for the model
        message = {
            "role": "user",
            "content": [
                {
                    "toolResult": {
                        "toolUseId": tool_use["toolUseId"],
                        "content": [
                            {"text": json.dumps(tool_result)}
                        ],
                        "status": "success",
                    }
                }
            ],
        }
        return message
```

The tools are defined with JSON schemas that provide clear contracts for the model to follow:

```
tool_config = {
    "toolChoice": {"auto": {}},
    "tools": [
        {
            "toolSpec": {
                "name": "get_order_by_id",
                "description": "Retrieves the details of a specific order based on the order ID.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "order_id": {
                                "type": "string",
                                "description": "The unique identifier for the order.",
                            }
                        },
                        "required": ["order_id"],
                    },
                },
            },
        }
    ]
}
```

The previous snippet code shows only one example of tool definition, however in the implementation there are three different tools configured. For full details, refer to
[backend/tools\_config/entry\_intent\_tool.py](https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow/blob/main/backend/tools_config/entry_intent_tool.py)
or
[backend/tools\_config/agent\_tool.py](https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow/blob/main/backend/tools_config/agent_tool.py)

This capability grounds the model to real-world data and systems, reduces hallucinations by providing factual information, extends the model’s capabilities beyond what it could do alone, and enforces consistent patterns for system interactions. The structured nature of function calling means that the model can only request specific data through well-defined interfaces rather than making assumptions.

LangGraph provides the orchestration framework for building stateful, multistep applications using a directed graph approach. It offers explicit tracking of conversation state, separation of concerns where each node handles a specific conversation phase, conditional routing for dynamic decision-making based on context, cycle detection to handle loops and repetitive patterns, and flexible architecture that’s straightforward to extend with new nodes or modify existing flows. You can think of LangGraph as creating a flowchart for your conversation, where each box represents a specific part of the conversation and the arrows show how to move between them.

The conversation flow is implemented as a directed graph using LangGraph. For reference, check the agentic flow graphic in the
**Solution architecture**
section.

The following code snippet shows the state graph that is a structure graph context used to collect information across different user interactions giving the agent the proper context:

```
class State(TypedDict):
    # Messages tracked in the conversation history
    messages: list
    # Transcription attributes tracks updates posted by the agent
    transcript: list
    # Session Id is the unique identifier attribute of the conversation
    session_id: str
    # Order number
    order_number: str
    # tracks in the conversation is still active
    session_end: bool
    # tracks the current node in the conversation
    current_turn: int
    # tracks the next node in the conversation
    next_node: str
    # track status of the confirmation
    order_confirmed: bool
    # track status of the orders eligible
    order_info_found: bool
```

This state object maintains the relevant information about the conversation, allowing the system to make informed decisions about routing and responses.

Our conversation flow uses three main nodes: the entry intent node handles initial user requests and extracts key information, the order confirmation node verifies details and confirms user intent, and the resolution node executes requested actions and provides closure. This approach offers explicit state management, conditional routing, separation of concerns, reusability across different conversation flows, and clear visualization of conversation paths:

```
# Define nodes and edges
graph_builder = StateGraph(State)
# Add nodes
graph_builder.add_node("entry_intent", entry_intent.node)
graph_builder.add_node("order_confirmation", order_confirmation.node)
graph_builder.add_node("resolution", resolution.node)
# Add conditional edges with routing logic
graph_builder.add_conditional_edges(
    START,
    initial_router,
    {
        'entry_intent': 'entry_intent',
        'order_confirmation': 'order_confirmation',
        'resolution': 'resolution'
    }
)
```

The edges between nodes use conditional logic to determine the flow on a runtime execution as shown in the following code snippet based on the content of the StateGraph:

```
graph_builder.add_conditional_edges(
    'entry_intent',
    lambda x: x["next_node"],
    {
        'order_confirmation': 'order_confirmation',
        '__end__': END
    }
)
```

Each node in the conversation graph is implemented as a Python function that processes the current state and returns an updated state. The entry intent node handles initial user requests, extracts key information such as order numbers, and determines next steps by interpreting customer queries. It uses tools to search for relevant order information, extract key details such as order numbers or customer identifiers, and determines if enough information is available to proceed. The order confirmation node verifies details and confirms user intent by presenting found order details to the customer, verifying this is the correct order being discussed, and confirming the customer’s intentions regarding the order. The resolution node executes requested actions and provides closure by executing necessary actions such as providing status or canceling orders, confirming successful completion of requested actions, answering follow-up questions about the order, and providing a natural conclusion to the conversation:

```
@mlflow.trace(span_type=SpanType.AGENT)
def node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Entry intent node for processing chat messages and managing order information.

    This node handles:
    1. Initial message processing with the chat model
    2. Tool execution for order information retrieval
    3. State management and updates
    4. Dynamic routing based on order information
    """
```

For full implementation details, refer to:
[backend/nodes](https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow/tree/main/backend/nodes)
.

The nodes use a consistent pattern of extracting relevant information from the state, processing the user message using the LLM, executing the necessary tools, updating the state with new information, and determining the next node in the flow.

Observability becomes essential because LLM applications present unique challenges including nondeterministic outputs where the same input can produce different results, complex chains where multiple models and tools interact in sequence, performance monitoring where latency affects user experience, and quality assessment that requires specialized metrics. Managed MLflow on Amazon SageMaker AI addresses these challenges through specialized tracing capabilities that monitor model interactions, latency, token usage, and conversation paths.

Each conversation node is decorated with MLflow tracing:

```
@mlflow.trace(span_type=SpanType.AGENT)
def node(state: Dict[str, Any]) -> Dict[str, Any]:
    # Node implementation
```

This straightforward decorator automatically captures rich information about each node’s execution. It records model invocations, showing which models were called and with what parameters. It tracks response metrics such as latency, token usage, and completion reasons. It maps conversation paths, showing how users navigate through the conversation graph. It also logs tool usage, indicating which tools were called and their results, as well as error patterns identifying when and why failures occur.

The captured data is visualized in the MLflow UI, providing insights for production performance monitoring, optimization opportunities, debugging, and business impact measurement.

MLflow traces capture the whole agentic workflow execution including the nodes involved in the interaction, the inputs and outputs per node, and additional metadata such as the latency, the tool calls, and the conversation sequence.

The following screenshot shows an example of MLFlow tracking server traces capturing the agentic workflow execution, including nodes involved, inputs and outputs per node, and metadata such a latency, tool calls, and conversation sequence.

![MLflow LangGraph experiment tracking interface showing conversational AI workflow execution timeline with task hierarchy, 48-second total duration, and input parameters for order cancellation request](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/17/ML-18704-3.png)

This traceability is critical for continuous improvement of the agent. Developers can identify patterns in successful conversations and opportunities for optimization.

## Prerequisites

To build a serverless conversational AI agent using Claude with LangGraph and managed MLflow on Amazon SageMaker AI, you need the following prerequisites:

AWS account requirements:

* An AWS account with permissions to create Lambda functions, DynamoDB tables, API gateways, S3 buckets, CloudFront distributions, Amazon RDS for PostgreSQL instances, and
  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)
  (Amazon VPC) resources
* Amazon Bedrock access with Claude 3.5 Sonnet by Anthropic enabled

Development environment:

Skills and knowledge:

* Familiarity with serverless architectures
* Basic knowledge of Python and React
* Understanding of AWS services (AWS Lambda, Amazon DynamoDB, Amazon VPC)

## Deployment guide

To build a serverless conversational AI agent using Claude with LangGraph and managed MLflow on Amazon SageMaker AI, follow these steps:

1. Clone the
   [repository](https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow)
   and set up the project root:

```
git clone https://github.com/aws-samples/sample-aws-genai-serverless-orchestration-chatbot-mlflow.git
cd sample-aws-genai-serverless-orchestration-chatbot-mlflow
export PROJECT_ROOT=$(pwd)
```

2. Bootstrap your AWS environment (required if the bootstrap wasn’t done before):

```
cd $PROJECT_ROOT/infra
cdk bootstrap
```

3. Install dependencies:

```
# Install dependencies
cd $PROJECT_ROOT
make install
```

4. Build and deploy application:

```
cd $PROJECT_ROOT
make deploy
```

This script will:

1. Deploy the backend infrastructure, including the VPC, Lambda function, database, and MLflow
2. Get the Lambda ARN from the backend stack
3. Deploy the frontend with integrated WebSocket API Gateway
4. Get the actual WebSocket API URL from the deployed stack
5. Create and upload
   `config.json`
   with runtime configuration to Amazon S3

## Clean up

To avoid ongoing charges from the resources created in this post, clean up the resources when they’re no longer needed. Use the following command:

```
cd $PROJECT_ROOT
make clean
```

## Conclusion

In this post, we showed how combining the reasoning capabilities of LLMs from Amazon Bedrock, orchestration capabilities of LangGraph, and observability of managed MLflow on Amazon SageMaker AI can be used to build customer service agents. The architecture enables natural, multiturn conversations while maintaining context across interactions, seamlessly integrating with backend systems to perform real-world actions such as order lookups and cancellations.

The comprehensive observability is provided by MLflow so developers can monitor conversation flows, track model performance, and optimize the system based on real usage patterns. By using AWS serverless services, this solution automatically scales to handle varying workloads while maintaining cost efficiency through pay-per-use pricing. You can use this blueprint to build sophisticated conversational AI solutions that bridge the gap between natural language interaction and structured business processes, delivering business value through improved customer experiences and operational efficiency.

Ready to take your conversational AI agent further? Get started with
[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
to accelerate your agents to production with intelligent memory and a gateway to enable secure, controlled access to tools and data. Discover how
[MLflow integrates with Bedrock AgentCore Runtime](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main/examples/sagemaker-mlflow-agentcore-runtime)
for comprehensive observability across your agent ecosystem.

---

## About the Authors

### Sri Potluri

**Sri Potluri**
is a Cloud Infrastructure Architect at AWS. He is passionate about solving complex problems and delivering well-structured solutions for diverse customers. His expertise spans across a range of cloud technologies, providing scalable and reliable infrastructures tailored to each project’s unique challenges.

### Luis Felipe Yepez Barrios

**Luis Felipe Yepez Barrios**
is a Machine Learning Engineer with AWS Professional Services, focused on scalable distributed systems and automation tooling to expedite scientific innovation in the field of machine learning (ML). Furthermore, he assists enterprise clients in optimizing their machine learning solutions through AWS services.