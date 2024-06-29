html'yi içe aktar

telegramdan içe aktar InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
telegram.error'dan içe aktar BadRequest
telegram.ext'ten içe CallbackContext, CallbackQueryHandler
telegram.utils.helpers'tan içe bahset_html

JarvisRobo'yu içe aktar .modules.sql.approve_sql as sql
JarvisRobo'dan DRAGONS'u içe aktarın, dağıtıcı
JarvisRobo.modules.disable'dan içe aktar DisableAbleCommandHandler
JarvisRobo.modules.helper_funcs.chat_status'tan içe aktar user_admin
JarvisRobo.modules.helper_funcs.extraction'dan import extract_user 
JarvisRobo.modules.log_channel'den içe aktarma günlüğe kaydedilebilir


@loggable
@user_admin
def onaylama(güncelleme, bağlam):
mesaj = update.active_message
chat_title = mesaj.chat.title
sohbet = update.active_chat
args = context.args
user = update.active_user
user_id = extract_user(mesaj, args)
if değilse user_id:
message.reply_text(
"Kim olduğunu bilmiyorum bahsettiğiniz şey, bir kullanıcı belirtmeniz gerekecek!"
)
return ""
deneyin:
üye = chat.get_member(user_id)
hariç BadRequest:
return "" 
if member.status == "yönetici" veya member.status == "yaratıcı":
message.reply_text(
"Kullanıcı zaten yönetici kilitleri, engelleme listeleri ve antiflood bunlar için zaten geçerli değil."
)
return ""
if sql.is_approved(message.chat_id, user_id):
message.reply_text(
f"[{member.user['first_name']}](tg://user? id={member.user['id']}) zaten {chat_title}'da onaylandı",
parse_mode=ParseMode.MARKDOWN,
)
return ""
sql.approve(message.chat_id, user_id) 
message.reply_text(
f"[{member.user['first_name']}](tg://user?id={member.user['id']}) {chat_title}'da onaylandı! Bunlar artık kilitleme, engelleme listeleri ve taşkın önleme gibi otomatik yönetici eylemleri tarafından göz ardı edilecek.",
parse_mode=ParseMode.MARKDOWN,
)
log_message = (
f"<b>{html.escape(chat.title) )}:</b>\n"
f"ONAYLANDI\n"
f"<b>Yönetici:</b> {mention_html(user.id, user.first_name)}\n"
f" <b>Kullanıcı:</b> {mention_html(member.user.id, member.user.first_name)}"
)

return log_message


@loggable
@user_admin
def onaylamama(güncelleme, bağlam):
mesaj = güncelleme.etkin_message
chat_title = mesaj.chat.title
sohbet = güncelleme.etkili_sohbet
args = bağlam.args
kullanıcı = güncelleme.etkili_kullanıcı
user_id = extract_user( message, args)
if not user_id:
message.reply_text(
"Kimden bahsettiğinizi bilmiyorum, bir kullanıcı belirtmeniz gerekecek!"
)
return " "
deneyin:
üye = chat.get_member(user_id)
BadRequest hariç:
return ""
if member.status == "yönetici" veya member.status == "yaratıcı":
mesaj. answer_text("Bu kullanıcı bir yöneticidir, onaylanmamış olamaz.")
return ""
değilse sql.is_approved(message.chat_id, user_id):
message.reply_text(f"{member.user ['first_name']} henüz onaylanmadı!")
return ""
sql.disapprove(message.chat_id, user_id)
message.reply_text(
f"{member.user['first_name'] } artık {chat_title} içinde onaylanmıyor."
)
log_message = (
f"<b>{html.escape(chat.title)}:</b>\n"
f"UNAPPROVED\ n"
f"<b>Yönetici:</b> {mention_html(user.id, user.first_name)}\n"
f"<b>Kullanıcı:</b> {mention_html(member.user. id, member.user.first_name)}"
)

return log_message


@user_admin
def onaylı(güncelleme, bağlam):
mesaj = güncelleme.etkili_mesaj
chat_title = mesaj. chat.title
chat = update.active_chat
msg = "Aşağıdaki kullanıcılar onaylandı.\n"
onaylanmış_kullanıcılar = sql.list_approved(message.chat_id)
for i,onaylanmış_kullanıcılarda:
üye = chat.get_member (int(i.user_id))
msg = f" `{i.user_id}`: {member.user['first_name']}\n"
if msg.endswith("approved.\n"): 
message.reply_text(f"{chat_title}'da hiçbir kullanıcı onaylanmadı.")
return ""
else:
message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)


@user_admin 
def onayı(güncelleme, bağlam):
mesaj = güncelleme.etkili_mesaj
sohbet = güncelleme.etkili_sohbet
args = bağlam.args
user_id = extract_user(mesaj, args)
üye = chat.get_member(int) (user_id))
if not user_id:
message.reply_text(
"Kimden bahsettiğinizi bilmiyorum, bir kullanıcı belirtmeniz gerekecek!"
)
return " "
if sql.is_approved(message.chat_id, user_id):
message.reply_text(
f"{member.user['first_name']} onaylı bir kullanıcıdır. Kilitler, taşkın önleme ve engelleme listeleri bunlara uygulanmaz."
)
else:
message.reply_text(
f"{member.user['first_name']} onaylı bir kullanıcı değil. Etkileniyorlar normal komutlarla."
)


def unapproveall(update: Update, context: CallbackContext):
chat = update.active_chat
user = update.active_user
üye = chat.get_member(user. id)
if member.status != "yaratıcı" ve user.id EJDERHALAR'da değil:
update.active_message.reply_text(
"Yalnızca sohbet sahibi tüm kullanıcıların onayını aynı anda iptal edebilir."
)
else :
düğmeler = InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=Tüm kullanıcıların onayını kaldır", callback_data=unapproveall_user"
)
],
[
InlineKeyboardButton(
text= "İptal", callback_data="unapproveall_cancel"
)
],
]
)
update.active_message.reply_text(
f"{chat.title} alanındaki TÜM kullanıcıların onayını kaldırmak istediğinizden emin misiniz? ? Bu eylem geri alınamaz.",
answer_markup=buttons,
parse_mode=ParseMode.MARKDOWN,
)


def unapproveall_btn(update: Update, context: CallbackContext):
query = update.callback_query 
sohbet = update.active_chat
mesaj = update.active_message
üye = chat.get_member(query.from_user.id)
if query.data == "unapproveall_user":
if member.status == "yaratıcı " veya EJDERHALAR'da query.from_user.id:
onaylanmış_kullanıcılar = sql.list_approved(chat.id)
kullanıcılar = [int(i.user_id) for i in onaylanmış_users]
for user_id in kullanıcılar:
sql.disapprove (chat.id, user_id)

if member.status == "yönetici":
query.answer("Bunu yalnızca sohbetin sahibi yapabilir.")

if member.status == " member":
query.answer("Bunu yapmak için yönetici olmanız gerekir.")
elif query.data == "unapproveall_cancel":
if member.status == "yaratıcı" veya query.from_user.id EJDERHALAR'da:
message.edit_text("Tüm onaylı kullanıcıların kaldırılması iptal edildi.")
return ""
if member.status == "yönetici":
query.answer("Sohbetin yalnızca sahibi bunu yapabilir.")
if member.status == "üye":
query.answer("Bunu yapmak için yönetici olmanız gerekir.")


__help__ = """~sᴏᴍᴇᴛɪᴍᴇs , ʏᴏᴜ ᴍɪɢʜᴛ ᴛʀᴜsᴛ ᴀ ᴜsᴇʀ ɴᴏᴛ ᴛᴏ sᴇɴᴅ ᴜɴᴡᴀɴᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ.
ᴍᴀʏʙᴇ ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇᴍ ᴀᴅᴍɪɴ, ʙᴜᴛ ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ᴏᴋ ᴡɪᴛʜ ʟᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ɴᴏᴛ ᴀᴘᴘʟʏɪɴɢ ᴛʜᴇᴍ.

ᴛʜᴀᴛ's ᴡʜᴀᴛ ᴀᴘᴘʀᴏᴠᴀʟs ᴀʀᴇ ғᴏʀ ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴛʀᴜsᴛᴡᴏʀᴛʜʏ ᴜsᴇʀs ᴛᴏ ᴀʟʟᴏᴡ ᴛʜᴇᴍ ᴛᴏ sᴇɴᴅ 

*ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀ ɴᴅs:*
❍ /approval*:* ᴄʜᴇᴄᴋ ᴀ ᴜsᴇʀ'nin ᴀᴘᴘʀᴏᴠᴀʟ sᴛᴀᴛᴜs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.
❍ /approve *:* ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜsᴇʀ. ʟᴏᴄᴋ'ler, ʙʟᴀᴄᴋʟɪsᴛ'ler, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴡᴏɴ'ᴛ ᴀᴘᴘʟʏ ᴛᴏ ᴛʜᴇᴍ ᴀɴ ʏᴍᴏʀᴇ.
❍ /unapprove *:* ᴜɴᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜsᴇʀ. ᴛʜᴇʏ ᴡɪʟʟ ɴᴏᴡ ʙᴇ sᴜʙᴊᴇᴄᴛ ᴛᴏ ʟᴏᴄᴋ'ler, ʙʟᴀᴄᴋʟɪsᴛ'ler, ᴀɴᴅ ᴀɴᴛɪғ ʟᴏᴏᴅ ᴀɢᴀɪɴ.
❍ /onaylandı *:* ʟɪsᴛ ᴀʟʟ ᴀᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀs.
❍ /onaylanmadı *:* ᴜɴᴀᴘᴘʀᴏ ᴠᴇ *ᴀʟʟ* ᴜsᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ. ᴛʜɪs ᴄᴀɴɴᴏᴛ ʙᴇ ᴜɴᴅᴏɴᴇ.
"""

APPROVE = DisableAbleCommandHandler("onayla", onayla, run_async=True)
DISAPPROVE = DisableAbleCommandHandler("onaylama", onaylama, çalıştır _async=Doğru)
ONAYLANDI = DisableAbleCommandHandler( "onaylandı", onaylandı, run_async=True)
APPROVAL = DisableAbleCommandHandler("onay", onay, run_async=True)
UNAPPROVEALL = DisableAbleCommandHandler("unapproveall", unapproveall, run_async=True)
UNAPPROVEALL_BTN = CallbackQueryHandler(
unapproveall_btn, desen=r"unapproveall_.*", run_async=True
)

dispatcher.add_handler(ONAYLA)
dispatcher.add_handler(ONAYLAŞMA)
dispatcher.add_handler(ONAYLANDI)
dispatcher.add_handler(ONAY) )
dispatcher.add_handler(UNAPPROVEALL)
dispatcher.add_handler(UNAPPROVEALL_BTN)

__mod_name__ = "🔱onaylama🔱"
__command_list__ = ["onayla", "onaylamayı kaldır", "onaylandı", "onaylandı"]
__handlers__ = [ONAYLA, ONAYLAMADIN, ONAYLANDI, ONAYLANDI]