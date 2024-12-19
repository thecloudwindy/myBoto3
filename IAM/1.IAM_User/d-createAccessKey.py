import boto3

iam_client = boto3.client('iam')

def createAccessKey(userName):
    try:
        response = iam_client.create_access_key(UserName=userName)
        return response

    except iam_client.exceptions.NoSuchEntityException:
        print("Username không tồn tại!")
        return None

    except Exception as e:
        print("Đã xảy ra lỗi! => ", e)
        return None

if __name__ == "__main__":
    userName = input("Enter the username: ").strip()
    result = createAccessKey(userName)

    if result:
        access_key = result['AccessKey']
        print(f"Username: {access_key['UserName']}")
        print(f"Access Key ID: {access_key['AccessKeyId']}")
        print(f"Secret Access Key: {access_key['SecretAccessKey']}")
    else:
        print("Không thể tạo Access Key.")
