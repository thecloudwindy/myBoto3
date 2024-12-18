import boto3

iam_client = boto3.client('iam')

def createLoginProfile(username, password):
    try:
        response = iam_client.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=False #True|False
        )
        return response
    
    except iam_client.exceptions.EntityAlreadyExistsException:
        print("Login Profile cuả User này đã tồn tại!")

    except iam_client.exceptions.NoSuchEntityException:
        print("User không tồn tại!")

    except iam_client.exceptions.PasswordPolicyViolationException:
        print("Mật khẩu không thỏa điều kiện!")

    except Exception as e:
        print("Đã xảy ra lỗi!", e)

if __name__ == "__main__":
    username = input("Nhập tên người dùng: ")
    password = input("Nhập password: ")
    if createLoginProfile(username, password):
        print("Success!!!")
