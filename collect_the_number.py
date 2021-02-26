def calc(number):  # собери число
    return number // 10 + number % 10


def collect():
    number = int(input())
    part_1 = number // 10
    part_2 = number % 100
    result = str(calc(part_2)) + str(calc(part_1))
    print(result)


collect()
