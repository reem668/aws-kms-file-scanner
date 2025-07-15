# aws-kms-file-scanner
A fully serverless file scanning pipeline built with AWS Lambda, KMS, and S3. Automatically scans encrypted files for sensitive content like "confidential" and logs the results securely using IAM-controlled access.



# 🔐 Secure File Scanner with AWS Lambda + KMS + S3

A fully serverless pipeline that scans uploaded files for sensitive content using AWS Lambda and KMS-encrypted S3 buckets.

---

## 📦 What it Does

Every time you upload a `.txt` file to an S3 bucket:
- The file is encrypted using AWS KMS.
- A Lambda function is triggered automatically.
- The function reads the file, decrypts it, and scans it for sensitive keywords (like `"confidential"`).
- It logs whether the file is safe or contains sensitive content.

---

## 🚀 Technologies Used

- **Amazon S3** – Secure file storage
- **AWS KMS** – Encryption key management
- **AWS Lambda** – Serverless file scanner
- **IAM** – Access control
- **CloudWatch** – Logs results

---

## 🧠 How It Works

1. Create a symmetric KMS key in AWS.
2. Create an S3 bucket with default encryption using that KMS key.
3. Create an IAM role for Lambda with permissions to:
   - Read from the bucket
   - Decrypt using KMS
   - Write logs to CloudWatch
4. Create a Lambda function with the `lambda_function.py` code in this repo.
5. Add an S3 trigger for `PUT` (upload) events.
6. Upload a `.txt` file → Lambda will run → Check CloudWatch for result.

---

## 📝 Sample Sensitive File

```txt
Internal Memo: Budget 2025
This document is confidential. Do not share externally.
