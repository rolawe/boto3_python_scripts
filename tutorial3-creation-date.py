import boto3
#s3_resource=boto3.client??
s3_resource=boto3.client("s3")
#bucket_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket['Name'])
    print(bucket['CreationDate'])