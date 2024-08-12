import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram import F
import aiohttp

TOKEN = "7453217661:AAErSkc2enBzM04Ovs3tVzjm4faEHq_KVM8"
CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
    "Doge": "DOGEUSDT"
}

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    for crypto_name in CRYPTO_NAME_TO_TICKER.keys():
        item_button = KeyboardButton(crypto_name)
        markup.add(item_button)
    await message.reply("Choose a crypto", reply_markup=markup)


@dp.message(F.text.in_(CRYPTO_NAME_TO_TICKER.keys()))
async def send_price(message: types.Message):
    crypto_name = message.text
    ticker = CRYPTO_NAME_TO_TICKER[crypto_name]
    try:
        price = await get_price_by_ticker(ticker=ticker)
        await message.reply(f"Price of {crypto_name} to USDT is {price}")
    except Exception as e:
        await message.reply(f"Could not retrieve the price for {crypto_name}. Please try again later.")
        print(f"Error occurred: {e}")


async def get_price_by_ticker(*, ticker: str) -> float:
    endpoint = "https://api.binance.com/api/v3/ticker/price"
    params = {'symbol': ticker}
    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint, params=params) as response:
            if response.status != 200:
                print(f"API request failed with status code {response.status}")
                print(f"Response: {response.text}")
                raise Exception("API request failed")
            data = await response.json()
            print(f"Response data: {data}")
            price = round(float(data["price"]), 2)
            return price


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
