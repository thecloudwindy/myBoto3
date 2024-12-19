import boto3

iam_client = boto3.client('iam')

def createGroup(groupname):
    try:
        response = iam_client.create_group(
            GroupName=groupname
        )
        return response 
    except Exception as e:
        print("Error => ", e)

if __name__ == "__main__":
    groupname = input("Nhập tên Group: ")
    if createGroup(groupname):
        print(f"Tạo {groupname} thành công!")
