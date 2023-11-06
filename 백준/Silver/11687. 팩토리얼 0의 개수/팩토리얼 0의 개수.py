M = int(input())

N = 1
cnt = 1

while cnt < M:
    N += 1
    cnt += 1

    tmp = N
    while tmp > 0 and not tmp % 5:
        tmp //= 5
        cnt += 1

if cnt == M:
    print(N * 5)
else:
    print(-1)