import math


def number():
    num = int(input())
    if num & (num - 1):
        print("NO")
    else:
        print(int(math.log(num, 2)))


number()
