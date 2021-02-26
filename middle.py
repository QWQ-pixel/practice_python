import math


def middle():  # умнее среднего
    iq_people = []
    num = int(input())
    for i in range(num):
        iq = int(input())
        iq_people.append(iq)
        if iq > math.fsum(iq_people) / len(iq_people):
            print(">")
        elif iq < math.fsum(iq_people) / len(iq_people):
            print("<")
        else:
            print(0)


middle()
