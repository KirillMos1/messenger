import main, menu, nick_edit, create_chat, talking

def s():
	chats_list = []
	for i in main.chats:
		chats_list.append(i)
	try:
		print("""
Выберите чат:""")
		for j in chats_list:
			print(f"\n{j}")
		select_chat_list = input("""

Вводите ---> """)
