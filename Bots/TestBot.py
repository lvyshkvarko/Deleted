import telebot

bot = telebot.TeleBot("1675463126:AAFaFBlsB6bo4V3WEF9su7UM1wduTai7RHc", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Ты попал(-а) в самую магическую игру-терпапию. Начнем?")


@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, message.chat.first_name + ', здравствуйте!')
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBdOxgzFavLbl_Z6SpTXHYrRJm_r52pwACyg0AApFgIUix94gF8D5V-B8E")


bot.polling()