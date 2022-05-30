import boto3
import logging

# Obtain references to AWS services
s3 = boto3.resource('s3')

# List the bucket names
for bucket in s3.buckets.all():
    bucketName = bucket.name + ", " + bucket.creation_date.strftime("%B %d, %Y") + "\n"
    print(bucketName)

quit()