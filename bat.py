import telebot;
bot = telebot.TeleBot('1568376034:AAEqko9CU5J2cDaAUy232IMuFTesL9SpRV4');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
      if message.text == 'привет':
            bot.send_message(message.from_user.id, 'привет, чем могу помочь?')
      elif message.text == '/help':
            bot.send_message(message.from_user.id, 'напиши привет')
      else:
            bot.send_message(message.from_user.id,'не понимаю. напиши /help')
bot.polling(none_stop=True, interval=0)
      
