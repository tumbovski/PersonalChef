import telebot
from telebot import types
import json
import sqlite3
import random as rn

bot = telebot.TeleBot('6019892545:AAGktOcqyIXrTIvxLUmJMKgnXMrtt4tKDkk')
lst = []

@bot.message_handler(commands=['start'])
def start(message):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton('Начать', callback_data = 'hub'))
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! 🧑‍🍳\nСпасибо, что решили попробовать нашего бота-шеф-повара Personal Chef!🥗 \n\nБот создан для тех, кто хочет разнообразить свой рацион или научиться готовить что-то новое.\n\nНаш бот только запустился и ещё находится в тестировании, и мы будем рады, если Вы отправите отзыв/предложение/жалобу на нашу почту personal.chef.bot@gmail.com \n\n🍔' )
    bot.send_message(message.chat.id, 'Привет, я шеф-бот Personal Chef\n\nВ моей базе находятся более 100 блюд, я уверен что смогу помочь Вам разнообразить Ваш рацион.\n\nНачнем?', reply_markup = btn)
    def data_add(us_data):
        """Эта функция добавляет нового пользователя в json файл"""
        with open ('usersData.json', 'r', encoding = 'utf-8') as f:
            lst = list(json.load(f))
            lst_id = []
            for user in lst:
                lst_id.append(user["ID"])
            if message.from_user.id not in lst_id:
                with open('usersData.json', 'w', encoding = 'utf-8') as f:
                    lst.append(user_data)
                    json.dump(lst, f, indent = 4, ensure_ascii = False)
    user_data = {
        'username': message.from_user.username,
        'first name': message.from_user.first_name,
        'last name': message.from_user.last_name,
        'ID': message.from_user.id
    }
    data_add(user_data)


@bot.message_handler(commands=['hub'])
def hub(message):
    file = open('./helloPhoto.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Рацион на день", callback_data = 'day_meal'))
    bot.send_message(message.chat.id, 'Это <b>хаб</b>, здесь вы можете выбрать интересующую Вас опцию 🍎🤗\n\n/help - помощь по командам бота\n\n Наш функционал постоянно обновляется, следите за обновлениями!', parse_mode = 'html', reply_markup = btn)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    """Функция отклика на нажатия кнопок"""
    if callback.data == 'hub':
        file = open('./helloPhoto.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file)
        btn = types.InlineKeyboardMarkup()
        btn.add(types.InlineKeyboardButton("Рацион на день", callback_data = 'day_meal'))
        bot.send_message(callback.message.chat.id, 'Это <b>хаб</b>, здесь вы можете выбрать интересующую Вас опцию 🍎🤗\n\n/help - помощь по командам бота\n\nНаш функционал постоянно обновляется, следите за обновлениями!', parse_mode = 'html', reply_markup = btn)
    if callback.data == 'day_meal':
       btn = types.InlineKeyboardMarkup()
       br_id = str(rn.randint(1, 20))
       ln1_id = str(rn.randint(1, 20))
       ln2_id = str(rn.randint(21, 40))
       dn_id = str(rn.randint(1, 20))
       con = sqlite3.connect('FoodBase.db')
       cursor = con.cursor()
       cursor.execute(f'SELECT Название, url, photo_url FROM breakfast WHERE id = {br_id}')
       br_name, br_url, br_photo = cursor.fetchone()
       cursor.execute(f'SELECT Название, url, photo_url FROM lunch WHERE id = {ln1_id}')
       ln1_name, ln1_url, ln1_photo = cursor.fetchone()
       cursor.execute(f'SELECT Название, url, photo_url FROM lunch WHERE id = {ln2_id}')
       ln2_name, ln2_url, ln2_photo = cursor.fetchone()
       cursor.execute(f'SELECT Название, url, photo_url FROM dinner WHERE id = {dn_id}')
       dn_name, dn_url, dn_photo = cursor.fetchone()
       btn.add(types.InlineKeyboardButton(f'{br_name}', url = br_url))
       btn.add(types.InlineKeyboardButton(f'{ln1_name}', url = ln1_url))
       btn.add(types.InlineKeyboardButton(f'{ln2_name}', url = ln2_url))
       btn.add(types.InlineKeyboardButton(f'{dn_name}', url = dn_url))
       bot.send_media_group(callback.message.chat.id, [types.InputMediaPhoto(br_photo), types.InputMediaPhoto(ln1_photo),
                                              types.InputMediaPhoto(ln2_photo), types.InputMediaPhoto(dn_photo)])
       bot.send_message(callback.message.chat.id, f'☕️🥪<u><b>Завтрак</b></u>: {br_name}\n\n🍲🍞<u><b>Первое на обед</b></u>: {ln1_name}\n\n🥘🧆<u><b>Второе на обед</b></u>: {ln2_name}\n\n🍽🍚<u><b>Ужин</b></u>: {dn_name}', parse_mode = 'html', reply_markup = btn)


@bot.message_handler(commands=['full_meal']) 
def full_m(message):
    btn = types.InlineKeyboardMarkup()
    br_id = str(rn.randint(1, 20))
    ln1_id = str(rn.randint(1, 20))
    ln2_id = str(rn.randint(21, 40))
    dn_id = str(rn.randint(1, 20))
    con = sqlite3.connect('FoodBase.db')
    cursor = con.cursor()
    cursor.execute(f'SELECT Название, url, photo_url FROM breakfast WHERE id = {br_id}')
    br_name, br_url, br_photo = cursor.fetchone()
    cursor.execute(f'SELECT Название, url, photo_url FROM lunch WHERE id = {ln1_id}')
    ln1_name, ln1_url, ln1_photo = cursor.fetchone()
    cursor.execute(f'SELECT Название, url, photo_url FROM lunch WHERE id = {ln2_id}')
    ln2_name, ln2_url, ln2_photo = cursor.fetchone()
    cursor.execute(f'SELECT Название, url, photo_url FROM dinner WHERE id = {dn_id}')
    dn_name, dn_url, dn_photo = cursor.fetchone()
    btn.add(types.InlineKeyboardButton(f'{br_name}', url = br_url))
    btn.add(types.InlineKeyboardButton(f'{ln1_name}', url = ln1_url))
    btn.add(types.InlineKeyboardButton(f'{ln2_name}', url = ln2_url))
    btn.add(types.InlineKeyboardButton(f'{dn_name}', url = dn_url))
    bot.send_media_group(message.chat.id, [types.InputMediaPhoto(br_photo), types.InputMediaPhoto(ln1_photo),
                                           types.InputMediaPhoto(ln2_photo), types.InputMediaPhoto(dn_photo)])
    bot.send_message(message.chat.id, f'☕️🥪<u><b>Завтрак</b></u>: {br_name}\n\n🍲🍞<u><b>Первое на обед</b></u>: {ln1_name}\n\n🥘🧆<u><b>Второе на обед</b></u>: {ln2_name}\n\n🍽🍚<u><b>Ужин</b></u>: {dn_name}', parse_mode = 'html', reply_markup = btn)

@bot.message_handler(commands=['breakfast'])
def breakfast(message):
    btn = types.InlineKeyboardMarkup()
    br_id = str(rn.randint(1, 20))
    con = sqlite3.connect('FoodBase.db')
    cursor = con.cursor()
    cursor.execute(f'SELECT Название, url, photo_url FROM breakfast WHERE id = {br_id}')
    br_name, br_url, br_photo = cursor.fetchone()
    btn.add(types.InlineKeyboardButton(f'{br_name}', url = br_url))
    bot.send_photo(message.chat.id, br_photo)
    bot.send_message(message.chat.id, f'☕️🥪<u><b>Завтрак</b></u>: {br_name}', parse_mode = 'html', reply_markup = btn)


@bot.message_handler(commands=['lunch'])
def lunch(message):
    btn = types.InlineKeyboardMarkup()
    ln_id = str(rn.randint(1, 40))
    con = sqlite3.connect('FoodBase.db')
    cursor = con.cursor()
    cursor.execute(f'SELECT Название, url, photo_url FROM lunch WHERE id = {ln_id}')
    ln_name, ln_url, ln_photo = cursor.fetchone()
    btn.add(types.InlineKeyboardButton(f'{ln_name}', url = ln_url))
    bot.send_photo(message.chat.id, ln_photo)
    bot.send_message(message.chat.id, f'🍲🥘<u><b>Обед</b></u>: {ln_name}', parse_mode = 'html', reply_markup = btn)


@bot.message_handler(commands=['dinner'])
def dinner(message):
    btn = types.InlineKeyboardMarkup()
    dn_id = str(rn.randint(1,20))
    con = sqlite3.connect('FoodBase.db')
    cursor = con.cursor()
    cursor.execute(f'SELECT Название, url, photo_url FROM dinner WHERE id = {dn_id}')
    dn_name, dn_url, dn_photo = cursor.fetchone()
    btn.add(types.InlineKeyboardButton(f'{dn_name}', url = dn_url))
    bot.send_photo(message.chat.id, dn_photo)
    bot.send_message(message.chat.id, f'🍽<u><b>Ужин</b></u>: {dn_name}', parse_mode = 'html', reply_markup = btn)


@bot.message_handler(commands=['random'])
def random(message):
    category = rn.randint(1, 3)
    if category == 1:
        breakfast(message)
    if category == 2:
        lunch(message)
    if category == 3:
        dinner(message)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'Вот комманды, которые Вы можете использовать:\n\n/hub - вернуться в хаб\n/full_meal - рацион на день\n/breakfast - завтрак\n/lunch - обед(первое и второе)\n/dinner - ужин\n\n/random - случайное блюдо из любой категории')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} 🍝!\n\nЧто вас интересует?\n\n/help - помощь по командам' )
    elif message.text.lower() == 'завтрак':
        breakfast(message)
    elif message.text.lower() == 'обед':
        lunch(message)
    elif message.text.lower() == 'ужин':
        dinner(message)

bot.infinity_polling()
