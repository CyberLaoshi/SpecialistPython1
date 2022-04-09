# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Вячеслав", "Ирина", "Василий", "Петр"]

# TODO: your code here
# Вариант 1
# longest_name_length = 0
# longest_name_index = 0
# for index, name in enumerate(names):
#     if len(name) > longest_name_length:
#         longest_name_length = len(name)
#         longest_name_index = index
# print(names[longest_name_index])

# Вариант 2
# length_list = []
# for name in names:
#     length_list.append(len(name))
# print(names[length_list.index(max(length_list))])

# Вариант 3
names.sort(key=len, reverse = True)
print(names[0])
