"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/59e521721f043e33f7c0a.jpg"
pm_caption = "**ᴹᵃⁿʲᵃᵖᵖᵃᵈᵃ ᵢₛ ₒₙₗᵢₙₑ**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴹᵃⁿʲᵃᵖᵖᵃᵈᵃ          : [ᴳʳᵒᵘᵖ ᴸⁱⁿᵏ](http://t.me/kbfcmanjappada)\n"

pm_caption += "ᴹᵃⁿʲᵃᵖᵖᵃᵈᵃ         : [ᶜʰᵃⁿⁿᵉˡ ᴸⁱⁿᵏ](https://t.me/kbfc_manjappada)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ              : [ʸᵉˡˡᵒʷ](https://telegra.ph/file/59e521721f043e33f7c0a.jpg)\n"

pm_caption += "ᴳʳᵒᵘᵖ ᴼʷⁿᵉʳ        :  [ʙɪᴊɪ ꜱᴀᴍ](http://t.me/kbfcmanjappada)\n"

pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Munnipopz)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
