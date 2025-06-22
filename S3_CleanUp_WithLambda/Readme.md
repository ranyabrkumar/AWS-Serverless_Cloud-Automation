# 🧹 S3 Cleanup Lambda Function (Metadata-Based)

This project contains an AWS Lambda function that automatically deletes files in an S3 bucket **based on their custom metadata timestamp**, simulating "old file cleanup" behavior.

Since you can't modify the `LastModified` field in S3, we use a custom metadata field like `original-upload-date` to represent when the file was logically created.

---


## Steps Involved

### 1. When uploading files, add metadata:  
   `original-upload-date = YYYY-MM-DDTHH:MM:SSZ` (ISO format)
### 2. Create IAM role with FULLEC2ACCESS

### 2. The Lambda function:
   - Lists all objects in a bucket
   - Fetches their metadata
   - Parses `original-upload-date`
   - Deletes objects where that date is older than 30 days
   - Logs deleted object keys to CloudWatch
### 3. manually trigger the run and test
![logs](https://github.com/user-attachments/assets/4f31c686-7448-487a-9895-54959d8205be)
---
Manua

![lambdafn](https://github.com/user-attachments/assets/903e8feb-db6f-4b7d-96c0-c320384a26d3)
![IAM_role](https://github.com/user-attachments/assets/7143751e-a33d-4cbc-a32e-d8b7f0c0df22)

