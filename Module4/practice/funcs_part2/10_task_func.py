# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    # TODO: your code here
    # Вариант 1
    # total = 0
    # for arg in args:
    #     total += arg
    # return total / len(args)
    # Вариант 2
    # return sum(args) / len(args)
    # Вариант 3
    import statistics
    return statistics.mean(args)


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
