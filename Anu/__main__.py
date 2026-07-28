# Powered By Team krishna_bots
import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Anu import LOGGER, app, userbot
from Anu.core.call import Anony
from Anu.misc import sudo
from Anu.plugins import ALL_MODULES
from Anu.utils.database import get_banned_users, get_gbanned
from Anu.utils.crash_reporter import setup_global_exception_handler  # ✅ Import crash handler

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Anu").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Anu").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Anu.plugins" + all_module)
    LOGGER("Anu.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    
    # 🔥 FIXED: Voice chat error aane par bot exit nahi hoga, bas warning show karega
    try:
        await Anony.stream_call("https://files.catbox.moe/sji2bj.jpg")
    except NoActiveGroupCall:
        LOGGER("Anu").warning(
            "[WARNING] - Logger Group's Voice Call is turned off. Continuing startup without streaming call..."
        )
    except Exception as e:
        LOGGER("Anu").warning(f"[WARNING] - Stream call failed: {e}")

    await Anony.decorators()
    LOGGER("Anu").info(
        "Anu Music Bot started successfully"
    )
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Anu").info("Stopping Anu Music Bot...")
