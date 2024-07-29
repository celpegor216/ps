N = int(input())

used = [0] * 100
used[N] = 1
cnt = 1

while 1:
    N = (N % 10) * 10 + (N // 10 + N % 10) % 10

    if used[N]:
        break

    cnt += 1

print(cnt)