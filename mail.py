def mail():  # регистрация почты
    login = input()
    address = input()
    if "@" not in login and "@" in address:
        print("OK")
    elif "@" in login:
        print("Некорректный логин")
    if "@" not in address:
        print("Некорректный адрес")


mail()
