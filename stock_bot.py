def bot():  # биржевой бот
    buy, sell = 0, 0
    num_1, num_2, stock = int(input()), int(input()), False
    while num_2 != 0:
        if num_1 < num_2 and not stock:
            buy = num_2
            stock = True
        if num_1 > num_2 and stock:
            sell = num_2
        num_1 = num_2
        num_2 = int(input())
    print(buy, sell, sell-buy)


bot()
