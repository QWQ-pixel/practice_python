def word():  # телеграммы
    letters = input()
    num_letters = len(letters) * 40
    print(num_letters // 100, "p.", num_letters % 100, "коп.")


word()
