## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3EC2 Auto-Tagging with AWS Lambda + Boto3

Automatically tag newly launched EC2 instances with helpful metadata using AWS Lambda and EventBridge (CloudWatch Events). This helps improve tracking, billing, and automation.

---

### Steps Involved

IAM Role Creation:
1. Create IAM Role for Lambda:
    - Go to IAM > Roles > Create role
    - Choose Lambda
    - Attach the policies:
        - AmazonEC2FullAccess
        - AWSLambdaBasicExecutionRole (for logging to CloudWatch)

2. Lambda function :
- Runs whenever a new EC2 instance is launched
- Automatically adds:
  - A `LaunchDate` tag with the current date (UTC)
  - A `CreatedBy` tag with a custom label like `AutoTagger`
3. Rule Creation:
    - Set up a CloudWatch Event Rule:
        1. Go to **CloudWatch > Rules** (or **EventBridge > Rules**)
        2. Click **Create rule**
        3. **Event Source:**
            - Service: EC2
            - Event type: EC2 Instance State-change Notification
            - Specific state: running (This triggers right after launch)
        4. **Target:** Choose your Lambda function

4. Test the Setup
    1. Go to **EC2 > Launch Instance**
    2. Use any AMI (e.g., Amazon Linux 2) and launch it
    3. Wait ~1 minute
    4. Go to **EC2 > Instances > Tags** tab
    5. You should see:
        - `LaunchDate = YYYY-MM-DD`
        - `CreatedBy = AutoTagger`
---

### Work flow

1. An EC2 instance is launched
2. AWS EventBridge  detects it
3. EventBridge triggers a Lambda function
4. Lambda reads the instance ID and applies tags
- [Read more] (https://github.com/ranyabrkumar/AWS-Serverless_Cloud-Automation/blob/main/EC2-Instance-Mangement-Lambda/README.md)

---
## Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

**Task:** Automate the deletion of files older than 30 days in a specific S3 bucket.

### Instructions

1. **S3 Setup:**
    - Navigate to the S3 dashboard and create a new bucket.
    - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

2. **Lambda IAM Role:**
    - In the IAM dashboard, create a new role for Lambda.
    - Attach the `AmazonS3FullAccess` policy to this role.  
      *(Note: For enhanced security in real-world scenarios, use more restrictive permissions.)*

3. **Lambda Function:**
    - Navigate to the Lambda dashboard and create a new function.
    - Choose Python 3.x as the runtime.
    - Assign the IAM role created in the previous step.
    - Write the Boto3 Python script to:
        1. Initialize a boto3 S3 client.
        2. List objects in the specified bucket.
        3. Delete objects older than 30 days.
        4. Print the names of deleted objects for logging purposes.

4. **Manual Invocation:**
    - After saving your function, manually trigger it.
    - Go to the S3 dashboard and confirm that only files newer than 30 days remain.
- [Read more] (https://github.com/ranyabrkumar/AWS-Serverless_Cloud-Automation/blob/main/S3_CleanUp_WithLambda/Readme.md)

## Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

**Task:** Automatically tag any newly launched EC2 instance with the current date and a custom tag.

### Instructions

1. **EC2 Setup:**
   - Ensure you have the capability to launch EC2 instances.

2. **Lambda IAM Role:**
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role.

3. **Lambda Function:**
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.
     4. Print a confirmation message for logging purposes.

4. **CloudWatch Events:**
   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.
   - Attach the Lambda function as the target.

5. **Testing:**
   - Launch a new EC2 instance.
   - After a short delay, confirm that the instance is automatically tagged as specified.
- [Read more] (https://github.com/ranyabrkumar/AWS-Serverless_Cloud-Automation/blob/main/EC2-AutoTagger/Readme.md)
---
### Assignment 14: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS

Task: Set up a Lambda function that listens to EC2 state change events and sends SNS notifications detailing the state changes.

Instructions:

1. SNS Setup:

   - Navigate to the SNS dashboard and create a new topic.

   - Subscribe to this topic with your email.

2. Lambda IAM Role:

   - Create a role with permissions to read EC2 instance states and send SNS notifications.

3. Lambda Function:

   - Create a function and assign the above IAM role.

   - Use Boto3 to:

     1. Extract details from the event regarding the EC2 state change.

     2. Send an SNS notification with details about which EC2 instance changed state and the new state (e.g., started, stopped).

4. EC2 Event Bridge (formerly CloudWatch Events):

   - Set up an Event Bridge rule to trigger your Lambda function whenever an EC2 instance state changes.

5. Testing:

   - Start or stop one of your EC2 instances.

- [Read more] (https://github.com/ranyabrkumar/AWS-Serverless_Cloud-Automation/blob/main/EC2StatusMontor/Readme.md)
