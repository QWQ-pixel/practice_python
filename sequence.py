def sequence():  # Сиракузская последовательность
    num = int(input())
    step = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            step += 1
        else:
            num *= 3
            num += 1
            step += 1
        if num == 1:
            print(step)


sequence()
