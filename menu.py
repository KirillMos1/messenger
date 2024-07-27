import main
from main import *


def main_menu():
	main.os.system('cls' if os.name == 'nt' else 'clear')
	print(f"""
	
Привет, {main.user}!""")