# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
list_numbers = [4, 5, 1, -4, 2, -3]
total = 0

# Вариант 1
# for num in list_numbers:
#     total += num

# Вариант 2
total = sum(list_numbers)
print(total)
