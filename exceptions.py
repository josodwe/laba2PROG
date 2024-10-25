import tkinter.messagebox as messagebox

# Обработка исключений в случае ошибок
def handle_exception(exc_type, exc_value, exc_traceback):
    messagebox.showerror("Ошибка", f"{exc_type.__name__}: {exc_value}")

# Подключаем обработку глобальных исключений
import sys
sys.excepthook = handle_exception
