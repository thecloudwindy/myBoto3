import boto3
from botocore.exceptions import ClientError

iam_client = boto3.client('iam')


# Ham kiem tra Username
def getUser(username):
    try:
        response = iam_client.get_user(
            UserName=username
        )
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            print(f"User {username} khong duoc tim thay.")
        else:
            print(f"Da xay ra loi: {e}")
        return None

# Ham kiem tra Groupname
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

# Ham them User vao Group
def addUserToGroup(group_name, user_name):
        try:
            response = iam_client.add_user_to_group(
                GroupName=group_name,
                UserName=user_name
            )
            return response
        except Exception as e:
            print("Error => ",e)

if __name__ == "__main__":
    group_name = input("Enter the Group Name: ").strip()
    flag1 = getGroup(group_name)
    user_name = input("Enter the User Name: ").strip()
    flag2 = getUser(user_name)

    if(flag1 != None) and (flag2 != None):
        result = addUserToGroup(group_name, user_name)
        if result:
            print("Adding Successful!!!")
    else:
        print("Khong the them User vao Group")

    
    
    
            

        



