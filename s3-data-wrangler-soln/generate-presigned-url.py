import boto3

# Obtain a references to the S3 service
s3 = boto3.resource('s3')

# Generate the URL
url = s3.meta.client.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': 'mattpurc-demo-data-wrangler', 'Key': 'data-files/bike-hire-data.csv'},
    ExpiresIn=3600)

print(url)