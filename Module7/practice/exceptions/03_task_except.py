# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
sent = "2 12 -45 7 10 0.3"
try:
    list = [int(x) for x in sent.split(" ")]
    print(min(list))
except ValueError:
    print("Есть нечисловое значение")
