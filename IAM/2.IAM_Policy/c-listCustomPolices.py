import boto3

iam_client = boto3.client('iam')

def listCustomPolicies():
    response = iam_client.list_policies(
        Scope= 'Local', #'All'|'AWS'|'Local'
        OnlyAttached=False, #True|False
    )
    return response

if __name__ == "__main__":
    result = listCustomPolicies()
    i  = 1
    for name in result['Policies']:
        print(i,'-',"Policy Name: ", name["PolicyName"], "\n", "ARN: ",name["Arn"])
        i += 1
