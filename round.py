def round_num():  # круглые
    number = int(input())
    while True:
        if number % 10 != 0:
            break
        number = int(input())


round_num()
