def parrot():  # обратный попугай
    words = list()
    for i in range(3):
        word = input()
        words.append(word)
    words.reverse()
    for item in words:
        print(item)


parrot()
