import boto3

vpc_client = boto3.client('ec2')

def createVPC(cidr_block, vpc_name):
    try:
        response = vpc_client.create_vpc(
            CidrBlock=cidr_block,
            TagSpecifications=[
                {
                    'ResourceType': 'vpc',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': vpc_name
                        },
                    ]
                },
            ],
            InstanceTenancy='default',
            AmazonProvidedIpv6CidrBlock=False
        )
        return response
    
    except Exception as e:
        print("Đã xảy ra lỗi! => ", e)

if __name__ == "__main__":
    try:
        vpc_cidr = input("CIDR block: ")
        vpc_name = input("VPC Name: ")
        result = createVPC(vpc_cidr, vpc_name)
        if result:
            print(f"VPC {vpc_name} kèm dải CIDR {vpc_cidr} đã được tạo thành công với VPC-ID là {result['Vpc']['VpcId']}")
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")

