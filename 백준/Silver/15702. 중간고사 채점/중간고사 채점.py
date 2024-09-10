N, M = map(int, input().split())
scores = [0] + list(map(int, input().split()))

maxv = 0
maxidx = 10 ** 6 + 1
for _ in range(M):
    lst = input().split()
    idx = int(lst[0])
    total = 0
    for n in range(1, N + 1):
        if lst[n] == 'O':
            total += scores[n]

    if total > maxv or (total == maxv and maxidx > idx):
        maxv = total
        maxidx = idx

print(maxidx, maxv)