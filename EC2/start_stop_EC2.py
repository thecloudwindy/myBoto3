import boto3
import time

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

def listInstances():
    print(list(ec2.instances.all()))

def stopInstances():
    listStopInstancesID=[]
    while True:
        instanceID = input("Instance ID muốn Stop: ")
        listStopInstancesID.append(instanceID)
        if input("Bạn có muốn nhập Instance ID để Stop nữa không? (Y|N): ") == 'N':
            break
    try:
        response = client.stop_instances(
            InstanceIds=listStopInstancesID
        )
        for instance in response['StoppingInstances']:
            print(f"{instance['InstanceId']} => {instance['CurrentState']['Name']}")
    except Exception as e:
        print(f"Đã xảy ra lỗi => {e}")

def startInstances():
    listStartInstancesID=[]
    while True:
        instanceID = input("Instance ID muốn Start: ")
        listStartInstancesID.append(instanceID)
        if input("Bạn có muốn nhập Instance ID để Start nữa không? (Y|N): ").strip().upper() == 'N':
            break
    try:
        response = client.start_instances(
            InstanceIds=listStartInstancesID
        )
        for instance in response['StartingInstances']:
            print(f"{instance['InstanceId']} => {instance['CurrentState']['Name']}")
    except Exception as e:
        print(f"Đã xảy ra lỗi => {e}")

if __name__ == "__main__":
    listInstances()
    time.sleep(3)
    #stopInstances()
    startInstances()



    

    





