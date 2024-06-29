içe aktarma istekleri
telegramdan içe aktarma ParseMode, Güncelleme
telegram.ext'ten içe aktarma CallbackContext, CommandHandler

JarvisRobo'dan içe aktar CASH_API_KEY, dağıtıcı


def dönüştürme(güncelleme: Güncelleme, bağlam: CallbackContext):
args = update.active_message.text.split(" ")

if len(args) == 4:
deneyin:
orig_cur_amount = float(args[1])

hariç ValueError:
update.active_message.reply_text("Geçersiz Para Birimi Tutarı")
return

orig_cur = args[2].upper()

new_cur = args[3].upper()

request_url = (
f"https://www.alphavantage.co/query"
f"?function=CURRENCY_EXCHANGE_RATE"
f"&from_currency={orig_cur}"
f"&to_currency={new_cur }"
f"&apikey={CASH_API_KEY}"
)
yanıt = request.get(request_url).json()
try:
current_rate = float(
Response["Gerçek Zamanlı Döviz Değişimi) Rate"]["5. Döviz Kuru"]
)
hariç KeyError:
update.active_message.reply_text("Para Birimi Desteklenmiyor.")
return
new_cur_amount = round(orig_cur_amount * current_rate, 5)
update.active_message.reply_text(
f"{orig_cur_amount} {orig_cur} = {new_cur_amount} {new_cur}"
)

elif len(args) == 1:
update.active_message.reply_text(__help__ , parse_mode=ParseMode.MARKDOWN)

else:
update.active_message.reply_text(
f"*Geçersiz Args!!:* Gerekli 3 Ancak Geçildi {len(args) 1}",
parse_mode=ParseMode .MARKDOWN,
)


__help__ = """
Parayı bir borsadan diğerine dönüştürür

Kullanım: /cash tutarı -den
Örnek: /cash 2 USD INR
"" "

CONVERTER_HANDLER = CommandHandler("nakit", dönüştürme, run_async=True)
dispatcher.add_handler(CONVERTER_HANDLER)
__command_list__ = ["nakit"]

__handlers__ = [CONVERTER_HANDLER]

__mod_name__ = "🔱nakit🔱"