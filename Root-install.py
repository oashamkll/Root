import baner

import time
from colorama import Fore, Style, init

init(autoreset=True)

# Переменная для отслеживания root-доступа
has_root = False

# Функция для вывода текста с эффектом печатной машинки
def typewriter_effect(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()  # Переход на новую строку

def root_checker():
    if has_root:
        typewriter_effect("Yes Root", Fore.GREEN)
    else:
        typewriter_effect("No Root", Fore.RED)

def get_root():
    global has_root
    typewriter_effect("The process is ongoing.......", Fore.BLUE)
    time.sleep(15)  # Задержка в 15 секунд
    has_root = True
    typewriter_effect("Выполнено успешно", Fore.GREEN)

def main():
    global has_root
    while True:
        typewriter_effect("[1] root checker\n[2] получить root\nВыбирайте: ", Fore.GREEN)
        choice = input()
        
        if choice == "1":
            root_checker()
        elif choice == "2":
            get_root()
        else:
            typewriter_effect("Неверный выбор. Попробуйте снова.", Fore.RED)

if __name__ == "__main__":
    main()
