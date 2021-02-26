def password():  # password123456
    pass_1 = input()
    pass_2 = input()
    if len(pass_1) < 8:
        print("Короткий!")
    elif "123" in pass_1:
        print("Простой!")
    elif pass_1 != pass_2:
        print("Различаются.")
    else:
        print("OK")


password()
