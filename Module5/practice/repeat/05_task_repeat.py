# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination(num_items, items_on_page):
    return num_items % items_on_page

test = pagination(16, 3)
print(test)
