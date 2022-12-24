N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for n in range(1, N):
    for i in range(3):
        lst[n][i] += min([lst[n - 1][x] for x in range(3) if x != i])

print(min(lst[n]))