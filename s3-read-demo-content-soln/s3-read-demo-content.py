import boto3

# Obtain a reference to the S3 service
s3 = boto3.resource('s3')

# Specify the bucket
demoContentBucket = s3.Bucket('mattpurc-demo-content')

# List the bucket's objects
for bucketObject in demoContentBucket.objects.all():
    print(bucketObject.key)

quit()