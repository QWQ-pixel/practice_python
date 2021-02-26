def count():  # обратный отсчет
    sec = int(input())
    if sec < 0:
        print("Пуск")
    else:
        for i in range(sec, -1, -1):
            print("Осталось секунд:", i)
            if i == 0:
                print("Пуск")


count()
