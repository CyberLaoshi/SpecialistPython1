# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.
import random

def gen_list(size, of, to):
    random_nums = []
    for _ in range(size):
        random_nums.append(random.randint(of, to))
    return random_nums

values = (1, -5, 10)
print(gen_list(*values))
