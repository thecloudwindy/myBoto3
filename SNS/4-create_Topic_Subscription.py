import boto3
import botocore
import botocore.exceptions

client = boto3.client('sns')

def create_subscriptions(topic_arn, protocol, endpoint):
    try:
        response = client.subscribe(
            TopicArn=topic_arn,
            Protocol=protocol,
            Endpoint=endpoint,
        )
        return response
    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])
    except botocore.exceptions.ParamValidationError as error:
        print(error)
        

if __name__ == "__main__":
    try:
        topic_arn = input("Topic ARN: ")
        protocol = input("Protocol: ")
        endpoint = input("Endpoint: ")

        create_subscriptions(topic_arn, protocol, endpoint)
    
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")
