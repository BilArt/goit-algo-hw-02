import queue
from collections import deque

# Завдання 1: Система обробки заявок

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації заявок
def generate_request():
    request = "Request" + str(request_queue.qsuze() + 1)
    request_queue.put(request)
    print(f"Заявка {request} додана до черги")

# Функція для обробки заявок
    def process_request():
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Заявка {request} оброблена")
        else:
            print("Черга порожня")

# Головний цикл програми
            while True:
                generate_request()
                process_request()

# Завдання 2: Перевірка на паліндром
                
def is_palidrome(s):
    s = s.lower().replace(" ", "")
    char_queue = deque(s)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Приклади використання функції is_palindrome()
print("////////////////////////////////")
input_string_false = "Hi! Jeg hedder Artem!"
print(input_string_false)
print(is_palidrome(input_string_false))
print("////////////////////////////////")
input_string_true = "A man a plan a canal Panama"
print(input_string_true)
print(is_palidrome(input_string_true))