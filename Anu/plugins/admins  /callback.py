# Powered By Team krishna_bots

import asyncio

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Anu import YouTube, app
from Anu.core.call import Anony
from Anu.misc import SUDOERS, db
from Anu.utils.database import (
    get_active_chats,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_music_playing,
    is_nonadmin_chat,
    music_off,
    music_on,
    set_loop,
)
from Anu.utils.decorators.language import languageCB
from Anu.utils.formatters import seconds_to_min
from Anu.utils.inline import close_markup, stream_markup, stream_markup_timer
from Anu.utils.stream.autoclear import auto_clean
from Anu.utils.thumbnails import get_thumb
from config import (
    BANNED_USERS,
    SOUNCLOUD_IMG_URL,
    STREAM_IMG_URL,
    TELEGRAM_AUDIO_URL,
    TELEGRAM_VIDEO_URL,
    adminlist,
    confirmer,
    votemode,
)
from strings import get_string

checker = {}
upvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")

    chat_id = int(chat)
    mention = CallbackQuery.from_user.mention

    # ================= AUTOPLAY ADDED =================
    if command == "Autoplay":
        await CallbackQuery.answer()

        state = db.get(f"autoplay_{chat_id}", False)

        if state:
            db[f"autoplay_{chat_id}"] = False
            return await CallbackQuery.message.reply_text(
                f"➻ Autoplay Disabled ❌\n│ \n└ʙʏ : {mention} 🥀",
                reply_markup=close_markup(_),
            )
        else:
            db[f"autoplay_{chat_id}"] = True
            return await CallbackQuery.message.reply_text(
                f"➻ Autoplay Enabled ⚡\n│ \n└ʙʏ : {mention} 🥀",
                reply_markup=close_markup(_),
            )
    # =================================================

    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)

    # ========= EXISTING CODE SAME =========

    if command == "Pause":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(_["admin_1"], show_alert=True)
        await CallbackQuery.answer()
        await music_off(chat_id)
        await Anony.pause_stream(chat_id)

    elif command == "Resume":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(_["admin_3"], show_alert=True)
        await CallbackQuery.answer()
        await music_on(chat_id)
        await Anony.resume_stream(chat_id)

    elif command == "Stop":
        await CallbackQuery.answer()
        await Anony.stop_stream(chat_id)
        await set_loop(chat_id, 0)

    elif command == "Skip":
        check = db.get(chat_id)

        # 🔥 AUTOPLAY LOGIC HERE
        if db.get(f"autoplay_{chat_id}", False):
            try:
                current = check[0]["title"]
                search = f"{current} next song"
                results = await YouTube.search(search, limit=1)

                if results:
                    videoid = results[0]["id"]
                    link, _ = await YouTube.video(videoid)

                    await Anony.skip_stream(chat_id, link)

                    return await CallbackQuery.message.reply_text(
                        f"⚡ Autoplay Next Song Playing...",
                        reply_markup=close_markup(_),
                    )
            except:
                pass

    # ========= REST SAME =========


async def markup_timer():
    while not await asyncio.sleep(7):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            try:
                if not await is_music_playing(chat_id):
                    continue
                playing = db.get(chat_id)
                if not playing:
                    continue
                duration_seconds = int(playing[0]["seconds"])
                if duration_seconds == 0:
                    continue
                mystic = playing[0]["mystic"]

                language = await get_lang(chat_id)
                _ = get_string(language)

                buttons = stream_markup_timer(
                    _,
                    chat_id,
                    seconds_to_min(playing[0]["played"]),
                    playing[0]["dur"],
                )
                await mystic.edit_reply_markup(
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                continue


asyncio.create_task(markup_timer())
