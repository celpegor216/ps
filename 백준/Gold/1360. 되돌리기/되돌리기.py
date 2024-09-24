N = int(input())
lst = []

for _ in range(N):
    cmd, a, b = input().split()
    b = int(b)
    if cmd == 'type':
        lst.append([cmd, a, b, 1])
    else:
        lst.append([cmd, int(a), b, 1])

result = ''
for n in range(N - 1, -1, -1):
    if not lst[n][-1]:
        continue

    if lst[n][0] == 'type':
        result += lst[n][1]
    else:
        for m in range(n - 1, -1, -1):
            if lst[m][2] + lst[n][1] < lst[n][2]:
                break
            lst[m][-1] = 0

print(result[::-1])