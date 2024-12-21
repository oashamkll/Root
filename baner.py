import os
import pyfiglet
from colorama import init, Fore

# Инициализация Colorama
init(autoreset=True)

# Функция для отображения статичного баннера
def print_banner():
    purple_color = Fore.MAGENTA  # Используем фиолетовый цвет

    # Генерация большого текста с помощью pyfiglet
    banner_text = pyfiglet.figlet_format("HACK ROOT", font="big")  # Используем крупный шрифт
    width = os.get_terminal_size().columns  # Ширина экрана
    height = os.get_terminal_size().lines  # Высота экрана
    
    banner_lines = banner_text.splitlines()
    banner_height = len(banner_lines)
    banner_width = len(banner_lines[0])
    
    # Вычисляем отступы для центрирования по горизонтали и вертикали
    spaces_horizontally = (width - banner_width) // 2
    spaces_vertically = (height - banner_height) // 2

    os.system('cls' if os.name == 'nt' else 'clear')  # Очистить терминал
    # Добавляем вертикальные отступы для центрирования
    print("\n" * spaces_vertically)
    # Печатаем сам баннер с горизонтальными отступами
    for line in banner_lines:
        print(" " * spaces_horizontally + purple_color + line)

# Запуск баннера
print_banner()
