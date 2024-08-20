K = int(input())

directions = [0] * 4
lst = []

for _ in range(6):
    d, num = map(int, input().split())
    directions[d - 1] += 1
    lst.append((d, num))

if directions[0] == directions[2] == 2:
    start = 2
elif directions[0] == directions[3] == 2:
    start = 3
elif directions[1] == directions[2] == 2:
    start = 4
else:
    start = 1

start_idx = 0
for i in range(6):
    if lst[i][0] == start:
        start_idx = i
        break

total = lst[start_idx][1] * lst[(start_idx - 1) % 6][1]
delete = lst[(start_idx + 2) % 6][1] * lst[(start_idx + 3) % 6][1]

print((total - delete) * K)