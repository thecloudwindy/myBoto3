import boto3

client = boto3.client('iam')

def listRoles():
    response = client.list_roles()
    return response

if __name__ == "__main__":
    result = listRoles()
    for role in result['Roles']:
        print(role['RoleName'])

