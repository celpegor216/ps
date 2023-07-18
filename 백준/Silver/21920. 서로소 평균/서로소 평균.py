N = int(input())
lst = list(map(int, input().split()))
X = int(input())

lst_X = []

num = 2
while X > 1:
    if not X % num:
        lst_X.append(num)

        while not X % num:
            X //= num
    num += 1

cnt = 0
total = 0
for item in lst:
    flag = 0

    for n in lst_X:
        if not item % n:
            flag = 1
            break

    if not flag:
        cnt += 1
        total += item

print(total / cnt)