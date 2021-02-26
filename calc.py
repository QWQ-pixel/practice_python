import math


def calc(num_1,  operation, num_2):  # многоразовый калькулятор
    if operation == "/":
        if num_2 != 0:
            return round(num_1 / num_2, 2)
    elif operation == "*":
        return num_1 * num_2
    elif operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "%":
        return num_1 % num_2
    else:
        return "x"


def calculator():
    while True:
        num_1 = int(input())
        operation = input()
        if operation == "x":
            print(num_1)
            break
        elif operation == "!":
            if num_1 > 0:
                print(math.factorial(num_1))
        else:
            num_2 = int(input())
            print(calc(num_1, operation, num_2))


calculator()
