import re

from blackpantherbot import bot
from blackpantherbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from blackpantherbot.cmdhelp import CmdHelp
from blackpantherbot.helpers.functions import deEmojify
from userbot.Config import Config
from . import *

@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(danish_baba):
    blackpanther = danish_baba.pattern_match.group(1)
    if not blackpanther:
        if danish_baba.is_reply:
            (await danish_baba.get_reply_message()).message
        else:
            await edit_or_reply(danish_baba, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(blackpanther))}")

    await troll[0].click(
        danish_baba.chat_id,
        reply_to=danish_baba.reply_to_msg_id,
        silent=True if danish_baba.is_reply else False,
        hide_via=True,
    )
    await danish_baba.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
