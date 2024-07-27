import os.path
import time
from time import *

import menu

ptof = open("data/ptof.txt", "r")
open_folder = "" # изменяется
chat = "" # изменяется
username = open("data/username.txt", "+w")
setup = open("data/setup-ready.txt", "+w")

mess = "" # переменная для ввода
user = username.read()
chat_history = "" # изменяется
new_username = "" # для ввода
path_chat = "" # для ввода
name_chat = "" # для ввода

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
	new_username = input("""
Введите Ваш никнейм.
Никнейм нужен для того, чтобы участ-
ники чата могли Вас узнать.
Никнейм может состоять из английских
букв и цифр. Желательно, чтобы Ваш
никнейм был не длиннее 10 символов.
Вводите ---> """)
	
	name_chat = input("""
Отлично. Теперь нужно название для
Вашего чата. Оно может состоять 
только из английских букв. Длина
до 10 символов.
Вводите ---> """)
	path_chat = input("""

									 
Теперь Вам предстоит создать локаль-
ную папку. Для этого проверьте, что 
у Вас и нового собеседника отобража-
ется хоть один компьютор с открытой
папкой. Там создайте еще одну папку
с названием mess. После, скопируйте
путь и вставьте сюда.
Вводите ---> """)
	
	os.makedirs("./data/chats_info/" + name_chat, exist_ok=True)
	os.makedirs(path_chat + "/" + name_chat, exist_ok=True)
	ptof_chat = open("data/chats_info/" + name_chat + "/ptof.txt", "+x")
	ptof_chat.write(path_chat)
	username.write(new_username)
	
	setup.write("True")

def login_status():
	if bool(setup.read()):
		menu.main_menu()
	else:
		reg()

login_status()