def school():  # школа танцев
    step = ["раз", "два", "три", "четыре"]
    num = int(input())
    right = 0
    while num > 0:
        for i in step:
            string = input()
            if string != i:
                print("Правильных отсчётов было", right, ", но теперь вы ошиблись.")
                right = 0
                num -= 1
                if num == 0:
                    print("На сегодня хватит.")
                    break
                break
            else:
                right += 1


school()
