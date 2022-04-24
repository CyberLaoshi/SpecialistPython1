# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
def days_in_year(num_year):
    days = 365
    if num_year % 4 == 0:
        days = 366
        if num_year % 100 == 0 and num_year % 400 == 0:
            days = 365
    return days

def days_in_month(month, year):
    thirty_one = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    if month in thirty_one:
        return 31
    if month in thirty:
        return 30
    if days_in_year(year) == 365:
        return 28
    if days_in_year(year) == 366:
        return 29

while True:
    sent = input("Введите два целых числа – номер месяца и номер года: ")
    try:
        month, year = sent.split(" ")
        month = int(month)
        year = int(year)
        if not 0 < month <= 12 or not year >= 0:
            raise ValueError
        print(days_in_month(month, year))
        break
    except ValueError:
        print("Неверное число")
