def way_1():  # прямо
    way = int(
        input("Не долго думая, Вы прошли прямо. Перед Вами лишь один проход.\nВы пойдете по нему? да(1)/нет(2) Надо "
              "ввести число\n"))
    if way == 1:
        print("Вы пошли по единственному пути. Вы долго шли по сырой пещере, которая казалась бесконечной..."
              "Ваши запасы еды и воды заканчивалсь.\nВы зашли слишком далеко и смысла поворачивать назад не было.."
              "Поняв, к чему все идет Вы смирились..\nСпустя несколько дней Вы погибли")
    else:
        print("Вы подскользнулись и потеряли сознание. Придя в себя, Вы обнаружили, что вас спас какой-то старик."
              "В благодарность, Вы остались помогать ему по хозяйству.")


def way_2():  # налево
    way = int(input("Вы повернули налево. Еще одна развилка, пещера все больше начинает походить на лабиринт..."
                    "Вы видите два пути.\nКакой путь Вы выберите: 1, 2?\n"))
    if way == 1:
        print("Предчувствуя успех, Вы смело зашагали по первому пути!"
              "Вам встречались на пути разного рода ловушки: начиная от ямы с шипами и заканчивая огненными стрелами.\n"
              "Но Вы ловко обходили ловушку за ловушкой и в конце концов дошли до большой двери.\n"
              "Боясь словить очередную ловушку, Вы аккуратно открыли дверь\n"
              "За ней пряталось сокровище!\nВы выполнили квест! Поздравляю!")
    elif way == 2:
        print("Вы долги шли и в конце-концов вышли из пещеры! Перед вами открылся чудесный вид!\nСтолько буйных красок "
              "разом! Не дав глазам привыкнуть к яркому свету, Вы зашагали вперед к светлому будущему.\n"
              "Но Вы не заметили, что стояли на краю обрыва...")
    else:
        print("Вы прилегли отдохнуть, но как только Вы уснули, на Вас напали.\nОни связали Вас и продали работорговцу. "
              "Вы не хотели мириться с такой судьбой, поэтому прыгнули со скалы.\nНо,увы, не пережили падения")


def way_3():  # направо
    way = int(input("Вы повернули направо. Опять развилка! На этот раз пути всего лишь два.\n"
                    "Какой путь выберите: 1, 2?\n"))
    if way == 1:
        print("Вы решили выбрать первый путь.\n"
              "Вы наткнулись на человеческие останки...\nВы запаниковали и решили вернуться назад, "
              "но было поздно!")
        print("Вас съел подземный монстр...")
    elif way == 2:
        print("Вы покинули пещеру без сокровища и провалили квест!")
    else:
        print("Вы не смогли определиться куда пойдете, поэтому решили устроить привал")


def maze():  # лабиринт
    way = int(input("Вы-начинающий путешественник! Приняв очередной квест, Вы сразу же принимаетесь за дело!"
                    "Однако на деле все оказалось не так просто!\nВам необходимо пройти через лабиринт и забрать "
                    "награду.\n"
                    "Следуя карте, Вы нашли пещеру и зашли. Перед Вами развилка, три пути: прямо(1), налево(2), "
                    "направо(3)\n"
                    "Какой путь выберите: 1, 2, 3?: \n"))
    if way == 1:
        way_1()
    elif way == 2:
        way_2()
    elif way == 3:
        way_3()
    else:
        print("Вы взвесили все шансы на успех и решили отказаться от квеста")


maze()
