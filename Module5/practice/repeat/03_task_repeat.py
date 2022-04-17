# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    num_reverse = ""
    num_string = str(number)
    for index in range(len(num_string)):
        num_reverse += num_string[-1]
        num_string = num_string[:-1]
    return number == int(num_reverse)

def count_palindrome(a,b):
    count = 0
    # list = []
    for i in range(a,b+1):
        if palindrome(i):
            # list.append(i)
            count += 1
    return count

range_ab=(10, 1000)
print(count_palindrome(*range_ab))
