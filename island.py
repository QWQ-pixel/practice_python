def bad_luck():  # остров невезения
    day, month, year = int(input()), int(input()), int(input())
    c = year // 100
    year = (year - c) % 100
    print(int((day + ((13 * month - 1) // 5) + year + (year // 4 + c // 4 - 2 * c + 777)) % 7))


bad_luck()
