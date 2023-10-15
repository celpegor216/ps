N = int(input())

num = [0]

for n in range(1, N):
    num[-1] += 1

    for i in range(len(num) - 1, 0, -1):
        if num[i] == num[i - 1]:
            if i == len(num) - 1:
                num[i] = 0
            else:
                num[i] = num[i + 1] + 1
            num[i - 1] += 1
        else:
            break
    
    if num[0] == 10:
        length = len(num)

        num = [x for x in range(length, -1, -1)]
    
    if num[0] > 9:
        num = [-1]
        break

for item in num:
    print(item, end='')