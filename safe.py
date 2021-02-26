def check_safe():  # надежность сейфа
    num = 0
    password = int(input())
    number_value = {}
    for i in set(str(password)):
        b = str(password).count(i, 0, len(str(password)))
        number_value[i] = b
    for key in number_value:
        if number_value.get(key) > num:
            num = number_value.get(key)
    if num == 2:
        print("В числе две одинаковые цифры")
    elif num == 3:
        print("В числе все цифры одинаковые")
    else:
        print("OK")


check_safe()
