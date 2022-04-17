# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# TODO: your code here
equation_one = "-2/3 - -2"
int_split_string = []
if equation_one.find(" + ") != -1:
    list_split = equation_one.split(" + ")
if equation_one.find(" - ") != -1:
    list_split = equation_one.split(" - ")
for el in list_split:
    n_value = el[:el.find(" ")] if el.find(" ") != -1 else 0
    n_value = el if el.find(" ") == -1 and el.find("/") == -1 else n_value
    x_value = el[el.find(" ") + 1:el.find("/")] if el.find("/") != -1 else 0
    y_value = el[el.find("/") + 1:] if el.find("/") != -1 else 0
    int_split_string.append(dict(n=n_value, x=x_value, y=y_value))
if equation_one.find(" - ") != -1:
    if int_split_string[1]["n"] != 0:
        int_split_string[1]["n"] = int(int_split_string[1]["n"]) * -1
    elif int_split_string[1]["x"] != 0:
        int_split_string[1]["x"] = int(int_split_string[1]["x"]) * -1
denominator = 1
total_numerator = 0
for el in int_split_string:
    el["n"] = int(el["n"])
    el["x"] = int(el["x"])
    el["y"] = int(el["y"])
for num in int_split_string:
    if num["y"] != 0:
        denominator = denominator * num["y"]
for num in int_split_string:
    sign_value = 1
    if (num["n"] < 0 and num["x"] > 0) or (num["n"] >= 0 and num["x"] < 0):
        sign_value = -1
    if num["y"] != 0:
        total_numerator = total_numerator + sign_value * (abs(num["n"]) * denominator + abs(num["x"] * denominator / num["y"]))
    if num["y"] == 0 and num["n"] > 0:
        total_numerator = total_numerator + sign_value * (abs(num["n"]) * denominator)
total_int = sign_value * (abs(total_numerator) // denominator)
if total_int == 0 and total_numerator < 0:
    total_int = "-"
total_numerator = abs(total_numerator) % denominator
for i in [2, 3, 5, 7]:
    while total_numerator % i == 0 and denominator % i == 0:
        total_numerator = total_numerator // i
        denominator = denominator // i
total = {"n":int(total_int), "x": int(total_numerator), "y": int(denominator)}
print(total["n"], " ", total["x"], "/", total["y"],sep="")
