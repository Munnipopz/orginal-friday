"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/6f8d9001de13b3f8e573a.jpg"
pm_caption = "**Fᵣᵢdₐy ᵢₛ ₒₙₗᵢₙₑ**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴍʏ ɢʀᴏᴜᴘ          : [ᴡᴇʟᴄᴏᴍᴇ](https://t.me/joinchat/Oq1jlViv1uS2AkOG9MKChw)\n"

pm_caption += "ᴍʏ ᴄʜᴀɴɴᴇʟ     : [ᴡᴇʟᴄᴏᴍᴇ](https://t.me/joinchat/AAAAAEdoBMaQSuvk0xFNCw)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ              : [ᴹᴵᵀ ᴸⁱᶜᵉⁿᶜᵉ](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ    :  [𝙎𝙩𝙖𝙧𝙠𝙂𝙖𝙣𝙜](GitHub.com/StarkGang)\n"

pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Munnipopz)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
