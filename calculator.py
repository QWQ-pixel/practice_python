def calc(a, b, operation):  # калькулятор
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b > 0:
            return a / b
        else:
            return 888888
    else:
        return 888888


def calculator():
    number_1 = float(input())
    number_2 = float(input())
    operation = input()
    print(calc(number_1, number_2, operation))


calculator()
