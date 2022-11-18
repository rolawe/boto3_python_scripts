import boto3
#s3_resource=boto3.client("s3")
#s3_resource.upload_file(Filename="LPIStudyGuide.pdf", Bucket="rolawebucket", Key="uploadtest.pdf")

import os
import glob

cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.png")

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
        Filename=file,
        Bucket="rolawebucket",
        Key=file.split("/")[-1])