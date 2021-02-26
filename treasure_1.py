def search():  # ищем клад 1
    opposite = {"север": "юг", "юг": "север", "запад": "восток", "восток": "запад"}
    side = ["север", "запад", "юг", "восток"]
    x, y = 0, 0  # наши координаты
    t_x, t_y = int(input()), int(input())  # координаты сокровища
    step, go, find = "", "север", False
    num_steps = 0
    step = input()
    while step != "стоп":
        num_steps += 1
        if step == "вперед":
            steps = int(input())
            if go == "север":
                y += steps
            elif go == "запад":
                x -= steps
            elif go == "юг":
                y -= steps
            elif go == "восток":
                x += steps
        elif step == "налево":
            for i in side:
                if go == i:
                    go = side[(side.index(i) - 1)]
                    break
        elif step == "направо":
            for i in side:
                if go == i:
                    go = side[(side.index(i) + 1) if side.index(i) < len(side)-1 else 0]
                    break
        elif step == "разворот":  # назад
            for i in opposite.keys():
                if go == i:
                    go = opposite.get(i)
                    break
        if x == t_x and y == t_y and not find:
            print(num_steps, go)
            find = True
        step = input()


search()
