def monkey():  # цирк, цирк, цирк
    num = int(input())
    step = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        step += 1
    print(step)


monkey()
