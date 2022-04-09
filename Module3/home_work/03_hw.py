# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
random_num_list = [-100, -90, -80, -40, 30, 20, 50, 70, 99, 100]
# Вариант 1
# total = 0
# for num in random_num_list:
#     if num > 0 and num % 2 == 0:
#         total += num
# print(total)

# Вариант 2
filtered = filter(lambda num: num > 0 and num % 2 == 0, random_num_list)
print(sum(filtered))

