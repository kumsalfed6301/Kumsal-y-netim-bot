import secureme
from pyrogram import filters
from JarvisRobo import pbot as jarvis


@jarvis.on_message(filters.command("encrypt"))
async def encyrpt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/encyrpt India`")
    m = message.text.split(' ',1)[1]
    try:
        Secure = secureme.encrypt(m)
        
        await message.reply_text(f"`{Secure}`")
        

    except Exception as e:
        await message.reply_text(f"Error {e}")

@jarvis.on_message(filters.command("decrypt"))
async def decrypt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/decrypt Nsinf`")
    m = message.text.split(' ',1)[1]
    try:
        Decrypt = secureme.decrypt(m)
        
        await message.reply_text(f"`{Decrypt}`")
        

    except Exception as e:
        await message.reply_text(f"{e}")


__mod_name__ = "🔱şifreleme🔱"

__help__ = """
*ᴄᴏɴᴠᴇʀᴛs*
 ❍ /encrypt*:* ᴇɴᴄʀʏᴘᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 ❍ /decrypt*:* ᴅᴇᴄʀʏᴘᴛs ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 ❍ /encode*:* ᴇɴᴄᴏᴅᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 ❍ /decode*:* ᴅᴇᴄᴏᴅᴇ ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 ❍ /morseencode*:* Mᴏʀsᴇ Eɴᴄᴏᴅᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 ❍ /morsedecode*:* ᴅᴇᴄʀʏᴘᴛs ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 ❍ /password *:*  ɢɪᴠᴇ ʟᴇɴɢᴛʜ ᴏғ ᴘᴀssᴡᴏʀᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ
 ❍ /uselessfact *:* Gᴇɴᴇʀᴀᴛᴇ  Rᴀᴍᴅᴏᴍ Usᴇʟᴇss Fᴀᴄᴛ
"""
