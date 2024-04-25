class script(object):  
    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {}(<code>{}</code>)
◉ ᴍᴇᴍʙᴇʀꜱ: {}
◉ ᴀᴅᴅᴇᴅ ʙʏ: {}"""
    
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}"""

    START_TXT = """Hᴇʟʟᴏ {}.
Mʏ Nᴀᴍᴇ Is <a href=https://t.me/{}>{}</a>. ɪ ᴀᴍ ᴀ sᴘᴇᴄɪᴀʟ ʙᴏᴛ"""

    HELP_TXT = """Hᴇʀᴇ ɪs Mʏ Hᴇʟᴩ.
ᴄʟɪᴄᴋ ᴛʜɪs /support"""

    ABOUT_TXT = """<b>✯ Mʏ ɴᴀᴍᴇ ɪs {} </>
✯ Dᴇᴠᴇʟᴏᴩᴇʀ: <a href='https://t.me/MrTG_Coder'>ᴍʀ.ʙᴏᴛ ᴛɢ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ Mʏ Sᴇʀᴠᴇʀ: <a href='https://www.render.com'>ʀᴇɴᴅᴇʀ </a>
✯ Pʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: ᴠ2.0.30
✯ Mʏ ᴠᴇʀsɪᴏɴ: ᴠ2.0"""

    STATUS_TXT =  """<b>◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code></b>
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>"""

    REPORT_MSG = """ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs"""

    REPORT_TXT = """@admins, @admins, /report. ғᴏʀ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs(ᴡᴏʀᴋ ᴏɴʟʏ ɪɴ  ɢʀᴏᴜᴘ)"""

    REQUEST_ACCEPT_TXT = """ʜᴇʏ {}\n ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴘᴛ ᴛᴏ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴛʜɪs ᴠɪᴅᴇᴏ ʜᴏᴡ ᴛᴏ sᴇᴛ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ʟɪᴋᴇ ʀᴇǫᴜᴇsᴛ ᴍᴇᴛʜᴏᴅ  https://t.me/TelegramTips/304
ᴄʀᴇᴅɪᴛs @MrTG_Coder"""

    BASE_TXT = """ʜᴇʏ {}\n/id - This command retrieves information about the user who sent the message. In private chats, it provides details like first name, last name, username, ID, data center ID, verification status, etc. In groupsorsupergroups, if it's a reply to a message, it gives details about the replied-to user. Otherwise, it provides the group name and ID.
/users- This command retrieves a list of all users stored in the bot's database. It displays the user's name, ID, and a link to their Telegram profile. It also indicates if the user is banned.
/chats (admin only) - This command retrieves a list of all chats stored in the bot's database. It shows the chat title, ID, and indicates if the chat is disabled.
/stats - This command displays statistics about the bot's usage. It shows the total number of users, total chats, and the size of the database.
/broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssɢᴇ.
/group_broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssɢᴇ ᴛᴏ ɢʀᴏᴜᴘs.
/group_broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssɢᴇ ᴛᴏ ɢʀᴏᴜᴘs."""
