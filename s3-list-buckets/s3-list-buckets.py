import boto3
import logging

# Obtain references to AWS services
s3 = boto3.resource('s3')
sns = boto3.resource('sns')

# List the bucket names
buffer = ""
for bucket in s3.buckets.all():
    buffer += bucket.name + ", " + bucket.creation_date.strftime("%B %d, %Y") + "\n"

print(buffer)

quit()