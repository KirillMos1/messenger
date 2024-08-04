import main, menu, nick_edit, create_chat, talking, os

def s():
	chats_list = []
	for i in main.chats:
		chats_list.append(i)
	main.os.system('cls' if os.name == 'nt' else 'clear')
	print("""
Выберите чат:""")

	for j in chats_list:
		print(f"\n{j}")

	select_chat_list = input("""

Вводите ---> """)
	talking.t(select_chat_list)
