# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)

# 1. Открываем файл с зарплатами для чтения. Создаем словарь с категориями и данными.
with open('dir/salaries.txt', "r", encoding="utf-8") as h:
    categories = []
    people = []
    for index, line in enumerate(h):
        line = line.rstrip().split(" ")
        line = list(filter(None, line))
        if index != 0:
            person = {}
            for category, info in zip(categories, line):
                person[category] = info
            people.append(person)
        else:
            for el in line:
                categories.append(el)
# 2. Создаем новый файл с именами людей, которые подходят под критерий
from operator import itemgetter
with open('dir/highly_paid.txt', "w", encoding="utf-8") as f:
    high_paid_people = list(filter(lambda x: int(x["Зарплата"]) > 60000, people))
    get_name = lambda x, y, z: str(f"{x} {y[0]}. {z[0]}.")
    f.write(get_name(*categories[0:3]) + '\n')
    for person in high_paid_people:
        name = itemgetter("Фамилия", "Имя", "Отчество")(person)
        f.write(get_name(*name) + '\n')
