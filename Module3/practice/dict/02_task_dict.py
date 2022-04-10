# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]
dictOne = {}
# TODO: your code here
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}
# Вариант 1
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     dictOne[key] = value
# print(dictOne)

# Вариант 2
new_dict = {x: values[keys.index(x)] for x in keys}
print(new_dict)
