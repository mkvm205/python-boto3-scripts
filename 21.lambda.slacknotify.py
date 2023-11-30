import requests
import json

slack_web_hook = 'https://hooks.slack.com/services/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'

def send_slack(event, context):
    print(str(even))
    slack_message = {'text': 'Ec2 Instance Stopped'}
    resp = requests.post(slack_web_hook,data = json.dumps(slack_message))
    return resp.txt               