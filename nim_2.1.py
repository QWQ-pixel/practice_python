def nim():  # ним 2 пасьянс
    heap_1, heap_2 = int(input()), int(input())
    while heap_1 != 0 or heap_2 != 0:
        heap = int(input())
        if heap < 0 or heap > 2:
            while heap != 1 or heap != 2:
                heap = int(input())
        take = int(input())
        if take < 0 or take > heap_1 if heap == 1 else heap_2:
            while take < 0:
                take = int(input())
        if heap == 1 and heap_1 > 0:
            heap_1 -= take
        if heap == 2 and heap_2 > 0:
            heap_2 -= take
        print(heap_1, heap_2)


nim()
