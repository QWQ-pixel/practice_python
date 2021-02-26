def search():  # ищем клад 2
    x, y = 0, 0  # наши координаты
    t_x, t_y = int(input()), int(input())  # координаты сокровища
    step, find = "", False
    num_steps = 0
    step = input()
    while step != "стоп":
        num_steps += 1
        steps = int(input())
        if step == "север":
            y += steps
        elif step == "запад":
            x -= steps
        elif step == "юг":
            y -= steps
        elif step == "восток":
            x += steps
        if x == t_x and y == t_y and not find:
            print(num_steps)
        step = input()


search()
