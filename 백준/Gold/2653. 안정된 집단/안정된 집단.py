N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [0] * N
groups = []

flag = 0

for n in range(N):
    if used[n]:
        continue

    groups.append([])
    for m in range(N):
        if lst[n] == lst[m]:
            used[m] = 1
            groups[-1].append(m + 1)

    if len(groups[-1]) < 2:
        flag = 1
        break

if flag:
    print(0)
else:
    print(len(groups))
    for group in groups:
        print(*sorted(group))