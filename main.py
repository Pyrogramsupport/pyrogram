from pyrogram import Client, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update

API_ID="17795696"
API_HASH="afcbcd249c7d8728d9b213b10d39a649"
BOT_TOKEN="5324288989:AAEZNpMAf6DOHveFMOjm-Mxmeu_9TgVBsSg"

Siva = Client(
   name="PyrogramBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)
@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
   await message.reply_text("Hello! Iam pyrogram bot "),
   await message.reply_text("My master is siva the boss"),
button = [
    [         
             InlineKeyboardButton(
                  text=" hi"
                  call_back_data="miku_")
              ],

]
if query.data == "miku_":
        query.message.edit_text(
            text=f"""Hello [{update.effective_user.first_name}](tg://user?id={update.effective_user.id}) I'm {context.bot.first_name}, a powerful group management bot built to help you manage your group easily.
                 \n❍ I can restrict users.
                 \n❍ I can greet users with customizable welcome messages and even set a group's rules.
                 \n❍ I have an advanced anti-flood system.
                 \n❍ I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc.
                 \n❍ I have a note keeping system, blacklists, and even predetermined replies on certain keywords.
                 \n❍ I check for admins' permissions before executing any command and more stuffs
                 \n❍ shu licensed under the GNU General Public License v3.0
                 \n❍ If you have any question about aigar, let us know at [aigar support ](t.me/aigar_support).""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="🌏 My Master", url="t.me/Sivathe_boss"),
                    InlineKeyboardButton(text="✨ Try Inline", switch_inline_query_current_chat="",),
                 ],
                 [
                    InlineKeyboardButton(text="🕊️ Updates", url="t.me/aigar_updates"),
                    InlineKeyboardButton(text="🚑 Support", url="t.me/aigar_support"),
                 ],
                 [
                    InlineKeyboardButton(text="❌ Back", callback_data="miku_back")
                 ],
                ]
            ),
        )
    elif query.data == "miku_back":
        first_name = update.effective_user.first_name
        query.message.edit_text(
                PM_START_TEXT.format(
                    escape_markdown(context.bot.first_name),
                    PM_PHOTO,
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=5,
                disable_web_page_preview=False,
        )






print("Bot strarted")

Siva.run()
