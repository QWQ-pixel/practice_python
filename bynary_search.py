def search():  # бинарная угадайка
    left, right, op, middle, attempt, num = 1, 10, "", 0, 10, 0
    while attempt > 0:
        middle = (left + right) // 2
        print(middle)
        op = input()
        if op == "<":
            left = middle + 1
            right += 1
        elif op == ">":
            right = middle - 1
            left -= 1
        elif op == "=":
            break
        attempt -= 1
        if attempt == 0:
            print("Компьютер не угадал :(")


search()
