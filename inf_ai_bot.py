import telebot
from telebot import types
import apiai
import json
import config_bot #make config_bot.py
import markups_bot 
import answers_bot #make answers_bot.py

bot = telebot.TeleBot(config_bot.TG_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
		bot.reply_to(message, text='', reply_markup=markups_bot.markup_start_inline_menu)


@bot.message_handler(commands=['order'])
def get_order(message):
		bot.reply_to(message, text='', reply_markup=markups_bot.markup_start_inline_menu)
		bot.forward_message(chat_id=config_bot.CHAT_ID, from_chat_id=message.from_user.id, message_id=message.message_id)

@bot.message_handler(content_types=['text'])
def text_message(message):
		request = apiai.ApiAI(config_bot.DIA_TOKEN).text_request()
		request.lang = 'ru'
		request.session_id = 'ID_SESSION'
		request.query = message.text
		responseJson = json.loads(request.getresponse().read().decode('utf-8'))
		response = responseJson['result']['fulfillment']['speech']

		if response:
				bot.send_message(message.chat.id, response)
		else:
				bot.send_message(message.chat.id, text='')

@bot.callback_query_handler(func=lambda call: True)
def call_back_start_menu(call):
		if call.data == 'events':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_events, reply_markup=markups_bot.markup_events_inline_menu)

		elif call.data == 'price':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_price, reply_markup=markups_bot.markup_price_inline_menu)

		elif call.data == 'contacts':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_contact, reply_markup=markups_bot.markup_start_inline_menu)

		elif call.data == 'corporates':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_corporates, reply_markup=markups_bot.markup_choose_inline_menu)

		elif call.data == 'back_menu':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_back_menu, reply_markup=markups_bot.markup_start_inline_menu)

		elif call.data == 'order':
				bot.send_message(call.message.chat.id, text = answers_bot.answer_order, reply_markup=markups_bot.keyboard_hider)

		elif call.data == 'weddings':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_weddings, reply_markup=markups_bot.markup_choose_inline_menu)

		elif call.data == 'pcorporates':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_pcorporates, reply_markup=markups_bot.markup_choose_inline_menu)
		
		elif call.data == 'pweddings':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_pweddings, reply_markup=markups_bot.markup_choose_inline_menu)

		elif call.data == 'news':
				bot.send_message(call.message.chat.id, text=answers_bot.answer_news, reply_markup=markups_bot.markup_start_inline_menu)
		
		elif call.data == 'talk':
			bot.send_message(call.message.chat.id, text=answers_bot.answer_talk, reply_markup=markups_bot.markup_start_inline_menu)


if __name__ == "__main__":
		bot.polling(none_stop=True)


