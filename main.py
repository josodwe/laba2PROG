import tkinter as tk
from settings import SettingsWindow
from game import MemoryGame
from exceptions import handle_exception


# Основной файл, создающий главное окно
class MemoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тренировка памяти")
        self.memory_game = MemoryGame(self.root)
        self.create_menu()

    # Создаем меню с настройками
    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Настройки", command=self.open_settings)
        settings_menu.add_separator()
        settings_menu.add_command(label="Выход", command=self.root.quit)

        menu_bar.add_cascade(label="Меню", menu=settings_menu)
        self.root.config(menu=menu_bar)

    # Функция открытия окна настроек
    def open_settings(self):
        SettingsWindow(self.root, self.memory_game)


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryApp(root)
    root.mainloop()


