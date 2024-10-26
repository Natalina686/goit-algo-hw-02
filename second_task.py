from collections import deque

def is_palindrome(input_string):
    # Очищуємо рядок: видаляємо пробіли і переводимо в нижній регістр
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Створюємо двосторонню чергу (deque) з символів рядка
    char_queue = deque(cleaned_string)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False  # Якщо символи не співпадають, рядок не є паліндромом
    
    return True  # Якщо всі символи співпали, рядок є паліндромом

# Приклад використання
input_string = input("Введіть рядок для перевірки: ")
if is_palindrome(input_string):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")