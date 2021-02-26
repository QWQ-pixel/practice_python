def find():  # найди кота 2(break)
    string = ""
    all_strings = list()
    while string != "СТОП":
        string = input()
        all_strings.append(string)
        if "кот" in string.lower():
            print(all_strings.index(string)+1)
            break
        elif string == "СТОП":
            all_strings.remove(string)
            for i in all_strings:
                if "кот" in i.lower():
                    print(all_strings.index(i)+1)
                    break
                if i == all_strings[-1]:
                    print(-1)


find()
