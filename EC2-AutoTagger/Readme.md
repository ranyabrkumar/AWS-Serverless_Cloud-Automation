# EC2 Auto-Tagging with AWS Lambda + Boto3

Automatically tag newly launched EC2 instances with helpful metadata using AWS Lambda and EventBridge (CloudWatch Events). This helps improve tracking, billing, and automation.

---

## Steps Involved

IAM Role Creation:
1. Create IAM Role for Lambda:
    - Go to IAM > Roles > Create role
    - Choose Lambda
    - Attach the policies:
        - AmazonEC2FullAccess
        - AWSLambdaBasicExecutionRole (for logging to CloudWatch)
![IAM_Role](https://github.com/user-attachments/assets/d5d1b544-1b97-48d5-abcf-40a114e48b15)

2. Lambda function :
- Runs whenever a new EC2 instance is launched
- Automatically adds:
  - A `LaunchDate` tag with the current date (UTC)
  - A `CreatedBy` tag with a custom label like `AutoTagger`
![lambdafn](https://github.com/user-attachments/assets/27265782-6900-4326-95cd-a34128cae37f)

3. Rule Creation:
    - Set up a CloudWatch Event Rule:
        1. Go to **CloudWatch > Rules** (or **EventBridge > Rules**)
        2. Click **Create rule**
        3. **Event Source:**
            - Service: EC2
            - Event type: EC2 Instance State-change Notification
            - Specific state: running (This triggers right after launch)
        4. **Target:** Choose your Lambda function
![Rule](https://github.com/user-attachments/assets/787e2e36-9ecc-4ec4-ba99-d988f5513bc6)

4. Test the Setup
    1. Go to **EC2 > Launch Instance**
    2. Use any AMI (e.g., Amazon Linux 2) and launch it
    3. Wait ~1 minute
    4. Go to **EC2 > Instances > Tags** tab
    5. You should see:
        - `LaunchDate = YYYY-MM-DD`
        - `CreatedBy = AutoTagger`

![EC2_tag](https://github.com/user-attachments/assets/22c9e491-2913-4f3c-b20f-e8c9171ae389)
![logs](https://github.com/user-attachments/assets/3d8adc99-8b7e-4693-b710-65ffbbbce6cf)

---

## Work flow

1. An EC2 instance is launched
2. AWS EventBridge  detects it
3. EventBridge triggers a Lambda function
4. Lambda reads the instance ID and applies tags

---


