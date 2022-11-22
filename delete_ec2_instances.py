import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()

data = x["Reservations"]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        print(instance_id)
