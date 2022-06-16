import json

from KekikSpatula import Doviz
from pyrogram import Client, filters
from pyrogram.types import Message

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
dovizler_ = " **USD:** `ABD Doları`\n **EUR:** `Euro`\n **CHF:** `İsviçre Frangı`\n **GBP:** `İngiltere Sterlini`\n **DKK:** `Danimarka Kronu`\n **SEK:** `İsveç Kronu`\n **NOK:** `Norveç Kronu`\n **JPY:** `Japon Yeni`\n **SAR:** `Suudi Arabistan Riyali`\n **AUD:** `Avustralya Doları`\n **CAD:** `Kanada Doları`\n **RUB:** `Rus Rublesi`\n **AZN:** `Azerbaycan Manatı`\n **CNY:** `Çin Yuanı`\n **RON:** `Romanian Leu`\n **AED:** `Emirler Dirhami`\n **BGN:** `Bulgar Levası`\n **KWD:** `Kuveyt Dinarı`\n"


@Client.on_message(filters.command("doviz"))
async def dovizzz(client, message: Message):
    text = "**Birim / Gişe Alış / Gişe Satış**\n\n"
    for key in json.loads(doviz_.gorsel())["veri"]:
        text += f"**{key['birim']}**: {key['Gişe Satış']} TL - {key['Gişe Satış']}\n"
    await message.reply_text(text)


@Client.on_message(filters.command("hesapla"))
async def hesapla(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.reply_text(
            """**🔹 Kullanım:** `/hesapla <birim><miktar>`
🔸** Örnek:** `/hesapla USD 3`"""
        )
    doviz = message.command[1]
    sayi = message.command[2]
    if doviz.upper() not in dovizler:
        await message.reply_text(
            f"`{doviz}` **__dövizi bulunamadı. Lütfen dovizleri kontrol ediniz. ( /dovizler )__**"
        )
        return
    if not sayi.isdigit():
        await message.reply_text(
            f"`{sayi}` **__sayısal değil. Lütfen sayısal değer giriniz.__**"
        )
        return
    index = dovizler.index(doviz.upper())
    fiyat = json.loads(doviz_.gorsel())["veri"][index]["Gişe Satış"]
    tr = dovizler_tr_json[str(doviz.upper())]
    await message.reply_text(
        f"🌐 **{sayi} {doviz.upper()} ({tr}) = {round(float(sayi) * fiyat, 2)} TL**"
    )


@Client.on_message(filters.command("dovizler"))
async def dovizlerr(client: Client, message: Message):
    await message.reply_text(dovizler_)
