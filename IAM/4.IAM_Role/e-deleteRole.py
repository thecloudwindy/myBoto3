import boto3
import pprint

iam_client = boto3.client('iam')

def deleteRole():
    response = iam_client.delete_role(
        RoleName=input("Role Name: ")
    )
    pprint.pprint(response)

deleteRole()
