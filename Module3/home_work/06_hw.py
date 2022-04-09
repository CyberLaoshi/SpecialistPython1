# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 1000
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here
brand_list = []
for item in items:
    if item["brand"] not in brand_list:
        brand_list.append(item["brand"])
print(", ".join(brand_list))

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

# Вариант 1
# done = False
# brand_quantity_list = []
# for item in items:
#     done = False
#     for thing in brand_quantity_list:
#         if item["brand"] == thing["brand"]:
#             thing["quantity"] += 1
#             done = True
#     if done == False:
#             brand_quantity_list.append(dict(brand=item["brand"], quantity = 1))
# brand_quantity_list.sort(key=lambda x: x.get('quantity'), reverse=True)
# print(brand_quantity_list[0]["brand"])

# Вариант 2
# brand_checked_list = []
# brand_quantity_dic = {}
# for item in items:
#     if item["brand"] in brand_checked_list:
#         brand_quantity_dic[item["brand"]] += 1
#     else:
#         brand_checked_list.append(item["brand"])
#         brand_quantity_dic[item["brand"]] = 1
# print(max(brand_quantity_dic, key = brand_quantity_dic.get))

# Вариант 3
from collections import Counter
cnt = Counter()
for item in items:
    cnt[item["brand"]] += 1
print(max(cnt))

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
items.sort(key=lambda x: x.get("price"), reverse=True)
print(items[0]["brand"])
