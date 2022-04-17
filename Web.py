from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from DB import botDB
import json

cnt = 0

#Создание базы данных
BotDB = botDB('messages.db')

bot = Bot(token='5254134567:AAHHaYAbhnCPki38OXpOH40TdbG0beCkTqw')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message : types.Message):
    await message.answer(message.text)

    BotDB.add_message(message.from_user.id, message.text)

    # Нужно отправлять в HTTP!!!
    res = requests.post("http://localhost:3000/api/v1/message/",
                        {"user_id": int(message.from_user.id), "message": str(message.text)})
    res = requests.get("http://localhost:3000/api/v1/message/")
    if res is None:
        await message.answer("Пулл пустой!")
    else:
        await message.answer(json.dumps(res.json()))


executor.start_polling(dp, skip_updates=True)