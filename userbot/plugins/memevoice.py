# Credits to @spechide and his team for @TROLLVOICEBOT
# made by @danish_baba_the_badass from the snippets of waifu AKA stickerizerbot....
# kang karega kya madarchod?
# aukaat h bsdk teri...jake baap ka loda chus ke aa....


import re

from userbot import bot
from blackpantherbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(danish_baba):
    blackpanther = danish_baba.pattern_match.group(1)
    if not blackpanther:
        if danish_baba.is_reply:
            (await danish_baba.get_reply_message()).message
        else:
            await edit_or_reply(danish_baba, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(blackpanther))}")

    await troll[0].click(
        danish_baba.chat_id,
        reply_to=danish_baba.reply_to_msg_id,
        silent=True if danish_baba.is_reply else False,
        hide_via=True,
    )
    await danish_baba.delete()
    

CmdHelp("memevoice").add_command(
  "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
