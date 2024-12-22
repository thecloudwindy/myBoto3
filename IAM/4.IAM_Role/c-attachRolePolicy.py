import boto3
import pprint

iam_client = boto3.client('iam')

def attachRolePolicy():
    response = iam_client.attach_role_policy(
        RoleName=input("Role Name: "),
        PolicyArn=input("Policy ARN: ")
    )
    pprint.pprint(response)

attachRolePolicy()
