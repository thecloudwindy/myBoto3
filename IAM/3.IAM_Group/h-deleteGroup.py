import boto3

iam_client = boto3.client('iam')

def deleteGroup(group_name):
    try:
        response = iam_client.delete_group(
            GroupName=group_name
        )
        return response
    except Exception as e:
        print("Error! => ", e)

if __name__ == "__main__":
    group_name = input("Group name: ")
    if deleteGroup(group_name):
        print(f"Xoa group {group_name} thanh cong!")
