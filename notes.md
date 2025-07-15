
---

## ✅ `notes.md`

```md
# Dev Notes – Secure File Scanner

## Setup Steps

1. Created a symmetric KMS key (`secure-s3-key`)
2. Created an S3 bucket (`secure-file-bucket-reem`) with KMS encryption
3. Created IAM role `lambda-s3-kms-role` and attached custom inline policy
4. Created Lambda function `secure-kms-function`
5. Added an S3 trigger to Lambda (for PUT events)
6. Uploaded a `.txt` file with the word `confidential`
7. Checked CloudWatch → Confirmed detection works

---

## Commands / Links

- 🔑 KMS: https://console.aws.amazon.com/kms
- 🪣 S3: https://console.aws.amazon.com/s3
- 🤖 Lambda: https://console.aws.amazon.com/lambda
- 📋 IAM: https://console.aws.amazon.com/iam

---

## Future Features

- Alert via SNS or email when sensitive data is found
- Store scan results in DynamoDB
- Web dashboard to show scan history
- Multi-keyword scan (e.g. "salary", "secret", "classified")

