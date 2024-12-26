import boto3
import botocore

client = boto3.client('sns')

def listTopicSubscriptions():
    try:
        response = client.list_subscriptions()
        for subscription in response['Subscriptions']:
            print(f"Subscription ARN: {subscription['SubscriptionArn']}")

    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])

if __name__ == "__main__":
    listTopicSubscriptions()
