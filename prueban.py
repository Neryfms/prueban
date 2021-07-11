import telebot

bot = telebot.TeleBot("1870547467:AAE60nhk7RWqvdvN0p2PExv86MoacMzYEF4")

@bot.message_handler(commands=["hola1" ])
def hola1 (mensaje):
    bot.reply_to(mensaje, "Hola, un gusto saludarte, ¿cómo estás?")
    print ("hola")

@bot.message_handler(commands=["comoestas2"]) 
def comoestas2 (mensaje):
    bot.reply_to(mensaje, "Estoy muy bien, ¿y tu?")
    print("como estas")

bot.polling()