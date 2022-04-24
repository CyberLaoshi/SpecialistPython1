# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
def ran_num(amount, low, high):
    lst = []
    for _ in range(amount):
        lst.append(random.randint(low, high))
    return lst
lst1 = ran_num(3, 0, 100)
print(lst1)
fewer_than_ten = [x for x in lst1 if x < 10]
print(len(fewer_than_ten))
# 2. Сумму всех положительных элементов списка
sum_positives = sum([x for x in lst1 if x > 0])
print(sum_positives)
# 3. Среднее арифметическое всех четных элементов
even_numbers = [x for x in lst1 if x % 2 == 0]
print(even_numbers)
average_even = sum(even_numbers) / len(even_numbers)
print(average_even)
