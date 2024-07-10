N = int(input())
M = int(input())
lst = [[21e8] * (N + 1) for _ in range(N + 1)]
group = [n for n in range(N + 1)]
cnt = [1] * (N + 1)

for n in range(N + 1):
    lst[n][n] = 0

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        if group_a < group_b:
            group[group_b] = group_a
            cnt[group_a] += cnt[group_b]
            cnt[group_b] = 0
        else:
            group[group_a] = group_b
            cnt[group_b] += cnt[group_a]
            cnt[group_a] = 0

for _ in range(M):
    a, b = map(int, input().split())

    lst[a][b] = 1
    lst[b][a] = 1

    union(a, b)

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

leaders = []

for n in range(1, N + 1):
    if cnt[n]:
        min_v = 21e8
        leader = 0

        for i in range(1, N + 1):
            if find(i) == n:
                tmp = 0

                for j in range(1, N + 1):
                    if lst[i][j] != 21e8:
                        tmp = max(tmp, lst[i][j])

                if tmp < min_v:
                    min_v = tmp
                    leader = i
        
        leaders.append(leader)

print(len(leaders))

leaders.sort()

for leader in leaders:
    print(leader)