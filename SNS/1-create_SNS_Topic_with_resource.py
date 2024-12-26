import boto3
import botocore
import botocore.exceptions

sns = boto3.resource('sns')

def create_sns_topic(topic_name, display_name, key, value ):
    try:
        topic = sns.create_topic(
            Name=topic_name,
            Attributes={
                'DisplayName': display_name
            },
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ],
        )
        print(f"SNS Topic has just been created: {topic.arn}")
    except botocore.exceptions.ClientError as error:
        print(error.response["Error"]["Message"])
    except botocore.exceptions.ParamValidationError as error:
        print(error)

if __name__ == "__main__":
    try:
        topic_name = input("Topic Name: ")
        display_name = input("Display Name: ")
        tag_key = input("Tag Key: ")
        tag_value = input("Tag Value: ")

        create_sns_topic(topic_name, display_name, tag_key, tag_value)
    
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")
