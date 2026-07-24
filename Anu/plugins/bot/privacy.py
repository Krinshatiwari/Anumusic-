# Powered By Team Krishna_bots

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

from Anu import app
import config


TEXT = f"""
🔒 **Privacy Policy for {app.mention}**

We value your privacy and are committed to protecting your personal information when you use our Telegram voice chat player bot.

**What Data We Collect:**
We do **not** collect or store any personal data such as your name, phone number, messages, or media.

**How We Use Your Data:**
Your interaction (like commands or voice activity) remains confidential and is only used to provide requested services.

**Data Sharing and Selling:**
We do **not** share, sell, or distribute any information. Your data remains completely private.

**Security Measures:**
Our bot operates under Telegram’s secure infrastructure, with no external data logging.

**Your Control:**
You're free to remove the bot or revoke access anytime.

**Updates to this Policy:**
This policy may be updated. We recommend reviewing it periodically.

📎 **Full Privacy Document**: [View Here](https://telegra.ph/Privacy-Policy-Bot-Hub-12-18-2)

---

🤖 Powered with ❤️ by **Team krishna_bots** – committed to open, safe, and secure bot experiences.
"""

# 📍 Privacy Command Handler
@app.on_message(filters.command("privacy"))
async def privacy(client, message: Message):
  
    # 💬 Reply with UI and text
    await message.reply_text(
        TEXT,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )
