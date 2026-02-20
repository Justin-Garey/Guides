# Simple API

## Basic Endpoints

- Lambda for functionality
- API Gateway for the API endpoints
- IAM roles for permissions between the API Gateway and Lambda
- CloudWatch Logs 

### Storage

- DynamoDB for a NoSQL, key-value and document database
- RDS/Aurora for relational databases
- S3 for storage

### API Keys

- API Gateway must be a REST API configuration
- In the API methods, set the API Key Required to true
- Create an API key and usage plan
- Add the API stage to the usage plan and attach the API key
- Client calls should include the API key in the `x-api-key` header.

### API Key Authentication

- For HTTP API in API Gateway, Lambda Authorizer is used to authenticate a key from DynamoDB/Secrets Manager.

### Authentication

- Cognito JWT Authorizer can be used.
- A user would have a username + password and would get a token from Cognito for session verification.

### Custom Domain

- Get an ACM Certificate
- Create the custom domain name in API Gateway
- Map the domain to the API and stage
- Create the DNS record in Route53
- Redirect HTTP to HTTPS