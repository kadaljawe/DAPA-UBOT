# Copyright (C) 2019 The Raphielscape Company LLC.
# RAM-UBOT MINTA
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register


daksss = [
    "**Hai orang keren**",
    "**Halo Dapa** 😍",
    "**Dapa kemana sj?** 🤗",
    "**Ini kak** 😉",
    "**Hadir bang Dap** 😁",
    "**Iyaa dap** 🥺",
    "**Aku slalu ada kalo bang dapa butuh🥵**",
    "**Bang Dapa, Aku lagi pengen:(**",
    "**Jangan pergi lagi ya bang**",
    "**Cocok banget emang, aku lagi kangen**",
    "**Dapa on juga akhirnya**🥵",
    "**Mau pap dari aku ngga?** 😋",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

@register(incoming=True, from_users=1900124946, pattern=r"^.daksss$")
async def _(dapa):
    await dapa.reply(random.choice(daksss))



@register(outgoing=True, pattern="^Sping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sabar.__")
    await pong.edit("__Sabar..__")
    await pong.edit("__Sabar...__")
    await pong.edit("__Sabar....__")
    await pong.edit("__Bentar.__")
    await pong.edit("__Bentar..__")
    await pong.edit("__Bentar...__")
    await pong.edit("__Bentar....__")
    await pong.edit("__Nah!!__")
    await pong.edit("💫")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**╭━━━━━━━━━━━━━━━━━╮** \n"
                    f"**       🐯 𝗗𝗔𝗣𝗔-𝗨𝗕𝗢𝗧 🐯** \n"
                    f"**  ✠╼━━━━━━❖━━━━━━━✠** \n"
                    f"**        • sɪɢɴᴀʟ  :** `%sms` \n"
                    f"**        • ᴏᴡɴᴇʀ   :** `{ALIVE_NAME}` \n"
                    f"**        • ʙᴏᴛ ᴠᴇʀ  :** `7.0` \n"
                    f"**╰━━━━━━━━━━━━━━━━━╯** \n" % (duration))


@register(outgoing=True, pattern="^Lping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Sabar Ngentot...`")
    await asyncio.sleep(2)
    await pong.edit("😈")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"✧ **-ꜱɪɢɴᴀʟ- :** "
                    f"`%sms` \n"
                    f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Mohon menunggu.__")
    await pong.edit("__Mohon menunggu..__")
    await pong.edit("__Mohon menunggu...__")
    await pong.edit("__Mohon menunggu.__")
    await pong.edit("__Mohon menunggu..__")
    await pong.edit("__Mohon menunggu...__")
    await pong.edit("__Mohon menunggu.__")
    await pong.edit("__Mohon menunggu..__")
    await pong.edit("__Mohon menunggu...__")
    await pong.edit("💀")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                    f"┣[•**PONG!!**\n"
                    f"┣[•__Signal__    __:__ "
                    f"`%sms` \n"
                    f"┣[•__Uptime__ __:__ "
                    f"`{uptime}` \n"
                    f"╰✠╼━━━━━━❖━━━━━━━✠╯\n" % (duration))


@register(outgoing=True, pattern="^Ping$")
@register(incoming=True, from_users=1900124946, pattern=r"^\.cping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Ping.__")
    await pong.edit("__Pong..__")
    await pong.edit("__Ping...__")
    await pong.edit("__Pong....__")
    await pong.edit("__Ping.__")
    await pong.edit("__Pong..__")
    await pong.edit("__Ping...__")
    await pong.edit("__Pong....__")
    await pong.edit("🔥")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**╭✠╼━━━━━━❖━━━━━━━✠╮**\n"
                    f"**       🔥𝗗𝗔𝗣𝗔-𝗨𝗕𝗢𝗧🔥**\n"
                    f"**╰✠╼━━━━━━❖━━━━━━━✠╯**\n"
                    f"** •  Sɪɢɴᴀʟ   :** "
                    f"`%sms` \n"
                    f"** •  Uᴘᴛɪᴍᴇ  :** "
                    f"`{uptime}` \n"
                    f"** •  Oᴡɴᴇʀ   :** `{ALIVE_NAME}` \n" 
                    f"** •  ʙᴏᴛ ᴠᴇʀ  :** `7.0` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
@register(incoming=True, from_users=1900124946, pattern=r"^\.cping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("NGENTOT!")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**KONTOOLLLL!!**\n**KEKUATAN KONTOL** : `%sms`\n**DURASI KONTOL** : `{uptime}🕛`" % (duration))


@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...✨`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✧ **BOT:** 🐯𝗗𝗔𝗣𝗔-𝗨𝗕𝗢𝗧🐯")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("PONG")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**Oᴡɴᴇʀ : {ALIVE_NAME}**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Ping` | `Lping` | `Xping` | `.ping` | `Sping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Pong`\
         \n↳ : Sama Seperti Perintah Ping."})
