import telebot
from telebot import types

markup_start_inline_menu = types.InlineKeyboardMarkup()
btn_in_events = types.InlineKeyboardButton('Мероприятия', callback_data='events')
btn_in_price = types.InlineKeyboardButton('Стоимость', callback_data='price')
btn_in_contacts = types.InlineKeyboardButton('Контакты', callback_data='contacts')
btn_in_talk = types.InlineKeyboardButton('Поболтать', callback_data='talk')
btn_in_news = types.InlineKeyboardButton('Новости', callback_data='news')
markup_start_inline_menu.add(btn_in_news, btn_in_contacts, btn_in_talk, btn_in_events, btn_in_price)

markup_events_inline_menu = types.InlineKeyboardMarkup()
btn_in_corporates = types.InlineKeyboardButton('Корпоративы', callback_data='corporates')
btn_in_weddings = types.InlineKeyboardButton('Свадьбы', callback_data='weddings')
markup_events_inline_menu.add(btn_in_corporates, btn_in_weddings)

markup_price_inline_menu = types.InlineKeyboardMarkup()
btn_in_corporates_price = types.InlineKeyboardButton('Корпоративы', callback_data='pcorporates')
btn_in_weddings_price = types.InlineKeyboardButton('Свадьбы', callback_data='pweddings')
markup_price_inline_menu.add(btn_in_corporates_price, btn_in_weddings_price)

markup_choose_inline_menu = types.InlineKeyboardMarkup()
btn_in_order = types.InlineKeyboardButton('Забронировать', callback_data='order')
btn_in_back_menu = types.InlineKeyboardButton('Вернуть меню', callback_data='back_menu')
markup_choose_inline_menu.add(btn_in_order, btn_in_back_menu)

keyboard_hider = types.ReplyKeyboardRemove()