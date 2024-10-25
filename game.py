import tkinter as tk
import random
from utils import generate_sequence


# Класс игры, где отображаются числа для запоминания
class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.sequence = []
        self.user_input = ""
        self.setup_game_interface()

    # Интерфейс игры
    def setup_game_interface(self):
        self.label = tk.Label(self.frame, text="Нажмите 'Начать', чтобы начать игру")
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.frame, text="Начать", command=self.start_game)
        self.start_button.pack()

    # Логика запуска игры
    def start_game(self):
        self.sequence = generate_sequence(5)
        self.show_sequence()

    # Показ последовательности чисел
    def show_sequence(self):
        self.label.config(text=" ".join(map(str, self.sequence)))
        self.root.after(2000, self.clear_sequence)

    # Скрытие последовательности и начало ввода
    def clear_sequence(self):
        self.label.config(text="Введите числа по памяти")
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        self.entry.bind("<Return>", self.check_sequence)

    # Проверка правильности введенных данных
    def check_sequence(self, event):
        self.user_input = self.entry.get().split()
        if self.user_input == list(map(str, self.sequence)):
            self.label.config(text="Верно!")
        else:
            self.label.config(text="Неверно. Попробуйте снова!")
        self.entry.delete(0, tk.END)
