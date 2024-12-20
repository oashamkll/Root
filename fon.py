# Установка темно-синего фона в терминале Termux
def set_background():
    # ANSI код для темно-синего фона
    print("\033[44m")  # Устанавливает фон на темно-синий
    print("\033[2J")   # Очищает экран

def reset_terminal():
    # Сброс цветов к стандартным
    print("\033[0m")

try:
    set_background()
    input("Темно-синий фон активен. Нажмите Enter для выхода...")
finally:
    reset_terminal()
