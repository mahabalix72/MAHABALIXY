import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bae74190b4bbcfa058415.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = ðð ðððððð ðð ð](https://t.me/BROKENLONDAZ)

ðð«ððð­ð¨ð« :- [â¨ ðð ðððððð ðð ð](https://t.me/BROKENLONDAZ)
ðð®ð©ð©ð¨ð«ð­ :- [â¨ ðððððððð â¤ï¸ð¸](https://t.me/Flarting_chatting)
ðð¢ð¬ðð®ð¬ð¬ :- [â¨  ððððð ð§](https://t.me/Flarting_chatting)

ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = ðð ðððððð ðð ð](https://t.me/BROKENLONDAZ)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/Flarting_chatting")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bae74190b4bbcfa058415.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://t.me/Flarting_chatting")
                ]
            ]
        ),
    )
