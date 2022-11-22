#!/usr/bin/env python3
import json
import boto3
import os

def lambda_handler():
    # Reading json file
    file = open(os.getenv('QUALYS_REPORT'))
    json_data = json.loads(file.read())
    
    header = 'Scanned Packages'
    
    data = []
    # data.append(header)
    # Recording Packages and version of softwares
    for name in json_data["softwares"]:
      package_data = name["name"] + "-" + name["version"]
      data.append(package_data)
      # s3_upload(package_data)
    
    data_format = data[1:]
    
    final_data = "\n".join(data[1:])
    
    s3_upload(final_data)
    
    return

def s3_upload(data):
    string = data
    encoded_string = string.encode("utf-8")

    bucket_name = "docker-s3-test-bucket-1"
    file_name = "hello.txt"
    s3_path = "100001/20180223/" + file_name
    
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
 
lambda_handler()
