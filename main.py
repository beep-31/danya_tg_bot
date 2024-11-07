# import aiogram
import os
import dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.handlers import CallbackQueryHandler
import logging
import asyncio
import keyboards

dotenv.load_dotenv()

TELEGRAM_API = os.getenv('TELEGRAM_API')
CHANNEL_ID = os.getenv('CHANNEL_ID')

ONE_MONTH_LINK = os.getenv('1_month_link')
THREE_MONTH_LINK = os.getenv('3_month_link')
SIX_MONTH_LINK = os.getenv('6_month_link')

dp = Dispatcher()

inline_keyboard_start = keyboards.inline_keyboard_start
inline_keyboard_subscription = keyboards.inline_keyboard_subscription
inline_keyboard_payment_method = keyboards.inline_keyboard_payment_method
inline_keyboard_go_back = keyboards.inline_keyboard_go_back

user_subscription_state = {}

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    # Создаем клавиатуру
    inline_keyboard = inline_keyboard_start
    # Отправка сообщения
    await message.answer(
        "Приветствую друг!👋 Этот бот поможет тебе попасть в приватное сообщество Дани Шевцова.\n\n"
        "Подписка - ежемесячная, оплату можно произвести в любой валюте и крипте.\n\n"
        "Отписаться можно в любой момент 🤝",
        reply_markup=inline_keyboard
    )

@dp.callback_query(lambda call: call.data == "pay_access")
async def handle_pay_access(callback_query: types.CallbackQuery):
    inline_keyboard = inline_keyboard_subscription
    await callback_query.message.answer(
        "💵 Стоимость подписки\n\n"
        "1 месяц 1500 рублей\n\n"
        "3 месяца 4500 рублей\n\n"
        "6 месяцев 9000 рублей\n\n"
        "*цена в долларах/евро - конвертируется ботом по курсу\n\n"
        "*оплачивай любой картой в долларах/евро/рублях, бот сконвертирует сам\n\n"
        "Оплатить и получить доступ\n\n"
        "👇👇👇", 
        reply_markup = inline_keyboard)
    await callback_query.answer()

@dp.callback_query(lambda call: call.data == "go_back")
async def go_back(callback_query: types.CallbackQuery):
    user_subscription_state[callback_query.from_user.id] = ''
    await send_welcome(callback_query.message)
    await callback_query.answer()

@dp.callback_query(lambda call: call.data == "go_back_to_subscription")
async def go_back_to_subscription(callback_query: types.CallbackQuery):
    user_subscription_state[callback_query.from_user.id] = ''
    await handle_pay_access(callback_query)
    await callback_query.answer()

#отработка кнопок подписки
@dp.callback_query(lambda call: call.data == "1_month_subscription")
async def one_month_subscription(callback_query: types.CallbackQuery):
    inline_keyboard = inline_keyboard_payment_method
    user_subscription_state[callback_query.from_user.id] = '1 month'
    await callback_query.message.answer(
        "Выберите способ оплаты"
        "👇👇👇", 
        reply_markup = inline_keyboard)
    await callback_query.answer()

@dp.callback_query(lambda call: call.data == "3_month_subscription")
async def three_month_subscription(callback_query: types.CallbackQuery):
    inline_keyboard = inline_keyboard_payment_method
    user_subscription_state[callback_query.from_user.id] = '3 month'
    await callback_query.message.answer(
        "Выберите способ оплаты"
        "👇👇👇", 
        reply_markup = inline_keyboard)
    await callback_query.answer()

@dp.callback_query(lambda call: call.data == "6_month_subscription")
async def six_month_subscription(callback_query: types.CallbackQuery):
    inline_keyboard = inline_keyboard_payment_method
    user_subscription_state[callback_query.from_user.id] = '6 month'
    await callback_query.message.answer(
        "Выберите способ оплаты"
        "👇👇👇", 
        reply_markup = inline_keyboard)
    await callback_query.answer()

#пользователь выбрал способ оплаты. Присылаем ему ссылку
@dp.callback_query(lambda call: call.data == "RUB")
async def payment(callback_query: types.CallbackQuery):
    inline_keyboard = inline_keyboard_go_back
    user_id = callback_query.from_user.id
    subscription_type = user_subscription_state.get(user_id)
    if subscription_type == '1 month':
        link = ONE_MONTH_LINK
    elif subscription_type == '3 month':
        link = THREE_MONTH_LINK
    elif subscription_type == '6 month':
        link = SIX_MONTH_LINK
    else:
        link = None
    if link:
        await callback_query.message.answer(
            f"Перейдите по ссылке чтобы завершить оплату 👇👇👇 \n\n {link}",
            reply_markup = inline_keyboard)
    else: 
        await callback_query.message.answer("Не удалось определить выбранную подписку. Попробуйте еще раз.", reply_markup = inline_keyboard)
    await callback_query.answer()

@dp.callback_query(lambda call: call.data == "USD/EURO")
async def usd_euro_payment(callback_query: types.CallbackQuery):
    await payment(callback_query)
    await callback_query.answer()

@dp.callback_query(lambda call: call.data == "USDT")
async def usdt_payment(callback_query: types.CallbackQuery):
    await payment(callback_query)
    await callback_query.answer()

async def main():    
    bot = Bot(token=TELEGRAM_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    