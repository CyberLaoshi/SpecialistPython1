# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количество товара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите цену всех товаров с названием "name" в долларах

item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12

# TODO: your code here
total = float(item["price"]) / dollar_rate * float(item["count"])
print(total)
