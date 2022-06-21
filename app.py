import telebot
from telebot import types
import random

bot = telebot.TeleBot('5540579046:AAHSPojPUsMxN4dzKlaWewD6Cpzm4q4B4Oc')


@bot.message_handler(commands=['start'])
def start(message):
     mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>, пиши команду /help для вызова меню'
     bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
     bot.send_message(message.chat.id, "<b>Я возбудился</b>", parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Группа в вк с негро-приколами", url="https://vk.com/nigga_memes"))
     bot.send_message(message.chat.id, "Перейдите на смешинку", reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

     funpic = types.KeyboardButton('Прикол')
     website = types.KeyboardButton('Группа в вк с негро-приколами')

     markup.add(website, funpic)
     bot.send_message(message.chat.id, "Перейдите на смешинку", reply_markup=markup)

     ###########################                 MESSAGES               #################################
@bot.message_handler(content_types=['text'])
def get_user_text(message):
     if message.text == "Привет":
          bot.send_message(message.chat.id, "Привет, сладкий!", parse_mode='html')
     elif message.text == "Id":
          bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')

     elif message.text == "Прикол":
          photo = open('icon.jpg', 'rb')
          bot.send_photo(message.chat.id, photo)
     elif message.text == "Группа в вк с негро-приколами":
          markup = types.InlineKeyboardMarkup()
          markup.add(types.InlineKeyboardButton("Перейдите на смешинку", url="https://vk.com/nigga_memes"))
          bot.send_message(message.chat.id, "Перейдите на смешинку", reply_markup=markup)
     elif message.text == "Спасибо":
          bot.send_message(message.chat.id, "Спасибо в карман не положишь")
     elif message.text == "Положишь":
          bot.send_message(message.chat.id, "Нет")
     elif message.text == "Да":
          photo = open('pizda.jpg', 'rb')
          bot.send_photo(message.chat.id, photo)
     elif message.text == "Нет":
          photo = open('otvet_net1.jpg', 'rb')
          bot.send_photo(message.chat.id, photo)
     elif message.text == "Не спорь":
          bot.send_message(message.chat.id, "нет, ты не спорь")
     else:
          if random.randint(0, 5) == 1:
               bot.send_message(message.chat.id, "Я тупой негр")
          elif random.randint(0, 5) == 2:
               bot.send_message(message.chat.id, "Я тебя не понимаю")
          elif random.randint(0, 5) == 3:
               bot.send_message(message.chat.id, "Напиши что-то другое")
          elif random.randint(0, 5) == 4:
               photo = open('elsemess4.jpg', 'rb')
               bot.send_photo(message.chat.id, photo)
          elif random.randint(0, 5) == 5:
               photo = open('elsemess5.jpg', 'rb')
               bot.send_photo(message.chat.id, photo)
     #################################################################################################

bot.polling(none_stop=True)