import boto3

ec2 = boto3.resource('ec2')

print(list(ec2.instances.all()))
