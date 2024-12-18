import boto3

iam_client = boto3.client('iam')

def change_password(oldPassword, newPassword):
    try:
        response = iam_client().change_password(
            OldPassword=oldPassword,
            NewPassword=newPassword
        )
        return response
    except iam_client.exceptions.NoSuchEntityException:
        print("User không tồn tại")
    except Exception as e:
        print("Đã xảy ra lỗi! => ", e)



'''
Thay đổi mật khẩu của IAM User đang thực hiện thao tác này. Thao tác này có thể được thực hiện bằng CLI, Amazon Web Services API hoặc ở phần My Security Credentials trong Amazon Web Services Management Console. Mật khẩu người dùng root của tài khoản Amazon Web Services không bị ảnh hưởng bởi thao tác này.
'''


