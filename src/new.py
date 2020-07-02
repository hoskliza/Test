import telebot;

bot = telebot.TeleBot('');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):