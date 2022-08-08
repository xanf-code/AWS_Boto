# -----------------------------------------------
# Create S3 bucket - done
# Add Data into s3 bucket - done 
# Get file and Delete file - done
# Delete S3 bucket - done
# Bucket Policy (Insert/Delete) - done
# KMS S3 Integration - 
# ------------------------------------------------

import json
import boto3
import uuid

s3_client = boto3.client('s3')

BUCKET_POLICY = {
    "Version": "2012-10-17", #YYYY-MM-DD
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::test-bucket-darshan/*"
        }
    ]
}

def create_bucket(bucket_name,acl_permission,region):
    s3_client.create_bucket(
    Bucket=bucket_name,
    ACL=acl_permission,
    CreateBucketConfiguration= None if region == 'us-east-1' else {
        'LocationConstraint': region,
    }
    )
    print("S3 bucket created successfully!!!!")

def delete_bucket(bucket_name):
    s3_client.delete_bucket(
    Bucket=bucket_name
    )
    print("Bucket Deleted")   
    
def upload_files(filepath,bucket_name):
    s3 = boto3.resource('s3')
    id_key = str(uuid.uuid5(uuid.NAMESPACE_DNS,"buckets3"))
    s3.meta.client.upload_file(filepath, bucket_name , id_key)
    print("Upload Successfull!!")
    
def get_file(bucket_name,key):
    file = s3_client.get_object(
    Bucket=bucket_name,
    Key=key,
    )
    print(file)

def delete_file(bucket_name,key):
    s3_client.delete_object(
    Bucket=bucket_name,
    Key=key,
    )
    print("Successfully Deleted!") 
    
def create_bkt_policy(bucket_name, policy_json):
    policy_document = json.dumps(policy_json)
    s3_client.put_bucket_policy(
        Bucket = bucket_name,
        Policy = policy_document
    )
    print("Policy Created!!")
    
def delete_bkt_policy(bkt_name):
    s3_client.delete_bucket_policy(Bucket=bkt_name)
    print('Policy Deleted from ' + bkt_name + "!!")
        
# create_bucket('test-bucket-darshan','private','ap-south-1')
# upload_files('files/hello.txt','test-bucket-darshan')
# delete_file('test-bucket-darshan','2b1f514b-007a-56c1-a2c4-f26302ed671f')
# delete_bucket('test-bucket-darshan')
# create_bkt_policy('test-bucket-darshan', BUCKET_POLICY)
# delete_bkt_policy('test-bucket-darshan')