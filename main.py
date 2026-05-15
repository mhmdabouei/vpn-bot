from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

BOT_TOKEN = "8899555331:AAEQ0_hZhRslIcC5_pyEj3XTFerQYVunP1E"

ADMIN_ID = 8565856486

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

users_wallet = {}

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 خرید VPN", callback_data="buy")],
    [InlineKeyboardButton(text="💰 شارژ کیف پول", callback_data="wallet")],
    [InlineKeyboardButton(text="📦 سرویس‌های من", callback_data="myvpn")],
    [InlineKeyboardButton(text="🎧 پشتیبانی", url="https://t.me/ertebatsariadmin")]
])

@dp.message(CommandStart())
async def start(message: types.Message):
    uid = message.from_user.id

    if uid not in users_wallet:
        users_wallet[uid] = 0

    text = '''
🚀 به ربات ارتباط سریع خوش اومدی

✔️ سرعت بالا
✔️ بدون ضریب
✔️ پینگ پایین
✔️ اتصال روی تمامی اینترنت‌ها

💰 تعرفه‌ها:

🔹 زیر ۱۰ گیگ:
هر گیگ ۳۵۰ هزار تومان

🔹 ۱۰ گیگ به بالا:
هر گیگ ۲۲۰ هزار تومان
'''

    await message.answer(text, reply_markup=menu)

@dp.callback_query(F.data == "wallet")
async def wallet(callback: types.CallbackQuery):
    await callback.message.answer(
        "💳 مبلغ را کارت به کارت کنید و سپس عکس رسید را ارسال نمایید."
    )

@dp.message(F.photo)
async def handle_receipt(message: types.Message):

    caption = f'''
📩 رسید جدید دریافت شد

👤 کاربر:
@{message.from_user.username}

🆔:
{message.from_user.id}
'''

    await bot.send_photo(
        ADMIN_ID,
        photo=message.photo[-1].file_id,
        caption=caption
    )

    await message.answer(
        "✅ رسید شما برای ادمین ارسال شد."
    )

@dp.callback_query(F.data == "buy")
async def buy(callback: types.CallbackQuery):
    await callback.message.answer(
        "🛒 حجم موردنظر را ارسال کنید. مثال: 10 گیگ"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
