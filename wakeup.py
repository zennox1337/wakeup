import sys

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
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
        await message.reply("Включаю компьютер")
        send_magic_packet(MAC,
                          ip_address=IP,
                          port=9)
    except Exception as e:
        await message.reply("Вызвано исключение, попробуйте еще раз")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
