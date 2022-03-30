# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

a = int(input("a: "))
for i in range(a):
    if i == 0 or i == a-1:
        hashtag = "#"
        result = ""
        for j in range(a):
            result = result + hashtag
        print(result)
    if 0 < i < (a-1):
        hashtag = "#"
        space = " "
        result = "#"
        for j in range(a-2):
            result = result + space
        result += hashtag
        print(result)
