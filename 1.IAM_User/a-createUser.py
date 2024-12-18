import boto3

iam_client = boto3.client('iam')

def create_user(username):
    try:
        response = iam_client.create_user(UserName = username)
        print("Người dùng đã được tạo thành công: ", response)
    except iam_client.exceptions.EntityAlreadyExistsException:
        print("Người dùng này đã tồn tại!")
    except Exception as e:
        print("Đã xảy ra lỗi!", e)

if __name__ == "__main__":
    username = input("Nhập tên người dùng: ")
    create_user(username)
