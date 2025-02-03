import boto3

client = boto3.client('sns')

def delete_SNS_Topic(topic_arn):
    try:
        # Kiểm tra xem topic có tồn tại không
        topics = client.list_topics()['Topics']
        topic_exists = any(topic['TopicArn'] == topic_arn for topic in topics)
        
        if not topic_exists:
            raise ValueError(f"Topic with ARN '{topic_arn}' does not exist.")
        
        # Nếu topic tồn tại, thực hiện xóa
        response = client.delete_topic(
            TopicArn=topic_arn
        )
        return response
    
    except Exception as e:
        print("Error => ", e)
        return None

if __name__ == "__main__":
    topic_arn = input("Topic ARN: ")
    result = delete_SNS_Topic(topic_arn)
    if result:
        print("Topic deleted successfully.")
    else:
        print("Failed to delete topic.")
