#  EC2 State Change Monitor with AWS Lambda, Boto3, and SNS

This project automatically notifies you by email whenever an EC2 instance is **started** or **stopped**. It uses:

- AWS Lambda
- Amazon SNS (for notifications)
- Amazon EventBridge (formerly CloudWatch Events)
- Boto3 (AWS SDK for Python)

---

## WorkFlow

- Watches for EC2 instance state changes (e.g., started, stopped)
- Sends a notification via **email** (using SNS)
- Triggered automatically — no manual checking needed

---

## Project Components

| Component     | Purpose                                      |
|---------------|----------------------------------------------|
| Lambda        | Processes EC2 events and sends notification  |
| SNS Topic     | Sends email alert to subscribers             |
| EventBridge   | Detects EC2 state changes                    |
| Boto3         | AWS SDK used inside Lambda                   |

---

## Step Involved

### 1. Create SNS Topic and Email Subscription

1. Go to **AWS SNS > Topics > Create Topic**
   - Type: `Standard`
   - Name: `EC2StateChangeTopic`

2. After creating, click **Create Subscription**
   - Protocol: `Email`
   - Endpoint: _your email address_

3. **Confirm the email subscription** from your inbox

---

### 2. IAM Role for Lambda

Create a role named `LambdaEC2MonitorRole` with the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    }
  ]
}
### 3. Lambda Function Code
Create a Lambda function named EC2StateChangeNotifier.

Runtime: Python 3.x

IAM Role: LambdaEC2MonitorRole

Environment Variable:

Key: TOPIC_ARN

Value: your SNS topic ARN

### 4. Set Up EventBridge Rule
Go to Amazon EventBridge > Rules > Create Rule

Rule Name: EC2StateChangeMonitor

Event Pattern:

json
Copy
Edit
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running", "stopped"]
  }
}
Target: Select the EC2StateChangeNotifier Lambda function

### 4. Set Up EventBridge Rule
Go to Amazon EventBridge > Rules > Create Rule

Rule Name: EC2StateChangeMonitor

Event Pattern:
Target: Select the EC2StateChangeNotifier Lambda function

###Testing
Start or stop any EC2 instance

Wait a few seconds

Check your email for a message.