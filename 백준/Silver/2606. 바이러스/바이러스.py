N = int(input())
lst = [[] for _ in range(N + 1)]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

start = now = 1
used = [0] * (N + 1)
used[start] = 1
stack = []

while 1:
    for nxt in lst[now]:
        if not used[nxt]:
            used[nxt] = 1
            stack.append(now)
            now = nxt
            break
    else:
        if stack:
            now = stack.pop()
        else:
            break

print(sum(used) - 1)    # 1번 제외