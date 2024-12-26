import boto3
import botocore

client = boto3.client('sns')

def listTopicSubscriptions():
    try:
        response = client.list_subscriptions()
        while True:
            for subscription in response['Subscriptions']:
                print(f"Subscription ARN: {subscription['SubscriptionArn']}")

            if 'NextToken' in response:
                response = client.list_subscriptions(NextToken=response['NextToken'])
            else:
                break

    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])

if __name__ == "__main__":
    listTopicSubscriptions()
