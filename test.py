def test():  # тест на делимость 
    for i in range(17):
        num = int(input())
        if i % num == 0:
            print("ДА")
        else:
            print("НЕТ")


test()
