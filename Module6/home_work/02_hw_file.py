# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r", encoding="utf-8") as f:
    # Вариант 1
    # total = 0
    # num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # numbers_in_line = []
    #
    # for line in f:
    #     line = line.rstrip()
    #     is_number = False
    #     for num in num_list:
    #         if str(num) in line:
    #             append_or_not = True
    #     if is_number:
    #         numbers_in_line.append(line)
    # numbers_in_line = [int(x) for x in numbers_in_line]
    # # print(numbers_in_line)
    # print(sum(numbers_in_line))

    # Вариант 2.Число и текст перемешаны в строке
    # 1. Подсчет общего числа строк.
    total_line_count = 0
    for line in f:
        total_line_count += 1
    # 1.1 Проверка на наличие строк
    if total_line_count == 0:
        print("Empty file")
    else:
        f.seek(0)
        # 2. Поиск строк с цифрами
        num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        numbers_in_text = []
        current_line = 0
        for line in f:
            # 2.1 Подсчет текущей строки
            current_line += 1
            numbers_in_line = []
            number_seperate = ""
            for letter in line:
                # 2.2 Перебор символов в строке для поиска чисел
                if letter in num_list:
                    number_seperate += letter
                # 2.3 Если за совокупностью чисел идет текст или конец строки, сохраняем число
                else:
                    numbers_in_line.append(number_seperate)
                    number_seperate = ""
            # 2.4 Для последней строки (в т.ч. в однострочном документе) стоит учитывать отсутствие символа \n.
            if total_line_count == current_line:
                numbers_in_line.append(number_seperate)
            # 2.5 Перед переходом к новой строке проходимся по имеющимся числам и добавляем их в общий список чисел
            for num in numbers_in_line:
                if num:
                    numbers_in_text.append(num)
        numbers_in_text = [int(x) for x in numbers_in_text]
        print(numbers_in_text)
        print(sum(numbers_in_text))
