
import io
from random import randint, uniform

from PIL import Image, ImageEnhance, ImageOps
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP
from blackpantherbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="frybot$"))
@bot.on(sudo_cmd(pattern="frybot$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        event = await edit_or_reply(event, "Reply to any user message.")
        return
    reply_message = await event.get_reply_message()
    if event.is_reply:
        reply_message = await event.get_reply_message()
        data = await check_media(reply_message)
        if isinstance(data, bool):
            event = await edit_or_reply(event, "`I can't deep fry that!`")
            return
    if not event.is_reply:
        event = await edit_or_reply(
            event, "`Reply to an image or sticker to deep fry it!`"
        )
        return
    chat = "@image_deepfrybot"
    if reply_message.sender.bot:
        event = await edit_or_reply(event, "Reply to actual users message.")
        return
    event = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=432858024)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock @image_deepfrybot and try again")
            return
        await bot.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.client.send_file(event.chat_id, response.message.media)
        await event.delete()


@bot.on(admin_cmd(pattern="deepfry(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="deepfry(?: |$)(.*)", allow_sudo=True))
async def deepfryer(event):
    try:
        frycount = int(event.pattern_match.group(1))
        if frycount < 1:
            raise ValueError
    except ValueError:
        frycount = 2
    if event.is_reply:
        reply_message = await event.get_reply_message()
        data = await check_media(reply_message)
        if isinstance(data, bool):
            event = await edit_or_reply(event, "`I can't deep fry that!`")
            return
    if not event.is_reply:
        event = await edit_or_reply(
            event, "`Reply to an image or sticker to deep fry it!`"
        )
        return
    # download last photo (highres) as byte array
    image = io.BytesIO()
    await event.client.download_media(data, image)
    image = Image.open(image)
    # fry the image
    hmm = await edit_or_reply(event, "`Deep frying media…`")
    for _ in range(frycount):
        image = await deepfry(image)
    fried_io = io.BytesIO()
    fried_io.name = "image.jpeg"
    image.save(fried_io, "JPEG")
    fried_io.seek(0)
    await event.reply(file=fried_io)
    await hmm.delete()


async def deepfry(img: Image) -> Image:
    colours = (
        (randint(50, 200), randint(40, 170), randint(40, 190)),
        (randint(190, 255), randint(170, 240), randint(180, 250)),
    )
    img = img.copy().convert("RGB")
    # Crush image to blackpanther and back
    img = img.convert("RGB")
    width, height = img.width, img.height
    img = img.resize(
        (int(width ** uniform(0.8, 0.9)), int(height ** uniform(0.8, 0.9))),
        resample=Image.LANCZOS,
    )
    img = img.resize(
        (int(width ** uniform(0.85, 0.95)), int(height ** uniform(0.85, 0.95))),
        resample=Image.BILINEAR,
    )
    img = img.resize(
        (int(width ** uniform(0.89, 0.98)), int(height ** uniform(0.89, 0.98))),
        resample=Image.BICUBIC,
    )
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, randint(3, 7))
    # Generate colour overlay
    overlay = img.split()[0]
    overlay = ImageEnhance.Contrast(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageEnhance.Brightness(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageOps.colorize(overlay, colours[0], colours[1])
    # Overlay red and yellow onto main image and sharpen the blackpanther out of it
    img = Image.blend(img, overlay, uniform(0.1, 0.4))
    img = ImageEnhance.Sharpness(img).enhance(randint(5, 300))
    return img


async def check_media(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            data = reply_message.photo
        elif reply_message.document:
            if (
                DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
                in reply_message.media.document.attributes
            ):
                return False
            if (
                reply_message.gif
                or reply_message.video
                or reply_message.audio
                or reply_message.voice
            ):
                return False
            data = reply_message.media.document
        else:
            return False
    if not data or data is None:
        return False
    return data


CmdHelp("frybot").add_command(
  'frybot', '<reply to a image/sticker>', 'Fries the given sticker or image'
).add_command(
  'deepfry', '<1-9> <reply to image/sticker>', 'Fries the given sticker or image based on level if you dont give anything then it is default to 2'
).add()
