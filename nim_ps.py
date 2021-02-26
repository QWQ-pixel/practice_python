from random import randint


def AI_take(num):
    if num > 3:
        if num % 3 != 0:
            take = 2 if (num - 2) % 3 != 0 else 1
        else:
            take = randint(1, 3)
    else:
        take = num
    num -= take
    return num, take


def person_takes(num):
    per_take = int(input())
    while per_take > 3 or per_take <= 0 or per_take > num:
        per_take = int(input("Число не должно превышать 3 или быть отрицательным\n"))
    num -= per_take
    return num, per_take


def nim():  # псевдоним
    num_rock = abs(int(input()))
    while num_rock > 0:
        num_rock, ai_take = AI_take(num_rock)
        if num_rock > 0:
            print("ИИ взял", ai_take, "Осталось в куче", num_rock)
        else:
            print("Выиграл ИИ!")
            break
        num_rock, per_take = person_takes(num_rock)
        if num_rock > 0:
            print("Вы взяли", per_take, "Осталось в куче", num_rock)
        else:
            print("Вы выиграли!")


nim()
