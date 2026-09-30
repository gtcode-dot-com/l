---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-30T02:43:31.869049+00:00'
exported_at: '2026-09-30T02:43:35.344501+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/automate-user-level-custom-permissions-for-amazon-quick
structured_data:
  about: []
  author: ''
  description: 'Amazon Quick custom permissions let you enforce least-privilege access
    by toggling features per user. This post walks through four patterns to automate
    custom permissions across the user lifecycle: a RegisterUser API parameter, account
    and role defaults, event-driven Amazon EventBridge and AWS Lambda automation,
    and...'
  headline: Automate user-level custom permissions for Amazon Quick
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/automate-user-level-custom-permissions-for-amazon-quick
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Automate user-level custom permissions for Amazon Quick
updated_at: '2026-09-30T02:43:31.869049+00:00'
url_hash: 40b2e49a962d14793535c0f4d57473e3e7bf78b0
---

As
[Amazon Quick](/quick/)
environments scale and new AI-powered capabilities expand what users can do, automating user-level custom permissions becomes critical to maintaining the principle of least privilege. To address this, with
[custom permissions](https://docs.aws.amazon.com/quick/latest/userguide/custom-permissions.html)
in Quick, you can enforce fine-grained access control by toggling specific features on or off for individual users. For example, with custom permissions, you can control access so that financial analysts author reports without exporting raw data, and external partners view dashboards without accessing sharing controls.

While Quick provides various options to apply custom permissions at the account, role, and user level, there are scenarios where your organization’s specific permissions need to be applied dynamically. This post walks through four architectural patterns to automate custom permissions assignment at key stages of the user lifecycle. The approaches range from a single API parameter to an event-driven automation, covering new users, future users, group-based logic, and retroactive bulk updates.

## What we will cover

We will explore four scenarios to handle key stages of the user lifecycle:

1. **Pre-registered users**
   : If you build custom portals or scripts, we show how to apply custom permissions proactively at the exact moment of user creation using the
   `RegisterUser`
   API.
2. **Default account or role permissions:**
   To set default custom permissions at the account or role level, we cover how to use the
   `UpdateAccountCustomPermission`
   and
   `UpdateRoleCustomPermission`
   APIs to enforce a default profile for all existing and future users, no additional automation required.
3. **Event-driven custom logic**
   : When you need conditional logic beyond native defaults (such as applying different profiles based on group membership) we show how to use Amazon EventBridge and AWS Lambda to automatically detect new group memberships and apply permissions dynamically. This supports both native Quick groups and AWS IAM Identity Center (IDC) groups.
4. **Retroactive batch updates**
   : For existing users who were provisioned before automation was in place, we provide a robust Python script to retroactively apply custom permissions to all users in specified Quick groups.

## Scenario 1: Pre-registered users (API and CLI)

If you have a custom onboarding portal that provisions users using the
[RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html)
API, you don’t need complex automation. You can apply custom permissions during the creation of the Quick user by including the
`--custom-permissions-name`
parameter in your call.

**When to use this approach**
: Your organization controls the user creation process end-to-end through a custom portal or script. This is the most direct path, no event-driven infrastructure required. This is especially common for software as a service (SaaS) companies embedding Quick across customer accounts. For instance, automatically restricting premium features like paginated reports and GenBI based on a customer’s pricing tier at the moment each user is provisioned.

The following example applies a custom permissions profile named
**Restricted-Author-Profile**
to Authors in the account, but the same API can be used to apply permissions profiles to any role (including Author Pros, Admins, Admin Pros, Readers, and Reader Pros).

```
aws quicksight register-user \
    --aws-account-id 123456789012 \
    --namespace default \
    --identity-type QUICKSIGHT \
    --user-role AUTHOR \
    --email user@example.com \
    --user-name user_name \
    --custom-permissions-name "Restricted-Author-Profile"
```

## Scenario 2: Default account or role permissions (API and CLI)

With two native APIs, you can set default custom permission profiles without per-user automation. Note that Quick custom permissions follow a three-level hierarchy (account, role, and user) where user-level settings override role-level, which override account-level,
[allowing administrators to implement flexible, layered security policies](/blogs/business-intelligence/establishing-enterprise-governance-in-amazon-quick-using-custom-permissions/)
.

**When to use this approach:**
These APIs cover both current and future use cases with minimal operational overhead. Start here before building custom automation. Move to Scenario 3 only if you need conditional logic beyond what account or role-level defaults support. For example, a 50,000-user enterprise may need all newly launched GenBI features and connectors blocked by default until their security team completes a 60–90-day review. An account-level default enforces that restriction instantly, without requiring any per-user automation and with no provisioning gap.

### Option A: Account-level default

The
[UpdateAccountCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountCustomPermission.html)
API sets a fallback custom permission profile that Quick applies to any user who doesn’t have an explicit profile assigned, including new users created with Just-In-Time provisioning.

```
aws quicksight update-account-custom-permission \
    --aws-account-id 123456789012 \
    --custom-permissions-name "Restricted-User-Profile"
```

### Option B: Role-level default

With the
[UpdateRoleCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateRoleCustomPermission.html)
API, you can set a default custom permission profile per Quick role (READER, AUTHOR, ADMIN, and PRO roles).

```
aws quicksight update-role-custom-permission \
    --aws-account-id 123456789012 \
    --role AUTHOR \
    --namespace default \
    --custom-permissions-name "Restricted-Author-Profile"
```

## Scenario 3: Event-driven custom logic (Amazon EventBridge and Lambda)

This scenario addresses more granular requirements: applying different custom permissions profiles to users based on which Quick or IAM Identity Center group they belong to. For example, a 125,000-employee technology services company needs authors in each business unit to receive distinct permission profiles at the moment of group assignment. This prevents cross-unit asset sharing while granting power-user access only to approved individuals, even though all authors share the same Quick role. Because we don’t have a native API for assigning custom permissions to a Group, we will need an architecture that detects when a user is added to a group that should have specific permissions.

**Note: We suggest combining this approach with Scenario 2 for a fully layered permissions strategy.**
Scenarios 2 and 3 are complementary, not alternatives. When a user is provisioned through Just-In-Time federation, there’s an unavoidable window between account creation and the moment an administrator adds them to the appropriate group. Scenario 3 only fires on the group membership event.

To keep users from ever being in an unrestricted state, apply Scenario 2 first as a baseline: set an account-level or role-level default that enforces your most restrictive acceptable profile. Then use Scenario 3 to refine permissions once the user is assigned to a group. The user-level override from Scenario 3 will take precedence over the Scenario 2 default, so there is no conflict, only complementary layers of control.

Consider a global bank with more than 200,000 users, provisioned through single sign-on (SSO), that must block data export the instant an employee joins. Scenario 2 closes that gap immediately with a restrictive account-level default, and Scenario 3 refines permissions once the user is assigned to their compliance group. This prevents employees from downloading sensitive client data during the window between provisioning and group assignment.

Quick and IAM Identity Center emit distinct AWS CloudTrail events for group membership changes. Quick emits
`CreateGroupMembership`
when a user is added and
`DeleteGroupMembership`
when removed. IAM Identity Center emits
`AddMemberToGroup`
when a user is added and
`RemoveMemberFromGroup`
when removed. The following architecture detects these events to trigger permission updates automatically.

We will build this using Amazon EventBridge (to detect the event) and AWS Lambda (to apply the fix).

[![Event-driven flow where a group membership change captured by CloudTrail triggers an Amazon EventBridge rule and a Lambda function that applies a Quick custom permission profile](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/09/02/ML-21102-1.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/09/02/ML-21102-1.png)

Figure 1: Event-driven architecture that applies a custom permission profile when a user is added to a Quick or IAM Identity Center group

1. A user is added to a Quick or Identity Center group.
2. **Amazon CloudTrail:**
   Captures the
   `CreateGroupMembership`
   or
   `AddMemberToGroup`
   events.
3. **Amazon EventBridge:**
   Filters these logs to identify when a user is successfully added to the group.
4. **AWS Lambda:**
   Extracts the user details and applies the correct permission profile using the
   `UpdateUserCustomPermission`
   API.

### Prerequisites

Before implementing this solution, confirm you have the following:

1. An
   [AWS account](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fportal.aws.amazon.com%2Fbilling%2Fsignup%2Fresume&amp;client_id=signup)
   with administrative access.
2. [AWS Identity and Access Management (IAM)](/iam/)
   permissions to create and manage AWS resources using AWS CloudFormation.
3. Access to the following AWS services:
   1. [AWS CloudFormation](/cloudformation)
      : deploys and manages the infrastructure stack as code.
   2. [Amazon Quick](/quick/)
      : the target service where custom permissions are applied.
   3. [AWS CloudTrail](/cloudtrail/)
      : must be enabled in the target AWS Region. Captures Quick and IDC API events that Amazon EventBridge consumes.
   4. [Amazon EventBridge](/eventbridge/)
      : filters CloudTrail events to detect group membership changes.
   5. [AWS Lambda](/lambda/)
      : executes the automation logic that calls the
      `UpdateUserCustomPermission`
      API.
   6. [AWS IAM Identity Center](/iam/)
      : required only if using IDC group-based triggers.
4. Python 3.9+ and AWS Command Line Interface (AWS CLI) v2 are required for running the batch update script in Scenario 4.

### Deploy with CloudFormation

You can deploy the full pipeline (IAM role, Lambda function, and Amazon EventBridge rule) using the provided CloudFormation template. The CloudFormation stack must be deployed in the same AWS Region as your Amazon Quick subscription, since Amazon EventBridge rules only capture events within their own Region.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/04/29/launch-stack-button.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=quickcustompermissions&amp;templateURL=https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/ML-21102/AutomateUser-LevelCustomPermissionsforAmazonQuick.yaml)

The template accepts the following parameters:

|  |  |
| --- | --- |
| **Parameter** | **Description** |
| UseIdentityCenter | Set to true if your Quick account uses IAM Identity Center |
| TargetGroupName | The name of the group to apply custom permissions to. For Quick groups, this is the Quick group name. For IDC groups, this is the IDC group DisplayName.  Important: Each deployment targets either a Quick group or an IDC group, never both. To monitor both group types, deploy separate stacks. |
| PermissionProfileName | Name of the Quick custom permissions profile to apply to members of this group. This profile must already exist in your Quick account before deployment. |
| QuickNamespace | Quick namespace for user management. |
| LambdaFunctionPrefixName | Prefix used for the Lambda function name. |

If you prefer to deploy manually, follow these steps:

#### Step 1: Create the IAM role for Lambda

Your Lambda function needs permission to interact with Quick.

1. Go to the
   **IAM Console**
   →
   **Policies**
   →
   **Create policy**
   .
2. Switch to the
   **JSON**
   tab and paste this policy:
   1. **Note**
      : the permissions to IdentityStore are only needed if your Quick account is integrated with IAM Identity Center.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogGroup",
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Resource": "arn:aws:logs:*:YOUR_ACCOUNT_ID:log-group:/aws/lambda/Auto-Assign-QS-Permissions:*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "quicksight:UpdateUserCustomPermission",
                   "quicksight:DeleteUserCustomPermission",
                   "quicksight:UpdateUser",
                   "quicksight:DescribeUser"
               ],
               "Resource": "arn:aws:quicksight:*:*:user/*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "identitystore:DescribeUser",
                   "identitystore:DescribeGroup"
               ],
               "Resource": "*"
           }
       ]
   }
   ```
3. Name the policy
   `Quick-Lambda-Policy`
   and choose
   **Create policy**
   .
4. Navigate to
   **Roles**
   →
   **Create role**
   .
5. Select
   **AWS Service**
   and choose
   **Lambda**
   .
6. Choose
   **Next**
   .
7. Search for and select the
   `Quick-Lambda-Policy`
   .
8. Choose
   **Next**
   .
9. Name the Role
   `Quick-Auto-Permissions-Role`
   and select
   **Create role**
   .

#### Step 2: Deploy the Lambda function

1. Go to the
   **Lambda Console**
   →
   **Create function**
   .
2. **Function name:**
   `Auto-Assign-QS-Permissions`
   .
3. **Runtime:**
   Python 3.14 (or latest available).
4. **Execution role:**
   Use another role → Select
   `Quick-Auto-Permissions-Role`
   .
5. Choose
   **Create function**
   .
6. Under
   **Configuration**
   →
   **General configuration**
   , increase the timeout to 30 seconds.
   1. This should be sufficient for single-event processing. If you observe timeouts in Amazon CloudWatch Logs, increase this value accordingly.
7. Set the following environment variables under
   **Configuration**
   →
   **Environment Variables:**
   .

|  |  |
| --- | --- |
| **Variable Name** | **Description** |
| PERMISSION\_PROFILE | Exact name of the custom permissions profile created in Quick to apply |
| TARGET\_GROUP\_NAME | Name of the group to monitor (Quick group name or IDC group DisplayName) |
| NAMESPACE | Quick namespace (typically “default”) |

8. Navigate back to the
   **Code Source**
   editor and paste the following code:

   ```
   import logging
   import os
   import time
   import boto3

   logger = logging.getLogger()
   logger.setLevel(logging.INFO)

   quicksight = boto3.client("quicksight")
   identity_store = boto3.client("identitystore")

   def lambda_handler(event, context):
       detail = event.get("detail", {})
       event_source = detail.get("eventSource", "")
       event_name = detail.get("eventName", "")
       permission_profile = os.environ["PERMISSION_PROFILE"]
       target_group = os.environ["TARGET_GROUP_NAME"]
       namespace = os.environ["NAMESPACE"]

       account_id = (
           detail.get("userIdentity", {}).get("accountId")
           or detail.get("recipientAccountId")
       )

       logger.info(
           "Event received: source=%s, name=%s", event_source, event_name
       )

       try:
           if event_source == "sso-directory.amazonaws.com":
               return handle_idc_event(detail, account_id, namespace, permission_profile, target_group)
           elif event_source == "quicksight.amazonaws.com":
               return handle_quicksight_event(detail, account_id, namespace, permission_profile, target_group)
           else:
               logger.warning("Unknown event source: %s", event_source)
               return {"statusCode": 200, "body": "Unknown event source"}
       except Exception as e:
           logger.error("Error processing event: %s", str(e))
           return {"statusCode": 500, "body": str(e)}

   def handle_idc_event(detail, account_id, namespace, permission_profile, target_group):
       """Handle AddMemberToGroup or RemoveMemberFromGroup from sso-directory.amazonaws.com."""
       request_params = detail.get("requestParameters") or {}
       identity_store_id = request_params.get("identityStoreId")
       group_id = request_params.get("groupId")
       # AddMemberToGroup nests memberId under "member"; RemoveMemberFromGroup puts it at top level
       member_id = (request_params.get("memberId")
           or (request_params.get("member") or {}).get("memberId"))

       if not identity_store_id or not group_id or not member_id:
           logger.warning("Missing identityStoreId, groupId, or memberId.")
           return {"statusCode": 200, "body": "Missing IDC event info"}

       # Resolve group name from group ID
       group_resp = identity_store.describe_group(
           IdentityStoreId=identity_store_id,
           GroupId=group_id,
       )
       group_name = group_resp.get("DisplayName", "")
       logger.info("IDC group resolved: '%s' (ID: %s)", group_name, group_id)

       if group_name != target_group:
           logger.info(
               "Group '%s' does not match target '%s'. Skipping.",
               group_name,
               target_group,
           )
           return {"statusCode": 200, "body": f"Group {group_name} not targeted"}

       # Resolve user name from member ID
       idc_user = identity_store.describe_user(
           IdentityStoreId=identity_store_id,
           UserId=member_id,
       )
       user_name = idc_user.get("UserName")
       if not user_name:
           logger.warning("No UserName found for IDC user %s", member_id)
           return {"statusCode": 200, "body": "No UserName in IDC"}

       logger.info("IDC user resolved: %s (ID: %s)", user_name, member_id)

       # Wait for Quick to sync the user
       qs_user = None
       for attempt in range(5):
           try:
               qs_user = quicksight.describe_user(
                   AwsAccountId=account_id,
                   Namespace=namespace,
                   UserName=user_name,
               )
               break
           except quicksight.exceptions.ResourceNotFoundException:
               logger.info(
                   "User '%s' not yet in Quick (attempt %d/5). Waiting...",
                   user_name,
                   attempt + 1,
               )
               time.sleep(3)

       if qs_user is None:
           logger.warning(
               "User '%s' not found in Quick after retries.",
               user_name,
           )
           return {"statusCode": 200, "body": f"User {user_name} not in Quick"}

       event_name = detail.get("eventName", "")
       if event_name == "RemoveMemberFromGroup":
           return remove_permissions(account_id, namespace, user_name)
       else:
           return apply_permissions(account_id, namespace, user_name, permission_profile)

   def handle_quicksight_event(detail, account_id, namespace, permission_profile, target_group):
       """Handle CreateGroupMembership or DeleteGroupMembership from quicksight.amazonaws.com."""
       request_params = detail.get("requestParameters") or {}
       group_name = request_params.get("groupName", "")
       member_name = request_params.get("memberName", "")

       if not group_name or not member_name:
           logger.warning("Missing groupName or memberName in event.")
           return {"statusCode": 200, "body": "Missing event info"}

       event_name = detail.get("eventName", "")
       action = "removed from" if event_name == "DeleteGroupMembership" else "added to"
       logger.info(
           "Quick group membership: user '%s' %s '%s'",
           member_name,
           action,
           group_name,
       )

       if group_name != target_group:
           logger.info(
               "Group '%s' does not match target '%s'. Skipping.",
               group_name,
               target_group,
           )
           return {"statusCode": 200, "body": f"Group {group_name} not targeted"}

       if event_name == "DeleteGroupMembership":
           return remove_permissions(account_id, namespace, member_name)
       else:
           return apply_permissions(account_id, namespace, member_name, permission_profile)

   def apply_permissions(account_id, namespace, user_name, permission_profile):
       """Apply the custom permission profile to a Quick user."""
       quicksight.update_user_custom_permission(
           AwsAccountId=account_id,
           Namespace=namespace,
           UserName=user_name,
           CustomPermissionsName=permission_profile,
       )
       logger.info(
           "Permission profile '%s' applied to user '%s'.",
           permission_profile,
           user_name,
       )
       return {
           "statusCode": 200,
           "body": f"Permission applied for user: {user_name}",
       }

   def remove_permissions(account_id, namespace, user_name):
       """Remove custom permissions, reverting user to account/role-level default."""
       try:
           quicksight.delete_user_custom_permission(
               AwsAccountId=account_id,
               Namespace=namespace,
               UserName=user_name,
           )
           logger.info("Permission removed for user '%s'.", user_name)
           return {
               "statusCode": 200,
               "body": f"Permission removed for user: {user_name}",
           }
       except quicksight.exceptions.ResourceNotFoundException:
           logger.info("User '%s' had no custom permission to remove.", user_name)
           return {"statusCode": 200, "body": f"No permission to remove for: {user_name}"}
   ```
9. Choose
   **Deploy**
   .

#### Step 3: Create the Amazon EventBridge rule

Now we must configure this function so that it runs only when a user is successfully added to a group.

1. Go to the
   **Amazon EventBridge Console**
   .
2. Select
   **Rules**
   →
   **Create rule**
   .
3. Opt out of the
   **Visual rule builder**
   .
4. Under
   **Name**
   enter
   `Quick-Group-Membership-Creation-Rule`
   and choose
   **Next**
   .
5. Select
   **Other**
   under
   **Event source**
   .
6. Paste the following into the JSON editor for
   **Event pattern:**
   .When the Quick account is integrated with IDC, the source of this event will be the IDC identity store whereas the source will be Quick otherwise. Therefore, the Amazon EventBridge rule we will create will depend on the account authentication mechanism:
   **Option A: IAM Identity Center**

   ```
   {
       "source": ["aws.sso-directory"],
       "detail-type": ["AWS API Call via CloudTrail"],
       "detail": {
           "eventSource": ["sso-directory.amazonaws.com"],
           "eventName": ["AddMemberToGroup", "RemoveMemberFromGroup"],
           "errorCode": [{ "exists": false }]
       }
   }
   ```

   **Option B: Other Authentication (using Quick Groups)**

   ```
   {
       "source": ["aws.quicksight"],
       "detail-type": ["AWS API Call via CloudTrail"],
       "detail": {
           "eventSource": ["quicksight.amazonaws.com"],
           "eventName": ["CreateGroupMembership", "DeleteGroupMembership"],
           "errorCode": [{ "exists": false }]
       }
   }
   ```
7. Select
   **AWS Service**
   as the
   **Target type**
   .
8. Select
   **Lambda function**
   as the target and choose
   `Auto-Assign-QS-Permissions`
   (the function you built in Step 2).
9. Choose
   **Next**
   and
   **Create rule**
   .

#### Step 4: Add the Amazon EventBridge trigger

1. Return to the
   `Auto-Assign-QS-Permissions`
   Lambda function.
2. Navigate to
   **Configuration**
   →
   **Triggers → Add trigger**
   .
3. Select
   **Amazon EventBridge**
   as the source.
4. Choose
   **Existing rules**
   and select the
   `Quick-Group-Membership-Creation-Rule`
   created in Step 3.
5. Choose
   **Add**
   .

#### Step 5: Verify the setup

To test this, add a user to a Group in Quick or IDC:

1. **Test:**
   Manually add a new or existing user to the target Group.
2. **Monitor:**
   Go to the CloudWatch Logs for your Lambda function.
3. **Confirm:**
   You should see a log entry like: Permission profile ‘123’ applied to user ‘XYZ’.
4. **Result:**
   When that user logs in, they will be restricted by the profile.

### Design considerations

**Group removal:**
This solution for Scenario 3 already handles removal events. When a user is removed from the target group, the Lambda calls
`DeleteUserCustomPermission`
, reverting them to the account or role-level default from Scenario 2. No additional configuration is needed.

**Multi-group membership:**
Quick supports only one custom permissions profile per user at a time. If your organization assigns users to multiple groups with different profiles, you can extend the Lambda logic to list all groups the user belongs to, look up the profile mapped to each group, and apply the highest-priority profile (for example, the most restrictive profile). This multi-group conflict resolution isn’t included in the provided solution and must be implemented by your team based on your organization’s specific priority rules.

## Scenario 4: Batch update for existing group members

You likely have existing groups (for example, “Finance-Readers” or “Marketing-Authors”) containing users who need specific restrictions applied retroactively. Because these users were created in the past, the Amazon EventBridge automation (Scenario 3) won’t catch them.

To fix this, we use a Python script to iterate through a specific
**Quick Group**
and apply the custom permission profile to every member.

Quick groups can contain thousands of users. The API
`ListGroupMemberships`
only returns
**100 members at a time**
. If you write a script without pagination logic, it will stop after the first 100 users, leaving the rest unsecured. The following script handles this automatically using
`NextToken`
.

Copy the following code. You only need to edit the
**Configuration Section**
at the top.

```
import boto3
import sys
import time
import csv
from botocore.exceptions import ClientError

# =========================================================
# CONFIGURATION - Edit these values before running
# =========================================================

# 1. Your AWS Account ID
AWS_ACCOUNT_ID = '279938032093'

# 2. The Quick Group whose members you want to target
# (e.g., 'finance-users', 'marketing-group')
TARGET_GROUP_NAME = 'BlogTestGroup'

# 3. The name of the Custom Permission Profile you want to apply
# (Must already exist in Quick)
PERMISSION_PROFILE_NAME = 'TestBlog'

# 4. Namespace (almost always 'default')
NAMESPACE = 'default'

# =========================================================

# Initialize the Quick client
qs = boto3.client('quicksight')

def get_all_group_members(group_name):
    """
    Generator function that yields members one by one,
    handling pagination automatically.
    """
    print(f"Fetching members from group: '{group_name}'...")
    next_token = None
    while True:
        try:
            # Construct the API call arguments
            api_args = {
                'AwsAccountId': AWS_ACCOUNT_ID,
                'Namespace': NAMESPACE,
                'GroupName': group_name,
                'MaxResults': 100
            }
            if next_token:
                api_args['NextToken'] = next_token

            # Call API
            response = qs.list_group_memberships(**api_args)

            # Yield members from the current page
            for member in response.get('GroupMemberList', []):
                # We only need the MemberName (which corresponds to UserName)
                yield member.get('MemberName')

            # Check if there are more pages
            next_token = response.get('NextToken')
            if not next_token:
                break

        except qs.exceptions.ResourceNotFoundException:
            print(f"ERROR: The group '{group_name}' does not exist.")
            sys.exit(1)
        except ClientError as e:
            print(f"CRITICAL API ERROR: {e}")
            sys.exit(1)

def apply_permission(user_name):
    """
    Applies the custom permission profile to a single user.
    """
    try:
        qs.update_user_custom_permission(
            AwsAccountId=AWS_ACCOUNT_ID,
            UserName=user_name,
            Namespace=NAMESPACE,
            CustomPermissionsName=PERMISSION_PROFILE_NAME
        )
        return True, "Success"
    except qs.exceptions.ResourceNotFoundException as e:
        error_msg = str(e)
        if 'User' in error_msg or 'user' in error_msg:
            return False, "User not found (might have been deleted)"
        else:
            return False, f"Profile '{PERMISSION_PROFILE_NAME}' not found"
    except ClientError as e:
        return False, str(e)

def main():
    print("--------------------------------------------")
    print(f"STARTING BATCH UPDATE")
    print(f"Target Group: {TARGET_GROUP_NAME}")
    print(f"Applying Profile: {PERMISSION_PROFILE_NAME}")
    print("--------------------------------------------\n")

    success_count = 0
    fail_count = 0
    failed_users = []

    # Iterate through the generator
    for user_name in get_all_group_members(TARGET_GROUP_NAME):
        print(f"Processing: {user_name}...", end=" ")
        status, message = apply_permission(user_name)

        if status:
            print("OK")
            success_count += 1
        else:
            print(f"FAILED ({message})")
            fail_count += 1
            failed_users.append({'UserName': user_name, 'Error': message})

        # Rate Limiting: Sleep briefly to avoid hitting API limits
        time.sleep(0.1)

    print("\n--------------------------------------------")
    print("JOB COMPLETED")
    print(f"Total Success: {success_count}")
    print(f"Total Failed: {fail_count}")
    print("--------------------------------------------")

    # Export failed users to CSV for review/retry
    if failed_users:
        csv_filename = f"failed_users_{TARGET_GROUP_NAME}.csv"
        with open(csv_filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['UserName', 'Error'])
            writer.writeheader()
            writer.writerows(failed_users)
        print(f"\nFailed users written to: {csv_filename}")

if __name__ == "__main__":
    main()
```

**Note:**
The default delay of 0.1 seconds between API calls (~10 requests/second) is suitable for most deployments. For large-scale groups (over 10,000 members), increase
`API_DELAY_SECONDS`
to avoid API throttling. Monitor for ThrottlingException errors in the output and adjust as needed for your environment.

### Detailed execution steps

1. **Prepare your environment**
   .You can run this locally or in
   **AWS CloudShell**
   directly in your browser, which comes pre-authenticated and has Boto3 installed.
   * Sign in to the AWS Management Console.
   * Choose the
     **CloudShell**
     icon (terminal icon) in the top navigation bar.
2. **Create the script file**
   .In the CloudShell terminal, enter the following command to open a text editor:
   `nano update_permissions.py`
   * Paste the preceding Python code into the editor.
   * Edit the
     `AWS_ACCOUNT_ID`
     and
     `TARGET_GROUP_NAME`
     variables at the top of the file to match your environment.
   * Press Ctrl+X, then Y, then Enter to save and exit.
3. **Run the script**
   .Execute the script with Python:
   `python3 update_permissions.py`
4. **Verify results**
   .
   * The script will print “OK” next to every user it successfully updates.
   * If any users fail, the script writes a
     `failed_users_{GROUP_NAME}.csv`
     file with the username and failure reason for each. Review this file to identify users that need manual follow-up.
   * If you see “Profile not found,” double-check that you created the Custom Permission Profile in the Amazon Quick console exactly as spelled in the script.
   * Run
     `aws quicksight describe-user --aws-account-id &lt;ACCOUNT_ID&gt; --namespace &lt;NAMESPACE&gt; --user-name &lt;USERNAME&gt;`
     and confirm that the
     `CustomPermissionsName`
     field in the response matches your expected profile.

## Clean up

If you deployed using the CloudFormation template, delete the stack to remove all resources it created, including the Amazon EventBridge rule, Lambda function, and associated IAM role and policy.

If you deployed manually, delete the following resources:

* The Amazon EventBridge rule (
  `Quick-Group-Membership-Creation-Rule`
  ).
* The Lambda function (
  `Auto-Assign-QS-Permissions`
  ).
* The IAM role (
  `Quick-Auto-Permissions-Role`
  ) and policy (
  `Quick-Lambda-Policy`
  ).

The batch update script (Scenario 4) does not deploy any infrastructure and requires no clean up.

## Conclusion

Automating custom permissions in Amazon Quick is a foundational step toward a secure, scalable user governance strategy. As your Quick environment grows, the patterns in this post help verify that authentication and authorization scale together, not independently.

The following table summarizes the four scenarios and when to apply each:

|  |  |  |
| --- | --- | --- |
| **Scenario** | **Trigger** | **Best For** |
| 1. Pre-registered users | `RegisterUser` API call | Organizations with custom onboarding portals |
| 2. Account/role defaults | Native API, always on | Consistent restrictions across all users or by role |
| 3. Event-driven group logic | Group membership added | Custom permissions logic like profiles per group; IDC or Quick groups |
| 4. Retroactive batch | Manual script execution | Existing users provisioned before automation was in place |

One manual step remains in the Scenario 3 flow: an administrator must add each user to the appropriate group before the event-driven pipeline fires. You can remove this step entirely by extending the same Amazon EventBridge + Lambda architecture to listen for new user creation events.

When new users are provisioned through Just-In-Time federation, CloudTrail captures a
`CreateUser`
event (when Quick users are invited by admins, this produces a
`BatchCreateUser`
event). A Lambda function can intercept that event and apply custom logic to determine the correct group based on email domain, internal user mapping, or any available user attribute. It then calls
`CreateGroupMembership`
to assign the user to that group automatically.

Combined with Scenario 3, this approach can create a fully automated pipeline with no manual steps. A full implementation of this extension is beyond the scope of this post. However, the building blocks (CloudTrail event capture, Amazon EventBridge filtering, and Lambda-based Quick API calls) are identical to those described in Scenario 3.

Start with Scenario 2 to establish your baseline today. For more details, see
[Amazon Quick Custom Permissions](https://docs.aws.amazon.com/quick/latest/userguide/custom-permissions.html)
in the Amazon Quick User Guide.

---

## About the authors

### Leona Li

Leona is a Specialist Solutions Architect for Amazon Quick Suite. She focuses on enabling data intelligence and helping enterprise customers become more data-driven by designing, building, and modernizing their solutions in the cloud.

### Ashok Dasineni

Ashok is a Solutions Architect for Amazon Quick Suite. Before joining AWS, Ashok worked with clients and organizations in the banking and financial domain, focusing on fraud research and prevention. He designed and implemented innovative solutions to improve business process, reduce cost, and increase revenue, helping companies around the world achieve their highest potential through data.

### Srikanth Baheti

Srikanth is a Senior Manager for Amazon QuickSight. He started his career as a consultant and worked for multiple private and government organizations. Later he worked for PerkinElmer Health and Sciences &amp; eResearch Technology Inc, where he was responsible for designing and developing high traffic web applications and highly scalable and maintainable data pipelines for reporting platforms using AWS services and serverless computing.

### Jackson Dowden

Jackson is a Gen AI Solutions Architect for Amazon Quick. He began at AWS as a Partner Solutions Architect and now focuses on helping ISV and healthcare &amp; life sciences customers implement AI-driven analytics and embedded insights with Amazon Quick.