# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
location = [(8, 15), (12, 18), (10, 25)]
def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

dist_ab = distance(*location[0], *location[1])
dist_bc = distance(*location[1], *location[2])
dist_ac = distance(*location[0], *location[2])

dist_list = {"AB": dist_ab, "BC": dist_bc, "AC": dist_ac}
# TODO: your code here
print("Самый короткий отрезок:", min(dist_list))  # Выводим название отрезка, например “АС”.
