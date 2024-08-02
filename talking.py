import main, menu, selector, create_chat, nick_edit, invite_chat

def t(chat_name):
	try:
		chat_ptof = open("/data/chats_info/" + chat_name + "/", "r")
		chat_chat = open("/data/chats_info/" + chat_name + "/" + "chat.txt", "+a")
	except:
		main.os.system('cls' if os.name == 'nt' else 'clear')
		print("""
Ошибка InputError
Описание: Введено несуществуещее название
чата
Код: 1
Вас перенаправит обратно в меню""")
		main.sleep(5)
		menu.main_menu()