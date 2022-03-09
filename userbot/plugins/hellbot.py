# this plugin made by BlackPanther Userbot

"""Plugin for HellBot Repo

\nCode by @DANISH_BABA

type '.destroyx' to get Destroyx userBot repo
"""

import random, re
from blackpantherbot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="destroyx ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://github.com/CRiMiNaL786/DESTROYX) to open this 🔥**Lit AF!!**🔥 **Hêllẞø†** Repo.. Join channel :- @Its_HellBot Repo Uploaded By @BlackPantherBot_Support")
    
  
