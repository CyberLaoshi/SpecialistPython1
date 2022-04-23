# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
file='dir/items_sold.txt'
with open(file) as f:
    # Создаем словарь со списком покупателей и их чеками
    customers = {}
    for index, line in enumerate(f, 1):
        purchases = {}
        line = line.rstrip()
        items = line.split(" ")
        for item in items:
            item = item.split(":")
            purchases[item[0]] = float(item[1])
        customers["Customer " + str(index)] = purchases
    # 1. Какова общая выручка магазина
    turnover = 0
    for receipt in customers.values():
        turnover += sum(receipt.values())
    print(f"Total turnover is {turnover}\n")
    # 2. Какова выручка магазина по каждому типу товаров
    shop_items = []
    for item in customers.values():
        for name in list(item.keys()):
            if name not in shop_items:
                shop_items.append(name)
    shop_items_turnover = {}
    for item in shop_items:
        shop_items_turnover[item] = 0
    for receipt in customers.values():
        for item, item_price in receipt.items():
            shop_items_turnover[item] += item_price
    for item, sales in shop_items_turnover.items():
        print(f"Total sales of {item} is {round(sales, 2)}")
    print("\n")
    # 3. Какой тип товара был продан на самую большую сумму
    max_sales_item = max(shop_items_turnover, key=shop_items_turnover.get)
    print(f"Our sales champion is {max_sales_item}\n")
    # 4. Сколько различных типов товаров было продано за день
    item_types = {}
    for item in shop_items:
        item_types[item] = 0
    for receipt in customers.values():
        for item in receipt:
            item_types[item] += 1
    for name, quantity in item_types.items():
        print(f"Today we sold {name} {quantity} time(s)")
