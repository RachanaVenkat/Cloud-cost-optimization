import boto3

# Create an S3 client
client = boto3.client('s3')

# Create the bucket
response = client.get_bucket_acl(
    Bucket='rachana-boto3-demo-789'
)
print(response)
# response = client.create_bucket(
#     Bucket='rachana-boto3-demo-789',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1'
#     },
# )

