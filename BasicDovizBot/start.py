from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Config import *


@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        """<p style="text-align: center;"><em><strong>💰 Basic Döviz Botu\n</strong></em></p>
<p><strong>• Botu kullanarak döviz kurlarını görüntüleyebilir ve hesaplayabilirsiniz.\n</strong><br /><strong>• Botu gruplarda ve özel sohbetlerde de kullanabilirsiniz.</strong></p>""",
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🕹 Komutları Gör", callback_data="help")]]
        ),
    )


@Client.on_callback_query()
async def help(client, callback_query):
    if callback_query.data == "help":
        await callback_query.message.edit_text(
            f"""**__💰 Basic Döviz Botu__

• Botu kullanarak döviz kurlarını görüntüleyebilir ve hesaplayabilirsiniz.
• Botu gruplarda ve özel sohbetlerde de kullanabilirsiniz.

🕹 Komutlar**
• /doviz - Döviz kurlarını görüntelemeni, içindir.
• /hesapla - istediğiniz döviz kurunu hesaplamanız içindir.
• /dovizler - desteklenen dövizleri görmeniz içindir.

**Bot satır içi modunda da çalışmaktadır.**
**Örnek:** `@{BOT_USERNAME} USD 1`
**Satır içi modunda tüm dövizleri görebilirsiniz.**
**Örnek:** `@{BOT_USERNAME} dovizler`""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔹 Daralt", callback_data="back"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🔸 Döviz Hesapla", switch_inline_query="USD 1"
                        ),
                        InlineKeyboardButton(
                            "🔹 Tüm dövizler", switch_inline_query="dovizler"
                        ),
                    ],
                ],
            ),
        )
    elif callback_query.data == "back":
        await callback_query.message.edit_text(
            """<p style="text-align: center;"><em><strong>💰 Basic Döviz Botu\n</strong></em></p>
<p><strong>• Botu kullanarak döviz kurlarını görüntüleyebilir ve hesaplayabilirsiniz.\n</strong><br /><strong>• Botu gruplarda ve özel sohbetlerde de kullanabilirsiniz.</strong></p>""",
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🕹 Komutları Gör", callback_data="help")]]
            ),
        )
