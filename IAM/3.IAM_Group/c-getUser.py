import boto3
from botocore.exceptions import ClientError

iam_client = boto3.client('iam')

def getUser(username):
    try:
        response = iam_client.get_user(
            UserName=username
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            print(f"User {username} khong duoc tim thay.")
        else:
            print(f"Da xay ra loi: {e}")
        return None

if __name__ == "__main__":
    user_name = input("Enter the User Name: ")
    if getUser(user_name):
        print("This User exist!")
