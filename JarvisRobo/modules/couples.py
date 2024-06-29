rastgele içe aktar
tarihsaatten tarihsaati içe aktar

pyrogram içe aktarma filtrelerinden
pyrogram.enums'tan ChatType'ı içe aktar

JarvisRobo'dan pbot'u içe aktar
JarvisRobo.utils.mongo'dan içe aktar get_couple, save_couple

Tarih ve time
def dt():
şimdi = datetime.now()
dt_string = now.strftime("!^d/!^m/!^Y !^H:!^M")
dt_list = dt_string.split(" ")
return dt_list

def dt_tom():
a = (
str(int(dt()[].split("/")[]) 1)
"/"
dt()[].split("/")[1]
"/"
dt()[].split("/")[2]
)
return a

bugün = str(dt()[])
yarın = str(dt_tom())

COUPLES_PIC = "https://telegra.ph/file/c54ab3e58161c7ee.jpg"
CAP = "" "
**ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ :**

{} {} = 💗
ɴᴇᴡ ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴄᴀɴ ʙᴇ ᴄʜᴏsᴇɴ ᴀᴛ 12 ᴀᴍ {}
"""

CAP2 = "" "
**ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ :**

{} {} = 💗
ɴᴇᴡ ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴄᴀɴ ʙᴇ ᴄʜᴏsᴇɴ ᴀᴛ 12 ᴀᴍ {}
"""

@pbot.on_message (filters.command(["çift", "çiftler"]))
async def çift(_, mesaj):
if message.chat.type == ChatType.PRIVATE:
return wait message.reply_text(" ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ.")
şunu deneyin:
chat_id = message.chat.id
is_selected = get_couple'ı bekliyor(chat_id, bugün)
eğer seçili değilse:
liste _of_users = []
i için eşzamansız pbot.get_chat_members(message.chat.id, limit=5):
değilse i.user.is_bot:
list_of_users.append(i.user.id)
if len(list_of_users) < 2:
return wait message.reply_text("ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴜsᴇʀ")
c1_id = random.choice(list_of_users)
c2_id = random.choice(list_of_users)
while c1_id == c2_id:
c1_id = random.choice(list_of_users) 
c1_mention = (pbot.get_users(c1_id) bekleniyor).mention
c2_mention = (pbot.get_users(c2_id) bekleniyor).mention

double_selection_message = CAP.format(c1_mention, c2_mention, yarın)
pbot bekleniyor .send_photo(message.chat.id, photo=COUPLES_PIC, caption=couple_selection_message)
çift = {"c1_id": c1_id, "c2_id": c2_id}
wait save_couple(chat_id, bugün, çift)

elif is_selected:
c1_id = int(is_selected["c1_id"])
c2_id = int(is_selected["c2_id"])
c1_name = (pbot.get_users(c1_id) bekleniyor).mention
c2_name = (pbot bekleniyor) .get_users(c2_id)).mention
double_selection_message = CAP2.format(c1_name, c2_name, yarın)
wait pbot.send_photo(message.chat.id, photo=COUPLES_PIC, caption=couple_selection_message)
istisna hariç: e: 
print(e)
wait message.reply_text(str(e))

__help__ = """
ᴄʜᴏᴏsᴇ ᴄᴏᴜᴘʟᴇs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

❍ /couples *:* sᴇ 2 ᴜsᴇʀs ᴀɴᴅ sᴇɴᴅ ᴛʜᴇɪʀ ɴᴀᴍᴇ ᴀs ᴄᴏᴜᴘʟᴇs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
"""

__mod_name__ = "🔱çift🔱"