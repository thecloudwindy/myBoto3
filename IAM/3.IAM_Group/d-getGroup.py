import boto3
from botocore.exceptions import ClientError

iam_client = boto3.client('iam')

def getGroup(groupname):
    try:
        response = iam_client.get_group(
            GroupName=groupname,
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            print(f"Group {groupname} khong duoc tim thay.")
        else:
            print(f"Da xay ra loi: {e}")
        return None
    
if __name__ == "__main__":
    groupname = input("Enter the Group Name: ")
    if getGroup(groupname):
        print("This Group already exist!")
