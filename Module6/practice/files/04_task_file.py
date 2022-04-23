# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# Работаем с исходным файлом в режиме чтения
file = 'dir/fruits.txt'
with open(file, encoding="utf-8") as f:
    # Удаляем символы переноса и пустые строки, сортируем список по первой букве
    fruits = []
    for line in f:
        line = line.rstrip()
        if len(line) > 0:
            fruits.append(line)
    fruits = sorted(fruits, reverse=False)
    # Создаем список из первых букв
    fruits_first_letter = []
    fruits_grouped = {}
    for fruit in fruits:
        if fruit[0] not in fruits_first_letter:
            fruits_first_letter.append(fruit[0])
    # Создаем словарь, где key - первая буква, value - пустой список.
    # В список будем добавлять слова с первой буквой из key
    for letter in fruits_first_letter:
        fruits_grouped[letter] = []
    for fruit in fruits:
        fruits_grouped[fruit[0]] += [fruit]
# Через итерацию создаем новые файлы, где key - первая буква сгрупированных слов, values - список этих слов.
# Вписываем в файл новые слова из списка. Учитываем, что последнему слову не нужен символ переноса.
for key, values in fruits_grouped.items():
    new_file = f"dir/fruits_sorted/fruits_{key}.txt"
    with open(new_file, "w", encoding="utf-8") as f:
        for value in values:
            f.write(value + "\n") if value != values[-1] else f.write(value)
