import modules.client
from telethon import events
from telethon import version
from platform import python_version

client = modules.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.afoot'))
async def runafoot(event):
    await event.delete()
    ridogramuserdetails = await event.get_sender()
    messagelocation = event.to_id
    ridogramimage = "https://media.discordapp.net/attachments/847160530191122482/943525406655524905/20220216_210354.jpg"
    await client.send_file(messagelocation, ridogramimage, caption=f"Dear {ridogramuserdetails.first_name} {ridogramuserdetails.last_name},\nI'm glad to announce that Team Tasik is able to assist you.\n\n╭─⊸ Team Tasik Version: 0.2.0\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You,\nTeam Tasik")
