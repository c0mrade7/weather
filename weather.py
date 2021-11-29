import time
import colorama
import os
from colorama import Fore, Back, Style
colorama.init()
from pyowm import OWM
from pyowm.utils.config import get_default_config

os.system('cls' if os.name == 'nt' else 'clear')

logo = """\033[31m
 __      __   ___    __ _  | |_  | |__     ___   _ __ 
 \ \ /\ / /  / _ \  / _` | | __| | '_ \   / _ \ | '__|
  \ V  V /  |  __/ | (_| | | |_  | | | | |  __/ | |   
   \_/\_/    \___|  \__,_|  \__| |_| |_|  \___| |_|   
\033[34m
                                  Developer- @soeden1x
"""
print(logo)
try:
	os.system("termux-open-url https://t.me/joinchat/ra49fxzPRw5kNzYy")
except:
	pass

config_dict = get_default_config()
config_dict['language'] = 'ru'
place = input(Fore.MAGENTA + "Введите свой город: ")
owm = OWM('2d30572fb9d1dbd4b95b8c28a5a5c006', config_dict)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
t = w.temperature("celsius")
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

wi = w.wind()['speed']
humi = w.humidity
cl = w.clouds
st = w.status
dt = w.detailed_status
ti = w.reference_time('iso')
pr = w.pressure['press']
vd = w.visibility_distance

print(f""""В городе {place} температура {t1} °C"
Максимальная температура {t3} °C
Минимальная температура {t4} °C
Ощущается как {t2} °C
Скорость ветра {wi} м/с
Давление {pr} мм.рт.ст
Влажность {humi} %
Видимость {vd} метров
Описание {st} {dt}""")
time.sleep(15)