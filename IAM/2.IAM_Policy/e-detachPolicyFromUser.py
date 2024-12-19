import boto3
from botocore.exceptions import ClientError

iam_client = boto3.client('iam')

def detachPolicyToUser(username, policy_arn):
    try:
        response = iam_client.detach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            print(f"User policy {policy_arn} khong duoc tim thay.")
        else:
            print(f"Da xay ra loi: {e}")
        return None

if __name__ == "__main__":
    username = input("Nhap vao Username: ").strip()
    policy_arn = input("Nhap vao Policy ARN: ").strip()
    if detachPolicyToUser(username, policy_arn):
        print("Go bo policy ra khoi user thanh cong!")
    else:
        print("Go bo Policy that bai!")
