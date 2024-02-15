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
