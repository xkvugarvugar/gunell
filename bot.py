import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**LegendTagger Bot**, \nDaha çox bilgi üçün **/help**'i yazın.",
                    buttons=(
                      [Button.url('Məni qrupa əlavə et', 'https://t.me/loungetaggerbot?startgroup=a'),
                      [Button.url(' Support', 'https://t.me/legendsup'),
                      [Button.url('Master', 'https://t.me/@aliyefh_sos'),
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Legendtagger bot'un helper Menusu**\n\nəmr: /all \n`Örnək: /all Salam Chat!`  \nBu Əmr'i hər hansı bir mesaja reply ataraq yoxlaya bilərsiniz."
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Məni qrupa əlavə et', 'https://t.me/loungetaggerbot?startgroup=a'),
                      [Button.url(' Support', 'https://t.me/legendsup'),
                      [Button.url('Master', 'https://t.me/@aliyefh_sos'),
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Buranın Bir qrup vəya kanal olduğundan əminsən ?__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Yalnızca adminlər!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__XƏTA \nKöhnə mesajlarda tag edə bilmirəm!\n.........__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Mənə bir mətn vəya söz ver !__")
  else:
    return await event.respond("__Mənə bir mətn vəya söz ver !__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("işləmə dayandırıldı.❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("işləmə dayandırıldı.❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


print(">> Owner @quliyevv_17\nMaster BGMALIY⋈\nBot online <<")
client.run_until_disconnected()
