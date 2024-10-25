import random

# Генерация последовательности случайных чисел
def generate_sequence(length):
    return [random.randint(0, 9) for _ in range(length)]
