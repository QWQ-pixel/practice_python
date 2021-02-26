def draw():  # пирамида
    height = int(input())
    symbol, count, space = "*", 1, height - 1
    for i in range(height):
        print(" " * space + symbol * count)
        count += 2
        space -= 1


draw()
