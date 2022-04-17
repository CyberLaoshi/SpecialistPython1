# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    # Вариант 1
    # num_reverse = 0
    # num_modified = number
    # while num_modified != 0:
    #     num_reverse = num_reverse * 10 + num_modified % 10
    #     num_modified = num_modified // 10
    # return number == num_reverse

    # Вариант 2
    num_reverse = ""
    num_string = str(number)
    for index in range(len(num_string)):
        num_reverse += num_string[-1]
        num_string = num_string[:-1]
    return number == int(num_reverse)

print(palindrome(12321))
