import boto3
import json

iam_client = boto3.client('iam')

def policy_document():
    document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt1734566237374",
                "Action": "s3:*",
                "Effect": "Allow",
                "Resource": "*"
            }
        ]
    }
    return document

def createPolicy(policy_name, policy_document):
    try:
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document,
            Description='demo my custom policy 01',
        )
        return response
    
    except iam_client.exceptions.EntityAlreadyExistsException:
        print("Policy Name Already Exists")
    
    except Exception as e:
        print("Đã xảy ra lỗi! => ", e)

if __name__ == "__main__":
    policy_name = input("Policy Name: ")
    policy_document = json.dumps(policy_document())
    if createPolicy(policy_name, policy_document):
        print(f"Policy {policy_name} được tạo thành công!")



