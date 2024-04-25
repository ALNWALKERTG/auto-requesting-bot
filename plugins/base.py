from pyrogram import Client as user, filters, enums
from pyrogram.types import Message

@Client.on_message(filters.command("id",prefixes="."))
async def id_handler(client, message:Message):
      chat_type = message.chat.type
      if chat_type in [enums.ChatType.PRIVATE]:
          if message.reply_to_message:
              user_id = message.reply_to_message.from_user.id
              first = message.reply_to_message.from_user.first_name
              last = message.reply_to_message.from_user.last_name or ""
              username = message.reply_to_message.from_user.username
              dc_id = message.reply_to_message.from_user.dc_id or ""
              fake = message.reply_to_message.from_user.is_fake
              bot = message.reply_to_message.from_user.is_bot
              scam = message.reply_to_message.from_user.is_scam
              upgrade = message.reply_to_message.from_user.is_premium
              verify = message.reply_to_message.from_user.is_verified
              online = message.reply_to_message.from_user.last_online_date or ""
              await message.reply_text(
                  f"<b>➲ ғɪʀsᴛ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last}\n<b>➲ ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}\n<b>➲ ɪᴅ:</b> <code>{user_id}</code>\n<b>➲ ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>\n➲ Is ғᴀᴋᴇ: {fake}\n➲ Is ʙᴏᴛ: {bot}\n➲ ɪs sᴄᴀᴍ: {scam}\n➲ Is ᴠᴇʀɪғɪᴇᴅ: {verify}\n➲ Is ᴘʀᴇᴍɪɴᴜᴍ: {upgrade}\n➲ Lᴀsᴛ ᴏɴʟɪɴᴇ ᴅᴀᴛᴇ: {online}" ,
                  quote=True)
          else:
              user_id = message.from_user.id
              first = message.from_user.first_name
              last = message.from_user.last_name or ""
              username = message.from_user.username
              dc_id = message.from_user.dc_id or ""
              fake = message.from_user.is_fake
              bot = message.from_user.is_bot
              scam = message.from_user.is_scam
              upgrade = message.from_user.is_premium
              verify = message.from_user.is_verified
              online = message.from_user.last_online_date or ""
              await message.reply_text(
                  f"<b>➲ ғɪʀsᴛ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last}\n<b>➲ ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}\n<b>➲ ɪᴅ:</b> <code>{user_id}</code>\n<b>➲ ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>\n➲ Is ғᴀᴋᴇ: {fake}\n➲ Is ʙᴏᴛ: {bot}\n➲ ɪs sᴄᴀᴍ: {scam}\n➲ Is ᴠᴇʀɪғɪᴇᴅ: {verify}\n➲ Is ᴘʀᴇᴍɪɴᴜᴍ: {upgrade}\n➲ Lᴀsᴛ ᴏɴʟɪɴᴇ ᴅᴀᴛᴇ: {online}" ,
                  quote=True)
      elif chat_type in [enums.ChatType.GROUP , enums.ChatType.SUPERGROUP]:
          if message.reply_to_message:
              user_id = message.reply_to_message.from_user.id
              first = message.reply_to_message.from_user.first_name
              last = message.reply_to_message.from_user.last_name or ""
              username = message.reply_to_message.from_user.username
              dc_id = message.reply_to_message.from_user.dc_id or ""
              fake = message.reply_to_message.from_user.is_fake
              bot = message.reply_to_message.from_user.is_bot
              scam = message.reply_to_message.from_user.is_scam
              upgrade = message.reply_to_message.from_user.is_premium
              verify = message.reply_to_message.from_user.is_verified
              online = message.reply_to_message.from_user.last_online_date or ""
              await message.reply_text(
                  f"<b>➲ ғɪʀsᴛ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last}\n<b>➲ ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}\n<b>➲ ɪᴅ:</b> <code>{user_id}</code>\n<b>➲ ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>\n➲ Is ғᴀᴋᴇ: {fake}\n➲ Is ʙᴏᴛ: {bot}\n➲ ɪs sᴄᴀᴍ: {scam}\n➲ Is ᴠᴇʀɪғɪᴇᴅ: {verify}\n➲ Is ᴘʀᴇᴍɪɴᴜᴍ: {upgrade}\n➲ Lᴀsᴛ ᴏɴʟɪɴᴇ ᴅᴀᴛᴇ: {online}" ,
                  quote=True)
          else:
            grp_id = message.chat.id
            first = message.chat.title
            await message.reply_text(
                f"<b>➲ ɢʀᴏᴜᴘ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ɢʀᴏᴜᴘ ɪᴅ:</b> {grp_id}\n" ,
                quote=True)
      else:
          grp_id = message.chat.id
          first = message.chat.title
          await message.reply_text(
              f"<b>➲ ɢʀᴏᴜᴘ ɴᴀᴍᴇ:</b> {first}\n<b>➲ ɢʀᴏᴜᴘ ɪᴅ:</b> {grp_id}\n" ,
              quote=True)

@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Getting List Of chats')
    chats = await db.get_all_chats()
    out = "Chats Saved In DB Are:\n\n"
    async for chat in chats:
        out += f"**Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Disabled Chat )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List Of Chats")

@Client.on_message(filters.command('stats'))
async def get_stats(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    total_chats = await db.total_chat_count()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)    
    await rju.edit(script.STATUS_TXT.format(total_users, total_chats))
