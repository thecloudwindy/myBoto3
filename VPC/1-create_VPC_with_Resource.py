import boto3

ec2_resource = boto3.resource('ec2')
def create_vpc(vpc_name, vpc_cidr):
    try:
        vpc = ec2_resource.create_vpc(
            CidrBlock=vpc_cidr,
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
        print(f"VPC Name {vpc_name} mang dải VPC CIDR: {vpc_cidr} đã được tạo thành công! với ID: {vpc.id}")
    except Exception as e:
        print("Đã xảy ra lỗi! => ", e)

if __name__ == "__main__":
    try:
        vpc_name = input("VPC Name: ")
        vpc_cidr = input("CIDR block: ")
        create_vpc(vpc_name, vpc_cidr)
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")


