N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

lamps = [0] * (M + 1)

for n in range(N):
    for i in range(1, lst[n][0] + 1):
        lamps[lst[n][i]] += 1

result = 0

for n in range(N):
    check = 0
    for i in range(1, lst[n][0] + 1):
        if lamps[lst[n][i]] - 1 == 0:
            check = 1
            break
    
    if not check:
        result = 1
        break

print(result)    