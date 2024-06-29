import io
import os

değerlendirme için ortak içe aktarmalar
import textwrap
import traceback
from contextlib import direct_stdout

from telegram import ParseMode, Güncelleme
from telegram.ext import CallbackContext, CommandHandler

JarvisRobo'dan içe aktar LOGGER, dağıtıcı,OWNER_ID
JarvisRobo.modules.helper_funcs.chat_status'tan import dev_plus

namespaces = {}


def namespace_of(sohbet, güncelleme, bot):
if chat ad alanlarında değil:
ad alanları[sohbet] = {
"__builtins__": globals()["__builtins__"],
"bot": bot,
"etkili_message": update.tained_message,
"etkili_kullanıcı" : güncelleme.etkili_kullanıcı,
"etkili_sohbet": güncelleme.etkili_sohbet,
"güncelleme": güncelleme,
}

ad alanlarını döndür[sohbet]


def log_input(güncelleme):
kullanıcı = update.active_user.id
sohbet = update.active_chat.id
LOGGER.info(f"IN: {update.active_message.text} (user={user}, chat={chat})")~

~def send(msg, bot, update):
if len(str(msg)) > 2:
io.BytesIO(str.encode(msg)) ile out_file:
out_file.name = " çıktı.txt"
bot.send_document(chat_id=update.active_chat.id, document=out_file)
else:
LOGGER.info(f"OUT: '{msg}'")
bot.send_message(
chat_id=update.active_chat.id,
text=f"`{msg}`",
parse_mode=ParseMode.MARKDOWN,
)


@dev_plus
def değerlendirme(güncelleme: Güncelleme, bağlam: CallbackContext):
bot = context.bot
send(do(eval, bot, update), bot, update)


@dev_plus
def executive(update: Update, context: CallbackContext) :
bot = context.bot
send(do(exec, bot, update), bot, update)


def cleanup_code(code):
if code.startswith("```") ve code.endswith("```"):
return "\n".join(code.split("\n")[1:1])
return code.strip("` \n") 


def do(işlev, bot, güncelleme):
log_input(güncelleme)
içerik = update.message.text.split(" ", 1)[1]
body = temizleme_kodu(içerik) 
env = namespace_of(update.message.chat_id, update, bot)

os.chdir(os.getcwd())
with open(
os.path.join(os.getcwd(), " JarvisRobo/modules/helper_funcs/temp.txt"), "w"
) as temp:
temp.write(body)

stdout = io.StringIO()

to_compile = f'def func ():\n{textwrap.indent(body, " ")}'

try:
exec(to_compile, env)
hariç İstisna olarak e:
return f"{e.__class__.__name__} : {e}"

func = env["func"]

deneyin:
ile yönlendirme_stdout(stdout):
func_return = func()
hariç İstisna:
değer = stdout.getvalue ()
return f"{value}{traceback.format_exc()}"
else:
değer = stdout.getvalue()
result = Yok
if func_return Yok:
if değer:
sonuç = f"{değer}"
else:
try:
sonuç = f"{repr(eval(body, env))}"
hariç:
pass
else:
sonuç = f "{value}{func_return}"
if result:
return result


@dev_plus
def clear(update: Update, context: CallbackContext):
bot = context.bot
log_input( update)
genel ad alanları
ad alanlarında update.message.chat_id varsa:
del ad alanları[update.message.chat_id]
send("Yereller temizlendi.", bot, güncelleme)


EVAL_HANDLER = CommandHandler(("e", "ev", "eva", "eval"), değerlendir, run_async=True)
EXEC_HANDLER = CommandHandler(("x", "ex", "exe", "exec", " py"), çalıştır, run_async=True)
CLEAR_HANDLER = CommandHandler("clearlocals", clear, run_async=True)

dispatcher.add_handler(EVAL_HANDLER)
dispatcher.add_handler(EXEC_HANDLER)
dispatcher.add_handler( CLEAR_HANDLER)

__mod_name__ = "🔱eval🔱"
__help__ = f"""
★ᴏᴡɴᴇʀ ᴄᴍᴅ ★
★ /eval : basit kodu değerlendirmek için
★ /ex : kodu çalıştırmak için
★ /clear : cmd'yi temizlemek için 
"""