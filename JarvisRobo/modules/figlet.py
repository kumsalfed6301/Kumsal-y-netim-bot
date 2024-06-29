pyrogram içe aktarma filtrelerinden
asyncio'yu içe aktar
pyfiglet'i içe aktar 
rastgele içe aktarma olanağından
pyrogram.types'ten içe aktar InlineKeyboardButton, InlineKeyboardMarkup, Mesaj, CallbackQuery
pyrogram.handler'lardan içe aktar MesajHandler 
from .. pbot'u İstemci olarak içe aktar
def figle(text):
x = pyfiglet.FigletFont.getFonts()
font = seçim(x)
figled = str(pyfiglet.figlet_format(text) ,font=font))
klavye = InlineKeyboardMarkup([ [InlineKeyboardButton(text = "ᴄʜᴀɴɢᴇ", callback_data = "figlet"), InlineKeyboardButton (text = "ᴄʟᴏsᴇ", callback_data = "close_reply")])
return dosyalandı, klavye

@Client.on_message(filters.command("figlet"))
async def echo(bot, message):
global text
try:
text = message.text.split(' ' ,1)[1]
IndexError hariç:
return wait message.reply_text("Örnek:\n\n`/figlet Jarvis`")
kul_text, klavye = figle(text)
wait message.reply_text( f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ғɪɢʟᴇᴛ :\n<pre> {kul_text</pre>", quote=True, answer_markup=keyboard)

@Client.on_callback_query(filters.regex("figlet"))
async def figlet_handler(İstemci, sorgu: CallbackQuery):
deneyin:
kul_text, klavye = figle(metin)
wait query.message.edit_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ғɪɢʟᴇᴛ :\n<pre>{kul_text</pre> ", answer_markup=keyboard)
İstisna hariç e olarak: 
wait message.reply(e)
__mod_name__ = "🔱istisna🔱" 
__help__="""
❍ /figlet*:* ᴍᴀᴋᴇs ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛ ᴇxᴛ 
Örnek:\n\n` / Figlet Jarvis`"""