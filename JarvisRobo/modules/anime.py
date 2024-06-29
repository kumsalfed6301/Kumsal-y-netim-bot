json'u içeri aktar
rastgele içe aktar

istekleri içe aktar
telegramdan içe aktar InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
telegram.ext'ten CallbackContext, CallbackQueryHandler'ı içeri aktarma

JarvisRobo transfer aktarma dağıtıcısından,OWNER_ID
JarvisRobo.modules'dan .disable import DisableAbleCommandHandler


def anime_quote():
url = "https://animechan.vercel.app/api/random"
çünkü metin özellikleri dize gibi bir sözlük döndürmek için
yanıt = request.get (url)
deneyin:
dic = json.loads(response.text)
hariç İstisna:
pass
quote = dic["alıntı"]
karakter = dic["karakter"]
anime = dic["anime"]
return alıntı, karakter, anime


def tırnak tırnakları(güncelleme: Güncelleme, bağlama: Geri Arama Bağlamı):
mesaj = güncelleme.etkili_message
alıntı, karakter, anime = anime_quote( )
msg = f"<i>❝{alıntı}❞</i>\n\n<b>{karakter} {anime</b> 'den"
klavye = InlineKeyboardMarkup(
[[InlineKeyboardButton( text = "Değiştir🔁", callback_data = "change_quote")]]
)
message.reply_text(
msg,
answer_markup=klavye,
parse_mode=ParseMode.HTML,
)


def change_quote(update: Update, context: CallbackContext):
update.callback_query
update.active_chat
mesaj = update.active_message
alıntı, karakter , anime = anime_quote()
msg = f"<i> ❝{quote}❞</i>\n\n<b>{karakter} {anime</b>'den"
klavye = InlineKeyboardMarkup(
[[InlineKeyboardButton(text = "ᴄʜᴀɴɢᴇ🔁", callback_data = ") quote_change")]]
)
message.edit_text(msg, answer_markup=klavye, parse_mode=ParseMode.HTML)


def animequotes (güncelleme: Güncelleme, bağlama: CallbackContext):
mesaj = update. etkili_message
message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
answer_photo = (
message.reply_to_message.reply_photo
if message.reply_to_message
else message.reply_photo
)
answer_photo (random.choice(QUOTES_IMG))


QUOTES_IMG = (
"https://i.imgur.com/Iub4RYj.jpg",
"https://i.imgur.com/uvNMdIl. jpg",
"https://i.imgur.com/YOBOntg.jpg",
"https://i.imgur.com/fFpO2ZQ.jpg",
"https://i.imgur. com/fxZceK.jpg",
"https://i.imgur.com/RlVcCip.jpg",
"https://i.imgur.com/CjpqLRF.jpg",
"https:// i.imgur.com/8BHZDk6.jpg",
"https://i.imgur.com/8bHeMgy.jpg",
"https://i.imgur.com/5K3lMvr.jpg",
" https://i.imgur.com/NTzw4RN.jpg",
"https://i.imgur.com/wJxryAn.jpg",
"https://i.imgur.com/9LDWzC.jpg" ,
"https://i.imgur.com/sBe8TTs.jpg",
"https://i.imgur.com/1Au8gdf.jpg",
"https://i.imgur.com/ 28hFQeU.jpg",
"https://i.imgur.com/Qvc3JY.jpg",
"https://i.imgur.com/gSX6Xlf.jpg",
"https://i. imgur.com/iP26Hwa.jpg",
"https://i.imgur.com/uSsJoX8.jpg",
"https://i.imgur.com/OvX3oHB.jpg",
"https: //i.imgur.com/JMWuksm.jpg",
"https://i.imgur.com/lhM3fib.jpg",
"https://i.imgur.com/64IYKkw.jpg",
"https://i.imgur.com/nMbyA3J.jpg",
"https://i.imgur.com/7KFQhY3.jpg",
"https://i.imgur.com/mlKb7zt. jpg",
"https://i.imgur.com/JCQGJVw.jpg",
"https://i.imgur.com/hSFYDEz.jpg",
"https://i.imgur. com/PQRjAgl.jpg",
"https://i.imgur.com/ot9624U.jpg",
"https://i.imgur.com/iXmqN9y.jpg",
"https:// i.imgur.com/RhNBeGr.jpg",
"https://i.imgur.com/tcMVNa8.jpg",
"https://i.imgur.com/LrVg81.jpg",
" https://i.imgur.com/TcWfQlz.jpg",
"https://i.imgur.com/muAUdvJ.jpg",
"https://i.imgur.com/AtC7ZRV.jpg" ,
"https://i.imgur.com/sCObQCQ.jpg",
"https://i.imgur.com/AJFDI1r.jpg",
"https://i.imgur.com/ TCgmRrH.jpg",
"https://i.imgur.com/LMdmhJU.jpg",
"https://i.imgur.com/eyyaxN.jpg",
"https://i. imgur.com/YtYxV66.jpg",
"https://i.imgur.com/292w4ye.jpg",
"https://i.imgur.com/6Fm1vdw.jpg",
"https: //i.imgur.com/2vnBOZd.jpg",
"https://i.imgur.com/j5hI9Eb.jpg",
"https://i.imgur.com/cAv7pJB.jpg",
"https://i.imgur.com/jvI7Vil.jpg",
"https://i.imgur.com/fANpjsg.jpg",
"https://i.imgur.com/5o1SJyo. jpg",
"https://i.imgur.com/dSVxmh8.jpg",
"https://i.imgur.com/2dXlAD.jpg",
"https://i.imgur. com/htvIoGY.jpg",
"https://i.imgur.com/hy6BXOj.jpg",
"https://i.imgur.com/OuwzNYu.jpg",
"https:// i.imgur.com/L8vwvc2.jpg",
"https://i.imgur.com/3VMVF9y.jpg",
"https://i.imgur.com/yzjq2n2.jpg",
" https://i.imgur.com/qK7TAN.jpg",
"https://i.imgur.com/zvcxSOX.jpg",
"https://i.imgur.com/FO7bApW.jpg" ,
"https://i.imgur.com/KK6gwg.jpg",
"https://i.imgur.com/6lG4tsO.jpg",
)

ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes) ) ", animequotes)
QUOTES_HANDLER = DisableAbleCommandHandler("alıntı", tırnak sembolleri)

CHANGE_QUOTE = CallbackQueryHandler(değişim_quote, desen=r"değişim_.*")
QUOTE_CHANGE = CallbackQueryHandler(değişim_quote, desen=r"quote_ .* ")

dispatcher.add_handler(CHANGE_QUOTE)
dispatcher.add_handler(QUOTE_CHANGE)
dispatcher.add_handler(ANIMEQUOTES_HANDLER)
dispatcher.add_handler(QUOTES_HANDLER)

__mod_name__ = "🔱alıntılar🔱 "
__help__ = "" "
/quote : ᴡʀɪᴛᴇ alıntılar
/animequotes : ᴡʀɪᴛᴇ ᴀɴɪᴍᴇǫᴜᴏᴛᴇs
"""

__command_list__ = [
"animequotes",
"alıntı ",
]

__işleyiciler__ = [
ANIMEQUOTES_HANDLER,
QUOTES_HANDLER,
] 