def number():  # красивое число
    num = int(input())
    numbers = list(str(num))
    numbers.sort()
    minim = numbers.pop(0)
    maxim = numbers.pop(len(numbers)-1)
    result = numbers.pop()
    if (int(maxim) + int(minim)) / 2 == int(result):
        print("Вы ввели красивое число")
    else:
        print("Жаль, вы ввели обычное число")


number()
