import boto3

iam_client = boto3.client('iam')

def list_users():
    response = iam_client.list_users()
    for user in response['Users']:
        print("Username: ", user['UserName'], '-', "ARN: ", user['Arn'] )
if __name__ == "__main__":
    list_users()
