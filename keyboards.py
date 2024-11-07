from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


inline_keyboard_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Оплатить доступ", callback_data="pay_access"),
    InlineKeyboardButton(text="🔍 Подробнее о канале", callback_data="channel_info")],
    [InlineKeyboardButton(text="🙋 Задать вопрос", callback_data="ask_question"),
    InlineKeyboardButton(text="🎁 Подарить подписку", callback_data="gift_access")],
])

inline_keyboard_subscription = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подписка на месяц 1️⃣", callback_data="1_month_subscription")],
    [InlineKeyboardButton(text="Подписка на 3 месяца 3️⃣", callback_data="3_month_subscription")],
    [InlineKeyboardButton(text="Подписка на 6 месяцев 6️⃣", callback_data="6_month_subscription")],
    [InlineKeyboardButton(text="Вернуться назад ⬅️", callback_data="go_back")]
])

inline_keyboard_payment_method = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="РУБ", callback_data="RUB"),
    InlineKeyboardButton(text="Доллар-евро", callback_data="USD/EURO")],
    [InlineKeyboardButton(text="USDT", callback_data="USDT")],
    [InlineKeyboardButton(text="Вернуться назад ⬅️", callback_data="go_back_to_subscription")]
])

inline_keyboard_go_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вернуться назад ⬅️", callback_data="go_back_to_subscription")]
])