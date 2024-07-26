M, N = map(int, input().split())

horizontal = [0]
vertical = [0]

K = int(input())
for _ in range(K):
    t, i = map(int, input().split())
    if t == 0:
        vertical.append(i)
    else:
        horizontal.append(i)

horizontal.append(M)
vertical.append(N)

horizontal.sort()
vertical.sort()

maxh = maxv = 0

for i in range(len(horizontal) - 1):
    maxh = max(maxh, horizontal[i + 1] - horizontal[i])
for i in range(len(vertical) - 1):
    maxv = max(maxv, vertical[i + 1] - vertical[i])

print(maxh * maxv)