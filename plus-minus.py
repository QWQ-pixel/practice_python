def plus_minus():  # плюс-минус
    number = float(input())
    if number < 0:
        print("-")
    elif number > 0:
        print("+")
    else:
        print("0")


plus_minus()
