import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info("🛠️ Initializing Anu Music Bot...")
        super().__init__(
            name="LearningBots",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<b>✅ Bot Started Successfully!</b>\n\n"
                    f"<b>Name:</b> {self.name}\n"
                    f"<b>Username:</b> @{self.username}\n"
                    f"<b>User ID:</b> <code>{self.id}</code>"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "❌ Unable to send message to the log group/channel."
            )
            raise SystemExit

        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Failed to access the log group/channel: {type(ex).__name__}"
            )
            raise SystemExit

        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "⚠️ Bot must be admin in LOGGER_ID chat."
                )
                raise SystemExit
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Failed to check admin status: {type(ex).__name__}"
            )
            raise SystemExit

        LOGGER(__name__).info(
            f"🎶 Bot is online as {self.name} (@{self.username})"
        )

    async def stop(self):
        LOGGER(__name__).info("🛑 Stopping Anu Music Bot...")
        await super().stop()
