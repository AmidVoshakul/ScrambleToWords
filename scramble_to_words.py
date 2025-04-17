import time
import string
import random


def animated_text_search(target_text, delay=0.1):
    alphabet = string.ascii_letters + string.punctuation + ' '  # Все возможные символы
    current_text = [random.choice(alphabet)
                    for _ in target_text]  # Случайные стартовые буквы

    while "".join(current_text) != target_text:  # Пока не достигнем нужного текста
        for i in range(len(target_text)):
            if current_text[i] != target_text[i]:  # Только если буква не найдена
                possible_letters = [
                    letter for letter in alphabet if letter >= current_text[i] and letter <= target_text[i]]
                if possible_letters:
                    # Меняем букву, но приближаемся к нужной
                    current_text[i] = random.choice(possible_letters)
                else:
                    # Фиксируем, если не осталось вариантов
                    current_text[i] = target_text[i]
        print("\r" + "".join(current_text), end='',
              flush=True)  # Вывод всего текста
        time.sleep(delay)

    print()  # Завершающий перенос строки


# Тестируем с "Hello world"
animated_text_search("Download free Editing Icons in design styles.")
