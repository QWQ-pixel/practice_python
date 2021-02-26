def find():  # найди кота
    num = int(input())
    cat = False
    for i in range(1, num + 1):
        string = str(input())
        if "кот" in string.lower():
            cat = True
    if cat:
        print("МЯУ")
    else:
        print("НЕТ")


find()
