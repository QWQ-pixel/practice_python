def conversation():  # короткая светская беседа
    answer = input("Здравствуйте! Как ваше настроение сегодня?\n")
    answer = answer.lower()
    if "хорош" in answer or "отличн" in answer or "прекрасн" in answer:
        print("Отлично, у меня тоже всё хорошо :)")
    elif "плох" in answer or "ужасн" in answer:
        print("Ничего, скоро всё наладится")
    elif "не" in answer or "?" in answer:
        print("Мне об этом ничего не известно.")
    else:
        print("Сегодня нет настроения вести светские беседы... Увидимся позже!)")


conversation()
