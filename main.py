# API import
import telebot
from telebot import types
import os

# Place for variables
token = "<TOKEN>"
path=os.path.dirname(__file__)

# Create an instance of the class
bot = telebot.TeleBot(token)


# Response to start command(greetings)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGhmRjflroGx4xQ5x5N5yTXYfuAvoZrwAC4BkAAmFQQUmg29eSrVAdyCsE")

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Биология")
    item2 = types.KeyboardButton("География")
    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name} !\nЯ - <b>{1.first_name}</b>, бот созданный чтобы-бы помочь с учебой.".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


# Item selection
@bot.message_handler(content_types=['text'])
def item_selection(message):
    if message.text == 'Биология':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("7", callback_data='seven_b')
        item2 = types.InlineKeyboardButton("8", callback_data='eight_b')
        item3 = types.InlineKeyboardButton("9", callback_data='nine_b')
        item4 = types.InlineKeyboardButton("10", callback_data='ten_b')
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, "За какой класс?", reply_markup=markup)
    elif message.text == 'География':

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("7", callback_data='seven_g')
        item2 = types.InlineKeyboardButton("8", callback_data='eight_g')
        item3 = types.InlineKeyboardButton("9", callback_data='nine_g')
        item4 = types.InlineKeyboardButton("10", callback_data='ten_g')
        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, "За какой класс?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


# Topic selection
@bot.callback_query_handler(func=lambda call: True)
def callback_topic(call):
    try:
        if call.message:
            # list of topics
            if call.data == 'seven_b':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Строение микроскопа", callback_data='bio_7_1')
                item2 = types.InlineKeyboardButton("Строение клетки растения", callback_data='bio_7_2')
                item3 = types.InlineKeyboardButton("Виды растительных тканей", callback_data='bio_7_3')
                item4 = types.InlineKeyboardButton("Правила микроскопировпния", callback_data='bio_7_4')
                item5 = types.InlineKeyboardButton("Семя", callback_data='bio_7_5')
                item6 = types.InlineKeyboardButton("Корень", callback_data='bio_7_6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, "Выбери тему", reply_markup=markup)
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            elif call.data == 'eight_b':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Простейшие", callback_data='bio_8_1')
                item2 = types.InlineKeyboardButton("Плоские черви", callback_data='bio_8_2')
                item3 = types.InlineKeyboardButton("Кишечно-полосные", callback_data='bio_8_3')
                item4 = types.InlineKeyboardButton("...", callback_data='bio_8_4')
                markup.add(item1, item2, item3, item4)
                bot.send_message(call.message.chat.id, "Выбери тему", reply_markup=markup)
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            # Coming soon
            elif call.data == 'nine_b' or call.data == 'ten_b' or call.data == 'seven_g' or call.data == 'eight_g' or call.data == 'nine_g' or call.data == 'ten_g':
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                bot.send_message(call.message.chat.id, "coming soon")
            # Getting results
            elif call.data == 'bio_7_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\7\\1\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_7_2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\7\\2\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_7_3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\7\\3\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_7_4':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\7\\4\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_7_5':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\7\\5\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\7\\5\\2.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\7\\5\\3.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\7\\5\\4.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\7\\5\\5.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_7_6':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\7\\6\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\7\\6\\2.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\7\\6\\3.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_8_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                file = open(path+"\\data\\bio\\8\\1\\1.docx", 'rb')
                bot.send_document(call.message.chat.id, file)
            elif call.data == 'bio_8_2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                img = open(path+"\\data\\bio\\8\\2\\1.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\8\\2\\2.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\8\\2\\3.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\8\\2\\4.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
                img = open(path+"\\data\\bio\\8\\2\\5.jpg", 'rb')
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bio_8_3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вот, держи", reply_markup=None)
                file = open(path+"\\data\\bio\\8\\3\\1.docx", 'rb')
                bot.send_document(call.message.chat.id, file)
            elif call.data == 'bio_8_4':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="coming soon", reply_markup=None)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
