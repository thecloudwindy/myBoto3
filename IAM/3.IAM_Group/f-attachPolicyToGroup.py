import boto3

iam_client = boto3.client('iam')

def attachGroupPolicy(group_name, policy_arn):
    try:
        response = iam_client.attach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        return response
    except Exception as e:
        print("ERROR! =>", e)

if __name__ == "__main__":
    group_name = input("Group Name: ")
    policy_arn = input("Policy ARN: ")
    if attachGroupPolicy(group_name, policy_arn):
        print("Success!")

