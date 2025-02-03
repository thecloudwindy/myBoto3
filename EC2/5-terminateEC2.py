import boto3
import time

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

def listInstances():
    print(list(ec2.instances.all()))

def checkInstanceStatus():
    listInstancesID_toCheckStatus = []
    while True:
        instanceID = input("Instance ID muốn kiểm tra trạng thái: ")
        listInstancesID_toCheckStatus.append(instanceID)
        if input("Bạn có muốn nhập Instance ID để kiểm tra trạng thái nữa không? (Y|N): ").strip().upper() == 'N':
            break

    try:
        response = client.describe_instances(
            InstanceIds=listInstancesID_toCheckStatus
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                print(f"{instance_id} => {state}")
    except Exception as e:
        print(f"Đã xảy ra lỗi => {e}")

def terminateInstances():
    listTerminateInstancesID=[]
    while True:
        instanceID = input("Instance ID muốn Stop: ")
        listTerminateInstancesID.append(instanceID)
        if input("Bạn có muốn nhập Instance ID để Terminate nữa không? (Y|N): ").strip().upper() == 'N':
            break
    try:
        response = client.terminate_instances(
            InstanceIds=listTerminateInstancesID
        )
        for instance in response['TerminatingInstances']:
            print(f"{instance['InstanceId']} => {instance['CurrentState']['Name']}")
    except Exception as e:
        print(f"Đã xảy ra lỗi => {e}")

if __name__ == "__main__":
    listInstances()
    checkInstanceStatus()
    time.sleep(3)
    terminateInstances()

