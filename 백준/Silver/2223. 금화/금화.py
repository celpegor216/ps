T, X, M = map(int, input().split())

minv = T

for _ in range(M):
    d, s = map(int, input().split())
    tmp = d // s
    if not d % s:
        tmp -= 1
    minv = min(minv, tmp)

if minv <= 0 or T == 0:
    print(0)
else:
    print((minv + (T - minv) // 2) * X)