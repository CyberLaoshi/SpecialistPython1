# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
list_numbers = [20, 5, 1, -4, 2, -3]
total = 0

for num in list_numbers:
    total += num if num >= 0 else 0

print(total)
