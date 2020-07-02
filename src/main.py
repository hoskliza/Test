import telebot
import requests

tokenbot = ""
token = ""
url = "https://api.vk.com/method/{method}?{params}&access_token={token}&v={version}"
method = "docs.search"
v = 5.68

bot = telebot.TeleBot("")

data = {}


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Привет! Я най книгу, которая тебе нужна. Напиши ее автора и название!")


@bot.message_handler(content_types=["text"])
def find(message):
    user = message.chat.id
    query = message.text
    data[user] = query[:10]
    params = "q={0}&count"
    # скачиваем ссылки по нужному нам запросу
    items = []
    for i in range(0, 5):
        print("downloading - {}".format(i))
        response = requests.get(url.format(method=method, version=v, params=params.format(query, 0), token=token))
        result = response.json()
        count = result['response']['count']
        items += result['response']['items']

    # выводим ссылки на скачивание
    for item in items[:5]:
        bot.send_message(item['url'], item[['ext']])


bot.polling(none_stop=True)

for i in range(0, 5):
    print("downloading - {}".format(i))
    response = requests.get(url.format(method=method, version=v, params=params.format(query, 0), token=token))
    result = response.json()
    count = result['response']['count']
    items += result['response']['items']

    # выводим ссылки на скачивание
for item in items[:5]:
    bot.send_message(user, item['url'], item['ext'])

bot.polling(none_stop=True)
