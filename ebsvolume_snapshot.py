import boto3
ec2_client=boto3.client("ec2")
#ec2_client.create_snapshot(Description='snapshot from basevolume using python',
   # VolumeId='vol-01c452af295181ed3')
ec2_client.create_volume(AvailabilityZone='us-east-2b',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-014986d03d486cf9e',
      VolumeType='gp2')