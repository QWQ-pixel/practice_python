import math


def average_number():  # среднее
    temperature = 0
    temperatures = []
    while temperature > -300:
        temperature = float(input())
        if temperature < -300:
            print(round(math.fsum(temperatures) / len(temperatures), 2))
        else:
            temperatures.append(temperature)


average_number()
