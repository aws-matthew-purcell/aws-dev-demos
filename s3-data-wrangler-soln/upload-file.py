import boto3

# Obtain a references to the S3 service
# Notice we are now using the high-level API (resource) as we are dealing with
# objects rather than the bucket itself
s3 = boto3.resource('s3')

# Define the bucket name
bucketName = "mattpurc-demo-data-wrangler"

# Upload the file
# Point out the first argument is the location of the file on the local system, the second is the key it will assume in S3
s3.Bucket(bucketName).upload_file("/home/ec2-user/environment/aws-dev-demos/s3-data-wrangler/bike-hire-data.csv", "data-files/bike-hire-data.csv")