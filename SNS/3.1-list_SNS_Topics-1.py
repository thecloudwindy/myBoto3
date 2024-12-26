import boto3
import botocore
import botocore.exceptions

client = boto3.client('sns')

def list_SNS_Topics():
    try:
        response = client.list_topics()
        for topic in response['Topics']:
            print(topic['TopicArn'])
    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])

if __name__ == "__main__":
    try:
        list_SNS_Topics()
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")
