def division():  # таблица деления
    h = int(input())
    w = int(input())
    table = []
    for i in range(w):
        table.append([])
        for j in range(h):
            table[i].append(round((j + 1) / (i + 1), 7))
    for row in table:
        for x in row:
            print(x, end=" ")
        print()


division()
