---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-30T18:15:39.028297+00:00'
exported_at: '2026-04-30T18:15:41.255716+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/configuring-amazon-bedrock-agentcore-gateway-for-secure-access-to-private-resources
structured_data:
  about: []
  author: ''
  description: In this post, you will configure Amazon Bedrock AgentCore Gateway to
    access private endpoints using Resource Gateway, a managed construct that provisions
    Elastic Network Interfaces (ENIs) directly inside your Amazon VPC, one per subnet.
    You will explore two implementation modes (managed and self-managed) and walk
    th...
  headline: Configuring Amazon Bedrock AgentCore Gateway for secure access to private
    resources
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/configuring-amazon-bedrock-agentcore-gateway-for-secure-access-to-private-resources
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Configuring Amazon Bedrock AgentCore Gateway for secure access to private resources
updated_at: '2026-04-30T18:15:39.028297+00:00'
url_hash: c1fd27a525c0e0c09b2b8e30056250bf1197d3f8
---

AI agents in production environments often need to reach internal APIs, databases, and private resources that sit behind
[Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/)
boundaries. Managing private connectivity for each agent-to-tool path adds operational overhead and slows deployment. Amazon Bedrock AgentCore
[VPC connectivity](https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html)
is designed to deploy AI agents and
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro)
servers without requiring the network traffic to be exposed to the public internet. This capability extends to managed Amazon VPC egress for
[Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
, so you can connect to endpoints inside private networks across your AWS environment.

In this post, you will configure Amazon Bedrock AgentCore Gateway to access private endpoints using
[Resource Gateway](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-gateway.html)
, a managed construct that provisions
[Elastic Network Interfaces (ENIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)
directly inside your Amazon VPC, one per subnet. You will explore two implementation modes (managed and self-managed) and walk through three practical scenarios: connecting to a private
[Amazon API Gateway](https://aws.amazon.com/api-gateway/)
endpoint, integrating with a MCP server on
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/)
(Amazon EKS), and accessing a private REST API.

## Key terms

The following terms are used throughout this post. Review them before proceeding to understand how each component fits into the AgentCore Gateway VPC egress architecture.

**Resource VPC:**
The Amazon VPC where your private resource lives. For example, the VPC containing your privately hosted MCP server or API endpoint. This is the Amazon VPC that AgentCore Gateway needs to reach. Resource VPC can either be in the same AWS account as the AgentCore Gateway account or in a different account.

**AgentCore Gateway account:**
The AWS account where you create and manage your AgentCore Gateway resources. This account may or may not be the same account as the Resource VPC.

**Resource Gateway:**
[Resource gateway](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-gateway.html)
acts as the private entry point into your Resource VPC. When created, it provisions one ENI per subnet that you specify, each sitting inside your VPC. Traffic from AgentCore Gateway to your private resource arrives through these ENIs.

**Resource Configuration:**
[Resource configuration for VPC resources](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-configuration.html)
defines the specific resource AgentCore Gateway is allowed to reach through the Resource Gateway, identified by a domain name, or IP address. Rather than granting access to your entire Amazon VPC, a Resource Configuration scopes connectivity to a single endpoint.

**Service Network Resource Association**
: A service network resource association connects a resource configuration to the AgentCore service network, which allows AgentCore Gateway service to invoke your private endpoint. AgentCore creates and manages this association on your behalf, regardless of which mode you use.

## How does AgentCore Gateway VPC egress work?

AgentCore Gateway VPC egress supports two modes depending on how much control you want over the underlying networking infrastructure and how you want to architect for cross-VPC connectivity.

### Managed VPC resource

In this mode, AgentCore Gateway handles everything on your behalf. You provide your VPC ID, subnet IDs, and security groups as part of your target configuration, and AgentCore automatically creates and manages the VPC Resource Gateway in your account. This mode integrates with existing network architectures, whether you use
[VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
for same-Region or cross-Region connectivity or a hub-and-spoke model with
[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
for multi-VPC and hybrid environments.

The following architecture shows how AgentCore Gateway connects to private
[Amazon API Gateway](https://aws.amazon.com/api-gateway/)
using managed VPC resource mode.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-1-12.png)

When you create an AgentCore Gateway Target with a managed VPC resource configuration, AgentCore Gateway initiates the request and routes it to the Resource Gateway inside your Resource Owner VPC. The Resource Gateway forwards traffic through an ENI provisioned in your subnet, governed by the security groups you configure. From the ENI, the request reaches the
[execute-api VPC endpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
. In managed VPC Resource mode, AgentCore creates and manages the Resource Gateway on your behalf, you only have read-only visibility into it.

### Self-managed Lattice resource

In this mode, you create and manage the VPC Lattice Resource Gateway and Resource configuration before referencing it during target creation on AgentCore Gateway. This gives you visibility and control over the Resource configuration, including the number of IPv4 addresses per ENI, subnet placement, and security group rules. More importantly, it gives you visibility into the resource configuration itself, with the ability to view it, share it using
[AWS Resource Access Manager (AWS RAM)](https://aws.amazon.com/ram/)
(required for cross-account connectivity), see associations tied to it, and retain the ability to revoke those associations when you choose.

The following architecture shows how AgentCore Gateway connects to private Rest API endpoints using self-managed lattice resource mode.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-2-9.png)

In self-managed lattice resource mode, you pre-create the Resource Gateway and Resource Configuration before configuring your AgentCore Gateway Target. When you call
[CreateGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.html)
, you pass the Resource Configuration ID to associate AgentCore Gateway target with your private endpoint. At invocation time, Resource Gateway forwards the request through an ENI provisioned in your subnet, governed by the security groups you configure. From the ENI, the request reaches the execute-api VPC endpoint. Unlike managed VPC Resource mode, you own and manage the Resource Gateway and Resource Configuration.

Use the following table to determine which mode fits your architecture. Choose managed VPC resource mode for streamlined setup, or self-managed Lattice resource mode for control over Resource Gateway lifecycle, cross-account connectivity, and visibility into associations.

|  |  |  |
| --- | --- | --- |
| **Dimension** | **AgentCore Managed VPC Resource** | **Self-Managed Lattice Resource** |
| Setup complexity | Straightforward; provide VPC ID, subnet IDs, and security group IDs. AgentCore manages the rest | Advanced; you create and manage the Amazon VPC Lattice Resource Gateway and Resource Configurations yourself, then pass the resource configuration ID to each target |
| IPv4 consumption | Each managed resource gateway consumes 1 IP address per ENI. This is not configurable | When used with Amazon Bedrock AgentCore, it consumes one IP address per subnet. If also attached to other VPC Lattice service networks, it consumes additional IPs based on the ipv4AddressesPerEni value on the resource gateway |
| Cross-account | Not natively supported use hub-and-spoke architectures ( [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) or [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) ) for cross-account / cross-VPC scenarios. | Supported with [AWS Resource Access Manage (AWS RAM)](https://aws.amazon.com/ram/) . Enables direct cross-account connectivity without requiring VPC peering or Transit Gateways. |
| Reusing existing ENIs | AgentCore automatically reuses one Resource Gateway (and its ENIs) across targets in the account whose managedVpcResource config matches on Amazon VPC, subnet set, security-group set, tags, and IP address type | You attach multiple Resource Configurations to a single Resource Gateway you own; target whose resourceConfigurationIdentifier resolves to that Resource Gateway shares its ENIs |
| Resource Gateway Lifecycle management | Amazon Bedrock AgentCore creates, reuses, and deletes Resource Gateways on your behalf | You own the full lifecycle of resource gateways and resource configurations |
| Governance and visibility | Resource Configurations are managed in the Amazon Bedrock AgentCore service account and aren’t visible in your Amazon VPC console. The underlying Resource Gateway is visible in your account in read-only mode | Full visibility into Resource Configurations, Service Network associations, and connected domains in your Amazon VPC Lattice console. You can audit connections and revoke access at a granular level |
| Pricing | Per-GB data processing charges only (for data processed through the Resource Gateway) | 1) Hourly charge for Service Network association2) Per-GB data processing charges |

## Get started with AgentCore Gateway VPC egress

In this post, you focus on the managed VPC resource mode. If you want to explore the self-managed lattice resource offering, follow the
[code samples](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/16-vpc-egress)
. Before getting started, this post assumes basic familiarity with Amazon VPC,
[AWS Command Line Interface](https://aws.amazon.com/cli/)
(AWS CLI), Amazon Bedrock AgentCore, and Amazon Bedrock AgentCore Gateway. Make sure that you have the following in place.

Currently AgentCore Gateway’s trusts publicly signed TLS certificates; it doesn’t trust certificates signed by a private CA, so the handshake to your backend fails. If your endpoint is protected by a private or self-signed certificate, find the working solution sample on
[GitHub](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/16-vpc-egress)
.

Your IAM principal needs the iam:CreateServiceLinkedRole permission for bedrock-agentcore.amazonaws.com, so that AgentCore can create the service-linked role on your behalf if it does not already exist. For the required IAM policy, see Gateway
[service-linked role](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/service-linked-roles.html#gateway-service-linked-role)
.

The Resource Gateway security group controls what traffic the Resource Gateway ENIs can send outbound to resources inside your Amazon VPC. If you don’t provide the security group while invoking
[CreateGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.html)
API, then the default security group is used.

This walkthrough assumes that you have an existing AgentCore Gateway. If you haven’t created one yet, run:

```
aws bedrock-agentcore create-gateway \
  --name my-gateway \
  --role-arn arn:aws:iam::<account-=id>:role/AgentCoreGatewayRole
```

Note the
`gatewayId`
from the response. You need it when creating AgentCore Gateway Targets in the steps that follow.

* For in-depth examples, see the GitHub
  [repository](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/16-vpc-egress)
  .

### Private Amazon API Gateway

In this section, you create an AgentCore Gateway target that routes to a private Amazon API Gateway. Call the
[CreateGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.html)
API with the following parameters. In the openApiSchema field, provide your private Amazon API Gateway endpoint URL (
`https://{api-id}-{vpce-id}.execute-api.{region}.amazonaws.com/{stage}`
). In the managedVpcResource block, provide your VPC ID, subnet IDs, and security group ID.

```
  aws bedrock-agentcore-control create-gateway-target \
    --region us-west-2 \
    --cli-input-json '{
      "gatewayIdentifier": "<GATEWAY_ID>",
      "name": "private-apigw",
      "description": "Private API Gateway",
      "targetConfiguration": {
        "mcp": {
          "openApiSchema": {
            "inlinePayload": "..."
          }
        }
      },
      "credentialProviderConfigurations": [...],
      "privateEndpoint": {
        "managedVpcResource": {
          "vpcIdentifier": "<VPC_ID>",
          "subnetIds": ["<SUBNET_ID_1>", "<SUBNET_ID_2>"],
          "endpointIpAddressType": "IPV4",
          "securityGroupIds": ["<VPCE_SG_ID>"]
        }
      }
    }'
```

After you run the command, AgentCore Gateway uses its service-linked role to provision a Resource Gateway in your VPC, creating one ENI per subnet you specified.

The following architecture diagram shows the network flow.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-3-8.png)

AgentCore Gateway initiates the request and routes it to the Resource Gateway provisioned inside Resource Owner VPC. Traffic passes through the ENI inside your private subnet, where your security group rules govern what reaches the next hop. From there, the request reaches the execute-api VPC endpoint, which provides private connectivity to your Amazon API Gateway internal endpoint. The endpoint URL format https://{api-id}-{vpce-id}.execute-api.{region}.amazonaws.com/{stage} is what you provided in the openApiSchema field of your CreateGatewayTarget call.

### Private MCP server on Amazon EKS

In this section, you create an AgentCore Gateway target that routes to a private MCP server running on Amazon EKS. Call the CreateGatewayTarget API with the following parameters. In the mcpServer block, provide your internal MCP server endpoint URL. In the managedVpcResource block, provide your VPC ID, subnet IDs, and security group ID.

```
  aws bedrock-agentcore-control create-gateway-target \
    --region us-west-2 \
    --cli-input-json '{
      "gatewayIdentifier": "<GATEWAY_ID>",
      "name": "private-apigw",
      "description": "Private API Gateway",
      "targetConfiguration": {
        "mcp": {
          "mcpServer": {
            "endpoint": "https://internal.example.com/csm/mcp"
          }
        }
      },
      "credentialProviderConfigurations": [...],
      "privateEndpoint": {
        "managedVpcResource": {
          "vpcIdentifier": "<VPC_ID>",
          "subnetIds": ["<SUBNET_ID_1>", "<SUBNET_ID_2>"],
          "endpointIpAddressType": "IPV4",
          "securityGroupIds": ["<VPCE_SG_ID>"]
        }
      }
    }'
```

After you run this command, AgentCore provisions a Resource Gateway in your VPC, creating one ENI per subnet you specified. The following architecture diagram shows the end-to-end traffic path.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-4-8.png)

AgentCore Gateway sends an HTTPS request to your internal endpoint. The Amazon Route 53 private hosted zone resolves that domain to the internal
[Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#:~:text=Classic%20Load%20Balancers.-,Network%20Load%20Balancer%20components,listeners%20to%20your%20load%20balancer.)
(NLB). The request enters the Resource Owner VPC through the Resource Gateway, passes through the ENI governed by your security groups, and arrives at the NLB. The NLB terminates TLS on port 443 using an
[AWS Certificate Manager (ACM) public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html)
, then forwards the request over HTTP on port 80 to the
[NGINX Ingress Controller](https://docs.nginx.com/nginx-ingress-controller/)
running on Amazon EKS, which routes it to the appropriate pod.

### Private REST API target

In this section, you create an AgentCore Gateway target that routes to a private REST API endpoint. This applies to any REST API running inside your Amazon VPC such as a containerized microservice. The CreateGatewayTarget API call follows the same pattern as the previous sections. In the openApiSchema field, provide your OpenAPI schema describing the REST API. In the
`managedVpcResource`
block, provide your VPC ID, subnet IDs, and security group ID. After AgentCore Gateway provisions the Resource Gateway in your VPC, the following architecture diagram shows the end-to-end traffic path.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-5-8.png)

AgentCore Gateway sends an HTTPS request to your internal endpoint. The Amazon Route 53 private hosted zone resolves that domain to the internal
[Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
(ALB). The request enters the Resource Owner VPC through the Resource Gateway, passes through the ENI governed by your security groups, and arrives at the internal ALB. The ALB terminates TLS on port 443 using an AWS Certificate Manager (ACM) public certificate, then forwards the request over HTTP on port 8000 to the target group containing your backend servers.

## Clean up

To avoid ongoing charges, delete all resources created in this walkthrough. For reference, see the AgentCore Gateway VPC egress
[pricing page](https://aws.amazon.com/bedrock/agentcore/pricing/)
. Additionally, Amazon EKS clusters, load balancers, and API Gateway endpoints incur charges while running. Verify that your resources are deleted to stop charges. If you followed the GitHub
[sample](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/16-vpc-egress)
, make sure to run the cleanup section at the end of each Jupyter Notebook.

If you used managed VPC resource mode, deleting the Gateway Target removes the associated Amazon VPC Resource Gateway.

```
aws bedrock-agentcore delete-gateway-target \
    --gateway-identifier <gateway-id> \
    --target-id <target-id>
```

## Conclusion

As AI agents take on more complex tasks, they need secure access to the tools and services that power your business, many of which live inside private networks. AgentCore Gateway VPC egress allows your agents to reach private MCP servers, internal APIs, databases, and on-premises systems without exposing them to the public internet.Managed VPC resource mode integrates directly with your existing VPC and requires minimal configuration. Self-managed lattice resource mode gives you fine-grained control but requires additional setup. Both route traffic through a Resource Gateway that doesn’t leave the AWS network.

## Next steps

* Identify one internal API or MCP server in your environment that would benefit from AI agent access
* Review your existing Amazon VPC architecture to determine which mode (Managed VPC Resource or Self-Managed Lattice Resource) fits your requirements
* Review the Amazon Bedrock AgentCore Gateway
  [documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-vpc-egress.html)
  for additional configuration options
* Explore the Amazon VPC Lattice Resource Gateway
  [documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-egress-private-endpoints.html)
  for cross-account scenarios
* Explore additional integration patterns and advanced configurations, see
  [GitHub samples.](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/16-vpc-egress)

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-6-5.png)**
[Eashan Kaushik](https://www.linkedin.com/in/eashan-kaushik/)
is a Specialist Solutions Architect AI/ML at Amazon Web Services. He is driven by creating cutting-edge generative AI solutions while prioritizing a customer-centric approach to his work. Before this role, he obtained an MS in Computer Science from NYU Tandon School of Engineering. Outside of work, he enjoys sports, lifting, and running marathons.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-7-5.png)
Thomas Mathew Veppumthara](https://www.linkedin.com/in/thomasmathewv/)
is a Sr. Software Engineer at Amazon Web Services (AWS) with Amazon Bedrock AgentCore. He has previous generative AI leadership experience in Amazon Bedrock Agents and nearly a decade of distributed systems expertise across Amazon eCommerce Services and Amazon Elastic Block Store (Amazon EBS). He holds multiple patents in distributed systems, storage, and generative AI technologies.

[Rohin Meduri](https://www.linkedin.com/in/rohin-meduri-bb3b2113b/)
[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/29/image-8-5-100x137.png)](https://www.linkedin.com/in/rohin-meduri-bb3b2113b/)
is a Software Engineer at Amazon Web Services (AWS) with Amazon Bedrock AgentCore. He has previous AI development experience with Amazon Bedrock Agents and Amazon Lex. Before this role, he obtained a BS in Computer Science from the University of Washington. Outside of work, he enjoys chess, pool, and music production.