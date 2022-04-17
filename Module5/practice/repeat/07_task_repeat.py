# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает число -
# сколько денег получит Иван в результате.

def deposit(x, a, n):
    total = x * ((1 + a / 100) ** n)
    return round(total, 2)
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.

test = deposit(100, 100, 1)

print(test)
