import boto3

iam_client = boto3.client('iam')

def deleteUser(username):
    try:
        response = iam_client.delete_user(
            UserName=username
        )
        return response
    except Exception as e:
        print("Đã xảy ra lỗi! =>", e)

if __name__ == "__main__":
    username = input("Enter the UserName: ").strip()
    if deleteUser(username):
        print("Xóa người dùng thành công!!!")
