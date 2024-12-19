import boto3

iam_client = boto3.client('iam')

def deleteAccessKey(userName, accessKeyID):
    try:
        response = iam_client.delete_access_key(
            UserName = userName,
            AccessKeyId=accessKeyID
        )
        return response
    
    except iam_client.exceptions.NoSuchEntityException:
        print(f"Giá trị nhập vào không đúng. Vui lòng kiểm tra lại!")

    except Exception as e:
        print("Đã xảy ra lỗi! =>", e)

if __name__ == "__main__":
    userName = input("Nhập UserName: ").strip()
    accessKeyID = input("Nhập Access Key ID: ").strip()
    if deleteAccessKey(userName, accessKeyID):
        print("Xóa Access Key thành công!")
    
    
