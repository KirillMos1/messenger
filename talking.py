import main, menu, selector, create_chat, nick_edit, invite_chat

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
			print("""
Доступ получен""")
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