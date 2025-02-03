import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-01816d07b1128cd2d',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=2,
    SecurityGroups=[
        'default'
    ],
    KeyName='demoKeyPair'
)

print(list(ec2.instances.all()))
