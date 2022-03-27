from telethon import events
from time import sleep
from urllib.request import urlopen
import json

@events.register(events.NewMessage(outgoing=True, pattern=r'\.tiktok'))
async def runiptrace(event):
    getip = event.message.raw_text.split()
    messagelocation = event.to_id
    await event.edit("Tracing...")
    sleep(2)
    await event.delete()
    targetip = getip[1]
    url = "https://www.tiktok.com/node/share/user/"
    start = urlopen(url+targetip)
    ipdata = start.read()
    information = json.loads(ipdata)
    await event.client.send_message(messagelocation, f"Name: {information['name']}\nDescription: {information['description']}\nFollowers: {information['followerCount']}\nFollowing: {information['followingCount']}\nTotal Heart: {information['heartCount']}\nTotal Video: {information['videoCount']}\nVerified Account: {information['verified']}\nPrivate Account: {information['privateAccount']}\nTikTok ID: {information['id']}\nAvatar HD: {information['avatarLarger']}\n")