import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import config
from pyowm.utils import timestamps
import pyowm
config_dict = get_default_config()
owm = pyowm.OWM('31d1ad9fac528e02417756ad22dbf0e4')
config_dict['language'] = 'ru'
bot = telebot.TeleBot("6073138429:AAFFPZ52agv4uW0WuDcg-tzL8e0kpp_bUq8")
@bot.message_handler(commands=['start', 'help'])
@bot.message_handler (conntent_types=['text'])
def send_welcome(message):
    bot.send_message (message.chat.id, "Назови город в котором мне нужно узнать погоду")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  try:
	  mgr=owm.weather_manager()
	  observation = mgr.weather_at_place( message.text )
	  w = observation.weather
	  a = w.temperature('celsius')["temp"]
	  answer="В городе "+ message.text + " сейчас " + w.detailed_status+'\n'
	  answer+="Температура:"+str(a)+'\n\n'
	  if a > +30:
	    answer += "Сейчас довольно жарко, будь внимательней и не перегрейся на солнце)"
	  elif a > +20:
	    answer += "Отличная погода, чтобы прогуляться"
	  else:
	    answer += "Там прохладно, будь внимательнее"
	  bot.send_message(message.chat.id, answer)
  except:
	  bot.send_message(message.chat.id,'Ошибка! Город не найден.')
bot. polling(non_stop=True)