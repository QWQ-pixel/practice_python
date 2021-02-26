def draw():  # рисуем прямоугольник
    w = int(input())
    h = int(input())
    symbol = str(input())
    rectangle = []
    for i in range(w):
        rectangle.append([])
        for j in range(h):
            if i == 0 or i == w-1:
                rectangle[i].append(symbol)
            else:
                if j == 0 or j == h-1:
                    rectangle[i].append(symbol)
                else:
                    rectangle[i].append(" ")
    for row in rectangle:
        for x in row:
            print(x, end=" ")
        print()


draw()
