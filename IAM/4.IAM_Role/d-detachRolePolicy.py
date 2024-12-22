import boto3
import pprint

iam_client = boto3.client('iam')

def detachRolePolicy():
    response = iam_client.detach_role_policy(
        RoleName=input("Role Name: "),
        PolicyArn=input("Policy ARN: ")
    )
    pprint.pprint(response)

detachRolePolicy()
