N = 9
lst = [list(map(int, input().split())) for _ in range(N)]

result_idx = []
result_v = -1

for i in range(N):
    for j in range(N):
        if result_v < lst[i][j]:
            result_v = lst[i][j]
            result_idx = [i + 1, j + 1]

print(result_v)
print(*result_idx)