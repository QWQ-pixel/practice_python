def find():  # найди кота 4
    num = int(input())
    cat = 0
    for i in range(1, num+1):
        string = input()
        if 'кот' in string.lower():
            cat += 1
        if 'пес' in string.lower():
            cat -= 1
    if cat > 0:
        print("МЯУ")
    else:
        print("НЕТ")


find()
