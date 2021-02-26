def find():  # найди кота(break)
    num = int(input())
    for i in range(1, num + 1):
        string = str(input())
        if "кот" in string.lower():
            print("МЯУ")
            break
        if i == num:
            print("НЕТ")


find()
