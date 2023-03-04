N, M, K = map(int, input().split())
lst = [0] + list(map(int, input().split()))
cuts = []
for m in range(M):
    x, y = sorted(map(int, input().split()))
    if x == 1 and y == N:
        cuts.append((y, x))
    else:
        cuts.append((x, y))
cuts.sort()

group = []

start = 1
for cut in cuts:
    temp = []
    for i in range(start, cut[0] + 1):
        temp.append(i)
    group.append(temp)
    start = cut[1]

if start != 1:
    for i in range(start, N + 1):
        group[0].append(i)

total = 0

if len(group) == 1:
    print('YES')
else:
    for g in group:
        temp = 50e10
        for item in g:
            if lst[item] < temp:
                temp = lst[item]
        total += temp

    if total <= K:
        print('YES')
    else:
        print('NO')