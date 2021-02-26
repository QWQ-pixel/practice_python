def yes_or_no():  # да или нет?!
    word_1 = input()
    word_2 = input()
    if word_1 == "да" or word_1 == "нет" and word_2 == "да" or word_2 == "нет":
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")


yes_or_no()
