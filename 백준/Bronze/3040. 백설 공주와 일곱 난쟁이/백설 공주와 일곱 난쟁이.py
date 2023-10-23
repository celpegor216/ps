lst = [int(input()) for _ in range(9)]

total = sum(lst)

flag = 0
for i in range(9):
    if flag:
        break
    for j in range(i + 1, 9):
        if total - lst[i] - lst[j] == 100:
            flag = 1

            for n in range(9):
                if n not in (i, j):
                    print(lst[n])