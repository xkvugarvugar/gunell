# Oğurlayan mənə ata desin
# @SmokAndMe


import asyncio
import random
from os import execl
import sys
import io
import sys
from userbot.events import register as brend
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from telethon.tl.types import ChannelParticipantsAdmins as cp
from time import sleep
from userbot.cmdhelp import CmdHelp
from telethon.tl.functions.channels import JoinChannelRequest

class FlagContainer:
    is_active = False


silah = ("M16A4","M416","AKM","G36C","Qroza","QBZ","M762","Mk47","UMP45","Vektor","Tompson","MP5K","PP-19","VSS","QBU","Mini14","Mk14","SLR","AWM","Kar98k","M24","M249","DP-28","S12K","P92","P18C","Molotov")

şəhər = ("Zharki","Georgepol","ShottingRange","Hospital","Gatka","Pochinki","Severny","Ruins","YasnayaPolyana","Stalber","Quary","Primorsk","Kameshki","Rozhok","School","Farm","Shelter","Manison","Prison","Lipovka","FerryPier","Sosnovka","Military","Base","Novorepnoye","Mylta","MyltaPower","Wengen","Gass","LupinFelt","Blomster","Gronhus","HotSpring","RoseFarm","İceborg","Eastport","Fiskerhus","Midtstein","Crabgrass","Helle","Reeds","Watterfall","ShipYard","LumberYard","Aqueduct","Ystad","Holdhus","PowerPlant","Bootcamp","ParadiseResort","Miramar","Erangel","Livik","Sanhok","Wikendi")

# Silah adları ile Tağ 
@brend(outgoing=True, pattern="^.otag.*")
async def pubgtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozcm = None
          aykhan5 = event.message.text.split(" ", 1)
          if len(aykhan5) > 1:
              sozcm = aykhan5[1]
  
          chat = await event.get_input_chat()
          await event.delete()
  
          tags = list(map(lambda m: f"[{random.choice(silah)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(silah)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozcm:
                      tags.append(sozcm)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(1.5) 
      finally:
          FlagContainer.is_active = False
  
# Şəhər adları ilə Tağ 
@brend(outgoing=True, pattern="^.atag.*")
async def pubgtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozcm = None
          aykhan5 = event.message.text.split(" ", 1)
          if len(aykhan5) > 1:
              sozcm = aykhan5[1]
  
          chat = await event.get_input_chat()
          await event.delete()

          tags = list(map(lambda m: f"[{random.choice(şəhər)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(şəhər)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozcm:
                      tags.append(sozcm)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(1.5) 
      finally:
          FlagContainer.is_active = False
   
   
#Bu plugində aykhan_s əməyi vardır

  await a.client(JoinChannelRequest("smokplugin"))
  await a.client(JoinChannelRequest("UpsaSohbet"))
  await a.client(JoinChannelRequest("relaxpagee"))
  await a.client(JoinChannelRequest("smokesoxri"))
    
CmdHelp('tagmodulu').add_command(
    'otag', None, 'Silah adları ilə Tag edər'
    ).add_command(
    'atag', None, 'Şəhər adları ilə tag edər'
    ).add()