HELP_1 = """<b><u>𝖠𝖣𝖬𝖨𝖭 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲</u></b> 🎵

💬 𝖳𝗂𝗉: To control music in a channel, just add <b>𝖼</b> at the beginning of the command.  
Example: <code>/cpause</code>

🎯 <b>/pause</b> – Pause the current playing stream.  
🎯 <b>/resume</b> – Resume the paused stream.  
🎯 <b>/skip</b> – Skip the current track and play the next one in queue.  
🎯 <b>/end</b> or <b>/stop</b> – Clear the queue and stop the stream.  
🎯 <b>/player</b> – Display an interactive player panel.  
🎯 <b>/queue</b> – Show the list of queued tracks.
"""

HELP_2 = """
<b><u>𝖠𝖴𝖳𝖧 𝖴𝖲𝖤𝖱𝖲</u></b> 🛡

👥 <b>Auth users</b> can use admin-level commands in the bot <i>without</i> being actual chat admins.

🔐 <b>/auth [username/user_id]</b> – Add a user to the bot's auth list.  
🔐 <b>/unauth [username/user_id]</b> – Remove a user from the auth list.  
🔐 <b>/authusers</b> – Show the list of currently authorized users in the group.
"""

HELP_4 = """
<b><u>𝖢𝖧𝖠𝖳 𝖡𝖫𝖠𝖢𝖪𝖫𝖨𝖲𝖳</u></b> 🔒 [Sudo Users Only]

🧱 <b>Restrict unwanted or abusive chats</b> from accessing the bot to keep it safe and focused.

🚫 <b>/blacklistchat [chat_id]</b> – Blacklist a chat from using the bot.  
🚫 <b>/whitelistchat [chat_id]</b> – Remove a chat from the blacklist.  
🚫 <b>/blacklistedchat</b> – Display the list of currently blacklisted chats.

⚠️ Use responsibly. This feature is powerful and meant for protection.
"""

HELP_5 = """
<b><u>𝖡𝖫𝖮𝖢𝖪 𝖴𝖲𝖤𝖱𝖲</u></b> 🧨 [Sudo Users Only]

🙅 <b>Block users from interacting with the bot commands entirely.</b> This helps prevent spam or misuse.

🚫 <b>/block [username | reply]</b> – Block a user from using the bot.  
🚫 <b>/unblock [username | reply]</b> – Unblock a previously blocked user.  
🚫 <b>/blockedusers</b> – Show the list of all blocked users.

⚠️ <i>Blocked users will be ignored completely by the bot.</i>
"""

HELP_6 = """
<b><u>𝖢𝖧𝖠𝖭𝖭𝖤𝖫 𝖯𝖫𝖠𝖸</u></b> 📺

🎤 <b>Stream audio or video directly in your connected channel's video chat!</b>

📼 <b>/cplay</b> – Start streaming the requested <b>audio</b> track in the channel.  
📼 <b>/cvplay</b> – Start streaming the requested <b>video</b> track in the channel.  
📼 <b>/cplayforce</b> or <b>/cvplayforce</b> – Forcefully stop the current stream and play a new audio/video track.

🛰 <b>/channelplay [chat username or ID]</b> – Connect a channel to the group and control playback from the group itself.  
❎ <b>/channelplay disable</b> – Disconnect the linked channel.

<i>➤ Make sure the bot has required permissions and is an admin in both the group</i>
"""

HELP_7 = """
<b><u>𝖠𝖢𝖳𝖨𝖵𝖤 𝖢𝖠𝖫𝖫𝖲</u></b> 🎙 [Sudo Users Only]

🎚 <b>Monitor all active voice and video streams across the bot's network.</b>

📞 <b>/activecalls</b> or <b>/acalls</b> – Shows a complete list of ongoing voice/video calls across all groups where the bot is active.

🧠 <i>This command helps you keep track of live streams handled by the bot in real-time.</i>
"""

HELP_8 = """
<b><u>𝖫𝖮𝖮𝖯 𝖲𝖳𝖱𝖤𝖠𝖬</u></b> 🔂

🔄 <b>Loop the currently playing stream automatically.</b>

Use this to play the same track multiple times without re-queuing it manually.

⏺ <b>/loop enable</b> – Enable looping for the ongoing stream.  
⏹ <b>/loop disable</b> – Disable the loop and continue normally.  
🎯 <b>/loop [1, 2, 3, ...]</b> – Set a custom number of times to loop the current stream.

📝 <i>Helpful when you want to replay a specific song multiple times during a session.</i>
"""

HELP_9 = """
<b><u>𝖬𝖠𝖨𝖭𝖳𝖤𝖭𝖠𝖭𝖢𝖤 𝖬𝖮𝖣𝖤</u></b> 🧰 [Sudo Users Only]

🧑‍🔧 <b>Essential tools for bot management and debugging.</b>

📂 <b>/logs</b> – Fetch the latest logs from your bot’s system for debugging or review.

📍 <b>/logger [enable/disable]</b> – Turn on or off activity logging.

🚧 <b>/maintenance [enable/disable]</b> – Switch the bot to maintenance mode.  
  • In this mode, the bot will stop responding to commands in user chats.  
  • Useful when performing updates or backend fixes.

📝 <i>Only authorized sudoers should use these powerful administrative controls.</i>
"""

HELP_10 = """
<b><u>𝖯𝖨𝖭𝖦 & 𝖲𝖳𝖠𝖳𝖲</u></b> 🖥

🔍 <b>Monitor the bot's performance and get quick access to system status.</b>

🆗 /start – Initiates the music bot and verifies if it's active in the chat.  
📖 /help – Opens the full help menu.  
📶 /ping – Shows ping and system info.  
📊 /stats – Shows uptime, usage, and system info.

🧩 <i>Use these commands to ensure everything is running smoothly or to debug latency issues.</i>
"""

HELP_11 = """
<b><u>𝖯𝖫𝖠𝖸 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲</u></b> 🎼

🎥 <b>v</b> = Play in video mode  
🚨 <b>force</b> = Force play (interrupts current stream)

🎧 <b>/play</b> or <b>/vplay</b> – Stream requested track in audio or video.  
⏭ <b>/playforce</b> or <b>/vplayforce</b> – Force play a new track.

📝 <i>Use force play responsibly — it will disrupt what's currently playing.</i>
"""

HELP_12 = """
<b><u>𝖲𝖧𝖴𝖥𝖥𝖫𝖤 𝖰𝖴𝖤𝖴𝖤</u></b> 🎲

🔃 <b>/shuffle</b> – Randomly reshuffles the current queue of tracks.  
📜 <b>/queue</b> – Displays the current shuffled queue.

✨ <i>Use shuffle to surprise your audience or break the monotony of the playlist!</i>
"""

HELP_13 = """
<b><u>𝖲𝖤𝖤𝖪 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲</u></b> ⏭

⏩ <b>/seek [seconds]</b> – Jump forward in the stream.  
⏪ <b>/seekback [seconds]</b> – Rewind the stream.

⚠️ <i>Only works if the media source supports it.</i>
"""

HELP_14 = """
<b><u>𝖡𝖱𝖮𝖠𝖣𝖢𝖠𝖲𝖳 𝖥𝖤𝖠𝖳𝖴𝖱𝖤</u></b> 📣 [Only for Sudo Users]

📝 <b>/broadcast [message or reply]</b> – Send messages to users or chats.

Broadcast Modes:  
📩 -forward – Forward message  
👥 -users – Send to users  
💬 -chats – Send to groups  
🌍 -all – Send everywhere

📌 Example:  
<code>/broadcast -all -forward Hello</code>

📟 <b>/status</b> – Show broadcast progress/status.

⚠️ <i>Don’t spam! Telegram may limit your bot.</i>
"""

HELP_15 = """
<b><u>𝖲𝖯𝖤𝖤𝖣 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲</u></b> 🚀 [Admins Only]

⏱ <b>/speed</b> or <b>/playback</b> – Set stream speed.  
🎛 <b>/cspeed</b> or <b>/cplayback</b> – Channel speed control.

Available Speeds:  
▫️ 0.5x – Slow  
▫️ 1x – Normal  
▫️ 1.5x – Fast  
▫️ 2x – Very Fast

📌 Example:  
<code>/speed 1.5</code>

⚠️ <i>Not all sources support speed control.</i>
"""
