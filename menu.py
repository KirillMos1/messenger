import main, selector, nick_edit, create_chat, invite_chat, talking


def main_menu():
	main.os.system('cls' if os.name == 'nt' else 'clear')
	print(f"""
	
Привет, {main.user}! Ты попал в меню
программы FoKas Local Messenger! Вы-
берите опцию, что бы продолжить:
s -----------> выбрать чат
n ----------> изменить ник
c -----------> создать чат
i -------> присоедениться к
чату
""")
	command = input("""
Вводите ---> """)
	if command == "s":
		selector.s()
	elif command == "n":
		nick_edit.n_e()
	elif command == "c":
		create_chat.c_c()
	elif command == "i":
		invite_chat.i_c()
	else:
		print("""
Некорректный ввод. Повторите
ввод данных.

""")
		main.sleep(5)
		main_menu()