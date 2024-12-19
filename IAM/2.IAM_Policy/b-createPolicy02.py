import boto3

iam_client = boto3.client('iam')

def readFile():
    jsonfilename = input("Enter the Json File: ") + ".json"
    #print(jsonfilename)
    with open(jsonfilename, "r") as file:
        content = file.read()
    return content

def createPolicy(policy_name, policy_document):
    try:
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document,
            Description='demo my custom policy',
        )
        return response
    
    except iam_client.exceptions.EntityAlreadyExistsException:
        print("Policy Name Already Exists")
    
    except Exception as e:
        print("ERROR! => ", e)

if __name__ == "__main__":
    readJsonFile = readFile()
    policy_name = input("Policy Name: ")
    if createPolicy(policy_name, readJsonFile):
        print(f"Policy {policy_name} was create successfully!")
