import boto3

iam_client = boto3.client('iam')

def listGroups():
    try:
        response = iam_client.list_groups()
        return response
    except Exception as e:
        print("Error =>", e)

if __name__ == "__main__":
    result = listGroups()
    i = 1
    for group in result['Groups']:
        print(f"""
                {i}.Group Name: {group['GroupName']}
                Group ID: {group['GroupId']}
                Group Arn: {group['Arn']}""")
        print("+"*20)
        i += 1
