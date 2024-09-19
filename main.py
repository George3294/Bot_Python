import telebot
from telebot import types
import sqlite3

token = '6816017020:AAGbb3BOczYoI8OlT47YepkX1d716PUgkF0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Вас приветсвует новый бот помощник напиши /help и узнаешь что можешь делать )))")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, " Вам доступны команды /low, /high, /custom, /history")

@bot.message_handler(commands=['low'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти в поисковую систему, самых низких цен на авто", url = "https://auto.ru/saratov/cars/all/do-100000/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

@bot.message_handler(commands=['high'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти в поисковую систему, самых высоких цен на авто", url = "https://auto.ru/mag/article/samye-dorogie-mashiny-v-mire-rekordnye-cennik/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


@bot.message_handler(commands=['custom'])
def help_price(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url_button = types.KeyboardButton("до 1.000.000")
    url_button_2 = types.KeyboardButton("от 1.000.000 до 2.000.000")
    url_button_3 = types.KeyboardButton("от 2.000.000 до 3.000.000")
    url_button_4 = types.KeyboardButton("Можете посмотреть машины, с автоматической коробкой передач")
    url_button_5 = types.KeyboardButton("Можете выбрать автомобиль, с механической коробкой передач")
    url_button_6  = types.KeyboardButton("Можете посмотреть кузов универсал")
    url_button_7 = types.KeyboardButton("Можете посмотреть кузов хетч-бек")
    url_button_8 = types.KeyboardButton("Можете посмотреть кузов седан")
    keyboard.add(url_button, url_button_2, url_button_3, url_button_4, url_button_5, url_button_6, url_button_7, url_button_8)
    bot.send_message(message.chat.id, "Привет, так же вы можете выбрать цену сами \n Также вы можете выбрать автомобиль"
                      " c автоматической коробкой передач и механической коробкой передач\n"
                      "А еще вы можете посмотреть разные кузовы автомобилей", reply_markup=keyboard)
@bot.message_handler(content_types = 'text')
def message_replay(message):
    if message.text == "до 1.000.000":
        bot.send_message(message.chat.id, "https://auto.ru/saratov/cars/used/?price_to=1000000")
    if message.text == "от 1.000.000 до 2.000.000":
        bot.send_message(message.chat.id, "https://auto.ru/saratov/cars/used/?price_from=1000000&price_to=2000000")
    if message.text == "от 2.000.000 до 3.000.000":
        bot.send_message(message.chat.id, "https://auto.ru/saratov/cars/used/?price_from=2000000&price_to=3000000")
    if message.text == "Можете посмотреть машины, с автоматической коробкой передач":
        bot.send_message(message.chat.id,"https://auto.ru/saratov/cars/used/?transmission=AUTOMATIC" )
    if message.text == "Можете выбрать автомобиль с механической коробкой передач":
        bot.send_message(message.chat.id,"https://auto.ru/saratov/cars/used/transmission-mechanical/" )
    if message.text == "Можете посмотреть кузов универсал":
        bot.send_message(message.chat.id,"https://auto.ru/saratov/cars/all/body-wagon/" )
    if message.text == "Можете посмотреть кузов хетч-бек":
        bot.send_message(message.chat.id,"https://auto.ru/saratov/cars/all/body-hatchback/" )
    if message.text == "Можете посмотреть кузов седан":
        bot.send_message(message.chat.id,"https://auto.ru/saratov/cars/all/body-sedan/" )


# Создание подключения к базе данных
conn = sqlite3.connect('history.db')
c = conn.cursor()

# Создание таблицы для хранения истории запросов
c.execute('''CREATE TABLE IF NOT EXISTS requests
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
             command TEXT)''')

# Функция для добавления запроса в историю
def add_request(command):
    c.execute("INSERT INTO requests (command) VALUES (?)", (command,))
    conn.commit()

# Функция для получения последних десяти запросов
def get_history():
    c.execute("SELECT * FROM requests ORDER BY timestamp DESC LIMIT 10")
    rows = c.fetchall()
    return rows

# Пример использования функций
add_request('/low')
add_request('/high')
add_request('/custom')

history = get_history()
for row in history:
    print(row)

# Закрытие подключения к базе данных
conn.close()

bot.infinity_polling()