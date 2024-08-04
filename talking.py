import main, menu, selector, create_chat, nick_edit, invite_chat, os

def t(chat_name):
	try:
		chat_ptof = open("/data/chats_info/" + chat_name + "/", "r")
		chat_chat = open("/data/chats_info/" + chat_name + "/" + "chat.txt", "+a")
		chat_key = open("/data/chats_info/" + chat_name + "/" + "key.txt", "r")
		key_checking = input("""
Введите ключ что бы получить доступ
к чату
Вводите ---> """)
		if key_checking == chat_key.read():
			main.os.system('cls' if os.name == 'nt' else 'clear')
			print("""
Доступ получен""")
			main.sleep(3)
			main.os.system('cls' if os.name == 'nt' else 'clear')
			command = input("""
Выберите действие:
h - прочитать переписку
s - отправить сообщение
d - удалить чат
Вводите ---> """)
			if command == "h":
				for i in chat_chat.read():
					print(i)
		else:
			main.os.system('cls' if os.name == 'nt' else 'clear')
			print("""
К сожалению, вы ввели неправильный пароль.
Доступ не предоставляется.
Возвращаем Вас в меню""")
		main.sleep(5)
		menu.main_menu()
	except:
		main.os.system('cls' if os.name == 'nt' else 'clear')
		print("""
Ошибка InputError
Описание: Введено несуществующее название
чата
Код: 1
Вас перенаправит обратно в меню""")
		main.sleep(5)
		menu.main_menu()
