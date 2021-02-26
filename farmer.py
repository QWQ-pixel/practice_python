
# if __name__ == '__main__':
def task():  # начинающий фермер
    money = int(input())
    head = int(input())
    bull, cow, calf = min(head, money // 20), min(head, money // 10), min(head, money // 5)
    bull_pr, cow_pr, calf_pr = 20, 10, 5
    for i in range(1, bull + 1):
        for j in range(0, cow + 1):
            for k in range(0, calf + 1):
                if i * bull_pr + j * cow_pr + k * calf_pr == money and i + j + k == head:
                    print(i, j, k)


task()
