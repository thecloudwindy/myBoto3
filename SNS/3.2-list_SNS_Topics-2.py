import boto3
import botocore.exceptions

client = boto3.client('sns')

def list_SNS_Topics():
    try:
        response = client.list_topics()
        while True:
            for topic in response['Topics']:
                print(topic['TopicArn'])

            if 'NextToken' in response:
                response = client.list_topics(NextToken=response['NextToken'])
            else:
                break

    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])

if __name__ == "__main__":
    try:
        list_SNS_Topics()
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")
