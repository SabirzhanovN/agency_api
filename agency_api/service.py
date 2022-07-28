import telepot

token = '5480532945:AAHotdH0GrwycxQcnOF1D4_LxhyvHkhO14A'
my_id = '1404363032'
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")
