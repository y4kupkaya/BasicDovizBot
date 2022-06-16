import json

from KekikSpatula import Doviz
from pyrogram import Client, filters
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from Config import *

doviz_ = Doviz()
dovizler = [
    "USD",
    "EUR",
    "CHF",
    "GBP",
    "DKK",
    "SEK",
    "NOK",
    "JPY",
    "SAR",
    "AUD",
    "CAD",
    "RUB",
    "AZN",
    "CNY",
    "RON",
    "AED",
    "BGN",
    "KWD",
]
dovizler_tr_json = {
    "USD": "ABD Doları",
    "EUR": "Euro",
    "CHF": "İsviçre Frangı",
    "GBP": "İngiltere Sterlini",
    "DKK": "Danimarka Kronu",
    "SEK": "İsveç Kronu",
    "NOK": "Norveç Kronu",
    "JPY": "Japon Yeni",
    "SAR": "Suudi Arabistan Riyali",
    "AUD": "Avustralya Doları",
    "CAD": "Kanada Doları",
    "RUB": "Rus Rublesi",
    "AZN": "Azerbaycan Manatı",
    "CNY": "Çin Yuanı",
    "RON": "Romanian Leu",
    "AED": "Emirler Dirhami",
    "BGN": "Bulgar Levası",
    "KWD": "Kuveyt Dinarı",
}


@Client.on_inline_query()
async def inline_query_handler(client: Client, query: InlineQuery):
    text = query.query
    if text == "" or len(text.split()) < 2:
        try:
            await query.answer(
                results=[
                    InlineQueryResultArticle(
                        title="Kullanım",
                        description=f"Örnek: @{BOT_USERNAME} USD 1",
                        thumb_url="https://telegra.ph/file/a6c49a0f97f5828068208.jpg",
                        input_message_content=InputTextMessageContent(
                            f"**🔹 Kullanım:** `@{BOT_USERNAME} birim / miktar`\n🔸**Örnek:** `@{BOT_USERNAME} USD 3`"
                        ),
                    ),
                ]
            )
        except Exception as e:
            print(e)
            return
    if text == "dovizler":
        try:
            await query.answer(
                [
                    InlineQueryResultArticle(
                        title=f"{doviz} ({value})",
                        input_message_content=InputTextMessageContent(
                            f'1 {doviz} ({value}) = {json.loads(doviz_.gorsel())["veri"][dovizler.index(doviz.upper())]["Gişe Satış"]} TL',
                        ),
                        description=f'{json.loads(doviz_.gorsel())["veri"][dovizler.index(doviz.upper())]["Gişe Satış"]} TL',
                        thumb_url="https://telegra.ph/file/a6c49a0f97f5828068208.jpg",
                    )
                    for doviz, value in dovizler_tr_json.items()
                ]
            )
        except Exception as e:
            print(e)


@Client.on_inline_query(filters.regex("^(\w+) (\d+)?$"), group=1)
async def inline(client: Client, query: InlineQuery):
    doviz = query.matches[0].group(1)
    sayi = query.matches[0].group(2)
    if doviz.upper() not in dovizler:
        await query.answer(
            [
                InlineQueryResultArticle(
                    title="Döviz Bulunamadı",
                    input_message_content=InputTextMessageContent(
                        f"⚠️ `{doviz}` **dövizi bulunamadı. Lütfen dovizleri kontrol ediniz. (** `@{BOT_USERNAME} dovizler` **)**"
                    ),
                    description=f"{doviz} bulunamadı",
                    thumb_url="https://telegra.ph/file/3846bd37647161f5b1f7c.jpg",
                )
            ]
        )
        return
    if not sayi.isdigit():
        try:
            await query.answer(
                [
                    InlineQueryResultArticle(
                        title="Hatalı Kullanım",
                        input_message_content=InputTextMessageContent(
                            f"⚠️ `{sayi}` **sayısal değil. Lütfen sayısal değer giriniz.**"
                        ),
                        description=f"{sayi} sayısal değil. Lütfen sayısal değer giriniz.",
                        thumb_url="https://telegra.ph/file/3846bd37647161f5b1f7c.jpg",
                    )
                ]
            )
        except Exception as e:
            print(e)
            return
        return
    index = dovizler.index(doviz.upper())
    fiyat = json.loads(doviz_.gorsel())["veri"][index]["Gişe Satış"]
    await query.answer(
        [
            InlineQueryResultArticle(
                title=f"{sayi}{doviz.upper()} -> TL",
                input_message_content=InputTextMessageContent(
                    f"**🌐 {sayi} {doviz} = {round(float(sayi) * fiyat, 2)} TL**"
                ),
                description=f"{sayi} {doviz.upper()} = {round(float(sayi) * fiyat, 2)} TL",
                thumb_url="https://telegra.ph/file/699be67597195cd542666.jpg",
            ),
        ],
    )
