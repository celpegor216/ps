N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])

max_h = max([x[1] for x in lst])
max_idx = []

for i in range(N):
    if lst[i][1] == max_h:
        max_idx.append(i)

result = 0
temp_idx = 0
for i in range(1, max_idx[0] + 1):
    if lst[temp_idx][1] < lst[i][1]:
        result += (lst[i][0] - lst[temp_idx][0]) * lst[temp_idx][1]
        temp_idx = i

result += max_h if len(max_idx) == 1 else max_h * (lst[max_idx[-1]][0] - lst[max_idx[0]][0] + 1)

temp_idx = N - 1
for i in range(N - 2, -max_idx[-1] - 1, -1):
    if lst[temp_idx][1] < lst[i][1]:
        result += (lst[temp_idx][0] - lst[i][0]) * lst[temp_idx][1]
        temp_idx = i

print(result)
