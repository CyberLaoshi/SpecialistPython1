# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["банан", "киви", "арбуз", "авокадо", "гранат"]

# TODO: your code here
max_length = 0
for fruit in fruits:
    current_length = len(fruit)
    if current_length > max_length:
        max_length = current_length
for count, value in enumerate(fruits, 1):
    difference = max_length - len(value)
    print(count, ". " + " " * difference, value)
# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
