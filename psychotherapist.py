def strings():  # сколько строк?
    string = ""
    nums_strings = 0
    while string != "Спасибо.":
        string = input()
        nums_strings += 1
    print(nums_strings)


strings()
