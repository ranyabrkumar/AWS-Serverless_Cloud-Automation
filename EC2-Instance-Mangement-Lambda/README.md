#  EC2 Auto Start/Stop with AWS Lambda

A simple AWS Lambda function written in Python that automatically **starts** or **stops EC2 instances** based on their `Action` tag value.

## Lambda function:
- Finds all EC2 instances with the tag `Action=Auto-Stop` and stops them (if not already stopped).
- Finds all EC2 instances with the tag `Action=Auto-Start` and starts them (if not already running).

Trigger it manually and Test 

---

## Steps Involved

### 1. Create EC2 Instances
- launch two EC2 t2.micro instances .
- Tag them as follows:
  - **Instance 1** → `Action = Auto-Stop`
  - **Instance 2** → `Action = Auto-Start`
  ![EC2_instance](https://github.com/user-attachments/assets/37ff74b7-decf-41fc-beaf-d913ae8e7f8d)


### 2. Create IAM Role for Lambda
- Go to **IAM > Roles > Create Role**
- Choose **Lambda** as the service
- Attach the following policies:
  - `AmazonEC2FullAccess` *(for managing EC2)*
  - `AWSLambdaBasicExecutionRole` *(for CloudWatch logging)*
- Name of role `Lambda_EC2_Management`
![IAMRole](https://github.com/user-attachments/assets/a339f667-5f9d-4bbb-a8e8-d8fb83c7ae92)

### 3. Create the Lambda Function
- Go to **AWS Lambda > Create Function**
- Runtime: `Python 3.x`
- Assign the IAM role you just created
- Paste in the function code from `lambda_function.py` (in this repo)
![lambdafn](https://github.com/user-attachments/assets/76969a81-309d-461b-91cc-67fe12e6f739)

---
### 4. Manual Execution
- Manual Test the lambda function
- After execution confirm whether instance status chnages as expected.
  
![ManualTest_execution](https://github.com/user-attachments/assets/d8d992bb-7c02-4a5a-a73e-f1f64f858378)
![ManualTest_Logs](https://github.com/user-attachments/assets/9480f10b-e306-49d1-bc2e-d27d799f6e50)
