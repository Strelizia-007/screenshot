from pyrogram import filters

from bot.screenshotbot import ScreenShotBot
from bot.database import Database


db = Database()


@ScreenShotBot.on_message(filters.private & filters.command("set_watermark"))
async def _(c, m):

    if len(m.command) == 1:
        await m.reply_text(
            text="✨ 𝗖𝗮𝗻 𝗔𝗗𝗗 𝗖𝘂𝘀𝗧𝗼𝗠 𝗪𝗮𝘁𝗲𝗿𝗠𝗮𝗿𝗸 𝗧𝗲𝘅𝗧 𝘁𝗼 𝗦𝗰𝗿𝗲𝗲𝗻𝗦𝗵𝗼𝗧𝘀.\n\n𝗨𝘀𝗮𝗴𝗲: `/set_watermark text`. "
            "𝗧𝗲𝘅𝗧 𝗦𝗵𝗼𝘂𝗹𝗗 𝗡𝗼𝗧 𝗘𝘅𝗰𝗲𝗲𝗱 𝟯𝟬 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗥𝘀. 🍁",
            quote=True,
            parse_mode="markdown",
        )
        return

    watermark_text = " ".join(m.command[1:])
    if len(watermark_text) > 30:
        await m.reply_text(
            text=f"𝗧𝗵𝗲 𝗪𝗮𝘁𝗲𝗿𝗠𝗮𝗿𝗞 𝗧𝗲𝘅𝗧 𝗬𝗼𝘂 𝗣𝗿𝗼𝘃𝗶𝗗𝗲𝗗 (__{watermark_text}__) 𝗶𝘀 `{len(watermark_text)}` "
            "𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗥𝘀 𝗟𝗼𝗻𝗚! 𝗬𝗼𝘂 𝗖𝗮𝗻𝗻𝗼𝘁 𝗦𝗲𝗧 𝗪𝗮𝘁𝗲𝗿𝗠𝗮𝗿𝗞 𝗧𝗲𝘅𝗧 𝗚𝗿𝗲𝗮𝗧𝗲𝗥 𝘁𝗵𝗮𝗻 𝟯𝟬 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗥𝘀. ⚙️",
            quote=True,
            parse_mode="markdown",
        )
        return

    await db.update_watermark_text(m.chat.id, watermark_text)
    await m.reply_text(
        text=f"🐾 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗦𝘂𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗦𝗲𝘁  __{watermark_text}__ 𝗮𝘀 𝘆𝗼𝘂𝗿 𝗪𝗮𝘁𝗲𝗿𝗠𝗮𝗿𝗞 𝗧𝗲𝘅𝗧. "
        "𝗧𝗵𝗶𝘀 𝗧𝗲𝘅𝘁 𝗪𝗶𝗹𝗹 𝗯𝗲 𝗔𝗗𝗗𝗲𝗗 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗤𝘂𝗲𝗿𝗶𝗲𝘀! /settings 𝗧𝗼 𝗥𝗲𝗠𝗼𝘃𝗘. 🎗️",
        quote=True,
        parse_mode="markdown",
    )
