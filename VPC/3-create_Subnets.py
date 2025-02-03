import boto3
from itertools import cycle
import ipaddress
import botocore
import botocore.exceptions 

# Liệt kê các Availability Zones trong Region hiện tại
def list_AZs(vpc_cidr_block, subnetmask):
    try:
        ec2_client = boto3.client('ec2')
        vpc_mask = int(vpc_cidr_block[-2:])
        max_num_subnets = pow(2, subnetmask - vpc_mask)
        results = ec2_client.describe_availability_zones()
        available_azs = []
        for az in results['AvailabilityZones']:
            available_azs.append(az['ZoneName'])

        azs = []
        count = 0
        for az in cycle(available_azs):
            if count < max_num_subnets:
                azs.append(az)
                count += 1
            else:
                break
        return azs
    
    except botocore.exceptions.ClientError as e:
        return e.response["Error"]["Message"]
    except botocore.exceptions.ParamValidationError as e:
        return e 
    
def create_subnet(vpc_id, subnet_prefix, subnet_mask, num_subnets):
    try:
        ec2_resource = boto3.resource("ec2")
        vpc = ec2_resource.Vpc(vpc_id)
        azs = list_AZs(vpc.cidr_block, subnet_mask)
        ip_addr = ipaddress.ip_network(vpc.cidr_block)
        subnet_cidr_blocks = list(ip_addr.subnets(new_prefix=subnet_mask))

        if num_subnets <= lens(azs):
            for _ in range(num_subnets):
                az = azs.pop(0)
                subnet = vpc.create_subnet(
                    TagSpecifications=[
                        {
                            'ResourceType': 'subnet',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': subnet_prefix + "-" + az
                                },
                            ]
                        },
                    ],
                    AvailabilityZone='string',
                    AvailabilityZoneId='string',
                    CidrBlock='string',
                    Ipv6CidrBlock='string',
                    OutpostArn='string',
                    Ipv6Native=True|False,
                    Ipv4IpamPoolId='string',
                    Ipv4NetmaskLength=123,
                    Ipv6IpamPoolId='string',
                    Ipv6NetmaskLength=123,
                    DryRun=True|False
                )

    except botocore.exceptions.ClientError as e:
        return e.response["Error"]["Message"]
    except botocore.exceptions.ParamValidationError as e:
        return e 
