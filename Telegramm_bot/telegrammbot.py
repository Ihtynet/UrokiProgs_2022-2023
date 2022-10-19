from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "5484655211:AAGTy36WFfKnWUFoV70OXTUW4_oRQH_5sfo"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer('Я бот. Приятно познакомиться!')

"""    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await msg.answer("Как подавать котлеты?", reply_markup=keyboard)"""

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
       photo = open('empty.png', 'rb')
       await msg.answer_photo(photo, "мое фото")
   else:
       await msg.answer('Не понимаю, что это значит.')

if __name__ == '__main__':
   executor.start_polling(dp)