N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

before = [0] * (K + 1)
now = [0] * (K + 1)

for n in range(N):
    nowv = lst[n]

    for k in range(K + 1):
        if k < nowv:
            now[k] = before[k]
        elif k == nowv:
            now[k] = before[k] + 1
        else:
            now[k] = before[k] + now[k - nowv]
    
    before = now[:]
    now = [0] * (K + 1)

print(before[-1])