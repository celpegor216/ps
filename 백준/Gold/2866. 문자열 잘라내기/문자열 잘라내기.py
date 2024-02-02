N, M = map(int, input().split())
lst = [input() for _ in range(N)]

dic = dict()

result = N

for m in range(M):
    now = dic
    
    for n in range(N - 1, 0, -1):
        if now.get(lst[n][m], -1) != -1:
            result = min(result, n)
        else:
            now[lst[n][m]] = dict()
        now = now[lst[n][m]]

print(result - 1)