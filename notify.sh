#!/bin/sh
# Telegram Login Notifications
CHATID=CHANGEME
BOTKEY=CHANGEME
#get hostname
HOSTNM=$( hostname )
#get external IP address
IP=$( curl -s http://whatismyip.akamai.com/ )
#find IP address of person last logged in
LOGININFO=$( last -1 -i | head -n 1)
#parse into nice format
LOGININFO1=$( python3 -c "login='$LOGININFO'.split('   '); del login[1]; del login[1]; print(''.join([x.strip(' ') + '   \n' for x in login]));" )
#send infomration to telegram notification bot
curl -X POST -H 'Content-Type: application/json' -d "{\"chat_id\": \"$CHATID\", \"text\": \"Log in to: $HOSTNM\n$IP\nfrom: $LOGININFO1\", \"disable_notification\": false}" https://api.telegram.org/bot$BOTKEY/sendMessage --silent > /dev/null
