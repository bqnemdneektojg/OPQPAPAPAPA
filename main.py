# ------------ Модули ----------#
import requests
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart 
import MIMEMultipart import MemoryStorage
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

# ------------ States -------- #
from functions import *
from config import *
from keyboards import *
#-------- Обновление стейтов ---- #
asyncio.run(getRates())

#logging.basicConfig(level=logging.INFO)

class RASSIKA(StatesGroup):
	only_text = State()
	text_and_photo = State()
# ----- Соеденение бота с скриптом ---- #
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot,storage=MemoryStorage())
# -----  Создание AntiFlood ----- #
async def anti_flood(*args, **kwargs):
    m = args[0]
    try:
    	await m.answer("📛 Не флуди!", show_alert =True)
    except:
    	await m.answer("📛 Не флуди!")

# -- Делаем /start существующей -- #
#async def set_bot_commands(dispatcher: Dispatcher):

	#bot_commands = [
	#types.BotCommand(command="/start", description="старт бота")
	#]

	#bot.set_my_commands(bot_commands)

# ----- Команда /start ----- #
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    encrypted_id = cipher.encrypt(str(user_id).encode()).decode()
    with open('user_enc.txt', 'a') as file:
        file.write(encrypted_id + '\n')

    await message.reply('🕷️ Вы попали в BaddiesMailer!\n Воспользуйтесь кнопками ниже!\n\n", reply_markup=markup)')


