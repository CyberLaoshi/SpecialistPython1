# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
# Вариант 1
print(max(tup))

# Вариант 2
max_num = 0
for num in tup:
    max_num = num if num > max_num else max_num
print(max_num)
