import json
from botocore.vendored import requests
import urllib3
import boto3
from botocore.exceptions import ClientError

http = urllib3.PoolManager()

SENDER = "GetTheDigital Request <hello@gethedigital.com>"
RECIPIENT = "Vitaliy.maliy@gmail.com"
# CONFIGURATION_SET = "ConfigSet"
AWS_REGION = "us-east-1"

TELE_TOKEN='1561781013:AAHOpWSkUtz1tL7DcnXZ1I79dceOj1PsvUg'

def send_email(phone, first_name, last_name, chat_id):
    # if (chat_id == 571417480):145868031
    phone_button = "My phone number"
    token = TELE_TOKEN
    URL = "https://api.telegram.org/bot{}/".format(token)
    final_text = "Thank you. Our managers will contact you shortly."
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
    responce = http.request('GET', url)
        
    SUBJECT = "New GetTheDigital customer wants to have a call back"
    BODY_HTML = """<html>
    <head></head>
    <body>
        <h1>Customer {}wants to have a call back</h1>
        <h3>Please call using this phone number: {}</h3>
    </body>
    </html>
            """.format(first_name + ' ' + last_name + ' ', phone)
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # ConfigurationSetName=CONFIGURATION_SET,
        )	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def send_message(reply, chat_id, text):
    # if (chat_id == 571417480):
    phone_button = "My phone number"
    token = TELE_TOKEN
    URL = "https://api.telegram.org/bot{}/".format(token)
    if (text == "/start"):
        final_text = "Welcome! Please, authorize your number and we will contact you as soon as possible."
    else:
        final_text = "Authorize your number and we will contact you as soon as possible."
    
    data = {
        'chat_id': chat_id,
        'reply_to_message_id': reply,
        'text': final_text,
        'reply_markup': {
            "one_time_keyboard": True,
            "keyboard": [[{
                'text': phone_button,
                'request_contact': True
            }]]
        }
    }
    url = URL + 'sendMessage'
    response = http.request('POST',
                        url,
                        body = json.dumps(data),
                        headers = {'Content-Type': 'application/json'},
                        retries = False)

def lambda_handler(event, context):
    print(event)
    chat_id = event['message']['chat']['id']
    reply = event['message']['message_id']
    if "text" in event['message']:
        text = event['message']['text']
        send_message(reply, chat_id, text)
    if "contact" in event['message']:
        phone = event['message']['contact']['phone_number']
        first_name = ''
        last_name = ''
        if "first_name" in event['message']['contact']:
            first_name = event['message']['contact']['first_name']
        if "last_name" in event['message']['contact']:
            last_name = event['message']['contact']['last_name']
        print(phone)
        print(first_name)
        print(last_name)
        send_email(phone, first_name, last_name, chat_id)  
    return {
        'statusCode': 200
    }