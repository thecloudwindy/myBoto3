import time
import boto3 
import botocore 

def iam_client():
    client = boto3.client('iam')
    return client

# Hàm này liệt kê các Custom Policies
def listCustomerPolicies():
    responseListCustomerPolicies = iam_client().list_policies(
        Scope = "Local",        
    )
    return responseListCustomerPolicies

# Hàm này để xóa các Custom Policies
def deletePolicy(arn):
    responseDeletePolicy = iam_client().delete_policy(
        PolicyArn=arn
    )
    return responseDeletePolicy

# Hàm có chức năng chuyển từ kiểu Dict sang List
def dictToList():
    # Liệt kê các ARN của Policies sau đó ghi chúng vào file myArn
    result = listCustomerPolicies()
    for name in result['Policies']:
        with open("myArn", "+a") as file:
            file.write(name["Arn"] + "\n")
    
    time.sleep(5)

    # Đọc file arn và chuyển chúng sang dạng list
    with open("myArn", 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    return lines

if __name__ == "__main__":
    result = dictToList()
    #print(result)
    for arn in result:
        #while(True):
        #arn = input("Arn of Policy: ")
        try:
            print(deletePolicy(arn))
        except botocore.exceptions.ClientError as error:
            # Nếu Policy nào đang được sử dụng hay được gán vào thực thể (như user, group, role) thì ghi vào file riêng
            if error.response['Error']['Code'] == 'DeleteConflict':
                with open("cannotDeleteArn1",'+a') as file:
                    file.write(arn + "\n")
                    continue
            # Hoặc nếu xóa Policy nào mà gặp lỗi khác lỗi ở trên cũng ghi ra một file riêng
            else:
                with open("cannotDeleteArn2",'+a') as file:
                    file.write(arn + "\n")
                    continue

                