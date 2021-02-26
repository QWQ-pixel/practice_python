import math


def sequence():  # сумма ряда
    count = int(input())
    if count > 0:
        numbers = list()
        result = 0
        for i in range(count):
            numbers.append(int(input()))
        n = 0
        for num in numbers:
            result += num * math.pow(-1, n)
            n += 1
        print(int(result))


sequence()
