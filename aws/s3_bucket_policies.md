# Example S3 Bucket Policies

## Publicly Accessible Bucket Endpoints

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::justin-garey-public-storage/*",
                "arn:aws:s3:::justin-garey-public-storage"
            ]
        }
    ]
}
```