import boto3
import sys

s3 = boto3.resource('s3')

def create_bucket(bucketName, region):
    bucket = s3.create_bucket(
        Bucket=bucketName, 
        CreateBucketConfiguration={'LocationConstraint': region}) # Create a the named bucket
    bucket.wait_until_exists() # Pause execution of code until the bucket is created
    s3.Object(bucketName, 'index.html').put(
        ACL='public-read',
        ContentType='text/html',
        Body=open('index.html', 'rb')
    ) # Upload index.html and set the policy and content type, upload any other documents here.
    bucket_website = bucket.Website() # Define bucket as website which sets the policies as well
    bucket_website.put(WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'}
    }) # Set the index document to index.thml
    print ('Website is live at: http://' + bucket.name + '.s3-website-' + region + '.amazonaws.com')
    return bucket.name

if __name__ == "__main__":
    create_bucket(sys.argv[1], sys.argv[2]) # Pass the command line argument to create bucket
