import urllib3
import json
import os
http = urllib3.PoolManager()

def lambda_handler(event, context):
    url = os.environ['TEAMS_URL']
    send_notification(url, event)

def send_notification(url, event):
    event_message = json.loads(event['Records'][0]['Sns']['Message'])
    accountId = event_message["account"]
    pipeline = event_message["detail"]["pipeline"]
    state = event_messge["detail"]["state"]
    time = event_message["time"]
    message = '''
        Pipeline: {pipeline}
        Account: {account}
        Event: {event}
        Time: {time}
    '''.format(pipeline=pipeline, account=accountId, event=state, time=time)
    msg = {
        "text": message
    }

    encoded_msg = json.dumps(msg).encode('utf-8')
    response = http.request('POST', url, body=encoded_msg)
    print(response)
    