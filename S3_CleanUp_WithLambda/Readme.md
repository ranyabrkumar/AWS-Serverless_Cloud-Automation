# 🧹 S3 Cleanup Lambda Function (Metadata-Based)

This project contains an AWS Lambda function that automatically deletes files in an S3 bucket **based on their custom metadata timestamp**, simulating "old file cleanup" behavior.

Since you can't modify the `LastModified` field in S3, we use a custom metadata field like `original-upload-date` to represent when the file was logically created.

---


## Steps Involved

1. When uploading files, add metadata:  
   `original-upload-date = YYYY-MM-DDTHH:MM:SSZ` (ISO format)

2. The Lambda function:
   - Lists all objects in a bucket
   - Fetches their metadata
   - Parses `original-upload-date`
   - Deletes objects where that date is older than 30 days
   - Logs deleted object keys to CloudWatch

---

## 📦 Folder Structure

