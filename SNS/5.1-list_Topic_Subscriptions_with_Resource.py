import boto3
import botocore

resource = boto3.resource('sns')

def listTopicSubscriptions():
    try:
        subscriptions_iterator = resource.subscriptions.all()
        for subscription in subscriptions_iterator:
            print(f"Subscription ARN: {subscription.arn}")

    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])

if __name__ == "__main__":
    listTopicSubscriptions()
