# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import math
from operator import itemgetter

# Создадим функцию, которая преобразует таблицу в словарь,
# где key - имя и фамилия сотрудника, value - словарь,
# в котором key - название колонки из таблицы сотрудников, value - содержимое ячейки(имя, зп, часы)
def table_scan(text):
    categories = []
    people = {}
    for index, line in enumerate(text):
        line = line.rstrip().split(" ")
        line = list(filter(None, line))
        if index != 0:
            person = {}
            for category, info in zip(categories, line):
                person[category] = info
            names = person["Фамилия"] + " " + person["Имя"]
            people[names] = person
        else:
            for el in line:
                categories.append(el)
    return(people)

file = 'dir/workers.txt'
with open(file, "r", encoding="utf-8") as f:
    people = table_scan(f)
    for person in people.values():
        person["Оклад"] = int(person["Зарплата"]) / int(person["Норма_часов"])
hours = 'dir/hours_of.txt'
with open(hours, "r", encoding="utf-8") as f:
    hour_people = table_scan(f)
    for name, info in people.items():
        # Добавляем графу отработанных часов в общий словарь
        info["Отработано"] = hour_people[name]["Отработано"]
        # Преобразуем числа из string в float
        for key, value in info.items():
            try:
                info[key] = float(value)
            except ValueError:
                info[key] = str(value)
        # Сравниваем часы и считаем зарплату
        hours_worked = info["Отработано"]
        hours_min = info["Норма_часов"]
        hour_wage = info["Оклад"]
        if hours_worked < hours_min:
            info["Зарплата фактическая"] = math.floor(hour_wage * hours_worked)
        if hours_worked > hours_min:
            extra_hours_payment = (hours_worked - hours_min) * 2 * hour_wage
            info["Зарплата фактическая"] = info["Зарплата"] + extra_hours_payment
            info["Зарплата фактическая"] = math.floor(info["Зарплата фактическая"])
        result = itemgetter("Фамилия", "Имя", "Норма_часов", "Отработано", "Зарплата фактическая")(info)
        result_text = f"Сотрудник {result[0]} {result[1]} при норме {result[2]} отработал {result[3]} и заработал {result[4]}"
        print(result_text)


    #     hours_worked = float(person["Отработано"])
    #     hours_min = float(person["Норма_часов"])
    #     hour_wage = float(person["Оклад"])
    #     if hours_worked < hours_min:
    #         person["Зарплата фактическая"] = math.floor(hour_wage * hours_worked)
    #     if hours_worked > hours_min:
    #         extra_hours = hours_worked - hours_min
    #         person["Зарплата фактическая"] = float(person["Зарплата"]) + extra_hours * 2 * hour_wage
    #         person["Зарплата фактическая"] = math.floor(person["Зарплата фактическая"])
    #     result = itemgetter("Фамилия", "Имя", "Норма_часов", "Отработано", "Зарплата фактическая")(person)
    #     result_text = f"Сотрудник {result[0]} {result[1]} при норме {result[2]} отработал {result[3]} и заработал {result[4]}"
    #     print(result_text)
