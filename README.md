# Contact Form Lambda

### Development / Setup


* A Lambda Function written in Python which connects to a simple contact form through an API gateway. 
* An IAM role is created with access to AWS Simple Notification Service (SNS) and attached to the lambda.
* When an event occurs, the contents of the form body is extracted and validated, after which an email notification is triggered to the preconfigured SNS Topic.



