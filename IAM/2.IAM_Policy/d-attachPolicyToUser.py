import boto3

iam_client = boto3.client('iam')

def attachPolicyToUser(username, arn):
    try:
        response = iam_client.attach_user_policy(
            UserName=username,
            PolicyArn=arn
        )
        return response
    
    except Exception as e:
        print("ERROR! =>", e)

if __name__ == "__main__":
    username = input("Enter the Username: ").strip()
    arn = input("Enter the Arn: ")
    if attachPolicyToUser(username, arn):
        print("Attach successfully!")
        
