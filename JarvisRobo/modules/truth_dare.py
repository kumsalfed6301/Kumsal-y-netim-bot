import requests
from telegram import Update
from telegram.ext import CallbackContext
from MukeshAPI import api 
from JarvisRobo import dispatcher
from JarvisRobo.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    truth =api.truth()
    update.effective_message.reply_text(truth)


def dare(update: Update, context: CallbackContext):
    dare =api.dare()
    update.effective_message.reply_text(dare)

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
"""
__mod_name__ = "🔱Tʀᴜᴛʜ-Dᴀʀᴇ🔱"
