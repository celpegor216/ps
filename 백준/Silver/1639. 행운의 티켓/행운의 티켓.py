S = list(map(int, input()))
length = len(S)

for n in range(length // 2, 0, -1):
    flag = 0

    N = n * 2
    for j in range(length - N + 1):
        if sum(S[j:j + n]) == sum(S[j + n:j + N]):
            flag = 1
            break

    if flag:
        print(N)
        break
else:
    print(0)