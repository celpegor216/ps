N = int(input())
lst = list(map(int, input().split()))

result = []

used = [0] * N
def dfs(level, now):
    global result

    if level == N:
        check = [0] * N
        for i in range(N):
            for j in range(i):
                if now[j] > now[i]:
                    check[now[i]] += 1

        for i in range(N):
            if lst[i] != check[i]:
                break
        else:
            result = now
        return

    for n in range(N):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, now + [n])
            used[n] = 0

        if result:
            return

dfs(0, [])

for item in result:
    print(item + 1, end=' ')