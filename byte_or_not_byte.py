def table():  # бит или не бит
    table_pro = ["1 бит - минимальная единица количества информации.", "1 байт = 8 бит.", "1 Килобит = 1024 бита.",
                 "1 Килобайт = 1024 байта.", "1 Килобайт = "+str(8*1024)+" бит."]
    for i in table_pro:
        print(i)


table()
