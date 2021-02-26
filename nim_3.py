from random import randint


def AI_take(h_1, h_2, h_3):
    heaps = [h_1, h_2, h_3]
    heaps_s = heaps
    heaps_s.sort()
    max_1, max_2 = 0, 0
    for i in heaps:
        if i == heaps_s[-1]:
            max_1 = heaps[heaps.index(i)]
        if i == heaps_s[-2]:
            max_2 = heaps[heaps.index(i)]
    if max_1 == max_2:
        num = randint(1, 3)
        if num == h_1 and h_1 != 0:
            h_1 -= 1
        elif num == h_2 and h_2 != 0:
            h_2 -= 1
        elif h_3 != 0:
            h_3 -= 1
    else:
        take = max_1 - max_2
        if max_1 == h_1:
            h_1 -= take
        elif max_1 == h_2:
            h_2 -= take
        else:
            h_3 -= take
    return h_1, h_2, h_3


def nim():  # ним 3
    heap_1, heap_2, heap_3 = int(input("Первая куча\n")), int(input("Вторая куча\n")), int(input("Третья куча\n"))
    while heap_1 != 0 or heap_2 != 0 or heap_3 != 0:
        heap_1, heap_2, heap_3 = AI_take(heap_1, heap_2, heap_3)
        if heap_1 == 0 and heap_2 == 0 and heap_3 == 0:
            print("ИИ выиграл!")
        else:
            print(heap_1, heap_2, heap_3)
            heap = int(input("1, 2 или 3?\n"))
            while heap < 0 or heap > 3:
                heap = int(input("Число должно быть в интервале от 1 до 3"))
            take = int(input())
            if heap == 1:
                while take < 0 or take > heap_1:
                    take = int(input("Ошибка ввода\n"))
                heap_1 -= take
            elif heap == 2:
                while take < 0 or take > heap_2:
                    take = int(input("Ошибка ввода\n"))
                heap_2 -= take
            else:
                while take < 0 or take > heap_3:
                    take = int(input("Ошибка ввода\n"))
                heap_3 -= take
            if heap_1 == 0 and heap_2 == 0 and heap_3 == 0:
                print("Вы выиграли!")
                break
            else:
                print(heap_1, heap_2, heap_3)


nim()
