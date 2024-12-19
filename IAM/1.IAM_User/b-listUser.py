import boto3

iam_client = boto3.client('iam')

def list_users():
    try:
        response = iam_client.list_users()
        for user in response['Users']:
            print("Username: ", user['UserName'], ' - ', "ARN: ", user['Arn'])
    except iam_client.exceptions.ServiceFailureException:
        print("Dịch vụ đang bị lỗi, bạn thử lại sau nhé!")
if __name__ == "__main__":
    list_users()
