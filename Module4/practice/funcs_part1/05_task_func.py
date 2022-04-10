# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here
a = (10, 12)
b = (14, 18)
c = (12, 12)

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

def can_triangle(p1, p2, p3):
    # TODO: your code here
    d1 = distance(*p1, *p2)
    d2 = distance(*p1, *p3)
    d3 = distance(*p3, *p2)
    if d1 + d2 > d3 and d3 + d2 > d1 and d1 + d3 > d2:
        p = d1 + d2 + d3
        size = (p * (p - d1) * (p - d2) * (p - d3)) ** .5
        return p, size
    return False
# Не забудьте протестировать вашу функцию
print(can_triangle(a, b, c))
