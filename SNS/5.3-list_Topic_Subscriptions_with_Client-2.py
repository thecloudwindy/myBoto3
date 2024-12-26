import boto3
import botocore

client = boto3.client('sns')

def listTopicSubscriptions():
    try:
        next_token = None
        while True:
            if next_token:
                response = client.list_subscriptions(NextToken=next_token)
            else:
                response = client.list_subscriptions()

            # In ra các subscriptions trong trang hiện tại
            for subscription in response['Subscriptions']:
                print(f"Subscription ARN: {subscription['SubscriptionArn']}")

            # Kiểm tra xem có trang kế tiếp hay không
            next_token = response.get('NextToken')
            if not next_token:  # Không còn trang kế tiếp
                break

    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])

if __name__ == "__main__":
    listTopicSubscriptions()
