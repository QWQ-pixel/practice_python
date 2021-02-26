def find():  # найди кота 2
    string = ""
    all_strings = list()
    cat = False
    while string != "СТОП":
        string = input()
        if string == "СТОП":
            for i in all_strings:
                if "кот" in i.lower() and not cat:
                    print(all_strings.index(i)+1)
                if i == all_strings[-1] and cat:
                    print(-1)
        else:
            all_strings.append(string)


find()
