N = int(input())

cnt = 0
now = N

while 1:
    cnt += 1
    now = (now // 10 + now % 10) % 10 + (now % 10) * 10

    if now == N:
        break

print(cnt)