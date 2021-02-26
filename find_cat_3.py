def find():  # найди кота3
    string = ""
    all_strings = list()
    count = 0
    while string != "СТОП":
        string = input()
        all_strings.append(string)
        if string == "СТОП":
            all_strings.remove(string)
            for i in all_strings:
                if "кот" in i.lower():
                    if count == 0:
                        print(all_strings.index(i) + 1, end=" ")
                    count += 1
                if i == all_strings[-1] and count == 0:
                    print(-1, end=" ")
            print(count)


find()
