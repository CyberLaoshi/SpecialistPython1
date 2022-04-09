# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import math
random_list_num = [2, -5, 8, 9, -25, 25, 4, 3, 100, -110, -100, 121, 225]
new_list_num = []

# Вариант 1
# for num in random_list_num:
#     square_root = num ** .5
#     if type(square_root) != complex:
#         if square_root - int(square_root) == 0:
#             new_list_num.append(int(square_root))
# print(new_list_num)

# Вариант 2
filtered = filter(lambda num: num > 0 and math.isqrt(num) ** 2 == num, random_list_num)
for item in filtered:
    new_list_num.append(int(math.sqrt(item)))
print(new_list_num)
