def fight():  # шварцнеггер против годзиллы
    a, d = 0, 1
    for i in range(int(input())):
        num_1, num_2 = int(input()), int(input())
        a = a * num_2 + num_1 * d
        d *= num_2
    x, y = a, d
    while y > 0:
        x, y = y, x % y
    print(a // x, '/', d // x, sep='')


fight()
