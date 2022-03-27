from telethon import events
from googletrans import Translator

@events.register(events.NewMessage(outgoing=True, pattern=r'\.tr'))
async def runtr(event):
    language = event.message.raw_text.split()
    getmessage = await event.get_reply_message()
    translator = Translator()
    try:
        messagetranslate = translator.translate(f"{getmessage.message}", dest=f"{language[1]}")
        await event.edit(f"Translate: {messagetranslate.text}")
    except:
        pass