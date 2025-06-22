import boto3
from datetime import datetime, timedelta, timezone

s3 = boto3.client('s3')
bucket = 's3-cleanup-ranya'
key = 's3doc/s3_document (1).txt'

# Simulated "original" date (35 days ago)
fake_date = (datetime.now(timezone.utc) - timedelta(days=35)).isoformat()

s3.put_object(
    Bucket=bucket,
    Key=key,
    Body='This file was originally uploaded 35 days ago.',
    Metadata={'original-upload-date': fake_date}
)
print(f"Uploaded {key} to {bucket} with simulated original upload date {fake_date}.")