# Powered By Team LearningBots
import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from LearningBots import LOGGER, app, userbot
from LearningBots.core.call import Anony
from LearningBots.misc import sudo
from LearningBots.plugins import ALL_MODULES
from LearningBots.utils.database import get_banned_users, get_gbanned
from LearningBots.utils.crash_reporter import setup_global_exception_handler  # ✅ Import crash handler

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LearningBots").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("LearningBots").warning(
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
        importlib.import_module("LearningBots.plugins" + all_module)
    LOGGER("LearningBots.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://files.catbox.moe/10xn4h.jpg")
    except NoActiveGroupCall:
        LOGGER("LearningBots").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("LearningBots").info(
        "LearningBots Music Bot started successfully"
    )
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("LearningBots").info("Stopping LearningBots Music Bot...")
