import boto3
s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket="rolawebucket",Key='upload1.png')

import os
import glob
s3_resource.list_objects(Buckets="rolawebucket")["Contents"]

for file in files:
    s3_resource.download_file(Bucket="rolawebucket",
    Key=file["Key"],
    Filename=cwd+"download_"+file["Key"])
    