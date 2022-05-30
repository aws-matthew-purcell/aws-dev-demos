import boto3
import logging

# Obtain a references to the S3 service
s3 = boto3.resource('s3')

# List the bucket names
for bucket in s3.buckets.all():
    bucketName = bucket.name + ", " + bucket.creation_date.strftime("%B %d, %Y") + "\n"
    print(bucketName)

quit()