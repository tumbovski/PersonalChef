# Telegram bot "Personal Chef" 

***
_Данный бот был выполнен в качестве проекта на весннюю_
_практику студентами ДВФУ_
***


Бот позволяет разширять свой кулинарный кругозор и будет предлагать пользователю блюда с сылками на рецепты.


Проект полностью выполнен на языке Python с использованием библиотек:
- Telegram Bot API (telebot)
- json
- SQLite3
- random


### Команды бота


- __/start__ - первая команда которую вводит пользователь при   заходе в бота. Во время выполнения данной команды данные о пользователе (username, first name, last name, Telegram ID) сохраняются в _json_ файл _usersData.json_ (также предусмотрена проверка на уникального пользователя)
- __/hub__ - возвращает пользователя в хаб, из которого при помощи встроенных кнопок пользователь может выбрать интересующую его опцию
- __/full_meal__ - выдаёт пользователю из базы данных _FoodBase.db_ при помощи библиотеки _random_ блюдо на завтрак, первое, второе на обед и блюдо на ужин с фотографиями и ссылками на рецепты в виде приложенных к сообщению кнопок
- __/breakfast__ - выдаёт пользователю случайный завтрак по аналогии с _/full_meal_ (далее тоже)
- __/lunch__ - выдаёт пользователю случайный обед
- __/dinner__ - выдаёт пользователю случайный ужин
- __/random__ - выдаёт пользователю случайное блюдо из любой категории
- __/help__ - выдаёт пользователю список команд с описанием


### Примеры использования библиотек

- Teelgram Bot API:
```py
@bot.message_handler(commands=['hub'])
def hub(message):
    file = open('./helloPhoto.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Рацион на день", callback_data = 'day_meal'))
```
- json:
```py
with open('usersData.json', 'w', encoding = 'utf-8') as f:
    lst.append(user_data)
    json.dump(lst, f, indent = 4, ensure_ascii = False)
```
- SQLite3:
```py
con = sqlite3.connect('FoodBase.db')
cursor = con.cursor()
cursor.execute(f'SELECT Название, url, photo_url FROM breakfast WHERE id = {br_id}')
br_name, br_url, br_photo = cursor.fetchone()
btn.add(types.InlineKeyboardButton(f'{br_name}', url = br_url))
```

- random:
```py
br_id = str(rn.randint(1, 20))
```

### Пример использования бота

![](/example.jpg)