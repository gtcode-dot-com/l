---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-12T22:51:26.422752+00:00'
exported_at: '2025-11-12T22:54:41.477158+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agents-to-cross-account-knowledge-bases
structured_data:
  about: []
  author: ''
  description: Organizations need seamless access to their structured data repositories
    to power intelligent AI agents. However, when these resources span multiple AWS
    accounts integration challenges can arise. This post explores a practical solution
    for connecting Amazon Bedrock agents to knowledge bases in Amazon Redshift clusters
    residing in different AWS accounts.
  headline: Connect Amazon Bedrock agents to cross-account knowledge bases
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agents-to-cross-account-knowledge-bases
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Connect Amazon Bedrock agents to cross-account knowledge bases
updated_at: '2025-11-12T22:51:26.422752+00:00'
url_hash: ad3e031c992d03885802062d820a214d59e5ed0a
---

Organizations need seamless access to their structured data repositories to power intelligent AI agents. However, when these resources span multiple AWS accounts integration challenges can arise. This post explores a practical solution for connecting Amazon Bedrock agents to knowledge bases in
[Amazon Redshift](https://aws.amazon.com/redshift/)
clusters residing in different AWS accounts.

## **The challenge**

Organizations that build AI agents using Amazon Bedrock can maintain their structured data in Amazon Redshift clusters. When these data repositories exist in separate AWS accounts from their AI agents, they face a significant limitation:
[Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
doesn’t natively support cross-account Redshift integration.

This creates a challenge for enterprises with multi-account architectures who want to:

* Leverage existing structured data in Redshift for their AI agents.
* Maintain separation of concerns across different AWS accounts.
* Avoid duplicating data across accounts.
* Ensure proper security and access controls.

## **Solution overview**

Our solution enables cross-account knowledge base integration through a secure, serverless architecture that maintains secure access controls while allowing AI agents to query structured data. The approach uses
[AWS Lambda](https://aws.amazon.com/lambda/)
as an intermediary to facilitate secure cross-account data access.

![Cross-Account Amazon Bedrock knowledge base architecture](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-architecture.png)

The action flow as shown above:

1. Users enter their natural language question in
   [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/)
   which is configured in the
   **agent**
   account.
2. **Amazon Bedrock Agents**
   invokes a
   **Lambda function**
   through action groups which provides access to the
   **Amazon Bedrock knowledge base**
   configured in the
   **agent-kb**
   account above.
3. Action group
   **Lambda function**
   running in
   **agent account**
   assumes an IAM role created in
   **agent-kb**
   account above to connect to
   **the knowledge base**
   in the
   **agent-kb**
   account.
4. **Amazon Bedrock Knowledge Base**
   in the
   **agent-kb**
   account uses an
   **IAM role**
   created in the same account to access
   **Amazon Redshift**
   data warehouse and query data in the data warehouse.

The solution follows these key components:

1. **Amazon Bedrock agent**
   in the
   **agent**
   account that handles user interactions.
2. **Amazon Redshift serverless workgroup**
   in VPC and private subnet in the
   **agent-kb**
   account containing structured data.
3. **Amazon Bedrock Knowledge base**
   using the Amazon Redshift serverless workgroup as structured data source.
4. **Lambda function**
   in the
   **agent**
   account.
5. **Action group configuration**
   to connect the agent in the
   **agent**
   account to the Lambda function.
6. **IAM roles and policies**
   that enable secure cross-account access.

## **Prerequisites**

This solution requires you to have the following:

1. Two AWS accounts.
   [Create an AWS account](https://aws.amazon.com/resources/create-account/)
   if you do not have one. Specific permissions required for both account which will be set up in subsequent steps.
2. [Install the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)
   (2.24.22 – current version)
3. [Set up authentication using IAM user credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html)
   for each account
4. Make sure you have
   [jq](https://jqlang.org/)
   installed,
   `jq`
   is lightweight command-line JSON processor. For example, in Mac you can use the command
   `brew install jq`
   (jq-1.7.1-apple – current version) to install it.
5. Navigate to the Amazon Bedrock console and make sure you enable access to the
   **meta.llama3-1-70b-instruct-v1:0**
   model for the
   **agent-kb**
   account and access for
   **us.amazon.nova-pro-v1:0**
   model in the
   **agent**
   account in the us-west-2, US West (Oregon) AWS Region.

## **Assumption**

Let’s call the AWS account profile,
**agent**
profile that has the Amazon Bedrock agent. Similarly, the AWS account profile be called
**agent-kb**
that has the Amazon Bedrock knowledge base with Amazon Redshift Serverless and the structured data source. We will use the us-west-2 US West (Oregon) AWS Region but feel free to choose another AWS Region as necessary (the prerequisites will be applicable to the AWS Region you choose to deploy this solution in). We will use the
**meta.llama3-1-70b-instruct-v1:0**
model for the
**agent-kb**
. This is an available on-demand model in us-west-2. You are free to choose other models with cross-Region inference but that would mean changing the roles and polices accordingly and enable model access in all Regions they are available in. Based on our model choice for this solution the AWS Region must be us-west-2. For the
**agent**
we will be using an Amazon Bedrock agent optimized model like
**us.amazon.nova-pro-v1:0**
.

## **Implementation walkthrough**

The following is a step-by-step implementation guide. Make sure to perform all steps in the same AWS Region in both accounts.

*These steps are to deploy and test an end-to-end solution from scratch and if you are already running some of these components, you may skip over those steps.*

1. 1. Make a note of the AWS account numbers in the agent and agent-kb account. In the implementation steps we will refer them as follows:


      |  |  |  |
      | --- | --- | --- |
      | **Profile** | **AWS account** | **Description** |
      | agent | 111122223333 | Account for the Bedrock Agent |
      | agent-kb | 999999999999 | Account for the Bedrock Knowledge base |

      **Note:**
      These steps use example profile names and account numbers, please replace with actuals before running.
   2. Create the Amazon Redshift Serverless workgroup in the
      **agent-kb**
      account:
      1. Log on to the
         **agent-kb**
         account
      2. Follow the
         [workshop link](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/getting-started/using-your-aws-account/019-cloudformation)
         to create the Amazon Redshift Serverless workgroup in private subnet
      3. Make a note of the namespace, workgroup, and other details and follow the rest of the
         [hands-on workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/dataloads-configurations)
         instructions.
   3. [Set up your data warehouse](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/dataloads-configurations/enabletpch)
      in the
      **agent-kb**
      account.
   4. [Create your AI knowledge base](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/dataloads-configurations/createkb)
      in the
      **agent-kb**
      account. Make a note of the knowledge base ID.
   5. [Train your AI Assistant](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/dataloads-configurations/configurekb)
      in the
      **agent-kb**
      account.
   6. [Test natural language queries](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/dataloads-configurations/testkb)
      in the
      **agent-kb**
      account. You can find the code in aws-samples git repository:
      [sample-for-amazon-bedrock-agent-connect-cross-account-kb](https://github.com/aws-samples/sample-for-amazon-bedrock-agent-connect-cross-account-kb)
      .
   7. Create necessary roles and policies in both the accounts. Run the script
      [create\_bedrock\_agent\_kb\_roles\_policies.sh](https://github.com/aws-samples/sample-for-amazon-bedrock-agent-connect-cross-account-kb/blob/main/scripts/create_bedrock_agent_kb_roles_policies.sh)
      with the following input parameters.


      |  |  |  |
      | --- | --- | --- |
      | **Input parameter** | **Value** | **Description** |
      | –agent-kb-profile | agent-kb | The agent knowledgebase profile that you set up with the AWS CLI with aws\_access\_key\_id, aws\_secret\_access\_key as mentioned in the prerequisites. |
      | –lambda-role | lambda\_bedrock\_kb\_query\_role | This is the IAM role the agent account Bedrock agent action group lambda will assume to connect to the Redshift cross account |
      | –kb-access-role | bedrock\_kb\_access\_role | This is the IAM role the agent-kb account which the `lambda_bedrock_kb_query_role` in agent account assumes to connect to the Redshift cross account |
      | –kb-access-policy | bedrock\_kb\_access\_policy | IAM policy attached to the IAM role `bedrock_kb_access_role` |
      | –lambda-policy | lambda\_bedrock\_kb\_query\_policy | IAM policy attached to the IAM role `lambda_bedrock_kb_query_role` |
      | –knowledge-base-id | XXXXXXXXXX | Replace with the actual knowledge base ID created in Step 4 |
      | –agent-account | 111122223333 | Replace with the 12-digit AWS account number where the Bedrock agent is running. (agent account) |
      | –agent-kb-account | 999999999999 | Replace with the 12-digit AWS account number where the Bedrock knowledge base is running. (agent-kb acccount) |
   8. Download the script (create\_bedrock\_agent\_kb\_roles\_policies.sh) from
      [the aws-samples GitHub repository](https://github.com/aws-samples/sample-for-amazon-bedrock-agent-connect-cross-account-kb/blob/main/scripts/create_bedrock_agent_kb_roles_policies.sh)
      .
   9. Open Terminal in Mac or similar bash shell for other platforms.
   10. Locate and change the directory to the downloaded location, provide executable permissions:

       ```
       cd /my/location
       chmod +x create_bedrock_agent_kb_roles_policies.sh
       ```
   11. If you are still not clear on the script usage or inputs, then you can run the script with the –help option and the script will display the usage:

       `./create_bedrock_agent_kb_roles_policies.sh –help`
       ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-TC1.png)
   12. Run the script with the right input parameters as described in the previous table.

       ```
       ./create_bedrock_agent_kb_roles_policies.sh --agent-profile agent \
         --agent-kb-profile agent-kb \
         --lambda-role lambda_bedrock_kb_query_role \
         --kb-access-role bedrock_kb_access_role \
         --kb-access-policy bedrock_kb_access_policy \
         --lambda-policy lambda_bedrock_kb_query_policy \
         --knowledge-base-id XXXXXXXXXX \
         --agent-account 111122223333 \
         --agent-kb-account 999999999999
       ```

       ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-TC2.png)
   13. The script on successful execution shows the summary of the IAM, roles and policies created in both accounts.

       ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-TC3.png)
   14. Log on to both the
       **agent**
       and
       **agent-kb**
       account to verify the IAM roles and policies are created.
       * + - **For the agent account:**
             Make a note of the ARN of the
             `lambda_bedrock_kb_query_role`
             as that will be the value of CloudFormation stack parameter
             *AgentLambdaExecutionRoleArn*
             in the next step.

             ![Agent IAM Role](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-agent_IAM_role.png)
           - **For the agent-kb account:**
             Make a note of the ARN of the
             `bedrock_kb_access_role`
             as that will be the value of CloudFormation stack parameter
             `TargetRoleArn`
             in the next step.

             ![Agent KB IAM Role](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-agent-kb_IAM_Role.png)
   15. Run the
       [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
       script to create a Bedrock agent:
       1. 1. 1. 1. Download the CloudFormation script: cloudformation\_bedrock\_agent\_kb\_query\_cross\_account.yaml from the
                   [aws-samples GitHub repository](https://github.com/aws-samples/sample-for-amazon-bedrock-agent-connect-cross-account-kb/blob/main/scripts/cloudformation_bedrock_agent_kb_query_cross_account.yaml)
                   .
                2. Log on to the
                   **agent**
                   account and navigate to the CloudFormation console, and verify you are in the us-west-2 (Oregon) Region, choose
                   **Create stack**
                   and choose
                   **With new resources (standard)**
                   .

                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF1.png)
                3. In the
                   **Specify template**
                   section choose
                   **Upload a template file**
                   and then
                   **Choose file**
                   and select the file from (1). Then, choose
                   **Next**
                   .
                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF2.png)
                4. Enter the following stack details and choose
                   **Next**
                   .


                   |  |  |  |
                   | --- | --- | --- |
                   | **Parameter** | **Value** | **Description** |
                   | Stack name | bedrock-agent-connect-kb-cross-account-agent | You can choose any name |
                   | AgentFoundationModelId | us.amazon.nova-pro-v1:0 | Do not change |
                   | AgentLambdaExecutionRoleArn | arn:aws:iam:: 111122223333:role/lambda\_bedrock\_kb\_query\_role | Replace with you **agent** account number |
                   | BedrockAgentDescription | Agent to query inventory data from Redshift Serverless database | Keep this as default |
                   | BedrockAgentInstructions | You are an assistant that helps users query inventory data from our Redshift Serverless database using the action group. | Do not change |
                   | BedrockAgentName | bedrock\_kb\_query\_cross\_account | Keep this as default |
                   | KBFoundationModelId | meta.llama3-1-70b-instruct-v1:0 | Do not change |
                   | KnowledgeBaseId | XXXXXXXXXX | Knowledge base id from **Step 4** |
                   | TargetRoleArn | arn:aws:iam::999999999999:role/bedrock\_kb\_access\_role | Replace with you **agent-kb** account number |

                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF3.png)
                5. Complete the acknowledgement and choose
                   **Next**
                   .
                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF4.png)
                6. Scroll down through the page and choose
                   **Submit**
                   .
                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF5.png)
                7. You will see the CloudFormation stack is getting created as shown by the status
                   **CREATE\_IN\_PROGRESS**
                   .
                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF6.png)
                8. It will take a few minutes, and you will see the status change to
                   **CREATE\_COMPLETE**
                   indicating creation of all resources. Choose the
                   **Outputs**
                   tab to make a note of the resources that were created.
                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/10/ML-19289-CF7.png)

                   In summary, the CloudFormation script does the following in the
                   **agent**
                   account.
                   1. 1. * Creates a Bedrock agent
                         * Creates an action group
                         * Also creates a Lambda function which is invoked by the Bedrock action group
                         * Defines the OpenAPI schema
                         * Creates necessary roles and permissions for the Bedrock agent
                         * Finally, it prepares the Bedrock agent so that it is ready to test.
   16. Check for model access in Oregon (us-west-2)
       1. 1. 1. 1. Verify Nova Pro (us.amazon.nova-pro-v1:0) model access in the
                   **agent**
                   account. Navigate to the Amazon Bedrock console and choose
                   **Model access**
                   under
                   **Configure and learn**
                   . Search for
                   **Model name : Nova Pro**
                   to verify access. If not, then enable model access.

                   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-agent-model-access.png)
                2. Verify access to the
                   **meta.llama3-1-70b-instruct-v1:0**
                   model in the agent-kb account. This should already be enabled as we set up the knowledge base earlier.
   17. Run the agent. Log on to
       **agent**
       account. Navigate to Amazon Bedrock console and choose
       **Agents**
       under
       **Build**
       .
       ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-agent-bedrock.png)
   18. Choose the name of the agent and choose
       **Test**
       . You can test the following questions as mentioned the workshop’s
       [Stage 4: Test Natural Language Queries](https://catalog.us-east-1.prod.workshops.aws/workshops/a0b74876-043f-4cdb-9024-ce2b8471542d/en-US/dataloads-configurations/testkb)
       page. For example:
       1. 1. 1. 1. Who are the top 5 customers in Saudi Arabia?
                2. Who are the top parts supplier in the United States by volume?
                3. What is the total revenue by region for the year 1998?
                4. Which products have the highest profit margins?
                5. Show me orders with the highest priority from the last quarter of 1997.

       ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-agent-run.png)
   19. Choose
       **Show trace**
       to investigate the agent traces.
       ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-agent-trace.png)

Some recommended best practices:

1. 1. * Phrase your question to be more specific
      * Use terminology that matches your table descriptions
      * Try questions similar to your curated examples
      * Verify your question relates to data that exists in the TPCH dataset
      * Use
        [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
        to add configurable safeguards to questions and responses.

## Clean up resources

It is recommended that you clean up any resources you do not need anymore to avoid any unnecessary charges:

1. 1. 1. Navigate to the CloudFormation console for the
         **agent**
         and
         **agent-kb account**
         , search for the stack and and choose
         **Delete**
         .
      2. S3 buckets need to be deleted separately.

         ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-CF-click-delete.png)
      3. For deleting the roles and policies created in both accounts, download the script
         `delete-bedrock-agent-kb-roles-policies.sh`
         from the
         [aws-samples GitHub repository](https://github.com/aws-samples/sample-for-amazon-bedrock-agent-connect-cross-account-kb/blob/main/scripts/delete-bedrock-agent-kb-roles-policies.sh)
         .
         1. Open Terminal in Mac or similar bash shell on other platforms.
         2. Locate and change the directory to the downloaded location, provide executable permissions:

         ```
         cd /my/location
         			chmod +x delete-bedrock-agent-kb-roles-policies.sh
         ```
      4. If you are still not clear on the script usage or inputs, then you can run the script with the –help option then the script will display the usage:

         `./ delete-bedrock-agent-kb-roles-policies.sh –help`
         ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-TC4.png)
      5. Run the script:
         `delete-bedrock-agent-kb-roles-policies.sh`
         with the same values for the same input parameters as in Step7 when running the
         `create_bedrock_agent_kb_roles_policies.sh`
         script.
         **Note:**
         Enter the correct account numbers for agent-account and agent-kb-account before running.

         ```
         ./delete-bedrock-agent-kb-roles-policies.sh --agent-profile agent \
           	--agent-kb-profile agent-kb \
         	  --lambda-role lambda_bedrock_kb_query_role \
         	  --kb-access-role bedrock_kb_access_role \
         	  --kb-access-policy bedrock_kb_access_policy \
         	  --lambda-policy lambda_bedrock_kb_query_policy \
         	  --agent-account 111122223333 \
         	  --agent-kb-account 999999999999
         ```

         The script will ask for a confirmation, say
         **yes**
         and press enter.

         ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-TC5.png)

## **Summary**

This solution demonstrates how the Amazon Bedrock agent in the
**agent**
account can query the Amazon Bedrock knowledge base in the
**agent-kb**
account.

## **Conclusion**

This solution uses Amazon Bedrock Knowledge Bases for structured data to create a more integrated approach to cross-account data access. The knowledge base in
**agent-kb**
account connects directly to Amazon Redshift Serverless in a private VPC. The Amazon Bedrock agent in the
***agent***
account invokes an AWS Lambda function as part of its action group to make a cross-account connection to retrieve response from the structured knowledge base.

This architecture offers several advantages:

1. 1. * Uses Amazon Bedrock Knowledge Bases capabilities for structured data
      * Provides a more seamless integration between the agent and the data source
      * Maintains proper security boundaries between accounts
      * Reduces the complexity of direct database access codes

As Amazon Bedrock continues to evolve, you can take advantage of future enhancements to knowledge base functionality while maintaining your multi-account architecture.

###

---

### About the Authors

![Author Kunal](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-author-kunal-100x133.jpeg)
**Kunal Ghosh**
is an expert in AWS technologies. He passionate about building efficient and effective solutions on AWS, especially involving generative AI, analytics, data science, and machine learning. Besides family time, he likes reading, swimming, biking, and watching movies, and he is a foodie.

![Author Arghya](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-author-arghya.jpeg)
**Arghya Banerjee**
is a Sr. Solutions Architect at AWS in the San Francisco Bay Area, focused on helping customers adopt and use the AWS Cloud. He is focused on big data, data lakes, streaming and batch analytics services, and generative AI technologies.

![Author Indranil](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-author-indranil-100x100.jpeg)
**Indranil Banerjee**
is a Sr. Solutions Architect at AWS in the San Francisco Bay Area, focused on helping customers in the hi-tech and semi-conductor sectors solve complex business problems using the AWS Cloud. His special interests are in the areas of legacy modernization and migration, building analytics platforms and helping customers adopt cutting edge technologies such as generative AI.

![Author Vinayak](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/11/ML-19289-author-vinayak-100x133.jpeg)
**Vinayak Datar**
is Sr. Solutions Manager based in Bay Area, helping enterprise customers accelerate their AWS Cloud journey. He’s focusing on helping customers to convert ideas from concepts to working prototypes to production using AWS generative AI services.