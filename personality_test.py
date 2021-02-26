def season(num, index):
    seasons_list = ["зима", "весна", "лето", "осень"]
    for i in seasons_list:
        if str(num).lower() == i:
            index += seasons_list.index(i)
            return True, index
        elif i == seasons_list[-1]:
            return False, 0


def days(num, index):
    days_list = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    for i in days_list:
        if str(num).lower() == i:
            index += days_list.index(i)
            return index


def test():  # личностный тест 2
    results = {1: "Вы любимчик жизни", 2: "Вы душа любой компании", 3: "У вас хорошее чувство юмора",
               4: "Вы обладаете незаурядным умом.", 5: "Вы утонченная натура", 6: "Вы прирожденный лидер"}
    index = 0
    answer = str(input("Какое ваше любимое время года?\n"))
    right, index = season(answer, index)
    if right:
        answer = str(input("Какой ваш любимый день недели?\n"))
        index = days(answer, index)
        if index > 6:
            print(results.get(index//2))
        else:
            print(results.get(index))
    else:
        print("Не сегодня")


test()
