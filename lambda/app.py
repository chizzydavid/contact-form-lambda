import json
import boto3

sns_client = boto3.client("sns")

def lambda_handler(event, context):
    try:
        if 'body' in event:
            event = json.loads(event['body'])
            
        sns_client.publish(
            TargetArn = 'TargetResource::ARN',
            Subject = 'Portfolio Contact Form: '+ event["subject"],        
            Message = 'Sender Name: ' + event["name"] + '\n' + 'Sender Email: ' + event["email"] + '\n' + event["message"]
        )
            
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Message sent successfully.'
            }),
            'headers':{ 'Access-Control-Allow-Origin' : '*' }
        }
                
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                "error": 'Something went wrong. ' + str(e)
            }),
            'headers':{ 'Access-Control-Allow-Origin' : '*' }
        }


