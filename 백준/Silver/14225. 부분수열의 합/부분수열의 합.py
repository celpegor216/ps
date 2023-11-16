N = int(input())
lst = list(map(int, input().split()))

s = set()

used = [0] * N
def dfs(now, total):
    s.add(total)

    for n in range(now + 1, N):
        if not used[n]:
            used[n] = 1
            dfs(n, total + lst[n])
            used[n] = 0

dfs(-1, 0)

result = 1

while 1:
    if result not in s:
        print(result)
        break

    result += 1