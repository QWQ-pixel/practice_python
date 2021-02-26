from random import randint


def AI_take(h_1, h_2):
    if h_1 > h_2:
        num = h_1 - h_2
        h_1 -= num
    elif h_2 > h_1:
        num = h_2 - h_1
        h_2 -= num
    else:
        num = randint(0, 1)
        if num:
            h_1 -= 1
        else:
            h_2 -= 1
    return h_1, h_2


def nim():  # ним 2
    heap_1, heap_2 = int(input("Первая куча\n")), int(input("Вторая куча\n"))
    while heap_1 != 0 or heap_2 != 0:
        heap_1, heap_2 = AI_take(heap_1, heap_2)
        if heap_1 == 0 and heap_2 == 0:
            print("ИИ выиграл!")
        else:
            print(heap_1, heap_2)
            heap = int(input("1 или 2?\n"))
            while heap < 0 or heap > 2:
                heap = int(input("Число должно быть в интервале от 1 до 2"))
            take = int(input())
            while take < 0:
                take = int(input())
            if heap == 1:
                while take > heap_1:
                    take = int(input("Ошибка ввода\n"))
                heap_1 -= take
            else:
                while take > heap_2:
                    take = int(input("Ошибка ввода\n"))
                heap_2 -= take
            if heap_1 == 0 and heap_2 == 0:
                print("Вы выиграли!")
                break
            else:
                print(heap_1, heap_2)


nim()
