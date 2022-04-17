# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
coordinates_one = {"x1": 5, "y1": 5, "R1": 1}
coordinates_two = {"x2": 7, "y2": 5, "R2": 1}


# R1*R1>(a1-a2)*(a1-a2)+(b1-b2)*(b1-b2)+R2*R2

def circle_inside(circle_one, circle_two):
    statement_one = circle_one["R1"] ** 2 > (circle_one["x1"] - circle_two["x2"]) ** 2 + (circle_one["y1"] - circle_two["y2"]) ** 2 + circle_two["R2"] ** 2
    statement_two = circle_two["R2"] ** 2 > (circle_two["x2"] - circle_one["x1"]) ** 2 + (circle_two["y2"] - circle_one["y1"]) ** 2 + circle_one["R1"] ** 2
    return statement_one or statement_two

print(circle_inside(coordinates_one, coordinates_two))
