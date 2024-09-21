N, K = map(int, input().split())
lst = []

for _ in range(N):
    w, s, e = map(int, input().split())
    if w == 5:
        continue
    lst.append((w, s, e))

lst.sort()
N = len(lst)
result = 0

def dfs(level, start, noww, nowe):
    global result

    if level > K:
        return
    
    if level == K:
        result += 1
        return
    
    for n in range(start, N):
        w, s, e = lst[n]
        if noww == w and s <= nowe:
            continue

        dfs(level + (e - s + 1), n + 1, w, e)

dfs(0, 0, 0, 0)

print(result)