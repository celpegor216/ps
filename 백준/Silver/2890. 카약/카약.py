N, M = map(int, input().split())
lst = [input() for _ in range(N)]
head_position = []

for n in range(N):
    for m in range(M - 1, 0, -1):
        if lst[n][m].isdigit():
            head_position.append((m, int(lst[n][m]) - 1))
            break

head_position.sort(key=lambda x: -x[0])
result = [0] * 9
rank = 1
for i in range(9):
    if i and head_position[i - 1][0] != head_position[i][0]:
        rank += 1
    result[head_position[i][1]] = rank

print(*result, sep='\n')