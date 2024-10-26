import queue
import random
import time

# Створюємо чергу заявок
request_queue = queue.Queue()

def generate_request():
    # Генеруємо нову заявку з унікальним номером.
    request_id = random.randint(1000, 9999)  # Генерація випадкового ID заявки
    request_queue.put(request_id)  # Додаємо заявку до черги
    print(f"Заявка {request_id} додана до черги.")

def process_request():
    # Обробляємо заявку з черги.
    if not request_queue.empty():
        request_id = request_queue.get()  # Видаляємо заявку з черги
        print(f"Обробка заявки {request_id}...")
        time.sleep(1)  # Імітація часу обробки
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга пуста.")

def main():
    # Головний цикл програми.
    while True:
        user_input = input("Введіть 'g' для генерації нової заявки, 'p' для обробки, або 'q' для виходу: ").strip().lower()
        
        if user_input == 'g':
            generate_request()  # Генерація нової заявки
        elif user_input == 'p':
            process_request()  # Обробка заявки
        elif user_input == 'q':
            print("Вихід з програми.")
            break
        else:
            print("Невірний ввід. Будь ласка, спробуйте ще раз.")

if __name__ == "__main__":
    main()