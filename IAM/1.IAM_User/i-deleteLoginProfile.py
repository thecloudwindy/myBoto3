import boto3

iam_client = boto3.client('iam')

def deleteLoginProfile(username):
    try:
        response = iam_client.delete_login_profile(
            UserName=username,
        )

        return response
    
    except iam_client.exceptions.NoSuchEntityException:
        print("User không tồn tại!!!")

    except Exception as e:
        print("Đã xảy ra lỗi! => ", e)

if __name__ == "__main__":
    username = input("Enter the Username: ")
    if deleteLoginProfile(username):
        print("Delete Login Profile Successful!")
