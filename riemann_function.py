import math


def function():  # дзета-функция римана
    num = int(input())
    total = 0
    numbers = range(1, num+1)
    for i in numbers:
        total += 1 / math.pow(i, 2)
    print(math.pow(round(math.pi, 20), 2) / total)


function()
