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
   - Name: `<Topic_name>`

2. After creating, click **Create Subscription**
   - Protocol: `Email`
   - Endpoint: _your email address_

3. **Confirm the email subscription** from your inbox
![Subscription](https://github.com/user-attachments/assets/624eb94d-8a60-487e-ab4b-6b7d4e49aefe)
![Topics](https://github.com/user-attachments/assets/a1d89cf9-22b0-483c-b277-71f3ef124c35)

---
---
### 2. IAM Role for Lambda

![IAM_Role](https://github.com/user-attachments/assets/02e5069b-394c-4b35-bb53-ea33a17977d6)

---

---

### 3. Create Lambda Function

Create a Lambda function r.

Runtime: Python 3.x

IAM Role: <IAM RoleName>

Environment Variable:

Key: TOPIC_ARN

Value: your SNS topic ARN
![lambdafn](https://github.com/user-attachments/assets/0cebd1af-a21e-40b2-b25e-e804a15e0f27)

---

---

### 4. Set Up EventBridge Rule
Go to Amazon EventBridge > Rules > Create Rule

Rule Name: <Rulename>

Event Pattern:

  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
  "state": ["running", "stopped"]

Target: Select the Lambda function
![EventBridge_rule_source](https://github.com/user-attachments/assets/a97a1bfc-8336-4e33-8f10-9dea7c7fe1e8)

---

---

### 5. Testing
- Start or stop any EC2 instance
- Check your email for a message.
- ![logs](https://github.com/user-attachments/assets/6eb57806-ccb9-4e6d-a710-012977e70403)
- ![emailNotification](https://github.com/user-attachments/assets/99e0be1f-674b-4399-aba7-ad502ffc01c7)

