N = 36
lst = []
used = set()
result = 'Valid'

for _ in range(N):
    tmp = input()
    y, x = list(tmp)
    lst.append((ord(y) - ord('A') + 1, int(x)))
    if tmp not in used:
        used.add(tmp)
    else:
        result = 'Invalid'

lst.append(lst[0])

if result == 'Valid':
    for n in range(N):
        y, x = lst[n]
        flag = 0
        for dy, dx in ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)):
            ny, nx = y + dy, x + dx
            if (ny, nx) == lst[n + 1]:
                flag = 1
                break
        if not flag:
            result = 'Invalid'

print(result)