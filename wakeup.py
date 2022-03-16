import sys
import time

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from time import gmtime, strftime
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from wakeonlan import send_magic_packet

TOKEN = sys.argv[1]
MAC = sys.argv[2]
IP = sys.argv[3]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['on'])
async def wakeup(message: types.Message):
    try:
        await message.reply(strftime("%d-%m-%Y %H:%M:%S", gmtime()) + "\nВключаю компьютер")
        send_magic_packet(MAC,
                          ip_address=IP,
                          port=9)
        time.sleep(1)
        await bot.send_message(chat_id=message.chat.id, text='Компьютер включен, можете подключаться по VNC')
    except Exception as e:
        await message.reply("Вызвано исключение, попробуйте еще раз")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
