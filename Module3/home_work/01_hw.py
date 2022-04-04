# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names_new = ""
for i, name in enumerate(names, 1):
    if i != len(names):
        names_new = names_new + name + ", "
    else:
        names_new = names_new + name
print(names_new)
# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
