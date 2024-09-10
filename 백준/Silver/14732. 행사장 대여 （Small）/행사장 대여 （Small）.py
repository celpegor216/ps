N = int(input())
MAX = 500
used = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for _ in range(N):
    l, u, r, d = map(int, input().split())

    for i in range(u, d):
        for j in range(l, r):
            used[i][j] = 1

print(sum([sum(line) for line in used]))