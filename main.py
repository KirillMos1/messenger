import os.path
import time
import subprocess, talking
from time import sleep

import menu

ptof = open("data/ptof.txt", "r")
open_folder = "" # изменяется
chat = "" # изменяется
username = open("data/username.txt", "+w")
setup = open("data/setup-ready.txt", "+w")
chats = open("data/chats.txt", "+a")

mess = "" # переменная для ввода
user = username.read()

chat_history = "" # изменяется
new_username = "" # для ввода
path_chat = "" # для ввода
name_chat = "" # для ввода
key_chat = "" #для ввода

def reg():
	print("""
			 
Здравствуйте! Вы попали в программу
FoKas Local Messenger. Сейчас Вы
пройдете регистрацию в программе.
Ваши данные никто не узнает, так
как подключение к Интернету не
обязательно, но подключение к ло-
кальной сети обязательно
			 
			 """)
	sleep(7)
	subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
	new_username = input("""
Введите Ваш никнейм.
Никнейм нужен для того, чтобы участ-
ники чата могли Вас узнать.
Никнейм может состоять из английских
букв и цифр. Желательно, чтобы Ваш
никнейм был не длиннее 10 символов.
Вводите ---> """)
	time.sleep(2)
	subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
	name_chat = input("""
Отлично. Теперь нужно название для
Вашего чата. Оно может состоять 
только из английских букв. Длина
до 10 символов.
Вводите ---> """)
	time.sleep(2)
	subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
	path_chat = input("""

									 
Теперь Вам предстоит создать локаль-
ную папку. Для этого проверьте, что 
у Вас и нового собеседника отобража-
ется хоть один компьютор с открытой
папкой. Там создайте еще одну папку
с названием mess. После, скопируйте
путь и вставьте сюда.
Вводите ---> """)
	time.sleep(2)
	subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
	key_chat = input("""


Супер! До конца осталось немного - 
надо ввести специальный ключ для
чата. Данный ключ нужен для защиты
Вашего чата от посторонних. 
Ключ может содержать только англий-
ские буквы и цифры. Длина не огра-
ничена
Вводите ---> """)
	time.sleep(7)
	subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
	
	os.makedirs("./data/chats_info/" + name_chat, exist_ok=True)
	os.makedirs(path_chat + "/" + name_chat, exist_ok=True)
	ptof_chat = open("data/chats_info/" + name_chat + "/ptof.txt", "+x")
	ptof_chat.write(path_chat)
	username.write(new_username)
	chat_ptof = open(path_chat + "/" + name_chat + "/chat.txt", "+x")
	key_ptof = open(path_chat + "/" + name_chat + "/key.txt", "+x")
	key_ptof.write(key_chat)
	chats.write(name_chat)
	setup.write("True")

	global user
	user = username.read()

def login_status():
	if bool(setup.read()) == True:
		menu.main_menu()
	else:
		reg()

login_status()