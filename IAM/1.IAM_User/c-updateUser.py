import boto3 

iam_client = boto3.client('iam')

def updateUser(oldUserName, newUserName):
    try: 
        response = iam_client.update_user(
            UserName = oldUserName,
            NewUserName = newUserName
        )
        return response
    
    except iam_client.exceptions.EntityAlreadyExistsException:
        print("Tên người dùng này đã tồn tại!")
        
    except Exception as e:
        print("Đã xảy ra lỗi! =>", e)

if __name__ == "__main__":
    oldUserName = input("Enter the old username: ")
    newUserName = input("Enter the new username: ")

    result = updateUser(oldUserName, newUserName)
    print(result)
