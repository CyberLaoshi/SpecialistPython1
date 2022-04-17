# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
import math


def lucky_ticket(ticket_number):
    # TODO: your code here

    # Вариант 1
    # sum_one = 0
    # sum_two = 0
    # if len(str(ticket_number)) % 2 == 0:
    #     middle_even = int(len(str(ticket_number)) / 2)
    #     for num_str in str(ticket_number)[:middle_even]:
    #         sum_one += int(num_str)
    #     for num_str in str(ticket_number)[middle_even:]:
    #         sum_two += int(num_str)
    # if len(str(ticket_number)) % 2 == 1:
    #     middle = math.ceil(len(str(ticket_number)) / 2) - 1
    #     for num_str in str(ticket_number)[:middle]:
    #         sum_one += int(num_str)
    #     for num_str in str(ticket_number)[middle+1:]:
    #         sum_two += int(num_str)
    # return sum_one == sum_two

    # Вариант 2
    sum_one = 0
    sum_two = 0
    digit_list = list(str(ticket_number))
    digit_list_int = [int(x) for x in digit_list]
    middle_index = len(digit_list) / 2
    middle_num = math.ceil(middle_index)
    if len(digit_list) <= 1:
        return False
    if middle_index % 1 == 0:
        sum_one = sum(digit_list_int[:middle_num])
        sum_two = sum(digit_list_int[middle_num:])
    if middle_index % 1 == .5:
        sum_one = sum(digit_list_int[:middle_num - 1])
        sum_two = sum(digit_list_int[middle_num:])
    return sum_one == sum_two


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(430751))
print(lucky_ticket(82321))
print(lucky_ticket(12325))

