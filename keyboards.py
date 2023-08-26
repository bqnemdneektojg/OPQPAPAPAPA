from aiogram import types
import requests

async def menu_keyboard(us_id):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=2)
	btn = [
	types.KeyboardButton(text="🕷️ Отправить письмо"),
types.KeyboardButton(text="🥷 Профиль"),
types.KeyboardButton(text="🎓 Информация"),
]
	admin = types.KeyboardButton(text='Админка')
	keyboard.add(*btn)
	from functions import GET_ADMIN_STATUS
	if await GET_ADMIN_STATUS(us_id) == 1:
		keyboard.add(admin if await GET_ADMIN_STATUS(us_id) == 1 else [])
	return keyboard

async def proxy_profile_keyboard():
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	keyboard.add(*[
		types.InlineKeyboardButton(text="💳 Пополнить баланс", callback_data='deposit'),
])
	return keyboard

async def deposit_keyboard():
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.add(*[
		types.KeyboardButton(text='💠 Cryptobot'),
		])
	return keyboard

async def admin_keyboard():
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard = False, resize_keyboard=True, row_width=2)
	keyboard.add(*[
		types.KeyboardButton(text = 'Сделать рассылку'),
])
	keyboard.add(
		types.KeyboardButton(text= 'Меню')
		)
	return keyboard


