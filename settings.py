import tkinter as tk
import json
import os

SETTINGS_FILE = "settings.json"


# Окно настроек для выбора размеров окна
class SettingsWindow:
    def __init__(self, root, memory_game):
        self.root = root
        self.memory_game = memory_game
        self.window = tk.Toplevel(self.root)
        self.window.title("Настройки")

        tk.Label(self.window, text="Выберите размер окна:").pack(pady=10)
        self.size_var = tk.StringVar(value=self.load_settings().get("window_size", "400x400"))

        tk.Entry(self.window, textvariable=self.size_var).pack(pady=10)
        tk.Button(self.window, text="Сохранить", command=self.save_settings).pack(pady=10)

    # Загружаем настройки из файла
    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        return {}

    # Сохраняем выбранные настройки
    def save_settings(self):
        window_size = self.size_var.get()
        with open(SETTINGS_FILE, "w") as f:
            json.dump({"window_size": window_size}, f)
        self.memory_game.update_window_size(window_size)
        self.window.destroy()
