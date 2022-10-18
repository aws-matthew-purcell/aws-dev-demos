import boto3

# Obtain a references to the S3 service
# Notice we are using the low-level API (i.e. client, not resource)
# as head_bucket() is not available in the high-level API
s3 = boto3.client('s3')

# Helper function to check whether bucket exists
def verifyBucketName(s3Client, bucket):
    try:
        s3Client.head_bucket(Bucket=bucket)
        raise SystemExit('This bucket already exists')
    except s3Client.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            # A 404 means the bucket does not exist
            print('Bucket not found')
        if error_code == 403:
            # A 403 indicates the bucket exists in another AWS account
            raise SystemExit('This bucket is owned by another AWS account')
            
# We first need to check whether the bucket already exists
bucketName = "mattpurc-demo-data-wrangler"
verifyBucketName(s3, bucketName)

# If we get here then it hasn't error'ed out, so we can proceed to create the bucket
location = {'LocationConstraint': 'ap-southeast-2'}
s3.create_bucket(Bucket=bucketName, CreateBucketConfiguration=location)

# Implement a waiter to block until the bucket is created
waiter = s3.get_waiter('bucket_exists')
waiter.wait(Bucket=bucketName)

print("Bucket created!")

# Check in the S3 console it has been created

# Rerun the script again to show it fails on the head_bucket check