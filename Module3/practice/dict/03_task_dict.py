# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
# Вариант 1
# staff.sort(key=lambda x: x.get("salary"), reverse = True)
# print(staff[0]["name"], staff[0]["surname"])

# Вариант 2
high_paid_empl_list = max(staff, key=lambda x: x.get("salary"))
print(high_paid_empl_list["name"], high_paid_empl_list["surname"])
# TODO: your code here

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here
# Вариант 1
# staff.sort(key=lambda x: x.get("salary"), reverse = False)
# print(staff[0]["name"], staff[0]["surname"])

# Вариант 2
high_paid_empl_list = min(staff, key=lambda x: x.get("salary"))
print(high_paid_empl_list["name"], high_paid_empl_list["surname"])

print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here
total_sum = 0
empl_num = len(staff)
for empl in staff:
    total_sum += empl["salary"]
aver = total_sum / empl_num
print(aver)

print("Количество однофамильцев в организации")

# TODO: your code here
repeat_surname_list = []
repeat_surname_num = {}
for empl in staff:
    if empl["surname"] in repeat_surname_list:
        repeat_surname_num[empl["surname"]] += 1
    else:
        repeat_surname_list.append(empl["surname"])
        repeat_surname_num[empl["surname"]] = 1
print(repeat_surname_num)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
staff.sort(key=lambda x: x.get("salary"), reverse = False)
print(staff)
