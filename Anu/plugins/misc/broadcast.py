import time
import logging
import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMembersFilter
from pyrogram.errors import FloodWait, RPCError
from pyrogram.types import Message

from Anu import app
from Anu.misc import SUDOERS
from Anu.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)
from Anu.utils.decorators.language import language
from Anu.utils.formatters import alpha_to_int
from config import adminlist
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("Broadcast")

SEMAPHORE = asyncio.Semaphore(10)

@app.on_message(filters.command("broadcast") & SUDOERS)
async def broadcast_command(client, message: Message):
    command = message.text.lower()
    mode = "forward" if "-forward" in command else "copy"

    if "-all" in command:
        users = await get_served_users()
        chats = await get_served_chats()
        target_users = [u["user_id"] for u in users]
        target_chats = [c["chat_id"] for c in chats]
    elif "-users" in command:
        users = await get_served_users()
        target_users = [u["user_id"] for u in users]
        target_chats = []
    elif "-chats" in command:
        chats = await get_served_chats()
        target_users = []
        target_chats = [c["chat_id"] for c in chats]
    else:
        return await message.reply_text("❗ Usage:\n/broadcast -all/-users/-chats [-forward]")

    if not target_users and not target_chats:
        return await message.reply_text("⚠ No recipients found.")

    # Get content
    if message.reply_to_message:
        content = message.reply_to_message
    else:
        text = message.text
        for kw in ["/broadcast", "-forward", "-all", "-users", "-chats"]:
            text = text.replace(kw, "")
        text = text.strip()
        if not text:
            return await message.reply_text("📝 Provide a message or reply to one.")
        content = text

    total = len(target_users + target_chats)
    sent_users = 0
    sent_chats = 0
    failed = 0

    await message.reply_text(
        f"📢 <b>Broadcast Started</b>\n\n"
        f"➤ Mode: <code>{mode}</code>\n"
        f"👤 Users: <code>{len(target_users)}</code>\n"
        f"👥 Chats: <code>{len(target_chats)}</code>\n"
        f"📦 Total: <code>{total}</code>\n"
        f"⏳ Please wait while messages are being sent..."
    )

    async def deliver(chat_id, is_user, retries=1):
        nonlocal sent_users, sent_chats, failed
        async with SEMAPHORE:
            try:
                if isinstance(content, str):
                    await app.send_message(chat_id, content)
                elif mode == "forward":
                    await app.forward_messages(chat_id, message.chat.id, [content.id])
                else:
                    await content.copy(chat_id)
                if is_user:
                    sent_users += 1
                else:
                    sent_chats += 1
            except FloodWait as e:
                await asyncio.sleep(min(e.value, 60))
                if retries > 0:
                    return await deliver(chat_id, is_user, retries - 1)
                failed += 1
            except RPCError:
                failed += 1
            except Exception:
                failed += 1

    targets = [(uid, True) for uid in target_users] + [(cid, False) for cid in target_chats]
    for i in range(0, len(targets), 100):
        batch = targets[i:i + 100]
        await asyncio.gather(*[deliver(chat_id, is_user) for chat_id, is_user in batch])
        await asyncio.sleep(1.5)

    await message.reply_text(
        f"✅ <b>Broadcast Completed</b>\n\n"
        f"➤ Mode: <code>{mode}</code>\n"
        f"👤 Users Sent: <code>{sent_users}</code>\n"
        f"👥 Chats Sent: <code>{sent_chats}</code>\n"
        f"📦 Total Delivered: <code>{sent_users + sent_chats}</code>\n"
        f"❌ Failed: <code>{failed}</code>"
    )


async def auto_clean():
    while True:
        await asyncio.sleep(10)
        try:
            chats = await get_active_chats()
            for chat_id in chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []

                # use the proper enum here 👇
                async for member in app.get_chat_members(
                    chat_id, filter=ChatMembersFilter.ADMINISTRATORS
                ):
                    # some admins may not have .privileges (older Telegram versions)
                    if getattr(member, "privileges", None) and member.privileges.can_manage_video_chats:
                        adminlist[chat_id].append(member.user.id)

                # add authorised helper‑users
                for username in await get_authuser_names(chat_id):
                    user_id = await alpha_to_int(username)
                    adminlist[chat_id].append(user_id)

        except Exception as e:
            logger.warning(f"AutoClean error: {e}")
