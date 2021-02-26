def nim():  # ним 3 пасьянс
    heap_1, heap_2, heap_3 = int(input()), int(input()), int(input())
    while heap_1 != 0 or heap_2 != 0 or heap_3 != 0:
        heap = int(input())
        while heap < 0 or heap > 3:
            heap = int(input("Число должно быть положительное и не больше 3\n"))
        take = int(input())
        if heap == 1:
            heap_1 -= take
        elif heap == 2:
            heap_2 -= take
        else:
            heap_3 -= take
        print(heap_1, heap_2, heap_3)


nim()
