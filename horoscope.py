def horoscope():  # гороскоп
    name = input()
    last_name = input()
    animal = input()
    zodiac_sign = input()
    print("Индивидуальный гороскоп для пользователя", name, last_name+":\n",
          "Кем вы были в прошлой жизни ", animal+".\n",
          "Ваш знак зодиака -", zodiac_sign+", поэтому вы - тонко чувствующая натура.")


horoscope()
