import boto3

iam_client = boto3.client('iam')

def detachGroupPolicy(group_name, policy_arn):
    try:
        response = iam_client.detach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        return response
    except Exception as e:
        print("ERROR! => ", e)

if __name__ == "__main__":
    group_name = input("Group Name: ")
    policy_arn = input("Policy ARN: ")
    if detachGroupPolicy(group_name, policy_arn):
        print("Detach Successfully!")
