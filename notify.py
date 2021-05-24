from slack_sdk.webhook import WebhookClient
import os
import requests


# Add in from Telegram
CHATID = "CHANGEME"
BOTKEY = "CHANGEME"


TGURL = f"https://api.telegram.org/bot{BOTKEY}/sendMessage"

# Chance to match slack webhook
slackurl = "https://hooks.slack.com/services/VALUE1/VALUE2"
webhook = WebhookClient(slackurl)
HOSTNM = os.popen('hostname').read()
IP = os.popen('curl -s http://whatismyip.akamai.com/').read()
LOGININFO=os.popen('last -1 -i | head -n 1 | cut -d " " -f 1').read()

tgheaders = {
    'Content-Type': 'application/json',
}

tgdata = '{"chat_id": "{}", "text": "Log in to: {}\\n{}\\nfrom: {}", "disable_notification": false}'.format(CHATID,HOSTNM,IP,LOGININFO)

tgresponse = requests.post(f'https://api.telegram.org/bot{BOTKEY}/sendMessage', headers=tgheaders, data=tgdata)


response = webhook.send(text='Log in to: {}\n from {}\n by\n User: {} \n'.format(HOSTNM,IP,LOGININFO))
assert response.status_code == 200
assert response.body == "ok"